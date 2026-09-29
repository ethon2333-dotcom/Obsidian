---
date: 2026-09-18
tags: [AppIntent, 每日情报, 执行安全, 端侧Agent执行总线, 跨平台, 框架复核]
source: "https://developer.apple.com/wwdc26/guides/ios/ | https://developer.android.com/ai/appfunctions | https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkaf-overview | https://msftnewsnow.com/microsoft-copilot-actions-ai-power-task-automation/ | https://llmlearner.com/rankings/bfcl-v4 | https://www.cisoplatform.com/profiles/blogs/owasp-top-10-agentic-applications-2026-ai-agent-testing-guide | https://microsoft.github.io/RAMPART/attacks/xpia"
importance_score: "★★☆☆"
intent_category: "框架复核·无净新增（四平台官方框架层 + BFCL v4 榜单 + XPIA 研究线均无 24h 净新增）"
---

# AppIntent 每日情报 2026-09-18

> [!abstract]
> **30 秒速览（窗口 2026-09-17 22:38 → 09-18 21:00，约 22h）**
> - **核心结论**：**四大 OS 官方框架层本窗口（24h）无净新增 API**，且 **BFCL v4 榜单 + XPIA 研究线亦无 24h 净新增**——完全符合「OS 框架不日更」规律，也与 09-17（含 22:38 日间补充 SIR + 权重级持久化）的结论连续一致。本期为**复核型运行**，价值在于把「已复核·无净新增」显式落档，避免下次重复检索。
> - **唯一低于收录阈值的状态更新（★5/10，不入新 B 节点）**：Windows Copilot Actions 经 msftnewsnow 报道已随 Copilot app 更新 **1.25112.74+** 向 Windows Insiders **分批推送「Now Available」**——属已记录预览功能的部署推进，非框架 API 新增；已作为状态行追加至 [[Windows Copilot Actions 与 Agent Workspace 2026]]。
> - **关键校正**：Apple `iOS 27.1` 首个 beta **尚未发布**（Macworld 09-18 确认），即短期内无新的 App Intents API 可期；搜索命中的 iOS 27 文章全部为 09-14 GA 后的二次复述（TechPillow / Cropsly / ecorpit / byteiota / dev.to / macworld），无 WWDC 之外的新 API。
> - **OS Agent 场景**：iOS 27 GA 后第 4 日、Windows 26H2（9 月下旬~10 月初）窗口在即。本期增量 = 0；执行安全最新进展仍停在 09-17 的 **SIR 自改进攻击 + 自修改 Agent 权重级持久化** 两条。

## 正文拆解

### ① Schema 定义与语义路由机制

- **四大 OS 官方框架层本窗口无净新增 API（逐项复核）**：
  - **Apple**：`developer.apple.com/wwdc26/guides/ios` App Intents 段落自 GA 后未变；本轮搜索命中的 iOS 27 文章（TechPillow、Cropsly、ecorpit、braze、byteiota、dev.to、macworld）均为 **09-14 GA 后的二次复述**——App Intents 成唯一 Siri 路径、SiriKit 弃用、Foundation Models 多模型路由、View Annotations、App Intents Testing，全部为 WWDC26 已宣布 / 09-15 已录内容，**无 WWDC 之外全新 API**。**iOS 27.1 首个 beta 尚未发布**（Macworld 09-18：「Apple hasn't released the first iOS 27.1 beta yet」）→ 短期内无新 App Intents API 信号。
  - **Android**：`developer.android.com/ai/appfunctions` 仍标 **Experimental 预览**，Jetpack 库**仍为 alpha（本库 09-01 录 alpha11，窗口内无 alpha12）**；`EXECUTE_APP_FUNCTIONS` / `EXECUTE_APP_FUNCTIONS_SYSTEM` 权限与 `AppFunctionsManager` 框架（含 `AppFunctionState` 三态、`PROPERTY_SUPPORT_APP_FUNCTION_USER_CONTROL`）为既有稳定文档内容。Android Police「security cage is empty」（09-14）复述 `EXECUTE_APP_FUNCTIONS` 目前仅对第一方 Gemini 开放——属已覆盖事实的媒体化复述，非 24h 新增。
  - **HarmonyOS**：`developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkaf-overview` + `intents-access-flow` 为稳定文档，三层框架（意图框架 / Skills / 端侧 A2A）无新 API；搜索命中的 AI News / pandaily / heyupnow / CSDN / Sohu 均为 **HDC2026 / 09-07 消费版**的旧文复述（Intelligent Agent Framework 2.0、intent-as-service、小艺 2100+ 系统能力），无 24h 净新增。
  - **Windows**：`windowsnews.ai` / `msftnewsnow` / `windowsforum` 的 Copilot Actions 报道为 08-02/08-05/09-13/09-16/09-17 已记录能力（Copilot Actions / Agent Workspace / ODR / Agent Launchers / Execution Containers / 签名吊销）的**部署推进**，非框架 API 新增；`dev.to`「Microsoft Copilot September 2026 Updates」讲的是**云端 Copilot**（SharePoint 技能 / Brand Kit / Notebooks），属应用层、非 OS agentic 框架，按规则丢弃。
- **语义路由 / 端侧 Planner 评测线无 24h 新增**：BFCL v4 镜像榜（llmlearner / datalearner）当前 SOTA 仍为 **MiniCPM5-2B 66.6（2026-09-07）**、**Spark-X2.5-4B 65.1（2026-09-01）**，窗口内**无新模型入榜**；BenchLM「Best Tool Use 2026」（截至 2026-09-10）Qwen3.7 Plus 72 居首，属通用 tool-use 榜非新发布。FunctionGemma 270M / qwen3-0.6b-tool-router 等端侧 Planner 内容均为 2025/2026 上半年旧文。→ 端侧 Planner 评测表维持 09-13 后的稳定态。

