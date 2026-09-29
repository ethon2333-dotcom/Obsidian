---
title: 服务端 LLM 推理引擎生态 学习笔记
tags: [AI工程, 推理引擎, LLMServing, 服务端推理, GPU推理]
created: 2026-09-17
source: "WebSearch/WebFetch 联网核实"
---

## 一句话心智模型

> LLM 推理引擎 = 把"已经训练好的模型权重"在 GPU/服务器上**又快又省地变成 token 流**的运行系统；它关心的是 KV Cache、调度、批处理与内核，而不是"模型怎么训练"或"请求从哪个 API 进来"。

## 本文与相邻笔记的关系

- 本文聚焦**服务端/云端推理引擎本身**（模型如何在数据中心 GPU 上被高效执行）。
- 与 [[端侧推理框架生态 学习笔记]] 的关系：那边讲**移动端 / on-device 运行时**（手机 NPU、GGUF 量化、功耗散热），本文讲**数据中心高吞吐服务**，二者是"端 vs 云"的镜像。
- 与 [[模型服务化与 LLM 网关 学习笔记]] 的关系：那边讲**统一 API / 路由 / 限流 / 多模型抽象层**（请求进来的那一层），本文讲**网关之下真正跑模型的引擎**；网关把请求派发给本文的引擎。
- 与 [[端侧大模型推理 学习笔记]] 的关系：那边讲**端侧推理的原理与约束**，本文讲**服务端规模化 serving**的原理与生态，互补不重叠。
- 关联：[[LLM 跨学科发散]]（建立"LLM 是什么"的全景）｜ [[Agent 推理成本优化 学习笔记]]（推理引擎选型直接影响 agent 每步成本）。

---

## 1. 定义：什么是 LLM 推理引擎 / 服务运行时

**LLM 推理引擎（inference engine / serving runtime）**：把训练好的模型权重加载到加速器（主要是 NVIDIA/AMD/昇腾 GPU，也包括 CPU、TPU），接收 prompt、调度计算、管理 KV Cache、流式输出 token 的服务端软件。核心职责是**最大化吞吐、压低延迟与单位 token 成本**。

**与邻近概念的边界**（避免混淆）：

| 概念 | 关注点 | 代表 | 与"推理引擎"的区别 |
|---|---|---|---|
| 推理引擎 / serving runtime | 模型怎么在硬件上跑得快又省 | vLLM、SGLang、TensorRT-LLM | 本文主角，处于栈的最底层执行层 |
| 端侧推理框架 | 模型在手机/PC 本地 on-device 跑 | llama.cpp、Ollama、MLC LLM | 硬件是端侧 NPU/CPU，约束是功耗/内存，见 [[端侧推理框架生态 学习笔记]] |
| LLM 网关 / 模型服务化 | 统一 API、路由、限流、多模型抽象 | LiteLLM、APISIX AI Gateway | 在引擎"上面"一层，不直接执行模型，见 [[模型服务化与 LLM 网关 学习笔记]] |
| 训练框架 | 怎么训练模型 | PyTorch、Megatron | 目标是梯度/吞吐，不是在线 serving |

> 生产请求的真实流向：**应用 → 网关(路由/限流) → 推理引擎(vLLM等) → GPU(prefill+decode)**。本文只覆盖最后两层。

---

## 2. 分类与主流方案（广度速览）

按"定位"大致分三层（注意 Ollama/llama.cpp 既可本地也可跑服务端轻量场景，但生产高并发不在其列）：

