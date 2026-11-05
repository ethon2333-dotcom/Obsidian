---
title: AI Agent 的持久化与状态管理 学习笔记
tags: [AI Agent, 状态管理, 持久化, Durable Execution, Checkpoint]
created: 2026-10-10
source: [LangGraph docs / aiwiki.ai, activewizards.com (State Management), agentnative.dev (Agentic SaaS Blueprint 2026), niteagent.com (durable-execution-agents-2026), reactify-solutions.com (durable-ai-agents-2026), temporal.io]
---

# AI Agent 的持久化与状态管理 学习笔记

> [!abstract] 心智模型
> 把 Agent 运行中的「对话 / 进度 / 工具 / 内存」四类状态，在 **进程内 → 外部存储 → 分布式** 三层落盘，让长程任务能 **断点续跑、人工介入、状态隔离**——本篇聚焦「运行态任务的状态如何落盘、恢复、隔离」，区别于 [[Agent 记忆系统 学习笔记]]（长期记忆模型）与 [[多智能体协作与编排 学习笔记]]（编排模式）。

---

## 一、定义：什么叫「Agent 的状态」

Agent 不是无状态函数——它跑着跑着，会积累一堆「下次还得用」的东西。广义的「状态」可拆成四类（点到为止）：

| 状态类型 | 是什么 | 典型落点 |
|---|---|---|
| **对话态** | messages 历史、最近几轮上下文 | 会话存储 / 上下文窗口 |
| **任务进度态** | 当前在哪个 step / phase、retry 次数、是否完成 | checkpointer / workflow journal |
| **工具调用态** | 已发出的 tool call、返回结果、pending 的异步调用 | 执行引擎的事件历史 |
| **内存态** | 工作记忆、临时变量、sub-agent 的中间产物 | 运行时内存 / 外部 KV |

> 关键区分：**本篇的「状态」是运行态任务的「当下进度与上下文」**，而 [[Agent 记忆系统 学习笔记]] 讲的是「跨会话沉淀下来的长期知识」。两者会交接（例如把进度态收敛成记忆），但问题域不同。

---

## 二、分类：持久化层级

状态落盘的「远近」分三档，选型本质是「能活到哪种故障」：

| 层级 | 代表方案 | 能扛住什么 | 扛不住什么 |
|---|---|---|---|
| **进程内** | LangGraph `MemorySaver` / InMemorySaver | 同进程内多轮接续；开发测试 | 进程/容器一重启就全丢 |
| **外部存储** | `SqliteSaver` / `PostgresSaver` / `RedisSaver` / MongoDB saver | 进程重启、跨进程共享、多实例 | SQLite 写锁串行化；Redis 默认不持久（需 AOF）；需自己管并发/重试 |
| **分布式（Durable Execution）** | Temporal / Inngest / Restate / DBOS / Hatchet / Cloudflare Workflows / AWS Bedrock AgentCore / Vercel WDK | 跨机器、跨天 HITL、崩溃自动重放、恰好一次 side-effect | 引入编排运行时复杂度；需写「确定性 Workflow + 非确定性 Activity」 |

---

## 三、主流方案（广度地图）

### 3.1 LangGraph Checkpointer（图状态机视角）
- **机制**：图编译时绑定 checkpointer，调用时传 `thread_id`；每个 superstep 后自动存快照，下次同 `thread_id` 续跑。
- **后端**：`MemorySaver`（内存，重启丢）→ `SqliteSaver`（单文件）→ `PostgresSaver` / `AsyncPostgresSaver`（生产推荐）→ `RedisSaver`（社区，高吞吐）→ `MongoDB` / DynamoDB / S3（自定义 `BaseCheckpointer`）。
- **两个原语**：`Checkpointer`（单线程运行态）+ `Store`（跨线程长期记忆 KV，对应 [[Agent 记忆系统 学习笔记]]）。
- **中断-恢复**：`interrupt_before/after`（静态）+ `interrupt()`（动态，节点内任意行暂停）；恢复时传 `None` 作输入。
- **时间旅行**：`get_state_history` 回滚到任意历史检查点改 state 再续跑（Studio 的 undo/what-if 基础）。
- **经验口径**：单 checkpoint >50KB 应外置（只存 ID 不存内容）；用 `Annotated[list, operator.add]` reducer 做 append-only 合并，避免覆盖。

