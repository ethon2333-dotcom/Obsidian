---
title: AI 搜索与 RAG 问答产品生态 学习笔记
tags:
  - ai-search
  - rag-product
  - 知识库AI化
  - pkm
  - 产品生态
  - 广度种子笔记
created: 2026-09-01
source:
  - "Sacra《Perplexity revenue, valuation & funding》（sacra.com/c/perplexity）｜核实日期 2026-09-01"
  - "Forge Global《Perplexity's rise toward a potential $30 billion valuation and IPO》｜核实日期 2026-09-01"
  - "AICPB / AI 产品榜《AI Search Rankings by Website Visits — Issue 37（2026-06）》｜核实日期 2026-09-01"
  - "华军软件园《国内AI产品排行榜·AI搜索》2026-02 期｜核实日期 2026-09-01"
  - "Anthem Création《AI plugins for Obsidian 2026: complete comparison》｜核实日期 2026-09-01"
  - "PromptQuorum《Obsidian + 本地大模型：5 个插件打造您的第二大脑（2026）》｜核实日期 2026-09-01"
  - "Atlas Workspace《Smart Notes App (2026): 7 AI-Powered Note-Taking Tools》｜核实日期 2026-09-01"
  - "Value Add VC《NotebookLM 2026: 17M Users, $7.99-$200 Pricing Model》｜核实日期 2026-09-01"
  - "zarifautomates《Notion AI vs Mem: AI Note-Taking Compared》｜核实日期 2026-09-01"
  - "腾讯网《AI 知识库工具怎么选？研发场景下 6 类能力与主流工具横向对比》2026-08｜核实日期 2026-09-01"
  - "百度百科 / 搜狐《2026 职场 AI 知识库：腾讯 ima 方案》｜核实日期 2026-09-01"
  - "Ahrefs《5 AI Search Trends I'm Seeing in 2026》｜核实日期 2026-09-01"
  - "DevCuration / HokAI / techvernia 关于 Genspark 的第三方评测（口径互相冲突，见待核实清单）｜核实日期 2026-09-01"
---

> 学习定位：这是一篇**广度种子笔记**。目标是把「AI 搜索 + 知识库 AI 化」的**产品版图**一次铺开，建立品类坐标系。
>
> **刻意不写技术原理**——chunking、embedding、rerank、混合检索、GraphRAG 全部见 [[RAG 详细学习笔记]]。本文只从 PM 视角看：谁在做、卖给谁、靠什么收钱、护城河在哪。
>
> 这篇补的缺口：库里有 RAG 的「怎么做」，没有 RAG 的「谁在做、做成了什么生意」。技术可行性和产品可行性，是两件事。

---

**一句话心智模型：这一轮变的不是检索技术，而是「谁承担阅读成本」——搜索从「给你 10 个链接、你自己读」变成「给你 1 个带引文的答案」；知识库从「人找信息」变成「AI 替你答」。于是产品竞争的焦点从『索引谁更全』转移到『答案谁更可信 + 上下文谁更私有』：公开网页人人可爬（所以 AI 搜索必然内卷成红海），而你的 vault、你公司的 Confluence 别人爬不到（所以知识库 AI 化才是有壁垒的生意）。**

---

## 一、品类格局：三个层，商业模式完全不同

同样是「RAG 产品」，语料的**所有权**不同，生意的形状就完全不同。这是理解整个生态最省力的一刀。

