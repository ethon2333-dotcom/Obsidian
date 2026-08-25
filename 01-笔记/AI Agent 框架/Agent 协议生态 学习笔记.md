---
title: Agent 协议生态 学习笔记
tags: [AgentProtocol, A2A, ANP, MCP, 端侧意图框架, 学习笔记]
created: 2026-08-06
source: 一手源（官方 spec/Linux Foundation/2026 公开资料），2026-08-06 核实
---

# Agent 协议生态 学习笔记

> 学习定位：这是一篇**广度种子笔记**。目标是先把「Agent 之间怎么互操作」这张地图**铺满**——有哪些协议、各管哪一层、谁在治理、边界在哪——**而不是把任何一条讲深**。
> 深度留白：每一节末尾的 `- [ ]` 就是我后续要自己补的坑。库内已有 [[MCP 与设备侧 MCP]]（Agent→Tool 那条线）和 [[A2A 端侧智能体协议]]（局部），本文负责**把它们串成一张网**。

---

## 一、一句话心智模型

**Agent 协议生态 = 给「机器社会」补基础设施：先能连，再能信，最后能找。**

如果说 MCP 解决的是「一个 Agent 怎么够到外面的东西」，那 Agent 协议生态解决的是**另一个层级的问题**：

> **当满世界都是别人家的 Agent，我的 Agent 怎么知道它们存在、怎么确认它们是谁、怎么把活儿派给它们？**

一个便于记忆的类比（我自己用的）：

| 互联网早期 | Agent 生态对应物 |
|---|---|
| TCP/HTTP（怎么传） | A2A / SLIM（消息怎么走） |
| DNS（怎么找到对方） | AgentCard / Agent Directory / Registry |
| TLS + CA（怎么确认对方是谁） | Signed AgentCard / DID / Agent Identity |
| REST API（对方能干什么） | AgentCard skills / OASF / ADP |
| 支付网关（怎么结账） | AP2 / ANP 支付协议 |

**最关键的那条边界**（后面第四节展开）：

> **MCP 管「往下够工具」，A2A 管「往旁边找同类」，端侧意图框架管「OS 往下调 App」。三者不是竞品，是三个方向。**

---

## 二、为什么需要 Agent 互操作标准

### 2.1 问题的本质：N×M 又回来了一次

MCP 已经把「Agent × 工具」的 N×M 压成 N+M（见 [[MCP 与设备侧 MCP]] 第二节）。但 2025 年以后出现了**第二个 N×M**：

- 企业里同时跑着 LangGraph 写的、CrewAI 写的、Semantic Kernel 写的、厂商 SaaS 自带的 Agent；
- 跨组织场景更糟：你的采购 Agent 要和供应商的报价 Agent 谈；
- 每接一个就写一套私有 REST——**和 MCP 出现之前的工具集成一模一样**。

A2A 官方对这件事的定性很朴素：**协调（coordination）成了瓶颈**，不是能力。

### 2.2 为什么不能直接用 MCP 顶上

这是我一开始想错的地方。把远端 Agent 包成一个 MCP tool 技术上**完全可行**，很多人也这么干。但会丢三样东西：

| 丢掉的东西 | 为什么工具模型装不下 |
|---|---|
| **自主性** | 工具按参数执行；Agent 会自己规划、可以反问、可以拒绝 |
| **长任务** | MCP 以请求-响应为主（异步 Tasks 到 2026-07 才移为正式扩展）；A2A 的任务状态机是**一等公民** |
| **不透明性（opacity）** | 工具要暴露 schema；A2A 明确支持 **opaque agent**——不共享内部记忆、工具和专有逻辑 |

A2A 官网自己给的判据（我认为是全场最清楚的一句）：

> **区别取决于「Agent 在和什么交互」**——对方是「有明确输入输出、常常无状态的原语」→ 工具（MCP 域）；对方是「会推理、会规划、跨多轮维持状态的自治系统」→ Agent（A2A 域）。

⚠️ 但要诚实：这条边界**是设计决策，不是物理定律**。从调用方视角看，「另一个 Agent」也是一种工具，灰区是真实存在的（这一点在第四节展开）。

