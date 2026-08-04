---
type: raw
status: inbox
date: 2026-08-04
run: 09:00 每日自动化
window: 2026-07-29 → 2026-08-04（7 天滚动窗口）
source:
  - https://gorilla.cs.berkeley.edu/leaderboard.html
  - https://benchlm.ai/benchmarks/bfcl-v4
  - https://dreaming.press/posts/berkeley-function-calling-leaderboard-bfcl-v4
  - https://microsoft.github.io/agent-governance-toolkit/compliance/data-provenance-model
  - https://news.microsoft.com/source/asia/2026/07/28/projectperception-2026
  - https://www.techrepublic.com/article/news-microsoft-project-perception-preview/
  - https://learn.microsoft.com/en-us/windows/security/book/operating-system-agentic-security
captured: 2026-08-04
importance_score: ★★★★☆（8/10，单条最高：BFCL v4 权重重构 8/10、AGT 数据溯源模型 8/10）
intent_category: 端侧 Planner 评测口径 / 执行安全数据来源分级
tags: [AppIntent, BFCL, 端侧Planner, 数据溯源, ADI, 执行安全, 原始资料]
---

# AppIntent 每日情报 2026-08-04

> [!abstract] 30 秒速览
> **核心突破（两条，都是「口径级」而非「功能级」）：**
> ① **BFCL 改版把「意图路由该怎么评」的标准换掉了**——v4 把权重重排为 **Agentic 40% / Multi-Turn 30% / Live 10% / Non-Live 10% / Hallucination 10%**，经典单轮 function calling 只剩 20%，另加 10% 专门奖励「**没有合适工具时正确地不调用**」。这意味着本库此前记录的所有 BFCL 分数（Bonsai 73.3%、qwen3-0.6b-tool-router 90.42%、Phi-4-mini 80 分段）**全部是 v3 时代的「格式合规分」，与 v4 分数不可同栏比较**。08-03 榜单快照显示端侧模型断崖：LFM2.5-8B-A1B **49.7%**、MiniCPM5-1B **25.1%**、LFM2.5-230M **21.0%**。
> ② **连续 3 日未解的最高优先待办，今天拿到第一个实质答案**——微软 **Agent Governance Toolkit** 公开了完整的**数据溯源（provenance）记录模式**：来源六类枚举（`tool_output / api_response / agent_message / user_input / database / file`）+ 数据四级分类（`public → internal → confidential → restricted`）+ **单调棘轮（monotonic ratchet）**——工具一旦返回 confidential 数据，会话敏感度**只能升不能降**。这正是 [[Agent Data Injection 数据注入攻击]] 指出的缺口的工程化答案。⚠️ 但它是**开源治理工具包，不是 Windows OS 内建能力**；同日复核 Windows 官方 agentic security 文档，**OS 层仍无任何数据来源分级**。
>
> **关键指标：** BFCL v4 Agentic+Multi-Turn 合计 **70%** 权重｜端侧模型 v4 最高 49.7%｜MDASH+MAI-Cyber CyberGym **95.95%~96%**（口径冲突）、成本降约 50%
> **OS Agent 场景：** 端侧 Planner 选型表须整栏标注基准版本；意图 Registry 的元数据字段应引入「来源类型 + 分类 + 棘轮」三件套

---

## 一、本轮窗口说明与去重声明

