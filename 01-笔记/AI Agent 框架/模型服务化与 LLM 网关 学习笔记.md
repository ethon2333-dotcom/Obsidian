---
title: 模型服务化与 LLM 网关 学习笔记
tags: [LLM网关, 模型服务化, AI Agent框架, 基础设施, BREADTH]
created: 2026-09-04
source:
  - "techsy.io — Best LLM Gateway 2026 (2026-07-25)"
  - "futureagi.com — Best LLM Gateways in 2026"
  - "wetheflywheel.com — AI Gateways & LLM Routing: The 2026 Guide (2026-06-10)"
  - "inventivehq.com — Find your AI gateway (对比器)"
  - "devopsness.com — AI Gateway Comparison (Portkey/LiteLLM/Cloudflare)"
  - "helicone.ai — OpenRouter Alternatives in 2025"
  - "opticflux.com — LLM API Gateway Explained"
---

# 模型服务化与 LLM 网关 学习笔记

> **一句话心智模型**：LLM 网关是「应用与一堆模型供应商之间的统一接入层 + 控制面」——你的代码只调一个 OpenAI 兼容端点，网关负责路由、兜底、限流、密钥、缓存、守护与埋点，把"多供应商运维"这件苦活从业务里剥离出来。

> 本文是「AI Agent 框架」锚点向外辐射的一跳，聚焦**网关 / 服务化基础设施层**。它与 [[Agent 推理成本优化 学习笔记]] 互补但不同：那篇讲具体的成本优化*技巧*（prompt caching / 投机采样 / 上下文裁剪本身），本篇讲支撑这些技巧的*接入与治理基础设施*。

## 1. 定义：网关 ≠ 代理 ≠ 路由器

三者常被混用，职责有梯度（据 wetheflywheel / ai-solutions.wiki）：

- **LLM Proxy**：转发请求 + 加日志，逻辑最少。
- **LLM Router**：按成本 / 延迟 / 内容给每次请求挑最优模型或供应商。
- **LLM Gateway**：完整包——proxy + router + 成本追踪 + 缓存 + 守护(guardrails) + 可观测。

**何时需要网关**：调用 ≥2 个供应商、需要跨供应商成本归因、需要供应商宕机自动 failover、需要跨供应商 prompt 缓存。单供应商且无意切换则不必引入。

## 2. 分类（按部署形态）

| 形态 | 代表 | 选型要点 |
|---|---|---|
| 自建 / 开源 (self-hosted OSS) | LiteLLM、Helicone OSS、Portkey OSS | 数据不出网、无按调用抽成；代价是自己运维(Redis/PG/扩缩容) |
| 托管 SaaS / 聚合器 | OpenRouter、Portkey 托管、Cloudflare AI Gateway、Vercel AI Gateway、FutureAGI ACC | 最快接入、零运维；代价是按调用收费 + 流量过其基础设施 |
| 云厂商原生 | Azure AI Gateway / Azure AI Foundry、AWS Bedrock、GCP Vertex / Apigee | 深度集成自家云栈；但主要 front 自家模型，跨厂商灵活性弱 |
| 企业 API 管理扩展 | Kong AI Gateway、Traefik Hub AI Gateway | 已有 API 网关的组织"顺手扩展"，统一控制面治理 API+AI 流量 |

> 第一性分叉往往是「托管 vs 自建」——数据驻留(合规)通常比功能清单更决定选型。

## 3. 主流方案对比（广度覆盖，点到为止）

