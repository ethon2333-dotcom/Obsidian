---
title: "GraphRAG 与知识图谱增强 Agent 学习笔记"
tags: [广度种子, GraphRAG, RAG, 知识图谱, Agent]
created: 2026-09-02
source: "WebSearch/WebFetch 核实（见文末来源清单）"
---

# GraphRAG 与知识图谱增强 Agent 学习笔记

> **心智模型：向量 RAG 检索的是「像不像」，GraphRAG 检索的是「连不连」。**GraphRAG = 把语料先抽成「实体—关系」图，再在图上做检索/遍历/聚合，用来补 vanilla RAG 的三个结构性缺口——多跳推理、全局归纳、关系可解释。原因很朴素：答案如果从来没有以「一段连续文本」的形式存在过，那么无论怎么调 chunk size、加 reranker、堆 Top-K，向量相似度都取不出来。

> [!warning] 本笔记的分工（避免与库内已有笔记重复）
> - [[RAG 详细学习笔记]] §7 已讲**微软 GraphRAG 的流水线机制**（Leiden 社区检测、社区摘要、成本落在哪两个 LLM 密集环节）。
> - [[Graph Engineering 图谱工程]] 已讲**图谱构建工程学**（五阶段架构、Schema 优先、实体消歧、Ontology 本体）。
> - [[向量数据库 学习笔记]] 讲**存储与 ANN 索引层**。
> - **本笔记只做广度地图**：方案横向全景、范式分类、2025–2026 进展、以及 GraphRAG 与 Agent 的结合面。机制细节请回上面三篇，不在此重复。

---

## 一、主流方案横向全景（广度主表）

| 方案 / 项目 | 出品方 | 核心思路 | 图谱来源 | 适用场景 |
|---|---|---|---|---|
| **Microsoft GraphRAG** | Microsoft Research | LLM 抽实体关系 → Leiden 社区检测 → 社区摘要 → local / global / DRIFT 三种查询 | LLM 自动抽取 | 大语料全局主题分析、行业研究、静态高价值语料 |
| **LazyGraphRAG** | Microsoft Research | 索引期只建**便宜的结构图**，把贵的语义摘要**推迟到查询时** | LLM 自动抽取（延迟） | 想要 GraphRAG 效果但吃不下索引成本的场景 |
| **LightRAG** | 港大 HKUDS | **双层检索**（低层实体 + 高层主题），省掉社区摘要；核心卖点是**增量更新只做并集，不重建全图** | LLM 自动抽取 | MVP / 中小知识库 / 语料持续更新 |
| **HippoRAG / HippoRAG 2** | 俄亥俄州立 OSU-NLP | 仿海马体：查询命中种子节点后跑 **Personalized PageRank** 在图上扩散，一次检索完成多跳 | LLM 抽取的开放式 KG | 多跳推理研究基线；HippoRAG 2 明确把 KG-RAG 定位成「非参数持续学习 = 记忆」 |
| **KAG（OpenSPG）** | 蚂蚁集团 + OpenKG | **逻辑形式驱动**：Schema 约束抽取 + 逻辑规划器分解问题 + 知识与原文块互索引（可回溯证据） | Schema 约束抽取 / 可接已有 KG | 医疗、法律、金融、政务——要求可审计推理路径的严谨领域 |
| **Youtu-GraphRAG** | 腾讯优图（ICLR 2026） | **垂直统一 agentic 范式**：同一份 seed schema 同时驱动「抽取」和「查询分解」；四层知识树（属性/关系/关键词/社区）+ 双重感知社区发现 + IRCoT 迭代反思 | Seed schema 引导抽取，运行时可扩展 | 企业私域多跳推理；schema 换一份即可迁移领域 |
| **Fast-GraphRAG** | Circlemind AI | PageRank 图探索 + 增量更新 + **人类可浏览的图谱视图**（重可解释/可调试） | LLM 自动抽取 | 需要调试和解释检索路径的中小项目 |
| **Graphiti / Zep** | Zep | **双时间轴（bi-temporal）**：每条边同时记「事实何时为真」与「系统何时得知」；事实变更时**关闭旧边的有效期而非删除** | 从对话/事件流增量抽取 | **Agent 长期记忆**、用户偏好随时间漂移、"它当时知道什么"审计 |
| **Cognee** | topoteretes | KG 三元组 + 向量（LanceDB），MCP 原生，支持本地运行 + 本体接地 | 多源接入自动抽取 | 给现有 agent 快速加一层图记忆；数据敏感需本地化 |
| **Neo4j GraphRAG / neo4j-agent-memory** | Neo4j | 图库作**存储基座**：向量索引 + 图遍历混合；官方 SDK + MCP server；agent-memory 库补「推理记忆」层 | 已有 KG 或自建 | 已有图库/企业级审计；上面多数方案的落地底座 |
| **私有 KG + RAG（传统路线）** | 企业自建 | 不做 LLM 抽取，直接把**已有的**业务知识图谱接进检索：Text-to-Cypher/SPARQL 或子图序列化 | **已有 KG**（人工/业务系统沉淀） | 图谱早已存在（组织架构、商品、设备台账），抽取成本为零 |

