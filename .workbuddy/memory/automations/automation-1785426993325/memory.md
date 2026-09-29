---
automation: AppIntent 每日情报（自动化 09:00 版，实际按 7 日滚动窗口运行）
last_run: 2026-09-26
window: 2026-09-25 → 2026-09-26
---

# 执行摘要（2026-09-21）

## 本轮产出（窗口 2026-09-20 21:00 → 09-21 22:00，约 25h）
- **四大 OS 官方框架层 API 无净新增**（iOS 27.1 beta 已放出、Duo 向无 Schema 新增；AppFunctions 仍 alpha11 无 alpha12；HarmonyOS HC2026 为既有框架数据补强；Windows 四支柱 + Execution Containers 无新 Registry API）。与 09-18→09-20 连续「OS 框架不日更」结论一致。
- **真增量①（★7/10，既有节点数据补强）：HC2026 鸿蒙智能体框架 2.0 端云混合规划 90%+ 成功率 + 生态数字** → 华为全联接大会2026（9-17 开幕、9-19~21 集中报道）官方口径：端云混合规划（任务复杂度+设备资源分配计算）把复杂任务成功率推至 90%+（四平台首个 OS 厂商量化端云协同规划成功率）；生态：HarmonyOS 6|7 终端破 8500 万、注册开发者 1100 万+、应用与服务 40 万+、接入 AI 开放能力应用 1 万+、日均调用 36.8 亿次、OpenHarmony 13 亿+；Skill 确定性/A2A 多轮 + 端/云双模；端侧文本搜图不出端（provenance-at-source 信号，不推翻来源轴空白）。补 [[HarmonyOS Intents Kit 与 ArkAF 2026]]。
- **真增量②（★6/10，新攻击面）：BragJack「Prompt Forcing」浏览器扩展劫持 AI 助手信道** → Forever Security Gal Weizman（09-16 公开）：单一恶意扩展经 Chromium DNR 跨入 AI 助手特权控制平面，CVE-2026-0628（Chrome 8.8，143.0.7499.192/.193 修）/CVE-2026-55945（Edge race condition）。区别于 prompt injection（控制完整 prompt，绕过模型过滤）。与 08-09晚「confused deputy」同构。补 [[XPIA 跨提示注入]]（威胁模型扩展至第⑧支·信道/身份信任劫持）。
- **真增量③（★6/10，治理层）：Microsoft Foundry 托管智能体网络出网控制 public preview** → FQDN 通配 + 允许/拒绝/改写出站头/改写目的地，与「发布到 M365/Teams GA + Agent 365 启用停用」构成治理闭环。补 [[Agent 365 与 Entra Agent ID 智能体控制平面与身份基座 2026]]（出网边界维度，非 OS 执行总线）。
- **真增量④（★5/10，低置信）：Android App Functions Manager「safety cage」** → ai.jp.net 二次分析称 Google 在 App Functions Manager 框架层嵌入 agent 安全护栏，仅开发者文档/SDK 注释暗示，待官方复核（可能=既有 AppFunctionState 门控复述）。补 [[Android AppFunctions 设备侧意图 2026]]。
- **真增量⑤（★5/10，强化 09-20 主题）：Plugin4Shell** → Claude Code/Codex/Copilot/Gemini CLI 零点击 RCE，绕过 SHA pinning 经 Git branch/commit 碰撞，强化 Skill/插件供应链投毒靶面。补 [[XPIA 跨提示注入]]。
- **窗口外校正（★5/10，关闭 09-20 前瞻待办）：iOS 27.1 beta 已放出** → Xcode 27.1 Beta 1（约 09-18/19）含 iOS 27.1 SDK，内容=iPhone Duo 折叠屏适配，无新 App Intents Schema API；代码级 Model Delegation API 反编译信号（外部模型可作 Siri 扩展，非官方）。补 [[Apple AppIntents Schema Protocol 2026]]。
- **落库**：A 索引 [[AppIntent 每日情报 2026-09-21]]、D 速览 [[AppIntent 每日情报速览 2026-09-21]]、B 既有增补 5（鸿蒙/XPIA×2/Agent 365/Android/Apple）、看板「本次新增（2026-09-21）」已登记。**0 新建 B 节点**。
- **环境**：未调用 Horizon MCP（环境仅 `agent-mail` 连接器在线）；按任务 fallback 改用 WebSearch/WebFetch 直查官方源与权威媒体。**HC2026 数字、BragJack CVE、Foundry 出网控制均来自官方/媒体转述，待一手复核**。