### 2.3 谁在推这件事（治理视角，PM 最该看的一层）

2025—2026 最大的结构性变化不是技术，是**所有权集体让渡**：

- Anthropic 把 MCP 捐给 Linux Foundation（2025-12-09，AAIF）
- Google 把 A2A 捐给 Linux Foundation（2025-06，见下）
- Cisco 把 AGNTCY 捐给 Linux Foundation（2025-07）
- IBM 把 ACP 直接**并入** A2A（2025 下半年）

> **PM 判断**：这和当年 Kubernetes 的路径一模一样——**谁先放弃所有权，谁的标准先赢**。竞争对手只肯采用「没人拥有」的东西。这句我在 [[MCP 与设备侧 MCP]] 里写过一次，A2A 是它的第二个样本，可以当规律用了。

- [ ] 「Agent 之间的 N×M」到底有多痛？想找**真实企业案例的量化数据**（集成工时、维护成本），不要供应商 PPT 数字。
- [ ] MCP 包住远端 Agent 的做法在生产里占比多少？灰区是不是其实是主流？→ 待查。

---

## 三、主流协议分类（广度地图）

先说清楚**分层**，否则会把不同层的东西放在一张表里比，这是这个领域最常见的错误：

```
应用/领域层    AP2（支付）· UCP（商务）· 各垂域协议
交互语义层     A2A（Agent↔Agent 的任务与消息）
描述与发现层   AgentCard · OASF · Agent Directory · ANP-AD · MCP Registry
身份与信任层   Signed AgentCard · did:wba · AGNTCY Identity
安全传输层     SLIM（原 AGP）· HTTPS/gRPC
—— 以上是 Agent↔Agent ——
工具接入层     MCP（Agent→Tool）
系统能力层     AppFunctions / App Intents / Intents Kit（OS→App）
```

### 3.1 协议一览表

| 协议 | 提出方 / 治理 | 管哪一层 | 核心机制 | 状态（2026-08） |
|---|---|---|---|---|
| **A2A（Agent2Agent）** | Google 提出（2025-04-09），捐给 **Linux Foundation** | **Agent ↔ Agent**（交互语义） | AgentCard / Task / Message / Artifact；JSON-RPC、HTTP+SSE、gRPC 多绑定 | **v1.0 已发布**，事实标准 |
| **ACP（Agent Communication Protocol）** | IBM Research（2025-03，BeeAI） | Agent ↔ Agent（REST 轻量派） | REST + MIME 消息；构建期打包能力描述，无运行时发现依赖 | **已并入 A2A**，停止独立演进 |
| **AGNTCY**（含 SLIM / OASF / dir / Identity） | Cisco Outshift 发起（2025-03），捐给 LF（2025-07） | **基础设施层**（发现/身份/传输/可观测） | OASF 描述 + Agent Directory 联邦发现 + SLIM 传输 + Identity | 活跃，明确**不与 A2A/MCP 竞争** |
| **AGP（Agent Gateway Protocol）** | Cisco / AGNTCY | 传输/网关 | — | **已更名为 SLIM**，AGP 是旧称 ⚠️ |
| **SLIM** | AGNTCY / LF | **安全传输层** | gRPC over HTTP/2 + MLS 端到端加密 + pub/sub + 层级命名（无需入站端口） | 可承载 A2A、MCP、自定义协议 |
| **ANP（Agent Network Protocol）** | 开源社区协议栈（中文生态活跃） | **去中心化身份 + 发现 + 消息 + 支付**（全栈） | `did:wba` + WNS Handle；AD 描述与发现；IM Profiles（含 E2EE）；AP 领域协议 | ANP 1.1，三层架构 |
| **MCP** | Anthropic → LF/AAIF | **Agent → Tool（不是 Agent→Agent）** | Tools/Resources/Prompts + JSON-RPC | 日期版本制，当前 2026-07-28 |
| **AGENTS.md** | OpenAI → LF/AAIF | 「Agent ↔ 代码仓库」的约定 | 纯 Markdown 约定，无 schema | 6 万+ 开源项目采用（捐赠时口径） |
| **AP2（Agent Payments Protocol）** | A2A 生态扩展 | **支付/经济协调** | 加密可验证的用户购买同意（mandates） | 60+ 支付与金融机构支持 |
| **端侧意图框架** | 各 OS 厂商各自为政 | **OS → App 能力** | AppFunctions / App Intents / Intents Kit | **互不兼容**，见 [[端侧意图框架 学习笔记]] |