### 3.2 Durable Execution（运行时视角）
| 引擎 | 持久化模型 | 粒度 / side-effect 保证 | 备注 |
|---|---|---|---|
| **Temporal** | 每 workflow 的 Append-only Event History（事件溯源）+ 重放 | Activity 级恰好一次；Saga 补偿；多语言 SDK；MIT | 生态最成熟；2026 Replay 大会发布 Serverless Workers / Standalone Activities / Workflow Streams，并集成 Google ADK、OpenAI Agents SDK（Python GA 于 2026-03，待核实口径） |
| **Inngest** | step 级 checkpoint（event log） | `step.run` 缓存+可重试；`step.waitForEvent` 零算力挂起等 HITL；Agent Kit | serverless-native，可跑 Vercel/任意 serverless/自托管 |
| **Restate** | 每实体 journal + Virtual Objects（内嵌 KV，单写保证） | idempotency key 去重；suspend on FaaS | 注意：BSL 1.1 许可，非 OSI 开源 |
| **DBOS Transact** | 直接落你已有的 Postgres（`@DBOS.workflow/step/transaction`） | 无独立编排服务；每 workflow 仅恢复一次 | 库不是服务，运维轻 |
| **Hatchet** | durable task checkpoint | 面向 agentic HITL 循环、非幂等工作 | 类似模型 |

> **Checkpointing ≠ Durable Execution**（2025-2026 反复被强调的口径）：checkpointer 只负责「在标记点存状态、下次还给你」，重试/恢复/去重仍是开发者手写；Durable Execution 让运行时接管这三件事，开发者写普通代码即可。

### 3.3 各框架 / SDK 的 Session & State（2025-2026）
- **OpenAI Agents SDK**：`Sessions` 提供持久对话记忆，后端 SQLAlchemy / SQLite / Redis / MongoDB / Dapr + 加密变体；**不内置向量库**（语义召回需自带）。2026-04 更新引入 native sandbox（可 resume sandbox 快照）、subagents（隔离上下文聚合回写）。
- **CrewAI（1.14.7 口径）**：把短/长/entity/外部记忆统一为单一 `Memory` 类，LLM 打分召回（语义+新鲜度+重要性），默认 LanceDB，可插 `StorageBackend`（Postgres/Qdrant/Pinecone）。
- **Claude Agent SDK**：默认**无状态**，每个 session 是本地 CLI 子进程，JSONL transcript 写在 `~/.claude`；上下文满自动 compact 总结；`SessionStore` 适配器「尽力」镜像 transcript，容器重启丢本地 transcript（需镜像才可控 resume）。
- **Google ADK**：sessions / memory / artifacts 自成上下文层；2.0 引入图式 workflow runtime（routing/fan-out/fan-in/loop/retry/state/HITL/嵌套）+ Task API。
- **AutoGen / AG2**：会话内可见，但无跨会话内建持久记忆（需自定义 hook / DB）。

---

