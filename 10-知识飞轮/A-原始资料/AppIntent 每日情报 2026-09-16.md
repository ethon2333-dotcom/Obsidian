---
date: 2026-09-16
tags: [AppIntent, 每日情报, 执行安全, 端侧Agent执行总线, 跨平台, 库内空白补漏]
source: "https://learn.microsoft.com/en-gb/windows/security/book/operating-system-agentic-security | https://developer.apple.com/ios/whats-new | https://securityexpress.info/qualcomm-hexagon-npu-agentic-ai | https://developer.android.com/blog/posts/top-ai-on-android-updates-for-building-intelligent-experiences-from-google-i-o-26"
importance_score: "★★★☆"
intent_category: "执行安全官方确认 / 端侧Agent执行总线硅底 / 库内空白补漏"
---

# AppIntent 每日情报 2026-09-16

> [!abstract]
> **30 秒速览（窗口 2026-09-15 → 09-16）**
> - **核心突破**：① **Windows Agent 代码签名/吊销由「第三方口径」升为「官方确认」**——learn.microsoft.com「agentic security」文档把「Operational trust」列为 OS agentic security 四大原则之一：Agent 须可信源签名、可被证书校验/吊销阻断，补齐执行安全「身份级可信」一块。② **跨平台新信号**：Qualcomm Hexagon NPU 披露 **on-die agentic loop**（感知→Oryon CPU 编排 planning/routing/tool call/reflection→Hexagon+Adreno 异构推理→端上响应闭环）+ MediaTek Dimensity 9500S CIM/原生 BitNet 1.58-bit，「端侧 Agent 执行总线」下沉到芯片。
> - **关键指标 / 校正**：③ 重核官方「What's New in iOS 27」页，**Per-Intent Privacy Manifest 仍无此 API** → 维持 09-15「GA 后待官方复核」、四平台来源轴空白结论不变。④ 库内空白补漏：Android I/O '26 三条路由/编排原语（Firebase AI Logic Hybrid Inference 端云路由 / ADK for Android 多智能体 / A2UI Compose Renderer）。
> - **OS Agent 场景**：本窗口距 iOS 27 GA（09-14）仅 1 天，**四大 OS 官方框架层无净新增 API**（iOS 27 GA 后无新 App Intents；AppFunctions 守 alpha11 无 alpha12；HarmonyOS 同 HDC2026；Windows 四支柱无新 Registry API）。真增量 = 2 处官方复核升格 + 1 处跨平台硅底信号 + 库内空白补漏，符合框架不日更规律。

## 正文拆解

### ① Schema 定义与语义路由机制

- **四大 OS 官方框架层本窗口无净新增 API**：iOS 27 GA 后无新 App Intents 能力（官方页重核仅列 WWDC26 已宣布项）；AppFunctions 仍 `1.0.0-alpha11`（2026-08-26），窗口内**无 alpha12**；HarmonyOS Intents Kit / ArkAF 2.0 同 HDC2026 / 09-07 消费版；Windows Copilot Actions / Agent Workspace / ODR / Agent Launchers 四支柱无新 Registry API。
- **库内空白补漏（标真实日期 I/O '26）**：Android 补三条与「语义路由 / 跨应用编排」直接相关的原语——① **Firebase AI Logic Hybrid Inference**：显式路由模式 `PREFER_ON_DEVICE / PREFER_CLOUD / ONLY_ON_DEVICE / ONLY_CLOUD`，与 iOS 27 Foundation Models 多模型路由方向同构（端云推理路由原语）；② **ADK for Android**：首版跨端+云多智能体工作流编排（orchestration / context / sessions）；③ **A2UI Jetpack Compose Renderer**：把 A2UI 消息自动渲染为原生 UI 组件（与 09-12 高德 AGenUI 基于 Google A2UI 形成框架层呼应）。此前库内仅记 A2UI 鸿蒙落地，未单列这三者为 Android 路由/编排原语。
- **跨平台新信号**：高通 Hexagon NPU（Snapdragon Summit 2026 前披露）把「端侧 Agent 执行总线」下沉到芯片——**on-die agentic loop** 在片内闭环完成感知→编排（tokenization / planning / routing / tool calls / reflection）→异构推理→响应，支持 32K 长上下文 + KV-Cache 硬件加速 + 端上 30B MoE；联发科 Dimensity 9500S 以 Compute-in-Memory + 原生 BitNet 1.58-bit，3B 模型 50% 更低功耗、128K 上下文。这是端侧 Planner/路由的**算力底座升级**，与 [[Function Calling 端侧工具调用]] 评测表（Needle 2 / FunctionGemma / Apple FM）形成「模型 ↔ 芯片」闭环。

### ② 系统安全与用户体验（Confirmation / 隔离 / 防注入）

