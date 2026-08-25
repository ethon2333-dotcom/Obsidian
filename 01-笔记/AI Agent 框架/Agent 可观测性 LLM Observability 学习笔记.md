---
title: "Agent 可观测性 / LLM Observability"
tags: [广度种子, AIAgent, 可观测性]
created: 2026-08-17
source: "WebSearch/WebFetch 联网核实 + 公开资料综述"
---

Agent 可观测性（LLM Observability）是「给生产环境里的 LLM Agent 装黑匣子」——把每一次推理、工具调用、检索、成本与用户反馈都变成可回放、可度量、可告警的 trace，本质是**在线行为监控**，区别于 [[Agent 评测与基准 学习笔记]] 中的离线基准 accuracy。

## 一、心智锚点：在线 vs 离线

| 维度 | 在线可观测（本篇） | 离线评测基准（另篇） |
|---|---|---|
| 关注点 | 生产真实流量里 Agent 的行为 | 固定数据集上的准确率/能力上限 |
| 手段 | tracing / monitoring / 在线 eval | benchmark / 数据集跑分 |
| 价值 | 及时发现退化、成本爆炸、异常 | 选型、横向对比、发布前门禁 |
| 代表 | LangSmith / Langfuse / Phoenix | MMLU / AgentBench 等 |

两者互补：离线基准管「该不该上线」，在线可观测管「上线后有没有坏」。详见 [[Agent 评测与基准 学习笔记]]。

## 二、核心能力（点到为止）

| 能力 | 是什么 | 关键信号 |
|---|---|---|
| Tracing 链路追踪 | 把一次 Agent run 拆成 span 树（LLM/TOOL/RETRIEVER…） | span、parent-child、session.id、user.id |
| 在线 Eval | 生产流量上跑 LLM-as-Judge / 分数 | groundedness、hallucination rate、task completion |
| Prompt 版本管理 | prompt 变更可追溯、可回滚 | version、A/B |
| Cost & Latency 监控 | 按 run / agent / user 归因 token 与花费 | token_count、cost、TTFT、P95 |
| 用户 Feedback 回路 | 点赞/点踩、会话放弃、重试 | thumbs、abandonment、retry |
| Drift 检测 | 输入/输出质量/成本/行为漂移告警 | rolling avg、PSI、KL | 

工具调用安全（权限、审批）也应作为 span 的 authorization 状态被记录，见 [[工具调用安全 学习笔记]]。

## 三、主流方案横向对比

| 产品 | 开源 | 部署形态 | 定位侧重 |
|---|---|---|---|
| LangSmith | 否（SaaS） | SaaS / 企业自托管 | LangChain 生态深集成 |
| Langfuse | 是（MIT） | OSS 自托管 + Cloud | 开源、可移植、prompt+eval |
| Phoenix / Arize AX | Phoenix 开源（Elastic-2.0） | OSS + 企业云 | eval、embedding drift、OTel 原生 |
| Helicone | 是 | 代理网关 + Cloud | 成本追踪、缓存、多供应商 |
| W&B Weave | 是（部分） | SaaS | MLOps 实验跟踪 |
| Braintrust | 否 | SaaS | eval-first、持续评测循环 |
| Traceloop / OpenLLMetry | 是 | OSS 插桩 + 可选后端 | 供应商中立 OTel 插桩 |
| Datadog LLM Observability | 否 | SaaS（APM 插件） | 与企业现有 APM 统一 |
| AgentOps / Opik | 是（Opik Apache-2.0） | SaaS + OSS | Agent run 级证据、版本方差 |
| OpenLIT | 是 | OSS + SaaS | OTel 原生、含 GPU 监控 |

> 价格（Plus/Pro/Team 档位）各媒体口径差异较大，具体数字**待核实**；自托管普遍免费或按用量。

## 四、与现有 APM / 标准的关系

| 层次 | 角色 | 备注 |
|---|---|---|
| OpenTelemetry (OTel) | 厂商中立传输层（trace/span/OTLP） | 现有 APM（Jaeger/Prometheus/Grafana/Datadog）可直接复用 |
| OpenInference | Arize 主导的 LLM 语义约定（2023 起，较稳定） | span kind：AGENT/LLM/TOOL/RETRIEVER/RERANKER/CHAIN/GUARDRAIL/EVALUATOR/EMBEDDING/PROMPT；默认记录完整消息 |
| OTel GenAI 语义约定 (gen_ai.*) | OTel 社区官方 AI 词汇（2024 立项，2025 首发） | 截至 2026 中仍为 **Development/实验状态**，内容捕获需 opt-in（`OTEL_SEMCONV_STABILITY_OPT_IN=gen_ai_latest_experimental`） |
| 双轨共存 | Phoenix 15.10.0+(2026-05) 可自动把 gen_ai.* 转 OpenInference | 传闻·未证实：Arize 拟将 OpenInference 插桩捐赠给 OTel 项目（待核实） |

