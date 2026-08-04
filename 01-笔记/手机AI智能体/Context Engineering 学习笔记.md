---
title: Context Engineering 学习笔记
tags: [ContextEngineering, 上下文工程, RAG, 端侧意图框架, 安卓PM, 学习笔记]
created: 2026-08-05
source: 一手源（Anthropic 官方工程博客 / Anthropic Cookbook / docs.anthropic.com / Tobi Lütke 原推 / Karpathy 原推），2026-08-05 核实
---

# Context Engineering（上下文工程）

> 学习定位：把「上下文工程」这条线**从一个 buzzword 一路推到端侧 Agent 的工程约束上**——它到底是什么、和 Prompt Engineering 差在哪、上下文窗口里都装了什么、有哪些真正管用的技术手段，以及**手机上那个只有几 K 有效窗口的小模型为什么反而最需要它**。
> 本文是 **own-words 综合**，不是情报简报。原始定义我尽量引官方原话；我自己的判断写在第六节和待解问题里；拿不准的都进了文末「⚠️ 待核实清单」。

---

## 一、一句话心智模型

**Prompt Engineering 是打磨「一句话」；Context Engineering 是设计「模型每一步看到的整个世界」。**

再具体一点，三句话钉死它：

- **对象变了**：从「一条 prompt」变成 **agent 每一轮推理前被组装出来的整个 token 集合**——系统指令 + 对话历史 + 检索文档 + 工具定义 + 工具返回 + 工作记忆 + 长期记忆。
- **时态变了**：写 prompt 是**一次性**的离散动作；上下文工程是**每一步都要重做一次的**筛选动作（Anthropic 原话：*"context engineering is iterative and the curation phase happens each time we decide what to pass to the model"*）。
- **约束变了**：上下文不是「能塞多少塞多少」的存储，而是一份**会被消耗、边际收益递减的注意力预算**。

> 最反直觉、也最值得记住的一条（Anthropic 原话）：
> **"Good context engineering means finding the smallest possible set of high-signal tokens that maximize the likelihood of some desired outcome."**
> 目标不是"短"，是**信息密度最高**。砍到最短和砍到最有信号，是两件事。

---

## 二、Context Engineering 是什么（vs Prompt Engineering）

### 2.1 词是怎么来的（时间线，均为一手可查）

| 时间 | 谁 | 说了什么 |
|---|---|---|
| **2025-06-19** | **Tobi Lütke（Shopify CEO）** | > "I really like the term **context engineering** over prompt engineering. It describes the core skill better: **the art of providing all the context for the task to be plausibly solvable by the LLM**." |
| **2025-06（数日后）** | **Andrej Karpathy**（前 OpenAI / 前 Tesla，**不是 Shopify 的人**） | 回了 "+1"，并给出至今被引用最多的技术版定义：> "Context engineering is **the delicate art and science of filling the context window with just the right information for the next step**." 并补一句心智模型：**LLM 是 CPU，context window 是 RAM，上下文工程就是决定每一步往内存里装什么的操作系统。** |
| **2025-06 前后** | **Lance Martin（LangChain）** | 提出流传最广的**四动作分类法**：**Write / Select / Compress / Isolate**（写出去 / 挑进来 / 压缩 / 隔离）。后续他在演讲里收敛为三个词：**Offload / Reduce / Isolate**。 |
| **2025-09-29** | **Anthropic 工程博客《Effective context engineering for AI agents》** | 目前**最系统的一手论述**，本文第三、四节主要依据它。 |

> ⚠️ **一个我原本记错、这次纠正掉的点**：Lütke 是 Shopify CEO，**Karpathy 不是 Shopify 的**；两条推是两个人、隔了几天，经常被合并引用成"Shopify 提出了 context window 那句话"，这是错的。
> 另外「**context is the new weights（上下文即权重）**」这句**不是 Lütke 也不是 Karpathy 说的**——它出现在 2025 年底围绕 Google DeepMind《Evo-Memory》与 Stanford/SambaNova《Agentic Context Engineering》两篇论文的讨论里，**目前我只见到中文二手报道用这个措辞**，一手英文出处待核实（见文末）。