> 关键分野：**图从哪来**。上表大部分方案在解「从非结构化文本自动造图」；最后一行提醒——很多企业图谱本来就有，此时 GraphRAG 的成本结构完全不同（省掉了最贵的抽取环节）。

## 二、范式分类（五种，按「成本花在哪」切）

| 范式 | 代表 | 成本花在 | 换来什么 |
|---|---|---|---|
| **重索引 + 层次摘要** | MS GraphRAG | 索引期（每 chunk 抽取 + 每社区摘要） | 全局归纳 / 跨语料主题综合 |
| **轻索引 + 延迟计算** | LazyGraphRAG、Fast-GraphRAG | 查询期 | 逼近前者质量而摆脱前置大额投入 |
| **轻图 + 增量友好** | LightRAG | 索引期但很薄 | 语料能天天更新（原版 GraphRAG 的最大痛点） |
| **图上扩散 / 记忆化** | HippoRAG 2 | 检索期（PPR 一跳到位） | 多跳；并把检索当成"会长大的记忆" |
| **Schema / 逻辑约束** | KAG、Youtu-GraphRAG、OG-RAG | 前期 schema 与本体设计（人的时间） | 可审计推理路径、抗噪、领域可迁移 |
| **时序图谱** | Graphiti / Zep | 增量写入期 | 回答"何时为真"「当时知道什么」 |

## 三、2025–2026 进展（点到为止）

1. **成本不再是拒绝理由**。LazyGraphRAG 路线把索引成本压到原版的一个很小比例（各源引「约 0.1%」，⚠️ 数字待核实），并在 2026 被产品化进 Microsoft Discovery / Azure Local（预览）——从"研究项目"变成"可采购选项"。
2. **微软主线仍在活跃迭代**。官方 GitHub 最新 release 为 **v3.1.2（2026-08-21）**，含 local / global / **DRIFT** 三类查询（DRIFT 动态选社区，融合全局与局部）。✅ 一手核实。
3. **学术进入正规会场**。LightRAG（EMNLP 2025 Findings）、HippoRAG 2（ICML 2025）、Youtu-GraphRAG（**ICLR 2026**，✅ 已在 ICLR 官网 poster 页核实）。GraphRAG 不再是博客技术。
4. **出现了独立评测，并且结论刺耳**。GraphRAG-Bench / 《When to use Graphs in RAG》（arXiv 2506.05690）系统评测后指出：**GraphRAG 在很多真实任务上跑不过 vanilla RAG**；优势高度集中在多跳、时序、全局综合三类问题。另一个反复被强调的发现：**图的"质量/密度"比"规模"更重要**——MS-GraphRAG 图很大但节点连接稀疏，反而落后。
5. **上下文膨胀成为新瓶颈**。图检索塞进 prompt 的 token 量可以是传统 RAG 的几十倍（有源称 global 检索 prompt 达 4×10⁴ tokens，⚠️ 待核实）——于是出现 **PathRAG（路径剪枝）** 这类专治 context bloat 的方案。这条直接连到 [[Agent 推理成本优化 学习笔记]]。
6. **图谱正在从"检索层"漂移到"记忆层"**。Graphiti / Zep / Cognee / Mem0 图变体 / LangMem / neo4j-agent-memory 全都在做同一件事：**用图存 agent 的长期状态**，而不只是存文档。见下节与 [[Agent 记忆系统 学习笔记]]。
7. **中国厂商在场**。腾讯 Youtu-GraphRAG（schema 驱动 + agentic 分解）、蚂蚁 KAG/OpenSPG（逻辑形式驱动）都是有顶会背书的自研路线，不是跟随实现。
8. **⚠️ 一个必须知道的元教训**：这个领域**厂商自评的 benchmark 数字互相打脸**。同一个 LightRAG，在某综述里是"最高平均准确率 71.16%"，在 HippoRAG 2 论文的独立评测里只有"平均 F1 6.6"。**不要采信只由作者自己跑的评测**——这条比任何具体数字都重要。

## 四、与 Agent 结合的四个面

