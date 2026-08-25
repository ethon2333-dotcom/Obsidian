---
title: Apple Intelligence 端侧架构 学习笔记
tags: [AppleIntelligence, 端侧AI, PrivateCloudCompute, 意图框架, 学习笔记]
created: 2026-08-06
source: 一手源（Apple 官方/ML Blog/WWDC/2026 公开资料），2026-08-06 核实
---

# Apple Intelligence 端侧架构

> 学习定位：这是一篇**广度种子笔记**——先把 Apple Intelligence 的**骨架**铺全（两层架构 / 能力边界 / 与 Siri 和 App Intents 的接线 / 四平台位置 / 2025—2026 演进），**深度留白**。
> 每一节我都刻意只写到"够画架构图"的粒度，具体机制、API 细节、以及我自己的 PM 判断，留在第八节的 `- [ ]` 里慢慢补。
> 已有的深度片段在 [[Apple Intelligence 与 App Intents]]（App Intents 侧 / WWDC26 确认机制），本文不重复，只做**架构侧的补位**。

---

## 一、一句话心智模型

**Apple Intelligence = 把"云"当成设备的一块外接内存，而不是当成一个外部服务。**

别家的路线是"端侧做点小活，重活发给云上的某个 API"；Apple 的路线是**造一朵在信任模型上等同于本机的云**——PCC 上的服务器被要求满足和 iPhone 同一档的安全属性，设备**在密码学上拒绝连接不匹配的服务器**。

所以这套架构真正的设计目标不是"性能分层"，而是：

> **让「上不上云」这个决定，不再改变用户的隐私处境。**

一旦这条成立，模型放端上还是放云上就退化成纯粹的**工程调度问题**（算力、延迟、功耗），而不再是产品/合规问题。**这是整个 Apple Intelligence 架构的支点**，也是我认为最值得安卓侧偷师的一条。

配套的三句话：

- **端侧**负责：低延迟、高频、贴身数据（个人语料、屏幕内容、语义索引）
- **PCC**负责：端上放不下的模型、复杂推理、agentic 工具调用
- **第三方模型（ChatGPT / Gemini）**负责：世界知识与开放生成 —— **这一层是显式征询、边界另算的**

---

## 二、是什么：两层架构（其实是 2 + 1 层）

### 2.1 骨架

```
        用户请求
            │
   ┌────────▼─────────┐
   │  系统调度 / 编排  │  ← Siri、App Intents、System Orchestrator
   └────────┬─────────┘
            │  「这个请求端上能干完吗？」
     ┌──────┴───────┐
     │              │
┌────▼────┐   ┌─────▼──────────────┐
│  端侧    │   │ Private Cloud      │
│  AFM     │   │ Compute（PCC）      │
│（Apple    │   │ Apple silicon 服务器 │
│  silicon）│   │ + （2026）GCP/NVIDIA │
└─────────┘   └─────┬──────────────┘
                    │
          ┌─────────▼──────────┐
          │ 第三方模型（ChatGPT）│ ← 显式征询，边界另算
          └────────────────────┘
```

**关键：前两层是"同一个信任域"，第三层不是。** 我一开始把三层当成"由弱到强的算力阶梯"来理解，是错的——前两层之间的界线是**工程界线**，第二层和第三层之间的界线是**信任界线**。这两种界线的性质完全不同。

### 2.2 端侧那一层（AFM 家族，2026 已到第三代）

来自 Apple ML Research《Introducing the Third Generation of Apple's Foundation Models》（2026-06-08）：

| 模型 | 位置 | 规模 | 角色 |
|---|---|---|---|
| **AFM 3 Core** | 端侧 | **30 亿参数，稠密** | 端侧基线模型（初代 3B 的下一代） |
| **AFM 3 Core Advanced** | 端侧 | **200 亿参数，稀疏；单次仅激活 1—4B** | 最强端侧模型，**原生多模态**；仅"最强的 Apple silicon 系统"解锁 |
| **AFM 3 Cloud** | PCC | 未公布 | 服务端主力（速度/效率/性能） |
| **ADM 3 Cloud (Image)** | PCC | 未公布 | 图像生成与编辑（Image Playground、高级修图） |
| **AFM 3 Cloud Pro** | PCC | 未公布 | 最强服务端模型，**专供 agentic 工具调用与复杂推理** |

