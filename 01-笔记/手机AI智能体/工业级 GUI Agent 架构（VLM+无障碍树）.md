# 工业级 GUI Agent 架构（VLM + 无障碍树）

> 将端侧 VLM（视觉语言大模型）与 Android 结构化节点树（AccessibilityNodeInfo）结合，是目前打造工业级 GUI Agent 最具可行性的架构。

纯视觉 Agent（单靠 VLM 看图找坐标）：延迟高、坐标定位不准、功耗大。
纯无障碍 Agent（单靠 DOM 树）：遇到 WebView、Flutter 渲染、自定义 Canvas 或缺失语义标签时瞬间「致盲」。

**融合逻辑**：用无障碍节点树提供「毫秒级定位与精确点击」，用端侧 VLM 提供「语义理解与视觉补位」。

## 系统整体 Pipeline（五阶段闭环）

```
                 工业级 GUI Agent 底层流水线
  [1. 双通道感知] → [2. 节点清洗与 SoM] → [3. 端侧 VLM 推理]
   • SurfaceControl     • 树结构过滤/平铺        • SoM 图 + 节点文本 Prompt
   • Accessibility      • 绘制 ID 标注框         • 输出 JSON Action Schema
                                                        │
  [5. 闭环断言自愈] ← [4. 分层精准执行] ←──────────┘
   • 状态变化校验         • 优先 A11y 节点 Action
   • 降级重试机制         • 备选 Gesture 坐标点击
```

## 架构核心实现五步

### 1. 双通道并发感知层（Dual-Channel Perception）
唤醒时刻同时触发两个并发采集：
- **视觉通道**：`SurfaceControl.captureDisplay()`（厂商内嵌权限）或 MediaProjection 直接获高清 Bitmap。
- **结构通道**：`AccessibilityService.getRootInActiveWindow()` 递归拉取整棵 `AccessibilityNodeInfo` 树。

```java
CompletableFuture screenshotFuture = captureScreenAsync();
CompletableFuture nodeTreeFuture = captureA11yTreeAsync();
CompletableFuture.allOf(screenshotFuture, nodeTreeFuture).join();
```

### 2. 节点树清洗与 Set-of-Marks（SoM）融合
- **树剪枝与过滤**：剔除 `isVisibleToUser == false`、尺寸 0 或后台遮挡节点，提取 `boundsInScreen`（Rect）、`text`、`contentDescription`、`className`、`isClickable`。
- **SoM 视觉标注**：在截屏对应坐标上用 Canvas 绘制递增数字编号框（[1] [2] [3]）。
- **视觉补全兜底**：对 Flutter / Canvas / WebView 等无障碍节点为空区域，用轻量 CV（轮廓检测 / YOLO Icon 检测）识别孤立图标，生成虚构节点加入列表。
- **产物**：「带数字编号框的标注图」+「数字 ID → 控件属性及 Rect 坐标映射表（JSON）」。

### 3. 端侧 VLM 结构化推理 Engine
SoM 标注图 + 精简节点列表 Prompt，输入端侧轻量 VLM（Qwen2-VL-2B、MiniCPM-V 等量化模型，运行在 Qualcomm NPU / Executorch / QNN）。强制模型经 JSON Schema（Structured Outputs）返回严格格式决策：

```json
{
  "thought": "用户想找杭州酒店，输入框[4]为空，需先输入文本",
  "action_type": "INPUT",
  "target_id": 4,
  "input_text": "杭州",
  "next_expectation": "输入框显示杭州，并弹出联想下拉菜单"
}
```

### 4. 分层精准执行引擎（Grounding & Execution）
收到 `target_id` 经映射表找节点，两级降级：
- **L1 优先（Node API 驱动）**：对应真实 `AccessibilityNodeInfo` 且 `isClickable == true`，直接 `nodeInfo.performAction(ACTION_CLICK)`。零动画等待、最快、免疫分辨率缩放。
- **L2 降级（Gesture 坐标模拟）**：虚构节点或 `performAction` 失败时，算 `Rect.exactCenter()` 得绝对坐标，用 `AccessibilityService.dispatchGesture()` 模拟触控。

```java
Path path = new Path();
path.moveTo(centerX, centerY);
GestureDescription.StrokeDescription stroke =
    new GestureDescription.StrokeDescription(path, 0, 50);
dispatchGesture(new GestureDescription.Builder().addStroke(stroke).build(), null, null);
```

### 5. 状态迁移校验与自愈闭环（Self-Healing Loop）
执行后不盲目进下一步，做 UI 沉降防抖（Debounce ~300ms），重捕屏幕做 State Diff 校验：
- **断言成功**：新界面 DOM Hash / 视觉特征符合 `next_expectation`，推进下一子任务。
- **断言失败**：触发自愈。L1 无效则下次切 L2 坐标强制点击；连续 2 次失败则向云端上报 Trace 并引导用户接管。

## 工业级落地必须解决的 3 个关键技术瓶颈

### 1. 动态布局与防遮挡（Z-Order & Overlay）
弹窗、悬浮窗、Toast 常遮挡底层 View。A11y 树按 Hierarchy 排序，易点到被遮挡的不可见按钮。
**解法**：清洗节点树时引入 Z-Index 算子，依据 `windowId` 及节点在 ViewTree 绘图深度，剔除被顶层 Modal 遮挡节点。