### 2.2 Anthropic 的官方定义（原话，值得原样背）

- **Prompt engineering**：*"methods for writing and organizing LLM instructions for optimal outcomes"*——**写指令的方法**，尤其是系统提示。
- **Context engineering**：*"the set of strategies for **curating and maintaining the optimal set of tokens (information) during LLM inference**, including all the other information that may land there outside of the prompts."*——注意末半句：**重点恰恰是那些"不是你写的"的信息**（工具返回、检索结果、历史）。
- Anthropic 明确把二者定性为**演进关系而非替代关系**："we view context engineering as the natural progression of prompt engineering"。**Prompt Engineering 是 Context Engineering 的一个子集，没有被废掉**——系统提示写得烂，上下文工程救不了。

### 2.3 为什么在 Agent 时代才变成核心问题

单轮问答里，上下文 ≈ 你写的那句 prompt，所以打磨 prompt 就够了。
Agent 是 **LLM 在循环里反复调工具**：每一轮的工具返回都会沉淀进下一轮的输入。于是出现两个只有 agent 才有的麻烦：

1. **上下文是自己长出来的，不是你写进去的**——你控制不了工具吐回来多少 token。
2. **它单调增长**——不主动裁剪，几十上百轮之后必然撞墙。

（业界常引的量级：Manus 官方说一个典型任务平均约 50 次工具调用；Anthropic 说生产级 agent 动辄上百轮。⚠️ 这两个数字来自二手转述，见待核实清单。）

### 2.4 两个概念对照

| 维度 | Prompt Engineering | Context Engineering |
|---|---|---|
| 优化对象 | 一条指令的**措辞与结构** | **整个 token 集合**的构成 |
| 时机 | 写的时候（离线，一次性） | **每一次推理前**（在线，反复） |
| 谁产生内容 | 人写 | 人写 + **工具返回 + 检索 + agent 自己生成** |
| 主要失效模式 | 指令歧义、格式不对 | **窗口溢出 / context rot / 注意力被噪声稀释** |
| 产物 | 一个模板 | **一个运行时的信息编排系统** |
| 类比 | 写好一道题的题干 | 设计考场：给他哪些资料、什么时候发、发多少 |

---

## 三、Context Window 的解剖（表格）

Anthropic 把 context 定义为 *"the set of tokens included when sampling from a large-language model"*。拆开看，一个 agent 的窗口通常是这么几块——**每一块的取舍逻辑完全不同，这是我觉得最该记住的一张表**：

| 块 | 作用 | 谁产生 | 典型问题 | 取舍原则 |
|---|---|---|---|---|
| **系统指令** | 定身份、规则、边界、输出契约 | 人（一次写好） | 要么过于死板（硬编码复杂 if-else），要么过于含糊 | Anthropic 说要找 **"right altitude"（正确的高度）**——两种失效模式之间的 Goldilocks 区间；用 XML 标签 / Markdown 分块；**从最小提示起步，按失败模式增量补** |
| **对话历史** | 维持任务连续性 | 人 + 模型 | 单调增长，最先撑爆窗口 | *informative, yet tight*；靠 compaction / 剪裁 |
| **检索文档（RAG）** | 补模型不知道的事实 | 检索系统 | Top-K 设太大反而淹没信号；**检索内容是不可信输入** | 精准 > 多；**必须带来源标注**（见第五、六节） |
| **工具定义** | 定义 agent 能做什么，是它与外部世界的**契约** | 人 | 工具集膨胀、功能重叠、参数含糊 → 模型选错工具 | 官方建议：**最小化、无重叠、自包含、参数明确**；工具本身也要 token-efficient |
| **工具返回** | 观察结果 | 工具 | **agent 上下文膨胀的头号来源**（一次网页抓取可能几万 token） | Offload 到窗口外，只回摘要 / 路径 / URL；用 tool-result clearing |
| **工作记忆 / scratchpad** | 当前任务的中间结论、todo、计划 | 模型自己 | 容易被压缩掉 | Anthropic 的 **structured note-taking**：写到 `NOTES.md` / todo list 这类**窗口外的文件**，需要时再拉回 |
| **长期记忆** | 跨会话的偏好、结论、教训 | 系统沉淀 | 只增不减会被噪声淹没；错误记忆会持续污染 | 需要检索 + 反思 + 修剪，不能只写不删 |
| **示例（few-shot）** | 用样例代替长篇描述 | 人 | 堆边缘案例 | Anthropic 原话：**"For an LLM, examples are the 'pictures' worth a thousand words."** 要**多样、规范**的典型例，不是堆 corner case |

