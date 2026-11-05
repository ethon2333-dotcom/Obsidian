---
title: 多模态 RAG 产品实测
tags: [RAG, 多模态RAG, ColPali, ColQwen2, 实测, 文档检索, 知识库]
created: 2026-10-07
source: ColPali 论文(arXiv 2407.01449, ICLR 2025) / ViDoRe benchmark / Qdrant·Vespa 技术博客 / SmolVLM 论文(arXiv 2504.05299) / 公开实测博客（详见「来源清单」，厂商/媒体口径数字均标「待核实」）
---

# 多模态 RAG 产品实测

> [!abstract] 心智模型
> 多模态 RAG 实测的本质一句话：**把 PDF 页面当「图」直接编码成上千个 patch 向量、用 late-interaction（MaxSim）做细粒度匹配，换来图表/表格类召回的显著增益，代价是存储 30–50×、延迟更高、且对域偏移与对抗投毒更敏感**——它不是一个开箱即用的替换，而是文本 RAG 之外的「视觉召回通道」。

> 本文刻意区别于库内已立题的三篇：[[多模态 RAG 与文档问答产品 学习笔记]]（产品形态广度）、[[知识库问答与 Enterprise Search 学习笔记]]（企业级 RAG）、[[多模态文档智能 DocAI 学习笔记]]（解析引擎）。本文只聚焦 **empirical 实测维度**：recall 实测、延迟/吞吐、存储开销、与文本 RAG 的成本/精度对照、真实部署教训。纵深原理见 [[RAG 详细学习笔记]]（向量检索/重排/评估），多向量存储底座见 [[向量数据库 学习笔记]]，端侧可行性见 [[端侧多模态 VLM 学习笔记]]。

---

## 一、广度覆盖总表（BREADTH > DEPTH）

