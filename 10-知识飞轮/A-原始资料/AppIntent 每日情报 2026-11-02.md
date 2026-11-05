---
date: 2026-11-02
tags: [AppIntent, 每日情报, 复核型, 零净新增, 来源轴延续, OS框架不日更, WindowsCopilotActions收敛]
source: "https://developer.apple.com/documentation/updates/appintents ; https://developer.apple.com/ios/whats-new/ ; https://developer.android.com/jetpack/androidx/versions/all-channel ; https://www.anddev.org/article/android-development-moves-to-agentic-apis-and-adaptive-compose-boundaries.html ; https://developer.android.com/blog/posts/the-intelligent-os-making-ai-agents-more-helpful-for-android-apps ; https://developer.huawei.com/consumer/en/doc/HarmonyOS-Guides/intents-introduction ; https://developer.huawei.com/consumer/en/doc/HarmonyOS-Guides/arkaf-overview ; https://www.analyticsinsight.net/news/microsoft-removes-8-copilot-ai-actions-from-windows-11-file-explorer ; https://pan.parallax.kr/article/14mb-ai-model-ubiquitous-on-device-intelligence ; https://www.microsoft.com/en-us/security/blog/2026/09/30/secure-whats-next-your-guide-to-microsoft-security-at-microsoft-ignite-2026/ ; WebSearch/WebFetch 直查官方/权威源（无 Horizon MCP，仅 agent-mail 在线）"
importance_score: "★★☆☆☆"
intent_category: "系统级意图框架 / 24h+ 复核 / 四平台零净新增 / 来源轴延续 / Windows Copilot Actions 收敛"
---

# AppIntent 每日情报 2026-11-02

> [!abstract] 30 秒速览
> 本窗口（2026-10-31 21:53 → 2026-11-02 12:21，约 38h）**四平台官方框架层 + 跨平台 BFCL 端侧 Planner + XPIA 研究线，再次全部零净新增 API / 评测 / 研究突破**——与连续多轮「OS 框架不日更」结论完全连续，本运行为**纯复核型**。逐平台核验结论：Apple（App Intents Updates 官方页 WebFetch 直查仍列 iOS 27 时代 API 集、无 2026-11 新 schema；iOS 27.2 已 GA、无 iOS 27.3 新意图 Schema 信号）/ Android（官方 Jetpack Release Notes 直查确认 **AppFunctions 仍 `1.0.0-beta01`（10-21）最新**、无 beta02/alpha14；A2UI 仍 alpha、ML Kit Agentic API 仍 alpha；Dev Summit 10-28 状态边界确认「AppFunctions is in beta」）/ HarmonyOS（Intents Kit 指南/ArkAF 概述稳定，无 11-01/02 新 API）/ Windows（无新 OS 执行总线 API；但 MC1515940 公告 **File Explorer 右键菜单 8 项 OneDrive Copilot Actions 将于 2026-11 中旬起分阶段整合进「Ask Copilot」**——属 surface 收敛，非新 API）/ BFCL v4（FunctionGemma 270M / qwen3-0.6b-tool-router 仍不在榜，无新端侧 ≤数 B Planner official entry）。**本运行 0 新建 B 节点、0 既有 B 增补**（无 ≥6/10 真增量），仅对 Windows B 笔记追加一条 ★5 状态行；最高优先「来源轴四平台全空白」待办延续。

## ① Schema 定义与语义路由（本窗口）

| 平台 | 本窗口 Schema/路由层净新增 | 重要性 | 处置 |
|---|---|---|---|
| Apple | App Intents Updates 官方页（developer.apple.com/documentation/updates/appintents）WebFetch 直查仍列 iOS 27 时代 API 集（SyncableEntity / OwnershipProvidingEntity / RelevantEntities / EntityCollection / IndexedEntity / ExecutionTargets / @UnionValue / View Annotations / App Intents Testing / Suggested Actions / Media Intents / IntentDonationManager 扩展捐赠），**无 2026-11 新 schema 条目**；iOS 27.2 已 GA；检索未见 iOS 27.3 beta 引入新 `@AppIntent(schema:)` 信号 | ★★☆☆☆（无净新增） | 已复核·无净新增 |
| Android | 官方 Jetpack Release Notes（d.android.com/jetpack/androidx/versions/all-channel）直查确认 **AppFunctions 仍 `1.0.0-beta01`（2026-10-21）最新**，无 `1.0.0-beta02` / `alpha14`；A2UI 仍 alpha（all-channel 10-21 列 alpha02、本窗口无新进位）；ML Kit Agentic API 仍 alpha；「The Intelligent OS」博客（developer.android.google.cn）为既有 beta + Samsung Gallery/Galaxy S26 伙伴实例，**非新 API 进位** | ★★☆☆☆（无净新增） | 已复核·无净新增 |
| HarmonyOS | Intents Kit 指南（developer.huawei.com/consumer/en/doc/harmonyos-guides/intents-introduction）与 ArkAF 概述（arkaf-overview）稳定；检索未捕获 11-01/02 新 API | — | 已复核·无净新增 |
| 跨平台 BFCL | FunctionGemma 270M / qwen3-0.6b-tool-router 仍不在精选榜；PAN 对 Needle 2 / FunctionGemma 270M / LFM2.5-230M 的 BFCL v4 single-turn 拆解（Simple 73.3/63.2/48.1；Overall 61.7/46.1）与库内 08-26/10-26 数据一致，**无新端侧（≤数 B）Planner official entry** | ★★☆☆☆（无端侧净新增） | 已复核·无端侧净新增 |