**AFM 3 Core Advanced 的架构值得单独记一笔**，因为它解的是**端侧最硬的那道题：DRAM 装不下**。

传统做法（不论稠密还是 MoE）要求**全部权重常驻 DRAM**。Apple 的做法是：

- 全量权重存在 **闪存（NAND）**，不进 DRAM
- 但 NAND→DRAM 带宽太慢，**做不到标准 MoE 那样逐 token 换专家**
- 所以改成 **per-prompt 路由**：一个轻量稠密块在初始处理时选定一组专家，生成过程中**周期性重选**
- 大比例"**常驻共享专家**" + 少量"**按输入换入的路由专家**"，拼成 DRAM 里的一个稠密模型
- 技术名：**Instruction-Following Pruning（IFP）**，Apple 自研

> **这条对做 OS 的我最有用**：它把"模型大小"从**内存约束**里解耦出去了。副产品是**推理时弹性**——按任务难度预设激活参数量（官方举例：语音场景在 1B 激活档位跑），**同一个模型可以按场景变胖变瘦**。
> → 这不是模型技巧，这是**端侧调度原语**。安卓侧要做同类事，得先有对应的存储/内存/调度协同，不是模型团队单方面能干成的。

### 2.3 PCC 那一层：不是"Apple 的云"，是"可验证的云"

PCC 的五条核心要求（Apple Security Research 原文，2024 提出，**2026-06-08 明确重申"remain exactly the same"**）：

| 要求 | 我的理解 |
|---|---|
| **Stateless computation** | 个人数据**只**用于完成本次请求；响应返回后**不可再访问** |
| **Enforceable guarantees** | 所有关键组件都必须可约束、可分析——**不靠承诺，靠可检验** |
| **No privileged runtime access** | **连 Apple 的 SRE 都没有绕过隐私保证的特权接口**。这条最狠 |
| **Non-targetability** | 攻击者**没法只打你一个人**，除非把整个 PCC 系统一起打下来 |
| **Verifiable transparency** | 外部安全研究者可高置信度验证"承诺 = 实现" |

落地手段（一手源）：

- 每个生产版本的 PCC 软件镜像**全部公开供二进制审查**，与透明日志中的度量值可比对；写入日志后**无法在不被发现的情况下移除**
- 设备**只**把请求载荷密钥封装给"证明度量值匹配公开透明日志中某个发布版"的 PCC 节点 → **不匹配就不发**
- **Virtual Research Environment（VRE）**：在 Apple silicon Mac 上跑一个虚拟 PCC 节点，含**虚拟 SEP**，可启动、可调试、可对已发布模型做推理
- 部分安全关键组件**开源**（`apple/security-pcc`：CloudAttestation、Thimble、splunkloggingd、srd_tools）
- **Apple Security Bounty** 覆盖 PCC，赏金与 iOS 同级

> **PM 视角**：PCC 真正的创新不在密码学，在**把"信任"变成了一个可被第三方复核的工程产物**。
> 隐私承诺从"我们保证"变成"你自己去验"——这是一次**举证责任的转移**。任何厂商要对标，抄的不该是架构图，是这个举证结构。

### 2.4 2026 的大变化：PCC 出了 Apple 的机房

《Expanding Private Cloud Compute》（Apple Security Research，2026-06-08）：