> **业界还有一套更粗的四支柱切法**，记起来更快：**Instructions / Retrieval / Memory / Tools**（来自 Sourcegraph 的表述，⚠️ 二手源）。和上表能一一对上，可以当索引用。

---

## 四、关键技术

### 4.1 底层约束：注意力预算与 context rot（先理解为什么，再谈手段）

这是整套技术栈的**物理基础**，Anthropic 讲得最清楚：

- **Context rot（上下文腐烂）**：*"as the number of tokens in the context window increases, the model's ability to accurately recall information from that context decreases."* 所有模型都有这个特性，只是衰减曲线陡缓不同。
- **为什么**：Transformer 里每个 token 要 attend 所有其他 token，n 个 token 就有 **n² 对关系**；窗口越长，注意力被摊得越薄。加上训练数据里短序列远多于长序列，模型对长程依赖的"经验"本来就少。
- **注意力预算**：*"Like humans, who have limited working memory capacity, LLMs have an 'attention budget'… Every new token introduced depletes this budget by some amount."*
- **重要限定**：Anthropic 强调这是 **"a performance gradient rather than a hard cliff"**——**是渐变的性能滑坡，不是断崖**。所以"长窗口模型出来了就不需要上下文工程了"是错的，但"超过 X token 就完蛋"也是错的。

> ⚠️ 常被引来佐证的 Chroma 报告《Context Rot: How Increasing Input Tokens Impacts LLM Performance》（约 2025-07），我这次**没读到一手原文**，只见转述，标待核实。

### 4.2 Prompt Caching（省钱省延迟，但它同时是一条设计约束）

一手源：`docs.anthropic.com` — Prompt caching（2026-08-05 核实）。

- **机制**：缓存 prompt 的**前缀**。缓存范围是 **tools → system → messages 这个固定顺序**，一直到打了 `cache_control` 断点的那一块。
- **计价倍率**（官方明列）：**5 分钟缓存写 = 1.25×** 基础输入价；**1 小时缓存写 = 2×**；**缓存读 = 0.1×**（即约 90% 折扣）。
- **TTL**：默认 **5 分钟**，每次命中免费续期；另提供 1 小时档（加价）。
- **两种用法**：自动缓存（顶层加一个 `cache_control`，断点随对话自动前移）/ 显式断点。

> **这条对架构设计的真正含义，比"省钱"重要得多**：既然缓存的是**前缀**，那么**上下文里越靠前的内容就越应该是稳定不变的**。
> → 系统指令、工具定义放最前（几乎不变，长期命中缓存）；易变的检索结果、工具返回放后面。
> → **反过来说：任何"动态改写系统提示"的设计，都会把整条缓存打穿。** 这是"动态组装"和"缓存友好"之间一个真实存在的矛盾，做 agent 架构时必须显式取舍。
> ⚠️ 最小可缓存 token 数（有二手源说 Haiku 1024 / Sonnet-Opus 2048）我未在官方文档原文中核到，标待核实。

### 4.3 长任务三件套（Anthropic 官方给的三种手段）

