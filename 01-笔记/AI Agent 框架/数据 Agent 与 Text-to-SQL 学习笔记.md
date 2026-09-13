---
title: 数据 Agent 与 Text-to-SQL
tags: [Agent, Text-to-SQL, 数据Agent, NL2SQL, 广度种子, AI Agent 框架]
created: 2026-09-13
source:
  - https://spider2-sql.github.io/   # Spider 2.0 官方（632 个企业级 text-to-SQL workflow）
  - https://arxiv.org/pdf/2509.00581v1   # SQL-of-Thought: Multi-agentic Text-to-SQL with Guided Error Correction (2025-08)
  - https://www.emergentmind.com/topics/agenticsql   # AgenticSQL 范式综述（plan→generate→verify 模块化）
  - https://www.agilytic.com/blog/databricks-genie-cortex-analyst-fabric-data-agents   # 三大家 warehouse-native AI 对比
  - https://colrows.com/blogs/snowflake-databricks-semantic-layer/   # 语义层 / OSI 互通标准
  - https://ibillxia.github.io/blog/2026/08/20/data-agent-servey-from-arch-to-practice   # Data Agent 全景调研（架构→产业）
---

# 数据 Agent 与 Text-to-SQL 学习笔记

> 心智模型一句话：**让 Agent 把"人话"翻译成 SQL/分析动作并自我纠错，是结构化数据问答从"一次生成"走向"会查会验的 Agent"的关键跃迁。**

本文是「AI Agent 框架」MOC 的 🌱 广度种子笔记，定位为**结构化数据 / 数据库**侧的 Agent 化问答索引。它与非结构化侧的 [[RAG 检索增强生成]] / [[RAG 详细学习笔记]] 形成对照：RAG 解决"从一堆文档里检索片段再生成"，本文解决"从一张张表里生成可执行 SQL 并跑出可信数字"。两者共享 Agent 循环、可观测、记忆等底层能力（见 [[Agent 可观测性 LLM Observability 学习笔记]]、[[Agent 记忆系统 学习笔记]]）。

---

## 1. 定义：NL2SQL 与 Data Agent 是什么

- **Text-to-SQL / NL2SQL**：把自然语言问题转换为可在数据库执行的 SQL 语句的任务。早期是单轮语义解析（text → SQL），现在主流是 LLM 提示 + 执行反馈。
- **数据 Agent（Data Agent）**：不止生成一条 SQL，而是"理解问题 → 探索 schema/数据 → 多步分析 → 执行 → 校验 → 可视化 → 给结论"的 agentic 数据分析助手。它把 NL2SQL 当作**内部工具之一**，而不是终点。

核心差异：**一次性 NL2SQL = 翻译器；Data Agent = 会查会验的分析师**。

---

## 2. 分类对比：一次性 NL2SQL vs Agentic 数据分析

| 维度 | 一次性 NL2SQL（单轮生成） | Agentic 数据分析（Data Agent） |
|---|---|---|
| 目标 | 生成一条能跑的 SQL | 端到端回答问题 / 给出可信结论 |
| 循环 | 无循环，text→SQL 一次成型 | plan → schema linking → generate → execute → verify → 自我纠错迭代 |
| 错误处理 | 跑挂了就盲重试或放弃 | 用执行报错 + 错误分类做定向修正（guided correction） |
| 工具 | 仅 SQL 生成 | SQL + 数据探查 + 可视化 + 文档/语义层检索 |
| 典型形态 | SQLDatabaseChain / 单条 prompt | SQL-of-Thought、Spider-Agent、企业 Copilot |
| 准确率瓶颈 | 复杂 join、歧义列名、长 schema | 同上 + 多步规划、跨表语义一致性 |
| 适用 | 单表/简单查询 | 企业级多表 workflow、探索式分析 |

> 与 [[多智能体协作与编排 学习笔记]] 的关系：agentic NL2SQL 常把"规划 / schema linking / 生成 / 校验"拆成多个角色（多 agent 或单 agent 内部分工），本质是多智能体协作在 SQL 场景的特例。

---

## 3. 主流方案横向表（开源模型 / 框架 / 企业）