- 与 **Google、NVIDIA** 合作，把 **AFM 3 Cloud Pro** 跑在 **Google Cloud 的 NVIDIA GPU** 上——**首次把 PCC 承诺延伸到第三方数据中心**
- 实现底座换了：**NVIDIA Confidential Computing + Intel TDX + Google Titan 芯片**；**五条核心要求不变**
- Apple 明确**不只依赖机密计算**：从固件到宿主/客户机 OS 栈到应用代码**全部算进可信计算基**，一并纳入可验证透明与无特权访问
- 防供应链攻击：对 PCC 舰队中的**全部 GCP 硬件**维护**密码学可验证的仅追加账本**；关键组件的软件证明**根植于两家独立厂商的两个信任根**
- 一句定海神针：> "**Apple retains complete control over PCC software; Apple devices will only trust PCC software that is cryptographically approved by Apple.**"

> **我的判断**：这一步的产品含义比技术含义大。Apple 证明了**"隐私架构"可以是一层能套在别人机房上的抽象**，而不是必须绑定自家硬件。
> 反过来看也成立：**Apple 承认自己的算力供给撑不住 agentic 那一档需求了**——这是架构选择，也是产能妥协。

---

## 三、能力边界：端侧能做什么 / 不能做什么

**先说结论：端侧的边界不是"模型能力"，是「延迟 × 内存 × 功耗 × 数据敏感度」四维联合约束下的可行域。** 拆开看：

| | 典型放**端侧** | 典型放 **PCC** | 典型交给**第三方模型** |
|---|---|---|---|
| **写作** | Rewrite / Proofread / Summarize（系统级 Writing Tools，全系统可用） | 长文、复杂重写 | Compose（从零生成） |
| **图像** | — | **Image Playground / 高级修图（ADM 3 Cloud）** | ChatGPT 图像工具 |
| **摘要** | 通知摘要、邮件摘要、通话/录音摘要 | 超长上下文 | — |
| **个人语料** | **语义索引、个人上下文、屏幕感知** | 仅按需上送**任务相关**片段 | ❌ 需显式征询 |
| **推理 / Agent** | 有限 | **agentic 工具调用 + 复杂推理（AFM 3 Cloud Pro）** | 世界知识问答 |

**端侧做不了 / 做不好的（诚实版）**

1. **重推理与长链 agent**——官方把 agentic tool use 明确划给了 **PCC 上的 Cloud Pro**，不是端侧。
2. **图像生成**——三个 PCC 模型里专门有一个 ADM 3 Cloud (Image)，端侧不承担。
3. **世界知识**——这是 ChatGPT / Gemini 那一层存在的理由。
4. **大上下文**——开发者侧的 PCC 模型给到 **32K token 上下文**，并明确"比端侧模型大得多"（WWDC26 Session 241）；端侧上下文小得多，官方在 iOS 26.4 专门新增了**查询上下文大小 + 计算 token 数**的 API，要求开发者**按运行硬件自适应**。

**"设备算力限制"具体长什么样**

- 初代门槛：**iPhone 15 Pro / 15 Pro Max、M1 及以上的 iPad 与 Mac**（2024 官方口径）
- 2026 新增了**档位分化**：AFM 3 Core 是通用档，**AFM 3 Core Advanced 只被"最强的 Apple silicon 系统"解锁**
- → **端侧 AI 第一次出现了明确的"设备分层"**。这对做 OS 产品是个大事：**同一份系统能力，在不同机型上模型不同**，功能一致性怎么保、怎么讲，是个真问题。

> 一句话收口：**端侧不是"缩小版的云"，是「贴身 + 即时 + 常在」这三件事的专属承包商。** 拿它去比通用能力，方向就错了。

---

## 四、与 Siri / App Intents 的关系：系统级 Agent 入口

### 4.1 分工

| 层 | 角色 | 一句话 |
|---|---|---|
| **AFM（端 + PCC）** | 大脑 | 理解、规划、生成 |
| **Siri** | 入口 + 编排 | 接自然语言，拆解成动作链 |
| **App Intents** | 手脚 | App 把能力声明成**强类型结构化 API** |
| **App Entities + 语义索引** | 记忆 | 让"我上周拍的那张照片"这种指代可解析 |
| **屏幕感知** | 眼睛 | 让"这个""它"这类指示代词可解析 |

