---
date: 2026-09-20
tags: [AppIntent, 每日情报, 执行安全, 端侧Agent执行总线, 跨平台, 框架复核, Skills供应链投毒, XPIA防御]
source: "https://developer.apple.com/wwdc26/guides/ios/ | https://www.macworld.com/article/2986799/ios-27-features-compatiblity-siri-ai-updates.html | https://appauxin.com/ios-27-1-release-date | https://developer.android.com/ai/appfunctions | https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkaf-overview | https://msftnewsnow.com/windows-11-security-model-copilot-actions-ai-agent/ | https://learn.microsoft.com/fil-ph/windows/security/book/operating-system-agentic-security | https://www.vectra.ai/topics/prompt-injection | https://agentmelt.com/glossary/indirect-prompt-injection | https://www.linkedin.com/pulse/ai-security-research-february-2026-tal-eliyahu-zphie | https://gorilla.cs.berkeley.edu/leaderboard.html"
importance_score: "★★★☆"
intent_category: "框架复核·无净新增 + 库内空白补漏（Skills 层供应链投毒攻击类 + XPIA 防御侧 PromptArmor/Zylos）"
---

# AppIntent 每日情报 2026-09-20

> [!abstract]
> **30 秒速览（窗口 2026-09-18 21:00 → 09-20 21:00，约 48h）**
> - **核心结论**：**四大 OS 官方框架层本窗口（48h）仍无净新增 API**——完全符合「OS 框架不日更」规律，与 09-13→09-19 连续多轮结论连续一致。本期为**复核型运行 + 库内空白补漏**：框架层无新增，但检索首次把两类高价值、此前未入库的研究补进对应 B 节点（★6/10）。
> - **真增量①（★6/10，库内空白补漏）：技能层供应链投毒成实证攻击类** —— Skill-Inject（arXiv 2602.20156）/ Malicious Agent Skills in the Wild（arXiv 2602.06547，分析 **~100,000 个 skills**）/ SkillJect（arXiv 2602.14211）三篇 2026-02 实证研究，把「恶意 Skill / manifest 注入」从概念警告推为可测攻击类，直接对应 HarmonyOS ArkAF Skills 上架、Android AppFunctions agent skill、A2A 分发层。补 [[XPIA 跨提示注入]] + [[Agent Skills 技能范式 2026]]。
> - **真增量②（★6/10，库内空白补漏）：XPIA 防御侧量化补强** —— PromptArmor（ICLR 2026）用现成 LLM 检测/净化注入，AgentDojo 上 **FP/FN <1%**；Zylos 2026 基准显示即便开全部厂侧缓解，间接注入对最强前沿模型仍有 **~32% 成功率**（量化天花板）。补 [[XPIA 跨提示注入]]。
> - **窗口外前瞻（★5/10，非净新增）：iOS 27.1 首个 beta 预期 2026-09-21~23 放出**（Macworld 09-20 仍确认「尚未发布」）；Messages「加到提醒事项/备忘录」任务建议 = App Intents 主动式能力分发面扩大。已登记为下一窗口头号跟踪项，未新建 B 节点。
> - **OS Agent 场景**：四平台 GA/预览均已落地（iOS 27 GA 09-14 / HarmonyOS 7 09-07 / Android 17 / Windows 26H2 在即）；本期净新增 = 0，价值在把「已复核·无净新增」+「Skills 层投毒新攻击类」显式落档。

## 正文拆解

### ① Schema 定义与语义路由机制