| 技术 | 干什么 | 适用 | 代价 / 风险 |
|---|---|---|---|
| **Compaction（压缩 / 压紧）** | 把接近上限的窗口**蒸馏成一份高保真摘要**，然后用摘要重新初始化上下文继续跑 | 需要**维持对话流**的长会话 | 官方原话：*"The art of compaction lies in the selection of what to keep versus what to discard, as overly aggressive compaction can result in the loss of subtle but critical context whose importance only becomes apparent later."*——**你无法预知哪条信息十步之后才变关键** |
| **Structured note-taking（结构化笔记 / agent 记忆）** | 定期把笔记**持久化到上下文之外**（`NOTES.md`、todo 列表），需要时再读回 | 有清晰里程碑的迭代型任务 | 开销小、收益大；难点在摘要写得够不够让模型知道"外面存了什么" |
| **Sub-agent architectures（子智能体）** | 主 agent 只做高层编排，子 agent 用**干净的窗口**处理专项任务，各烧几万 token，**只回 1000–2000 token 的浓缩结果** | 需要并行探索的复杂研究 | 关注点分离的收益明显，但**交接摘要是新的信息损耗点** |

配套还有一个更轻量的手段：**tool-result clearing（工具结果清理）**——只清掉臃肿的工具返回，保留对话骨架。Anthropic Cookbook 把 **compaction / tool-result clearing / memory** 并列为三条可组合的杠杆，并强调它们**都有一方 API 支持，不用自己造编排基建**。

**关于压缩的一条重要工程判断（Manus 的做法，⚠️ 二手转述）**：
> **任何不可逆的压缩都是有风险的。** 所以先把工具的完整结果 **offload 到磁盘**，再做有损压缩——只要 URL / 文件路径还在上下文里，内容随时能捞回来。**"可恢复的压缩"应当是默认设计。**

### 4.4 Just-in-Time 上下文（动态组装的核心）

传统 RAG 是**推理前预检索**，把料先铺好。JIT 反过来：

- agent 只在窗口里维护**轻量标识符**——文件路径、URL、查询语句；
- 运行时通过工具**按需加载**；
- 类比：人不背整个图书馆，靠**书签和文件系统**。

好处除了省 token，还有两个容易被忽略的：**元数据本身就是信号**（文件名 `test_utils.py` 已经告诉了模型它的用途），以及支持**渐进式披露**——让 agent 一层层探索着发现上下文。
代价：运行时探索比预取**慢**，且需要认真设计防止工具误用。
**现实答案是混合策略**：稳定的先预加载（如 `CLAUDE.md`），其余靠 glob/grep 即时取。

### 4.5 记忆分层

| 层 | 存在哪 | 生命周期 | 端侧对应物 |
|---|---|---|---|
| **工作记忆（working）** | 上下文窗口内（scratchpad、todo） | 当前若干轮 | 当前这次意图执行的中间态 |
| **短期记忆（short-term）** | 会话历史 | 单次会话 | 一次多轮澄清对话 |
| **长期记忆（long-term）** | 窗口外的文件 / 向量库 / 结构化存储 | 跨会话 | 用户偏好、常用联系人、"上次我说过别再问我这个" |

> 这三层的边界不是学术划分，**是"什么时候该把东西写出去、什么时候该捞回来"的工程决策点**。

### 4.6 窗口溢出的处理顺序（我给自己的判断，非官方）

按**信息损耗从小到大**排，遇到溢出应当依次尝试：

1. **Cache 命中优化**（不减信息，只减成本/延迟）
2. **Offload**：大块工具返回落盘，窗口里只留指针（**可逆，零信息损失**）
3. **Tool-result clearing**：清掉旧的工具返回（保留决策骨架）
4. **Select / 重排**：只把这一步真正需要的捞回来
5. **Compaction**：有损摘要（**从这一步开始不可逆，务必先做过第 2 步**）
6. **Isolate / 子 agent**：换个干净窗口重开

**先做无损的，再做有损的。** 大多数 agent 翻车是因为跳过 2–4 直接上 5。

---

## 五、与 RAG / 端侧 Agent 的关系

### 5.1 与 RAG：RAG 是「Select」这一格里的一种实现，不是全部

库内 [[RAG 检索增强生成]] 已经把 Naive → Advanced → Modular → 自适应 → Agentic 五阶段讲清楚了。放到上下文工程的坐标系里看，关系是这样的：