## 诚实标注 / 待办
- HC2026 生态数字与「端云混合规划 90%+」为华为官方口径经媒体转述；「端云混合规划」算法、端侧文本搜图字段、星河互联是否接意图回路待华为开发者文档逐字。
- BragJack 为 09-16 公开、09-20 周报覆盖，非本窗口 24h 首发；CVE 编号/修补版本来自 Forever Security 转述；Opera Neon/Comet/Claude-in-Chrome 修补状态部分未确认；Plugin4Shell 一手 CVE 与版本清单待补。
- iOS 27.1 beta 功能来自开发者博客/媒体转述；Model Delegation 为 pdfu 反编译、Apple 未官方确认；Android「safety cage」为二次分析。
- 跟踪：iOS 27.1 正式 beta 是否带新 Schema API；AppFunctions alpha12；把 BragJack Prompt Forcing 与 [[隔离执行]]/[[确认机制]] 映射；Per-Intent Privacy Manifest 官方逐字 / Watch OS 26 / NowSecure / AgentAntibody / Chrome Origin Sets / 高通 NPU exact specs / Berkeley 官方 BFCL v4 博客 / Skill-Inject 一手数字。

# 执行摘要（2026-09-20）

## 本轮产出（窗口 2026-09-18 21:00 → 09-20 21:00，约 48h，iOS 27 GA 后第 6 日）
- **四大 OS 官方框架层 + BFCL v4 官方榜（Last Updated 仍 2026-04-12）均无 48h 净新增 API / 评测**——完全符合「OS 框架不日更」规律，与 09-13→09-19 连续结论连续一致。本期为**复核型运行 + 库内空白补漏**。
- **真增量①（★6/10，库内空白补漏）：技能层供应链投毒成实证攻击类** → Skill-Inject（arXiv 2602.20156）/ Malicious Agent Skills in the Wild（arXiv 2602.06547，分析 ~100,000 skills）/ SkillJect（arXiv 2602.14211）三篇 2026-02 arXiv 实证，把「恶意 Skill/manifest 注入」从概念警告推为可测攻击类，直接映射 HarmonyOS ArkAF Skills 上架 / Android AppFunctions agent skill / A2A。补 [[XPIA 跨提示注入]]（威胁模型扩为「能力描述(Skill)注入」靶面，防御谱七支）+ [[Agent Skills 技能范式 2026]]（实证 + Skill manifest 签名护栏）。
- **真增量②（★6/10，库内空白补漏）：XPIA 防御侧量化** → PromptArmor（ICLR 2026）现成 LLM 检测/净化注入 AgentDojo FP/FN<1%；Zylos 2026 间接注入对最强前沿模型仍 ~32% 成功率（量化天花板）。补 [[XPIA 跨提示注入]]。
- **窗口外前瞻（★5/10，未发布）：iOS 27.1 首个 beta 预期 2026-09-21~23**（Macworld 09-20 仍确认未发布）；Messages「加到提醒事项/备忘录」= App Intents 主动式分发面扩大。已登记为下一窗口头号跟踪项。补 [[Apple AppIntents Schema Protocol 2026]]。
- **落库**：A 索引 [[AppIntent 每日情报 2026-09-20]]、D 速览 [[AppIntent 每日情报速览 2026-09-20]]、B 既有增补 3（XPIA / Agent Skills / Apple）、看板「本次新增（2026-09-20）」已登记。**0 新建 B 节点**。
- **环境**：未调用 Horizon MCP（环境仅 `agent-mail` 连接器在线）；按任务 fallback 改用 WebSearch/WebFetch 直查官方源与权威综述。Skill-Inject/Malicious Skills/SkillJect/PromptArmor/Zylos 具体数字来自 arXiv/厂商综述转述，待一手复核，先不写精确百分数（诚实）。

## 诚实标注 / 待办
- Skill-Inject / Malicious Skills / SkillJect / PromptArmor / Zylos 具体 benchmark 数字待一手论文页复核。
- 跟踪 iOS 27.1 beta（预期 09-21~23）是否引入新 `@AppIntent(schema:)` / App Intents Domains API；跟踪 AppFunctions alpha12。
- 把 Skill-Inject 等一手数字与「OS 级 Skill Registry 签名」机制做映射表。
- 沿用：OWASP Agentic AI Top 10 2026 映射 / Berkeley 官方 BFCL v4 榜逐字 / Watch OS 26 / NowSecure / AgentAntibody / Chrome Origin Sets / Per-Intent Privacy Manifest / 高通 NPU exact specs。

# 执行摘要（2026-09-18）