- **四大 OS 官方框架层本窗口无净新增 API（逐项复核）**：
  - **Apple**：`developer.apple.com/wwdc26/guides/ios` App Intents 段落自 GA 后未变；本轮搜索命中的 iOS 27 文章（macworld / braze / byteiota / scand / ecorpit / webpronews）均为 **09-14 GA 后的二次复述**——App Intents 成唯一 Siri 路径、SiriKit 弃用、App Intents 2.0（Streaming / multi-turn / View Annotations / App Schemas / App Intent Domains）、Foundation Models 多模型路由，全部为 WWDC26 已宣布 / 09-15 已录内容，**无 WWDC 之外全新 API**。**iOS 27.1 首个 beta 截至 09-20 21:00 尚未发布**（Macworld 09-20 确认），短期无新 App Intents API 信号。
  - **Android**：`developer.android.com/ai/appfunctions` 仍标 **Experimental 预览**，Jetpack 库**仍为 alpha（本库 09-01 录 alpha11，窗口内无 alpha12；androidboss 09-06 复核亦确认 alpha11）**；`EXECUTE_APP_FUNCTIONS` 权限 + `AppFunctionsManager` + `AppFunctionState` 三态为既有稳定文档。本轮命中的 InfoQ / zooz / androidboss 均为 I/O '26 旧文或 alpha 状态复述，无 24h 新增。
  - **HarmonyOS**：`developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkaf-overview` + `intents-access-flow` 为稳定文档，三层框架（意图框架 / Skills / 端侧 A2A）无新 API；搜索命中的 163 / ifanr / cbismb / sohu / softunis 均为 **HDC2026 / 09-07 消费版**旧文复述（Intelligent Agent Framework 2.0、intent-as-service、小艺 2100+ 系统能力、Ability Kit 工具/Skill/端侧 A2A），无 48h 净新增。
  - **Windows**：`learn.microsoft.com` agentic security 文档与 msftnewsnow / windowsnews.ai / windowsforum 的 Copilot Actions 报道为 08-02~09-18 已记录能力（Copilot Actions / Agent Workspace / ODR / 四安全原則 / 代码签名吊销）的**部署推进**，非框架 API 新增；positioniseverything / techbloat（09-19）的「Copilot 改为独立可缩放窗口、更谨慎集成」属 **UX/定位调整，无安全/框架层变更**，按规则丢弃（仅记为已复核）。
- **语义路由 / 端侧 Planner 评测线无 48h 新增**：Berkeley BFCL v4 官方榜（gorilla.cs.berkeley.edu）**Last Updated 仍停在 2026-04-12**，SOTA 维持 **MiniCPM5-2B 66.6（09-07）/ Spark-X2.5-4B 65.1（09-01）** 量级，窗口内**无新端侧 Planner 模型入榜**；aibacon（Needle 2 14MB ESP32）/ explainx.ai（Gemma 4 tool-call patch）/ ertas（Qwen3-4B vs Gemma4 E4B vs Phi-4-Mini 手机延迟）均为旧文或社区微调，非框架级新增。→ 端侧 Planner 评测表维持 09-13 后稳定态。
- **窗口外前瞻（★5/10）：iOS 27.1 beta 在即** —— 首个 developer beta 预期 **2026-09-21~23**（appauxin 引 MacRumors）；公开版随 iPhone Duo（折叠屏）**10-23** 预装、10-19~21 推全量。已知 27.1 与 App Intents 相关内容：**Siri AI 新增 5 语言**（法/日/韩/葡/西，本地化扩张非新 Schema）；**Messages 任务建议回炉**——对话触发「加到提醒事项/备忘录」= `reminders.createReminder` / `notes.createNote` schema 以**零短语主动建议**形态入 Messages（App Intents 主动式分发面扩大）；自动改密（Passwords App，走既有 Confirmation UI）。**当前所有 27.1 报道均未提新 `@AppIntent(schema:)` / App Intents Domains API**，预期为 GA 补全 + 本地化，非框架级新增。

### ② 系统安全与用户体验（Confirmation / 隔离 / 防注入）