| 结合面 | 图在做什么 | 代表 |
|---|---|---|
| **图作检索工具** | Agent 把「查图谱」当成 loop 里的一个 tool；LangChain 的 `GraphCypherQAChain`、LlamaIndex 的 GraphRAG query engine、Dify/Open WebUI 内置图检索 | 主流框架已内置 |
| **Agentic 图检索（查询分解）** | 反过来让 **Agent 来驱动图检索**：按 schema 把复杂问题拆成并行子查询 → 图上取证 → 反思迭代（IRCoT）。这已经不是"检索"而是"在图上做规划" | Youtu-GraphRAG、KAG 逻辑规划器 |
| **图作 Agent 记忆** | 用户偏好、会话事实、实体关系存成时序图；解决"用户三个月前喜欢 Python，现在主要用 Go"这类**状态漂移**问题 | Graphiti/Zep、Cognee、Mem0 图变体 |
| **图作推理记忆 / 决策留痕** | 把「请求 → 规划步骤 → 调了哪些工具 → 用了哪些证据 → 成功与否」整条 trace 存成图，使决策**可解释、可审计、可复用** | neo4j-agent-memory 的"reasoning memory" |

> 对**工具选择/规划**的启发：如果 tool 之间的依赖（A 的输出是 B 的输入、C 需要 D 先授权）本身就是一张图，那么"选哪个工具、按什么顺序"在原理上就是一次图检索，而不是让模型在扁平的 tool 列表里凭 description 相似度猜。⚠️ 这条目前更多是推论与早期实践，尚未见到成熟的公开范式，留待深挖。

> [!note] 别混淆两个 "graph"
> 本笔记的 graph = **数据**（实体/关系）；[[LangGraph 概览]] 的 graph = **控制流**（节点=步骤）。两者可以叠：LangGraph 编排的 loop 里，某一步是"查知识图谱"。[[Graph Engineering 图谱工程]] 开篇也强调了这个边界。

## 五、与相邻概念的关系

| 相邻概念 | 关系 | 一句话切分 |
|---|---|---|
| [[RAG 详细学习笔记]] | **上游/兄弟** | 它讲向量相似检索的原理与调优；本文讲"当相似度根本不够用时换成图" |
| [[向量数据库 学习笔记]] | **底层** | 存储与 ANN 层。GraphRAG 几乎从不纯用图——主流是**图库 + 向量索引混合**，向量负责语义入口，图负责关系扩展 |
| [[Graph Engineering 图谱工程]] | **构建方法论** | 它答"图怎么造、schema 怎么定"；本文答"造好之后有哪些方案、怎么选、怎么接 Agent" |
| [[Agent 记忆系统 学习笔记]] | **收敛点** | 时序知识图谱正在成为记忆层的一种主流实现，GraphRAG 与记忆系统在 2026 已经在同一处会合 |
| [[多智能体协作与编排 学习笔记]] | **共享基座** | 多 agent 读写同一张图 = 天然的共享记忆，且带来一致性/写冲突问题 |
| [[Agent 评测与基准 学习笔记]] | **验证** | GraphRAG-Bench 属于 RAG 类基准；本文第三节的"自评打脸"正是污染与可信度问题的实例 |
| [[Agent 协议生态 学习笔记]] | **接入方式** | Graphiti、Neo4j、Cognee 均已出 MCP server，图谱正通过 MCP 变成 agent 的标准可插工具 |
| 长上下文（1M token） | **竞争者** | "全塞进上下文，不要检索了"是 2026 的对手路线；但 mid-context 信息准确率下降的问题使其未能取代检索 |

## 六、对 Android OS PM 的一点启发（不展开）

- **端侧的图谱天然存在**：联系人、App、日程、设备、地理位置之间的关系本来就是一张图，不需要 LLM 去从文本里抽——这正好落在上表最后一行「已有 KG」，成本结构远优于服务端从文档造图的路线。
- **"我当时知道什么"就是隐私审计**：Graphiti 的双时间轴模型和端侧"用户数据可解释/可撤回"的诉求同构。
- **抽取错误在系统层后果更重**：应用层抽错一条边只是答案错，系统层抽错一条关系可能**直接触发一次执行**。这条与 [[Graph Engineering 图谱工程]] 末尾的判断一致。

---

## 待解问题（留给 Ethon）

- [ ] GraphRAG 的图构建成本在**端侧**是否可行？如果图不靠 LLM 抽而是靠系统已有的结构化关系（联系人/App/日程），"GraphRAG on device" 是不是一个成本完全不同的问题？
- [ ] LightRAG 与 MS GraphRAG 的工程取舍究竟怎么算？"能增量更新"值不值得放弃"社区摘要带来的全局归纳"？什么样的语料更新频率是分水岭？
- [ ] 独立评测说「GraphRAG 常常打不过 vanilla RAG」，而厂商说提升几十个点——怎么设计**自己的**小规模验证实验来判定某个具体业务语料到底该不该上图？
- [ ] 图谱作 Agent 记忆时，"事实变更由一次 LLM 调用判定要不要作废旧边"这个设计是否可靠？误判导致的记忆污染怎么回滚？
- [ ] 如果把「工具依赖关系」建成图来辅助 tool selection，收益是否能盖过维护这张图的成本？有无公开实践？