### 3.2 「Agent 发现 / 描述」这一层单独看（最容易被忽略）

所有协议最后都要回答同一个问题：**我怎么知道对面能干什么**。四种答案：

| 方案 | 归属 | 放在哪 | 特点 |
|---|---|---|---|
| **AgentCard** | A2A | `/.well-known/agent-card.json`（RFC 8615 约定） | 只要知道域名就能发现；v1.0 起可**加密签名** |
| **OASF + Agent Directory** | AGNTCY | 联邦式目录，多目录 P2P 同步 | 「Agent 界的 DNS」；**能同时索引 A2A agent 和 MCP server** |
| **ANP AD + did:wba** | ANP | DID Document + 服务端点 | DID 文档是「稳定入口」而非实时状态表，动态能力靠 `anp.get_capabilities` 拉 |
| **OS Registry** | Android / Apple / 鸿蒙 | 系统内置 | 设备内唯一权威，**跨厂商完全不通** |

> **这一层才是真正的战场。** 传输谁都能做，能力描述格式一旦形成事实标准，生态就锁定了。这和 [[Agent Skills 技能范式 2026]] 里 SKILL.md 之争、[[智能体互联国家标准与 AIP]] 里「能力描述是唯一必须跨厂商可迁移的一段」是**同一个问题的三个战场**。

### 3.3 框架 vs 协议：别混为一谈

Ethon 你库里 [[Agent 框架生态与竞品]] 讲的是**框架**，本文讲的是**协议**，两者关系是：

| | 框架 | 协议 |
|---|---|---|
| 例子 | LangGraph、CrewAI、Google ADK、OpenAI Agents SDK、goose、BeeAI | MCP、A2A、ANP、SLIM |
| 解决 | Agent **内部**怎么写（循环、状态、记忆） | Agent **之间/对外**怎么说话 |
| 关系 | 框架**实现**协议 | 协议**跨越**框架 |

A2A 官网自己划的界很干脆：**A2A 不是 Agent 开发套件，也不是 sub-agent / tool-call 协议**——Agent 调自己的子 Agent 和工具，用框架原生能力或 MCP。

官方推荐的组合口径原文大意：**用 ADK（或任意框架）构建 → 用 MCP（或任意工具）装备 → 用 A2A 与远端 Agent、本地 Agent 和人类通信。**

- [ ] **Google ADK** 的具体形态、版本、与 A2A 的绑定深度——本文只知道它是「框架侧」，细节全空。→ 需要一手源。
- [ ] **OpenAI 的 Agent 生态**（Agents SDK / AgentKit / Apps SDK）在协议层到底站在哪：它捐了 AGENTS.md、是 AAIF 白金成员、ChatGPT 采用 MCP，但**有没有自己的 Agent→Agent 主张**？→ 完全没查清，留白。
- [ ] ANP 的**发起组织、治理结构、真实采用率**——只看到规范网站和白皮书，**未见任何生产采用证据**。⚠️ 不要在任何对外材料里把它和 A2A 并列称"主流"。
- [ ] SLIM 与 A2A 的关系：官方说 SLIM 可以**承载** A2A，那实际部署里有多少人这么叠？还是 A2A 直接跑 HTTP 就够了？

---

## 四、边界：MCP / A2A / 端侧意图框架 三者分工

这一节是本文的核心，也是我最需要讲对的一节（对外讲错会很难看）。

### 4.1 三者对照