- **真增量①（★6/10，库内空白补漏）：技能层供应链投毒成实证攻击类** —— 本库 [[Agent Skills 技能范式 2026]] 此前仅在「反例与边界」点到「恶意 Skill 注入」概念警告、在待办列「企业级 Skill 市场来源校验与签名」，缺实证。本期检索首次把该攻击类落到可量化研究（均 2026-02 arXiv，首次入库）：
  - **Skill-Inject（arXiv 2602.20156，Schmotz et al.）**：基准测主流 LLM agent 在**恶意指令嵌入 skill 文件**时的遵从率，证明被污染 skill 可让 agent 执行有害动作，暴露 **agent 生态新供应链攻击面**。
  - **Malicious Agent Skills in the Wild（arXiv 2602.06547，Liu et al.）**：分析 **~100,000 个 agent skills**，识别恶意行为与漏洞，揭示被污染 skill 可触发**多阶段攻击链（数据外泄 + agent 劫持）**。
  - **SkillJect（arXiv 2602.14211，Jia et al.）**：闭环反馈自动生成 stealthy 恶意 skill，主动提升注入有效性——攻击侧也能自我进化，与 09-17 SIR 同源。
  - **直接映射四平台 Skills / A2A 分发层**：HarmonyOS ArkAF 2.0 **Skills 上架**（端侧/云端同名冲突、A2UI Schema 版本兼容坑）、Android AppFunctions **agent skill**、A2A 协议——「Skill = 能力分发单位」机制正是 Skill-Inject 靶面；**OS 级 Skill Registry 若不做来源校验 + 签名，等于把供应链投毒面原样搬进系统层**。→ 补 [[XPIA 跨提示注入]]（新增「Skill manifest 来源校验」第⑦支防御）+ [[Agent Skills 技能范式 2026]]（实证 + 护栏）。
- **真增量②（★6/10，库内空白补漏）：XPIA 防御侧量化补强** —— 本库 XPIA 此前重攻击演进（蠕虫/ADI/SIR/权重持久化）+ 静态/学习型防御，缺「检测净化」派的实用精度与天花板数据：
  - **PromptArmor（ICLR 2026）**：用**现成 LLM**检测并移除注入指令，在 **AgentDojo 上 FP/FN 均 <1%**——把「检测净化注入」推到可实用精度，是 09-08「④ 学习型防御 AgentAntibody（边界免疫）」的**互补支**。来源：Vectra AI 综述转述。
  - **Zylos 2026 benchmark**：即便开**全部厂侧缓解（all lab-side mitigations）**，间接注入对**最强前沿模型仍有 ~32% 成功率**——给「检测/净化」派一个**量化天花板**：再好分类器也压不到 0，印证 08-09晚 NCSC「confused deputy / 架构缺陷非可修 bug」与 08-26「边界优先于检测」元判断。来源：Agentmelt 综述。
  - → 落回 [[XPIA 跨提示注入]] 结论：防御谱系现为**七支**（隔离 / 确认 / 数据视图隔离 / 学习型边界免疫 / 读写边界 / 权重完整性 / **Skill manifest 来源校验**），叠加 PromptArmor 类「检测净化」实用增强，但受 Zylos 32% 天花板约束、不能替代边界。
- **Windows UX/定位调整（★4/10，已复核·丢弃）**：positioniseverything / techbloat（09-19）称 Copilot 改为独立可缩放窗口、更谨慎集成（「web app bolted onto taskbar」感减弱），但**无安全/框架 API 变更**、无新 Registry 权限；msftnewsnow 复述的四安全控件（User Control / Agent accounts / Agent workspace / User Transparency）与 09-16 已录一致。仅记「已复核·无净新增」，不新建内容。

## 索引（每条 1 行：重要性 + 原子笔记 + 枢纽 + 一手来源）

