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

## 关联
- 破局策略见 [[安卓厂商意图识别破局策略]]
- 国内落地阻力见 [[国内安卓厂商做 App Intent 的阻力]]
- 基础概念见 [[App Intent 的核心作用]]

#标签/GUIAgent #标签/端侧AI #标签/VLM
