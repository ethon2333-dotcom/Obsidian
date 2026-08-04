---
title: MCP 与设备侧 MCP
tags: [MCP, 设备侧MCP, AppFunctions, A2A, 端侧意图框架, 安卓PM, 学习笔记]
created: 2026-08-05
source: 一手源（Anthropic 官方博客 / modelcontextprotocol.io / developer.android.com / Linux Foundation 新闻稿），2026-08-05 核实
---

# MCP 与设备侧 MCP

> 学习定位：把 MCP 这条线**从协议本体一路推到手机上**——它是什么、这两年变成了什么样、"跑在设备上"到底改变了什么，以及它和 A2A、端侧 Intent 框架的边界在哪。
> 本文是**own-words 综合**，不是情报简报。平台细节请点深读链接；我自己的判断写在文末待解问题里。

---

## 一、一句话心智模型

**MCP = 给 AI 应用装的 USB-C 口。**

在 MCP 之前，"N 个 Agent × M 个工具"要写 N×M 套定制接线；MCP 把它压成 **N+M**——工具方按标准写一次 server，所有客户端都能插。

三层记忆（后面第五节展开）：

- **MCP** 管「Agent → 工具」（垂直，往下够东西）
- **A2A** 管「Agent → Agent」（水平，往旁边找人）
- **端侧 Intent 框架** 管「系统 → App 能力」（垂直 + 系统级，OS 当总机）

再加一句最关键的、我自己最容易讲错的：

> **设备侧 MCP 改变的是「工具在哪执行」，它不自动解决「谁在思考」和「数据从哪来」。**

---

## 二、MCP 是什么

### 2.1 谁提出、解决什么

- **Anthropic 于 2024-11-25 开源发布**，创建者 David Soria Parra 与 Justin Spahr-Summers（Anthropic 官方博客原文）。
- **要解决的痛点**（官方原话意译）：再强的模型也被"信息孤岛"困住——每接一个新数据源就要写一套定制实现，连不出规模。MCP 用**一个开放标准替代碎片化集成**。
- 首发三件套：规范 + SDK、Claude Desktop 的本地 server 支持、一批开源参考 server（Google Drive / Slack / GitHub / Git / Postgres / Puppeteer）。早期采用方 Block、Apollo，工具方 Zed、Replit、Sourcegraph 等。

### 2.2 核心概念（这一节记住就够用）

**三个角色**

| 角色 | 是什么 | 手机类比 |
|---|---|---|
| **Host** | 承载模型的宿主应用（IDE 助手、Agent 运行时、聊天客户端） | 装了 Agent 的那个 App |
| **Client** | Host 内部对接**单个** server 的连接器，1:1 关系 | 一个 App 里的一条连接 |
| **Server** | 对外暴露能力的进程 | 被调用的那个服务 |

**Server 给出的三种原语——这个区分很重要**

| 原语 | 谁决定用它 | 语义 |
|---|---|---|
| **Tools** | **模型**决定调用 | 动作，可能有副作用 |
| **Resources** | **用户 / Host** 挂载 | 只读上下文（文件、数据行、API 返回） |
| **Prompts** | **Server** 发布，用户/模型触发 | 工作流模板 |

> 为什么这个区分重要：三者混为一谈，模型就分不清「这是我能看的资料」还是「这是我能干的事」，**权限与副作用的边界就糊了**。做端侧 Agent 设计时同理——只读查询和写操作绝不能是同一类条目。

**Client 反向提供给 Server 的能力**：`sampling`（server 反过来请求宿主的 LLM 推理）、`roots`（文件/URI 边界）、`elicitation`（server 请求用户补充输入）。这条常被忽略——**MCP 不是单向的**，server 也能"回头找人/找模型"。

**传输层**：底座是 **JSON-RPC 2.0**，两种标准传输：

- **stdio**：server 作为本地子进程，管道通信 → 个人工具、本地场景
- **Streamable HTTP**：单个 HTTP 端点，可按需升级为 SSE 流 → 远程 server 的推荐路径
- 早期的 HTTP+SSE（2024-11-05）**自 2025-03-26 起弃用**