| | RAG | Context Engineering |
|---|---|---|
| 管的范围 | **怎么把外部知识捞进来** | **整个窗口装什么**（RAG 只是其中一块） |
| 在四动作里的位置 | 主要落在 **Select** | Write / Select / Compress / Isolate 全包 |
| 关心的指标 | 召回率、上下文相关性、忠实度 | 上面这些 **+ token 预算 / 延迟 / 缓存命中率 / 多轮不腐烂** |
| 关系 | **被包含**，但没有被取代 | 上位概念 |

**两条能直接互相解释的东西：**

- [[RAG 检索增强生成]] 第十三节那条坑「**过度检索：Top-K 设太大（如 K=20），模型在片段中迷失**」——这在上下文工程的语言里就是 **注意力预算被稀释 / context rot**。同一件事的两种说法，**上下文工程给了它一个物理解释**。
- 反过来，JIT 检索（4.4）本质上是把 RAG 从"预检索"改成"agent 自己按需检索"，也就是 [[RAG 检索增强生成]] 里的 **Agentic RAG**。

### 5.2 与端侧 Agent：**窗口越小，上下文工程的边际价值越高**

这是我认为最值得写进 PRD 论据的一段。

云侧模型现在动辄 128K–1M 窗口，很多团队因此觉得"上下文工程是过渡期技巧"。**端侧完全相反**：

- **纸面窗口 ≠ 可用窗口**。手机上真正的瓶颈是 **RAM 与 KV cache**：模型权重要整体装进内存，KV cache 还要再占一块。有实践者报告：**手机上实际可用的上下文常在 2K–4K token 量级，即便模型声称支持 128K**（⚠️ 二手，见待核实）。
- 一份 2026-06 的 Android 端侧 agent 实践博客（⚠️ 单一厂商来源，待核实）给的数字很有代表性：他们的 4B INT4 模型在 LiteRT 上**有效窗口约 8192 token**；而 Google Maps 一屏的无障碍树有 **600–900 个节点**，朴素序列化直接爆窗。他们的解法完全是教科书式的上下文工程：
  - 剥掉不可交互节点（**Select**）
  - 合并同类兄弟节点（40 行相同的联系人 → `[ContactList: 40 items, each with call/message actions]`）（**Compress**）
  - 按与上次交互的空间邻近度排序，只留 top 60–80（**Select + 排序**）
  - 对话历史只留 **3 轮**（**Compress**）
  - → 700 节点压到 **180–240 token**，全程稳在 2000 token 以内
  - 他们自己承认的代价：**剪枝偶尔会剪掉模型真正需要的节点**——这正是 4.3 里说的"你无法预知哪条信息之后才变关键"。

> **一句话收口：云侧的上下文工程主要在省钱和防腐烂；端侧的上下文工程是"能不能跑起来"的问题。**
> 它在端侧不是优化项，是**准入条件**。

### 5.3 和「端侧意图框架把工具清单交给 OS 托管」的呼应

这一层的联动最有意思，也是我这次真正想通的点：

[[MCP 与设备侧 MCP]] 里记的那条官方表述——agent 处理请求时 *"likely to consider both server-side remote MCP tools and local AppFunctions together"*，也就是**端侧工具和云侧工具在同一份清单里**。

把它翻译成上下文工程的语言：**这份清单是要进 context window 的。**

于是几件事立刻串起来了：

1. **工具定义是上下文的一块，而且是"必须常驻"的一块**（4.2 说了，它还得放在前缀里才能吃到缓存）。设备上装了 200 个 App、每个注册 5 个 AppFunction，**那就是 1000 条工具描述**——一个 8K 窗口的端侧模型**光工具清单就装不下**。
2. → 所以 **OS 必须承担"工具清单的上下文工程"**：不是把全量 Registry 丢给模型，而是**按当前意图、当前前台、当前时间地点，动态裁出一个 top-N 的子集**。
3. → 这恰好解释了 [[端侧意图框架 学习笔记]] 6.3 里记的那条 Android 独有能力——`isEnabled` **动态可见性**、"Registry 是随账号状态实时变化的动态视图，不是静态清单"。**动态可见性在系统设计上就是一次 Select。**
4. → 也解释了为什么 [[MCP 与设备侧 MCP]] 的待解问题里那个"谁定工具排序规则"如此关键：**工具排序 = 端侧上下文工程里最贵的那次 Select**，谁定这个排序，谁就实质掌握了入口。

