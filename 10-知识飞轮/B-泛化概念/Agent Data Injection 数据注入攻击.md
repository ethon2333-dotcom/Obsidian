---
type: concept
status: draft
derived_from: "[[AppIntent 每日情报 2026-08-03]]"
date: 2026-08-03
source:
  - "https://arxiv.org/abs/2607.05120 （Agent Data Injection Attacks are Realistic Threats to AI Agents，2026-07-06）"
  - "https://labs.cloudsecurityalliance.org/research/csa-research-note-agent-data-injection-attack-class-20260718 （CSA 研究简报，2026-07-18）"
tags: [ADI, XPIA, 执行安全, 元数据, OS-Agent, 攻击面]
---

# Agent Data Injection 数据注入攻击

## 一句话定义

**ADI（Agent Data Injection）** 是间接提示注入（IPI）的一个**全新子类**：攻击者**不注入任何指令**，而是伪造 Agent 视为可信的**安全关键元数据**（资源标识符、数据来源标记、发件人字段、工具调用/响应格式），让 Agent **基于被污染的结构自己推出错误结论**，从而执行攻击者想要的动作。

## 为什么重要

- **它掀翻了整个 IPI 防御的前提假设。** 2023 年以来所有防御都假设「攻击 = 伪装成数据的**指令**」，于是去找命令式语气、过滤祈使句、训练护栏模型识别注入命令。ADI 的载荷里**一句指令都没有**。
- **同环境对照数字极其悬殊**：经典指令注入成功率 **0–0.7%**，ADI 最高 **100%**。这不是防御强度不够，是**打错了靶子**。
- **它是 Agent 时代的 SQL 注入**（CSA 类比）。SQL 注入的根因是「应用没有分离 SQL 代码与用户数据」，修复靠**参数化查询这种架构改造**，不是靠过滤器。ADI 的根因同构：**当代 Agent 不隔离可信数据与不可信数据**。
- **对 OS 级 Agent 是直接威胁**：四平台的意图元数据（Android `AppFunctionMetadata`、Apple `AppEntity` 标识符 / View Annotations、HarmonyOS A2A 消息格式）**全部落在 ADI 定义的攻击面内**。

## 技术核心：概率性分隔符注入

**probabilistic delimiter injection** —— LLM 对大括号、引号、转义符这类**结构分隔符的解析是概率性、近似的**，不像确定性解析器那样要求精确匹配。攻击者因此可以**在一个 Agent 视为纯文本的字段内部，伪造出看起来可信的结构**，让模型误判字段边界与数据归属。

> 关键区别：**指令注入伪装的是「语义」（这句话看起来像命令吗），ADI 伪装的是「结构」（这段内容属于哪个可信字段）。** 语义可以被检测，结构在 LLM 眼里本就模糊。

## 适用边界

- **适用**：任何把外部数据结构化后喂给 LLM 的 Agent —— web agent（DOM）、coding agent（工具响应/仓库元数据）、OS 级 Agent（意图 Registry 元数据）、多 Agent 协作（消息格式）。
- **不适用/需注意**：ADI 描述的是**攻击类别**而非具体漏洞，不能靠打某个补丁关闭；它也**不取代**指令注入，两者可叠加。
- **防御边界**：过滤器类防御**完全无效**；只有**架构级隔离**（数据来源追踪、可信/不可信分区）有效，且当前均伴随可用性下降。

## 证据与例子（2026-07-06 论文，未复现）

**团队**：Woohyuk Choi、Juhee Kim、Taehyun Kang、Jihyeon Jeong、Luyi Xing、Byoungyoung Lee（**首尔国立大学 + 伊利诺伊大学厄巴纳-香槟分校 + Largosoft**）。19 页 / 19 图 / 7 表。⚠️ 部分二手报道机构名有误，以 arXiv 与 CSA 简报为准。

**三类攻击场景与中招的商用 Agent**：

| 场景 | 机制 | 中招产品 |
|---|---|---|
| **任意点击** | 伪造界面元素标识符 → Agent 点到攻击者指定位置；任何含 UGC 的页面均可载荷 | Claude in Chrome、Antigravity、Nanobrowser |
| **RCE** | 在 GitHub issue **冒充项目维护者**发评论 → Agent 在开发者机器执行恶意命令 | Claude Code、Codex、Gemini CLI |
| **供应链** | 伪造**工具执行历史**，让 Agent 相信 PR 已验证 → 合入恶意 PR 而未真正检查 | Claude Code、Codex、Gemini CLI |

**📊 成功率与防御失效（论文 / CSA 口径，未复现）**：