### 2.3 为什么说它是分水岭

1. **N×M → N+M**：写一次，被所有客户端复用。这是唯一真正重要的那条。
2. **工具与 Agent 解耦**：工具方和 Agent 方可以独立迭代、独立发版，不必同生命周期。
3. **能力从"硬编码"变成"可发现"**：不再是把 function schema 写死在提示里，而是运行时 `tools/list` 拉取。
4. **所有权中立化**（2025-12 起，见第三节）：一个没人拥有的协议，竞争对手才肯采用。这是它能赢的**制度性原因**，不是技术原因。

### 2.4 什么时候**不**该用 MCP（反 hype 一节）

- 只对接一两个自家团队的工具，且能接受同生命周期演进——直接写就行，不必上协议。
- 延迟极敏感的关键路径——协议开销不是零。
- 运行时已有成熟的原生工具模型且团队已深度投入——迁移成本可能大于收益。

---

## 三、2025—2026 关键进展

### 3.0 先纠一个常见误解：**MCP 没有 "1.0"**

官方 Versioning 文档写得很清楚：MCP 用 **`YYYY-MM-DD` 字符串版本号**，日期表示的是**"最后一次发生向后不兼容变更的日期"**，不是顺序递增的版本号。向后兼容的改动**不**会推进版本号。

所以正确说法是「MCP 2025-11-25 版」「MCP 2026-07-28 版」，**不存在 MCP 1.0**。（有 1.0 的是 A2A，见第五节——两件事很容易被混起来。）

**当前版本：2026-07-28**（官方标注为 current）。

### 3.1 版本时间线

| 版本 | 关键变化 |
|---|---|
| **2024-11-05** | 初始：Host/Client/Server 模型 + Tools/Resources/Prompts 三原语；stdio + HTTP+SSE |
| **2025-03-26** | **Streamable HTTP**（单端点，取代 HTTP+SSE）；**OAuth 2.1 授权框架**；工具行为注解（`readOnly` / `destructive`）；进度通知带 message；音频内容类型；JSON-RPC 批处理（后被移除） |
| **2025-06-18** | 结构化输出（structured output）；**elicitation**；授权收紧：MCP server 明确归类为 **OAuth Resource Server**，强制 **Resource Indicators（RFC 8707）**；移除 JSON-RPC 批处理；`MCP-Protocol-Version` 头变必需 |
| **2025-11-25** | 一周年版：**异步 Tasks**（当时为实验特性）、**无状态化**推进、**Server 身份（`.well-known`）**、官方扩展机制；授权发现改进；JSON Schema 2020-12 |
| **2026-07-28（current）** | **协议核心变无状态**：删除 `initialize` 握手与 `Mcp-Session-Id`；新增强制 `server/discover`；**MCP Apps**（服务端渲染 UI）；Tasks 移出核心变正式扩展；Extensions 框架；**正式弃用政策**；含破坏性变更 |

> 官方博客对 2026-07-28 的定性：**"launch 以来最大的一次修订"**。实际效果是：一台远程 MCP server 从"需要粘性会话 + 共享会话存储"变成"能挂在普通轮询负载均衡后面"。

### 3.2 授权（OAuth）这条线单独拎出来看

这条线的演进最能说明 MCP 在补什么课：

1. **2024-11-05**：没有标准鉴权，各自发挥。
2. **2025-03-26**：引入 **OAuth 2.1 + PKCE**。
3. **2025-06-18**：把**令牌受众绑定**写死——客户端 MUST 带 `resource=`，server MUST 校验受众，**MUST NOT** 把令牌透传给下游 API。堵的是一个很实在的洞：一个恶意 server 骗客户端交出本该给别家的令牌。
4. **2025-11-25**：用 **OAuth Client ID Metadata Document（URL 式注册）**替代脆弱的动态客户端注册（DCR）；加 **client credentials**（机器对机器）；加 **URL 模式 elicitation**——让用户在**自己的浏览器**里完成 OAuth / 支付，凭据**不经过 MCP 客户端**。
5. **2026-07-28**：进一步向 OAuth / OpenID Connect 的实际部署形态靠拢。