| 维度 | ① AI 搜索产品 | ② 个人知识库 AI 化 | ③ 企业知识库 RAG 平台 |
|---|---|---|---|
| **语料来源** | 公开互联网（人人可爬） | 用户自己的笔记 / 文档 | 企业内部多系统异构数据 |
| **核心价值** | 省掉「读 10 个网页」 | 唤回「我写过但忘了」 | 打通「知识散在 20 个系统」 |
| **代表玩家** | Perplexity、Genspark、纳米 AI 搜索、秘塔、Felo、Kagi | Obsidian 插件系、Notion AI、NotebookLM、Mem、腾讯 ima | Glean、Guru、Atlassian Rovo、飞书 AI 知识库、Dify / RAGFlow / MaxKB |
| **商业模式** | 订阅（$20/月档）+ 少量广告/电商分佣 | 订阅（$10–20/月）或插件 BYOK（自带 API key） | 按席位（seat）年付 + 私有化部署 + 集成服务费 |
| **护城河** | **弱**：语料公开、功能可抄、成本随每次回答烧钱 | **中**：数据在用户手里，迁移成本 = 笔记搬家成本 | **强**：连接器数量 + 权限体系 + 合规资质 + 集成沉没成本 |
| **主要风险** | 巨头免费捆绑（Google AI Mode / ChatGPT Search）+ 单位经济学 | 「AI 代写笔记」损害学习效果的伦理张力 | 交付周期长、知识质量差则「垃圾进垃圾出」 |
| **买单人** | C 端个人 | C 端个人 | B 端 IT / 知识治理负责人 |

> [!tip] PM 视角的第一性结论
> ① 层是**流量生意**（打不过分发），③ 层是**集成生意**（打的是脏活累活），② 层是**习惯生意**（打的是用户已有的数据惯性）。
> 三层里只有 ① 层的语料是公共品——所以 ① 层注定最卷、最难差异化。这解释了为什么 Perplexity / Genspark 都在往「Agent 执行任务」跑：不是搜索做完了，是搜索**不够值钱**。

---

## 二、① AI 搜索产品速查表

| 产品 | 归属 | 定位 | 差异化点 | 数字（均待核实） |
|---|---|---|---|---|
| **Perplexity** | 独立（美） | 答案引擎 → Agent 工作台 | 引文密度高、研究型查询最强；已扩到 Comet 浏览器 + Computer Agent | 估值 $20B（2025-09 轮）；有媒体报道 2026-01 达 $23B；ARR $450M+（2026-03 FT 口径）；MAU 100M+ |
| **Genspark** | 独立（美） | 多智能体生成「Sparkpage」 | 不给聊天式答案，给**结构化研究简报**；一路扩张到 Slides / Sheets / Call For Me | 估值口径混乱：$1.25B→$1.6B→$2.6B（2026-06）；ARR 媒体称 45 天 $36M |
| **纳米 AI 搜索** | 360 | 全模态搜索智能体 | 文字/语音/拍照/视频多入口发起搜索 | 网页月访问 1.80 亿（2026-06 第三方口径，MoM −8.8%） |
| **秘塔 AI 搜索** | 秘塔科技 | 中文专业资料检索 | 无广告 + 「先想后搜」深度研究模式，学术/资料场景口碑好 | 网页月访问 452 万；国内 AI 搜索榜常年前二 |
| **Felo** | 独立（日） | 跨语言 / 跨境研究 | 支持 30+ 语言整合，内置学术搜索；少见的**月访问还在正增长**的 | 网页月访问 145 万（MoM +6.5%） |
| **Kagi** | 独立（美） | 付费无广告搜索 | 反商业模式：只收订阅费、不做广告，主打结果纯净 | 网页月访问 506 万 |
| **New Bing / Copilot** | 微软 | 巨头捆绑 | 系统级分发，来源链接清晰，还给站长做 AI 引用看板 | 网页月访问 36.8 亿（量级碾压，但含浏览器默认流量） |
| **天工 AI / 知乎直答 / 百度 AI 助手** | 昆仑万维 / 知乎 / 百度 | 生态内嵌 | 各自绑定内容源或分发入口 | 百度 AI 助手页面访问 4301 万+ |

> [!warning] 一个反直觉的信号
> 2026-06 第三方榜单里，Top 20 的 AI 搜索**几乎全线月环比负增长**（Perplexity −16%、纳米 −8.8%、You −19%）。可能解释有三个，都需要验证：(a) 用量从网页迁移到 App / 浏览器 / 系统入口，网页 PV 已失真；(b) 巨头把 AI 答案免费塞进默认搜索框，独立产品被抽血；(c) 品类新鲜感退潮。**不要用单一网页流量口径下结论。**