---

## 附：来源清单

**✅ 一手 / 官方核实**
1. microsoft/graphrag GitHub Releases —— 最新版本 **v3.1.2，2026-08-21 发布**；v3.1.1（07-18）、v3.1.0（05-28）。（WebFetch 直取官方 releases 页）
2. ICLR 2026 官网 poster 页 —— Youtu-GraphRAG 论文《Vertically Unified Agents for Graph Retrieval-Augmented Complex Reasoning》确认被 ICLR 2026 接收；摘要自述 "up to 33.6% cost saving and 16.62% higher accuracy"。
3. TencentCloudADP/youtu-graphrag 仓库结构文档（DeepWiki）—— 四层知识树、FastTreeComm、GraphQ 查询分解、IRCoT 等组件与代码实体对应关系。

**📄 论文 / 学术来源**
4. 《When to use Graphs in RAG: A Comprehensive Analysis for Graph Retrieval-Augmented Generation》arXiv 2506.05690 —— GraphRAG-Bench 独立评测，图质量>图规模、context 膨胀、按问题类型路由等结论。
5. LightRAG（arXiv 2410.05779，EMNLP 2025 Findings，港大 HKUDS）；HippoRAG（NeurIPS 2024）/ HippoRAG 2（ICML 2025，OSU-NLP）；KAG（arXiv 2409.13731，蚂蚁 + OpenKG）。以上会议/编号来自多方二手转述互证，未逐一开原文核对。
6. 《When Does Graph RAG Pay Off?》隆德大学学生论文（含 GraphRAG-Bench 复现表格）。

**📰 综述 / 二手（口径不一，仅作地图用）**
7. Neo4j 官方博客（neo4j-agent-memory：短期/长期/**推理记忆**三层；context engineering 工具盘点）。
8. Atlan《Context Engineering / Context Graph Tools 2026》—— Graphiti 双时间轴、Cognee、TrustGraph、Zep CE 已于 2025-04 停止维护等。
9. AgentList《GraphRAG in Practice》、mnemoverse《Knowledge-Graph Memory for Agents》、dev.to 多篇 GraphRAG 综述、CSDN《GraphRAG 生态全景：6 大主流方案盘点》、腾讯云开发者社区 Youtu-GraphRAG 介绍。

---

## ⚠️ 待核实清单

- ⚠️ **所有性能与成本数字一律待核实，且各源互相矛盾**。同一个 LightRAG：某综述称 WildGraphBench 平均准确率 71.16%（最高），另一处引 HippoRAG 2 论文的独立评测称平均 F1 仅 6.6、HotpotQA 仅 9.9。同一个 MS-GraphRAG 既被称"global 模式 65.38%"也被称"医疗集 38.06%、落后 vanilla RAG"。**本笔记不采信任何单一数字**，只保留"图在多跳/时序/全局上占优、在单跳事实查找上不占优"这一**方向性**结论。
- ⚠️ **LazyGraphRAG「索引成本 0.1%、查询成本 1/700」**：多源转述一致，但均未回到 Microsoft Research 原文；与 [[RAG 详细学习笔记]] 的待核实清单是同一条，尚未消解。
- ⚠️ **MS GraphRAG 原版索引成本「约 $33,000」**：广泛流传，来源单一，量级可信但数字待核实。
- ⚠️ **Youtu-GraphRAG 的成本节省口径冲突**：ICLR 官方摘要写 "up to 33.6% cost saving"，腾讯云博客写 "Token 成本节省高达 90.71%"。**以论文摘要为准，博客口径待核实**。
- ⚠️ **微软 GraphRAG 版本号谣言**：某中文竞品报告称"2.0.0（2026 年 5 月发布）""Rust 重写索引引擎吞吐 +40%、内存 -25%"——与官方 releases 页（当时已 v3.1.0）矛盾，**该报告的版本与性能描述不可信**，本笔记不采用。
- ⚠️ **产品化状态**：LazyGraphRAG 进入 Microsoft Discovery / Azure Local 预览、Zep Community Edition 于 2025-04 停止维护 —— 均为二手，需查官方公告。
- ⚠️ **GitHub star 数**：各源差异大（MS GraphRAG 29.8k / 31k / 34k；LightRAG 29k / 36.9k；Graphiti 20k / 26.3k / 28.5k）。**本笔记正文一律不写 star 数**。
- ⚠️ **"图谱辅助工具选择/规划"**：第四节末尾的推论属笔者外推，未见成熟公开范式，勿当结论。
- ⚠️ 各类"幻觉率从 20–40% 降至 2–5%""ROI 230%"等厂商赞助研究数字，全部未采用。

---

#标签/广度种子/GraphRAG #标签/Agent/RAG #标签/知识图谱 #标签/Agent/记忆
