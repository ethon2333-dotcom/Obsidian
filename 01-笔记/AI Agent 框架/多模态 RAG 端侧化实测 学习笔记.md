---
title: 多模态 RAG 端侧化实测
tags: [多模态RAG, 端侧推理, 端侧RAG, ColPali, 视觉文档检索, 模型量化, 本地RAG, 隐私]
created: 2026-10-08
source: WebSearch/WebFetch 核实（ColPali arXiv 2407.01449·ICLR 2025 / ColQwen2 HF docs & Hub / SmolVLM arXiv 2504.05299 / Berlin Buzzwords 2025「Quantized ColPali」/ ICDCS 2025「Edge-First LM Inference」/ gufacode ColPali 教程 ch6/ch10 / MiniCPM-V 系列公开博客 2025-2026 / byaldi·AnswerDotAI）。厂商/媒体口径数字均标「待核实」，未编造。
---

# 多模态 RAG 端侧化实测

> [!abstract] 心智模型
> 多模态 RAG 端侧化的本质一句话：**把「页面当图、用 VLM patch 向量做 late-interaction 检索」这条原本吃 GPU 的链路，压到手机/笔记本本地跑——靠的是小 VLM 骨干 + 视觉编码器量化 + 多向量存储压缩三件套，换来的收益是「数据不出设备」的隐私与零网络延迟，代价是召回精度与 backbone 规模强相关、只适合离线/低资源/隐私红线场景，不能当高 stakes 精确检索主力。**

> 本文刻意区别于库内已立题的两篇相近笔记：[[多模态 RAG 产品实测 学习笔记]]（云端产品 empirical 实测视角）与 [[多模态 RAG 与文档问答产品 学习笔记]]（产品形态广度）、[[多模态文档智能 DocAI 学习笔记]]（解析引擎）。本文只聚焦 **端侧/边缘可行性（on-device feasibility）**：在手机/笔记本本地跑视觉-语言文档检索的延迟/显存/精度权衡、视觉编码器量化、本地文档 RAG 的隐私收益、与云端 ColPali 的对照。纵深原理见 [[RAG 详细学习笔记]]，多向量存储底座见 [[向量数据库 学习笔记]]，端侧 VLM 选型见 [[端侧多模态 VLM 学习笔记]]，量化工程见 [[端侧模型量化 学习笔记]]，本地知识库落地见 [[个人知识库 AI 化与本地 RAG 学习笔记]]。

---

## 一、广度覆盖总表（BREADTH > DEPTH）