| 引擎 | 出处 / 团队 | 定位 | 核心招牌技术 | 硬件 | 备注 |
|---|---|---|---|---|---|
| **vLLM** | UC Berkeley / LMSYS | 生产高吞吐**事实标准** | PagedAttention、Continuous Batching、V1 统一调度器 | NVIDIA/AMD/Intel/CPU | 社区最活跃，OpenAI 兼容 API |
| **SGLang** | UC Berkeley / LMSYS | 生产级 + 结构化/Agent/RAG | RadixAttention（前缀 KV 复用）、零开销 CPU 调度、xGrammar 约束解码 | NVIDIA/AMD | 共享前缀 workload 强（多轮/RAG/Agent） |
| **TensorRT-LLM** | NVIDIA | 极致单模型峰值性能 | 编译期 kernel 融合、FP8/FP4、in-flight batching | 仅 NVIDIA | 需 AOT 编译（约 10–30 分钟/模型，媒体口径**待核实**），换模型成本高 |
| **HuggingFace TGI** | HuggingFace | HF 生态集成 | 生产级默认值、可观测 | NVIDIA/AMD | **2025-12-11 进入 maintenance mode**，官方建议新项目转 vLLM/SGLang |
| **LMDeploy** | 上海人工智能实验室 / InternLM | 高并发、量化延迟 | TurboMind(C++)、blocked KV、dynamic split-and-fuse | 仅 NVIDIA | 中文社区强，Western 生态较小 |
| **llama.cpp** | ggml-org（Georgi Gerganov） | 端/边/CPU、极致可移植 | 纯 C/C++、GGUF 量化(1.5–8bit)、llama-server | 几乎任意硬件 | 基金会级可移植，单节点，非高并发取向 |
| **Ollama** | Ollama | 本地开发/原型体验 | 封装 llama.cpp + 模型管理 + 后台服务 | 含 Apple MLX(2026 新增) | 生产并发上限低（媒体口径约 50 并发后趋平，**待核实**） |
| **DeepSpeed-Inference** | Microsoft | 超大模型、显存卸载 | ZeRO-Inference、CPU/NVMe offload | NVIDIA | 擅长"跑得下"而非低延迟 |
| **OpenLLM** | BentoML | 把模型快速做成服务 | 内嵌于 BentoML 服务化栈 | 多后端 | 细节**待核实**（本次未单独深挖） |

**大致选型直觉**（广度层面，非精确基准）：
- 通用生产、要并发 → vLLM
- 多轮/RAG/Agent/结构化输出 → SGLang（RadixAttention 复用共享前缀）
- 单模型长期跑、NVIDIA、要榨干峰值 → TensorRT-LLM
- 量化低延迟（如 INT4） → LMDeploy
- 本地/CPU/边缘/原型 → llama.cpp / Ollama

> ⚠️ 所有"tok/s、倍数、市占率"类数字均来自厂商博客或媒体实测，**硬件/模型/上下文不同差异巨大，本文一律标记为待核实**，切勿当通用 SOTA。

---

## 3. 关键优化技术（点到为止）

这些技术**可叠加、效果常是乘法而非加法**：

| 技术 | 解决什么 | 一句话原理 | 代表实现 |
|---|---|---|---|
| **Continuous Batching** | GPU 空闲 | 请求完成即插入新请求，不等整批结束 | vLLM/SGLang/TGI 默认；llama.cpp 新版也支持 |
| **PagedAttention** | KV Cache 显存碎片 | 像操作系统虚拟内存一样把 KV 分页、按需分配、可共享/写时复制 | vLLM（vLLM 原创） |
| **Prefix Caching / RadixAttention** | 重复前缀重复计算 | 共享 system prompt / 文档 / 历史的 KV 只算一次 | vLLM APC、SGLang Radix Tree |
| **Speculative Decoding** | decode 串行瓶颈 | 小 draft 模型先猜多 token，大模型一次并行验证 | EAGLE-3、Medusa、MTP、NGram（TensorRT-LLM/SGLang/vLLM 均已支持） |
| **Chunked Prefill** | 长 prompt 阻塞 decode | 把 prefill 切块，与 decode 交错，避免一个长请求卡住全局 | vLLM/SGLang |
| **Attention backends** | attention 内核效率 | IO-aware 精确注意力，不物化完整注意力矩阵 | FlashAttention-3（Hopper/Blackwell+FP8）、FlashInfer（serving 内核引擎，已被多框架集成） |
| **Quantization 集成** | 显存/带宽 | 权重/激活/KV Cache 低比特（FP8/INT4/AWQ/GPTQ/GGUF） | 各引擎原生集成；KV Cache 量化（KIVI/TurboQuant 等）是 2025-26 热点 |
| **Disaggregated Prefill/Decode** | 两阶段互相干扰 | prefill（计算密集）与 decode（带宽密集）分到不同 GPU 池 | NVIDIA Dynamo、DistServe/Mooncake 思路，vLLM/TensorRT-LLM 均有相关能力 |