WWDC 2024 官方原话（2024-06 新闻稿）值得原样记：

> "With Apple Intelligence, Siri will be able to take **hundreds of new actions in and across Apple and third-party apps**."
> "With **onscreen awareness**, Siri will be able to understand and take action with users' content in more apps over time."

**这套接线的本质**：Apple 没有让模型去"学会用 App"，而是让 App **说一门模型已经会的语言**（App Schema）。所以 Siri 不需要针对某个 App 训练；**反过来，你不对齐 Schema，就永远进不了这套体系**。这条已在 [[Apple Intelligence 与 App Intents]] 展开，本文不重复。

### 4.2 值得单记的两条 2026 结构性变化

- **System Orchestrator**：跨 App 动作**统一由系统编排者路由，App 之间不直接互相驱动**——刻意为隐私与安全设计。
- **确认机制按"影响谁"而非"危不危险"触发**：实体 conform `OwnershipProvidingEntity`、声明 `.shared` / `.public` 后 Siri 才倾向弹确认。
  → 细节见 [[Apple Intelligence 与 App Intents]]。

### 4.3 开发者侧的对称开放：Foundation Models 框架

这条线常被忽略，但它决定了**生态能不能长起来**：

| 年份 | 开放了什么 |
|---|---|
| **WWDC25** | **Foundation Models 框架**：Swift API 直接调用驱动 Apple Intelligence 的**端侧模型**；**引导式生成（Generable）**、**流式**、**Tool 协议（工具调用）**、内置适配器（如内容标记）。卖点：**离线可用 / 无需账号与 API Key / 对开发者与用户零推理费用 / 不增加 App 体积** |
| **WWDC26** | ①端侧模型**从头重建**，工具调用更强，**新增 Vision 图像输入**；②新增 **`PrivateCloudComputeLanguageModel`**：开发者可直接调 PCC 模型（**32K 上下文 + `ReasoningLevel` 推理档位**，无需鉴权/密钥）；③**模型抽象层 `LanguageModel` 协议**——SystemLanguageModel / PCC / **Core AI** / **MLX** / **Anthropic、Google 的 Swift 包**同一套 API 互换；④**Dynamic Profile**（构建 agentic 体验的新原语）；⑤**Evaluations 框架**、`fm` 命令行、**Python SDK**、**Core Spotlight 驱动的 RAG 工具**；⑥**框架开源**，同一套 Swift API 可跑在服务端 |

> **这条比模型本身更有战略含义**：Apple 把「模型选择」变成了**可替换的实现细节**，而把 **API 形态**攥在自己手里。
> 谁定义调用形态，谁就定义生态。这和 [[MCP 与设备侧 MCP]] 那条"能力可被机器①描述②授权③调用"的主线是同一件事——只不过 Apple 用的是**语言级（Swift 协议）**而非**协议级（JSON-RPC）**的抽象。
> ⚠️ 同时注意成本口径：PCC 对**首次下载量 <200 万的开发者**免云 API 费用，iCloud+ 订阅用户额度更高（WWDC26 Session 241）——**这是一条带商业条件的"免费"**。

---

## 五、四平台对标

沿用库内 [[端侧意图框架 学习笔记]] 的四平台框架，本表**只从"端侧架构"这一个切面**重排（不重复意图框架维度）：