| 产品 | 形态 | 核心能力 | 备注 / 待核实 |
|---|---|---|---|
| **LiteLLM** | 自建 OSS (Python proxy) | 100+ 供应商、OpenAI 兼容、fallback / 负载均衡 / 预算 / 虚拟密钥 | 许可证 BSL 1.1(fair-use)；生产需 Redis+PostgreSQL；延迟开销约 10–50ms |
| **Portkey** | 混合 (OSS + 托管) | 1,600+ 模型、路由 / fallback / 负载均衡 / 守护 / prompt 管理 | MIT；托管从 $49/mo 起；⚠️ 多家来源称 2026-05-29 被 Palo Alto Networks 收购并入 Prisma AIRS，**待核实官方口径** |
| **Cloudflare AI Gateway** | 托管 (边缘) | 缓存 / 限流 / 重试 fallback / 动态路由 / 分析 | 免费层；边缘低延迟；深度路由逻辑弱于自建 |
| **OpenRouter** | 托管 SaaS 聚合器 | 300–500+ 模型 / 60+ 供应商、单一端点、按 token 计费 | 零搭建、模型最广；几乎无内置可观测；可 BYOK |
| **Azure AI Gateway / AI Foundry** | 云原生 | 路由 / 配额 / 内容守护 / 计费(走 Azure) | 主要 front Azure 模型；与 Azure 治理深度绑定 |
| **Kong AI Gateway** | 企业 API 管理扩展 | 在已有 Kong 上加 LLM 路由 / prompt 模板 / token 限流 / 语义缓存 | 适合 Kong 已是标准的组织，统一控制面 |
| **Helicone** | OSS 优先(可观测) | 网关 + tracing / 成本分析 / 缓存 / 限流 | Apache 2.0；Pro $79/mo；⚠️ 有来源称 2026-03 被 Mintlify 收购转维护模式，**待核实** |
| **FutureAGI ACC** | 托管 + 可自建 | 网关 + eval gates + 18+ 运行时守护 + BYOK | Apache 2.0；强在把"评测契约"直接焊进网关 |

> 数字口径（模型数、价格、star 数）各源差异大，本表仅列相对量级；精确数字以各产品官方文档为准。

## 4. 网关的八大能力面（基础设施层该覆盖什么）

1. **统一 API 接入层**：OpenAI 兼容 HTTP，屏蔽各供应商 SDK 差异；换模型只改 YAML / 配置，不改业务代码。
2. **模型路由**：按能力(强模型做难任务/小模型做分类)、成本(70% 流量走最便宜够用的模型)、延迟选路；可规则 / 分类器 / embedding 路由。
3. **限流与配额**：per-user / per-project / per-team 预算上限，硬切断 vs 软告警。
4. **密钥管理**：虚拟密钥 / BYOK，避免把真实供应商 key 散落各处。
5. **负载均衡与 fallback**：加权 / 按延迟 / 按成本分流；failover 链(主→同能力备份→小模型兜底)，错误(5xx / 配额 / 上下文溢出)自动游走。
6. **守护 (guardrails)**：输入/输出校验——PII 检测与脱敏、prompt injection 筛查、敏感词 /  toxicity / 品牌语气 / 自定义正则。
7. **可观测埋点**：每个请求发射 OTel 兼容 span(含 prompt/response/model/延迟/成本)，与 [[Agent 可观测性 LLM Observability 学习笔记]] 咬合。
8. **缓存**：精确匹配缓存 + 语义缓存(embedding 近似)，重复 query 直接命中，砍延迟与成本。

> **Wrap-then-replace 模式**：LiteLLM / Portkey 可把 OpenRouter 当作"一个供应商"前置——既保留其模型广度，又加上自建治理/缓存，避免 all-or-nothing 迁移。

## 5. 2025–2026 进展（公开资料归纳）

- **市场收敛到少数主流**：LiteLLM(开源事实标准)、OpenRouter(聚合器)、Portkey / Helicone / Cloudflare 占据各自甜区。
- **所有权变动频繁**：⚠️ Portkey → Palo Alto Networks(2026-05-29，据 techsy)、Helicone → Mintlify(2026-03，据 techsy)、**TensorZero 据称 2026-06 归档停止维护**(techsy)——均**待核实官方**。
- **新入场者**：Merge Gateway(据称 2026-03-31 发布，企业级按客户/功能路由与支出归属)、Bifrost(Go 架构，号称 ~11µs 开销、>5000 RPS)、FutureAGI ACC(网关+evals 一体)。
- **标准化**：OpenTelemetry / OpenInference 语义约定成为埋点互通基准(见 [[Agent 可观测性 LLM Observability 学习笔记]])。
- **与 Agent 协议分层清晰化**：网关是*传输/治理基础设施层*，与 [[Agent 协议生态 学习笔记]] 中的 MCP / A2A 等*应用协议层*正交——协议决定 agent 间"怎么对话"，网关决定"调模型时怎么路由/守护/记账"。