要点：
- **🔑 窗口内无 Schema/路由层真增量**：四平台本 38h 均无新 `@AppIntent(schema:)` / 新 AppFunctions 版本进位 / 新 Intents Kit API / 新 Windows 执行总线 Registry。Apple App Intents Updates 页经 WebFetch 直查确认仍停留在 iOS 27 时代 API 集（含 WWDC26 已发布的 View Annotations / App Intents Testing / Suggested Actions / Media Intents，但**无 2026-11 新条目**）。
- **Android 成熟度维持 + 状态边界确认**：AppFunctions `beta01`（10-21）经官方 Jetpack Release Notes 发布页直查确认仍最新；anddev 对 Android Dev Summit（10-28）的复盘明确列出能力边界表——AppFunctions **Beta** / A2UI for Jetpack Compose **Alpha** / ML Kit Agentic API **Alpha** / AppState **Alpha**，无新进位。
- **BFCL v4 端侧零净新增**：端侧小模型（FunctionGemma 270M / qwen3-0.6b-tool-router）仍不在榜；PAN 的 Needle 2 / LFM2.5-230M / FunctionGemma 270M BFCL v4 拆解数字与库内既有记录一致，无新 entry。

## ② 系统安全与 UX（Confirmation / 隔离 / 防注入）

### 窗口内命中但低于收录阈值（复述 / 部署 / 应用层 / surface 收敛，非新 OS API）
- **Windows File Explorer 右键菜单 8 项 OneDrive Copilot Actions 整合（MC1515940，analyticsinsight/thinkcomputers/Windows Latest 报道）**：微软宣布将移除 File Explorer 右键菜单中 8 项 OneDrive 关联 Copilot Actions（Summarize / Create FAQ / Compare Files / Ask a question / Explain image / Explain images / Compare images / Extract text），统一收纳进「Ask Copilot」入口；分阶段 **2026-11 中旬起**开始、**2026-12 初**完成。属 **Copilot Actions surface 收敛/整理**，能力本身保留（仍经右键「Ask Copilot」/File Explorer Home/OneDrive 活动中心可达），**非新框架 API / 非新安全机制**。★5/10 —— 直接落在任务范围「Windows：Copilot Actions」，故不丢弃、在 A 索引登记并追加一条 ★5 状态行到 [[Windows Copilot Actions 与 Agent Workspace 2026]]，但不升 B 节点（低于 6 阈值）。
- **Apple iOS 27 / Core AI / Foundation Models（iOS 27 whats-new 页）**：iOS 27 时代的 Core AI 框架（Apple Silicon 原生、自带模型 on-device、Metal tensors）+ Foundation Models 模型无关化（Apple/云/PCC/第三方）+ Evaluations 框架，均为 **WWDC26 已发布、已 GA（9-14）内容**，本窗口无新条目。★3/10
- **HarmonyOS 教程/生态复盘**：ArkAF 概述、Intents Kit 指南为官方稳定文档；CSDN「Agent 亲和架构」为开发者教程。低于阈值丢弃。
- **XPIA 原理/分类复述波（appsecmaster / nhimg / zone.ci）**：拆解直接/间接/XPIA/多模态/工具选择/工具描述/MCP-sampling/记忆投毒等注入类型，引用 OWASP Agentic AI Top 10（ASI02 Tool Misuse / ASI03 Identity & Privilege Abuse）/ MITRE ATT&CK T1204 / NIST SP 800-53 SI-10——均为**既有机制原理/教程，无新 OS 执行总线机制**，低于阈值丢弃。
- **Windows Ignite 2026 预热（Microsoft Security Blog 09-30 / redmondmag 10-05）**：Ignite 2026 定档 **11-17~11-20 旧金山**，安全主题含「Agentic security / Zero Trust runtime / Govern AI / Entra agent identity」；但**大会尚未开幕**，属路线图预告、非已发布 API，不计入本窗口净新增（延续 10-31「Ignite 仅为路线图，非已发布 API」纪律）。

