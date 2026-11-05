---
title: "AI Agent 的流式与实时交互架构"
tags: [广度种子, AIAgent, 流式, 实时交互, 架构]
created: 2026-10-17
source: "WebSearch/WebFetch 联网核实（OpenAI/Anthropic/LangGraph/MCP/A2A/Agent Protocol/Vercel AI SDK 官方与社区资料）+ 公开资料综述"
---

Agent 的流式与实时交互架构，本质是「把一次可能长达数分钟、跨数十次工具调用的 Agent 运行，变成一条可增量观看、可中途干预、可断线续传的事件流」——从「等结果」走向「看过程」。

> 心智锚点：流式（streaming）解决**感知延迟**（token 级、步骤级、状态级增量），实时（real-time）解决**回路延迟**（人机审批、多 Agent 协作、长任务状态同步）。两者正交但常叠加。相关概念见 [[AI Agent 的持久化与状态管理 学习笔记]]（断点续跑依赖 checkpoint）、[[Agent 可观测性 LLM Observability 学习笔记]]（事件流天然就是 trace）、[[Agent 协议生态 学习笔记]]（协议层如何承载事件）。

## 一、定义：什么是 Agent 的流式（streaming）与实时（real-time）交互

| 概念 | 是什么 | 典型载体 | 解决的核心问题 |
|---|---|---|---|
| Token 级流式输出 | 模型每生成一个 token/片段就推送，不等整句完成 | SSE、流式 API、Fetch ReadableStream | 感知延迟（TTFT），避免「空白屏」 |
| 事件流（Event Stream） | 把 Agent 内部「思考—调工具—拿结果」拆成结构化事件推送 | LangGraph `astream_events`、A2A Task*Event、Agent Protocol `/getevents` | 过程可见、可观测、可渲染进度 |
| 长时运行任务的状态推送 | 数分钟/数小时任务中，服务端主动把「working / input-required / completed」推给客户端 | A2A SSE、MCP notifications、Push webhook | 长任务的「活着」信号与结果可达性 |
| 人机协作的实时回路 | 人在执行中途介入：审批、补信息、打断、恢复 | LangGraph `interrupt()`+`Command(resume)`、A2A input-required、MCP MRTR | 把 HITL 从「轮询」升级为「事件驱动」 |

一句话：流式是**输出端**的增量；实时是**回路端**的双向低延迟。Agent 比单纯 Chatbot 更需要后者，因为它会「跑很久、自己调工具、跨进程协作」。

## 二、分类：从传输到渲染的几个正交维度

| 维度 | 选项 | 要点（点到为止） |
|---|---|---|
| 输出流式 - 传输层 | SSE / WebSocket / 流式 API | SSE 单向、HTTP 原生、自动重连，最适合「模型→用户」；WebSocket 全双工，适合「中途发取消/补上下文」；纯流式 API 是厂商封装 |
| 输出流式 - 内部事件 | 中间步骤可见 vs 仅最终文本 | ReAct 步骤、工具调用入参/出参、reasoning 摘要可独立成事件流，前端可分别渲染 |
| 同步 vs 异步 vs 长连接 | 单次响应 / 异步 + 轮询 / 持久 SSE | 短任务用阻塞式；长任务用 SSE 长连接或 webhook 推送，避免空轮询 |
| 前端渲染方式 | 增量渲染 / 打字机 / thinking 可见 | token 增量拼接；thinking/reasoning 块独立显示；工具调用以「卡片/进度条」呈现 |
| 可恢复性 | 可断线重连 vs 一次性 | 关键看是否支持 `Last-Event-ID` / session 恢复（MCP、A2A 已定义机制） |

## 三、主流方案与协议（点到为止）

