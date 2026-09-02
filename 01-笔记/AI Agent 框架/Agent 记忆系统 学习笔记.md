---
title: Agent 记忆系统
tags: [agent-memory, mem0, letTA, 长期记忆, 广度种子]
created: 2026-09-01
source: Mem0/Letta/LangMem/Zep 官方文档 + CoALA 框架(arXiv 2023) + 2025-2026 公开横评博客（见文末来源清单，数字均待核实）
---

# Agent 记忆系统（广度种子）

> 心智模型：Agent 的记忆 = 把"这次经历"结构化成外部记忆存盘，下次对话按需召回，而不是每次都把全部历史塞满上下文窗口——上下文是 RAM，长期记忆是硬盘，两者互补而非替代。

本文是「广度种子」，聚焦 Agent 长期记忆的**工程架构方案**（记忆分层 + 记忆中间件），与 [[个性化与端侧用户记忆 学习笔记]]（on-device 个性化建模）刻意区分：本文讲"记忆系统怎么存/取/管"，后者讲"端侧如何对用户建模"。两者是同一能力的两个切面。辐射锚点见 [[多智能体协作与编排 学习笔记]]（多 agent 共享记忆）与 Context Engineering（记忆即喂给上下文的筛选层）。

## 一、记忆分层对比（认知科学 → 工程映射）

主流分类来自 CoALA 框架（Sumers et al., 2023）：工作记忆 + 长期记忆（episodic / semantic / procedural）。这是设计"写路径、检索线索、遗忘策略"都不同的依据。

| 层级 | 存什么 | 典型实现 | 检索线索 | 遗忘策略 |
|---|---|---|---|---|
| **工作记忆 Working** | 当前任务、最近几轮、工具输出、中间推理（scratchpad） | 上下文窗口内的 message buffer / 命名 memory block（Letta 的 Human/Persona block） | 当前决策直接 attend | 滚动窗口 / 摘要压缩后驱逐（易失） |
| **情景记忆 Episodic** | 具体事件：某次对话/任务/失败原因（带时间戳与结果） | 向量库存 trajectory；MemGPT 把旧 episode 分页到 archival | 与当前情境的相似度（recency+importance+relevance 加权） | 摘要合并 / 重要性裁剪 |
| **语义记忆 Semantic** | 去语境化的稳定事实："用户是素食者""财年在 3 月" | 向量库 / 知识图谱；由多轮 episode 提炼 | query 语义相关性 | 冲突消解（同 key 旧事实置 invalid） |
| **程序记忆 Procedural** | "怎么做"：技能、规则、可复用 workflow、tool-call 模板 | 权重（fine-tune）/ system prompt / 可检索 skill 库；LangMem 会改写自身 system prompt | 任务类型匹配 | 极少被忘，随行为更新 |

> 记忆污染风险：semantic 是"从 episode 提炼的派生断言"，一条错误 consolidation 会毒化所有未来回答——这是分层架构最该警惕的洞。

## 二、记忆中间件 / 框架对比

2025-2026 四大主流（定位、接口、存储各异，数字见文末待核实清单）。

| 方案 | 定位 | 架构差异点 | 接口形态 | 存储后端 |
|---|---|---|---|---|
| **Mem0** | 框架无关、生产优先的托管记忆 API（"记忆的 Redux"） | vector + KV + graph 三后端；自动后台抽取 fact；user/session/agent 三级层级 | `Memory().add() / .search()` 简单 API | 可自托管或托管；SOC2 / HIPAA-ready（待核实） |
| **Letta**（原 MemGPT） | Agent 自我管理的"记忆操作系统" | Core（常驻上下文）/ Archival（向量）/ Recall（对话历史）三层；Agent 自己决定记/忘/取 | 显式 memory 工具调用（memory_replace 等） | 可插拔：Mongo/Weaviate/Mem0/Zep |
| **LangMem** | LangGraph 原生官方配套库 | semantic/episodic/procedural 三分法；procedural 会改写 agent system prompt | LangGraph 集成 SDK | 依赖 LangGraph 状态/持久层 |
| **Zep（Graphiti）** | 企业级、时态知识图谱 | 双时态 bi-temporal 图，追踪"何时为真/何时变更"，自动标记旧事实过期 | 按 episode 摄取，图遍历 + 向量召回融合 | Graphiti 图引擎（Apache 2.0 开源） |

