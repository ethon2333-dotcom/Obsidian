---
title: Agent 推理成本优化 学习笔记
tags: [llm-cost, inference-optimization, prompt-caching, agent, agent-cost, 广度种子]
created: 2026-09-01
source: "WebSearch/WebFetch 联网核实（Anthropic/OpenAI 官方文档 + vLLM/SGLang 资料 + 2025-2026 路由/网关综述）"
---

> **一句话心智模型**：Agent 的成本不在单次生成，而在多轮长上下文的重复计算——复用缓存与分级路由是核心，把"token / 延迟 / $"三笔账一起压下来。

本笔记是从 [[多智能体协作与编排 学习笔记]]（多 agent 扇出放大成本）与 [[Agent 可观测性 LLM Observability 学习笔记]]（成本归因、预算告警）向外辐射的广度种子，聚焦"成本优化工程面"。已覆盖的「投机采样」「PagedAttention·KV Cache」机制不在此重复，本文只谈它们作为**省钱杠杆**怎么用。

---

## 一、成本优化技术对比表（点到为止）

| 技术 | 机制（一句话） | 节省点 | 适用场景 |
|---|---|---|---|
| **Prompt Caching（厂商侧前缀缓存）** | 把稳定前缀的 KV 计算结果存服务器，重复调用只付零头 | input 缓存命中按 ~10% 计费（约 90% off），且跳过重算降延迟 | 长 system prompt、工具定义、长文档/RAG、多轮对话（前缀稳定） |
| **Prefix Sharing / KV Cache 复用（引擎侧）** | 跨请求复用相同前缀的 KV 张量，共享前缀"只算一次" | 多请求同前缀免重复 prefill；命中率越高越省 | 自托管高并发、多 agent 共享同一长上下文、tree-of-thought 分支 |
| **Batching（请求合并）** | 非实时请求攒批 / token 级连续批处理，摊薄固定开销、拉高 GPU 利用率 | Batch API 约 50% off；自托管连续批处理提升吞吐数倍 | 离线标注、批量摘要、eval、embedding 回填（非亚秒级 SLA） |
| **模型路由 Model Routing** | 简单任务走小/便宜模型，难题才上大模型（甚至级联回退） | 60–80% 请求走便宜模型 → 平均降本 40–85%（口径见尾） | 分类/抽取/简单 QA 走 SLM，规划/复杂推理才上前沿模型 |
| **上下文裁剪 Context Trimming** | 压缩/摘要历史、截断旧消息、保留比例截断，控制上下文长度 | 直接砍 input token 数与 KV 占用，避免无限膨胀 | 超长多轮 Agent、Realtime/流式会话、显存紧张端侧 |

> 五者大多可叠加：缓存省重复前缀、路由省"杀鸡用牛刀"、裁剪省"越长越贵"、批处理省异步请求、prefix sharing 在引擎层把前三者做实。

---

## 二、主流方案 / 厂商表（数字标「待核实」）

| 厂商 / 方案 | 缓存 / 路由策略 | 关键参数（联网核实，部分待核实） |
|---|---|---|
| **Anthropic Prompt Caching** | 显式 `cache_control` 断点；标准 5min TTL，2025 起新增 **extended 1h TTL**（额外费用，官方称相对 5min 是 12× 提升） | 缓存 read ≈ 0.10× base、write ≈ 1.25× base（Claude Sonnet 4.6 口径，第三方综述）；官方自报最长前缀 **最高 90% 降本 / 85% 降延迟**（上限值，非均值）｜⚠️ 待核实 |
| **OpenAI Prompt Caching** | 默认**自动**；GPT-5.6+ 改显式 cache breakpoint + `prompt_cache_key`；24h retention 在 GPT-5.5 等系列为默认 | 缓存命中 input 约 **10% of base（≈90% off）**；最小 1024 token；按前缀哈希路由到同机提命中｜官方文档口径，价格随档期变动 ⚠️ 待核实 |
| **vLLM Batching / Prefix Cache** | Continuous Batching（迭代级调度，V1 默认）+ PagedAttention + Chunked Prefill + Automatic Prefix Caching | 相比朴素 PyTorch 循环可达 **3–5×**（高并发 up to 24×，arXiv 2025）；`--max-num-seqs` / `--max-num-batched-tokens` 调吞吐｜基准数字 ⚠️ 待核实 |
| **SGLang RadixAttention** | 基数树做 token 级前缀匹配，多 agent 扇出/分支复用强 | prefix-heavy agentic 负载默认开；与 vLLM APC 互为替代｜命中率缺一手基准 ⚠️ 待核实 |
| **推理网关路由**（LiteLLM / Portkey / OpenRouter / Vercel AI Gateway / Azure AI Foundry Model Router / Cloudflare AI Gateway） | 网关层统一路由 + 语义缓存 + 预算/成本追踪 + failover | 路由策略：规则 / 意图分类 / 复杂度 / 级联 / 延迟 / 合规；成本降 **40–85%** 多为厂商/案例口径 ⚠️ 待核实 |