| 维度 | **MCP** | **A2A** | **端侧意图框架** |
|---|---|---|---|
| 一句话 | Agent **调工具** | Agent **调 Agent** | OS **调 App 能力** |
| 方向 | 垂直（Agent ↓ 工具） | 水平（Agent ↔ Agent） | 垂直 + 系统级（OS ↓ App） |
| 被调方 | 工具端点 | **另一个自治 Agent（黑箱）** | App 声明的能力 |
| 被调方有自主性吗 | ❌ | ✅ 可规划、可反问、可拒绝 | ❌ |
| 被调方要不要暴露内部 | 要（schema） | **不要**（opaque，保护 IP） | 要（schema） |
| 任务模型 | 请求-响应为主 | **长任务是一等公民**（状态机） | 平台各异 |
| 发现 | `tools/list` + Registry + `.well-known` | **AgentCard**（可签名） | **OS 内置 Registry** |
| 治理 | LF / AAIF | **Linux Foundation** | **各 OS 厂商，互不通** |
| 跨组织能力 | 可以（远程 server） | **这就是它的设计目标** | ❌ 出不了设备/生态 |

### 4.2 三个方向的直觉图

```
                 ┌──────────┐
        A2A      │  Agent A │      A2A
   ◄─────────────┤（我的）  ├─────────────►  别家 Agent
   别家 Agent    └────┬─────┘
                      │ MCP（往下够工具）
                 ┌────▼─────┐
                 │  工具/数据│
                 └──────────┘
                      ▲
                      │ 端侧意图框架（OS 往下调 App）
                 ┌────┴─────┐
                 │  手机 App │
                 └──────────┘
```

**三句话判断法**（我自己的判断题，从库内 [[MCP 与设备侧 MCP]] 沿用并扩展）：

- 对方**会自己做决定、可以拒绝、有任务生命周期** → **A2A**
- 对方**只是按你给的参数执行** → **MCP**
- 对方**必须由 OS 授权和路由才能碰** → **端侧意图框架**

### 4.3 官方给的「修车行」比喻（值得原样记住）

A2A 官方文档用一家全 AI 修车行讲清了分工：

| 场景 | 用什么 |
|---|---|
| 客户（或其助理 Agent）对「店长 Agent」说"我车有异响" | **A2A** |
| 店长多轮追问"能拍段视频吗"、"漏液多久了" | **A2A** |
| 技师 Agent 调诊断仪 `scan_vehicle_for_error_codes()`、查维修手册、升举升机 | **MCP** |
| 技师 Agent 问「配件供应商 Agent」有没有 12345 号件 | **A2A** |

一句话收口：**A2A 处理"对话式、任务式的协作"，MCP 处理"结构化的工具调用"。A2A 是"结伴做事"，MCP 是"使用能力"。**

### 4.4 ⚠️ 必须承认的灰区（反 hype 一节）

干净的说法是「MCP 管工具、A2A 管 Agent，零重叠」。**现实更脏**：

1. **远端 Agent 可以被包成 MCP tool**——A2A 官方自己也承认：A2A Server 可以把部分 skill 暴露成 MCP 兼容资源。
2. **A2A 的任务交换也能承载本可以做成 tool call 的活儿**。
3. → 所以「这是我调用的工具」还是「这是我委派的同伴」，**是架构选择，不是协议规定**。
4. → 更要警惕的是：「互补而非竞争」这句话**替供应商承担了很多说服工作**——它让你觉得应该把整套栈都装上。很多系统其实**只用一个就够了**。

**给端侧的第三条边界补充**（这条是我自己的推论，非官方）：

> 端侧意图框架和前两者最本质的差别不是"在哪执行"，是**谁是权威**。MCP/A2A 是**对等网络的协议**（谁都能发 AgentCard），端侧意图框架是**中心化授权的 API**（OS 说了算，`EXECUTE_APP_FUNCTIONS` 是系统权限）。
> 所以前两者的问题是"怎么建立信任"，后者的问题是**"入口所有权归谁"**——完全不同性质的战场。见 [[国内安卓厂商做 App Intent 的阻力]]、[[App Intent 的核心作用]]。