## 本轮产出（窗口 2026-09-17 22:38 → 09-18 21:00，约 22h，iOS 27 GA 后第 4 日）
- **四大 OS 官方框架层 + BFCL v4 榜单 + XPIA 研究线本窗口（24h）均无净新增 API / 评测 / 研究突破**——完全符合「OS 框架不日更」规律，与 09-17（含 22:38 日间补充 SIR + 权重级持久化）结论连续一致。本期为**复核型运行**：把「已复核·无净新增」显式落档，避免下次重复检索。
- **唯一低于收录阈值的状态更新（★5/10，不入新 B 节点）**：Windows Copilot Actions 经 msftnewsnow 报道已随 Copilot app 更新 **1.25112.74+** 向 Insiders 分批「Now Available」——属已记录预览能力的部署推进，非框架 API 新增；已追加 1 行状态至 [[Windows Copilot Actions 与 Agent Workspace 2026]]。
- **关键校正**：Apple `iOS 27.1` 首个 beta **尚未发布**（Macworld 09-18 确认），短期无新 App Intents API 信号；搜索命中的 7 篇 iOS 27 文章全部为 09-14 GA 后的二次复述。
- **去伪**：OWASP Agentic AI Top 10 2026 经多源确认 **2025-12-09 发布**（版本号指治理年份，非本期新发布）；Microsoft RAMPART 为 XPIA 测试框架工件（非 OS 机制变更）；dev.to 云端 Copilot（SharePoint 技能/Brand Kit）为应用层、丢弃。
- **落库**：A 索引 [[AppIntent 每日情报 2026-09-18]]、D 速览 [[AppIntent 每日情报速览 2026-09-18]]、B 既有增补 1（Windows 部署状态 1 行）、看板「本次新增（2026-09-18）」已登记。**0 新建 B 节点**。
- **环境**：未调用 Horizon MCP（环境仅 `agent-mail` 连接器在线，无 Horizon MCP 工具）；按任务 fallback 改用 WebSearch/WebFetch 直查官方源，已记于 A 索引诚实标注。

## 诚实标注 / 待办
- Windows Copilot Actions app v1.25112.74+「Now Available」报道未给精确发布日期，无法确认是否严格落在 24h 窗口，仅作状态更新处理。
- OWASP Agentic AI Top 10 2026（ASI01–ASI10）与 RAMPART 一手发布日期待补；建议后续把 ASI 十类与库内 [[XPIA 跨提示注入]] / [[Confirmation UI 安全机制]] / [[Agent Workspace 隔离执行]] 做映射表（非本期增量）。
- 跟踪 iOS 27.1 beta（预期 10 月）是否引入新 App Intents API；跟踪 AppFunctions alpha12。
- 沿用既有待办：Berkeley 官方 BFCL v4 榜逐字 / Watch OS 26 / NowSecure / AgentAntibody / Chrome Origin Sets / Per-Intent Privacy Manifest / 高通 NPU exact specs / SIR 一手 arXiv / Irregular 一手报告。

# 执行摘要（2026-09-17）

## 本轮产出（窗口 2026-09-16 → 09-17，iOS 27 GA 后第 3 日）
- **四大 OS 官方框架层无净新增 API**（iOS 27 GA 后无新 App Intents；AppFunctions 守 alpha11 无 alpha12；HarmonyOS 同 HDC2026；Windows 四支柱 + Execution Containers 无新 Registry API），符合框架不日更规律，已在 A 层显式列「已复核·无净新增」避免重复检索。
- **真增量①：XPIA 攻击侧首次「自改进」SIR（★6/10）** → 香港中文大学 arXiv 预印本（notatechguy 二次转述）：把提示注入当可演化攻击框架，ASR 经自我试错 Gemini 3.5 Flash 0%→28% / Claude Opus 4.8 4%→24%，且绕过原则跨模型零反馈迁移；与 08-09 AgentAntibody 形成攻防镜像。补 [[XPIA 跨提示注入]]。
- **真增量②：Windows ODR Agent Connectors 权限模式具象化（★6/10）** → 第三方教程（adersaytech）：预览 build 26100.7344+ 起 ODR 连接器默认关进 Agent Workspace、consent 三档（Ask every time / Allow always / Never allow），与 08-05 注册 + 09-16 代码签名构成「注册→签名→隔离→授权」闭环。补 [[Windows Copilot Actions 与 Agent Workspace 2026]]。
- **真增量③：Android 17 GA 确认 + AppFunctions 进智能系统叙事（★6/10，库内空白补漏）** → 官方 intelligence-system 页把 AppFunctions 与 Remote MCP / Computer Control 并列；AppFunctions 仍 alpha11 无 alpha12、compileSdk 建议升 37。补 [[Android AppFunctions 设备侧意图 2026]]。
- **落库**：A 索引 [[AppIntent 每日情报 2026-09-17]]、D 速览 [[AppIntent 每日情报速览 2026-09-17]]、B 既有增补 3（XPIA/Windows/Android）、看板「本次新增（2026-09-17）」已登记。**0 新建 B 节点**。