| 维度 | **Apple Intelligence** | **Android（AppFunctions）** | **HarmonyOS（元服务 / ArkAF）** | **Windows（Copilot Actions）** |
|---|---|---|---|---|
| 端侧模型 | **AFM 3 Core 3B + Core Advanced 20B 稀疏（激活 1—4B）**，官方公开架构 | Gemini Nano（规格随版本变） | 盘古端侧（规格口径待核实） | Phi Silica 等（待核实） |
| 云侧定位 | **PCC：与设备同信任域，可验证** | 常规云服务 | 常规云服务 | 常规云服务 |
| "理解"在哪跑 | 端 + PCC 协同，**同信任域** | 官方明示"**system agents may process user queries on the server**" | 图谱推理引擎 | 端侧隔离 Agent |
| 隐私的技术保证 | **五条硬要求 + 二进制公开 + 透明日志 + VRE + 赏金** | 权限模型（`EXECUTE_APP_FUNCTIONS`） | 系统权限 + A2UI | 隔离工作区 + 低权限 agent 账号 |
| 执行侧 | App Intents（强类型 Schema） | AppFunctions（≈端侧 MCP server） | 意图 → 技能 → A2A 三层 | MCP 连接器 + ODR |
| 确认由谁做 | **系统级**（按 entity ownership 差异化） | **下放 App 自己实现** | A2UI 系统级渲染 | 隔离工作区 |
| 开发者能否直调端侧大模型 | ✅ **Foundation Models 框架（2026 开源 + 多模型抽象）** | 待核实（有 ML Kit / Gemini Nano API，口径不同） | 待核实 | 待核实 |
| 模型分设备档位 | ✅ **明确分层**（Core / Core Advanced） | 待核实 | 待核实 | 待核实 |
| 生态推行方式 | 单一厂商强推标准 | 群雄割据 | 单一厂商强推标准 | 单一厂商 + 开放协议（MCP） |

> ⚠️ **这张表右三列多处"待核实"是刻意的**——本文是 Apple 侧的种子笔记，安卓/鸿蒙/Windows 的端侧模型规格我没有逐条对过一手源，**不猜**。补齐见第八节。
> 鸿蒙侧现有素材见 [[HarmonyOS 元服务 学习笔记]]；安卓侧阻力见 [[国内安卓厂商做 App Intent 的阻力]]、破局见 [[安卓厂商意图识别破局策略]]。

**从这张表里我目前能提炼的三条差异**

1. **只有 Apple 把"云"纳入了同一个信任域**。其余三家的端云分界仍是传统的"设备 vs 服务"。
2. **只有 Apple 公开了端侧模型的完整架构与参数量**，且做了**显式的设备档位分层**。
3. **确认/安全成本的归属**是最大分歧：Apple 由平台承担，Android 转嫁给开发者。→ 详见 [[Apple Intelligence 与 App Intents]]。

---

## 六、2025—2026 进展

| 时点 | 事件 | 性质 |
|---|---|---|
| 2024-06 | Apple Intelligence 发布；PCC 五条要求提出；ChatGPT 集成宣布 | 一手源 |
| 2024-07-29 | 首批开发者/测试者可用（iOS 18.1 beta，美式英语） | 一手源 |
| 2024-10 | PCC 安全指南、**VRE**、部分源码、Security Bounty 公开 | 一手源 |
| 2025-06 | **AFM 第二代**；**Foundation Models 框架**面向开发者开放（结构化输出 + 工具调用） | 一手源 |
| **2026-06-08** | **AFM 第三代：五模型家族**（2 端侧 + 3 PCC）；**与 Google 合作构建** | 一手源 |
| **2026-06-08** | **PCC 扩展到 Google Cloud + NVIDIA GPU**，五条要求不变 | 一手源 |
| 2026-06（WWDC26） | Foundation Models 框架**开源**；PCC 模型开发者可直调；模型抽象层接入 Anthropic / Google 的 Swift 包；Core AI 新框架；Dynamic Profile / Evaluations | 一手源 |
| 2026 春—秋 | **新 Siri**（个人上下文 / 屏幕感知 / 跨 App 动作）分批交付 | ⚠️ **媒体口径，见下** |

### 6.1 Apple 基础模型：三代路线的变化