## 四、2025-2026 进展（点到为止，数字标待核实）
- **Durable Execution「跨过鸿沟」**：2025 下半年 AWS（Durable Functions）、Cloudflare（Workflows GA）、Vercel（Workflow DevKit）下场，主因是 Agent 基础设施需求。
- **采购语言变化**：2026 年企业 Agent 上线常写「durable by default or do not ship」——可靠性成门槛而非加分项。
- **落地信号**：Replit Agent 3、OpenAI Codex web agent、Cursor 长程自动化据称跑在 Temporal 上（单源口径，待核实）。
- **资本信号**：a16z 据称领投 Temporal $300M Series D（单一来源口径，待核实）。
- **LangGraph 侧**：`langgraph-checkpoint` 1.2 / SQLite & Postgres 后端 3.1 加了 streaming delta channel history、降低高量线程每 checkpoint 字节数；`snapshot_frequency=K` 用全量快照换重建延迟。
- **HITL / 挂起**：跨天等人工审批成为一等公民（`step.waitForEvent` 零算力挂起、`interrupt()` 动态暂停）。

---

## 五、代表产品与框架（检索用）
- **Checkpointer 类**：LangGraph（Memory/Sqlite/Postgres/Redis/Mongo）
- **Durable Execution 类**：Temporal、Inngest、Restate、DBOS、Hatchet、Cloudflare Workflows、AWS Bedrock AgentCore、Vercel Workflow DevKit
- **SDK Session/State 类**：OpenAI Agents SDK（Sessions）、Claude Agent SDK、Google ADK、CrewAI（Memory）、AutoGen/AG2
- **与之咬合的观测面**：状态恢复/重放轨迹需要 tracing，见 [[Agent 可观测性 LLM Observability 学习笔记]]（resume 后的 span 重建、HITL 等待成本归因）。

---

## 六、深度盲区（待 Ethon 补充 `- [ ]`）
- [ ] LangGraph `snapshot_frequency=K` 在超长线程下如何权衡「checkpoint 体积 vs 重建延迟」？
- [ ] Durable Execution 的「确定性重放」对 LLM 非确定性调用有哪些陷阱（replay 时如何避免重复 side-effect / 重复花钱）？
- [ ] 多 Agent 并行 sub-task 时，每子 Agent 状态隔离 & 结果聚合回写如何设计（避免共享可变 state 竞争）？
- [ ] HITL 暂停（interrupt / waitForEvent）跨天等待时，状态存储的 TTL / 审计 / 安全边界如何定？
- [ ] Postgres checkpointer 在 >5k checkpoints/hour 下的连接池（asyncpg/psycopg_pool）+ retention 保留策略最佳实践？
- [ ] 「Checkpointing ≠ Durable Execution」——在什么业务边界（恰好一次 side-effect / 跨机器）必须从 checkpointer 升级到 Temporal / Inngest？

---

## 附：来源清单
1. LangGraph 官方/社区文档（aiwiki.ai/wiki/langgraph）—— checkpointer 机制、thread、interrupt、time travel
2. activewizards.com —《LangGraph State Management: Checkpointing, Recovery, and the Persistence Layer Decision》后端选型决策表 + state schema 设计
3. agentnative.dev —《Agentic SaaS Blueprint (2026)》Durable execution 三强（Temporal/Inngest/Restate）对比
4. niteagent.com —《Checkpointing is not durable execution (2026)》五引擎对比表
5. reactify-solutions.com —《Durable AI agents in 2026》Temporal/Inngest/DBOS/Restate 落地差异
6. temporal.io — Durable Execution 官方定位与 Replay 2026 发布

## ⚠️ 待核实清单
- ⚠️ Temporal × OpenAI Agents SDK「Python GA 于 2026-03」、Replay 2026 具体发布项——单源/厂商口径，待官方复核。
- ⚠️ a16z 领投 Temporal $300M Series D——单一来源，未写入具体数字。
- ⚠️ CrewAI「1.14.7 统一 Memory 类」、OpenAI Agents SDK「2026-04 sandbox/subagents」版本号与功能点，以各框架 PyPI/官方 changelog 为准。
- ⚠️ 各家 star / 采用率数字本篇一律未采纳，避免编造。
- ⚠️ Claude Agent SDK「重启丢 transcript、SessionStore 镜像为 best-effort」以 Anthropic 官方 hosting guide 最新版为准。

#标签/AI Agent框架/状态管理