## 日间延续巡查（2026-09-17 22:38，窗口 09-17 09:00→22:38）
- **结论维持**：四大 OS 官方框架层无净新增 API（Apple/Android/HarmonyOS 当日搜索空；Windows 仅无关 Defender KB）；BFCL v4 榜数据版本仍为 20260913、无新端侧 Planner 入榜（anotherwrapper「Llama 3.1 405B #1 88.5%」与权威镜像冲突、标待补）。
- **真增量（1 条，★6/10）**：「自修改 Agent 让注入获得持久化——权重级攻击面」（Irregular/IDC，Zicos/CSO 二次转述 09-17）→ 补 [[XPIA 跨提示注入]]：Agent 能改自身模型权重时，注入可沉淀进 checkpoint 跨会话存活（权重可改性 42% vs API-only 0%），与晨间 SIR 自改进攻击构成 XPIA 演进链第四环，直击端侧/自托管 Agent 执行总线权重边界。A 索引补「日间补充」小节、看板补 1 行、本记忆补本段。**0 新建 B 节点**。
- 诚实标注：Irregular 为二次转述，42%/3-of-6 密钥复现为测试条件数字，一手报告待补（已加进待办）。

## 诚实标注 / 待办
- SIR 为 notatechguy 二次转述，arXiv ID 与评测协议待一手复核；仅点名 Gemini 3.5 Flash / Claude Opus 4.8 两款模型。
- Windows ODR 权限模式 build 26100.7344+ 与三档 consent 为第三方教程，待 learn.microsoft.com 逐字复核；是否受 08-02 `Experimental agentic features` 同一 opt-in 管控待补。
- Android 17 精确 GA 日 + AppFunctions GA 日待补；compileSdk 37 为第三方复核结论。
- 沿用：Per-Intent Privacy Manifest 官方文档逐字 / Watch OS 26 / NowSecure / AgentAntibody / Chrome Origin Sets / 高通 NPU exact specs。

# 执行摘要（2026-09-16）

## 本轮产出（窗口 2026-09-15 → 09-16，iOS 27 GA 后 1 日）
- **四大 OS 官方框架层无净新增 API**（iOS 27 GA 后无新 App Intents；AppFunctions 守 alpha11 无 alpha12；HarmonyOS 同 HDC2026；Windows 四支柱无新 Registry API）。符合框架不日更规律，已在 A 层显式列「已复核·无净新增」避免重复检索。
- **真增量①：Windows Agent 代码签名/吊销由第三方升官方确认（★6/10）** → learn.microsoft.com agentic security 文档把「Operational trust」列为四大原则之一（Agent 须可信源签名、证书校验/吊销可阻断）；09-15 仅 windowsforum 第三方，本次获官方背书。补 [[Windows Copilot Actions 与 Agent Workspace 2026]] + [[Agent Workspace 隔离执行]]。
- **真增量②：Per-Intent Privacy Manifest 官方页重核（★3/10）** → 重核 developer.apple.com/ios/whats-new，App Intents 段落仍无此 API；维持 09-15「GA 后待官方复核」、来源轴空白结论不变。补 [[四平台意图 Registry 来源轴与权限模型对比 2026]]。
- **真增量③：跨平台硅底新信号 NPU 原生 agentic loop（★3/10，新 B 节点）** → 高通 Hexagon on-die agentic loop（感知→Oryon CPU 编排→异构推理→响应）+ 联发科 Dimensity 9500S CIM/1.58-bit；端侧 Agent 执行总线下沉芯片。新建 [[端侧 Agent 执行总线 NPU 原生 agentic loop 2026]]。
- **库内空白补漏：Android I/O '26 路由/编排原语（★3/10）** → Firebase Hybrid Inference 端云路由 / ADK for Android 多智能体 / A2UI Compose Renderer，补 [[Android AppFunctions 设备侧意图 2026]]，标真实日期 I/O '26。
- **落库**：A 索引 [[AppIntent 每日情报 2026-09-16]]、D 速览 [[AppIntent 每日情报速览 2026-09-16]]、B 新 1 + B 既有增补 3、看板「本次新增（2026-09-16）」已登记。