> **心智模型**：端侧意图框架把「发现 / 准入 / 编排」收进 OS，**本质上是 OS 接管了 agent 上下文中"工具"那一块的构造权**。
> 这不是类比，这是同一件事换个说法。

---

## 六、安卓 PM / 产品视角

### 6.1 上下文工程在产品上的一句话翻译

**"对的信息，在正确的时刻，出现在模型面前。"**
——注意，这句话和产品经理最熟的那句 **"对的信息，在正确的时刻，出现在用户面前"** 结构完全一样。
**上下文工程就是把信息架构（IA）这门手艺，从"给人看"迁移到"给模型看"。** PM 的老本行在这里是直接可迁移的：**信息优先级、渐进式披露、默认值设计**，三样全对得上。

### 6.2 系统级 Agent 的三条产品含义

**(1) 确认 UI 的上下文，本身就是一次上下文工程**

[[确认机制]] 关心"什么动作要确认"。上下文工程追问的是**另一半**：**确认弹窗上那句话，是从哪块上下文生成的？**

- 如果确认文案是模型基于**已被压缩过**的上下文生成的，那用户看到的"你确定要给张三转账 500 元吗"，**可能已经和真实将要执行的参数脱节了**。
- 所以我的判断是：**确认 UI 必须绑定在结构化的工具调用参数上，而不是模型的自然语言复述上。** 前者是确定的，后者是被上下文工程处理过的、有损的。
- 前面 5.2 那个端侧案例给了一个很好的印证：他们的**动作分级层是确定性规则层，不是 LLM**——模型只负责提出 JSON，规则层负责分级，Tier 3 必须用户点确认。**把安全判断放在上下文之外**，这是对的架构。

**(2) 来源可信分级必须进 context，而且必须是模型能看见的字段**

这条直接接上 [[Agent Data Injection 数据注入攻击]] 和 [[AppIntent 每日情报 2026-08-04]] 的"来源分级防注入"结论：

- 检索结果、工具返回、其他 App 共享的意图元数据，**在 context window 里和系统指令长得一模一样——都是 token**。模型天然分不清"这是我该信的指令"和"这是我该怀疑的数据"。
- **上下文工程给 ADI 防护提供了落点**：既然是"决定往窗口里装什么、怎么装"，那**"带着来源标签装进去"就是上下文工程的一部分**，不是额外加的安全模块。
- [[端侧意图框架 学习笔记]] 6.4 已经核实过：**四大 OS 的意图元数据都还没有来源类型字段、也没有分级**。→ 把它重新表述一遍会更有说服力：**这不是安全功能的缺失，是上下文构造规范的缺失。**
- 更极端一点：[[Agent Workspace 隔离执行]] 讲的隔离，在上下文工程里对应的就是 **Isolate**——**不可信来源的内容应当进不可信 agent 的独立窗口，而不是和系统指令共处一室。** 两个体系在这里完全同构。

**(3) 端侧的成本账要重算**

云侧上下文工程的 KPI 是 **$ / token**；端侧的 KPI 是 **RAM 占用、prefill 延迟、发热与耗电**。

- 每多 1K token 上下文，端侧付的是 **KV cache 内存 + prefill 时间 + 电量**，不是钱。
- 有实践者提到：**持续推理 30 秒以上手机会降频，速度掉 30–50%**（⚠️ 二手，待核实）。这意味着**端侧上下文预算不是常数，是随温度变化的**。
- → 这条直接接上库内的 [[端侧意图框架 学习笔记]] 里的"端侧调度与降级"：**降级策略里应该有一档是"缩上下文"**，而不是只有"降模型"和"甩到云端"。据我所知这一档在公开资料里没人写过，可以作为一个原创设计点。