| 维度 | 定义 | 分类 | 主流方案 | 2025-2026 进展 | 代表产品 / 研究 / 工具 |
|---|---|---|---|---|---|
| **核心范式：视觉文档检索（page-as-image late interaction）** | 跳过 OCR/版面解析，把渲染后的页面图像直接喂 VLM，产 patch 级多向量，检索时用 MaxSim 做 query-token × patch 细粒度匹配 | ① 视觉 late-interaction 检索（ColPali 系）② 文本 late-interaction（ColBERT 系）③ CLIP/双塔多模态检索 ④ 视觉重排（hybrid） | ColPali / ColQwen2 / ColQwen2.5 / ColSmol / ColNomic；ColBERT-v2 / Jina-ColBERT-v2 | ColPali 论文(arXiv 2407.01449) 录用 ICLR 2025；2026 主流默认 backbone 已迁到 Qwen2.5-VL（ColQwen2.5≈89 nDCG@5 on ViDoRe V1），ColQwen3 / ColNomic 跟进；`colpali-engine` 2026-08 被官方标记 deprecated，转向 Sentence Transformers 6.0 `MultiVectorEncoder` | HuggingFace `vidore/*` 系列；Illuin Tech（ColVision 家族）；Sentence Transformers |
| **基准评测：ViDoRe** | 视觉富文档检索基准（slides / 财报 / 论文 / 表格 / 图表），主指标 nDCG@5 / nDCG@10 | V1（已饱和，~90 nDCG@5）／ V2（2025-05，多语、更难）／ V3（2026，企业域多维、nDCG@10） | ViDoRe V1/V2/V3；MTEB 重算通道（vidore-benchmark 已停更，2025-02 后转 mteb） | V3 把榜单拉回「复杂真实场景」（多语扫描、混合模态查询、表格密集报备）；同一模型跨 V1/V2/V3 数字**不可直接比趋势**，必须带 harness 版本 | HuggingFace `vidore` leaderboard；MTEB embeddings-benchmark/results |
| **索引/存储代价** | 每页 ~1030 个 128 维 patch 向量（ColPali 论文 D=128），不压缩时约 257.5 KB/页 | 原始多向量 ／ token pooling 压缩 ／ 二值量化(BQ) ／ PLAID 聚类 | 行/列 pooling、hierarchical pooling、binary quantization | pooling（factor 3）减 66.7% 向量、保 97.8% 性能（论文）；BQ 可将存储再压 32×、MaxSim 提速 4× | Qdrant（row pooling 1030→38 向量）、Vespa（hamming + BQ）、ColBERT-v2/PLAID |
| **延迟与吞吐优化** | 原生 MaxSim 在百万页级是 O(页×patch×query-token) 的昂贵运算 | 两阶段检索（pooled 粗召→原分辨率重排）／ query-token 剪枝 ／ 量化 prefetch | Qdrant 13×、Vespa 15.1× 等加速方案 | Qdrant 两阶段 13×、NDCG@20=0.952；Vespa BQ 两阶段 15.1×、median 156ms（均 ViDoRe V3，**厂商基准，待核实**） | Qdrant、Vespa、Milvus、AstraDB、BentoML（均原生/一等 ColPali 集成） |
| **对照：与文本 / OCR RAG** | 在图表/表格/扫描件上视觉检索更强，但在纯文本密、域偏移大时可能不如 OCR+文本管线 | ① 纯文本 bi-encoder ② OCR+文本嵌入 ③ 视觉 late-interaction ④ 混合（BM25+向量+ColPali 重排） | hybrid 三路 + RRF 是 2026 主流栈 | 域偏移实测翻车：DocDeg 噪声/未见文档上 ColPali 系 MRR 0.247 vs OCR 管线 0.485；但同一论文 DocVQA 子集 ColQwen2 NDCG@5 0.603 vs OCR 0.337 → **强烈依赖域适配** | RAG 重排器（BGE-reranker v2 / Cohere Rerank 3 / Jina Reranker v2） |
| **部署形态与工具链** | 把视觉检索做成「并行索引 + 路由」而非替换 | 独立视觉索引 ／ 文本召回 + ColPali 重排 ／ 端到端多模态 Agent | Azure AKS + Qdrant + ColQwen3；Vespa 十亿级；自托管 vs 厂商托管 | 生产化趋于成熟：Vespa 声称可扩到十亿 PDF；微软开源 AKS+Qdrant ColQwen3 加速器；Mubadala PULSAR 据称 ~240 万页（**vendor-reported，待核实**） | Microsoft `multi-modal-rag-with-colpali`；Vespa；Qdrant；OpenSearch（视觉 RAG 基准，**媒体口径，待核实**） |
| **端侧 / 轻量化多模态 RAG** | 用 256M–500M 小 VLM 把视觉检索压到端/边设备 | ColSmol(256M/500M) ／ SmolVLM 派生 ／ 区域级对齐小模型 | ColSmolVLM、IndoColSmol、Smol Docling | SmolVLM-256M 在 MacBook Pro M4 Max 经 WebGPU 达 ~80 decode tok/s；IndoColSmol-256M/500M Recall@5 0.887/0.890（IEEE，低资源语料） | HuggingFace ColSmol 系列；SmolVLM（arXiv 2504.05299）；端侧落地意义见 [[端侧多模态 VLM 学习笔记]] |

---

## 二、实测要点（点到为止）

### 2.1 Recall 实测：增益真实，但高度依赖域
- **增益来源**：late-interaction 在 token/patch 粒度匹配，避免把整页压成单一向量造成的信息损失；图表/表格/扫描件上相对 OCR+文本基线普遍领先（ViDoRe V1 上 ColQwen2 ≈89 vs 文本基线 ~76–85 nDCG@5，差异量级 **厂商/媒体口径，待核实**）。
- **翻车边界（重要）**：独立论文（Most et al., 2025-05-08）在 **DocDeg 噪声/未见文档** 上测得 ColPali 系 MRR 0.247 / Recall@5 0.355 / NDCG@5 0.274，**低于** OCR+Llama-3.2+OCR 文本嵌入管线（MRR 0.485 / Recall@5 0.636 / NDCG@5 0.523）。同论文在 DocVQA 子集又反过来 ColQwen2 胜出。**结论：视觉检索的胜负值由域偏移、视觉质量、是否对目标分布微调决定，不能一概而论。**