| 维度 | 定义 | 分类 | 主流方案 / 代表产品 | 2025-2026 进展 | 代表产品 / 研究 / 工具 |
|---|---|---|---|---|---|
| **核心范式：视觉文档检索 page-as-image late interaction** | 跳过 OCR/版面解析，整页渲染图直接喂 VLM，产 ~1030 个 patch 多向量，检索时用 MaxSim 做 query-token × patch 细粒度匹配 | ① 视觉 late-interaction 检索（ColPali 系）② 文本 late-interaction（ColBERT 系）③ CLIP/双塔多模态检索 ④ 端侧轻量替代（小 VLM 编码） | ColPali / ColQwen2 / ColQwen2.5 / ColQwen3 / ColSmol；MiniCPM-V / SmolVLM / MobileVLM 作「读页」或「编码」替身 | ColPali(arXiv 2407.01449) 录用 ICLR 2025；2026 默认 backbone 迁到 Qwen2.5-VL（ColQwen2.5≈89 nDCG@5 on ViDoRe V1，**厂商/媒体口径，待核实**）；`colpali-engine` 2026-08 deprecated，转 Sentence Transformers 6.0 `MultiVectorEncoder` | HuggingFace `vidore/*` 系列；Illuin Tech；AnswerDotAI `byaldi`（本地 RAG 库，~10 行跑通） |
| **端侧可行性分级（按 backbone 规模）** | 能否在消费级设备（手机/笔记本/边缘 NPU）跑通「编码 + 检索」全链 | ① 云端大模型（ColQwen3/2.5，需 GPU）② 笔记本级小 VLM（ColSmol 256M/500M、SmolVLM）③ 手机 NPU 级（MiniCPM-V 4.6 1.3B、MiniCPM-o）④ 纯端侧量化 ColPali（int4，笔记本离线搜） | ColSmolVLM、IndoColSmol、SmolVLM-256M；MiniCPM-V 2.6/4.5/4.6；MiniCPM-o 2.6/4.5；量化 ColPali（Berlin Buzzwords 2025 发布消费级本地版） | 2025-2026 端侧多模态门槛快速下探：MiniCPM-V 4.6（2026-05，1.3B）宣称 6G 内存可跑；量化 ColPali 把整模型压到笔记本本地搜；SmolVLM-256M 在 M4 Max WebGPU ~80 decode tok/s | HuggingFace ColSmol 系列；OpenBMB MiniCPM；量化 ColPali（consumer build）；byaldi + Ollama/llama.cpp |
| **视觉编码器量化（端侧关键瓶颈）** | VLM 里 SigLIP/ViT 视觉编码器占显存与算力大头，量化它决定能否塞进端侧 | ① 权重量化（int8 / int4-NF4 / bitsandbytes）② 视觉 token 压缩（切片编码 + 浅层压缩）③ 混合 token 压缩（4×/16× 可调）④ 二值/标量量化（向量层） | ColPali/ColQwen2 int4（bitsandbytes NF4，双量化）；MiniCPM-V 4.6 用 LLaVA-UHD v4 重构 ViT，图像编码开销 -50%、高分辨率 FLOPs -55.8%、4×/16× token 压缩 | 量化 ColPali（int4）已可在笔记本离线搜（Berlin Buzzwords 2025 talk）；MiniCPM-V 4.6（2026-05）把 ViT 编码成本砍半、支持「性能优先/速度优先」切换 | bitsandbytes；llama.cpp（GGUF）；Ollama；QNN（骁龙 NPU）；Apple Neural Engine |
| **多向量存储压缩（让端侧装得下）** | 每页 ~1030 个 128 维 patch 向量、未压缩约 257.5 KB/页，端侧必须压 | ① token pooling（factor 3）② 二值量化 BQ（~4 KB/页）③ Matryoshka 降维（128→64→32）④ 两段式（BQ 粗筛 + bfloat16 精排） | Qdrant row pooling（1030→38 向量）、Vespa hamming+BQ；Matryoshka multi-vector（ColPali 取前 32 维粗筛） | 生产「最优配方」：BQ 4 KB 粗筛 + 按需拉全精度精排 → 每页 4 KB、nDCG@5 0.820、延迟比原生快 ~6×、存储约 1/128（gufacode 教程，**教程口径，待核实**）；百万页约 500GB→压到 ~4GB 量级 | Qdrant、Vespa、Milvus、AstraDB、byaldi（本地轻量） |
| **端侧 RAG 隐私收益** | 文档与 query 全程不出设备，无云端 API 往返、无 prompt 留存/训练风险 | ① 完全离线（本地索引 + 本地生成）② 端侧检索 + 端侧 VLM 读页 ③ 联邦/边缘集群（数据不动模型动） | ColPali + LLaVA 全离线闭环（ZOOZ 工程 PoC）；byaldi 本地索引；MiniCPM-o iPad 端跑 | ICDCS 2025「Edge-First LM Inference」系统论证：端侧在成本/延迟/可靠性/隐私四维优于云端，但容量受限时需云 fallback；隐私是端侧 RAG 首要卖点（prompt 不落日志、数据本地化） | llama.cpp / Ollama 本地栈；MiniCPM 系列 iOS/Android/HarmonyOS 端 app |
| **与云端 ColPali 的对照** | 端侧 vs 云端在精度/成本/延迟/隐私上的帕累托取舍 | ① 云端高精度主力（ColQwen2.5/3）② 端侧低资源离线（ColSmol/小 VLM）③ 混合（云检索 + 端读 / 端预筛 + 云精排） | 云端 ColQwen2.5/3（GPU 集群）；端侧 ColSmol/量化 ColPali/MiniCPM-V | 共识（2025-2026）：端侧只适合离线/隐私红线/低资源，不适合高 stakes 精确召回主力；域偏移下小模型翻车风险更高（见 [[多模态 RAG 产品实测 学习笔记]] 2.1 域偏移实测） | 对照结论见「二、权衡 frontier」；深读 [[多模态 RAG 产品实测 学习笔记]] |