> 进阶但本次未展开：KV Cache offloading（跨 GPU/CPU/SSD）、Mooncake 的 KV-centric 架构、FlashInfer 的可组合 attention 模板、多 token 并行 draft（DFlash 等）。留作待解问题。

---

## 4. 2025-2026 进展（竞争态势与关系）

**竞争态势**
- **双雄格局收敛**：vLLM 与 SGLang 成为新部署默认路径；TGI 2025-12 进入维护模式，HF 官方不再推新特性。
- **vLLM V1 架构落地**：统一调度器（2025-03 起默认），2026 年移除旧 V0 引擎，代码库收敛；社区活跃度极高（媒体口径单次发版 200+ 贡献者，**待核实**）。
- **"KV Cache 成为一等资源"**：从内存副产品升级为可复用、可路由、可卸载的资产——这是 2025-26 最清晰的系统级主线。
- **prefill/decode 解耦**成为规模化 serving 共识，NVIDIA Dynamo（GTC 2025 开源，Triton 的继任定位）把"KV 感知路由 + GPU 动态再分配 + KV offload(NIXL)"做成分布式框架，并**兼容 vLLM/SGLang/TensorRT-LLM/PyTorch**。
- **内核层成为差异化壁垒**：FlashAttention-3、FlashInfer 决定框架下限，框架竞争下沉到内核与调度。

**与 Agent / 长上下文 / 多模态的关系**
- **Agent**：每步工具调用都是一次请求，且共享 system prompt / 工具定义 → 前缀复用（RadixAttention）与低延迟 decode 直接决定 agent 成本；推理成本优化见 [[Agent 推理成本优化 学习笔记]]。
- **长上下文**：KV Cache 随长度线性膨胀，瓶颈从算力转向显存/带宽 → 推动 prefix caching、KV 量化、offloading、disaggregated serving。
- **多模态 / 推理型模型（reasoning）**：VLM 流式输出、test-time compute 产生超长输出（每 prompt 上万思考 token，媒体口径**待核实**）→ 进一步放大 decode 与 KV 成本，是 Dynamo 等"AI 工厂"框架的主战场。

---

## 5. 代表产品 / 厂商布局（广度）

| 厂商 / 项目 | 布局 | 定位 |
|---|---|---|
| NVIDIA | TensorRT-LLM + Dynamo + Triton + NIM 微服务 | 从单 GPU 内核到数千 GPU 分布式 serving 全栈 |
| LMSYS（UC Berkeley） | vLLM + SGLang | 开源 serving 双引擎事实标准 |
| HuggingFace | TGI（维护中）→ 推荐 vLLM/SGLang | 生态入口、迁移引导 |
| 上海 AI Lab / InternLM | LMDeploy（TurboMind） | 国产高并发、量化低延迟 |
| 云厂（AWS/Azure/GCP/OCI/CoreWeave 等） | 托管 vLLM/SGLang/Dynamo 兼容部署 | 把开源引擎做成托管服务 |
| BentoML | OpenLLM | 服务化封装 |
| 端侧延伸 | llama.cpp/Ollama（MLX 后端 2026） | 本地/开发侧，与云端引擎互补 |

---

## 待解问题（留白给 Ethon）

- [ ] vLLM 各版本号（0.11 / 0.20 / 0.26 等）时间线混乱，需以 GitHub release 为准核对真实版本与日期
- [ ] SGLang RadixAttention 与 vLLM APC 在"命中率/开销"上的真实边界：到底哪些 workload 该用哪个？
- [ ] TensorRT-LLM 的 AOT 编译耗时、换模型成本在 2026 年是否下降（媒体称仍 10–30 分钟）
- [ ] NVIDIA Dynamo 与 vLLM/SGLang 的"集成"是替换还是编排层？生产里怎么共存？
- [ ] 国产硬件（昇腾/寒武/海光）上各引擎的真实支持度与性能落差
- [ ] KV Cache 量化（KIVI/TurboQuant/QServe W4A8KV4）在长上下文下的精度损失实测
- [ ] FlashInfer 作为"内核引擎"是否正在成为框架的隐藏底座？vLLM/SGLang 各自内核策略差异
- [ ] OpenLLM 当前定位与活跃度（本次未深挖）