普遍结论（2026）：所有主流平台均已 emit/ingest OTel，可在不重新插桩前提下混用或切换。

## 五、对 OS PM 的意义（Android 端侧 / 系统级 Agent）

- **端侧 Agent 上线后怎么监控**：端侧推理无法简单套用云端 SaaS；更可能走 OTel 原生插桩 + 自有后端（或系统级 APM），把「on-device LLM 调用 / tool 调用 / 权限决策」作为 span 上报到系统遥测管道。
- **成本与功耗归因**：每条 Agent run 的 token、延迟、唤醒次数要能按功能/场景归因，才能评估「这个功能值不值得常驻」。
- **稳定性 vs 体验**：端侧非确定性强，需在线 eval + 用户反馈（放弃率、重试）而非仅看 crash rate；可参考 [[Loop Engineering 循环工程]] 把反馈回路接回迭代。
- **系统级护栏可观测**：[[工具调用安全 学习笔记]] 中的授权/审批状态应进入 trace，便于事后审计与越权告警。
- **协议层互联**：Agent 跨应用调用走 MCP/A2A 时，trace 需跨进程传播，关联 [[Agent 协议生态 学习笔记]]。

## 六、待解问题（深度留白）

- [ ] 端侧 Agent 的 trace 如何在不侵犯隐私前提下上报？on-device 聚合还是原始上报？
- [ ] 离线条基准（[[Agent 评测与基准 学习笔记]]）与在线 drift 指标如何对齐成同一套质量语言？
- [ ] OTel GenAI 约定何时进入 stable？现在押 gen_ai.* 还是 OpenInference？
- [ ] 多智能体（[[多智能体协作与编排 学习笔记]]）下，跨 agent 的 cost/latency 归因怎么做？
- [ ] 在线 LLM-as-Judge 本身的成本与可靠性如何评估？
- [ ] 系统级 Agent 的「成功」定义是什么？完成率还是用户留存？
- [ ] 与 Context Engineering（[[Context Engineering 学习笔记]]）的 context 膨胀如何被可观测性量化预警？
- [ ] 自托管 vs SaaS 在数据主权（端侧用户数据）上的合规边界？
- [ ] 如何把 RAG 检索质量（[[RAG 详细学习笔记]]）纳入在线 groundedness 监控？

## 附：来源清单

| 标题 | URL | 性质 |
|---|---|---|
| Top 5 Agent Observability Tools in Dec 2025 | https://getmaxim.ai/articles/top-5-agent-observability-tools-in-december-2025/ | 媒体/厂商 |
| AI Agent Observability & Monitoring Guide 2026 | https://aiagenttools.dev/blog-ai-agent-observability-guide | 媒体 |
| LLM Observability: What Breaks in Production | https://dev.to/devhelm/llm-observability-what-breaks-in-production-and-how-to-instrument-it-4o5d | 社区/技术博客 |
| OpenInference vs OpenTelemetry GenAI Conventions | https://niteagent.com/blog/2026-05-25-openinference-vs-otel-agent-tracing | 社区/技术博客 |
| AI agent tracing and evaluation (Arize) | https://arize.com/resources/ai-agent-tracing-evaluation | 官方 |
| Phoenix OTel GenAI auto-conversion (05.15.2026) | https://www.arize.com/docs/phoenix/release-notes/05-2026/05-15-2026-otel-semconv-conversion | 官方 |
| 8 Best AI Agent Observability Tools in 2026 | https://www.ayautomate.com/blog/best-ai-agent-observability-tools | 媒体 |
| Best LLM Observability Tools 2025 | https://firecrawl.org.cn/blog/best-llm-observability-tools | 媒体 |
| Top 10 Agent Monitoring Software 2026 | https://worldmetrics.org/best/agent-monitoring-software | 媒体（含付费位） |

## ⚠️ 待核实清单

- 各平台 Plus/Pro/Team 价格档位在不同媒体间差异显著（如 Langfuse Pro 有 $25/$59、$199 等说法），**具体价格待核实**，以官网为准。
- 「Arize 拟将 OpenInference 插桩捐赠给 OTel」为 Arize 文档/社区口径提及，**传闻·未证实**，待核实。
- OTel GenAI 语义约定的 stable 发布时间无公开承诺，**待核实**。
- 部分厂商所谓「百万级月下载/客户名单」为厂商自述，**待核实**。
- Phoenix 与 LangSmith 等 free tier 的额度（50K observations、5K traces 等）随套餐变动，**待核实**。

#标签/AIAgent/可观测性
