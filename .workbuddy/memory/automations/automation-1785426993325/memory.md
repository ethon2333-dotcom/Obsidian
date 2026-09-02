---
automation: AppIntent 每日情报（自动化 09:00 版，实际按 7 日滚动窗口运行）
last_run: 2026-09-01
window: 2026-08-25 → 2026-09-01
---

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
