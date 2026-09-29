---
date: 2026-09-17
tags: [AppIntent, 每日情报, 执行安全, 端侧Agent执行总线, 跨平台, 库内空白补漏]
source: "https://www.notatechguy.com/prompt-injection-attack-on-ai-agents-jumps-to-28-success | https://adersaytech.com/ai-tutorial/windows-ai-agent-permissions.html | https://developer.android.com/ai/intelligence-system | https://developer.android.com/blog/posts/android-17-is-here"
importance_score: "★★★☆"
intent_category: "执行安全 XPIA 自改进攻击 / Windows ODR 权限模式 / Android 17 GA 确认（库内空白补漏）"
---

# AppIntent 每日情报 2026-09-17

> [!abstract]
> **30 秒速览（窗口 2026-09-16 → 09-17）**
> - **核心突破**：① **XPIA 攻击侧首次出现「自改进」范式（SIR，香港中文大学 arXiv 预印本）**——把提示注入当可演化攻击框架，失败→诊断→提炼绕过→复用，ASR 经自我试错从 Gemini 3.5 Flash 0%→28%、Claude Opus 4.8 4%→24%，且绕过原则**跨模型零反馈迁移**，属执行安全研究范畴（★6/10）。② **Windows ODR Agent Connectors 权限模式具象化**（预览 build 26100.7344+，第三方教程）：连接器默认关进 Agent Workspace、consent 三档（Ask every time / Allow always / Never allow），与既有「签名 + 隔离 + 受控发现」形成闭环（★6/10）。③ **Android 17 GA 确认 + AppFunctions 进 Android 17 智能系统叙事**，但 AppFunctions 仍 alpha11、无 alpha12，compileSdk 建议升 37（★6/10，库内空白补漏）。
> - **关键校正**：④ **四大 OS 官方框架层本窗口（24h）无净新增 API**——Apple 守 iOS 27 GA 已录 Schema Protocol；HarmonyOS 守 HDC2026/09-07 消费版；Windows 四支柱 + Execution Containers 无新 Registry API。符合「OS 框架不日更」规律，已在 A 层显式列「已复核·无净新增」避免重复检索。
> - **OS Agent 场景**：iOS 27 GA 后第 3 日、距 Windows 26H2（9 月下旬~10 月初）尚有窗口。本期增量集中在**执行安全研究演进（SIR）**与**既有信号的实处化（Windows ODR 权限模式 / Android 17 GA 确认）**，无新框架 API。

## 正文拆解

### ① Schema 定义与语义路由机制

- **四大 OS 官方框架层本窗口无净新增 API**：iOS 27 GA 后无新 App Intents（官方页重核仅列 WWDC26 已宣布项，09-15/09-16 已录）；AppFunctions 仍 `1.0.0-alpha11`（2026-08-26），窗口内**无 alpha12**（第三方复核 androidboss 2026-09-06 + 官方 release page 一致）；HarmonyOS Intents Kit / ArkAF 2.0 同 HDC2026 / 09-07 消费版；Windows Copilot Actions / Agent Workspace / ODR / Agent Launchers 四支柱 + IFA 2026 Execution Containers 无新 Registry API。
- **Android 17 GA 确认（★6/10，库内空白补漏）**：官方 `developer.android.com/ai/intelligence-system` 将 AppFunctions 与 Remote MCP server、Computer Control 并列为「让系统 agent（如 Gemini）跨本地应用与 web 服务安全编排」的三条新能力，AppFunctions 正式纳入 Android 17「Intelligence System」主线；但 AppFunctions Jetpack 库**仍为 Alpha、无 GA 日期**，Gemini 集成仍「受信任测试者私测」。compileSdk 推荐基线由本库 08-03 记的 `≥ API 36` 升为 **37**（targetSdk 36），第三方复核（androidboss，Reviewed 2026-09-06）给出 `androidx.appfunctions:appfunctions:1.0.0-alpha11` + KSP 当前组合，并提示「alpha 版本常变、发布前复查 release page」。→ 含义：「框架进 OS 主版本」≠「API 稳定」，开发者仍须按 alpha 节奏跟版本（延续本笔记「AppFunctions 何时 GA 待补」待办）。
- **Windows ODR Agent Connectors 权限模式具象化（★6/10）**：第三方教程（adersaytech，聚合 learn.microsoft.com + 支持文档）披露，自预览 build **26100.7344+**，所有 ODR 注册的 agent connectors（本质是 MCP server）**默认在 Agent Workspace 隔离环境内执行**，Windows 先取得用户许可才让 agent 运行连接器；consent 三档 **Ask every time / Allow always / Never allow** 与 07 月「scoped file access 六文件夹 + 三档同意」同构，本次补的是「连接器」维度的同构三档。与 08-05 `odr.exe agent-info` 注册 + 09-16 代码签名构成「注册 → 签名 → 隔离 → 授权」闭环。⚠️ 第三方教程，build 号与三档模式待 Microsoft 官方文档逐字复核。

