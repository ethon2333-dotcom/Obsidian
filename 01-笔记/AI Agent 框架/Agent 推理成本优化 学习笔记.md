---
title: "Agent 推理成本优化"
tags: [广度种子, Agent, 推理成本, 成本优化]
created: 2026-08-19
source: "WebSearch/WebFetch 联网核实 + 公开资料综述"
---

> **一句话心智模型**：Agent 反复调用 LLM，推理成本优化 = 让"重复的算力只算一次"（cache / prefix sharing / batching）+ "用对的模型做对的事"（模型路由 / 端侧兜底），把 token、延迟、$ 三笔账一起压下来。

---

## 1. 推理成本的构成：为什么 Agent 比单次对话更烧钱

> 辐射锚点：AI Agent 框架。Agent 不是"一次问答"，而是**反复、多路径**地调 LLM，成本被结构性放大。

| 成本维度 | 含义 | 备注（联网核实） |
|---|---|---|
| **Token 数** | input + output 分别计费；output 通常比 input 贵 **2–4×** | 来源：intellineers / thread-transfer 2025 成本结构分析 |
| **延迟** | TTFT（首 token）、TPOT（每 token）、端到端步数 | Agent 多步链路把延迟"乘"起来 |
| **$** | 云 API 按 token 计费；自托管按 GPU·小时 | 生产 LLM 系统常 50–70% 推理成本花在"非必要"工作（aimenta 2025） |

**Agent 特有的"烧钱放大器"**（区别于单次对话）：

- **多轮 tool call / 反思循环**：每轮重发 system prompt + 历史上下文 → 上下文 token 线性累积。
- **多 agent 扇出**：一个任务拆成 N 个子 agent，共享同一份长 system prompt 与项目上下文，重复计算爆炸（见 [[多智能体协作与编排 学习笔记]]）。
- **重试 / 回退**：路由失败、429 限流重试会重复烧 token。

---

## 2. 优化手段表（点到为止，BREADTH > DEPTH）

| 手段 | 一句话 | 代表实现 / 厂商特性 | 大致收益（待核实口径见末尾） |
|---|---|---|---|
| **Prompt Caching（厂商侧）** | 把稳定前缀的"计算结果"存下来，重复调用只付零头 | Anthropic：显式 `cache_control`，read 0.10× / write 1.25×/2.0×（5min/1h TTL），1024 token 起，≤4 断点；OpenAI：自动，≥1024 token，cached input **50% off**；Gemini 2.5+：隐式/显式，cached ≈0.25× 或 10%（**冲突，待核实**） | Anthropic 自报最长前缀 **最高 90% 降本、85% 降延迟**（2025） |
| **KV Cache 复用 / Prefix Sharing（引擎侧）** | 跨请求复用相同前缀的 KV 张量，共享前缀"只算一次" | vLLM：PagedAttention + Automatic Prefix Caching（v1 默认开）；SGLang：RadixAttention 基数树 token 级匹配（默认开，多 agent 扇出强）；HiCache 层级缓存 GPU→CPU→disk | 活跃会话命中率可达 **95%+**；共享前缀越多优势越大（turion.ai / flexera 2026） |
| **Batching / 请求合并** | 把非实时请求攒批，摊薄固定开销、提升 GPU 利用率 | Continuous batching（token 级调度）；Batch API（OpenAI `/v1/batches`、Anthropic Message Batches）折扣 **最高 50%** | 适合离线标注、审核、批量摘要；云 API 省 $、自托管省 GPU |
| **Semantic Cache（语义缓存）** | 用 embedding 相似度命中"意思相同"的请求，直接返缓存 | GPTCache、Helicone 内置；Redis + 向量相似度 | 命中率常见 30–50%；2024 arXiv 研究称最高减少 API 调用 **68.8%**（语义缓存有"答非所问"风险，需校验） |
| **模型路由 Model Routing** | 简单任务走小/便宜模型，难题才上大模型 | LLMProxy、OpenRouter、Portkey（含 fallback 级联）；router 本身跑小模型 | 60–80% 请求走便宜模型 → 平均降本 **50–65%**（aimenta 2025） |
| **量化与成本的协同** | 低精度让"更小模型/更省显存"成立，从根上降本 | 权重量化：FP8 <1% 损、INT8 ~2%、INT4 8–10%；**KV Cache 量化 FP8/INT8 显存减半、提速**；端侧 SLM 跑本地免云费 | 与端侧部署强耦合（见 [[端侧大模型推理 学习笔记]]） |

---

## 3. 2025–2026 进展（联网核实）

- **厂商普遍上线 prompt caching**：Anthropic（自动 + 显式双模式）、OpenAI（自动；GPT-5.6+ 改显式、write 1.25×）、Google Gemini（隐式/显式）、AWS Bedrock（checkpoint 模式，Claude 1 小时 TTL 于 2026-01 GA）、Azure OpenAI（与直连 API 同机制）。
- **KV Cache 跨请求复用成为引擎默认能力**：vLLM v1 prefix caching 默认开；SGLang RadixAttention 默认开；层级缓存（HiCache）把热 KV 留在 GPU、冷 KV 沉降到 CPU/磁盘。
- **推理引擎格局变化**：Hugging Face TGI 于 2025-12 进入维护模式，SGLang 成为主流替代之一（turion.ai 2026）。
- **成本可观测成为标配**：LangSmith / Langfuse / Helicone / Phoenix / Portkey / OpenLLMetry 均支持 per-user、per-feature、per-model 的成本归因与预算告警——与 [[Agent 可观测性 LLM Observability 学习笔记]] 直接呼应。

---

## 4. 代表产品 / 玩家

