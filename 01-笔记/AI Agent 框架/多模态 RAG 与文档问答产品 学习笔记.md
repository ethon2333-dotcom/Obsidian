---
title: 多模态 RAG 与文档问答产品 学习笔记
tags: [multimodal-rag, document-qa, 视觉文档检索, ColPali, NotebookLM, 文档问答产品, 广度种子]
created: 2026-10-06
source: "WebSearch/WebFetch 核实 + 公开资料（2025-2026）"
---

# 多模态 RAG 与文档问答产品

> 一句话心智模型：把文档当"图"而非"字"来检索——页面渲染图直接被视觉语言模型编码成多向量，跨图文表混合召回，再让 LLM 基于像素级证据作答，于是"文档即知识库"的消费/通用产品形态成为可能。

> [!note] 与库内兄弟笔记的分工
> - 区别于 [[知识库问答与 Enterprise Search 学习笔记]]（企业级 RAG / 权限感知 / 租户隔离广度）。本笔记聚焦**多模态文档 RAG 的技术范式 + 消费/通用文档问答产品生态**。
> - 区别于 [[多模态文档智能 DocAI 学习笔记]]（文档解析技术）。本笔记侧重"RAG + 文档问答产品"而非解析引擎本身。
> - 与 [[RAG 详细学习笔记]]（检索原理）、[[向量数据库 学习笔记]]（向量底座）、[[GraphRAG 与知识图谱增强 Agent 学习笔记]]（图谱增强）、[[端侧多模态 VLM 学习笔记]]（端侧视觉编码器）互补。

## 广度覆盖

| 维度 | 要点（点到为止） |
| --- | --- |
| **定义** | 多模态 RAG（Multimodal RAG）= 在 RAG 管线中把图像/表格/图表/版式等视觉信号当作**一等检索对象**，与文本一起参与 embedding、检索、生成。区别于"先 OCR 抽文本再纯文本 RAG"。 |
| **分类（四类介入点）** | 多模态可进入管线的四个环节：ingestion / embedding / retrieval / generation。实践上三种主流模态：纯文本、位图（扫描/照片/图）、结构化视觉（表格/图表/示意图）。 |
| **主流技术方案（2025-2026）** | ① **Caption-and-index**：VLM 给图写说明→当文本嵌。简单但会丢信息、说明幻觉污染索引。<br>② **Unified embeddings（统一向量）**：Cohere Embed 4（2025-04，128K 上下文、Matryoshka）、voyage-multimodal-3.5（2026-01，加视频帧）、SigLIP 2（2025-02，文本-图像检索更强）、gemini-embedding-2（2026-03，文本+图+视频+音频+PDF 统一空间，3072 维）。单索引、跨模态查询。<br>③ **Page-as-image + late interaction（页面即图像·延迟交互）**：ColPali / ColQwen2 系列——不跑 OCR，整页渲染图编码成上千 patch 向量，用 MaxSim 延迟交互打分。视觉密集文档召回最高。<br>④ **Hybrid late-fusion**：文本 + 图像双索引、BM25 + dense + RRF 融合 + VLM reranker。最灵活、运维最复杂。 |
| **2025-2026 进展** | - ColPali（Faysse et al., ICLR 2025）确立视觉文档检索范式，ViDoRe 基准；**colpali-engine 已被官方标记 deprecated**，转向 Sentence Transformers 6.0.0（2026-08）的 `MultiVectorEncoder`；主线演进到 ColQwen2.5 / ColSmol（小 footprint）。ViDoRe 已迭代到 V3（2026-01，企业域 nDCG@10），V1/V2 归档为 legacy 标签。<br>- 统一多模态 embedding 成主流（Cohere/voyage/Google 三家 2025-2026 密集发布），"单检索空间吞下图文视频音频"成为卖点。<br>- 生产侧 RAG 向**托管服务**收敛：Vertex AI RAG Engine（GA 2025-01-10）、Azure AI Document Intelligence + AI Search、Cloudflare AutoRAG/AI Search、AWS Bedrock Knowledge Bases；Anthropic Contextual Retrieval（per-chunk 上下文预拼）成为默认生产栈。<br>- Azure "Content Understanding" GA（2025-11），把文档智能扩到 text/images/audio/video 统一 API；Azure AI Search 推 Agentic Retrieval、Multimodal Embeddings Skill。 |
| **代表产品（厂商）** | **消费/通用文档问答**：<br>- **ChatPDF**：极简 PDF 聊天、精确页码引用、有 API；免费 2 篇/天。<br>- **NotebookLM（Google）**：多源（PDF/网页/YouTube/音频）grounded 问答、内联引用、Audio/Video Overviews、Gemini 1M token 上下文；免费额度慷慨、无公开 API。<br>- **AskYourPDF**：浏览器扩展 + 多格式（PDF/PPT/EPUB/CSV）、API。<br>- **Humata / PDF.ai / Adobe Acrobat AI Assistant**：技术/法律长文档、扫描件 OCR、Acrobat 内嵌问答。<br>**企业/平台侧**：<br>- **Glean**：企业工作场所搜索，跨多应用按源权限检索，grounded 上下文。<br>- **Azure AI Document Intelligence + AI Search**：v4.0 Layout/Read、Content Understanding、多模态 embedding、Agentic Retrieval，文档解析→RAG 流水线。<br>- **Google Vertex AI RAG Engine**：可编程 RAG 原语，可选向量后端（Vertex Vector Search/Pinecone/Weaviate）+ Gemini/Claude/Llama 生成；配套 gemini-embedding-2 多模态 embedding。<br>**国内（RAG 化文档智能）**：<br>- **达观数据**：KMS 知识中台 + 深度文档解析（自研 OCR/NLP/知识图谱，版面解析 96% 口径）+ RAG/SFT，WAIC 2025 推"企业知识库 + Agent"融合。<br>- **合合信息 TextIn**：文档解析矩阵（目录/表格/公式/印章/跨页表还原），为 LLM 提供结构化语料支撑；企业知识库建设方案。<br>- **阿里云文档智能**：文档智能/IDP 能力 + 百炼/通义 RAG 组合（具体 RAG 化产品形态**待核实**）。 |