---

## 二、权衡 frontier（点到为止）

### 2.1 显存/延迟/精度三角（端侧实测视角）
- **骨干越小 → 显存/首响越低，但召回越弱**：ColPali 系骨干 3B（PaliGemma），int4 量化后约 1.7 GB 级权重（按 1B≈0.5GB @int4 推算，**待核实**）；ColSmol 256M/500M 可塞进端/边；MiniCPM-V 4.6（1.3B）宣称 6G 内存流畅跑、3136² 大图首响 ~75.7ms（厂商口径，**待核实**）。
- **MobileVLM（2024，v2 约 1.4B/3B）** 是早期端侧 VLM 代表，主打手机端视觉对话；作为「端侧读页」替身理论可行，但**视觉文档检索召回数字缺公开实测，本文不引用具体数字**（**待核实**）。
- **关键瓶颈是视觉编码器而非语言模型**：SigLIP/ViT 的 patch 编码占大头，量化 + token 压缩（MiniCPM-V 4.6 的 LLaVA-UHD v4：-50% 编码开销、-55.8% FLOPs）比压语言模型更划算。

### 2.2 量化后的精度衰减（必须带着口径看）
- 通用 LLM 量化经验（CSDN 实测，Qwen2-7B）：int8 掉分 ≈ -1.2% MMLU、int4 ≈ -2.7%，数学/代码敏感任务掉分可达 ~4.5%——**这是文本 LM 数据，视觉检索的量化掉分需另测，不能直接套**（**待核实迁移**）。
- 多向量层量化更成熟：BQ 把存储压 32×、MaxSim 提速 4×；token pooling 保 97.8% 性能（[[多模态 RAG 产品实测 学习笔记]] 已列论文数据）。**端侧落地的存储压缩链路已相对可靠，瓶颈在编码模型本身的大小。**

### 2.3 端侧 RAG 的隐私收益（真实且可量化的是「架构收益」）
- **可断言**：本地闭环（本地索引 + 本地 VLM 生成，如 ColPali+LLaVA、byaldi+Ollama）使文档与 query 不出设备，规避云端 prompt 留存/训练与网络往返延迟——这是架构级收益，非营销。
- **不可断言**：具体「延迟降低多少 ms、隐私合规省多少成本」取决于部署，无统一数字，厂商口径需标待核实。

### 2.4 与云端 ColPali 的决策边界
| 场景 | 端侧（ColSmol/量化 ColPali/小 VLM） | 云端（ColQwen2.5/3 + GPU） |
|---|---|---|
| 离线/无网/数据合规红线 | 首选，零外发 | 不可用 |
| 高 stakes 精确召回（财报/法律引文） | 易翻车，需微调且容量有限 | 主力 |
| 个人私密文档库（本地 RAG） | 天然契合，见 [[个人知识库 AI 化与本地 RAG 学习笔记]] | 过度暴露 |
| 百万页以上规模 | 存储/算力吃紧，需强压缩+分段 | 标配（Vespa 称可十亿级） |
| 最佳实践 | **混合**：端侧预筛/离线索引 + 云端精排兜底；或纯端侧仅作隐私通道 | 作为高精度主体召回 |

---

## 三、深度盲区（留给 Ethon 补充）

- [ ] **待解问题**：在你自己的 Android 产品手册/工单截图语料上，量化 ColPali（int4）vs ColSmol-256M vs OCR+文本 RAG 的 Top-5 命中与端侧首响延迟实测（手机 NPU 实测，非 M4 Max）。
- [ ] **待解问题**：视觉编码器（SigLIP）单独 int8 量化、语言模型保持 bf16 的「混合精度」方案，对 ViDoRe 风格中文文档召回的掉分有多大——这是端侧显存最划算的杠杆，缺公开数据。
- [ ] **待解问题**：端侧多向量索引（BQ/token pooling）在 1–10 万页本地库的 P99 检索延迟与内存峰值（byaldi + 本地 ANN，无云端 Vespa/Qdrant 时的真实曲线）。
- [ ] **待解问题**：MobileVLM / MiniCPM-V 4.6 作「端侧读页生成」替身时，对表格/扫描件的答案准确率相对云端 ColQwen3+GPT 级读页差多少——缺少同语料对照。
- [ ] **待解问题**：端侧 RAG 在「隐私合规」维度的可审计性——本地闭环如何向合规方证明「数据未外发」，有无端侧推理轨迹留痕方案（与 [[Agent 可观测性 LLM Observability 学习笔记]] 的端侧监控意义咬合）。
- [ ] **待解问题**：混合架构里端侧预筛误判、把本该云精排的页留下来的「召回天花板」损失，是否需要端侧小 reranker 兜底（参考 [[端侧推理的动态路由与模型选择 学习笔记]]）。