| 项目 | 数值 |
|---|---|
| ADI（JSON 结构化数据） | **31.3% – 43.3%** |
| ADI（网页 DOM 数据） | **33.3% – 最高 100%** |
| 真实商用 Agent（无专用攻击工具） | **最高 50%** |
| 经典指令注入（同环境对照） | **0 – 0.7%** |
| 输入 / 输出过滤器 | **完全失效** |
| dual-LLM 无严格策略 / CaMeL-No-Policy | 仍有 **25.0%** |
| CaMeL Normal | **23.1%**（作者报告存在污点传播 bug） |
| Progent | **22.2%** |
| 数据格式随机化 | **28.7%** |
| **CaMeL Strict** | **0%** —— 代价：可用性 **81.2–84.8% → 36.5%** |
| 数据消毒（sanitization） | 有效但可用性降至 **67.9–72.3%** |

**披露状态**：发表前已报告 **Anthropic、OpenAI、Google、Nanobrowser**，**前三家确认**。团队公开了**测试套件与 AgentDojo 扩展版**供第三方独立验证——这使其区别于一次性 PoC。

**作者结论（原文）**：`current agents do not isolate trusted data from untrusted data` —— 不是实现 bug，是**架构级缺失的基础安全原则**。

## 可复用启发

1. **判断一个 Agent 安全方案是否过时，只需一问：它假设攻击载荷长什么样？** 若答案是「像指令」，它对 ADI 无效。
2. **「安全 vs 可用」的兑换率现在有了锚点**：ADI 归零 = 可用性掉到 36.5%。任何声称「零损耗防注入」的方案都应被质疑。
3. **元数据必须有来源（provenance）**。凡是 Agent 会当作「事实」而非「内容」来读的字段（ID、来源、发件人、工具响应），都需要完整性保护，否则就是 ADI 靶面。
4. **对 OS PM 的落地判据**：设计意图 Registry 时，除了问「Schema 描述得清不清楚」，必须加问 **「这条元数据能被第三方伪造吗？系统怎么验证它的来源？」**
5. 与 [[Dual View 智能体数据视图隔离]] 配对理解：**ADI 说明问题（不隔离可信/不可信数据），DualView 给出一种架构级答案。**

## 四平台待查清单（截至 2026-08-04 均无公开评估）

| 平台 | 潜在靶面 | 是否有公开来源校验 |
|---|---|---|
| **Apple** | `.appEntityIdentifier` / View Annotations 实体标识符 —— **正是场景一的靶心形态** | 官方文档未见说明（待补） |
| **Android** | `AppFunctionMetadata`（KDoc 编译产出）、`app_metadata` manifest 属性、工具响应格式 | 未见（待补） |
| **HarmonyOS** | A2A 端侧/云侧消息格式、Skill 元数据 | 未见（待补） |
| **Windows** | Agent Workspace 内工具调用/响应格式 | 未见（待补） |

## 2026-08-04 增补：ADI 的「正面答案」出现了，但不在 OS 层（来源 [[AppIntent 每日情报 2026-08-04]]）

连续第 3 天挂着的跨日待办「四平台是否对意图元数据做来源校验」，本次有**实质进展但仍未解决**——结论从「没人做」精化为**「治理层已有成熟模型，OS 层仍空白」**。

**① 微软 Agent Governance Toolkit 给出了可落地的数据溯源模型**（`microsoft.github.io/agent-governance-toolkit`，开源治理层，**非 Windows OS 内建**）：

- **来源六类枚举**：`tool_output` / `api_response` / `agent_message` / `user_input` / `database` / `file` —— 正好覆盖 ADI 论文三类攻击场景的载荷入口（DOM=tool_output、GitHub 评论=api_response、伪造工具历史=tool_output）。
- **四级分类 + 单调棘轮**：`public → internal → confidential → restricted`，**只升不降**。数据一旦被标为高敏，下游任何环节都不能悄悄降级——这正是 ADI「伪造结构让 Agent 自己推出错误结论」最缺的那道闸。
- **多段流水线闸口**：`post_tool`（工具返回即打标）与 `pre_output`（输出前复核）两阶段拦截。
- 详见新建概念节点 [[数据溯源分级与单调棘轮]]。

**② Project Perception（微软，2026-08-03 公开预览）把「工具调用/响应」当成可检查流量**：Defender for Endpoint 直接检查 agent loop 三段——用户提示、工具调用、工具响应——并在执行前阻断。这是**首个端点侧把 ADI 靶面纳入实时检测**的机制（此前防御全在模型/框架层）。CyberGym 口径 95.95–96%（两处口径不一，待官方确认）。

**③ 对本笔记结论的修正**：