### ② 系统安全与用户体验（Confirmation / 隔离 / 防注入）

- **SIR 自改进 XPIA（★6/10，执行安全研究新机制）**：香港中文大学 arXiv 预印本（经 notatechguy 二次转述，2026-09）提出 **SIR（Self-Improving attack on computer-use agents）**——把提示注入当「bug bounty」跑：失败→诊断为何→把绕过提炼为命名策略→复用于后续任务，是首个把注入当**可演化攻击框架**处理的工作。量化（二次来源，待一手 arXiv 复核）：无迭代反馈时 ASR 为 Gemini 3.5 Flash 0% / Claude Opus 4.8 4%；加迭代反馈后升至 28% / 24%——攻击成功率可经自我试错被「训练」出来。更关键的性质 = **跨模型迁移**：在一款模型上发现的绕过原则，零额外反馈直接迁移到不同架构的另一款模型，意味着防御问题不是模型特定的、是系统性的（与 08-09晚 NCSC「confused deputy / 架构缺陷非可修 bug」定性同构）。目标层为 **OS 级 CUA（computer-use agent）**——看屏幕 + 真实 OS 操作，oracle 用文件系统/服务/权限状态作确定性判定，攻击在 agent 完成合法任务的同时并行发生、用户无感。→ 对 OS Agent 执行安全的含义：① 固定手写注入基准低估自适应对手，评测须用演化式红队；② 与 [[Agent Workspace 隔离执行]]「隔离压爆炸半径」范式一致——注入不可避免且会自我进化，**权限最小化 + 文件系统/服务边界**比「检测注入」更根本；③ 与 08-01 文档型 XPIA 自传播蠕虫、08-03 ADI 数据注入共同构成「注入会繁殖 / 不靠指令 / 会自我进化」三重递进。⚠️ 诚实标注：来源为二次转述，具体 arXiv ID 与评测协议待补；论文仅点名两款模型（Gemini 3.5 Flash / Claude Opus 4.8），第三款 CUA 未具名。
- **Windows 权限模式与 XPIA 风险同源**：adersaytech 教程直引官方警告——XPIA 让攻击者不必碰设备，只需让 agent 读到一份夹带恶意指令的文件/UI 元素即可劫持；隔离解「出事后能搞多大」、不解「会不会出事」。与 [[XPIA 跨提示注入]] 元判断「假定注入必然发生，用边界压爆炸半径」一致。

## 索引（每条 1 行：重要性 + 原子笔记 + 枢纽 + 一手来源）

- ★★★☆ **XPIA 攻击侧首次「自改进」范式 SIR（CUA 级、跨模型零反馈迁移、ASR 0%→28%）** → [[XPIA 跨提示注入]]（#执行安全）｜ 来源 <https://www.notatechguy.com/prompt-injection-attack-on-ai-agents-jumps-to-28-success>（二次转述，arXiv 待补）
- ★★★☆ **Windows ODR Agent Connectors 权限模式具象化（build 26100.7344+，默认隔离 + 三档 consent）** → [[Windows Copilot Actions 与 Agent Workspace 2026]] ＋ [[Agent Workspace 隔离执行]]（#执行安全）｜ 来源 <https://adersaytech.com/ai-tutorial/windows-ai-agent-permissions.html>（第三方教程，官方 build 号待核）
- ★★★☆ **Android 17 GA 确认 + AppFunctions 进 Android 17 智能系统叙事（仍 alpha11、compileSdk 37）** → [[Android AppFunctions 设备侧意图 2026]]（#语义路由）｜ 来源 <https://developer.android.com/ai/intelligence-system> + <https://developer.android.com/blog/posts/android-17-is-here>

