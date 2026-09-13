---
automation: AppIntent 每日情报（自动化 09:00 版，实际按 7 日滚动窗口运行）
last_run: 2026-09-13
window: 2026-09-06 → 2026-09-13
---

# 执行摘要（2026-09-13）

## 本轮产出（窗口 2026-09-06 → 09-13，7 日滚动）
- **四平台官方框架层 API 无净新增**：iOS 27 RC build 24A435（09-09）= Beta 5 收尾、无新 App Intents API；AppFunctions 守 alpha11（无 alpha12）；HarmonyOS 7 框架同 HDC2026 / 09-07 消费版；Windows Copilot Actions/Agent Workspace/ODR/Agent Launchers 四支柱无变化。
- **真增量①：BFCL v4 官方榜单上线（★7/10）** → 补 [[Function Calling 端侧工具调用]]：Berkeley Gorilla 维护、DataLearner 镜像 2026-09-07 更新，SOTA **MiniCPM5-2B（OpenBMB）66.60**（2.5B 免费商用，端侧级小模型首登官方 v4 榜首）；收口连续多轮「Berkeley 官方榜」待办，端侧分数升「可复核」；某中文综述「88.5%」标待补（疑单轮子集/厂商自报）。
- **真增量②：Windows IFA 2026 Microsoft Execution Containers（★7/10）** → 补 [[Windows Copilot Actions 与 Agent Workspace 2026]] + [[Agent Workspace 隔离执行]]：Agent 隔离升为内建沙箱容器，强制企业策略 + 全量日志；四平台最明确 OS 内建容器隔离原语。Project Zenith/RTX Spark 属硬件定位不计入。
- **真增量③：HarmonyOS 7 确认 API 26（★6/10）** → 补 [[HarmonyOS Intents Kit 与 ArkAF 2026]]：关闭「26 vs 23」冲突待办；新增安全相机2.0 数字内容溯源 + 数字身份 DID（provenance-at-source），但意图 Registry 层来源轴仍空白（不推翻来源轴结论）。
- **真增量④：iOS 27 RC + GA 09-14（★6/10）** → 索引 [[AppIntent 每日情报 2026-09-13]]，触发 per-intent 路由 API 核查（待办延续）。
- **落库**：A 索引 [[AppIntent 每日情报 2026-09-13]]、D 速览 [[AppIntent 每日情报速览 2026-09-13]]、B 既有增补 3（Function Calling/Windows/HarmonyOS）+ 关联增补 1（Agent Workspace）、看板「本次新增（2026-09-13）」已登记。**0 新建 B 节点**。

## 诚实标注 / 待办
- MiniCPM5-2B 66.60 为聚合镜像（DataLearnerAI）呈现、非逐字官方博客；Apple FM 61.7% / Needle 2 42.6% / FunctionGemma 27–46% 待用官方榜逐项复核。
- Execution Containers 是否复用 Agent Workspace 容器、opt-in 管控、与 ODR 关系待 Microsoft 官方文档。
- 鸿蒙 安全相机2.0/DID 字段、是否接意图回路待官方文档。
- **【最高优先·明日触发】9-14 iOS 27 GA 后核查 per-intent 路由/来源声明 API**（重评来源轴结论）。

# 执行摘要（2026-09-12）