| 类别 | 代表 | 与成本优化的关系 |
|---|---|---|
| 云厂商 cache 政策 | Anthropic、OpenAI、Google Gemini、AWS Bedrock、Azure OpenAI | 前缀缓存折扣梯度不同（50%–90% off），TTL/断点策略各异 |
| 推理服务引擎 | vLLM（PagedAttention）、SGLang（RadixAttention）、TensorRT-LLM、llama.cpp | 自托管按 GPU·小时计费，prefix sharing 提升"每 GPU 服务请求数" |
| 成本追踪 / 可观测 | LangSmith、Langfuse、Helicone（含内置缓存/路由）、Portkey、OpenLLMetry（OTel） | 把"哪条链路在烧钱"变成可度量、可告警 |
| 语义缓存 / 路由中间件 | GPTCache、Helicone、LLMProxy、OpenRouter | 在网关层做命中与级联，免改业务代码 |

---

## 5. 对 OS PM / Agent 产品的意义

> 端侧 Agent 没有"token 账单"，但有一套等价的**算力 / 功耗预算**——成本优化的思路在端侧换了一种货币。

- **成本结构不同**：端侧没有按 token 扣费，约束来自 NPU 利用率、内存（含 KV Cache 占用）、电池、散热与响应延迟 SLO。成本优化 → 同样预算下能跑更长上下文、更大模型，或同样体验更省电。
- **端云协同 = 模型路由的端侧版本**：简单意图走端侧小模型（SLM，免云调用费、隐私好、零网络延迟），复杂任务才上云大模型——正是第 2 节"模型路由"的产品化落地（见 [[端云协同推理与混合部署 学习笔记]]）。
- **量化是端侧降本的基石**：INT4/INT8 让 3B 级模型跑在端侧，直接省掉云端推理费；KV Cache 量化（FP8/INT8）在长上下文 Agent 里尤其关键——否则多轮 + 多 agent 的 KV 会先撑爆内存。
- **Prefix sharing 在端侧同样成立**：一个系统里多个 agent / 多用户共享同一份系统提示与项目上下文，端侧引擎的 prefix 复用能避免重复 prefill，降低首 token 延迟。
- **可观测性的端侧翻译**：云上的"成本归因"在端侧变为"功耗 / 延迟 / 内存归因"——哪些 tool call、哪条反思循环最费电，需要同样的可追踪能力（呼应 [[Agent 可观测性 LLM Observability 学习笔记]]）。
- **路由效果要评测兜底**：路由把简单请求降级到小模型，必须用 [[Agent 评测与基准 学习笔记]] 的指标体系验证"降本不降质"，否则静默退化。

---

## 待解问题

- [ ] 厂商 cache 折扣口径（尤其 Gemini cached token 是 10% 还是 25% of base）应以哪一版官方文档为准？
- [ ] RadixAttention vs vLLM Automatic Prefix Caching，在多 agent 扇出场景的真实命中率差异有多大（缺一手基准）？
- [ ] 语义缓存的"相似误命中"在 Agent 多步链路里如何设安全边界（避免答非所问被缓存放大）？
- [ ] 端侧 KV Cache 量化（FP8/INT4）对 tool-calling、长上下文任务的质量退化阈值是多少？
- [ ] 模型路由的 router 自身成本与延迟，何时会"为省钱反而更贵"（小模型路由 + 回退次数多）？
- [ ] 端侧 Agent 的"功耗/延迟预算"应如何建模成与云端 $ 可比的 ROI 指标？

---

## 附：来源清单

| 来源 | 主题 | 获取方式 |
|---|---|---|
| Anthropic Prompt Caching 文档（2025，经 promptvlt / hashlytics / thread-transfer 综述） | 厂商侧前缀缓存机制与折扣 | WebSearch 综述 |
| OpenAI / Google Gemini 官方 caching 说明（经上述综述） | 自动/隐式缓存、50% off、0.25× 口径 | WebSearch 综述 |
| Flexera "Prompt Caching breakdown"（2026） | AWS Bedrock checkpoint、各厂商模式对照 | WebSearch |
| turion.ai "vLLM vs SGLang 2026" / aimadetools / dreaming.press | RadixAttention vs PagedAttention、prefix caching 命中率 | WebSearch |
| intellineers / aimenta / aronhack / eidm "LLM cost optimization"（2025） | 语义缓存、模型路由、批处理、成本结构 | WebSearch |
| zylos.ai "AI Inference Optimization 2025-2026"、ai-master.cc、majid-mazouchi | 量化（FP8/INT8/INT4）、KV Cache 量化、压缩 | WebSearch |
| integritystudio / zenml / comet "LLM Observability 2025" | LangSmith/Langfuse/Helicone/Portkey/OpenLLMetry 成本归因 | WebSearch |

---

## ⚠️ 待核实清单

- **Gemini 缓存折扣冲突**：promptvlt 称 Gemini 2.5 cached token 为 standard input 的 **10%**；thread-transfer / hashlytics 称 **0.25×（25%）**。两者不一致，需以 Google 官方最新文档为准，本文未采用确定值。
- **Anthropic cache 命中率/折扣**：90% 降本、85% 降延迟为 Anthropic 官方自报的"最长前缀"上限值，非平均；实际取决于前缀长度、TTL 命中与流量形态。
- **语义缓存 68.8% 降幅**：来自 2024 arXiv 研究，针对特定 query 类别，非通用生产均值；30–50% 命中率为多来源共识区间。
- **模型路由 50–65% 降本**：依赖"60–80% 请求可走便宜模型"且小模型成本为前沿模型 1/10 的假设，需结合自有 eval 验证。
- **端侧量化质量退化**：INT4 在 math/code/long-context/tool-calling 上退化大于闲聊，阈值未统一，待针对目标模型实测。

---

#标签/Agent #标签/推理成本 #标签/成本优化 #标签/AI Agent框架