- [ ] 端侧 Agent 要和**云上别家 Agent** 通信时，走 A2A 还是走厂商私有通道？四大 OS 目前的实际做法？→ 待查，这是我最关心的一个空白。
- [ ] 鸿蒙的「端侧 A2A」和 Google A2A 协议**是否互通**？（库内 [[A2A 端侧智能体协议]] 已挂了这个问题，至今未解）
- [ ] 灰区里有没有**性能/成本层面的判据**（不是语义判据）？比如什么规模以下 MCP 包一层更划算。

---

## 五、2025—2026 进展

### 5.1 A2A 主线时间线

| 时间 | 事件 |
|---|---|
| **2025-04-09** | Google 在 Cloud Next 发布 **Agent2Agent（A2A）**，50+ 启动伙伴（Atlassian、Salesforce、SAP、ServiceNow、PayPal、Workday、LangChain、MongoDB、UiPath 等 + 四大咨询） |
| **2025-06**（日期待核实） | Google 把 A2A **捐给 Linux Foundation**，成立 Agent2Agent Protocol Project；初始成员 AWS、Cisco、Google、Microsoft、Salesforce、SAP、ServiceNow |
| **2025-08 / 09**（⚠️ 两说） | **IBM ACP 并入 A2A**；ACP 停止独立开发，Kate Blair 代表 IBM 进入 A2A TSC |
| **2025-11** | AWS 在 **Bedrock AgentCore Runtime** 支持 A2A server |
| **2025-12-09** | Linux Foundation 成立 **AAIF**（MCP / goose / AGENTS.md 三个创始项目）——⚠️ **A2A 是否同期并入 AAIF，两说，见待核实** |
| **2026 上半年** | **A2A v1.0 发布**（首个稳定版，含破坏性变更） |
| **2026-04-09** | LF 发布一周年新闻稿：**150+ 组织、22,000+ GitHub star、5 种生产级 SDK** |

### 5.2 v1.0 到底改了什么（这是"标准成熟"的教科书样本）

官方定性：**「强调成熟而非重造」**——核心思想不变，去掉毛边、澄清歧义、补上企业部署要求。四件大事：

| 特性 | 解决什么问题 |
|---|---|
| **多协议绑定 + 版本协商** | JSON+HTTP、gRPC、JSON-RPC 都行；不被单一厂商/技术栈绑死 |
| **企业级多租户** | 一个端点安全托管多个 Agent；平台方可以做统一网关路由到几百个 Agent |
| **Signed AgentCard** | **交互之前**先密码学验证身份——金融/医疗/保险的准入门槛 |
| **Web 对齐架构（无状态、分层）** | 能直接复用现成的负载均衡、网关、安全、可观测方案 |

**迁移设计值得单独学**：v1.0 在交互协议上**有破坏性变更**，但 **AgentCard 是向后兼容演进的**——同一个 Agent 可以同时声明支持 v0.3 和 v1.0，客户端**渐进迁移而不是一次性割接**。

> 对照 MCP 2026-07-28 那次「launch 以来最大修订」（删握手、删 Session-Id、转无状态），两个协议**在同一时期做了同方向的动作：向无状态和 Web 原生架构收敛**。这不是巧合，是"从玩具走向生产"的必经之路。

### 5.3 标准融合：从「协议战争」到「分层共识」

2026 年最值得记的一句话是：**Agent→Agent 这一层已经收敛，Agent→Tool 这一层早就定了。**

**融合的三种形态**：

| 形态 | 例子 |
|---|---|
| **吞并** | IBM ACP → A2A（同一层的直接竞品，输给了先发势能与 150 家生态） |
| **分层互补** | AGNTCY 明确定位为基础设施层，OASF 描述符可以**包住** MCP server 和 A2A agent，目录同时索引两者 |
| **叠加承载** | SLIM 作为传输层承载 A2A / MCP / 自定义协议——「A2A 定义**说什么**，SLIM 定义**怎么安全送达**」 |

> **ACP 的死法值得抄进产品笔记**：ACP 的技术选择（REST 轻量、构建期打包能力、无运行时发现依赖）在一类简单场景里**确实更优雅**，但它出现约半年就消失了。决定胜负的不是 REST vs 任务状态机，是**Google 的启动势能 + 生态规模**。
> → **同一生态位上的更轻量协议，不是竞争对手，是一个 feature request。** 这条对做平台/开放能力的 PM 是硬教训。