## 深度盲区（待 Ethon 补充）

- [ ] ColPali / ColQwen2 系列在**中文密集、双栏、印章遮挡**文档上的真实召回 vs 中文 OCR+RAG 基线的对照数据（厂商多为英文/欧语文档语料）。
- [ ] 统一多模态 embedding（Cohere/voyage/gemini-embedding-2）在**长 PDF 多页**场景的切分/上下文窗口限制与成本曲线。
- [ ] 消费级文档问答产品（NotebookLM/ChatPDF/AskYourPDF）底层是否真的用 page-as-image 多向量检索，还是仍以解析+OCR 文本 RAG 为主（产品口径不透明）。
- [ ] 国内厂商（达观/合合/阿里云）"文档智能 + RAG"是否各自闭源自研检索层，还是基于开源向量库（如 Milvus）拼装——架构差异待核实。
- [ ] 多模态 RAG 的**评测基准**除了 ViDoRe，是否有针对"图文混合问答准确率 / 幻觉率"的权威公开 benchmark。
- [ ] 端侧能否跑 ColPali 级别多向量编码（见 [[端侧多模态 VLM 学习笔记]]），消费产品离线化/隐私化的可行性边界。

## 附：来源清单

- ColPali / ColQwen2 / ViDoRe：Faysse et al. 2024 (arXiv 2407.01449, ICLR 2025)；colpali-engine 弃用公告与 Sentence Transformers 6.0.0 MultiVectorEncoder；ViDoRe V1/V2/V3 基准（via WebSearch 核实，2026-10-06）。
- 多模态 RAG 三类架构对比：bigdataboutique.com "Multimodal RAG in 2026"（Cohere Embed 4 / voyage-multimodal-3.5 / SigLIP 2 口径）。
- 文档问答产品（ChatPDF / NotebookLM / AskYourPDF / Humata / Glean / Adobe）：2026 年横向评测与对比站（ailternative、pdfgpt.io、chitika、needaitool、labibledelia，2026-10-06 检索）。
- Azure AI Document Intelligence：Microsoft Learn "What's new"（v4.0 / Content Understanding GA 2025-11 / Multimodal Embeddings Skill / Agentic Retrieval）。
- Google Vertex AI RAG Engine：aiwiki.ai/google_vertex_ai（GA 2025-01-10、Multimodal RAG）；gemini-embedding-2 发布（2026-03，Divinci blog 转述）。
- 国内厂商：达观数据官网博客与 WAIC 2025 报道；合合信息 TextIn 解决方案报道（2025-11）。

## ⚠️ 待核实清单

- Azure "75% 更快检索"、达观"版面解析 96% vs 行业 71%"、"综合推荐率 65%→95%"等为**厂商自报数字**，未独立复核，不纳入结论。
- 阿里云文档智能的具体 RAG 化产品形态与命名（2026 当前口径）**待核实**。
- NotebookLM / ChatPDF 等消费产品的**技术栈真假**（是否真多向量检索）厂商未公开，**待核实**。
- ViDoRe V1/V2/V3 分数跨版本不可直接比较（benchmark 已 rebaseline），文中未引具体数字，仅描述趋势。
- gemini-embedding-2 的 3072 维、Matryoshka 1,536/768 等规格来自第三方 blog 转述 Google 官方公告，**待以 Google 官方文档为准**。

#标签/多模态RAG #标签/文档问答 #标签/AI检索