---

## 三、② 个人知识库 AI 化：Obsidian 生态是最有意思的样本

这一层和 [[PKM 方法论与 Obsidian 生态 学习笔记]] 直接接壤——那篇讲「怎么组织笔记」，这里讲「组织好的笔记怎么被 AI 用起来」。

### 品类内部分两派

| 派别 | 主张 | 代表 | 代价 |
|---|---|---|---|
| **云原生 AI 笔记** | AI 是产品本身，你只管写，AI 负责组织 | Notion AI、Mem、Reflect、NotebookLM、腾讯 ima | 笔记必须上传；隐私与迁移风险 |
| **本地优先 RAG** | 文件永远在你硬盘上，AI 只是挂在旁边的插件 | Obsidian + Smart Connections / Copilot + Ollama | 要自己装模型、跑索引；效果约为云端的一部分 |

### 代表产品速查表

| 产品 | 定位 | 差异化 | 价格（待核实） |
|---|---|---|---|
| **Smart Connections**（Brian Petro） | Obsidian 库级语义检索 | 生态内**唯一对全库建嵌入索引**的插件；侧栏自动浮现「语义相关笔记」，能捞出无共同关键词的旧笔记 | 免费（可接本地 Ollama，零 API 成本） |
| **Copilot for Obsidian**（Logan Yang） | 库上下文聊天 | 补上 Smart Connections 缺的对话界面；Vault QA 模式带来源引用 | BYOK 免费 / Plus $14.99 月 |
| **Text Generator / Smart Composer / AI Tagger** | 模板生成 / 类 Cursor 编辑 / 自动打标 | 分别覆盖「重复工作流」「行内改写」「图谱补标签」 | 开源 + BYOK |
| **Notion AI** | 工作区级 Agent | 从写作助手升级为跨 Slack/Drive/GitHub 的企业搜索 + Custom Agents + Workers | 2026 初 AI 并入 Business $20/座，原 $10 add-on 对新用户取消 |
| **NotebookLM**（Google） | 源受限研究 | **拒绝回答上传源之外的问题**——用「不知道」换可信度；Audio / Video Overviews 是独特体验层 | 免费档 50 源/100 notebook；Pro $19.99；Ultra $200 |
| **Mem** | AI-first 极速捕获 | 无文件夹哲学，主张「先扔进去，AI 自己整理」；每日/每周摘要主动推送 | $10–14.99/月 |
| **腾讯 ima** | 中文个人+共享知识库 | 三级知识库（个人/共享/订阅）+「知识号」把知识库变成对外品牌门面 | 免费为主；MAU 1300 万+、库内文件 4.2 亿份 |

### 值得记住的三个工程事实

- **Obsidian 到 2026 年仍无原生 AI**——不是没跟上，是 file-over-app 的设计取舍：只要 vault 是纯 Markdown，任何插件都能索引，可移植性不破。
- **本地 RAG 的成本是时间不是钱**：第三方实测 nomic-embed-text 首次建索引约 1K 笔记 2 分钟 / 5K 约 10 分钟 / 20K 约 75 分钟（机器差异极大，待核实），之后增量重嵌。
- **两个插件各建一套索引**：Smart Connections 和 Copilot 的嵌入库互不复用，同库跑两个 ≈ 双倍磁盘。这是插件生态的典型碎片化代价。

> [!note] 对我自己的 vault 的直接启示
> 我的库目前**89+ 篇、强 wikilink、浅目录**——这恰好是 RAG 最友好的形态（原子化 = 好切块，链接 = 好扩展召回）。也就是说 [[PKM 方法论与 Obsidian 生态 学习笔记]] 里那套「浅结构 + 强链接」的方法论，顺手把 RAG 的数据准备工作做完了。**好的 PKM 结构 = 免费的检索质量。** 这条推论我还没验证，见待解问题。