| 此前判断 | 2026-08-04 修正后 |
|---|---|
| 「架构级隔离有效但都伴随可用性下降」（CaMeL Strict 归零→可用性 36.5%） | 仍成立，但**多了一条中间路线**：不做强隔离，只做「来源打标 + 单调棘轮 + 输出前复核」，成本远低于 Dual View（后者约 15× 调用开销） |
| 「元数据必须有来源（provenance）」是原则性建议 | 已有**可抄的字段级 schema**（六类来源 + 四级分类 + 不可降级），OS PM 可直接拿去做 Registry 最小字段提案 |
| 四平台全部「未见」 | 仍全部「未见」——**已 WebFetch 复核 Windows agentic security 官方文档，确认 OS 层无数据来源分级**；治理层的成熟不等于 OS 层的采纳 |

⚠️ **不要混淆层级**：AGT 是应用/治理层开源工具包，Windows 作为 OS **没有**把它内建成系统能力。四平台待查清单**保持全部待补**，跨日待办继续挂起（连续第 4 日）。

## 2026-08-09晚 增补：待办第二次实质进展——结论从「两层」精化为「三层」（来源 [[AppIntent 每日情报 2026-08-09-晚]]）

连续第 6 日挂起的最高优先待办「四平台是否对意图元数据做来源校验」本轮取得**第二次实质进展**，方向与 08-04 完全不同：08-04 找到的是**治理层**答案（微软 AGT），本轮找到的是**客户端 / 浏览器层**答案（Chrome）。

**Chrome Agent Origin Sets**（Nathan Parker，Chrome security team，**2025-12-08**，security.googleblog.com）——详见 [[Chrome Agent Origin Sets 与用户对齐评判器 2026]]：

- 按任务会话维护 **read-only / read-writeable** 两个 origin 白名单，由**不暴露给不可信内容的确定性门控函数**把关；
- **关键一句**：`"the planning model may ingest other non-web content such as from tool calls, so we also delineate those into read-vs-write calls and similarly check that those calls are appropriate for the task."` —— **tool call 也被划成读 / 写**。OS 意图框架里每个 intent 本质就是一次 tool call，**这是可直接迁移到意图 Registry 的原语**。

### 结论演进（三次修订）

| 时点 | 对「谁做了读入路径分级」的判断 |
|---|---|
| 2026-08-03 | 没人做（仅 CaMeL / Dual View 等**研究层**方案，且可用性代价大） |
| 2026-08-04 | **治理层**有成熟模型（AGT 六类来源 + 四级密级 + 单调棘轮），**OS 层空白** |
| **2026-08-09晚** | **三层**：研究层有方案 / 治理层有模型 / **客户端层已产品化（Chrome）**；**OS 意图层仍然全空白** |

### 四平台待查清单（更新：新增「跨层参照」列）

| 平台 | 潜在靶面 | 是否有公开来源校验 | 跨层已有的可抄原语 |
|---|---|---|---|
| **Apple** | `.appEntityIdentifier` / View Annotations 实体标识符 —— **正是场景一的靶心形态** | 官方文档未见（**待补**，连续第 6 日） | Chrome：调用级读 / 写划分 |
| **Android** | `AppFunctionMetadata`（KDoc 编译产出）、`app_metadata` manifest 属性、工具响应格式 | 未见（待补） | 同属 Google，但 **Chrome 的 origin set 未下沉到 AppFunctions** |
| **HarmonyOS** | A2A 端侧 / 云侧消息格式、Skill 元数据 | 未见（待补） | — |
| **Windows** | Agent Workspace 内工具调用 / 响应格式 | 未见（已 WebFetch 复核官方文档确认无） | AGT（治理层，非 OS 内建） |

⚠️ **层级纪律再强调**：Chrome 是**浏览器**，Origin Sets **没有**下沉为 Android 的 AppFunctions 能力。同一家公司在两条产品线上的成熟度不可互相代入——这是本待办连续 6 日最容易被误判「关闭」的一处。

**新增可执行判据（给 OS PM）**：意图 Registry 的最小防 ADI 字段，从此前的「六类来源 + 四级密级」（成本高）**降级出一个最低版本**——只加一个 `readOrWrite` 声明位。不需要密级体系，就能让系统拒绝「把读来的数据自动喂进写动作」，这是当前四平台**最低成本的补丁形态**。

## 2026-08-15 增补：`.appEntityIdentifier` 澄清 —— 它不是来源校验，是「实体-视图链接」

> 来源：[[AppIntent 每日情报 2026-08-15]]。关闭连续第 7 日最高优先待办的一个**错误前提**。