## 诚实标注 / 待办
- Windows 代码签名/吊销是否纳入 ODR 信任链、是否受 08-02 同一 opt-in 管控仍待 learn.microsoft.com 逐字（官方只确认原则，未给注册衔接）。
- Per-Intent Privacy Manifest 仍缺 Apple 官方文档逐字（多源报道未证伪、官方页未列，维持待复核）。
- 高通 NPU exact specs 待 Snapdragon Summit 2026 官方确认（当前为 keynote 前披露经第三方转述）。
- 鸿蒙 小艺导航条「复制即触发」置信度门控机制待官方文档；BFCL v4 官方榜复核 Needle 2/Apple FM/FunctionGemma 待补；沿用既有待办：Watch OS 26 / NowSecure / AgentAntibody / Chrome Origin Sets。

# 执行摘要（2026-09-15）

## 本轮产出（窗口 2026-09-13 → 09-15，真·GA 窗口）
- **iOS 27 正式版（09-14）GA 落地的框架级信号（★8/10）= 本日最高价值**：官方 post-GA「What's New in iOS 27」页确认 App Intents 能力（Entity/Intent schemas、View Annotations API、App Intents Testing，均为 WWDC26 已宣布、本次 GA）——**关键增量 = Foundation Models 框架宣布支持任意语言模型**（Apple FM / Claude / Gemini / 任何遵循 `Language Model` 协议者）+ Dynamic Profiles（连续会话实时切换模型/工具）+ Evaluations。**OS 级 Planner 首次把多模型路由写进一等公民框架**，端云路由从架构决策降为运行时旋钮。
- **最高优先待办收口进行中：Per-Intent Privacy Manifest 由「证伪」重开为「GA 后待官方复核」**：08-31 判定该 API「confirmed non-existent」；GA 后 WWDC 2026 多源（Lushbinary/ByteIota/TechTimes/AlgeriaTech）一致称 Apple 引入按意图声明「可上云/须留端」的隐私清单，但官方 post-GA 页未逐字列出 → 由证伪升为待复核。即使确认，属「路由轴」声明，与 provenance 轴不同，**不推翻来源轴全空白结论**。
- **Windows：Agent 代码签名 + 证书校验/吊销（★6/10）**：执行安全三原则（non-repudiation/confidentiality/authorization）落地细节补全，把「Agent 须数字签名」升级为可撤销身份机制（第三方 windowsforum 综述，非官方逐字）。
- **HarmonyOS 7 小艺 2.0 / 导航条主动服务入消费者（★6/10）**：系统级 Agent 感知 200+ 系统数据 / 调用 2100+ 系统能力 / 四层记忆；导航条「复制即触发意图预测」是四平台首个系统化 OS 级主动服务 UX。生态：HarmonyOS 7(API 26) 设备占比 5.27%、鸿蒙 6+7 终端破 8500 万。媒体口径。
- **BFCL v4 榜单稳定**（BenchLM 09-08：Qwen3.7 Max 75.0% 领先，与历次快照一致，无净变化）；qwen3-0.6b-tool-router 补 BFCL 子集分（Non-Live Parallel AST 83.50% / Live Simple 62.86% / Live Parallel 52.00%）。
- **落库**：A 索引 [[AppIntent 每日情报 2026-09-15]]、D 速览 [[AppIntent 每日情报速览 2026-09-15]]、B 既有增补 6（Apple/四平台对比/Windows/Agent Workspace隔离/HarmonyOS/Function Calling）+ 关联增补 1（Agent Workspace隔离）、看板「本次新增（2026-09-15）」已登记。**0 新建 B 节点**。

## 诚实标注 / 待办
- Per-Intent Privacy Manifest 仍缺 Apple 官方文档逐字确认（developer.apple.com 隐私清单 / App Intents GA 文档）；若确认则评估「路由轴」维度（区别于 provenance）。
- Windows 代码签名/吊销仍待 learn.microsoft.com 逐字；是否纳入 ODR 信任链、是否受同一 opt-in 管控待核。
- 鸿蒙 小艺 2.0 / 导航条仅媒体整理，缺华为开发者文档逐字；导航条预测置信度门控机制待确认。
- Android 版本口径冲突（博客 alpha08/09/10 vs 官方 alpha11；「Android 17」ADB vs compileSdk ≥36）待官方澄清。
- 沿用：Watch OS 26 / NowSecure / AgentAntibody / Chrome Origin Sets 官方 URL 复核；Berkeley 官方 BFCL v4 博客原文。

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

## 执行摘要（2026-09-26）