### 2. 敏感界面与隐私保护（FLAG_SECURE）
支付、密码、银行 App 触发 `WindowManager.LayoutParams.FLAG_SECURE`，`captureDisplay()` 截出纯黑屏。
**解法**：感知黑屏或 `isPassword == true` 节点时，自动把 VLM 切「纯 DOM 语义推理模式」，禁截图传模型，只靠 A11y 节点 `className` 与上下文属性生成动作指令，保障隐私且流程不断裂。

### 3. 端侧推理耗时与内存开销（Latency & Memory）
2B/3B VLM 在手机 NPU 上一次 Prefill + Decode 需 300ms~800ms，内存约 1.5GB~2GB。
**解法**：Speculative Decoding（推测解码）+ 缓存复用。前后两帧 A11y 树拓扑变化 <5%（界面基本没变）时，不调昂贵 VLM，直接复用上一次决策路径，将连续操作平均延迟压至 100ms 内。

## 结论
「A11y 骨架提供精确度与速度 + VLM 肌肉提供泛化与视觉理解」的双引擎架构，是让手机 AI Agent 从「实验室 Demo」走向「日常可用级」的最优技术路线。

## 深化补充（2026-08）

本文已把技术管线写透，这里只补三件本文没覆盖、但决定这套架构值不值得投的事。

### 一句话心智模型：Harness > 模型
OSWorld 榜单团队的归因值得记死：能力**不主要来自底座模型的「智力」，而来自整套工程调度系统（Harness）的可靠性**——「相当于汽车发动机与方向盘、制动系统的协同」。同一底座换一套调度/重试/校验工程，分数可以差出几十个点。

→ 这正好给本文第 5 节（状态迁移校验与自愈闭环）定了性：**那一节不是收尾工程，那是整套架构里 ROI 最高的一节**。VLM 换代随时可以做，Harness 是护城河。

### 能力天花板：这条曲线已经不是瓶颈了

| 时间 | OSWorld 最优 | 备注 |
|---|---|---|
| 2024（基准设立） | ~12% | GPT-4o / Claude |
| 2025 年底 | 72.6% | 首次超过人类平均 |
| 2026-05 | 83.6% | — |
| 2026-07-31 | **90.2%** | 强项含**跨应用协同**、系统底层操作类满分 |

⚠️ **待核实**：以上为媒体报道数据，OSWorld 官方榜单页与提交记录**尚未二次核验**，引用需标来源性质。

**含义**：本文开头列的「纯视觉 Agent 延迟高、定位不准」这些能力问题正在被解决。**矛盾已经转移到准入与风控**——豆包手机二代直接放弃 GUI 视觉模拟路线、改用 MCP 与 App 官方接口直连，公开动机就是规避风控封禁。

### 三条通道的定位（本文架构在整盘棋里的位置）

| 维度 | ① 官方 Intent/Function | ② MCP 连接器 | ③ **本文的 GUI 模拟** |
|---|---|---|---|
| 可靠性 | 最高（结构化返回） | 高 | 受 UI 改版影响 |
| 覆盖面 | 仅已适配 App | 已接协议方 | **理论全覆盖** |
| 准入成本 | 需 App 适配/授权 | 需协议对接 | **无需对方同意** |
| 风控风险 | 无 | 低 | **高（可被封禁）** |
| 可审计 | 强 | 强 | **弱** |

→ **本文这套架构的正确用法**：只在「无官方通道 + 任务低风险 + 可容忍失效」三条同时成立时启用。**不要用它做写操作和支付**——技术上点得动，责任链上说不清。同时用它的真实调用数据反推「该优先游说哪些 App 开放官方通道」。

### 待解问题
- [ ] 第 3 节的端侧 VLM 选型，我一直只看「识别准不准」。但 BFCL v4 有一栏叫 **Hallucination（无合适工具时正确拒绝调用）**——GUI Agent 有没有等价指标？「屏幕上根本没有这个按钮时，模型会不会硬点一个」，这是不是比准确率更该测？（见 [[Function Calling 端侧工具调用]]）
- [ ] 第 5 节的「云端自愈与轨迹共享」把用户屏幕轨迹上云复用。**这在 2026 的隐私合规下还做得成吗**？EU AI Act Article 10（数据治理）2026-08-02 起适用高风险条款——轨迹算不算需要溯源分级的数据？
- [ ] Harness 既然比模型重要，那**这套 Harness 的能力应该沉淀在哪一层**——ROM 系统服务、独立 App、还是可下发的策略包？三者的迭代速度和权限边界完全不同。

## 关联
- 破局策略见 [[安卓厂商意图识别破局策略]]
- 国内落地阻力见 [[国内安卓厂商做 App Intent 的阻力]]
- 基础概念见 [[App Intent 的核心作用]]
- 通道该不该选 GUI → [[端侧执行通道 GUI 与 MCP 路线之争]] ｜ PM 拍板 → [[GUI Agent vs 原生 API 产品决策树]]
- 能力天花板评测 → [[OSWorld 计算机操作基准]] ｜ 端侧端到端 → [[Local Agent Bench 端侧智能体基准]]
- 官方兜底通道（UI Automation）→ [[Android AppFunctions 设备侧意图 2026]]
- 屏幕内容被注入的风险 → [[XPIA 跨提示注入]]

#标签/GUIAgent #标签/端侧AI #标签/VLM