## 已复核·无净新增（避免重复检索）

- **Apple**：iOS 27 GA（09-14）后**无新 App Intents API**；官方「What's New in iOS 27」页 App Intents 段落仅列 WWDC26 已宣布、本次 GA 落地的能力（Entity/Intent schemas、View Annotations、App Intents Testing、Foundation Models 多模型路由），**无 WWDC 之外全新 API**。IntentValueRepresentation / RelevantEntities / EntityCollection 等 Schema 类型本笔记 08-01/08-02 已覆盖，非本期新增。
- **Android**：AppFunctions Jetpack 仍 **alpha11**（2026-08-26 官方 Release Notes），窗口内**无 alpha12**（androidboss 2026-09-06 复核 + 官方 release page 一致）；Android 17 官方博客重申 AppFunctions = 设备端 MCP、调用需 `EXECUTE_APP_FUNCTIONS`——与既有结论一致，非新 API。compileSdk 建议升 37（targetSdk 36）为版本基线上调，非 API 变更。
- **HarmonyOS**：Intents Kit / ArkAF 2.0 / A2UI 框架同 HDC2026 / 09-07 消费版，**无新意图框架 API**；小艺任务 / 导航条主动服务 / 碰一碰为消费者 UX 落地（已录 09-15），API 26 已确认（09-13）。
- **Windows**：Copilot Actions / Agent Workspace / ODR / Agent Launchers 四支柱 + IFA 2026 Execution Containers **无新 Registry API**；09-17 记的 ODR 权限模式为第三方教程对既有「受控发现 + 用户授权」原则的具象化，非新 API。
- **跨平台 BFCL v4**：BenchLM 2026-09-08 公开快照 **Qwen3.7 Max 75.0% 领先**，与历次快照一致（Ling 3.0 Flash 73.0% / LFM2.5-2.6B 56.9% 等），**榜单无净变化**；Needle 2（42.6% BFCL v4 单轮）/ Apple FM（61.7%）/ FunctionGemma（46.1%）分数稳定，待 Berkeley 官方榜复核。MiniCPM5-2B（66.60，09-08/09-09 开源）已录于 09-13，本窗口无新端侧 Planner 评测增量。

## 日间补充（2026-09-17 22:38 二次巡查，窗口 09-17 09:00 → 22:38）

> 自动化 09:00 主跑已覆盖 09-16→09-17 09:00。本次为当日夜间巡查，确认主跑结论未变，并补 1 条当日新出现的执行安全研究增量。

- **四大 OS 官方框架层仍无净新增 API（二次确认）**：Apple / Android / HarmonyOS 当日搜索无新框架结果；Windows 仅一条无关 Defender 杀毒 KB（非 agentic）。维持「OS 框架不日更」结论。
- **BFCL v4 榜单未变（数据版本 20260913）**：DataLearner 镜像的官方 Berkeley 榜本窗口无新端侧 Planner 模型入榜；第三方 anotherwrapper「Llama 3.1 405B #1 88.5%」与权威 Berkeley 镜像方法论冲突、且为 2024 模型，标待补、不计入。
- ★★★☆ **【新】自修改 Agent 让注入获得「持久化」——权重级攻击面（Irregular/IDC，Zicos/CSO 二次转述 09-17）** → [[XPIA 跨提示注入]]（#执行安全）｜ Agent 能改自身模型权重时，注入可沉淀进 checkpoint 跨会话存活（权重可改性 42% vs API-only 0%）；与晨间 SIR 自改进攻击构成 XPIA 演进链第四环，直接撞击「端侧/自托管 Agent 执行总线」权重边界。来源 <https://en.zicos.com/tech/i32759314-Self-modifying-AI-agents-expose-a-blind-spot-in-enterprise-security.html>（二次转述，Irregular 一手报告待补）

> [!note]
> 概念节点：[[Intent Schema Protocol 意图模式规范]] ｜ [[Intent Router 语义路由]] ｜ [[Function Calling 端侧工具调用]] ｜ [[Confirmation UI 安全机制]] ｜ [[Atomic Service 元服务]] ｜ [[Agent Workspace 隔离执行]] ｜ [[A2A 端侧智能体协议]] ｜ [[XPIA 跨提示注入]]