### 6.3 一条给自己的反 hype 提醒

"模型窗口会越来越大，上下文工程是过渡期产物"——**这个说法在云侧半对，在端侧全错**。

Anthropic 自己也承认 *"smarter models require less prescriptive engineering"*，但同一段的收尾是：**"treating context as a precious, finite resource will remain central to building reliable, effective agents."**
在手机上，"finite" 这个词是被 **RAM、电池和温度**三重锁死的，不会因为模型变聪明而放开。

---

## 七、库内关联

- **上位主题**：[[端侧意图框架 学习笔记]]（四平台格局；6.3 动态可见性 / 6.4 来源分级两节与本文第五、六节直接互文）
- **工具那一块的构造权**：[[MCP 与设备侧 MCP]]（端侧+云侧同一份工具清单 → 这份清单要进 context window）
- **检索那一块**：[[RAG 检索增强生成]]（RAG = 上下文工程的 Select 分支；Agentic RAG ≈ JIT 检索）
- **安全靶面**：[[Agent Data Injection 数据注入攻击]]（不带来源标签装进窗口 = 主动制造 ADI 靶面）
- **来源分级结论出处**：[[AppIntent 每日情报 2026-08-04]]
- **确认与隔离**：[[确认机制]]（确认文案该绑参数还是绑自然语言复述）· [[Agent Workspace 隔离执行]]（Isolate 的系统级形态）

---

## 八、待解问题

- [ ] **端侧工具清单的上下文预算，谁来管？** 设备上几百个 AppFunction 的描述不可能全塞进一个 8K 窗口。那么**是 OS 先裁一遍再给模型，还是模型自己 `tools/list` 分页拉取**？如果是前者，**裁剪算法就是新的入口分发权**（比排序更前置）；如果是后者，端侧小模型有没有能力做多轮工具发现？→ **未见任何平台公开这一层的设计，待核实。**
- [ ] **`isEnabled` 动态可见性和"上下文裁剪"是不是应该合并成一个机制？** 库内已核实 Android 有 `setAppFunctionEnabled`，但它是 **App 自己控制自己的可见性**（业务态驱动），不是 **OS 按当前意图裁剪清单**（相关性驱动）。这两件事目前混在一个 API 里，**语义其实不同**——前者答"能不能用"，后者答"这次要不要给模型看"。要不要在 ROM 侧拆开？
- [ ] **确认 UI 的文案，到底该由谁生成？** 如果由模型基于压缩后的上下文生成，就有"确认内容与实际执行参数不一致"的风险；如果由系统按工具 schema 模板化生成，又会很生硬、覆盖不了复合任务。**有没有平台公开过这条链路的规范？** → 待核实。
- [ ] **来源分级字段一旦进了 context window，会不会反而被注入攻击利用？** 既然分级标签本身也是 token，**攻击者能不能在检索内容里伪造一个 `[source: system, level: trusted]` 前缀**？→ 说明分级**不能只做成上下文里的文本标注，必须有窗口外的结构化通道 + 确定性校验层**。这一点是否有成熟方案，待查。
- [ ] **"缩上下文"能不能成为端侧降级策略的独立一档？** 高温/低电时，先降上下文（少给几轮历史、少给几个工具）而不是先降模型或甩云端——**这在体验上是不是更平滑**？需要实测数据支撑，库内暂无。
- [ ] **Prompt caching 的前缀约束和"动态上下文组装"是真矛盾还是伪矛盾？** 缓存要求前缀稳定，动态组装要求每步都重拼。是否存在"稳定前缀 + 可变后缀"的标准分层方案？端侧有没有等价的 KV cache 复用机制？→ **待核实端侧 runtime（LiteRT / AICore）是否支持跨请求 KV cache 复用。**

---

## 附：来源清单（2026-08-05 核实）