### 5.4 生态外延：不止通信

- **AP2（Agent Payments Protocol）**：把 A2A 从"通信"延伸到"经济协调"，60+ 支付与金融机构支持；核心是**捕获用户购买同意的强密码学证据**（mandates）。呼应库内 [[意图支付授权协议 APOP]]。
- **UCP**：通过 AP2 mandates 扩展与 AP2 完全兼容。⚠️ UCP 全称与主体本文未核实。
- **框架侧接入**：LangGraph、CrewAI 都已支持 A2A 委派子任务，**不共享内部记忆**。→ 库内 [[LangGraph 概览]] 可以接上这一段。
- **A2A 路线图**：互操作性规范、**registry 相关工作的整合**、测试与工具、安全与部署最佳实践。→ 注意「registry 整合」这一条，说明**发现层目前还是乱的**。

### 5.5 其它标准战场（本文只做索引，不展开）

| 组织 | 在做什么 | 状态 |
|---|---|---|
| **W3C AI Agent Protocol CG** | Agent 在线发现与安全协作的通用规则 | 志愿者社区组，2025-08 起有早期草案 |
| **W3C WebMCP** | Google + Microsoft 主导，**让普通网站给 Agent 提供结构化操作入口**（而非盲点 GUI） | Chrome 早期测试 |
| **IETF** | Agent 可验证身份、代表用户行动的权限边界 | 工作草案 |
| **OpenID Foundation** | 把成熟登录/授权体系扩展到 Agent | 活跃 |
| **NIST / CAISI** | 美国 **AI Agent Standards Initiative** | 2026-02-17 启动 |
| **中国国标 + AIP** | 《人工智能智能体互联》7 项国标（身份/描述/发现/协同/工具调用五段式） | 见 [[智能体互联国家标准与 AIP]] |

> **WebMCP 这条线对 Ethon 特别值得盯**：它是「结构化通道 vs GUI 兜底」之争在**浏览器侧**的翻版，和 [[端侧执行通道 GUI 与 MCP 路线之争]] 是同构问题。手机侧是 AppFunctions vs UI Automation，Web 侧就是 WebMCP vs Browser Use。

- [ ] A2A v1.0 的**确切发布日期**（本文只能确定在 2026-04-09 之前）。
- [ ] A2A **v0.3 → v1.0 的具体破坏性变更清单**——只知道"有"，不知道"是什么"。
- [ ] **AAIF 与 A2A 的确切治理关系**（见待核实清单，这是本文最大的一个事实缺口）。
- [ ] W3C WebMCP 的实际形态与进展；它和 MCP 是什么关系（同名但可能是两回事）。
- [ ] 三方渠道流传的 A2A 效益数字（"解决时长 -60%"、"IT 成本 -30%"等）——**一律不采信**，需要独立来源。

---

## 六、库内关联

- **Agent→Tool 那条线（本文的对照面）**：[[MCP 与设备侧 MCP]] ← 三者边界最初的对照表在这里
- **A2A 局部深读 + 端侧 A2A 纠偏**：[[A2A 端侧智能体协议]]
- **端侧那条线（OS→App）**：[[端侧意图框架 学习笔记]] · [[Android AppFunctions 设备侧意图 2026]] · [[HarmonyOS Intents Kit 与 ArkAF 2026]]
- **能力描述之争**：[[Intent Schema Protocol 意图模式规范]] · [[Agent Skills 技能范式 2026]] · [[智能体互联国家标准与 AIP]]
- **框架 vs 协议**：[[Agent 框架生态与竞品]] · [[应用层 Agent 框架 vs 系统级意图框架 对照]] · [[LangGraph 概览]]
- **上下文供给（协议之外的另一半）**：[[Context Engineering 学习笔记]] · [[Function Calling 端侧工具调用]]
- **信任与安全**：[[Agent 身份与硬件级审批]] · [[XPIA 跨提示注入]]
- **支付/商业**：[[意图支付授权协议 APOP]] · [[企业级 Agent 平台与 Agent-as-Asset 2026]]
- **通道之争（Web 侧同构）**：[[端侧执行通道 GUI 与 MCP 路线之争]]
- **索引**：[[AI Agent 框架 MOC]]