- **一代（2024）**：~3B 端侧 + PCC 服务端，全 Apple silicon，全自研。
- **二代（2025）**：服务端引入 **PT-MoE**；框架对外开放。
- **三代（2026）**：**两个转折**——
  1. **端侧内部分层**（Core / Core Advanced），并用 IFP 稀疏架构突破 DRAM 限制；
  2. **不再全自研**：官方原文承认这一代是"**custom-built in collaboration with Google**"，且是"**leverage the technologies behind its Gemini family of models**"。

> **值得警惕的措辞学**：Apple 说的是"借助 Gemini 背后的技术共建 AFM"，**不等于**"Siri 用的是 Gemini"。这两句在中文媒体里被大量混为一谈。我目前**只采信前者**（有一手源），后者的各种版本一律进待核实清单。

### 6.2 设备端语义索引

- 官方 2024 口径给到的是"**personal context**"这一层：Siri 能基于设备上的邮件、消息、文件、日历、照片作答，"用户不必记得那件事是在短信还是邮件里提过的"。
- App 侧的接法是把数据实体交给 **Spotlight 的语义索引**（见 [[Apple Intelligence 与 App Intents]]）。
- **2026 的新信号**：WWDC26 给开发者放出了**由 Core Spotlight 驱动的 RAG 工具**，以及 **Spotlight 系统工具**可挂进 Foundation Models 会话。
  → 也就是说，**语义索引正在从"系统专用"变成"开发者可调"**。这条线我判断在 2027 会更重要，但目前一手细节我没读全。

### 6.3 与 ChatGPT 的集成边界（这一节的重点是"边界"）

2024 官方口径（新闻稿原文，很清楚）：

- > "**Users are asked before any questions are sent to ChatGPT**, along with any documents or photos."
- 免费、**无需创建账号**即可用；订阅者可选择连接账号。
- 隐私措施：**IP 地址被遮蔽**，**OpenAI 不存储请求**；但**一旦连接账号，适用 OpenAI 自己的数据政策**。

> **这条边界的产品设计非常值得抄**：Apple 没有把第三方模型藏在系统里"无感调用"，而是把它做成一次**显式的、逐次的越界确认**。
> **信任域的边界 = 用户可感知的边界。** 这是我目前从这套架构里学到的最迁移得动的一条。
> 对应到安卓：如果厂商 Agent 会把 query 发给云上第三方模型，**这一跳是不是也该做成用户可感知的？**（目前普遍不是。）

---

## 七、库内关联

- **App Intents 侧深读**（Schema / 确认机制 / EntityCollection / System Orchestrator）→ [[Apple Intelligence 与 App Intents]]
- **App Intents 基础概念** → [[App Intent 的核心作用]]
- **底层支撑架构** → [[App Infra 应用基建]]
- **四平台格局与核心构件地图** → [[端侧意图框架 学习笔记]]
- **协议侧对照**（能力如何被描述 / 授权 / 调用）→ [[MCP 与设备侧 MCP]]
- **鸿蒙侧对照** → [[HarmonyOS 元服务 学习笔记]]
- **安卓落地阻力与破局** → [[国内安卓厂商做 App Intent 的阻力]] · [[安卓厂商意图识别破局策略]]
- **结构化路线的对立面（GUI 路线）** → [[工业级 GUI Agent 架构（VLM+无障碍树）]]
- **上下文/个人语料工程** → [[Context Engineering 学习笔记]]
- **主题索引** → [[意图框架·跨体系索引 MOC]]

---

## 八、待解问题（深度留白）

**架构层**

- [ ] **端 / PCC 的路由决策规则到底是什么？** 官方只说"先判断能不能在端上完成"，**没有公开判据**。是模型自评？是按 feature 硬编码？还是有一个 router？→ 这是整套架构里我最想搞清楚、目前**完全空白**的一块。
- [ ] **AFM 3 Core Advanced 的 per-prompt 专家路由，选错了会怎样？** 生成中"周期性重选"意味着中途可能换专家——**换的那一刻输出质量会不会跳变**？有没有回退机制？
- [ ] **IFP + NAND 常驻这套方案对闪存寿命和功耗的代价是多少？** 官方通篇讲延迟与规模，**没提写入/读取放大与耗电**。做 OS 的必须问这个。
- [ ] **端侧模型分档（Core / Core Advanced）之后，功能一致性怎么保？** 同一句话在两台机器上给出不同质量的结果，产品上怎么表达？降级策略是什么？