### 去伪 / 丢弃（按口径）
- **Apple 本窗口发新 `@AppIntent(schema:)` Schema / iOS 27.3 新意图 Schema**：不成立——App Intents Updates 官方页 WebFetch 直查仍 iOS 27 时代 API 集、无 2026-11 条目；检索未见 iOS 27.3 新意图 Schema 信号。
- **Android 发 AppFunctions beta02 / alpha14**：不成立——官方 Jetpack Release Notes 直查确认 beta01（10-21）仍最新。
- **LFM3-1.7B（Liquid AI，Oct 27，BFCL v4 ≈71.39）**：已于 10-29 运行捕获（标记为「新出、官宣日待补」），**非本窗口新事件**，不重复计。
- **Bonsai 2 三值量化家族（PrismML，Oct 15，2B/4B/9B，含 tool calling）**：Oct 15 落本窗口前约 18 天，纯模型发布、无 BFCL official entry 数字待核，**按「纯模型发布（除非直接用于端侧意图路由）」口径丢弃**（同 10-31 Muse Glimmer 30B / Needle 3 纪律）。
- **Nemotron 3.5 Bolt（Nvidia，Oct 19，74B A9B / E4B 本地 agent 模型）**：Oct 19 窗口外，纯模型发布，丢弃。
- **LFM2.5-24B-A2B（Liquid AI，BFCL v4 65.01）**：24B MoE（激活 2B）属**边缘大模型**而非「≤数 B 端侧 Planner」严格范畴，发布日疑似 10 月底（窗口外），**不计入本窗口端侧小模型净新增**；仅作跨平台端侧 agent 模型格局的 monitor 项（与库内 LFM2.5-230M 21% 区分规模档）。
- **Windows 本窗口有新 OS 执行总线 API**：不成立——仅 File Explorer Copilot Actions surface 收敛（MC1515940）+ Ignite 预热，无新 Registry API。

> [!note] 概念节点双链
> [[意图模式规范]] [[语义路由]] [[端侧工具调用]] [[确认机制]] [[元服务]] [[隔离执行]] [[A2A 端侧智能体协议]] [[XPIA 跨提示注入]]

---

> [!warning] 诚实标注
> - Apple App Intents Updates 官方页（developer.apple.com/documentation/updates/appintents）经本运行 WebFetch 直查，仍列 iOS 27 时代 API 集（含 WWDC26 发布的 View Annotations / App Intents Testing / Suggested Actions / Media Intents，但无 2026-11 新 schema 条目）；iOS 27.2 已 GA，未检索到 iOS 27.3 引入新 `@AppIntent(schema:)` 的信号；iOS 27 whats-new 的 Core AI / Foundation Models 模型无关化 / Evaluations 均属 9-14 GA 内容、非窗口内新增。
> - Android AppFunctions 仍 `1.0.0-beta01`（10-21）经官方 Jetpack Release Notes（d.android.com/jetpack/androidx/versions/all-channel）直查确认最新；A2UI 仍 alpha、ML Kit Agentic API 仍 alpha，Dev Summit 10-28 能力边界表（anddev）确认此状态；「The Intelligent OS」博客（developer.android.google.cn）为既有 beta 能力 + Samsung Gallery/Galaxy S26 伙伴实例展示，非新 API 进位；`@AppFunctionAccessLevel` 级别语义仍待 developer.android.com/ai/appfunctions 官方文档。
> - BFCL v4：PAN 对 Needle 2 / FunctionGemma 270M / LFM2.5-230M 的 BFCL v4 single-turn 拆解（Overall 61.7 / 46.1 / 42.6）与库内 08-26/10-26 数据一致，**无新端侧（≤数 B）Planner official entry**；官方 Berkeley 榜停滞（2026-04-12）。
> - Windows File Explorer 8 项 Copilot Actions 整合（MC1515940）经 analyticsinsight/thinkcomputers/Windows Latest 报道，分阶段 2026-11 中旬起 ~ 2026-12 初完成；属 Copilot Actions surface 收敛、非新 API，故仅记 ★5 状态行到 [[Windows Copilot Actions 与 Agent Workspace 2026]]、不升 B 节点。Ignite 2026（11-17~20）尚未开幕，预热议程（Agentic security/Zero Trust runtime）属路线图预告、非已发布 API。
> - 本运行未使用 Horizon MCP（仅 agent-mail 在线），全部以 WebSearch + WebFetch 直查官方源 + 权威媒体完成逐平台核验；**0 新建 B 节点、0 既有 B 增补（除 Windows B 一条 ★5 状态行）**（无 ≥6/10 真增量），符合去重纪律。
> - 窗口内 LFM3-1.7B（Oct 27）/ Bonsai 2（Oct 15）/ Nemotron 3.5 Bolt（Oct 19）均落本窗口之前，按「非 24h 内新事件」或「纯模型发布」口径处理，不重复计为净新增。