## 本轮产出（窗口 2026-09-25 13:06→09-26 00:17，约 11h）
- **四大 OS 官方框架层 API 无净新增**（iOS 27.1 beta 无新 Schema / AppFunctions 守 alpha12 无 alpha13 / A2UI 守 alpha01 / HarmonyOS ArkAF 2.0 无新 API / Windows 26H2 四支柱 + 权限治理无新 Registry API）。
- **真增量①（★8/10，关闭 09-16 待办）：Snapdragon Summit 2026 收官发布 Snapdragon 8 Elite Gen 6** → Hexagon NPU 首增「面向 Transformer/Agentic AI 的 element-wise accelerator」+ 共享内存 +50% + 端上 32K context + 可跑 30B+ MoE（每 token 激活 ~3B，UFS 5.0 直接跑）；Oryon CPU FlexCache 作协调中柢。补 [[端侧 Agent 执行总线 NPU 原生 agentic loop 2026]]。
- **真增量②（★6/10）：MLPerf Edge Agentic 把 BFCL v4 纳为精度门** → 参考 Qwen3.6-27B（Q4_K_M）Jetson AGX Thor 单轮 gated 86.23%（≥83.64% 通过）；多轮 optional 非 gated（200 条=70%）。补 [[Function Calling 端侧工具调用]]。
- **状态行（★5/10）：鸿蒙 7.0.0.109SP6 正式版信号 + 小艺Work 跨设备 agentic 办公（含 Windows 客户端）**；**Windows 26H2 enablement 9 月下旬~10 月初 + Ask Copilot/File Explorer agentic 入口**。补 [[HarmonyOS Intents Kit 与 ArkAF 2026]] / [[Windows Copilot Actions 与 Agent Workspace 2026]]。
- **落库**：A 索引 [[AppIntent 每日情报 2026-09-26]]、D 速览 [[AppIntent 每日情报速览 2026-09-26]]、B 既有增补 4、看板「本次新增（2026-09-26）」已登记。**0 新建 B 节点**。
- **环境**：未调用 Horizon MCP（仅 `agent-mail` 在线）；按任务 fallback 改用 WebSearch/WebFetch 直查官方/权威源（高通 keynote 多源 / MLPerf GitHub / 华为媒体 / PCWorld）。

## 诚实标注 / 待办
- 高通规格为 keynote+媒体转述，TOPS/功耗以官方 whitepaper 为准；「30B MoE 端上跑」为演示口径。
- MLPerf 参考模型 Qwen3.6-27B 非最小端侧 Planner；其 gated 86.23% 与库内端侧小模型 BFCL 分数不可混算。
- 鸿蒙 7.0.0.109SP6 是否=正式版、小艺Work 执行机制（是否走元服务/意图回路）待华为开发者文档复核。
- 沿用：alpha12 `scope`/`serialize` 官方逐字段确认 / Per-Intent Privacy Manifest 官方逐字 / Watch OS 26 / NowSecure / AgentAntibody / Chrome Origin Sets / 高通 NPU exact TOPS / Berkeley 官方 BFCL v4 博客 / AppFunctions alpha13 / A2UI alpha02 / 26H2 精确 GA 日。

# 执行摘要（2026-09-25）

## 本轮产出（窗口 2026-09-21 22:00 → 09-25 13:00，约 3.5 天，距上次跑约 4 天）
- **四大 OS 官方框架层唯一净新增 = Android AppFunctions `1.0.0-alpha12`（2026-09-23）+ A2UI `1.0.0-alpha01`（同日常）**。AppFunctions 自 alpha11（08-26）以来首个版本进位，含多项 Registry/权限/执行上下文相关 API 变更。
- **真增量①（★7/10，官方直查 Release Notes）：AppFunctions alpha12 API 变更** → `scope` 字段加入 `AppFunctionMetadata`/`AppFunctionSearchSpec`（四平台首个官方 Jetpack 显式「作用域」维度，服务 Registry 可见性/权限模型）；`activityId` 加入 `ExecuteAppFunctionRequest`（执行上下文绑定）；`AppFunctionUriValueConstraint` 公共 API（Uri 参数级安全约束）；`AppFunctionData#serialize` 要求调用方提供元数据（可能为 provenance 信号但须谨慎）；运行时注册 API 标 `@ExperimentalAppFunctionsApi`；**破坏移除 `AppFunctionContext`/`AppFunctionConfiguration`**（首参身份注入对象被删）。补 [[Android AppFunctions 设备侧意图 2026]] + [[四平台意图 Registry 来源轴与权限模型对比 2026]]（scope 维度入表；来源轴全空白结论不变）。
- **真增量②（★6/10，官方 alpha-channel）：A2UI `1.0.0-alpha01` 官方落地 Android Jetpack** → `androidx.a2ui`/`a2ui.compose`/`material3-a2ui`，JSONL agent-defined UI 协议 + Material3 基础 catalog 13+ 组件（Button/Image/TextField/Slider/Modal 等），原生 Compose 渲染免任意代码。四平台首个官方 A2UI 库。补 [[A2UI 生成式UI协议(Google)与鸿蒙落地 2026]]。
- **真增量③（★6/10，生态补强）：鸿蒙 9-22 小艺接入淘宝闪购智能体「一句话点外卖」闭环 + 9-25 HarmonyOS 7 公测开放 + 数字（500+ 伙伴 Skills / 2000+ 鸿蒙智能体 / 2100+ 系统能力）**。补 [[HarmonyOS Intents Kit 与 ArkAF 2026]]。
- **状态行（★5/10，低于阈值）：统一 Copilot 桌面 app 9 月中旬铺开** → Chromium 架构、个人/工作账户合一，应用层分发变更非 OS API 新增。补 [[Windows Copilot Actions 与 Agent Workspace 2026]]。
- **落库**：A 索引 [[AppIntent 每日情报 2026-09-25]]、D 速览 [[AppIntent 每日情报速览 2026-09-25]]（spec 格式）、B 既有增补 5（Android/Registry/A2UI/HarmonyOS/Windows）、看板「本次新增（2026-09-25）」已登记。**0 新建 B 节点**。
- **环境**：未调用 Horizon MCP（环境仅 `agent-mail` 连接器在线）；按任务 fallback 改用 WebSearch/WebFetch 直查官方源（developer.android.google.cn/jetpack/androidx/releases/appfunctions、alpha-channel、compose-material3 release notes）与权威媒体（网易 9-25、simoncarter.ai）。alpha12/A2UI 为官方 Release Notes 直查确认。