| 方案/协议 | 流式/实时机制 | 定位 | 备注 |
|---|---|---|---|
| OpenAI 流式 API | Chat Completions `stream=True`（delta）+ `stream_options.include_usage`；Responses API `response.output_text.delta` | 模型输出层 | 用法统计只在末块；token 边界跨块需重算 |
| Anthropic 流式 API | `messages.stream()`，typed events：`message_start/content_block_start/content_block_delta/message_stop` | 模型输出层 | 输入 token 在 start、输出 token 在 end；工具调用增量需累积 |
| SSE（Server-Sent Events） | `text/event-stream` 长连接，单向、自带重连 | 通用 Web 流式底座 | 多数 LLM/协议事实标准；非双向 |
| WebSocket | 全双工长连接 | 需双向信号场景 | 适合取消/补上下文；运维复杂度高 |
| ReAct 步骤流式 | 把「思考→行动→观察」拆事件 | 框架层 | reasoning 与工具调用可分别显示 |
| LangGraph 流式 | `stream_mode`: `values`(全状态)/`updates`(增量)/`messages`(消息级 token+工具)/`events`(`astream_events` v2 最细粒度)；v1.1+ 通过 `chunk["interrupts"]` 直接推审批 | Agent 编排层 | 1.0 GA（2025-10-22）；`interrupt()`+`Command(resume)` 配 checkpointer 做 durable execution |
| MCP 的 notifications | Streamable HTTP（2025-03 取代旧 HTTP+SSE，旧版 2025-05 弃用）；服务端主动通知、`Mcp-Session-Id`、`Last-Event-ID` 断线重放；MRTR（Multi Round-Trip）表达「要人补信息」 | Agent↔工具层 | 协议层「实时」，非 token 流；SEP-2575 推 `subscriptions/listen` 长连接订阅 |
| Agent Protocol（AGI Inc / 原 AI Engineer Foundation） | REST `/ap/v1/agent/tasks`+`/steps`+`/artifacts`；`/getevents?stream=True` 推 `step_created/step_updated/artifacts_created` 等事件 | Agent 生命周期/控制台层 | 刻意保守：不新造传输，偏「可持久、可检视」的工作流引擎而非细粒度 token 流 |
| A2A（Agent2Agent，Google，2025-04-09，Linux Foundation 治理） | Agent Card 发现；Task 状态机（submitted/working/input-required/completed/failed/canceled）；`tasks/sendSubscribe` 用 SSE 推 `TaskStatusUpdateEvent`/`TaskArtifactUpdateEvent`；webhook push | Agent↔Agent 层 | 与 MCP 互补：MCP 连工具，A2A 连 Agent；声明 `capabilities.streaming`/`pushNotifications` |
| Vercel AI SDK（前端流式框架） | `streamText`+`toDataStreamResponse` 走 Data Stream Protocol；`useChat`/`useCompletion` 管理消息/状态/错误/`stop`；`parts`（text/tool invocation/tool result）；`status`（submitted/streaming/ready/error） | 前端 UI 层 | 抽象掉 SSE 解析；provider 无关 |

> 分层关系：模型层（OpenAI/Anthropic）→ 前端框架层（Vercel AI SDK）→ Agent 编排层（LangGraph）→ 工具协议层（MCP）→ Agent 间协议层（A2A）→ 生命周期/控制台层（Agent Protocol）。网关/鉴权通常夹在模型层前，见 [[模型服务化与 LLM 网关 学习笔记]]。

## 四、2025-2026 进展（点到为止，媒体口径标注「待核实」）