---

## 三、2025–2026 进展（联网核实）

- **缓存成标配**：Anthropic（自动+显式双模式、extended 1h TTL）、OpenAI（自动→GPT-5.6+ 显式）、Google Gemini、AWS Bedrock、Azure OpenAI 均已上线前缀缓存，折扣梯度 50%–90% off 不一。
- **Prefix Sharing 进引擎默认**：vLLM v1 Automatic Prefix Caching、SGLang RadixAttention 默认开；层级缓存（GPU→CPU→disk）把热 KV 留住。
- **模型路由从研究变基础设施**：RouteLLM（Berkeley/LMSYS，ICLR 2025，MT Bench 上 85% 降本 @ 95% GPT-4 质量，但为该基准特定口径）、vLLM Semantic Router（2026-01，Rust/Golang + Candle BERT，K8s/Envoy 部署）、Martian / NotDiamond 商用 router。
- **Agent 专用成本网关兴起**：LiteLLM / Portkey / OpenRouter / Vercel AI Gateway（2025-08 GA，零加价、40+ 厂商、cost/ttft/tps 排序）把"路由 + 语义缓存 + per-feature 成本归因 + 预算"合一，切换模型成配置而非重构。
- **可观测与成本归因合一**：LangSmith / Langfuse / Helicone / Phoenix / Portkey / OpenLLMetry（OTel/OpenInference）均支持 per-user、per-feature、per-model 成本归因与预算告警——直接呼应 [[Agent 可观测性 LLM Observability 学习笔记]]。

---

## 四、代表工具 / 框架（按层）

| 层 | 代表 | 与成本优化的关系 |
|---|---|---|
| 云厂商 cache 政策 | Anthropic / OpenAI / Gemini / Bedrock / Azure | 前缀缓存折扣梯度与 TTL 策略各异，是"零代码改动"的第一杠杆 |
| 自托管推理引擎 | vLLM / SGLang / TensorRT-LLM / llama.cpp | 按 GPU·小时计费，prefix sharing 提升"每 GPU 服务请求数" |
| 语义缓存中间件 | GPTCache / Helicone 内置 / Redis+向量 | "意思相同"的请求直接返缓存，免新模型调用 |
| 网关 / 路由器 | LiteLLM / Portkey / OpenRouter / Vercel AI Gateway / Azure AI Foundry Model Router | 一层统一路由 + 缓存 + 成本追踪 + failover |
| 成本可观测 | LangSmith / Langfuse / Helicone / Phoenix / OpenLLMetry | 把"哪条链路在烧钱"变成可度量、可告警 |

---

## 五、与辐射锚点的咬合

- **多智能体协作与编排**：orchestrator-worker / supervisor 模式里，N 个子 agent 共享同一份长 system prompt 与项目上下文，重复计算会爆炸；prefix sharing + 统一前缀缓存是必须，否则多 agent 扇出直接放大账单（见 [[多智能体协作与编排 学习笔记]]）。
- **Agent 可观测性**：没有成本归因就谈不上优化——per-route、per-feature、per-model 的 token/$ 追踪与预算告警，是把"降本不降质"从口号变成可验证指标的前提（见 [[Agent 可观测性 LLM Observability 学习笔记]]）。

