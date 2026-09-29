---
date: 2026-09-15
tags: [AppIntent, 每日情报, 端侧Planner, 执行安全, 跨平台, iOS27GA]
source: "https://developer.apple.com/ios/whats-new | https://www.techtimes.com/articles/318005/wwdc-2026-app-intents-replaces-sirikit | https://www.windowsforum.com/threads/windows-agent-workspaces-ai-agents-in-isolated-sessions-with-safety-controls | https://caifuhao.eastmoney.com/news/20260911212754362221420 | https://huggingface.co/AryanNsc/qwen3-0.6b-tool-router | https://benchlm.ai/benchmarks/bfclV4"
importance_score: "★★★★☆"
intent_category: "iOS 27 GA / 执行安全 / 跨平台评测"
---

# AppIntent 每日情报 2026-09-15

> [!abstract]
> **30 秒速览（窗口 2026-09-13 → 09-15）**
> - **核心突破**：① **iOS 27 正式版（09-14）落地，App Intents 框架级能力获官方 post-GA 确认**——Entity schemas（写入 Spotlight 语义索引 + 归属回 App）、Intent schemas（免特定短语、免改码）、**View Annotations API**（视图→实体映射，对话式引用屏幕内容）、App Intents Testing 框架；**Foundation Models 框架宣布支持任意语言模型**（Apple FM / Claude / Gemini 或任何遵循 `Language Model` 协议者）+ Dynamic Profiles（连续会话内实时切换模型/工具/instructions）+ Evaluations。这是 OS 级 Planner 首次把「多模型路由」写进一等公民框架。
> - **关键指标 / 校正**：② **Per-Intent Privacy Manifest 待办重开**——08-31 判定「证伪」的结论在 GA 后被 WWDC 2026 多源二次报道挑战（Apple 据称引入按意图声明「可上云 / 须留端」的隐私清单）；但官方 post-GA「What's New in iOS 27」页未逐字列出该 API，**由「已证伪」升为「GA 后待官方文档逐字复核」**，不推翻来源轴空白结论。③ Windows 新增 **Agent 代码签名 + 证书校验/吊销**机制（执行安全加固）。④ HarmonyOS 7 小艺 2.0 / 导航条主动服务入消费者（ArkAF「意图即服务」真机落地）。
> - **OS Agent 场景**：本窗口是真·GA 窗口（iOS 27 09-14 / HarmonyOS 7 消费者 09-07 已在铺开 / Windows 26H2 下旬在即）——四大 OS 框架层除 iOS 27 GA 确认的 Schema Protocol 能力外**无其它净新增 API**（AppFunctions 守 alpha11 无 alpha12、Windows 四支柱 + 容器隔离无新 Registry API、鸿蒙意图框架同 HDC2026）。真增量 = GA 落地确认 + 一处执行安全机制 + 一处路由待办校正。

## 索引（每条 1 行：重要性 + 原子笔记 + 枢纽 + 一手来源）

- ★★★★☆ **iOS 27 GA（09-14）：App Intents Schema Protocol 能力获官方 post-GA 确认 + Foundation Models 多模型路由（Claude/Gemini via Language Model protocol）** → [[Apple AppIntents Schema Protocol 2026]]（#iOS27GA）｜ 来源 <https://developer.apple.com/ios/whats-new>（官方 post-GA 页，2026-09-14）
- ★★★☆ **Per-Intent Privacy Manifest 待办重开：08-31「证伪」被 WWDC 2026 多源二次报道挑战，官方页未列，升为 GA 后待复核** → [[四平台意图 Registry 来源轴与权限模型对比 2026]]（#来源轴）｜ 来源 <https://www.techtimes.com/articles/318005/wwdc-2026-app-intents-replaces-sirikit>（多源一致，2026-06-08 发布）+ <https://developer.apple.com/ios/whats-new>（官方 post-GA 页，未列该 API）
- ★★★☆ **Windows：Agent 代码签名 + 证书校验/吊销机制（执行安全加固，三原则 non-repudiation/confidentiality/authorization 落地）** → [[Windows Copilot Actions 与 Agent Workspace 2026]] ＋ [[Agent Workspace 隔离执行]]（#执行安全）｜ 来源 <http://www.windowsforum.com/threads/windows-agent-workspaces-ai-agents-in-isolated-sessions-with-safety-controls>（2026-09，第三方综述，非官方逐字）
- ★★★☆ **HarmonyOS 7 小艺 2.0 / 导航条主动服务入消费者（ArkAF「意图即服务」真机落地，200+ 系统数据 / 2100+ 系统能力 / 四层记忆 / 复制内容主动推荐）** → [[HarmonyOS Intents Kit 与 ArkAF 2026]]（#ArkAF落地）｜ 来源 <https://caifuhao.eastmoney.com/news/20260911212754362221420>（2026-09-11 媒体整理，厂商/媒体口径）
- ★★☆☆ **BFCL v4 榜单维持 Qwen3.7 Max 75.0% 领先（与 08-04/09-13 一致）；qwen3-0.6b-tool-router 补 BFCL 子集分（Non-Live Parallel AST 83.50% / Live Simple 62.86% / Live Parallel 52.00%）** → [[Function Calling 端侧工具调用]]（#跨平台评测）｜ 来源 <https://benchlm.ai/benchmarks/bfclV4>（2026-09-08 快照）+ <https://huggingface.co/AryanNsc/qwen3-0.6b-tool-router>（HF 模型卡）