| 类别 | 代表方案 | 定位 / 要点 |
|---|---|---|
| 开源模型 | **Defog SQLCoder** 系列 | 专训的 code LLM，面向 text-to-SQL；SQLCoder-7B/15B 等曾领先开源基线（具体版本与 SOTA 数字待核实） |
| 开源模型 | 通用 LLM + prompt | GPT / Claude / Gemini / DeepSeek 通过 few-shot + 执行反馈即可做 NL2SQL，无需专训 |
| 框架 | **LangChain SQL Toolkit / SQLDatabaseChain** | 早期成熟范式：把 DB 当工具，生成并执行 SQL 再回填；简单但基本无自我纠错（生产已演进到 agentic） |
| 框架 | **PandasAI** | 面向 DataFrame / 数据的对话式分析，生成 python/pandas 或 SQL，偏轻量探索 |
| 框架 | **SQLAgent / Spider-Agent** | 研究向 agentic NL2SQL，强调多步探索与工具调用（Spider 2.0 的官方 agent 评测载体） |
| 轻量产品 | **Vanna.ai** | RAG-for-SQL 思路：用历史查询 + 向量检索做 context，自托管友好 |
| 轻量产品 | **Evidence** | 把 SQL 当一等公民写成文档/报表，非 chat 但贴合"SQL 驱动分析" |
| 企业 | **Snowflake Cortex Analyst** | 语义模型（YAML Semantic View）优先，text→SQL 跑在 Snowflake 内；2026 含 MCP server + Teams/Copilot 集成 |
| 企业 | **Databricks Genie**（AI/BI Genie） | 基于 Unity Catalog 治理，2026 推 Genie One / Genie Ontology（上下文图谱统一指标）；单 Space ~30 表上限（待核实口径） |
| 企业 | **Microsoft Fabric Data Agent / Copilot** | 统一入口接 Lakehouse/Warehouse/Power BI 语义模型，按源走 NL2SQL/NL2DAX/NL2KQL；治理靠 Purview/RLS |
| 企业 | **Google Gemini in BigQuery** | BigQuery 控制台内 NL→SQL，读 Dataform 视图元数据，接 Looker |
| 企业 | **Tableau Pulse / Salesforce Agentforce Analytics** | BI 层"指标主动推送 / 分析技能"，更偏"分析—判断—执行"连续体而非纯问答 |

---

## 4. NL2SQL 演进：benchmark 与 agentic 转向

- **Spider（2018, Yale）**：跨库单轮 text-to-SQL 基准，顶级模型已达 ~91% EX（论文引用口径）。
- **BIRD（2023）**：强调真实数据库 + 外部知识 + 大规模值，难度高于 Spider；顶级模型约 ~70% 量级（具体数字待核实）。
- **Spider 2.0（2024, ICLR 2025 Oral）**：632 个**企业级** workflow，库常 >1000 列，跑在 BigQuery/Snowflake/DBT；o1-preview 仅 ~17–21% EX、GPT-4o 仅 ~10%，而 Spider 1.0 上 GPT-4o 为 86.6%——凸显"企业真实复杂度"鸿沟（分数动态变动，以官方榜为准）。
- **Spider2-lite / snow / DBT**：拆出的低成本与 code-agent 子设置（DBT 版 68 题，免 Docker）。

> agentic 转向的关键论文（2025）：
> - **SQL-of-Thought（2025-08）**：多 agent（schema linking→subproblem→query plan→SQL→guided correction loop），带 9 大类/31 子类错误分类做定向修正，Spider 上 ~91.59% EX（单轮基准，非企业级）。
> - **ReFoRCE（2025-02）**：表压缩 + 迭代列探索 + 自我精炼，Spider 2.0-snow（o1-preview）26.69% EX，远高于单轮基线。
> - **RAISE（2025-06）**：统一端到端 agent，用"交互式数据库探索深度"缩放 test-time compute，BIRD 上 44.8%→56.5% EX。

范式共识：**plan（规划）→ schema linking（表/列定位）→ generate（生成）→ execute（执行）→ verify（校验）→ 自我纠错迭代**，并把"执行反馈 + 错误分类"作为纠偏信号。

---

## 5. 2025–2026 进展要点

- **Agentic self-correction 成标配**：从"执行报错盲重试"升级为"错误分类 + 针对性修正"，避免重复生成错误 SQL。
- **Semantic layer / Metrics layer 成为准确率地基**：Cortex Analyst 靠 YAML Semantic View、Genie 靠 Unity Catalog + Genie Ontology、dbt Semantic Layer；共识是"LLM 只有在人类先编码好数据含义后才准"。厂商宣称成熟语义模型下可达 ~90% SQL 准确率（**待核实，属厂商口径**）。
- **语义层互通标准**：Snowflake 2025-09 推 **OSI（Open Semantic Interchange）**，v1.0 于 2026-01 发布，2026-06 进入 Apache 孵化器（Apache Ossie）——承认语义层不应锁死在单一仓库内。
- **Text-to-SQL + 数据治理咬合**：行/列级权限（Unity Catalog、Snowflake 策略、Purview RLS）直接成为 Data Agent 的可执行约束，否则"生成能跑但越权"的 SQL。
- **准确性仍是头号瓶颈**：Spider 2.0 企业级仍远低于可用线，多表 join、歧义命名、长 schema、跨方言（BigQuery/Snowflake）是主要失分项。