---

## 待解问题（深度盲区，留白给 Ethon）

- [ ] 多 Agent 共享 KV cache 的**跨会话**可行性？同一前缀在租户/会话间能否复用，安全隔离边界在哪（KV 与输入 token 存在唯一对应关系，跨用户共享有泄漏/投毒风险，NDSS 2025）？
- [ ] 端侧 Agent 成本优化手段？端侧没有 token 账单，等价货币是 **NPU 利用率 / 内存 / 电池 / 散热**，如何用 prefix sharing + SLM 路由 + KV 量化翻译这套思路？
- [ ] 上下文裁剪的"该砍哪段"策略？摘要式压缩 vs 保留比例截断（如 OpenAI Realtime `retention_ratio`）在长链路 Agent 里对质量/缓存命中的权衡？
- [ ] 模型路由的 router 自身成本/延迟何时"为省钱反而更贵"（小模型路由 + 多次回退）？级联（先小后大）的置信度阈值怎么定？
- [ ] 语义缓存的"相似误命中"在 Agent 多步链路里如何设安全边界，避免答非所问被缓存放大？

---

## 附：来源清单

| 来源 | 主题 | 获取方式 |
|---|---|---|
| Anthropic「Prompt caching」官方文档 +「agent-capabilities-api」新闻（2025） | extended 1h TTL、缓存折扣与延迟上限 | WebFetch 官方 |
| OpenAI「Prompt caching」开发者文档 + Prompt Caching 201 cookbook（2025-2026） | 自动/显式缓存、prompt_cache_key、24h retention、Realtime retention_ratio | WebFetch 官方 |
| vLLM / SGLang / LLM Serving Architecture 资料（hld.handbook、aiengineeringfromscratch、cloudai.pt，2025-2026） | Continuous Batching、PagedAttention、Chunked Prefill、RadixAttention、吞吐基准 | WebSearch |
| zylos.ai / digitalapplied / lushbinary / akshayghalme「LLM Routing & Gateway 2026」 | RouteLLM、vLLM Semantic Router、LiteLLM/Portkey/OpenRouter/Vercel、降本区间 | WebSearch |
| therouter.ai / respan.ai「Prompt Caching 2025-2026 对比」 | OpenAI/Anthropic/DashScope 缓存折扣与路由参数 | WebSearch |
| HalfSugar「大模型 API 缓存机制深度解析」（2026-07） | DeepSeek V4 Flash 98% 折扣、FlashMemory、DSA——**单篇中文博客，数字⚠️ 待核实** | WebSearch |
| integritystudio / zenml / comet「LLM Observability 2025」 | LangSmith/Langfuse/Helicone/Portkey/OpenLLMetry 成本归因 | WebSearch |

---

## ⚠️ 待核实清单

- **各家缓存折扣口径**：Anthropic/OpenAI 官方称缓存命中 ≈ 10% of base（≈90% off）；Gemini 各源在 10%–25% 间不一致；DeepSeek V4 Flash 98% 折扣来自单篇博客，未交叉验证，本文未采用为确定值。
- **Anthropic「90% 降本 / 85% 降延迟」**：官方自报"最长前缀"上限值，非平均；实际取决于前缀长度、TTL 命中与流量形态。extended 1h TTL 的"12× vs 5min"亦为厂商口径。
- **模型路由 40–85% 降本**：多为厂商/案例口径；RouteLLM 85% 仅限 MT Bench（GPT-4 Turbo vs Mixtral 8x7B），非通用均值，需自有 eval 验证。
- **vLLM 3–5× / 24× 吞吐**：来自 arXiv 2025 与厂商基准，依赖并发/模型/硬件，非普适。
- **TGI 维护模式 / SGLang 替代**：Hugging Face TGI 2026-03 转只读（据 hld.handbook），以官方公告为准。
- **价格随档期变动**：所有 $/MTok 数字会随厂商调价变化，落地前以各官网 pricing 页复核。

---

#标签/推理优化 #标签/Agent成本 #标签/LLM