---

## 附：来源清单

本次实际访问 / 检索到的来源（检索日 2026-09-17）：

1. NVIDIA 技术博客 — Introducing NVIDIA Dynamo（GTC 2025 开源、disaggregated serving、NIXL）：`developer.nvidia.com/blog/introducing-nvidia-dynamo-...`
2. NVIDIA Newsroom — Dynamo 开源发布稿（30x 吞吐、兼容 vLLM/SGLang/TensorRT-LLM/PyTorch）：`nvidianews.nvidia.com/news/nvidia-dynamo-open-source-library-...`
3. NVIDIA 中文博客 — Dynamo v0.2（Planner / K8s Operator / AWS EFA）：`developer.nvidia.cn/blog/nvidia-dynamo-adds-gpu-autoscaling-...`
4. SGLang 官方文档 — `docs.sglang.io/`（RadixAttention、多硬件、LMSYS 托管）
5. Prem AI 博客 — LLM Inference Servers Compared 2026（vLLM/SGLang/TGI/Triton，TGI 维护模式）：`blog.premai.io/llm-inference-servers-compared-vllm-vs-tgi-vs-sglang-vs-triton-2026/`
6. S-Samarth 笔记 — Serving Frameworks（SGLang vs vLLM、TGI 维护模式、TensorRT-LLM 定位）：`s-samarth.github.io/DataSciencePreparation/LLM/serving/sglang-and-alternatives`
7. Deploybase — LLM Serving Framework Comparison（吞吐/延迟/成本基准，媒体口径）：`deploybase.ai/articles/llm-serving-framework-comparison`
8. TensorFoundry — vLLM/SGLang/llama.cpp/Ollama 对比：`tensorfoundry.io/blog/llm-inference-servers-compared`
9. AwesomeAgents — Best Open-Source LLM Inference Servers 2026（TGI 维护模式、LMDeploy、Ollama 并发上限）：`awesomeagents.ai/tools/best-open-source-llm-inference-servers-2026`
10. DeepResearch.ninja — Open-Source LLM Inference Projects 2026（LMDeploy/llama.cpp/Ollama/MLC/TinyGrad 分层）：`deepresearch.ninja/2026/06/Open-Source-LLM-Inference-Projects-...`
11. MorphLLM — LLM Inference Optimization 2026（量化/连续批/投机解码/上下文压缩，含 TurboQuant）：`morphllm.com/llm-inference-optimization`
12. DataCamp — How LLM Inference Works（FlashAttention/FlashInfer、KV 优化、speculative decoding 变种）：`datacamp.com/tutorial/how-llm-inference-works`
13. AI Wiki — Continuous Batching 词条（vLLM V1 时间线、版本号）：`aiwiki.ai/wiki/continuous_batching`
14. 知乎/CSDN 类中文综述（vLLM 版本演进、SGLang 特性）若干 — 作为媒体口径交叉参考，**数字均待核实**

---

## ⚠️ 待核实清单

- vLLM 具体版本号与时间线（0.11.0 / 0.20.0 / 0.26.0 等说法来自不同媒体，需以 GitHub release 为准）
- SGLang 版本号（v0.5.8 Jan 2026 等媒体口径）
- 所有"tok/s、X 倍加速、X% 显存利用率、45% 市占率"类数字（来源为厂商博客/媒体实测，硬件模型不同差异极大）
- TensorRT-LLM 编译耗时（10–30 分钟/模型）、较 vLLM 的优势幅度（5–15% / 30–50% 各源不一）
- LMDeploy 与 SGLang 在 Llama 8B 上的 ~16,100 tok/s 对比数字
- Ollama 在 50 并发后趋平、vLLM 920 tok/s 等对比数字
- "每 prompt 推理模型生成上万思考 token"、"API 价格 2025→2026 降约 80%" 等趋势性数字
- DeepSpeed-Inference 与 OpenLLM 的当前活跃度与最新特性（本次未深挖）
- NVIDIA Dynamo 在真实生产中的部署形态（与 vLLM/SGLang 是编排还是替换）

---

#标签/AI工程 #推理引擎 #LLMServing #服务端推理