---

## 附：来源清单

1. Faysse et al., **ColPali: Efficient Document Retrieval with Vision Language Models**, arXiv 2407.01449（ICLR 2025）—— 范式、PaliGemma-3B 骨干、~1030 patch/页、257.5 KB/页。
2. HuggingFace `transformers` ColQwen2 model doc + `vidore/colqwen2-v1.0` Hub —— 架构、动态分辨率、int4（bitsandbytes NF4）量化示例、ColQwen2.5 兼容 checkpoint。
3. Marafioti et al., **SmolVLM: Redefining small and efficient multimodal models**, arXiv 2504.05299 —— 端侧小 VLM、SmolVLM-256M M4 Max WebGPU ~80 tok/s、ColSmolVLM。
4. **Berlin Buzzwords 2025**, 「Text Search on Images with Quantized ColPali」—— 量化 ColPali 消费级本地搜、late-interaction、本地部署。
5. ICDCS 2025, **Edge-First Language Model Inference: Models, Metrics, and Tradeoffs**（arXiv 2505.16508）—— 端侧 LM 在成本/延迟/可靠性/隐私四维优于云端、容量受限需云 fallback。
6. gufacode ColPali 教程 ch6（生产规模化 1/128）/ ch10（生态与端侧 ColSmolVLM + MLX/llama.cpp 离线搜）—— token pooling、BQ、Matryoshka、两段式配方、本地 Mac/iPhone 离线搜。
7. OpenBMB MiniCPM-V / MiniCPM-o 系列公开博客与 Nature Communications 报道（2025-2026）—— MiniCPM-V 2.6/4.5/4.6、MiniCPM-o 2.6/4.5 端侧延迟/内存/OpenCompass 数字（**厂商/媒体口径，待核实**）。
8. AnswerDotAI `byaldi` —— 本地 ColPali RAG 库，~10 行索引本地 PDF。
9. ZOOZ Engineering, *Reimagining Multimodal Retrieval with ColPali*（含 LLaVA 全离线生成 PoC）—— 本地生成 + ColPali 检索的隐私-respecting 闭环。
10. codesota / emergentmind（Matryoshka multi-vector retrieval）—— 多向量降维、PQ/BQ、端侧内存受限部署。

## ⚠️ 待核实清单

- ⚠️ MiniCPM-V 4.6「6G 内存、3136² 首响 75.7ms、7013 tok/s、54.79 张/秒」与 MiniCPM-o 4.5「OpenCompass 77.6 超 GPT-4o」——**厂商发布/媒体转引口径，未独立复核**。
- ⚠️ 量化 ColPali（int4）「笔记本离线搜」的具体显存占用与召回掉分——**Berlin Buzzwords 2025 talk 描述，缺公开 benchmark 数字**。
- ⚠️ 生产「最优配方」每页 4 KB、nDCG@5 0.820、比原生快 ~6×、存储 1/128——**gufacode 教程口径，非独立论文**。
- ⚠️ 通用 LLM int4 掉分 -2.7%、数学/代码 ~4.5%——**文本 LM（Qwen2-7B）实测，迁移到视觉检索量化需另测**。
- ⚠️ ColPali int4 权重「约 1.7 GB」由 1B≈0.5GB @int4 推算——**粗略估算，待 HF Model Memory Calculator 实算**。
- ⚠️ MobileVLM 端侧视觉文档检索召回数字——**公开资料缺专门实测，本文未引用具体值**。
- ⚠️ `colpali-engine` 2026-08 deprecated 与 Sentence Transformers 6.0 `MultiVectorEncoder` 时间线——**以 PyPI/GitHub 官方公告为准**。

#标签/多模态RAG/端侧推理/端侧RAG