## 诚实标注 / 待办
- alpha12 `scope` 语义（调用方可见性作用域 vs 功能分类域）、`serialize` 元数据字段定义待 developer.android.com/ai/appfunctions 官方文档逐字段确认；`scope` 是否=「可见性/权限作用域」在确认前不写入对比表正文（延续 08-31 纪律）。
- `serialize` 要求元数据可能是 provenance 信号但须谨慎——更可能是序列化结构元数据，未必等于 intent 来源 provenance；来源轴全空白结论不变。
- `AppFunctionContext`/`AppFunctionConfiguration` 移除后，调用方身份注入新机制待 alpha13+ 或官方指南；本笔记 08-03 开放问题「AppFunctionContext 是否携带可验证调用方身份」追问基础被削弱。
- A2UI alpha01 为首版，基础 catalog 组件集与字段稳定性待后续 release 复核（延续 08-26「A2UI 版本协商防静默空白」）。
- 小艺/淘宝闪购具体机制与闭环成功率、HarmonyOS 7 公测具体机型清单待华为开发者文档逐字复核（媒体口径）。
- 统一 Copilot app 为应用层变更非 OS 执行总线；26H2 GA 仍锚定 9 月下旬~10 月初。
- 跟踪：AppFunctions GA 日期；alpha13+ 身份注入机制；A2UI 后续 release；iOS 27.1 正式 beta 是否带新 Schema API；Per-Intent Privacy Manifest 官方逐字 / Watch OS 26 / NowSecure / AgentAntibody / Chrome Origin Sets / 高通 NPU exact specs / Berkeley 官方 BFCL v4 博客。

# 执行摘要（2026-09-25b · re-trigger 复核与补捕）

## 本轮产出（窗口 09-25 13:00 → 09-25 13:06，同日 re-trigger，约 6 分钟）
- **复核型运行 + 窗口内补捕**：对四大 OS 官方源二次核验，确认无新增 OS 框架层 API（无 AppFunctions alpha13 / iOS 27.1 新 `@AppIntent(schema:)` Schema / HarmonyOS 新 API / Windows OS 执行总线新 Registry API），与 09-25 主运行完全一致。
- **窗口内补捕（★5/10，治理层）**：Microsoft 365 Copilot **Declarative Agents 支持 Skills 转入 GA**（Message Center MC1476977，2026-09-22 公布，9 月中~月底全球铺开）。Skills 把指令/脚本/模板/资源打包为可复用模块、按需加载；脚本执行走**安全沙箱**、skill 文件上 **MIP 敏感度标签保留并生效**。与 [[Agent Skills 技能范式 2026]] / [[隔离执行]] / HarmonyOS Skills Framework / Android AppFunctions agent skill 构成跨平台「Agent Skill 上架 + 沙箱执行」范式对照。属 M365/Entra 治理层，非 Windows OS 执行总线。
- **落库**：既有 [[AppIntent 每日情报 2026-09-25]] 追加「复核与补捕」小节（不新建 A 文件）；[[Agent 365 与 Entra Agent ID 智能体控制平面与身份基座 2026]] 追加「2026-09-25 补捕」段；看板「本次新增（2026-09-25）」补 1 行。**0 新建 B 节点、0 新建 A/D 文件**。
- **环境**：同前，未调用 Horizon MCP，WebSearch 直查官方/权威源（developer.apple.com/documentation/updates、developer.android.com/ai/appfunctions、mwpro 对 MC1476977 转述）。

