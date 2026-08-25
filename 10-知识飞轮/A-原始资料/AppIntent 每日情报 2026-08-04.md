---
type: daily-index
status: index
captured: 2026-08-04
window: "7 日滚动窗口 2026-07-29 → 2026-08-04"
intent_category: "端侧 Planner 评测口径 / 执行安全数据来源分级 / 端点侧 agent loop 检查"
importance_score: "★★★★☆（8/10，窗口内真增量 3 条：2 条口径级 8/10 + 1 条 7/10）"
tags: [AppIntent, 情报, 索引, 2026-08-04]
---

# AppIntent 每日情报 2026-08-04（索引）

> [!abstract]
> 本期两条核心均为**「口径级」而非「功能级」**增量：① **BFCL v4 换掉了「意图路由该怎么评」的标准**——权重重排为 Agentic 40% / Multi-Turn 30% / Live 10% / Non-Live 10% / Hallucination 10%，经典单轮只剩 20%，库内所有 v3 分数与 v4 不可同栏比较；端侧模型断崖（8B MoE 仅 49.7%，1B 级 25.1%，亚 1B 21%）。② **连续 3 日最高优先待办拿到第一个实质答案**——微软 Agent Governance Toolkit 公开数据溯源模式（六类来源枚举 + 四级分类 + 单调棘轮），但它是**开源治理工具包而非 Windows OS 内建**，同日复核确认 OS 层仍无数据来源分级。**最高价值判据**：ADI 的结论从「无人做」升级为「**已有可抄的成熟模型，四大 OS 尚未采纳**」——这是产品优先级问题，不是技术空白。

## 本期条目索引