| 项 | 说明 |
|---|---|
| 本轮性质 | 2026-08-04 **09:00 每日自动化**（前次为 08-03 21:00 增补跑） |
| 检索窗口 | 2026-07-29 → 2026-08-04（沿用 08-02 起确立的 7 天滚动窗口） |
| 去重基线 | [[AppIntent 每日情报 2026-08-03]]、[[AppIntent 每日情报 2026-08-03-晚]] + `01-笔记\手机AI智能体\` 既有笔记 + B 层各概念节点 |
| 信息源 | Horizon MCP **仍未连接**（连续第 6 日，连接器状态全为 disconnected）→ 全程 WebSearch / WebFetch 直取官方源，综合由本 Agent 完成，未调用外部 gemini 分析额度 |

**已复核、确认无净新增（不重复记录，直接双链指向既有笔记）：**

- **Apple**：WebFetch WWDC26 Session 345 / Session 343 与 iOS 27 官方指南，逐条比对 [[Apple AppIntents Schema Protocol 2026]]——`ValueRepresentation` / `RelevantEntities` / `EntityCollection` / `SyncableEntity` / `IntentDonationManager` / `OwnershipProvidingEntity` / `IntentValueQuery` / View Annotations / `AppIntentsTesting` **全部已录，无新增 API**。
- **Android**：官方 `developer.android.google.cn/ai/appfunctions` 表述（Android 16+、设备端 MCP、`EXECUTE_APP_FUNCTIONS`、内建 Registry、Agent Skill、Gemini 私测自 2026-05）与 [[Android AppFunctions 设备侧意图 2026]] 一致；零代码 UI Automation（S26/Pixel 10、限美韩）亦已录。
- **HarmonyOS**：窗口内无官方渠道新增（Intents Kit / 元服务 / ArkAF / A2A 端云双模均见 [[HarmonyOS Intents Kit 与 ArkAF 2026]]）。
- **Windows OS 层**：WebFetch `learn.microsoft.com/.../operating-system-agentic-security`，四支柱（User Control / Agent accounts / Agent workspace / User Transparency）+ 四原则 + 6 个 known folders + ACL 表述**与 [[Windows Copilot Actions 与 Agent Workspace 2026]] 逐条一致，无变化**。

---

## 二、原始内容

### ① Schema 与语义路由：BFCL v4 权重重构 —— 「意图路由怎么评」的标准换了（重要性 8/10）

**来源**：Berkeley Gorilla 官方榜单页（确认 v4 主题为 "holistic agentic evaluation"）+ 第三方权重拆解 `dreaming.press` + 镜像站 `benchlm.ai` 08-03 快照。

#### A. v4 评分权重（这是本条的核心）

| BFCL v4 类别 | 权重 | 实际测什么 |
|---|---|---|
| **Agentic**（web search / memory / format sensitivity） | **40%** | 取外部信息、持有持久状态、对 Schema 与格式变动的鲁棒性 |
| **Multi-Turn** | **30%** | 对话中跨轮正确用工具（Base / Missing Functions / Missing Parameters / Long Context，约 800 例） |
| Live | 10% | 真实用户贡献的单轮 function calling |
| Non-Live | 10% | 精选单个/多个/并行调用（**这才是「经典 BFCL」**） |
| **Hallucination** | **10%** | **没有合适工具时正确地拒绝调用**（abstention） |

- 经典单轮 function calling（Live + Non-Live）**只剩 20%**；Agentic + Multi-Turn 合计 **70%**。
- 评分仍用 **AST（抽象语法树）+ 状态转移**判定，非 LLM judge，所以数字确定可复现——但也正因如此，它历史上测的是「**调用格式对不对**」而非「**该不该调**」。
- ⚠️ **口径**：权重数字来自第三方拆解文章（该文注明榜单末次更新 2026-04-12），**Berkeley 官方博客原文的权重表述待补核实**；方向性（v4 = holistic agentic evaluation）已由官方榜单页确认。

#### B. 08-03 榜单快照（镜像站 benchlm.ai，仅 9 个模型，非全量）

| 排名 | 模型 | 类型 | BFCL v4 总分 |
|---|---|---|---|
| 1 | Qwen3.7 Max（Alibaba） | 闭源 | **75.0%** |
| 2 | Qwen3.7 Plus（Alibaba） | 闭源 | 72.9% |
| 3 | **LFM2.5-8B-A1B（LiquidAI）** | 开源权重 | **49.7%** |
| 4 | Mellum2-12B-A2.5B-Thinking（JetBrains） | 开源权重 | 45.6% |
| 5 | Mellum2-12B-A2.5B-Instruct（JetBrains） | 开源权重 | 44.2% |
| 6 | ZAYA1-8B（Zyphra） | 开源权重 | 39.2% |
| 7 | **MiniCPM5-1B（OpenBMB）** | 开源权重 | **25.1%** |
| 8 | LFM2.5-VL-450M（LiquidAI） | 开源权重 | 21.1% |
| 9 | **LFM2.5-230M（LiquidAI）** | 开源权重 | **21.0%** |

⚠️ **口径三连警示**：① `benchlm.ai` 是**镜像/聚合站**，自述「mirrors the published score view」，且只收录 9 个模型，**不能等同于 Berkeley 官方全量榜**；② 该站同时标注 BFCL v4 在其体系内为「display only（仅展示、不计入加权）」；③ **本表分数与库内既有 v3 分数不可同栏比较**。

#### C. 值得保留的点（这条为什么值 8/10）

1. **这不是榜单更新，是评价标准的迁移。** BFCL 的作者用权重表承认：**单轮调用准确率已饱和，不再有区分度**。对 OS PM 的直接含义——「我们的意图路由模型 BFCL 多少分」这个问题，从 2026 起必须追问「**哪个版本**」，否则数字无意义。
2. **Hallucination 10% 是四大 OS 意图框架最该看的一栏。** 它测的是「**用户说了句话，但系统里没有任何 AppIntent / AppFunction 能满足它，模型会不会硬凑一个来调**」。这正是跨应用 Intent 路由在真机上最高频的失败模式——**Registry 越大，误召回代价越高**。而工具微调模型系统性地偏向「调点什么」，这一栏恰恰是它们的弱项。
3. **端侧模型在 v4 下的成绩非常难看，而这大概率是真实的。** 亚 1B 级（LFM2.5-230M 21.0%、LFM2.5-VL-450M 21.1%）与 1B 级（MiniCPM5-1B 25.1%）都在 20% 出头；即便是 8B MoE 的 LFM2.5-8B-A1B 也只有 49.7%。**这与本库 07-31 已确立的判断相互印证**：「<1B 通用 multi-turn 极低、1–3B 是甜点区」——现在 v4 给出了更硬的版本，即 **端侧模型的短板恰在 v4 加权最重的 Agentic + Multi-Turn 上**。
4. **与 08-03 晚间「BFCL vs NexusRaven 差 30 分」的结论合流成一条完整判据**：BFCL v3 测格式、NexusRaven 测语义、BFCL v4 测「多轮 + 该不该调」。**三者测三件事，任何单基准选型都会选错。**
5. ⚠️ **本库自查项**：[[Function Calling 端侧工具调用]] 与 [[Local Agent Bench 端侧智能体基准]] 中所有 BFCL 引用**必须补标版本号**，否则会误导选型。本轮已执行。

---

### ② 系统安全与体验：微软 Agent Governance Toolkit 数据溯源模型 —— 「元数据来源校验」的第一个可落地答案（重要性 8/10）

**来源**：`microsoft.github.io/agent-governance-toolkit/compliance/data-provenance-model`（微软 GitHub 组织下的**开源治理工具包**文档，Python 包命名空间 `agentmesh.governance`）。

> **这条直接回应本库连续 3 日挂起的最高优先待办**：「四平台是否对 Agent 读入的结构化元数据做来源校验 / 分级」——见 [[Agent Data Injection 数据注入攻击]] 的「四平台待查清单」。

#### A. 溯源记录模式（provenance record schema）

```yaml
provenance:
  record_id: "prov-2026-07-15-abc123"
  agent_did: "did:agentmesh:customer-service-agent"
  source:                       # 数据从哪来
    type: tool_output           # tool_output | api_response | agent_message | user_input | database | file
    tool_name: read_customer_record
    source_agent_did: null      # 若来自另一个 Agent
    source_classification: confidential
  data:
    classification: confidential  # public | internal | confidential | restricted
    contains_pii: true
    pii_types: [name, email, phone]
    jurisdiction: [EU, US]
    hash: "sha256:a1b2c3..."      # 内容哈希，做完整性校验
  transformation:
    type: none                    # none | aggregation | anonymization | redaction | enrichment
  purpose:
    decision_type: customer_inquiry_response
    policy_decision: allow
    audit_entry_id: "audit_abc123"
  retention:
    policy: "3_years"
    legal_hold: false