## 诚实标注 / 待办
- MC1476977 GA 日期与「安全沙箱 / MIP 标签」语法为 MWPro 对 Message Center 的转述（2026-09-22），待 learn.microsoft.com 逐字复核。
- 沿用 09-25 待办（alpha13 身份注入 / A2UI 后续 release / iOS 27.1 Schema / Per-Intent Privacy Manifest 官方逐字 / Watch OS 26 / NowSecure / AgentAntibody / Chrome Origin Sets / 高通 NPU / Berkeley BFCL v4 官方博客 / AppFunctions GA 日期）。

# 执行摘要（2026-09-26-晚）

## 本轮产出（窗口 2026-09-26 00:17→22:07，约 22h，晨间跑之后的日间延续）
- **四大 OS 官方框架层 API 仍零净新增**（iOS 27.1/27.2 双线无新 Schema / AppFunctions 守 alpha12 无 alpha13 / A2UI 守 alpha01 / HarmonyOS ArkAF 2.0 无新 API / Windows OS 执行总线四支柱无新 Registry API），与晨间跑「OS 框架不日更」连续一致。
- **真增量①（★6/10，M365 治理/执行层，非 OS API）：微软 09-25 Copilot 重架构** → Autopilot 常驻托管智能体（由 Scout 改名、自身身份/记忆/工作区）+ Copilot Managed Runtime 租户内沙盒托管运行时（npm @microsoft/managed-apps/-cli/-vite-plugin）+ 计费二分 USL/UBB。补 [[Agent 365 与 Entra Agent ID 智能体控制平面与身份基座 2026]] + [[Agent Workspace 隔离执行]]（Managed Runtime = SaaS 侧隔离执行样板）。
- **真增量②（★5/10，消费级实测补强）：鸿蒙小艺 9-26 评测数据** → CNMO 小艺 409 分登顶（领先 YOYO 30+）、中国电信四项第一、端侧盘古离线 12 秒会议记录、A2A 依托 2100+ 系统能力/500+ 伙伴 Skill。补 [[HarmonyOS Intents Kit 与 ArkAF 2026]]（评测机构/媒体口径，待华为文档核验）。
- **真增量③（★5/10，社区端侧实证）：Qwen3-0.6B Q4_K_M 在 2017 Note8（6GB）驱动真实桌面 Chrome** → 结构化页面感知层（~200 token）驱动、3 任务 10/10、结构化 500 token/80s vs 原始 HTML 12k token/22min。补 [[Function Calling 端侧工具调用]]（社区实验、非 BFCL、仅 3 固定任务）。
- **去伪**：Semantic Kernel CVE-2026-26030/25592（CVSS 9.9）经核查为 2026-05 已披露，非本窗口新 CVE；KOPA-BENCH（arXiv 2609.05395）新基准但非端侧 Planner 专项、低阈值丢弃。
- **落库**：A 索引 [[AppIntent 每日情报 2026-09-26-晚]]、D 速览 [[AppIntent 每日情报速览 2026-09-26-晚]]、B 既有增补 4（Agent 365 / Agent Workspace隔离 / HarmonyOS / Function Calling）、看板「本次新增（2026-09-26-晚）」已登记。**0 新建 B 节点**。
- **环境**：仅 `agent-mail` 在线，未调用 Horizon MCP，WebSearch/WebFetch 直查官方/权威源（微软 09-25 博文多源转述 / 网易 / 新浪 / 腾讯搜一搜 / 开发者社区）。

## 诚实标注 / 待办
- 微软 Copilot 重架构为官方博文（Spataro）多源转述，GA/预览日期与 Managed Runtime 沙箱语法待 learn.microsoft.com 逐字；Autopilot 9 月底私有预览、非 GA。
- 鸿蒙评测数字（409/四项第一/离线 12 秒）评测机构与媒体口径，待华为开发者文档核验。
- Qwen3-0.6B Note8 为 e2llm 社区仓库、仅 3 固定任务、非通用 benchmark，与其比端侧 Planner 准确率不严谨。
- 沿用：Per-Intent Privacy Manifest 官方逐字 / Watch OS 26 / NowSecure / AgentAntibody / Chrome Origin Sets / 高通 NPU exact specs / Berkeley BFCL v4 博客 / AppFunctions alpha13 / A2UI alpha02 / 26H2 GA 日 / iOS 27.1 正式 beta Schema / Managed Runtime 与隔离 SOP 跨厂商对照。