> **心智模型**：MCP 的授权史 = 从「你自己想办法」→「把浏览器和 IdP 请回来当可信第三方」。
> 这条对端侧特别有启发：**敏感授权不该由中间层代持，要么下沉到系统，要么弹回给用户本人**——和 Android 17 那套「系统代持的一次性确认」是同一个思路（见 [[Android AppFunctions 设备侧意图 2026]]）。

### 3.3 Registry / 发现机制

- **官方 MCP Registry 于 2025-09 进入预览**，社区驱动，定位是"agent 界的 npm"：一个规范的发布与发现入口，server 可版本化、带元数据、按能力检索。
- **2025-11-25 补上 Server 身份**：server 通过 `.well-known` URL 自述能力——**先读名片，再决定要不要连**，而不是"必须先连上才知道它能干什么"。
- **2026-07-28 的 `server/discover`** 把这件事变成协议内的强制 RPC。

> 三步走的逻辑很清楚：**先能连（transport）→ 再能信（OAuth）→ 最后能找（Registry + 身份）**。任何一个能力协议大概都得走这三步，端侧的也一样。

### 3.4 治理与生态（这一步比任何技术特性都关键）

- **2025-12-09**：Anthropic 把 MCP **捐给 Linux Foundation 旗下的 Agentic AI Foundation（AAIF）**（Linux Foundation 官方新闻稿 + Anthropic 官方博客）。
- AAIF 由 **Anthropic、Block、OpenAI 共同创立**，白金成员含 **AWS、Google、Microsoft、Bloomberg、Cloudflare**。三个创始项目：**MCP（Anthropic）、goose（Block）、AGENTS.md（OpenAI）**。
- 治理模型不变：维护者继续主导，社区输入优先。
- **官方口径的生态数据**（捐赠公告，2025-12）：**10,000+ 活跃公开 MCP server**；已被 **ChatGPT、Cursor、Gemini、Microsoft Copilot、VS Code** 采用；AWS / Cloudflare / Google Cloud / Azure 均有部署支持。

> ⚠️ **数字的坑**：三方媒体的口径分歧很大（月下载 97M vs 110M、server 数 10,000 vs 17,000+ 不等），且统计口径各不相同。本笔记只采信**官方公告口径**，其余标为待核实。
>
> **PM 视角一句话**：当直接竞争对手愿意共同托管你的协议时，协议就已经赢了。技术上 MCP 并不惊艳；**它赢在"没人拥有它"**。

---

## 四、设备侧 MCP（重点）

### 4.1 "在手机上跑 MCP server" 到底意味着什么

| | 传统（云侧）MCP | 设备侧 MCP |
|---|---|---|
| 工具执行发生在 | 别人的机房 | **你手机上的 App 进程里** |
| 读写的是 | 服务方的云端数据 | **设备上已有的状态**（登录态、本地库、草稿、缓存） |
| 前提条件 | App 得有一套云 API | App 只需在本地声明 |
| 运维负担 | 要维护 App 之外的服务 | **不需要** |

差别不是"快一点"，是**三件事换了性质**：数据不必出端 / 不必要求 App 有云 API / 不必维护 App 之外的服务。

### 4.2 Android AppFunctions 的官方定位

来源：`developer.android.com/ai/appfunctions`（2026-08-05 核实）。这几句是**官方原话**，值得原样记住：

- > "AppFunctions is an Android platform API with an accompanying Jetpack library to **simplify Android MCP integration**. It empowers your apps to **behave like on device MCP servers**…"
- > "AppFunctions serve as the **mobile equivalent of tools** within the Model Context Protocol (MCP). While MCP traditionally standardizes how agents connect to **server-side** tools, AppFunctions provide the same mechanism for Android apps."
- **准入**：调用方 **必须持 `EXECUTE_APP_FUNCTIONS` 权限**才能发现并执行；调用方可以是 agent、普通 App、以及 Gemini 这类 AI 助手。
- **版本**：**Android 16 及以上**。
- **状态**：**实验性预览（experimental preview）**，API 面可能变；截至 **2026-05**，与 Gemini 的集成仅对**可信测试者私测**；官方 FAQ 明说，实验阶段**只有有限数量的 App 和系统 agent 能走通整条 pipeline**；有 EAP 报名通道。