| 进展方向 | 2025-2026 表现 | 信号来源 |
|---|---|---|
| Agent 中间过程可观测流式 | 「thinking/reasoning 可见」成为主流 UI 范式；中间步骤作为独立事件流渲染而非藏后厨 | LangGraph `stream_mode="messages"` + `output_version="responses/v1"`；社区把 reasoning 当结构化 content block |
| 多步任务进度条/状态机可视化 | 长任务用状态机（working/input-required/completed）+ 进度条/进度Feed，告别「一直转圈」 | A2A Task 状态机、Agent Protocol Step 事件、前端 progress Feed |
| human-in-the-loop 实时审批回路 | 从「逐条轮询审批」升级为「事件驱动审批会话」；按可逆性分级（只读→可逆→不可逆强制同步门） | LangGraph interrupt、Temporal Signals、Realtime Collaboration APIs（2025 末–2026 初）；**「审批疲劳」 Anthropic 称用户批准 93% Claude Code 提示（2026-03），具体数字待核实** |
| 边缘/端侧流式推理 | 手机 NPU（骁龙 8 Elite 75 TOPS、A18/A19 Pro Neural Engine）跑量化小模型；StreamingLLM（attention sinks）、KV cache 压缩、speculative decoding（Medusa/EAGLE）、diffusion LLM 提速；Android 侧 Google AI Edge（LiteRT/MediaPipe/Gemini Nano via AICore） | 端侧 Agent 延迟/功耗/设备矩阵是核心约束；**iPhone 17 Pro 跑 397B 模型等属概念验证，未规模化，待核实** |
| 协议收敛 | MCP Streamable HTTP 标准化、A2A 捐 Linux Foundation、Agent Protocol 2025 草案——事件/任务生命周期逐渐成为「协议公民」 | 多协议互补而非竞争 |

## 五、代表产品/框架横向对比

| 产品/框架 | 层 | 流式粒度 | 实时回路 | 开源/治理 |
|---|---|---|---|---|
| OpenAI / Anthropic API | 模型 | token 级 | 无（仅输出） | 闭源厂商 API |
| LangGraph | 编排 | token + 步骤 + 事件（v2） | `interrupt`/断点恢复 | 开源（LangChain） |
| MCP | 工具协议 | 通知级（非 token） | 服务端通知 + MRTR | 开源（Anthropic+社区） |
| A2A | Agent 间 | 任务状态/工件增量（SSE） | input-required + push | 开源（Linux Foundation） |
| Agent Protocol | 生命周期 | step/artifact 事件 | WaitForInput/Resume | 开源（AGI Inc） |
| Vercel AI SDK | 前端 | token + 工具调用块 | stop/abort | 开源 |
| Temporal | 工作流引擎 | signal/等待条件 | `@workflow.signal` 外部入口 | 开源/商业 |

> 多 Agent 协作场景下的事件路由与状态同步，参见 [[多智能体协作与编排 学习笔记]]；跨协议 trace 传播见 [[Agent 可观测性 LLM Observability 学习笔记]]。

## 六、深度盲区（待解问题）

- [ ] 长任务断线重连与状态恢复：MCP/A2A 已定义 `Last-Event-ID`/session 机制，但「前端断网 + Agent 仍在跑 + 重连后如何对齐已流失事件」的工程范式仍不成熟。
- [ ] 流式输出的可撤销性（undo）：token 已渲染到一半，用户想「撤销这一句/这一步」——增量 UI 与不可逆工具调用之间的回滚边界如何定义？
- [ ] 成本与延迟权衡：流式降低 TTFT 但增加连接/重传开销；thinking 块、中间步骤全量推送在移动弱网下是否值得？
- [ ] 移动端弱网流式降级：Android 弱网/省电模式下，SSE 长连接被系统杀死时，如何优雅降级为轮询或本地端侧续跑（接 [[AI Agent 的持久化与状态管理 学习笔记]]）？
- [ ] HITL 实时审批的「疲劳 vs 漏判」均衡：审批疲劳使人工门控形同虚设（Rippling 将「Overwhelming HITL」列为威胁 T10）；基于可逆性的自动分级能否落地为通用 UX 标准？
- [ ] 边缘/端侧流式与云端流式的统一抽象：同一 Agent 在端侧（低带宽、断网优先）与云端（高带宽）是否需要两套流式管线？

## 附：来源清单