---

## 6. 与 RAG 的对照（结构化 vs 非结构化）

| 维度 | RAG（非结构化文档检索） | 数据 Agent / NL2SQL（结构化数据） |
|---|---|---|
| 数据形态 | 文档 / chunk / 向量 | 表 / 列 / 行 / schema |
| 检索对象 | 相关文本片段 | 相关表/列 + 正确 join 路径 |
| 生成产物 | 自然语言（引用文档） | 可执行 SQL + 数字/可视化 |
| 验证手段 | 片段相关性、引用溯源 | **执行报错 + 结果一致性 + 值校验** |
| 治理接口 | 文档权限 | 列掩码 / 行级安全 / 指标口径 |
| 代表笔记 | [[RAG 检索增强生成]]、[[RAG 详细学习笔记]] | 本文 |

互补点：Data Agent 也可"先 RAG 检索业务定义/文档，再生成 SQL"，即语义层文档 + 结构化查询的混合。

---

## 7. 待解问题（BREADTH > DEPTH，深钻留待后续）

- [ ] 复杂多表 join（>5 表、跨方言）的真实准确率与企业可用线到底在哪？benchmark 分数能否外推到自有库？
- [ ] 语义层 / metrics layer（Semantic View / Unity Catalog / dbt Semantic Layer / OSI）应如何工程化接入 Agent，避免"SQL 合法但口径错"？
- [ ] 私有库 schema 泄露风险：把 schema 整段喂给模型是否暴露业务结构？如何用最小上下文 + 脱敏 schema linking 缓解？
- [ ] Agent 改数 / 写数权限边界：何时只允许 SELECT，何时开放 UPDATE/INSERT，如何与治理层和人工 gate 咬合（参考 [[Agent 可观测性 LLM Observability 学习笔记]] 的审计追踪）？
- [ ] agentic 多步查询的**成本与延迟**如何优化（并行候选 + 一致性投票很贵）？与 [[Agent 推理成本优化 学习笔记]] 的模型路由/缓存如何结合？

---

## 附：来源清单

1. Spider 2.0 官方站（企业级 text-to-SQL 基准与排行榜）：https://spider2-sql.github.io/
2. SQL-of-Thought（多 agent + guided correction loop，arXiv:2509.00581，2025-08）：https://arxiv.org/pdf/2509.00581v1
3. AgenticSQL 范式综述（plan/generate/verify 模块化）：https://www.emergentmind.com/topics/agenticsql
4. Databricks Genie vs Snowflake Cortex Analyst vs Fabric Data Agents 对比：https://www.agilytic.com/blog/databricks-genie-cortex-analyst-fabric-data-agents
5. 语义层与 OSI 互通标准（Snowflake/Databricks 对照）：https://colrows.com/blogs/snowflake-databricks-semantic-layer/
6. Data Agent 全景调研（架构→产业实践）：https://ibillxia.github.io/blog/2026/08/20/data-agent-servey-from-arch-to-practice

## ⚠️ 待核实清单

- ⚠️ SQLCoder 具体版本（7B/15B）与开源 SOTA 数字随版本变动，本文未写死。
- ⚠️ 厂商宣称"成熟语义模型下 ~90% SQL 准确率"来自 Snowflake/第三方对比文，属厂商口径，应以自有评测集为准（建议自建业务问题集跑回归）。
- ⚠️ Spider 2.0 各方法分数动态变化（官方榜持续刷新），o1-preview 17.1%/21.3%、GPT-4o 10.1% 为论文引用口径，最新排名见官方榜。
- ⚠️ 各企业产品（Genie One、Cortex Analyst MCP、Gemini in BigQuery）的 GA 时间与功能以各厂商 2026 文档为准，本文按公开对比文整理。
- ⚠️ Databricks Genie "单 Space ~30 表上限"为官方文档口径，实际随版本可能调整。

#标签/Agent框架 #标签/Text-to-SQL #标签/数据Agent #标签/NL2SQL