- **Windows Agent 代码签名 + 证书校验/吊销（★6/10，官方确认升级）**：09-15 仅 windowsforum 第三方综述；本次 WebFetch **learn.microsoft.com 官方 agentic security 文档**确认「**Operational trust**」原则——「Agents that integrate with Windows must be signed by a trusted source so that maliciously or poorly behaved agents can be revoked and blocked with a range of defense-in-depth measures like certificate validation and antivirus」。由「第三方口径」升为**官方确认的 OS agentic security 四大原则之一**，补齐执行安全从「进程/账号隔离（Agent Workspace）+ 容器隔离（Execution Containers）」到「**身份级可信**」的第三块拼图；与 Android `EXECUTE_APP_FUNCTIONS` 系统特权签名、HarmonyOS 芯片级可信根形成四平台对照。
- **Per-Intent Privacy Manifest（★3/10，维持待复核）**：重核官方「What's New in iOS 27」页（developer.apple.com/ios/whats-new），App Intents 段落仍只列 Entity/Intent schemas、View Annotations API、App Intents Testing、Foundation Models 多模型——**无 per-intent privacy manifest API**。维持 09-15「GA 后多源一致报道、但官方页未确认 → 待官方文档逐字复核」，不推翻「四平台意图 Registry 来源/provenance 轴全空白」结论（即便确认亦属「路由目的地 cloud vs on-device」轴，与 provenance 正交）。
- **待办延续**：Windows 签名/吊销是否纳入 ODR 注册信任链、是否受 08-02 `Experimental agentic features` 同一 opt-in 管控（learn.microsoft.com 复核）；鸿蒙 小艺导航条「复制即触发」置信度门控机制（是否等价端侧 Router 门控）；Per-Intent Privacy Manifest 官方文档逐字。

## 索引（每条 1 行：重要性 + 原子笔记 + 枢纽 + 一手来源）

- ★★★☆ **Windows：Agent 代码签名 + 证书校验/吊销由第三方升为官方确认（learn.microsoft.com「Operational trust」原则）** → [[Windows Copilot Actions 与 Agent Workspace 2026]] ＋ [[Agent Workspace 隔离执行]]（#执行安全）｜ 来源 <https://learn.microsoft.com/en-gb/windows/security/book/operating-system-agentic-security>（官方 agentic security 文档，2026-09-16 复核）
- ★★★☆ **Per-Intent Privacy Manifest 官方页重核仍无此 API，维持「GA 后待官方复核」、来源轴空白结论不变** → [[四平台意图 Registry 来源轴与权限模型对比 2026]]（#来源轴）｜ 来源 <https://developer.apple.com/ios/whats-new>（官方 post-GA 页，2026-09-16 复核）
- ★★★☆ **跨平台新信号：Qualcomm Hexagon NPU on-die agentic loop + MediaTek Dimensity 9500S CIM/1.58-bit（端侧 Agent 执行总线下沉芯片）** → [[端侧 Agent 执行总线 NPU 原生 agentic loop 2026]]（#执行总线硅底）｜ 来源 <https://securityexpress.info/qualcomm-hexagon-npu-agentic-ai>（Snapdragon Summit 2026 前披露，待官方文档确认 exact specs）
- ★★★☆ **库内空白补漏：Android I/O '26 路由/编排原语（Firebase Hybrid Inference 端云路由 / ADK for Android 多智能体 / A2UI Compose Renderer）** → [[Android AppFunctions 设备侧意图 2026]]（#语义路由）｜ 来源 <https://developer.android.com/blog/posts/top-ai-on-android-updates-for-building-intelligent-experiences-from-google-i-o-26>（I/O '26，2026-05）

## 已复核·无净新增（避免重复检索）

- **Apple**：iOS 27 正式版（09-14）后**无新 App Intents API**；官方「What's New in iOS 27」页 App Intents 段落仅列 WWDC26 已宣布、本次 GA 落地的能力（Entity/Intent schemas、View Annotations、App Intents Testing、Foundation Models 多模型路由），**无 WWDC 之外全新 API**；Per-Intent Privacy Manifest 见上方索引②（重核仍无，维持待复核）。
- **Android**：AppFunctions Jetpack 仍 **alpha11**（2026-08-26 官方 Release Notes），窗口内**无 alpha12**；官方 I/O '26 博客重申「App=本地 MCP server / Platform=中央工具 Registry / Agent=MCP client 持 EXECUTE_APP_FUNCTIONS 系统特权」——与既有结论一致，非新 API。版本口径冲突（社区文引用 alpha08/09/10 vs 官方 alpha11；「Android 17」ADB vs compileSdk ≥36）仍待官方澄清。
- **HarmonyOS**：Intents Kit / ArkAF 2.0 / A2UI 框架同 HDC2026 / 09-07 消费版，**无新意图框架 API**；小艺 2.0 / 导航条主动服务 / 碰一碰为消费者 UX 落地（已录 09-15），API 26 已确认（09-13）。
- **Windows**：Copilot Actions / Agent Workspace / ODR / Agent Launchers 四支柱 + IFA 2026 Execution Containers 容器隔离**无新 Registry API**；Agent 代码签名/吊销见上方索引①（已由第三方升为官方确认）。
- **跨平台 BFCL v4**：BenchLM 2026-09-08 公开快照 **Qwen3.7 Max 75.0% 领先**，与本库历次快照一致（Ling 3.0 Flash 73.0% / Qwen3.7 Plus 72.9% / LFM2.5-2.6B 56.9% 等），**榜单无净变化**；Needle 2（42.6% BFCL v4 单轮 / 28.7% Seal-Tools OOD）、Apple FM（61.7%）、FunctionGemma（46.1%）分数稳定，待 Berkeley 官方榜复核。

> [!note]
> 概念节点：[[Intent Schema Protocol 意图模式规范]] ｜ [[Intent Router 语义路由]] ｜ [[Function Calling 端侧工具调用]] ｜ [[Confirmation UI 安全机制]] ｜ [[Atomic Service 元服务]] ｜ [[Agent Workspace 隔离执行]] ｜ [[A2A 端侧智能体协议]] ｜ [[XPIA 跨提示注入]]