此前待办把 Apple `.appEntityIdentifier` 当作「意图元数据来源绑定/签名」的候选项去查。本轮逐条核验 Apple 官方文档，结论：
- `NSUserActivity.appEntityIdentifier`：「The identifier of an app entity that you associate with the user activity... make the entity available to Siri and Apple Intelligence.」—— 把**实体关联到一个用户活动**（如 Now Playing / 通知 / 闹钟），使之可被 Siri 理解。
- `UIView.appEntityIdentifier` / `SwiftUI .appEntityIdentifier(_:)`：「Associate your view with one app entity to make its content discoverable by Apple Intelligence and Siri **when the view appears onscreen**.」—— 即 Session 343 **View Annotations** 的实体-视图链接，用于**屏幕感知（onscreen awareness）**。

→ **`.appEntityIdentifier` 解决的是「这个视图/活动对应哪个 app 实体」的**可发现性**问题，完全不涉及「这条实体数据的来源是否可信 / 是否经过签名校验」。** 它既不含来源签名，也不提供 ADI 意义上的来源分级。

**因此：四平台意图元数据来源分级这一最高优先待办，不能借 `.appEntityIdentifier` 关闭——Apple 侧依旧没有任何「来源绑定/签名」API（AI生成等尚未核实）。** 截至本窗口，四平台 OS intent 层在该维度**仍全空白**（Apple 视图链接 / Android app_metadata 无来源标记 / HarmonyOS 未公开 / Windows 官方文档已确认无）。最低成本补丁形态仍回到本笔记此前的判据：**意图 Registry 加 `readOrWrite` 声明位**，由应用/系统显式标注每条读入数据的读写意图，拒绝「读来的数据自动喂进写动作」。

## 关联

- 索引：[[意图框架·跨体系索引 MOC]]
- 来源：[[AppIntent 每日情报 2026-08-03]] ｜ [[AppIntent 每日情报 2026-08-04]] ｜ [[AppIntent 每日情报 2026-08-09-晚]]
- 客户端层答案：[[Chrome Agent Origin Sets 与用户对齐评判器 2026]]
- 上位/相邻概念：[[XPIA 跨提示注入]] ｜ [[文档型 XPIA 自传播蠕虫]] ｜ [[Dual View 智能体数据视图隔离]] ｜ [[数据溯源分级与单调棘轮]]
- 防线：[[Confirmation UI 安全机制]] ｜ [[Agent Workspace 隔离执行]] ｜ [[Agent 身份与硬件级审批]]
- 方法：[[Agent 读入路径可信数据边界 SOP]] ｜ [[Agent 写回路径 XPIA 风险评估 SOP]]
- 平台节点：[[Android AppFunctions 设备侧意图 2026]] ｜ [[Apple AppIntents Schema Protocol 2026]] ｜ [[HarmonyOS Intents Kit 与 ArkAF 2026]] ｜ [[Windows Copilot Actions 与 Agent Workspace 2026]]

## 2026-08-16 增补：待办演进 —— 副作用轴已解，来源轴仍空白（来源 [[AppIntent 每日情报 2026-08-16]]）

> 连续第 8 日最高优先待办「四平台意图元数据来源分级」本轮**取得实质但仍未全解**：结论从「全空白」精化为「**一个轴已解、一个轴仍空白**」。

- **副作用轴（side-effect axis）—— Apple 已解**：Session 347 确认 Apple 通过 schema 的**风险元数据**对意图做 destructive / exfiltration / shared-content 分类，并据此驱动确认与鉴权。这与本笔记「元数据必须有来源（provenance）」「元数据能被伪造吗」的判据**部分重合但不同轴**——它分类的是「**动作有多危险**」，不是「**这条数据从哪来、可不可信**」。
- **来源/溯源轴（provenance axis）—— 四平台仍空白**：Apple 的风险元数据**不含来源签名 / 来源类型字段**；`.appEntityIdentifier` 已证伪为视图链接（08-15 增补）；Android `app_metadata` / HarmonyOS A2A 消息 / Windows 工具响应均**无来源类型字段**。故待办**不关闭，但收窄为「来源轴」**。
- **`createTimer` 是 ADI 的具象实例**：Session 347 的反例——可选 String label 由模型填参、被 prompt injection 设为攻击者值，后续「list timers」把该值拉回上下文污染新上下文——正是本笔记定义的「**伪造结构化元数据让 Agent 自己推出错误结论**」的 ADI 形态（场景一·任意点击的「伪造标识符」同构）。它说明：即便没有「来源分类」，光有「副作用分类」也拦不住**数据经可信字段回流污染**。
- **最低成本补丁形态维持**：意图 Registry 加 `readOrWrite` 声明位（08-09晚 判据），由系统显式标注每条读入数据的读写意图，拒绝「读来的数据自动喂进写动作」。

#标签/ADI #标签/XPIA #标签/安全 #标签/元数据 #标签/攻击面