**官方 FAQ 里那段对比最值钱**（"AppFunctions 和 MCP 有什么区别"）：

> "AppFunctions are built-in OS-level hooks **exclusive to Android** that **execute locally**. By contrast, a standard MCP server is a **platform-agnostic** solution that **relies on cloud execution and network round-trips**." ——并补充：用 AppFunctions 可以**直接使用设备上已有的 app state**，且**不需要在 Android app 之外维护服务**。

**还有一条特别容易被忽略的官方表述**（在"How AppFunctions work"里）：

> Agent 在处理用户请求时，**"likely to consider both server-side remote MCP tools and local AppFunctions together"**。

→ 也就是说，**端侧工具和云侧工具是同一份工具清单里的两类条目，不是两套并行系统**。这句是理解"端侧执行总线"的前提，也是我下面那个待解问题的来源。

**标准 MCP server vs AppFunctions 速查**

| 维度 | 标准 MCP server | Android AppFunctions |
|---|---|---|
| 定位 | 平台无关的开放协议 | **Android 专属**的 OS 级 hook |
| 执行位置 | 云端 + 网络往返（官方措辞） | **端侧 App 进程内** |
| 能力描述 | server 自述，`tools/list` 拉取 | `@AppFunction` + KDoc，KSP 构建期生成 XML schema |
| 发现 | 客户端配置 / 官方 Registry / `.well-known` | **Android OS 内置 Registry** |
| 准入 | 客户端自行配置、OAuth | **`EXECUTE_APP_FUNCTIONS` 系统权限** |
| 拿状态 | 需要 App 有云 API | 直接用设备上现成的 App 状态 |
| 运维 | 要维护 App 外的服务 | 不需要 |

技术细节（Registry 硬细节、`isEnabled` 动态可见性、`AppFunctionServiceEntryPoint`、adb 验证命令等）不在这里重复，深读 [[Android AppFunctions 设备侧意图 2026]]。

### 4.3 隐私 / 延迟 / 离线：**必须分开算账**

这三个好处经常被打包成一句"端侧更好"，但它们各自成立的条件不一样：

**隐私 —— 只对"执行"那一段成立**

- ✅ 受益的是执行段：参数和结果留在设备，不经过第三方服务器。
- ⚠️ 但**理解那一段不一定**：库内 [[Android AppFunctions 设备侧意图 2026]] 已记录官方明示 **"system agents may process user queries on the server"**。
- → 准确表述是：**「执行在端侧」≠「全链路在端侧」**。用户说的那句话本身，可能还是上了云。这是最容易被自己的 PPT 骗过去的一句。

**延迟 —— 省掉的是"下半程"**

- ✅ 省掉「Agent → 云 server → 服务方后端」的网络往返和冷启动。
- ⚠️ 但如果 **Planner 本身在云上**，端到端延迟仍被云上那一跳支配。
- → 真正的低延迟需要 **端侧 Planner + 端侧工具** 两头都齐。AppFunctions 只搞定了工具这一头。

**离线 —— 三个条件缺一不可**

端侧模型 + 端侧工具 + 本地数据。AppFunctions 只解决第二项；被调 App 自己若要联网（查快递、下订单），照样离不了线。

> 一句话收口：**设备侧 MCP 是"执行侧的本地化"，不是"全栈本地化"。** 对外讲隐私时必须限定到执行段，否则就是过度承诺。

### 4.4 与"端侧 Agent 执行总线"的关系

**端侧执行总线**是那根 OS 级的主干：`语义理解 → 路由 → 选通道 → 执行 → 结果回显`。设备侧 MCP 是这根总线上**结构化通道的一种具体形态**，不是总线本身。

Android 的三条通道分工（详见 [[端侧执行通道 GUI 与 MCP 路线之争]]）：