### 2.2 存储开销（page-as-image 的真实代价）
- 论文口径：~1030 个 128 维 patch 向量/页 → **257.5 KB/页（未压缩，论文 subsec B.3）**。
- 量级对照（媒体/厂商口径，**待核实**）：10K 页约 1.3 GB float32 vs 文本索引 ~50 MB；或「约 8× / 30–50×」说法并存——数字取决于维度/压缩，务必带口径。
- 压缩杠杆：token pooling（factor 3 → 减 66.7% 向量、保 97.8%）、二值量化（再省 32×）。**多向量存储需要支持 MaxSim 的向量库**，见 [[向量数据库 学习笔记]]。

### 2.3 延迟 / 吞吐
- 原生：100K 页未优化 MaxSim 约 200–500ms（媒体口径，**待核实**）。
- 优化后：Qdrant 两阶段 row pooling（1030→38 向量）提速 **13×**、NDCG@20=0.952（**厂商基准，待核实**）；Vespa BQ+两阶段 **15.1×**、median 156ms（**厂商基准，待核实**）。
- 工程共识：**两阶段检索（粗召 Top-200 → 原分辨率重排 Top-20）是生产标配**，把 query 成本压到可控。

### 2.4 与文本 RAG 的精度/成本对照（决策用）
| 场景 | 视觉 late-interaction 优势 | 文本/OCR RAG 优势 |
|---|---|---|
| 图表/表格/扫描件密集（论文、财报、设备手册） | 强，免去 OCR/版面解析失败 | 易漏行、错列 |
| 纯文本密、域偏移大、未见文档 | 易翻车（见 2.1） | OCR+文本嵌入更稳 |
| 存储/延迟预算紧 | 劣势（30–50× 存储、GPU 推理） | 优势 |
| 最佳实践 | **并行索引 + 路由**：文本召回 Top-50 → ColPali 视觉重排 Top-5；或 RRF 三路融合 | 作为默认低成本的主体召回 |