---

## 七、待解问题

> 本节是这篇种子笔记的**主要价值**。上面每节末尾的 `- [ ]` 是章节内的局部空白，这里放跨章节的大问题。

### 7.1 边界类

- [ ] **「Agent 还是工具」这条线，有没有可操作的工程判据？** 官方给的是语义判据（自主性/状态/不透明性），但真到设计时，同一个远端服务两种包法都能跑。我需要一套**决策树**（延迟？调用频次？是否需要多轮？是否跨组织？），而不是形容词。→ 可能要自己写，参考库内 [[GUI Agent vs 原生 API 产品决策树]] 的写法。
- [ ] **端侧 Agent 要不要成为 A2A 的一等公民？** 手机上的系统 Agent 发不发 AgentCard？如果发，`/.well-known/` 挂在哪（设备没有域名）？如果不发，跨设备/跨厂商协作怎么谈？→ **这是我作为 Android OS PM 最该想清楚的一个问题，目前完全空白。**
- [ ] **端侧意图框架有没有可能被 A2A 吃掉？** 或者反过来——OS 把系统 Agent 包装成 A2A endpoint 对外，App 能力仍走私有 Registry。这两条路的生态后果差别是什么？

### 7.2 治理与生态类

- [ ] **发现层（Registry）为什么至今没收敛？** MCP 有官方 Registry，A2A 路线图上写着"registry 工作整合"，AGNTCY 有 Agent Directory，ANP 有 DID 体系，OS 各有内置 Registry。传输层都统一了，**发现层为什么反而最乱**？→ 我的假设：**因为发现层最接近分发权和入口价值**，谁都不肯让。待验证。
- [ ] **ANP 这条路（DID + 去中心化身份）会不会是被低估的一条？** 目前看采用率低、缺生产证据，但它是唯一一个**不依赖中心化目录**的方案。如果监管往"Agent 必须可追溯"走，DID 路线会不会突然变刚需？→ 呼应 [[智能体互联国家标准与 AIP]] 的"身份标识"段。
- [ ] **中国生态（国标五段式 + AIP + 鸿蒙端侧 A2A）与全球生态（A2A/MCP/AGNTCY）会走向互认还是分叉？** 目前看是**两套并行**。分叉的代价谁承担？

### 7.3 安全类

- [ ] **Signed AgentCard 只解决"你是谁"，不解决"你说的话可不可信"。** 一个身份合法的 Agent 完全可以传播被注入的内容——A2A 的多 Agent 消息链里有没有 provenance 机制？（库内 [[A2A 端侧智能体协议]] 和 [[数据溯源分级与单调棘轮]] 都挂着这个问题，至今未解）
- [ ] **A2A 的 opaque 设计（不暴露内部逻辑）和可审计要求天然冲突。** 对方是黑箱，出了事怎么定责？国标"审计标准"落地后这条会不会变成硬矛盾？

---

## 附：来源清单（2026-08-06 核实）