## 本轮产出（窗口 2026-09-04 → 09-12，补跑 9 天空窗）
- **四平台官方框架层 API 无净新增**：iOS 27 守 Beta 5 已录 schema；Android AppFunctions 仍 `1.0.0-alpha11`（无 alpha12）；HarmonyOS 7 框架同 HDC2026；Windows agentic security 四支柱一致。
- **真增量①：HarmonyOS 7（9-7 发布后）可信与安全实测** → 补 [[HarmonyOS Intents Kit 与 ArkAF 2026]]：信通院增强级端云协同 AI 安全认证（行业首个）、携手支付宝欺诈损失率 -35.8%/盗用拦截率 +42.3%、高频流畅度 +22%、应用跳转 +25%。来源为快科技/百度百科媒体口径，标待官方核验。
- **真增量②：跨平台 A2UI 落地（新 B 节点）** → 高德 AGenUI 明确基于 Google A2UI 协议，C++ 引擎把界面意图渲染为鸿蒙原生组件。新建 [[A2UI 生成式UI协议(Google)与鸿蒙落地 2026]]。
- **真增量③：Needle 2 跨模型 BFCL v4 对照 + 架构消融** → 补 [[Function Calling 端侧工具调用]]（单轮 Apple FM 61.7% / LFM2.5-230M 60.8% / FunctionGemma 46.1% / Needle 2 42.6%；Seal-Tools 域外 Needle 2 28.7% 居首）+ [[端侧 Router 置信度门控与工具可达性收缩 2026]]（attention-only 消融 0.47→0.006 nats、byte-level grammar 跳过 98% 词表、well-formed 93.4% 跨模型同档）。aibacon 第三方拆解，待官方榜复核。
- **真增量④：Windows 具体 build 号与交互** → 补 [[Windows Copilot Actions 与 Agent Workspace 2026]]：build 26200.8313（任务栏 Agent）/ 26220.7262（Agent Workspace）、Settings「Agents」面板、「@」调 Agent、悬停监控。第三方 tracker，非官方 blog。
- **落库**：A 索引 [[AppIntent 每日情报 2026-09-12]]、D 速览 [[AppIntent 每日情报速览 2026-09-12]]、B 新 1（A2UI）+ B 既有增补 4、看板「本次新增（2026-09-12）」已登记。

## 诚实标注 / 待办
- 信通院认证编号、支付宝联合测试方法论、AGenUI 协议字段遵循度、Windows build 号均媒体/厂商口径，待官方文档核验。
- Needle 2（42.6%）/ Apple FM（61.7%）跨模型对照仍第三方引述，待 Berkeley 官方 BFCL v4 榜复核。
- HarmonyOS 7 消费版真实 API level（26 vs 23 冲突）仍待官方文档回填。
- 9-14 iOS 27 GA 后核查是否新增 per-intent 路由/来源声明 API（将重评 [[四平台意图 Registry 来源轴与权限模型对比 2026]] 来源轴结论）。
- 延续：Watch OS 26 / NowSecure / AgentAntibody / Chrome Origin Sets 官方 URL 复核。

# 执行摘要（2026-09-03）

## 本轮产出（窗口 2026-08-27 → 09-03）
- **四平台官方框架层 API 无净新增**：iOS 27 RC 沿用 Beta 5 已录 `@AppIntent(schema:)`；Android AppFunctions 守 `1.0.0-alpha11`（官方 Release Notes 当前最新，无 alpha12）；HarmonyOS 7 框架同 HDC2026；Windows agentic security 四支柱一致。
- **真增量①：三平台消费级 GA 日期锁定**（OS PM 核心信号）
  - HarmonyOS 7 消费版 **2026-09-07** 随 Mate XT 2 铺开（ArkAF 2.0「意图即服务」入消费者）→ 新建/补 [[HarmonyOS Intents Kit 与 ArkAF 2026]]。
  - Windows 11 26H2 **9 月下旬~10 月初**（enablement package）：Ask Copilot 搜索层意图入口 + Sysmon 内置 → 补 [[Windows Copilot Actions 与 Agent Workspace 2026]]。
  - iOS 27 **2026-09-14** GA（框架不变）。
  - 含义：四平台 agentic 框架同步进入「发布前最后冲刺」；HarmonyOS 是首个把意图即服务做成消费者默认可用并锁 GA 的平台。
- **真增量②：Luxand LLM SDK BFCL v4 端侧 Agentic Score 快照**（第三方 SDK 自测，非官方榜）：Qwen3.6-35B-A3B 73.4% / Gemma4-26B-A4B 71.8% / Qwen3.5-4B 67.0% / LFM2.5-8B-A1B 62.3% / Gemma4-E2B 51.1% → 补 [[Function Calling 端侧工具调用]]，待 Berkeley 官方榜复核。
- **落库**：A 索引 [[AppIntent 每日情报 2026-09-03]]、D 速览 [[AppIntent 每日情报速览 2026-09-03]]、B 既有增补 3（HarmonyOS/Windows/Function Calling）、看板末尾「本次新增（2026-09-03）」已登记。

## 诚实标注 / 待办
- Luxand 为厂商 SDK 自测、量化/硬件/模板与官方榜不同，「Agentic Score」非 Berkeley 总分；须三问 + 标版本号。
- 9-7 后回填 HarmonyOS 7 消费版真实 API level（26 vs 23 冲突仍待官方）。
- 9-14 iOS 27 GA 后核查是否新增 per-intent 路由/来源声明 API（将重评来源轴结论）。
- 延续：Watch OS 26 是否 Trust Insights 类、NowSecure/AgentAntibody 独立核验、Chrome Origin Sets 官方 URL 逐字复核、Berkeley 官方 BFCL v4 博客原文。