## 已复核·无净新增（避免重复检索）

- **Apple**：iOS 27 正式版（09-14）官方 post-GA「What's New in iOS 27」页确认的 App Intents 新增（Entity/Intent schemas、View Annotations API、App Intents Testing）**均为 WWDC26 已宣布、本次 GA 落地的能力**（本库 08-02/08-26 已录），**无 WWDC 之外的全新 API**；本次属「GA 落地确认」而非新公告。**Foundation Models 多模型路由（Claude/Gemini）** 在 08-17 已记「可切换 Apple/Claude/Gemini」，本次获官方 post-GA 页重申并明确「任何遵循 Language Model 协议者」——属 GA 确认升级，非新 API。Per-Intent Privacy Manifest 见上方索引②（待办重开，非新 API）。
- **Android**：AppFunctions Jetpack 仍 **alpha11**（2026-08-26 官方 Release Notes），窗口内**无 alpha12**；Google 官方博客《由 AppFunctions 提供支持的 Android MCP》重申「App=本地 MCP server / Platform=中央工具 Registry / Agent=MCP client 持 EXECUTE_APP_FUNCTIONS_TRUSTED 系统特权」——与既有结论一致，非新 API。⚠️ 版本口径冲突：该博客及多篇社区文引用 alpha08/09/10，与官方 Release Notes alpha11 不一致；博客提及「Android 17 或更高」ADB 命令与库内「compileSdk ≥ 36（Android 16）」冲突——**均待官方文档澄清**。
- **HarmonyOS**：Intents Kit / ArkAF 2.0 / A2UI 框架同 HDC2026 / 09-07 消费版，**无新意图框架 API**；新增 小艺 2.0 / 导航条主动服务为**消费者 UX 落地**（非框架 API），API 26 已确认（09-13 收口）。星盾 AI 反诈（芯片级境外转打检测 / AI 变声检测 / 风险检出率 >90%）为安全能力，但**非 XPIA/ODR/Confirmation 框架层**，按规则作低优先上下文。
- **Windows**：Copilot Actions / Agent Workspace / ODR / Agent Launchers 四支柱 + IFA 2026 Execution Containers 容器隔离**无新 Registry API**；新增 Agent 代码签名/吊销为安全机制细节（已落 B 增补），非新 API。
- **跨平台 BFCL v4**：BenchLM 2026-09-08 公开快照 **Qwen3.7 Max 75.0% 领先**，与本库 08-04/08-05/08-26/09-13 历次快照一致（Ling 3.0 Flash 73.0% / Qwen3.7 Plus 72.9% / LFM2.5-2.6B 56.9% 等）；DataLearner 2026-09-07 镜像标「MiniCPM5-2B 66.60 榜首」疑为子集/滞后口径，与 BenchLM 全量镜像不冲突（Qwen3.7 Max 75.0% 始终为闭源榜首）。**榜单无净变化**，仅 qwen3-0.6b-tool-router 补 BFCL 子集分。

> [!note]
> 概念节点：[[Intent Schema Protocol 意图模式规范]] ｜ [[Intent Router 语义路由]] ｜ [[Function Calling 端侧工具调用]] ｜ [[Confirmation UI 安全机制]] ｜ [[Atomic Service 元服务]] ｜ [[Agent Workspace 隔离执行]] ｜ [[A2A 端侧智能体协议]] ｜ [[XPIA 跨提示注入]]
