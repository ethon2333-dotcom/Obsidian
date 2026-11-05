---
title: 跨模态统一表示与多模态 embeddings 学习笔记
tags: [multimodal, embedding, representation, cross-modal, 广度种子, AI模型基础]
created: 2026-10-29
source: [WebSearch: glukhov.org cross-modal embeddings, zilliz.com ai-faq, mixpeek.com best multimodal embedding models 2026, arxiv.org/abs/2502.14786 (SigLIP 2), modelscope.cn gme-Qwen2-VL, backblaze-labs awesome-multimodal-data]
---

# 跨模态统一表示与多模态 embeddings 学习笔记

**心智模型：把文本 / 图像 / 音频 / 视频编码进同一个向量空间，让"以文搜图、以图搜文、跨模态检索、零样本分类"成为可能——距离即相似，模态即通道。**

> 本篇聚焦「表示学习 / embedding 模型 / 跨模态对齐」本身，刻意区别于库内 [[多模态评测基准 学习笔记]]（怎么量这些模型）、[[多模态文档智能 DocAI 学习笔记]]（embedding 在文档 RAG 中的下游用法）、[[世界模型与仿真合成环境 学习笔记]]（合成数据/仿真作为训练上游）以及跨模态检索结构笔记（检索架构）。本篇只讲"空间怎么炼出来"。

## 一、定义与动机

| 维度 | 要点 |
| --- | --- |
| 定义 | 跨模态 embedding = 将不同模态（text/image/audio/video/depth/thermal/IMU…）映射到**共享向量空间**的稠密表示；同语义不同模态在空间中聚拢 |
| 核心度量 | 余弦相似度 / 欧氏距离做跨模态匹配；通常以 dual-encoder（各模态独立编码器）+ 对比损失训练 |
| 动机 | 传统单模态模型无法跨空间比较；统一空间解锁以文搜图、以图搜文、以音频搜视频、零样本分类、embedding 算术（image + "sunset"） |
| 对比范式 | 对比学习（CLIP/SigLIP/ImageBind）最主流；另有生成式对齐（BLIP-2 Q-Former）、共享编码器、cross-attention 拼接等 |

## 二、主流范式分类

| 范式 | 代表 | 机制 | 备注 |
| --- | --- | --- | --- |
| 对比学习（双编码器） | CLIP、SigLIP / SigLIP 2、ImageBind | InfoNCE / Sigmoid 对比损失，正对拉近、负对推远 | 工业落地最主流，检索友好 |
| 生成式桥接 | BLIP-2（Q-Former） | 可学习 query token 桥接冻结视觉编码器与 LLM | 偏生成/理解，非纯检索 embedding |
| 统一多模态对齐 vs 拼接 | UniCL、EVA-CLIP | 对齐=同空间映射；拼接=多特征 concat（非同一空间，检索需各自索引） | 对齐才能原生跨模态检索 |
| Hub 模态绑定 | ImageBind | 以图像为"绑定"模态，无需全模态两两配对即可涌现跨模态对齐 | 6 模态：text/image/audio/depth/thermal/IMU |

## 三、代表模型与方案

| 模型 / 方案 | 机构 | 模态 | 规模/维度 | 一句话定位 |
| --- | --- | --- | --- | --- |
| CLIP | OpenAI | 文+图 | 400M 图文对，ViT-B/L，512-d | 奠基者，零样本分类范式开创 |
| SigLIP 2 | Google DeepMind | 文+图（多语） | ViT-B(86M)/L(303M)/So400m(400M)/g(1B)；NaFlex 变体 | 2025-02 发布，Sigmoid 损失+多语+稠密特征+定位，零样本/检索全面超 SigLIP/CLIP |
| ImageBind | Meta | 6 模态 | 1024-d | 图像绑定六模态，开源 |
| OpenCLIP / EVA-CLIP | LAION / 社区 | 文+图 | 多尺度 | 开源复现+增强（masked image modeling） |
| BGE-M3 | BAAI（智源） | 文本为主（100+ 语） | 568M / 1024-d | 多粒度（稠密+稀疏+ColBERT 一模型），中文开源标杆 |
| Jina CLIP v2 / Embeddings v4 | Jina AI | 文+图（+PDF/图文档） | ~1B / 3.8B | 多语、Matryoshka、图文档检索 |
| Nomic Embed（Vision/Text） | Nomic | 文+图 | 768-d Matryoshka | ColBERT 式多向量，开源 |
| Cohere Embed v3/v4 | Cohere | 文本→v4 文+图+表 | 1024/1536-d | 原生二进制压缩省存储，企业 API |
| Voyage Multimodal 3 / 3.5 | Voyage AI（MongoDB） | 文+图（+视频） | 1024-d | 图文档/截图检索特化，API |
| GME-Qwen2-VL | 阿里 Tongyi | 文+图+图文对 | 2B/7B | 2025，VLM 改造的统一 embedding，Any2Any 检索 SOTA |
| Amazon Nova Multimodal | AWS | 文+图+视频+音频+文档 | 5 模态 | 单托管模型覆盖最广（待核实） |