## 三、2025-2026 进展（点到为止）

- **记忆成 Agent 标配**：从"RAG 顶一顶"变成独立技术层；模型厂商也开始下注（Claude memory tool 正式化、跨模型记忆导入；OpenAI Responses API 把长期记忆责任下放给开发者）。
- **三代架构演进**：Gen1 纯向量 RAG → Gen2 结构化 fact（带时序/冲突消解）→ Gen3 Memory Graph（实体+边+episode，多跳+时间旅行+可解释）。
- **结构化记忆抽取成共识**：把"塞原文"换成"抽 fact"，成本与准确率同时改善（mem0 论文口径，待核实）。
- **"Context Rot"反直觉现象**：上下文越长≠记得越好，长 prompt 反而掉准——凸显"筛选层"即长期记忆的价值。
- **基准成熟**：LongMemEval / LOCOMO / BEAM 等让记忆评估有客观数据；隐私与"被遗忘权"成企业级合规要求。

## 四、代表工具 / 框架（速查）

- 中间件：Mem0、Letta、LangMem、Zep/Graphiti
- 云托管：Vertex AI Memory Bank（TTL 过期 + 版本修订）、Claude Memory（consumer 跨会话 / Claude Code 项目级 md 文件）
- 基座范式：MemGPT（OS 隐喻）、Generative Agents（recency/importance/relevance 检索）、Reflexion（episodic 反思驱动提升）
- 关联：与 [[多智能体协作与编排 学习笔记]] 咬合——多 agent 共享记忆需解决一致性（Agent A 更新，Agent B 不能读到旧值）。

## 待解问题（深度盲区，留白给 Ethon）

- [ ] 记忆与端侧个性化如何结合？外部记忆中间件 vs [[个性化与端侧用户记忆 学习笔记]] 的 on-device 建模，边界在哪、能否互补？
- [ ] 记忆污染 / 遗忘机制怎么工程化？重要性打分 + TTL 够不够，错误 consolidation 如何回滚？
- [ ] 多 agent 共享记忆的一致性（stale read / 并发写）在编排层怎么解？
- [ ] 记忆的"可迁移/可审计/可删除"——跨厂商导入（如 ChatGPT→Claude）的真实可行性？
- [ ] 记忆系统与 fine-tuning 的边界是否正在模糊（反复经历同一任务≈轻量微调）？

## 附：来源清单

- CoALA: Cognitive Architectures for Language Agents（arXiv 2023）— 分层 taxonomy 权威出处
- Mem0 论文 Building Production-Ready AI Agents with Scalable Long-Term Memory（arXiv 2504.19413，LOCOMO 基准）
- MemGPT → Letta 更名 / Zep Graphiti / LangMem SDK 官方文档与博客（2024-2026）
- agentmarketcap.ai 2026-04 横评（Letta/Zep/Mem0/LangMem 对比）
- letsdatascience.com / tmls.nyc / mastra.ai 等公开博客（架构与分层说明）
- 中文 CSDN 综述《Agent 长期记忆三代演进》（2026-06，三代架构视角）

## ⚠️ 待核实清单

- 各源对 mem0 GitHub star 数说法不一（约 4.1 万 / 4.8 万），以官方为准。
- mem0 Series A 金额（约 2400 万美元 / $24M 口径一致，但不同源写法不同），待官方复核。
- Mem0 vs LangMem 延迟数字（p95 0.2s vs 59.8s）来自厂商/第三方横评，差距极端，待独立复现。
- "记忆基础设施市场 2025 年 $6.3B → 2030 年 $28.5B（35% CAGR）"为厂商预测，非审计数据。
- Zep 在 LongMemEval 上"领先 15 分"、Deep Memory Retrieval 94.8% vs MemGPT 93.4% 等为厂商自报，待核实。
- "Context Rot"实验（128K prompt 准确率 98%→64%）为 Chroma 复现，原始出处待查。

#标签/Agent记忆 #标签/Mem0 #标签/长期记忆