| 标题 | URL | 性质 |
|---|---|---|
| LangGraph Streaming Events and Modes (DeepWiki) | https://deepwiki.com/langchain-ai/langchain-academy/6.3-streaming-events-and-modes | 官方/社区文档衍生 |
| Streaming AI Agent with FastAPI & LangGraph (2025-26 Guide) | https://practicaldev.herokuapp.com/kasi_viswanath/streaming-ai-agent-with-fastapi-langgraph-2025-26-guide-1nkn | 社区/教程 |
| MCP Streaming and Triggers (GingerLabs) | https://gingerlabs.ai/blog/mcp-streaming-triggers-real-time-events-ai-agents | 社区/技术博客 |
| SEP-2575: Make MCP Stateless | https://modelcontextprotocol.net/seps/2575-stateless-mcp | 协议草案 |
| A2A Protocol (Agent2Agent) — a2aprotocol.ai / Taskade Wiki | https://www.taskade.com/wiki/ai/agent-to-agent-protocol | 社区文档 |
| A2A: Google's Agent-to-Agent protocol (noze.it) | https://www.noze.it/en/insights/a2a-agent-to-agent | 社区/分析 |
| Agent Protocol 官方站 | https://agentprotocol.ai/ | 官方 |
| Agent Protocol (2025 edition draft, GitHub) | https://www.github.com/colesmcintosh/agent-protocol | 协议草案 |
| Vercel AI SDK — Chatbot / useChat | https://sdk.vercel.ai/docs/ai-sdk-ui/chatbot | 官方文档 |
| How to Stream LLM Responses (OpenAI/Anthropic SSE) | https://getaibook.com/blog/how-to-stream-llm-responses-in-your-application/ | 社区/教程 |
| Human-in-the-Loop AI Agents: 2026 Guide (NeuralTrust) | https://neuraltrust.ai/blog/human-in-the-loop-ai-agents | 社区/分析（引 Anthropic/OWASP/Gartner） |
| LangGraph, Temporal, Humanloop: The HITL Tooling Race in 2026 | https://www.bestaiweb.ai/langgraph-interrupt-temporal-signals-and-humanloop-the-hitl-tooling-race-reshaping-agents-in-2026 | 社区/分析 |
| On-Device LLMs: State of the Union, 2026 | https://v-chandra.github.io/on-device-llms | 学术/综述 |
| On-Device AI: Run LLMs Locally on Mobile (Codestreaks) | https://www.codestreaks.com/blog/on-device-ai-running-llms-locally-for-privacy-first-mobile-saas | 社区/分析 |

## ⚠️ 待核实清单

- Anthropic「用户批准 93% Claude Code 权限提示」「新用户约 20% 全自动批准、750 会话后超 40%」为 NeuralTrust 引述的 Anthropic 2026 研究数据，**厂商自述，具体样本与口径待核实**。
- Gartner「到 2027 年底超 40% agentic AI 项目被取消」为分析师预测，**非承诺数字，待核实**。
- 文中出现的模型版本号（如 `gpt-5.4`、`gpt-5.2`、`claude-sonnet-4-6`、`claude-opus-4-6`、`Qwen3.5-397B` 等）散见于不同来源，**精确命名/发布状态以各家官方文档为准，待核实**。
- 「iPhone 17 Pro 跑 397B 模型约 1 token/s」「Flash-MoE 概念验证」属社区/媒体 PoC 报道，**未规模化、性能数字待核实**。
- 端侧 NPU TOPS 数值（骁龙 8 Elite 75 TOPS、移动内存带宽 50-90 GB/s vs 数据中心 2-3 TB/s）来自 2026 综述/媒体，**随芯片世代变动，待核实**。
- OWASP LLM06:2025「Excessive Agency」、EU AI Act Article 14 人类监督（自 2027-12-02 适用，依据 Regulation (EU) 2026/1744）为合规文本，**生效时间与适用边界以官方公报为准，待核实**。
- MCP「Streamable HTTP 取代旧 HTTP+SSE（2025-05 弃用）」、A2A「2025-04-09 发布、2025-06 捐 Linux Foundation」为社区记录，**以官方仓库发布历史为准，待核实**。

#标签/AI Agent 框架 #标签/流式 #标签/实时交互 #标签/架构