## 四、2025-2026 进展（广度扫描）

| 方向 | 进展 | 代表 |
| --- | --- | --- |
| 统一多模态嵌入 | 单模型覆盖 3-5 模态成为趋势，从"文图对齐"走向"Any2Any 检索" | GME-Qwen2-VL、Amazon Nova、Google Multimodal |
| 长文本 + 多模态 | 文本侧上下文拉长（32K-128K），图像侧动态分辨率/NaFlex 保宽高比 | Gemini Embedding 2、SigLIP 2 NaFlex、GME 动态分辨率 |
| 检索优化 | Matryoshka（可变维度）、二进制/int8 压缩、ColBERT 式 late interaction 多向量 | Cohere v4、Jina、Nomic |
| 开源可审计 | 训练数据/代码/权重全开放，自托管替代闭源 API | OpenCLIP、SigLIP 2、BGE-M3、GME |
| VLM 即 embedder | 用 VLM（Qwen2-VL 等）直接当单向量 embedder，免 OCR-then-embed | GME、TwelveLabs Marengo 3.0 |

## 五、代表产品与开源库

| 类别 | 名称 | 用途 |
| --- | --- | --- |
| 模型框架 | transformers（HF） | 加载 CLIP/SigLIP/ImageBind 等预训练权重，统一推理 API |
| Embedding 框架 | sentence-transformers | 文本/图/音/视频 bi-encoder 嵌入、训练、10k+ 模型 Hub，跨模态检索标配 |
| 开源复现 | OpenCLIP | CLIP 开源复现，含 SigLIP/EVA-CLIP 变体 checkpoint |
| 向量库 | FAISS / ChromaDB / pgvector / Milvus | ANN 相似度检索；FAISS IVF-PQ 量化支撑百万级低延迟 |
| 托管 API | Vertex AI Multimodal / Cohere / Voyage / OpenAI | 企业级统一 embedding 服务，免自托管 |

## 待解问题（深度盲区，留给 Ethon 补）

- [ ] 统一空间里"模态 gap"是否真的被抹平？音频/深度等弱模态对齐质量如何量化，是否只是靠图像 hub 间接对齐的"伪统一"？
- [ ] 跨模态检索的评测指标（Recall@K、R@10）在不同榜单差异极大，媒体口径数字（如"+40% recall"）是否可复现、是否过拟合特定分布？
- [ ] 端侧部署可行性：CLIP/SigLIP 可量化上手机，但 GME-7B / VLM-as-embedder 类重量级统一 embedding 在端侧 NPU 上的延迟与精度损失边界在哪？与 [[端侧模型量化 学习笔记]] 如何衔接？
- [ ] 多向量（ColBERT 式）vs 单向量在跨模态场景的精度/存储/延迟权衡，何时该用 late interaction 而非单向量？

## 附：来源清单

- WebSearch 主来源：glukhov.org《Cross-Modal Embeddings: Bridging AI Modalities》
- WebSearch 主来源：zilliz.com/ai-faq《latest multimodal embedding architectures》
- WebSearch 主来源：mixpeek.com《Best Multimodal Embedding Models in 2026》
- WebSearch 主来源：backblaze-labs/awesome-multimodal-data（开源库清单）
- WebFetch 权威来源：arXiv:2502.14786《SigLIP 2: Multilingual Vision-Language Encoders…》（提交 2025-02-20，模型尺寸 ViT-B/L/So400m/g 已核实）
- WebSearch 主来源：modelscope.cn gme-Qwen2-VL-7B-Instruct（GME 模型卡，2025-09 更新）
- 交叉参考：[[多模态评测基准 学习笔记]] · [[多模态文档智能 DocAI 学习笔记]] · [[世界模型与仿真合成环境 学习笔记]]

## ⚠️ 待核实清单

- 「Amazon Nova 是首个覆盖 text/document/image/video/audio 五模态的统一 embedding 模型」——出处为第三方 2025 综述，未查到 AWS 官方单一声明，待核实。
- Mixpeek 榜单称 TwelveLabs Marengo 3.0「自家实测 2.7 而非 3.0」——厂商数字 vs 第三方 benchmark 冲突，待核实。
- 「多模态 embedding 带来 +40% 跨模态 recall 提升」——出自 Ailog 2026 综述，无统一基准佐证，待核实。
- 「Voyage AI 于 2025-02 被 MongoDB 以 2.2 亿美元收购」——单源（CSDN）提及，待核实。
- 各媒体 benchmark 表中具体数值（MTEB Retrieval、Cross-modal Recall@10、维度、价格等）为第三方 2026 快照，随版本变动，选型前以官方/MTEB Leaderboard 最新为准，待核实。
- WMW/CSDN 2026 评测中 Gemini Embedding 2、Jina v4、Qwen3-VL-Embedding 等分数——媒体实测，非官方统一基准，待核实。

#标签/多模态/跨模态表示/embeddings/AI模型基础