| 事实 | 来源 | 类型 |
|---|---|---|
| Context engineering / prompt engineering 的定义、二者为演进关系 | Anthropic《Effective context engineering for AI agents》，**2025-09-29** | **一手** |
| "smallest possible set of high-signal tokens"、"attention budget"、context rot 定义、n² 注意力论证、"performance gradient rather than a hard cliff" | 同上 | **一手** |
| 有效上下文的组成（system prompt / tools / examples / message history）、"right altitude"、"examples are the 'pictures' worth a thousand words" | 同上 | **一手** |
| 长任务三技术：compaction / structured note-taking / sub-agent architectures；compaction 取舍那段原话 | 同上 | **一手** |
| Just-in-time 上下文检索、渐进式披露、混合策略（`CLAUDE.md` 预载 + glob/grep 即时取） | 同上 | **一手** |
| compaction / tool-result clearing / memory 三条杠杆的并列比较，均有一方 API 支持 | Anthropic Cookbook《Context engineering: memory, compaction, and tool clearing》（Isabella He） | **一手** |
| Prompt caching：缓存前缀顺序 tools→system→messages；5 分钟默认 TTL、命中免费续期、1 小时档加价；**写 1.25× / 1h 写 2× / 读 0.1×** | `docs.anthropic.com` — Prompt caching | **一手** |
| Tobi Lütke 原话（"the art of providing all the context…"），**2025-06-19** | Lütke @tobi 推文，多处原文转载一致 | **一手（推文原文）** |
| Karpathy "filling the context window with just the right information for the next step"；LLM=CPU / context window=RAM 类比 | Karpathy 推文，多处原文转载一致 | **一手（推文原文）** |
| Write / Select / Compress / Isolate 四动作分类法归于 LangChain 的 Lance Martin（2025-06） | 多篇二手技术博客一致归因 | 二手（归因一致） |
| 端侧 Android agent 的上下文裁剪实践（4B INT4 有效 ~8192 token、700 节点 → 180–240 token、历史留 3 轮、三级动作分类由确定性规则层执行） | 某厂商工程博客《Building Deft: On-Device AI Phone Agent for Android》，2026-06-16 | **二手 / 单一厂商自述** |

**⚠️ 待核实清单**

- **「context is the new weights / 上下文即权重」的一手出处**。目前只见到中文二手报道在解读 Google DeepMind《Evo-Memory》（约 2025-11-27）与 Stanford + SambaNova《Agentic Context Engineering》（arXiv 2510.04618）时使用该措辞。**它不是 Tobi Lütke 的话，也不是 Karpathy 的话**，我未找到任何权威人士以此原句公开表述。**在对外材料里不要引用这句并署名给任何人。**
- **Chroma《Context Rot: How Increasing Input Tokens Impacts LLM Performance》** 的发布日期（多处写 2025-07）与具体实验结论，本次未读到一手原文。
- **「Manus 一个典型任务约 50 次工具调用」「Anthropic 生产级 agent 上百轮」**——均为二手转述，未核到一手原文。
- **Prompt caching 的最小可缓存 token 数**（二手称 Haiku 1024 / Sonnet & Opus 2048），未在官方文档原文中核到。
- **「手机实际可用上下文常在 2K–4K token」「持续推理 30 秒以上降频、速度掉 30–50%」「单次长对话耗电 5–10%」**——均出自实践者博客，非厂商官方数据，**属经验值不是规格值**，引用时必须限定条件。
- **Gemma 4 E2B/E4B 支持 128K 上下文窗口**——来自中文科技媒体（2026-04），未核 Google 官方文档；且即便纸面支持 128K，与上一条"实际可用 2K–4K"并不矛盾，**注意区分"标称窗口"与"手机上可用窗口"**。
- **Sourcegraph「上下文工程四大支柱」（Instructions / Retrieval / Memory / Tools）**的一手出处未核。
- 第六节 6.2 中关于「确认 UI 应绑定结构化参数而非模型复述」「降级策略应含缩上下文一档」**均为我自己的判断，无一手依据**，需另行验证。

---

#标签/ContextEngineering #标签/上下文工程 #标签/RAG #标签/端侧意图框架 #标签/安卓PM