- ★★★☆ **（库内空白补漏·★6/10）技能层供应链投毒成实证攻击类（Skill-Inject / Malicious Skills ~100k / SkillJect）** → [[XPIA 跨提示注入]] ｜ [[Agent Skills 技能范式 2026]]（#执行安全）｜ 一手 arXiv 2602.20156 / 2602.06547 / 2602.14211（经 LinkedIn Tal Eliyahu AI Security Feb 2026 综述）
- ★★★☆ **（库内空白补漏·★6/10）XPIA 防御侧量化：PromptArmor AgentDojo FP/FN <1% + Zylos 2026 间接注入 ~32% 成功率天花板** → [[XPIA 跨提示注入]]（#执行安全）｜ <https://www.vectra.ai/topics/prompt-injection> ｜ <https://agentmelt.com/glossary/indirect-prompt-injection>
- ★★☆☆ **四平台官方框架层 + BFCL v4 榜本窗口（48h）无净新增 API / 评测** → 已复核·无净新增清单见下 ｜ developer.apple.com/wwdc26/guides/ios · developer.android.com/ai/appfunctions · developer.huawei.com harmonyos-guides/arkaf-overview · gorilla.cs.berkeley.edu/leaderboard.html
- ★★☆☆ **（窗口外前瞻·★5/10）iOS 27.1 首个 beta 预期 2026-09-21~23；Messages「加到提醒事项/备忘录」= App Intents 主动式分发面扩大** → [[Apple AppIntents Schema Protocol 2026]]（#Apple）｜ <https://appauxin.com/ios-27-1-release-date> ｜ <https://www.macworld.com/article/2986799/ios-27-features-compatiblity-siri-ai-updates.html>
- ★★☆☆ **（已复核·丢弃·★4/10）Windows Copilot 改为独立可缩放窗口（09-19 UX 调整，无安全/框架 API 变更）** → [[Windows Copilot Actions 与 Agent Workspace 2026]]（#执行安全）｜ <https://www.positioniseverything.net/microsoft-is-updating-copilot-for-windows-again/>

## 已复核·无净新增（避免重复检索）

- **Apple**：iOS 27 GA（09-14）后**无新 App Intents API**；官方页仅列 WWDC26 已宣布、本次 GA 落地项。**iOS 27.1 beta 截至 09-20 21:00 尚未发布**（Macworld 确认），短期无新信号。搜索命中的 iOS 27 文章均为 GA 后复述。
- **Android**：AppFunctions Jetpack 仍 **alpha（alpha11，2026-08-26）**，窗口内**无 alpha12**；`EXECUTE_APP_FUNCTIONS` + `AppFunctionsManager` + `AppFunctionState` 为既有稳定文档。androidboss 09-06 复核亦确认 alpha11。
- **HarmonyOS**：Intents Kit / ArkAF 2.0 / A2UI 框架同 HDC2026 / 09-07 消费版，**无新意图框架 API**；命中文多为旧文复述。API 26 已确认（09-13）。
- **Windows**：Copilot Actions / Agent Workspace / ODR / 四安全控件 / 代码签名吊销**无新 Registry API**；09-19 仅 Copilot 窗口 UX 调整（丢弃）。
- **跨平台 BFCL v4**：官方榜 **Last Updated 2026-04-12**（停滞），SOTA 维持 MiniCPM5-2B 66.6 / Spark-X2.5-4B 65.1，窗口内**无新端侧 Planner 模型入榜**；Needle 2 / Gemma 4 patch / Qwen3-4B 均为旧文/社区微调。
- **XPIA 研究线**：本窗口无 24h 新发布；**真增量来自库内空白补漏**（Skill-Inject / Malicious Skills / SkillJect 三篇 2026-02 arXiv + PromptArmor ICLR 2026 + Zylos 2026），均为此前未入库内容，非 24h 新研究。
- **诚实标注**：本运行未调用 Horizon MCP（环境仅 `agent-mail` 连接器在线，无 Horizon MCP 工具）；改用 WebSearch/WebFetch 直查官方源与权威综述，符合任务 fallback 约定。Skill-Inject / Malicious Skills / SkillJect / PromptArmor / Zylos 具体 benchmark 数字来自 arXiv 预印本 / 安全厂商综述转述，待一手论文页复核，先不写入精确百分数。

> [!note]
> 概念节点：[[意图模式规范]] ｜ [[语义路由]] ｜ [[端侧工具调用]] ｜ [[确认机制]] ｜ [[元服务]] ｜ [[隔离执行]] ｜ [[A2A 端侧智能体协议]] ｜ [[XPIA 跨提示注入]]