```

#### B. 三个可迁移的机制原语

| 机制 | 做法 | 对 OS 意图框架的映射 |
|---|---|---|
| **来源类型枚举** | `source.type` 六类硬编码，每条数据必须归类 | 意图 Registry 的每个元数据字段（Schema 描述、实体 ID、工具响应）都应标「谁写的」 |
| **单调棘轮（monotonic ratchet）** | `SessionAttribute(name="data_sensitivity", ordering=[public→internal→confidential→restricted], monotonic=True)`——工具一旦返回 confidential，**整个会话敏感度只升不降** | 端侧 Agent 会话一旦读过高敏内容，后续所有动作自动进入高门槛，**不依赖模型自觉** |
| **两阶段策略门** | `post_tool` 阶段查工具输出分类可 `deny`；`pre_output` 阶段查 PII 可 `require_approval` | 确认机制的触发点从「动作前」扩展为「**工具返回后**」和「**输出前**」两道 |

#### C. 溯源链与合规映射

- 多 Agent 传递时溯源记录形成**父子链**（`parent: prov-00x`），并在链上记录 **classification ratchet**（如 `confidential → confidential`）与变换类型。
- 官方页明确对齐 **EU AI Act Article 10（数据治理）**，逐条映射 10(2)(a)~(f)、10(3)、10(4)、10(5)，并标注「**高风险条款自 2026-08-02 起适用**」——与本库 08-02 记录的 **Article 15（准确性/鲁棒性/网络安全）同日生效**互为补充：**Article 15 管「防不防得住攻击」，Article 10 管「数据从哪来、怎么被处理」。**
- **实现状态（官方自述）**：溯源模式 ✅ 已定义、审计集成 ✅ 已发布、会话棘轮 ✅ 已发布、多阶段策略 ✅ 已发布；溯源链父子追踪 🔜 计划中、`ProvenanceTracker` Python API 🔜 计划中、自动 PII 检测 🔜 计划中。

#### D. ⚠️ 三条必须说清的边界（防止误读为「Windows 已支持」）

1. **它不是 Windows OS 能力**，是 microsoft GitHub 组织下的**开源治理工具包 / 参考实现**，面向企业 Agent 治理与 EU AI Act 合规，不是设备侧意图框架的内建机制。
2. **同日复核 Windows 官方 agentic security 文档，OS 层仍无任何数据来源分级**——Agent Workspace 隔离的是「进程与账号」，不是「数据可信度」。**这是一次有价值的负面确认**：微软在治理层已有成熟模型，但**尚未下沉到 OS 意图执行链路**。
3. 因此 [[Agent Data Injection 数据注入攻击]] 的四平台清单**仍全部为「待补」**，但结论从「无人做」精化为「**已有可抄的成熟模型，四大 OS 尚未采纳**」——这是产品判据的升级，不是问题的解决。

---

### ③ 系统安全：微软 Project Perception 进入公共预览（08-03，重要性 7/10）

**来源**：微软官方新闻室（07-27/28 发布）+ TechRepublic / RCPmag（08-03 公共预览确认）。

- **定位**：agentic security system。三类专职 Agent 闭环——**红队 Agent**（主动找攻击路径）/ **蓝队 Agent**（调查告警、判定真实风险）/ **绿队 Agent**（执行修复与加固）。
- **Cyber Stack 六层**（官方表述）：信号与传感器 → 安全情境（把信号转成 token 高效的可用理解）→ 模型 → **Harness（编排模型与 Agent）** → Agents → **执行器 actuators（把决策变成防护动作）**。
- **多模型路由**：按质量 / 可靠性 / 延迟 / 成本为不同任务选模型，前沿模型 + 专用安全模型混用。首个场景为软件漏洞管理，把自研 **MAI-Cyber-1-Flash** 放进多 Agent 系统 **MDASH**。
- **人类保留控制权**：高影响操作须人工确认；客户需自行定义哪些动作可自动执行、哪些必须审批。计量单位为 **SCU（Security Compute Unit）**，按量计费。

#### 为什么它进本库（而不是当成一条企业安全新闻）

**因为它把「Agent 执行循环」本身变成了被检查的对象。** 配套的 Defender 能力里有一条对 OS 级执行安全最关键：

> 对 Windows 端点上受支持的**本地 Agent**，**Defender for Endpoint 可以检查 agent loop 本身——包括用户提示、工具调用、工具响应**——并在风险动作**执行前阻断**，再把行为作为告警上报 Defender XDR。

- 这是本库记录到的**第一个「把工具调用与工具响应作为可检测流量」的端点侧机制**。此前 [[XPIA 跨提示注入]] 的缓解都在「Agent 自己内部」（提示加固、隔离、确认 UI）；这条把防线挪到了 **Agent 之外的端点安全栈**，与 [[Dual View 智能体数据视图隔离]] 提出的「**门不能是模型**」是同一方向的两种实现。
- 微软同时明示：**被投毒的 MCP 工具描述**可以让一个「已授权」的 Agent 通过看似合法的工具调用泄露数据——这与 [[Agent Data Injection 数据注入攻击]] 的攻击面判定完全一致。

⚠️ **口径冲突（不合并、原样并列）**：
- CyberGym 分数：微软亚洲站作 **96%**（较 Mythos 高 12 个百分点）；TechRepublic 作 **95.95%**，并说明是 MDASH 用 MAI-Cyber-1-Flash 承担大部分任务 + **GPT-5.4 处理最难任务**的组合，小模型可承担至多 **90%** 的 MDASH 任务。
- 模型名：微软亚洲站作 **MAI-Cyber-Flash-1**，英文报道作 **MAI-Cyber-1-Flash**。**以英文原文为准，中文站疑为译名错序，待官方模型卡确认。**
- 上述分数与成本口径**属于 MDASH，不等于 Project Perception 本身的定价或效果**；微软未公布公开定价、资格要求与 GA 日期。

---

## 三、本轮排除项（展示过滤纪律，沿用 08-02 对 M365 的同一判据）

| 条目 | 日期 | 排除理由 | 评分 |
|---|---|---|---|
| **钉钉 Agent OS**（阿里，宣称「全球首个工作智能操作系统」） | 08-04 | 企业协作 SaaS 平台层，非设备侧 OS 执行总线。与 08-02 排除 M365 Copilot Agentic 模式**同一判据**，保持一致 | 5/10 |
| **铁威马 TOS 7**（宣称全球首个 AI 原生 NAS OS，500+ 核心功能封装为原子 API 供 Agent 调用） | 08-04 | 设计与 AppFunctions 同构（**能力原子化 + Agent 直调内核**），但属 NAS 品类、非四大 OS 范围，且来源为厂商宣传稿 | 5/10 |
| **PilotDeck**（清华 THUNLP / 面壁 / OpenBMB / AI9stars 联合开源「智能体操作系统」） | 08-04 | PC 端多 workspace 协作壳，非系统级意图总线；无 OS 级权限/Registry 落地 | 5/10 |
| Windows 11 2026-08 Patch Tuesday（Copilot+ PC 可卸载 AI 图像模型等 AI 开关） | 08 月 | 属设置项与质量更新，非意图框架/执行安全机制级变更 | 4/10 |

---

## 四、我的问题（待验证）

1. **Berkeley 官方 v4 权重表在哪？** 当前权重（40/30/10/10/10）来自第三方拆解。需找到官方 BFCL-v4 博客原文核实，**这是本库所有端侧选型结论的地基**（待补）。
2. **v4 的 Hallucination 子集能否直接改造成「意图 Registry 误召回」的回归集？** 若可以，这是四大 OS 意图路由质量最直接的现成度量（待补）。
3. **AGT 的「单调棘轮」能否落进端侧？** 棘轮本身几乎零成本（一个会话变量 + 有序枚举），比 DualView 的 ~15× 调用便宜得多。**问题在于端侧谁来给数据打 classification** —— 是 AppFunction 的开发者自报（可被伪造 → 又回到 ADI），还是系统据来源类型强判？（待补）
4. **Apple `.appEntityIdentifier`、Android `AppFunctionMetadata` 是否可以直接套 `source.type` 六类枚举？** 若能，这就是一份可以直接写进 PRD 的字段扩展提案（待补）。
5. **跨日待办（连续第 3 日）**：四平台 ADI 类别评估——本轮已从「找不到任何东西」推进到「找到微软治理层的成熟模型，但 OS 层确认为无」。下轮方向：查 Apple Platform Security Guide 与华为鸿蒙安全白皮书 PDF 是否有对应表述。

## 五、后续动作

- [x] BFCL v4 权重与 08-03 快照 → 追加进 [[Function Calling 端侧工具调用]] + [[Local Agent Bench 端侧智能体基准]]（全库 BFCL 引用补标版本号）
- [x] AGT 数据溯源模型 → 新建 B 概念节点 [[数据溯源分级与单调棘轮]]（既有 ADI/DualView 节点讲的是攻击与隔离架构，无法承载「来源分级 + 棘轮」这一面）
- [x] AGT + Defender agent loop 检查 → 追加进 [[Agent Data Injection 数据注入攻击]] 与 [[Windows Copilot Actions 与 Agent Workspace 2026]]
- [x] 来源六类枚举 + 四级分类 + 棘轮 → 修订 [[Agent 读入路径可信数据边界 SOP]]，把「按不可信处理」升级为可执行的分级判据
- [ ] 核实 Berkeley 官方 v4 权重原文（最高优先，待补）
- [ ] 跟踪四平台是否采纳来源分级（跨日待办，连续第 3 日）
- [ ] 跟踪荣耀 Robot Phone 8 月发售（仍只有「8 月」，无确切日期）

---

> [!note] 概念双链
> [[意图模式规范]] ｜ [[语义路由]] ｜ [[端侧工具调用]] ｜ [[确认机制]] ｜ [[元服务]] ｜ [[隔离执行]] ｜ [[A2A 端侧智能体协议]] ｜ [[XPIA 跨提示注入]]

#标签/AppIntent #标签/BFCL #标签/端侧Planner #标签/数据溯源 #标签/ADI #标签/执行安全