| 通道 | 干什么 | 对应 |
|---|---|---|
| built-in intents | 拉起并履约 | 传统意图 |
| **AppFunctions** | **带类型参数调用 + 返回结构化结果** | **← 设备侧 MCP 在这里** |
| UI Automation | 未适配长尾的兜底 | GUI 路线 |

**为什么它算"总线"而不只是一个 API**——因为三件事都被收进了 OS：

1. **发现**：OS 内置 Registry，不是各 Agent 自己维护清单
2. **准入**：`EXECUTE_APP_FUNCTIONS` 是系统权限，不是 App 之间私下约定
3. **编排**：agent 把端侧工具和云侧 MCP 工具放在**同一份清单**里统一挑

App 只负责"声明"。这意味着 **App 从「被点的界面」退化成「被调的工具」**。

> **PM 判断**：一旦工具目录由 OS 托管，**入口价值就从 App 图标转移到系统 Agent**。这才是国内厂商和超级 App 真正在争的东西——不是技术接口，是入口所有权。见 [[国内安卓厂商做 App Intent 的阻力]]、[[App Intent 的核心作用]]。
>
> 另一面：端侧结构化通道能不能推起来，取决于能否被量化验证。评测侧见 [[Local Agent Bench 端侧智能体基准]]。

---

## 五、三者边界对照表：MCP / A2A / 端侧 Intent 框架

| 维度 | **MCP** | **A2A** | **端侧 Intent 框架** |
|---|---|---|---|
| 一句话 | Agent **调工具** | Agent **调 Agent** | 系统**调 App 能力** |
| 方向 | 垂直（Agent ↕ 工具） | 水平（Agent ↔ Agent） | 垂直 + 系统级（OS ↕ App） |
| 被调方是什么 | 工具端点 | **另一个自治 Agent（黑箱）** | App 声明的能力 |
| 被调方有自主性吗 | ❌ 执行确定动作 | ✅ 自己决定怎么做、可拒绝 | ❌（但 App 可自行插确认） |
| 任务模型 | 以请求-响应为主，长任务靠 Tasks 扩展 | **长任务是一等公民**（状态机） | 平台各异 |
| 发现机制 | `tools/list` + 官方 Registry + `.well-known` | **AgentCard**（`/.well-known/agent-card.json`，v1.0 起支持签名） | **OS 内置 Registry** |
| 治理 | AAIF / Linux Foundation（原 Anthropic，2025-12 捐赠） | Linux Foundation（原 Google 提出，v1.0 于 2026 初发布） | **各 OS 厂商自定，不互通** |
| 典型场景 | 接数据源、接 SaaS、接内部服务 | 跨组织 / 跨框架的任务委派 | 设备内 App 能力调度 |
| 互斥吗 | **完全不互斥**：Agent **内部**用 MCP，Agent **之间**用 A2A，**端上落地**用 Intent 框架 |

**怎么快速判断该归到哪一类（判断题）**

- 被调用方**会自己做决定、可以拒绝、有生命周期** → **A2A**
- 被调用方**只是按你给的参数执行** → **MCP**
- 被调用方**必须由 OS 授权和路由才能碰** → **端侧 Intent 框架**

**三者的共同点（这条最值得记）**

它们其实是同一件事的三个切面：**让能力可被机器①描述、②授权、③调用**。

| | 描述 | 授权 | 调用 |
|---|---|---|---|
| MCP | `tools/list` / schema | OAuth 2.1 + 受众绑定 | JSON-RPC over stdio / HTTP |
| A2A | AgentCard（可签名） | OAuth / mTLS / API Key | JSON-RPC / gRPC / HTTP |
| 端侧 Intent | KDoc → XML schema / 意图声明 | 系统权限（如 `EXECUTE_APP_FUNCTIONS`） | OS Registry + Manager |

→ **AgentCard、`tools/list`、OS Registry 是同一个概念的三种实现。** 看懂这一层，再看任何新协议都不会晕。

深读：A2A 侧见 [[A2A 端侧智能体协议]]（含端侧 A2A vs Google A2A 的层级纠偏）；端侧 Intent 框架全景见 [[端侧意图框架 学习笔记]]。