# 执行摘要（2026-09-01）

## 本轮产出
- **净新增 OS 框架 API（唯一）**：Android AppFunctions Jetpack **`1.0.0-alpha11`（2026-08-26 官方 Release Notes）**
  - `@AppFunctionSignature`（experimental）→ 支持**动态注册** AppFunction（b/501032667）
  - `AppFunctionState` + `AppFunctionManager#getAppFunctionStates` **取代** `AppFunctionMetadata#isEnabled`（元数据/状态分离，b/494238383）
  - 另：`getAppFunctionActivityStates`、`ExtensionsAppFunctionService`（sidecar）、`observeAppFunctions` 对齐平台 API；OOBE 阶段 `setAppFunctionEnabled` 崩溃修复。
  - 含义：本库 08-03 记的「四平台唯一动态可见性 API」机制升级为 state-based；Registry 仍为随状态实时变化的动态视图。
- **跨平台端侧 Planner 评测增量（BFCL v4，第三方来源，已标待补）**
  - Apple on-device Foundation Model 首登 BFCL v4 单轮 **61.7%**（aibacon 引 Berkeley 榜）
  - LittleLamb-ToolCalling-ONNX **0.3B**：BFCL v4 **51.55%（think）/ 50.51%（no-think）**（HF jromarllegue）
  - FunctionGemma 270M 全-v4 **27.03**（think=no-think，因其无 thinking 模式）
  - Needle 2 42.6% 获 aibacon 独立确认 + 「置信趋零→返回空调用」升级契约；MIT/Apache 许可，落 ESP32/树莓派5/Quest3S
  - Gemma 4 native tool tokens（d-central 第三方，待官方）
- **跨平台/监管**：欧盟 DMA 要求 Google 在 **2027-08 前**向竞品助手开放 11 项 Android AI 能力，AppFunctions Registry 使函数可被任一认证助手发现，`EXECUTE_APP_FUNCTIONS` 在 EU 下沉为「认证闸门」→ 新建 B 节点 [[AppFunctions 跨助手可发现性与 DMA 强制开放 2026]]。

## 落库
- A 原始资料：[[AppIntent 每日情报 2026-09-01]]（索引+已复核无净新增表）
- D 输出：[[AppIntent 每日情报速览 2026-09-01]]
- B 净新增 1：[[AppFunctions 跨助手可发现性与 DMA 强制开放 2026]]
- B 既有增补 4：[[Android AppFunctions 设备侧意图 2026]] / [[Function Calling 端侧工具调用]] / [[端侧 Router 置信度门控与工具可达性收缩 2026]] / [[四平台意图 Registry 来源轴与权限模型对比 2026]]
- 看板：知识飞轮看板.md 末「本次新增（2026-09-01）」区已登记。

## 已复核·无净新增（避免重复检索）
- Apple：iOS 27 Beta 8 与 08-15 Beta 5 逐字一致（同 bug 号）→ 不重复计数。
- HarmonyOS：7 开发者 Beta（6-12）/ 消费 Beta（8-3）/ 正式版秋季待发，无新 API。
- Windows：Copilot Vision 2026-05 GA；官方 agentic security 文档 2025-12-05 后再无更新；26H2/Ignite 2026-11 仅为路线图，非已发布 API。
- 跨平台 BFCL v4 镜像榜（benchlm）数字已在 08-26 入表。

## 诚实标注 / 待办
- Apple FM 61.7% 与 LittleLamb 0.3B 为**第三方引述**，待 Berkeley 官方榜复核。
- DMA「11 项能力清单 + 2027-08 deadline」为 ecorpit 分析，待欧盟官方文本回填。
- alpha11 `@AppFunctionSignature` 动态注册是否需要新 Manifest 权限/签名待核。
- 长期待办（延续）：Berkeley 官方 BFCL v4 博客原文；Watch OS 26 Trust Insights 类；NowSecure/AgentAntibody 独立核验；Chrome Origin Sets 官方 URL 逐字复核；把 alpha11 `AppFunctionState` 反映进对比表「运行时动态可见性 API」行。