| 重要性 | 条目 | 原子笔记（完整内容） | 主题枢纽 | 一手来源 |
|---|---|---|---|---|
| 8/10 | **BFCL v4 权重重构**：Agentic 40% / Multi-Turn 30% / Live 10% / Non-Live 10% / **Hallucination 10%（无合适工具时正确拒绝调用）**；AST + 状态转移评分；08-03 镜像站快照 9 模型（Qwen3.7 Max 75.0% → LFM2.5-8B-A1B 49.7% → MiniCPM5-1B 25.1% → LFM2.5-230M 21.0%）；库内 v3 分数（Bonsai 73.3%、qwen3-0.6b-tool-router 90.42%、Phi-4-mini 80 分段）**全部不可与 v4 同栏比较** | [[Function Calling 端侧工具调用]] · [[Local Agent Bench 端侧智能体基准]] · [[通用 AI Agent 评测基准 2026]] | [[端侧意图框架 学习笔记]] · [[Intent Router 语义路由]] | [Berkeley Gorilla 官方榜单](https://gorilla.cs.berkeley.edu/leaderboard.html) ｜ [benchlm.ai · BFCL v4 镜像](https://benchlm.ai/benchmarks/bfcl-v4) ｜ [dreaming.press · 权重拆解](https://dreaming.press/posts/berkeley-function-calling-leaderboard-bfcl-v4) |
| 8/10 | **微软 AGT 数据溯源模型**：来源六类枚举（`tool_output`/`api_response`/`agent_message`/`user_input`/`database`/`file`）+ 数据四级分类（`public→internal→confidential→restricted`）+ **单调棘轮**（只升不降）+ 两阶段策略门（`post_tool` / `pre_output`）+ 溯源父子链；显式对齐 **EU AI Act Article 10**（高风险条款 2026-08-02 起适用，与 Article 15 同日）。⚠️ **开源治理工具包（`agentmesh.governance`），非 Windows OS 能力** | [[数据溯源分级与单调棘轮]] · [[Agent Data Injection 数据注入攻击]] · [[Windows Copilot Actions 与 Agent Workspace 2026]] | [[App Infra 应用基建]] · [[意图框架·跨体系索引 MOC]] | [microsoft.github.io · data-provenance-model](https://microsoft.github.io/agent-governance-toolkit/compliance/data-provenance-model) |
| 7/10 | **Project Perception 进入公共预览**（08-03）：Defender for Endpoint **首次把 agent loop 三段流量（用户提示 / 工具调用 / 工具响应）当作可检查对象并在执行前阻断**——防线从「隔离」延伸到「检查」。微软同时明示**被投毒的 MCP 工具描述**可让「已授权」Agent 通过看似合法的调用泄露数据 | [[Windows Copilot Actions 与 Agent Workspace 2026]] · [[Agent Data Injection 数据注入攻击]] · [[Dual View 智能体数据视图隔离]] · [[XPIA 跨提示注入]] | [[MCP 与设备侧 MCP]] · [[端侧意图框架 学习笔记]] | [微软官方新闻室 · 07-28](https://news.microsoft.com/source/asia/2026/07/28/projectperception-2026) ｜ [TechRepublic · 公共预览确认](https://www.techrepublic.com/article/news-microsoft-project-perception-preview/) |

> 说明：本笔记为**索引**，不内联分析。每条信息的完整技术细节、字段清单、口径警示、待补项均在上方「原子笔记」链接中。

### 索引内保留细节（B 笔记未完整承载，防内容丢失）

仅条目 3 的产品形态层面细节，B 笔记只记录了其安全机制含义：

- **定位**：agentic security system，三类专职 Agent 闭环——**红队**（主动找攻击路径）/ **蓝队**（调查告警、判定真实风险）/ **绿队**（执行修复与加固）。
- **Cyber Stack 六层（官方表述）**：信号与传感器 → 安全情境（把信号转成 token 高效的可用理解）→ 模型 → **Harness（编排模型与 Agent）** → Agents → **执行器 actuators（把决策变成防护动作）**。
- **多模型路由**：按质量 / 可靠性 / 延迟 / 成本为不同任务选模型，前沿模型 + 专用安全模型混用；首个场景为软件漏洞管理（自研 **MAI-Cyber-1-Flash** 放进多 Agent 系统 **MDASH**）。
- **人类保留控制权 + 计费**：高影响操作须人工确认，客户自行定义哪些动作可自动执行 / 必须审批；计量单位 **SCU（Security Compute Unit）**，按量计费；微软未公布定价、资格要求与 GA 日期。
- ⚠️ **口径冲突（原样并列，不合并）**：CyberGym 分数微软亚洲站作 **96%**（较 Mythos 高 12 个百分点），TechRepublic 作 **95.95%**（MDASH 由 MAI-Cyber-1-Flash 承担大部分 + **GPT-5.4 处理最难任务**，小模型可承担至多 **90%** 的 MDASH 任务，成本降约 50%）；模型名中文站作 **MAI-Cyber-Flash-1**、英文报道作 **MAI-Cyber-1-Flash**，**以英文原文为准，待官方模型卡确认**。上述分数与成本口径**属于 MDASH，不等于 Project Perception 本身**。

## 已复核·无净新增（避免重复检索）

- **Apple**：WebFetch WWDC26 Session 345 / 343 与 iOS 27 官方指南逐条比对——`ValueRepresentation` / `RelevantEntities` / `EntityCollection` / `SyncableEntity` / `IntentDonationManager` / `OwnershipProvidingEntity` / `IntentValueQuery` / View Annotations / `AppIntentsTesting` **全部已录，无新增 API** → [[Apple AppIntents Schema Protocol 2026]]
- **Android**：官方 AppFunctions 表述（Android 16+、设备端 MCP、`EXECUTE_APP_FUNCTIONS`、内建 Registry、Agent Skill、Gemini 私测自 2026-05）与既有记录一致；零代码 UI Automation（S26 / Pixel 10、限美韩）亦已录 → [[Android AppFunctions 设备侧意图 2026]]
- **HarmonyOS**：窗口内无官方渠道新增（Intents Kit / 元服务 / ArkAF / A2A 端云双模）→ [[HarmonyOS Intents Kit 与 ArkAF 2026]]
- **Windows OS 层**：复核 [learn.microsoft.com · operating-system-agentic-security](https://learn.microsoft.com/en-us/windows/security/book/operating-system-agentic-security)，四支柱（User Control / Agent accounts / Agent workspace / User Transparency）+ 四原则 + 6 个 known folders + ACL **逐条一致，无变化**；且**确认 OS 层仍无任何数据来源分级**（一次有价值的负面确认）→ [[Windows Copilot Actions 与 Agent Workspace 2026]]
- 工况：Horizon MCP 连续第 6 日未连接，全程 WebSearch / WebFetch 直取官方源。

## 排除项

| 条目 | 排除理由 | 评分 |
|---|---|---|
| **钉钉 Agent OS**（阿里，称「全球首个工作智能操作系统」） | 企业协作 SaaS 平台层，非设备侧 OS 执行总线；与 08-02 排除 M365 Copilot Agentic 模式**同一判据** | 5/10 |
| **铁威马 TOS 7**（称全球首个 AI 原生 NAS OS，500+ 功能封装为原子 API 供 Agent 调用） | 设计与 AppFunctions 同构（能力原子化 + Agent 直调内核），但属 NAS 品类、非四大 OS 范围，且来源为厂商宣传稿 | 5/10 |
| **PilotDeck**（清华 THUNLP / 面壁 / OpenBMB / AI9stars 开源「智能体操作系统」） | PC 端多 workspace 协作壳，非系统级意图总线；无 OS 级权限 / Registry 落地 | 5/10 |
| **Windows 11 2026-08 Patch Tuesday**（Copilot+ PC 可卸载 AI 图像模型等开关） | 属设置项与质量更新，非意图框架 / 执行安全机制级变更 | 4/10 |

## 未决问题（→ 各自 B 笔记跟踪，不在本索引展开）

- 【最高优先】Berkeley 官方 BFCL v4 权重表原文逐字核实（当前 40/30/10/10/10 来自第三方拆解，该文注明榜单末次更新 2026-04-12）→ [[Function Calling 端侧工具调用]] · [[通用 AI Agent 评测基准 2026]]
- v4 的 Hallucination 子集能否直接改造成「意图 Registry 误召回」回归集？→ [[Local Agent Bench 端侧智能体基准]] · [[Intent Router 语义路由]]
- 单调棘轮能否落进端侧？核心难题是**端侧谁给数据打 classification**——开发者自报（可伪造，回到 ADI）还是系统按来源类型强判 → [[数据溯源分级与单调棘轮]]
- Apple `.appEntityIdentifier`、Android `AppFunctionMetadata` 能否直接套 `source.type` 六类枚举（可写进 PRD 的字段扩展提案）→ [[Agent Data Injection 数据注入攻击]]
- 【连续第 3 日】四平台 ADI 类别评估：本轮从「找不到任何东西」推进到「治理层有成熟模型、OS 层确认为无」；下轮查 Apple Platform Security Guide 与鸿蒙安全白皮书 PDF → [[Agent Data Injection 数据注入攻击]]
- Project Perception 口径统一（CyberGym 95.95 / 96、模型名两种写法）→ [[Windows Copilot Actions 与 Agent Workspace 2026]]
- 本期待办（过程项，不建 B 笔记）：跟踪荣耀 Robot Phone 8 月发售（仍只有「8 月」，无确切日期）。

> [!note] 关联枢纽
> **MOC**：[[意图框架·跨体系索引 MOC]] ｜ **主题枢纽**：[[端侧意图框架 学习笔记]] · [[App Infra 应用基建]] · [[MCP 与设备侧 MCP]] · [[Intent Router 语义路由]] · [[Intent Schema Protocol 意图模式规范]] · [[Confirmation UI 安全机制]]
> **本期原子笔记**：[[Function Calling 端侧工具调用]] · [[Local Agent Bench 端侧智能体基准]] · [[通用 AI Agent 评测基准 2026]] · [[数据溯源分级与单调棘轮]] · [[Agent Data Injection 数据注入攻击]] · [[Windows Copilot Actions 与 Agent Workspace 2026]] · [[Dual View 智能体数据视图隔离]] · [[XPIA 跨提示注入]]