| 事实 | 来源 | 类型 |
|---|---|---|
| A2A 定位、AgentCard、与 MCP 互补、"A2A 不是什么"、治理与 TSC 成员 | `a2a-protocol.org/latest/`（官网首页） | **一手** |
| A2A vs MCP 详细对照、修车行比喻、"A2A Server 可暴露 skill 为 MCP 资源" | `a2a-protocol.org/latest/topics/a2a-and-mcp/` | **一手** |
| v1.0 四大特性、Web 对齐架构、v0.3→v1.0 迁移设计、"强调成熟而非重造" | `a2a-protocol.org/dev/announcing-1.0`（官方公告） | **一手** |
| 150+ 组织、22,000+ star、5 种 SDK、Azure AI Foundry / Bedrock AgentCore 集成、AP2 60+ 机构、UCP 兼容、A2A 路线图、Cisco 关于 AGNTCY 的表态 | Linux Foundation 新闻稿，**2026-04-09** | **一手** |
| AAIF 成立、三创始项目（MCP/goose/AGENTS.md）、白金成员名单、MCP 10,000+ server | Linux Foundation / aaif.io 新闻稿，**2025-12-09** | **一手** |
| ANP 三层架构、did:wba、WNS、Agent DID / Group DID、AD 描述与发现、设计原则 | `agent-network-protocol.com` 官网 + 技术白皮书 + ANP 1.1 规范 | **一手** |
| SLIM 定位（"A2A 定义说什么，SLIM 定义怎么送达"）、MLS 加密、承载 A2A/MCP | `slim.agntcy.org` 官方文档 | **一手** |
| AGNTCY 组件（OASF / dir / Identity / SLIM / Observability）、AGP 更名为 SLIM | AGNTCY 官网 + 第三方整理（hivebook） | 一手 + 三方 |
| Cisco 捐赠 AGNTCY 给 LF、创始成员（Cisco/Dell/Google Cloud/Oracle/Red Hat）、70~75+ 参与公司 | TheNewStack 报道（引 Cisco 公告） | 三方（引一手） |
| IBM ACP 并入 A2A、Kate Blair 进入 TSC、BeeAI 迁移路径 | IBM 官方博文《ACP Joins Forces with A2A》 | **一手** |
| A2A 2025-04-09 发布、50+ 启动伙伴、2025-06-23 捐 LF | 三方整理（stellagent / agentmarketcap） | ⚠️ **三方** |
| W3C AI Agent Protocol CG、WebMCP、IETF、OpenID、NIST CAISI（2026-02-17） | Agentic Futures Initiative《The Agentic Standards Landscape》one-pager | ⚠️ **三方汇编** |
| MCP 侧全部事实 | 沿用库内 [[MCP 与设备侧 MCP]]（2026-08-05 核实） | 库内 |

**⚠️ 待核实清单**

1. **A2A 捐给 Linux Foundation 的确切日期与组织归属**——三方源给 **2025-06-23**（成立 Agent2Agent Protocol Project）；另有源称 **2025-12 并入 AAIF**；LF 2026-04 官方新闻稿只说 "hosted by the Linux Foundation"，未提 AAIF；**AAIF 官网项目页列出的是 MCP / goose / AGENTS.md / agentgateway，不含 A2A**。→ **三个说法需要一次一手源对齐**（此项同时是库内 [[MCP 与设备侧 MCP]] 遗留待核实项，本文把矛盾定位得更清楚了，但**仍未解决**）。
2. **A2A v1.0 确切发布日期**——只能确定早于 2026-04-09；三方称"2026 年初"/"2026-03"，**未采信**。
3. **IBM ACP 并入 A2A 的时间**——三方源分歧：2025-08 vs 2025-09；IBM 官方博文原文未见明确日期。另有源称并入的是 **"LF AI & Data"** 而非 LF 直属项目，与其它表述冲突。
4. **UCP 的全称、主体与状态**——LF 新闻稿提及但未展开，本文未核实，**不要对外引用**。
5. **AAIF 成员规模**——LF 官方 2025-12 只给白金成员名单；三方（AFI one-pager）称已增至"约 190 家组织"，**未采信为官方口径**。
6. **ANP 的发起主体、治理模式与真实采用率**——只核实到规范文本本身存在且完整（1.1 版），**未见任何生产部署证据**；不得称其为"主流协议"。
7. **AGNTCY 参与公司数**——"70+" / "75+" 两种口径并存。
8. **一切效益百分比数字**（"解决时长 -60%"、"开发效率 +50%"、"IT 成本 -30%"）——来自三方博客转述的营销材料，**本文一律不采用**。协议是线格式，不产生工作流加速。
9. **Google ADK / OpenAI Agents 生态的协议层立场**——本文只做了名词级提及，**未做任何事实核实**，不得直接引用（对应第三节留白）。

---

#标签/AgentProtocol #标签/A2A #标签/ANP #标签/MCP #标签/端侧意图框架 #标签/协议治理