### 2.5 真实部署教训（来自厂商/开源加速器与实测博客）
- **不要「每页都过 VLM」**：先用文档分类器——文本层 >100 字符的页走标准文本抽取，仅失败页走 VLM，企业语料可减 60–75% VLM 调用（实测博客，**待核实**）。
- **ColPali 不是 drop-in 替换**：它是「额外的视觉召回模态」，最佳形态是与混合文本检索 **并行 + 路由**（低置信文本结果或含空间/视觉词时路由到 ColPali）。
- **域适配成本**：开箱在通用文档好用，但专业域（分子生物、特定格式法律引文、技术图纸）需 500–2000 对精细微调，需 GPU + ML 工程带宽。
- **安全面**：像素投毒——单张对抗截图可污染 ColPali top-10 结果达 **26.4%** 查询（Zhuang et al., 2025-01-28，论文），因直接吃像素，攻击面不同于文本稠密检索。
- **冷启动成本**：重新索引 1 万页 PDF 在单卡 A10 上约 25 小时（媒体口径，**待核实**）——规模上来前先评估增量/池化策略。
- **生态迁移**：`colpali-engine` 2026-08 被官方 deprecated，新项目推荐 Sentence Transformers 6.0 `MultiVectorEncoder`（vidore/* 已补 ST 模块配置）。

### 2.6 端侧 / 轻量化可行性（与 [[端侧多模态 VLM 学习笔记]] 咬合）
- ColSmol（256M/500M）与 SmolVLM 派生把视觉检索压到端/边：SmolVLM-256M 在 M4 Max 经 WebGPU ~80 decode tok/s；IndoColSmol 在低资源语料 Recall@5 0.887–0.890。
- **结论（点到为止）**：小模型端侧「能跑视觉检索」，但召回质量与 backbone 规模强相关，端侧只适合低资源/离线/隐私红线场景，不适合高 stakes 精确召回主力。

---

## 三、深度盲区（留给 Ethon 补充）

- [ ] **待解问题**：在 Ethon 自己的 Android 产品文档/手册语料上，ColQwen2.5 vs OCR+文本 RAG 的 Top-5 命中对照实测（请跑 ViDoRe 风格内部集）。
- [ ] **待解问题**：10 万页量级下，Qdrant 两阶段 pooling 与 Vespa BQ 两阶段在「真实中文财报/研报」上的延迟-召回帕累托曲线（现有数字多为英文 ViDoRe，需中文复核）。
- [ ] **待解问题**：端侧 ColSmol 在手机 NPU 上的实际吞吐与量化后召回衰减（论文只到 M4 Max WebGPU，缺安卓端实测）。
- [ ] **待解问题**：像素投毒对「带截图的工单/手册 RAG」的具体可利用性与防御（colpali-engine 是否提供 patch 级异常检测）。
- [ ] **待解问题**：混合栈里 router（小 LLM/分类器）误路由到 ColPali 时的成本放大倍数，是否需要预算护栏（见 [[Agent 推理成本优化 学习笔记]]）。
- [ ] **待解问题**：ViDoRe V3 的「企业域 nDCG@10」与 V1 数字如何在汇报中避免被误读为「模型进步」而非「基准变难」。

---

## 附：来源清单

1. Faysse et al., **ColPali: Efficient Document Retrieval with Vision Language Models**, arXiv 2407.01449（ICLR 2025）—— 范式、257.5 KB/页、token pooling 数据。
2. **ViDoRe Benchmark** —— HuggingFace `vidore` org；V1/V2/V3 演进与 MTEB 重算口径。
3. Qdrant, *Optimizing ColPali for Retrieval at Scale, 13x Faster*（qdrant.tech/blog）—— 两阶段 row pooling 加速。
4. Vespa, *Scaling ColPali to billions of PDFs*（blog.vespa.ai）—— hamming + binary quantization 32×/15.1×。
5. Marafioti et al., **SmolVLM: Redefining small and efficient multimodal models**, arXiv 2504.05299 —— 端侧吞吐、ColSmolVLM、WebGPU。
6. Most et al. (2025-05-08), DocDeg 域偏移实测（emergentmind.com 综述转引）—— ColPali vs OCR 管线对照。
7. Zhuang et al. (2025-01-28), 像素投毒攻击（emergentmind.com 综述转引）—— 26.4% top-10 污染。
8. Microsoft, `multi-modal-rag-with-colpali`（GitHub）—— AKS + Qdrant + ColQwen3 生产加速器。
9. 公开实测博客（towardsdev / callsphere / bigdataboutique / tensoria / 今日头条 OpenSearch 基准）—— 提供「15+ NDCG 点」「8× 存储」「1683ms 延迟」「25h 重索引」等数字，**厂商/媒体口径，见待核实清单**。
10. IndoColSmol (IEEE ICoDSA 2025) —— 256M/500M 低资源语料 Recall@5。

## ⚠️ 待核实清单

- ⚠️ OpenSearch 视觉 RAG 基准（2026-04-21，经今日头条转引）：Top-5 命中 76%→91%、NDCG@10 0.77 vs 0.42、查询延迟 1683ms（P95 1969ms）、存储约 8×——**媒体/厂商口径，未独立复核**。
- ⚠️ 「ColPali 比文本基线高 15+ NDCG 点」「30–50× 存储」「每页 1024 向量」等跨博客数字——**口径不一，需带维度/压缩条件**。
- ⚠️ Qdrant 13×、Vespa 15.1× / 156ms median——**厂商自有基准**，方法可复现但数字未在独立集复核。
- ⚠️ Mubadala PULSAR ~240 万页、3000+ deals 实战规模——**vendor-reported**，非公开 benchmark。
- ⚠️ 单卡 A10 重索引 1 万页 ~25 小时、企业语料减 60–75% VLM 调用——**实测博客口径**，缺原文链接。
- ⚠️ `colpali-engine` deprecated 与 Sentence Transformers 6.0 `MultiVectorEncoder` 时间线（2026-08）——**以 PyPI/GitHub 官方公告为准**，本文依搜索时点整理。

#标签/AI Agent框架/多模态RAG/RAG实测