**PCC 层**

- [ ] **"stateless" 与"多轮对话"怎么共存？** PCC 安全指南里有 **Multi-Turn Agent**，描述为"**bounded cross-request state**"——**有界的跨请求状态**。这和"无态"是什么关系？边界划在哪？→ 需要读 PCC Security Guide 原文。
- [ ] **PCC 上了 GCP 之后，威胁模型实际扩大了多少？** Apple 说全栈纳入 TCB、双信任根、硬件账本；但**Google 仍是物理运维方**。这套设计能挡住的和挡不住的，各是什么？
- [ ] **"设备拒绝连接不匹配的 PCC 节点"——拒绝之后发生什么？** 功能静默降级到端侧？报错？用户可感知吗？→ 这是可用性与安全性的交换点，**官方材料我没找到**。

**Siri / App Intents 层**

- [ ] **新 Siri 的实际交付状态到 2026-08 究竟如何？** 媒体口径混乱（见待核实清单），**我需要一次以 Apple 官方发布说明为准的核对**。
- [ ] **屏幕感知与语义索引的数据，会不会进 PCC？** 如果会，"任务相关数据才上送"的粒度由谁判定？
- [ ] **Foundation Models 框架接入第三方模型（Claude / Gemini 的 Swift 包）后，隐私叙事怎么自洽？** 同一套 API，一个跑在 PCC 一个跑在别人的服务器——**用户在 App 里能分辨吗？** Apple 有没有强制的披露要求？→ **这可能是整套隐私叙事最脆弱的一处**，值得重点追。

**对标层（本文最大的空缺）**

- [ ] 第五节表格右三列的空白：**安卓 / 鸿蒙 / Windows 各自端侧模型的参数量、内存占用、是否分档、开发者可否直调**——全部待补一手源。
- [ ] **有没有第二家在做"可验证的云"？** 机密计算的原语大家都有，Apple 说"从未有人整合成端到端可全球规模运行的机密推理流水线"——**这句是不是仍然成立**？（有明显的自我宣传成分，需要外部视角核实。）

**PM 判断层（留给我自己想）**

- [ ] 如果国内安卓厂商要抄 PCC，**最小可行版本**是什么？（我的初步猜测：不必抄密码学，先抄"**举证责任转移**"这个结构——公开可审计的端云边界声明。但可行性存疑。）
- [ ] Apple 把"是否越界到第三方模型"做成显式确认，**这在国内生态会不会因为交互成本被砍掉**？如果砍掉，还剩什么替代方案？

---

## 附：来源清单（2026-08-06 核实）