---

## 四、③ 企业知识库 RAG 平台

| 平台 | 定位 | 差异化 |
|---|---|---|
| **Glean** | 企业全域搜索 + Agent | 2019 年由前 Google 搜索核心成员创立；主打上百款 SaaS 连接器 + 企业上下文；国内份额低 |
| **Guru** | 可信知识层 | 强调 verified knowledge、权限感知 AI、审计留痕——卖的是**知识治理**不是搜索 |
| **Atlassian Rovo** | Confluence/Jira 存量收割 | 能把答案直接转成 Jira work item，知识→行动闭环 |
| **飞书 / 钉钉 / 企微知识库** | 协同生态内嵌 | 上手零门槛，但公开评测普遍指出细粒度权限与海量检索是短板 |
| **360 亿方云等国内厂商** | 政企私有化 | 卖的是等保三级 / 信创适配 / 本地服务——**合规即产品** |
| **Dify / RAGFlow / MaxKB** | 开源自建 | 无授权费、可私有化；短板是知识审批、分级权限、多租户要自己写 |

> 开源那一行和 [[低代码无代码 Agent 搭建平台 学习笔记]] 高度重叠——**「企业 RAG 平台」和「Agent 搭建平台」正在收敛成同一个品类**：都在做「私有数据 + 编排 + 工具调用」。这条收敛趋势值得单独追。

---

## 五、2025–2026 关键进展（六条）

1. **AI 搜索从蓝海到红海**：巨头把 AI 答案免费塞进默认搜索框（Google AI Mode、Bing、ChatGPT Search），独立产品的「答案」本身不再稀缺。
2. **集体向 Agent 逃逸**：Perplexity 出 Comet 浏览器（2025-07）和 Computer（2026-02）、Genspark 出 Claw「AI 员工」——从「给答案」转向「替你干完」。定位漂移的本质是**答案不够值钱**。
3. **笔记工具全线内嵌 RAG**：Notion AI 3.x 的 Custom Agents（2026-02）+ Workers（2026-04）、NotebookLM 2026-06 加代码执行与 Office 导出、ima 上线 copilot Agent 模式与 Skill 广场——「问答」已是基线功能，竞争点移到「能不能执行」。
4. **本地优先 RAG 成为一个真实选项**：Ollama + nomic-embed-text 让「笔记不出本机的语义搜索」在消费级硬件上可跑，隐私敏感人群第一次有了非妥协方案。
5. **GEO / AEO 兴起，但有效性存疑**：generative engine optimization 搜索量 18 个月涨约 997%（Ahrefs 口径）；但也有实验显示套完 GEO checklist 后引用率反而从 13.3% 掉到 10.9–12.2%，「不如什么都不做」。**这是典型的方法论泡沫期**。
6. **企业侧从「文档问答」走向「知识 + 工作项打通」**：单纯能答文档问题已不构成卖点，能不能把答案变成需求单/工单才是。

---

## 六、代表工具/平台一览（便于日后检索）

- **AI 搜索**：Perplexity ｜ Genspark ｜ 纳米 AI 搜索 ｜ 秘塔 AI 搜索 ｜ Felo ｜ Kagi ｜ Consensus（学术）｜ Exa（面向开发者的检索 API）｜ 天工 AI ｜ 知乎直答
- **个人知识库 AI 化**：Obsidian + Smart Connections / Copilot / Text Generator / Smart Composer ｜ Notion AI ｜ NotebookLM ｜ Mem ｜ Reflect ｜ Tana ｜ 腾讯 ima
- **本地栈**：Ollama / LM Studio ｜ 嵌入模型 nomic-embed-text（768 维）、mxbai-embed-large（1024 维）
- **企业 RAG**：Glean ｜ Guru ｜ Atlassian Rovo ｜ Notion Enterprise Search ｜ 飞书 AI 知识库 ｜ Dify ｜ RAGFlow ｜ MaxKB ｜ 360 亿方云