## 6. 与 Agent 技术栈的关系

| Agent 栈位置 | 与网关的关系 |
|---|---|
| Agent 框架 / 编排层 (LangChain / LangGraph / 多智能体) | 业务代码只调网关统一端点；多 agent 扇出时网关提供 per-agent / per-tenant 预算与路由（见 [[多智能体协作与编排 学习笔记]]） |
| 可观测层 | 网关发射的 span 汇入 [[Agent 可观测性 LLM Observability 学习笔记]] 的 tracing 后端 |
| 成本优化层 | 网关的路由/缓存/配额是 [[Agent 推理成本优化 学习笔记]] 中技巧(缓存/路由)的*承载基础设施*，本篇不重复讲技巧本身 |
| 协议层 | 网关 ≠ MCP/A2A；二者正交，见 [[Agent 协议生态 学习笔记]] |
| 守护 / 安全 | 网关的内容审核 + 敏感词是前置于模型的"第一道闸门"，与 [[Agent 可观测性 LLM Observability 学习笔记]] 的安全边界互补 |

## 7. BREADTH > DEPTH：深度盲区（待 Ethon 后续补）

- [ ] 各网关「语义缓存」命中率与失效策略的实测对比（公开 benchmark 稀缺）
- [ ] 自建 LiteLLM 的高可用部署拓扑（Redis/PG 单点、健康探针、蓝绿）
- [ ] 网关引入的额外延迟 hops 在端侧 Agent(Android OS) 场景是否可接受？与端侧推理如何分工
- [ ] 虚拟密钥 / BYOK 的轮换与审计在合规(等保/GDPR)下的落地清单
- [ ] 模型路由策略(能力分级)如何与 agent 的"任务复杂度分类"对齐——能否复用 [[Loop Engineering 循环工程]] 的循环分型
- [ ] Portkey 被 Palo Alto 收购后对开源协议与定价走向的影响（**待核实**）
- [ ] 网关层 guardrails 与模型层安全微调的职责边界，避免过度拦截误杀正常请求

## 附：来源清单

- techsy.io — Best LLM Gateway Tools Ranked for 2026（2026-07-25，含所有权变动与 star 数）
- futureagi.com — Best LLM Gateways in 2026: 7 Provider Routing Platforms Compared
- wetheflywheel.com — AI Gateways & LLM Routing: The 2026 Guide（2026-06-10 核验）
- inventivehq.com — Find your AI gateway（多厂商对比器）
- devopsness.com — AI Gateway Comparison (Portkey / LiteLLM / Cloudflare)
- helicone.ai — OpenRouter Alternatives in 2025
- opticflux.com — LLM API Gateway Explained: Routing, Failover, Costs
- ai-solutions.wiki — Multi-Model Routing（proxy vs recommender 区分）

## ⚠️ 待核实清单

- ⚠️ Portkey 被 Palo Alto Networks 收购（2026-05-29）的官方口径与对开源影响。
- ⚠️ Helicone 被 Mintlify 收购（2026-03）并转维护模式的真实性。
- ⚠️ TensorZero 2026-06 归档停止维护一说，需官方仓库确认。
- ⚠️ Merge Gateway / Bifrost / FutureAGI ACC 的发布时间、许可证与性能数字（来自二手博客，未查官方）。
- ⚠️ 各产品「模型数 / 价格 / GitHub star」各源差距大，本笔记未写入精确数字，以官方为准。

#标签/AI Agent 框架
#标签/基础设施
#标签/LLM网关