### ② 系统安全与用户体验（Confirmation / 隔离 / 防注入）

- **XPIA / 执行安全研究线本窗口无 24h 净新增**：09-17 已记录 **SIR 自改进攻击（CUA 级、跨模型零反馈迁移）** 与 **自修改 Agent 权重级持久化** 两条，为本线最新进展；本次搜索命中的 Future AGI / Agentmelt / Casaba PDF / Microsoft RAMPART 均为**教育/防御类内容或旧标准**，非 24h 新研究突破：
  - **OWASP Agentic AI Top 10 2026** 经 cisoplatform / itmedia / akto / dsalta 多源确认 **发布于 2025-12-09**（版本号「2026」指其治理年份，同 LLM Top 10 按年版本化），属 9 个月前标准，非本期新发布；其 ASI01（Agent Goal Hijack，即 XPIA 在 agentic 语境的归位）与库内 [[XPIA 跨提示注入]] 元判断同源，可作为既有无净新增项的**标准化映射参考**，但不构成增量。
  - **Microsoft RAMPART**（github.io）为 XPIA **测试框架**（inline / surface-based / DOCX payloads + 组合式 evaluator），属红队评测工件、非 OS 执行安全机制变更，标「参考、待一手发布日期复核」。
- **Windows 部署状态更新（★5/10，低于收录阈值）**：msftnewsnow 报道 Copilot Actions 已随 Copilot app 更新 **1.25112.74+** 向 Insiders「Now Available」——把此前「预览 / opt-in 默认关」推进为**分批可安装**。属部署里程碑，能力清单（打开 app、点 UI、PDF 表提取、批量修图、邮件起草、Agent Workspace 内可见可中断）与 08-02 起记录一致，**无新框架 API**；已追加状态行至 [[Windows Copilot Actions 与 Agent Workspace 2026]]，未新建 B 节点。

## 索引（每条 1 行：重要性 + 原子笔记 + 枢纽 + 一手来源）

- ★★☆☆ **四平台官方框架层 + BFCL v4 + XPIA 研究线本窗口（24h）无净新增 API / 评测 / 研究突破** → 已复核·无净新增清单见下 ｜ 一手来源：developer.apple.com/wwdc26/guides/ios · developer.android.com/ai/appfunctions · developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkaf-overview · llmlearner.com/rankings/bfcl-v4
- ★★★☆ **（沿袭 09-17）XPIA 自改进攻击 SIR + 自修改 Agent 权重级持久化** → [[XPIA 跨提示注入]]（#执行安全）｜ 一手 arXiv / Irregular 报告待补（二次转述：notatechguy / Zicos-CSO）
- ★★☆☆ **Windows Copilot Actions 随 app v1.25112.74+ 向 Insiders 分批推送（部署里程碑，非 API 新增）** → [[Windows Copilot Actions 与 Agent Workspace 2026]]（#执行安全）｜ <https://msftnewsnow.com/microsoft-copilot-actions-ai-power-task-automation/>

## 已复核·无净新增（避免重复检索）

- **Apple**：iOS 27 GA（09-14）后**无新 App Intents API**；官方页仅列 WWDC26 已宣布、本次 GA 落地项，无 WWDC 之外全新 API。**iOS 27.1 beta 尚未发布**（Macworld 09-18 确认），短期无新信号。搜索命中的 7 篇 iOS 27 文章均为 GA 后复述。
- **Android**：AppFunctions Jetpack 仍 **alpha（alpha11，2026-08-26）**，窗口内**无 alpha12**；`EXECUTE_APP_FUNCTIONS` 权限 + `AppFunctionsManager` 框架 + `PROPERTY_SUPPORT_APP_FUNCTION_USER_CONTROL` 为既有稳定文档。Android Police 09-14「security cage」为媒体复述。Android 17 GA 已由 09-17 收录。
- **HarmonyOS**：Intents Kit / ArkAF 2.0 / A2UI 框架同 HDC2026 / 09-07 消费版，**无新意图框架 API**；搜索命中的 AI News / pandaily / heyupnow / CSDN / Sohu 均为旧文复述。API 26 已确认（09-13）。
- **Windows**：Copilot Actions / Agent Workspace / ODR / Agent Launchers / Execution Containers / 代码签名吊销**无新 Registry API**；本期仅 msftnewsnow 报道的 Insider 分批推送（app v1.25112.74+），属部署推进。云端 Copilot（dev.to SharePoint 技能/Brand Kit）为应用层、丢弃。
- **跨平台 BFCL v4**：数据版本维持 20260913 量级，SOTA **MiniCPM5-2B 66.6（09-07）/ Spark-X2.5-4B 65.1（09-01）**，窗口内**无新端侧 Planner 模型入榜**；FunctionGemma / qwen3-0.6b-tool-router 均为旧文。
- **XPIA 研究线**：OWASP Agentic AI Top 10 2026 = **2025-12-09 发布**（非本期）；Microsoft RAMPART 为测试框架工件。本期无新研究突破，最新进展仍停在 09-17（SIR + 权重级持久化）。
- **诚实标注**：本运行未调用 Horizon MCP（环境仅 `agent-mail` 连接器在线，无 Horizon MCP 工具）；改用 WebSearch/WebFetch 直查官方源，符合任务 fallback 约定。

> [!note]
> 概念节点：[[意图模式规范]] ｜ [[语义路由]] ｜ [[端侧工具调用]] ｜ [[确认机制]] ｜ [[元服务]] ｜ [[隔离执行]] ｜ [[A2A 端侧智能体协议]] ｜ [[XPIA 跨提示注入]]