---

## 六、库内关联

- **平台落地**：[[Android AppFunctions 设备侧意图 2026]]（AppFunctions 全部技术细节的深读入口）
- **通道路线**：[[端侧执行通道 GUI 与 MCP 路线之争]]（结构化 vs GUI 的选型判断）
- **横向协议**：[[A2A 端侧智能体协议]]（Agent 之间那一层）
- **主题全景**：[[端侧意图框架 学习笔记]]（四平台格局 + 核心构件地图）
- **PM 判断**：[[App Intent 的核心作用]] · [[国内安卓厂商做 App Intent 的阻力]]
- **评测**：[[Local Agent Bench 端侧智能体基准]]

---

## 七、待解问题

- [ ] **端侧工具与云侧工具同处一份清单时，谁定排序/择优规则？** 官方明说 agent 会"同时考虑" remote MCP tools 与 local AppFunctions，但**没看到消歧或优先级规则**。如果 Agent 系统性偏向云侧同名工具（服务方付费、自家生态、模型更熟），那 App 花力气做端侧适配是不是形同虚设？→ **待核实：Google 是否有公开的工具选择/排序策略。**
- [ ] **AppFunctions 走"开发者自由声明 schema"路线（KDoc 即描述），当多个 App 注册了语义近似的工具，OS 凭什么消歧？** 官方给的只有 Agent Skill 里的 KDoc Refinement 一步（提升单个描述质量），**未见消歧/竞价/排序 API**。对比鸿蒙"仅支持预置垂域、不允许自定义"（见 [[端侧意图框架 学习笔记]] 6.1），两条路线的代价分别落在哪？→ **待核实。**
- [ ] **MCP 侧 2025-03 就有 `readOnly` / `destructive` 工具注解，Android 为何把破坏性动作的确认下放给 App 自己实现？** 既然官方定位 AppFunctions 是"MCP 工具的移动端等效"，为什么不把这套已有的副作用语义一并搬进来、由系统统一处置确认？是能力缺口，还是刻意的责任切分？→ **待核实一手依据**（现有判断来自 [[Android AppFunctions 设备侧意图 2026]] 的 08-03 增补）。

---

## 附：来源清单（2026-08-05 核实）

| 事实 | 来源 |
|---|---|
| MCP 发布日期、创建者、要解决的问题、首发组件 | Anthropic《Introducing the Model Context Protocol》，2024-11-25 |
| 日期版本制、当前版本 2026-07-28 | modelcontextprotocol.io — Versioning |
| 各版本变更、Streamable HTTP、无状态化 | modelcontextprotocol.io — Changelog / Transports；MCP 官方博客（2026-07-28 RC、2025-09-26 next version update） |
| 捐赠 LF / AAIF、创始成员、官方生态口径 | Linux Foundation 新闻稿 2025-12-09；Anthropic《Donating the Model Context Protocol…》；OpenAI 同日博文 |
| AppFunctions 定位 / 权限 / 版本 / 实验状态 / 与 MCP 的 FAQ 对比 | developer.android.com/ai/appfunctions（含中文镜像 android-docs.cn） |
| A2A v1.0 特性与 MCP 互补定位 | a2a-protocol.org《A2A Protocol Ships v1.0》 |

**⚠️ 待核实清单**

- MCP 生态规模的三方数字（月下载量、server 总数）口径分歧大，本文一律不采用，只保留官方公告口径。
- A2A 捐赠 Linux Foundation 的确切时点：多方源在 **2025-06（Agent2Agent Protocol Project 成立）** 与 **2025-12（并入 AAIF）** 之间说法不一；库内 [[A2A 端侧智能体协议]] 记为 2025-04，**三者需要一次一手源对齐**。
- A2A v1.0 的确切发布月份（2026-03 / "early 2026" 两种说法），待一手源。
- AppFunctions 随 Android 17 的正式发布节点，库内已记为「Android 17 同期（日期待补）」，本文沿用。

---

#标签/MCP #标签/设备侧MCP #标签/AppFunctions #标签/端侧意图框架