---

## 待解问题

> 这些是本文**刻意留白**的深度盲区，留给后续单篇深挖。

- [ ] **本地优先 RAG 的隐私 / 效果权衡到底有多大？** 第三方普遍说本地栈「约为云端的 70% 能力」——这个数字怎么测出来的？在中文长笔记场景上差距是收窄还是放大？
- [ ] **Obsidian 生态 RAG 插件横评（拿我自己的 vault 做基准）**：Smart Connections vs Copilot Vault QA vs Smart Composer，在同一批「我明知答案在哪篇笔记里」的问题上，召回率各是多少？双索引的磁盘/CPU 代价值不值？
- [ ] **「好的 PKM 结构 = 免费的检索质量」这条假设成立吗？** 原子化笔记 + 强 wikilink 是否真的提升 RAG 召回？还是说链接结构对纯向量检索毫无帮助、非得上 GraphRAG（[[Graph Engineering 图谱工程]]）才吃得到？
- [ ] **AI 搜索的单位经济学能不能收敛？** 每次回答都烧推理成本，而订阅是固定价。Perplexity 放弃广告、转向按量计费的动作说明了什么？$20/月档位是不是本质上不可持续？
- [ ] **NotebookLM 式「源受限」是不是被低估的产品哲学？** 用「拒答」换可信度，牺牲覆盖率换零幻觉——这个取舍在什么场景下是对的？能不能移植到端侧个人助理？
- [ ] **AI 搜索网页流量集体负增长的真因**：入口迁移 / 巨头抽血 / 品类退潮，哪个是主因？需要交叉 App DAU 数据而非单一 PV 口径。

---

## 关联笔记

- [[RAG 详细学习笔记]] —— **技术原理层**：本文所有产品的共同底座（切块、嵌入、召回、重排、评估）。产品差异化的上限由这一层的工程能力决定。
- [[RAG 检索增强生成]] —— 概念入口
- [[PKM 方法论与 Obsidian 生态 学习笔记]] —— **方法论层**：笔记怎么组织。本文是它向「产品/工具 AI 化」方向的外沿延伸。
- [[向量数据库 学习笔记]] —— 本地插件的 `.smart-env/` 和企业平台的向量层，是同一个问题的两种规模
- [[Context Engineering 学习笔记]] —— 「检索到什么塞给模型」是产品体感差异的真正来源
- [[Graph Engineering 图谱工程]] —— wikilink 图谱能否喂给检索，是 PKM × RAG 的关键未解题
- [[低代码无代码 Agent 搭建平台 学习笔记]] —— 与企业 RAG 平台正在收敛为同一品类
- [[AI 编程助手与 Agentic Coding 工具生态 学习笔记]] —— 同属「AI 吃掉某个存量工作流」的产品叙事

---

## 附：来源清单