| 事实 | 来源 |
|---|---|
| AFM 3 五模型家族、参数量、端/云划分、"in collaboration with Google" | Apple ML Research《Introducing the Third Generation of Apple's Foundation Models》，2026-06-08 |
| AFM 3 Core Advanced 稀疏架构、IFP、NAND 存储、per-prompt 路由、1—4B 激活、推理时弹性 | 同上 |
| AFM 3 Cloud Pro 由 Google + NVIDIA 承载、专供 agentic tool use 与复杂推理 | 同上；Apple Security Research《Expanding Private Cloud Compute》，2026-06-08 |
| 初代 ~3B 端侧模型 + PCC 服务端模型、AXLearn、责任 AI 原则 | Apple ML Research《Introducing Apple's On-Device and Server Foundation Models》，2024-06（2024-07-29 更新） |
| PCC 五条核心要求原文、二进制公开、透明日志、VRE、源码、Security Bounty | Apple Security Research《Private Cloud Compute: A new frontier for AI privacy in the cloud》（2024-06）、《Security research on Private Cloud Compute》（2024-10）、PCC Security Guide 文档站 |
| PCC 扩展至 GCP/NVIDIA、NVIDIA CC + Intel TDX + Titan、双信任根、硬件账本、"Apple retains complete control" | Apple Security Research《Expanding Private Cloud Compute》，2026-06-08 |
| PCC Security Guide 中存在 Multi-Turn Agent（bounded cross-request state）、PCC Agent、Stateless Inference、PIR 等条目 | security.apple.com/documentation/private-cloud-compute 目录页 |
| Siri 跨 App 动作、屏幕感知、个人上下文、ChatGPT 显式征询与隐私措施、设备要求（15 Pro / M1+） | Apple Newsroom《Introducing Apple Intelligence…》，2024-06-10 |
| PCC 中文表述（仅上送任务相关数据、安全隔区/安全启动/可信执行监视器/认证模块） | apple.com.cn Newsroom《Apple 凭借全平台更新，巩固隐私保护领先地位》，2024-06 |
| Foundation Models 框架（WWDC25）：引导式生成、Tool 协议、有状态会话、内置适配器、离线/无密钥/零费用/不增体积 | WWDC25 Session 286《了解 Foundation Models 框架》；Meet With Apple 跟随编程 205 |
| WWDC26：端侧模型重建 + Vision、`PrivateCloudComputeLanguageModel`（32K + ReasoningLevel）、模型抽象层、Core AI、Dynamic Profile、Evaluations、`fm` CLI、Python SDK、Core Spotlight RAG、框架开源、PCC 免费额度条件 | WWDC26 Session 241《Foundation Models 框架的新功能》；Session 339《将 LLM 提供平台引入 Foundation Models 框架》；WWDC26 Platforms State of the Union |
| System Orchestrator、entity ownership 确认机制、EntityCollection | 库内 [[Apple Intelligence 与 App Intents]]（据 WWDC26 Session 343 / 345） |

**⚠️ 待核实清单**

- **新 Siri 的交付时间线**：媒体给出的版本互相矛盾——iOS 26.4（3 月末 / 4 月）、iOS 26.5（5 月）、iOS 27（9 月）三种说法并存，且对"哪些能力落在哪个版本"分歧极大。**本文正文一律不采用具体版本号**，只记"2026 分批交付"。→ 需以 Apple 官方发布说明核对。
- **"Siri 用 Gemini" 类说法**：媒体广泛流传的 **1.2 万亿参数 Gemini 模型**、**每年 10 亿美元合作金额**、**白标**等，**全部为媒体口径，Apple 未公开确认**。Apple 一手源只说了"与 Google 合作、借助 Gemini 背后的技术共建 AFM"。另有报道引 Craig Federighi 称新 Siri"不使用 Gemini 的模型或基础设施，而是用 Gemini 前沿模型的输出做精炼"——**该引述我未找到 Apple 官方原文，标为待核实**。
- **AFM 3 Cloud / ADM 3 Cloud / Cloud Pro 的参数量**：官方**均未公布**，任何流传的数字都不可信。
- **AFM 3 Core Advanced 的具体设备门槛**：官方只写"unlocked by and optimized for our most capable Apple silicon systems"，**未点名机型**。媒体列出的机型清单未经证实。
- **初代 PCC 之外的性能数字**（如 0.6ms 首 token、~30 tokens/s on iPhone 15 Pro）：来自三方转述 Apple 技术报告，**本文未采信进正文**，如需引用请回查 2024 技术报告原文。
- **第五节表格中安卓 / 鸿蒙 / Windows 的端侧模型规格**：未逐条核实一手源，表内已标"待核实"。
- **"从未有人整合成端到端可全球规模的机密推理流水线"**：Apple 自述，带宣传性质，需外部来源交叉验证。

---

#标签/AppleIntelligence #标签/端侧AI #标签/PCC #标签/端侧意图框架 #标签/学习笔记