| 来源 | 用于 | 核实日期 |
|---|---|---|
| Sacra《Perplexity revenue, valuation & funding》 | Perplexity 收入/估值/产品线（Comet、Computer、Labs、定价档位） | 2026-09-01 |
| Forge Global《Perplexity's rise toward a potential $30B valuation and IPO》 | Perplexity ARR / MAU / IPO 传闻 | 2026-09-01 |
| AICPB / AI 产品榜 AI Search Rankings Issue 37（2026-06） | 各 AI 搜索网页月访问量与环比 | 2026-09-01 |
| 华军软件园国内 AI 产品排行榜（2026-02） | 国内 AI 搜索榜位次 | 2026-09-01 |
| 凤凰网《2026 AI 搜索工具选型指南》 | 秘塔「先想后搜」、纳米全模态、Felo 多语言等定位描述 | 2026-09-01 |
| Anthem Création《AI plugins for Obsidian 2026》 | Obsidian 七大 AI 插件矩阵、作者、经济模型、无原生 AI 的设计取舍 | 2026-09-01 |
| PromptQuorum《Obsidian + 本地大模型（2026）》 | 本地栈配置、索引耗时、双索引磁盘代价、嵌入模型选择 | 2026-09-01 |
| Atlas Workspace《Smart Notes App (2026)》 | 智能笔记品类划分与定价横向 | 2026-09-01 |
| Value Add VC《NotebookLM 2026》 | NotebookLM 用户量、定价档位、2026-06 更新内容 | 2026-09-01 |
| zarifautomates《Notion AI vs Mem》 | Notion AI 定价变更、Custom Agents/Workers 时间线、Mem 能力 | 2026-09-01 |
| 腾讯网《AI 知识库工具怎么选（2026-08）》 | Glean / Guru / Rovo / 飞书 横向定位 | 2026-09-01 |
| 搜狐《2026 职场 AI 知识库：腾讯 ima 方案》+ 百度百科 ima 词条 | ima 三级知识库、知识号、MAU 与文件量 | 2026-09-01 |
| 搜狐《企业内部知识库选型指南 2026》 | 飞书/钉钉/企微短板、MaxKB/Dify 开源定位、国内私有化厂商 | 2026-09-01 |
| Ahrefs《5 AI Search Trends in 2026》 | GEO 搜索量增速、GEO 有效性反例实验 | 2026-09-01 |
| HokAI / DevCuration / techvernia / freemiumvisuals 的 Genspark 评测 | Genspark 产品线与融资（口径冲突，见下） | 2026-09-01 |

## ⚠️ 待核实清单

**所有商业数字均为第三方媒体 / 评测站口径，未经一手财报或官方公告验证，禁止直接引用于对外材料。**

1. **Perplexity 估值与 ARR 冲突**：$20B（2025-09 已宣布轮次）vs $23B（2026-01 Series E-6，仅媒体报道）vs 讨论中的 $30B；ARR 有 $450M（FT）/ $500M（Sacra 估算）/ $750M（2026-08 The Information）三个数。**唯一可确认的是量级在数亿美金 ARR、估值 200 亿美金以上。**
2. **Genspark 口径严重冲突**：估值 $1.25B / $1.6B / $2.6B 三个版本；创始人背景一说「前微软/Google/Meta 工程师」一说「前百度高管」；定价从 $9.99 到 $24.99 不等。**Genspark 的所有具体数字都不可信，只有「多智能体生成 Sparkpage」这个产品形态是各来源一致的。**
3. **网页月访问量数据**：来自 SimilarWeb 类第三方估算，只反映网页端，不含 App / 浏览器 / 系统级入口，**不能当作真实用量**。
4. **腾讯 ima 的 MAU 1300 万 / 文件 4.2 亿份**：来自媒体转述的官方宣传口径，未见第三方审计。
5. **本地 RAG 索引耗时**（1K≈2min / 20K≈75min）：来自个人博主实测，硬件（Apple Silicon vs x86）差异可达数倍。
6. **「本地栈约 70% 云端能力」**：来源未给出评测方法，属于体感估计，不应作为选型依据。
7. **NotebookLM 17M MAU**：媒体口径，Google 未官方披露。
8. **Notion AI 多模型路由（GPT-5.2 / Claude Opus 4.5 / Gemini 3）**：模型版本号来自第三方博客，需查 Notion 官方文档。
9. **360 亿方云「版式识别准确率 95.04%」**：厂商自述评测结果，未见公开测试集与第三方复现。
10. **GEO 反例实验（13.3% → 10.9~12.2%）**：单次小样本实验，不足以证伪整个 GEO 方法论，仅作为「方法论未成熟」的信号。
11. **本文未涉及任何非公开信息**，所有内容来自公开网页；竞品分析类结论均为基于公开资料的个人推断，标注为「PM 视角」的段落是我的判断而非事实。

---

#标签/AI搜索 #标签/RAG产品 #标签/知识管理 #标签/知识库AI化 #标签/广度种子
