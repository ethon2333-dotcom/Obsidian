---
title: "ANN 索引算法专题（HNSW / IVF-PQ / DiskANN）"
tags: [广度种子, ANN, 向量检索, RAG, AI-Agent框架, 知识拓展Loop]
created: 2026-09-12
source: 见文末来源清单
---

# ANN 索引算法专题（HNSW / IVF-PQ / DiskANN）

> 一句话心智模型：向量检索的快慢与内存，本质由"用哪种近似索引 + 怎么压缩向量"决定，选错算法亿级数据直接崩。

## 广度覆盖
### 定义
暴力检索（Flat / 线性扫描）复杂度为 O(N·D)，当 N 上亿、维度 D 上千时对延迟完全不可接受。ANN（Approximate Nearest Neighbor）用"近似换速度"：牺牲少量召回率换取亚线性查询复杂度与更低内存。核心权衡是 **召回率@k ↔ 延迟 ↔ 内存三者取二**——这是所有选型的根，没有算法能在这三项外加建库速度、动态更新、成本上全面第一。

### 分类 / 主流算法
| 算法 | 核心思想 | 查询复杂度 | 内存 | 适用规模 |
| --- | --- | --- | --- | --- |
| Flat | 线性 / 暴力精确扫描（精确 baseline，非近似） | O(N·D) | 全量原向量（最高） | <100K，或必须完美召回 |
| HNSW | 多层级小世界图，粗→细 zoom-in，支持增量增删 | ~O(log N) | 高（图结构 + 原向量，随连接度 M 线性增长） | 千万 ~ 2 亿，需实时增删 |
| IVF-PQ | k-means 聚类分桶 + Product Quantization 压缩 | O(nprobe·D/PQ) | 低（压缩码） | 十亿级，内存受限 |
| IVF-HNSW | 倒排桶内各挂 HNSW 子图（倒排+图混合） | 子图查询 | 中高 | 十亿级 + 高召回 |
| DiskANN / Vamana | SSD 友好的 Vamana 图，最小化随机读，盘为主存 | ~O(log N)，I/O 绑定 | 极低（盘存） | 数十亿 ~ 千亿，内存放不下 |
| ScaNN | 分区 + 各向异性量化（anisotropic）+ SIMD 打分 | 子空间扫描 | 低 ~ 中 | 十亿级，GPU / 吞吐优先 |
| LSH | 相似向量高概率落入同桶，只查本桶 | 桶内扫描 | 较低 | 中等，理论保证强但召回难追 |

### 量化压缩（PQ / SQ）
- **PQ（Product Quantization）**：向量切 M 段，各段独立聚类成码本，原向量 → M 个码（如 M=8、每码 8bit → 压到 8 字节）。内存从 N·D·4B 降到 N·M 字节，距离在压缩空间算。FAISS 经典方案。
- **SQ（Scalar Quantization）**：逐维标量量化（float32→int8 等），压缩比 ~4x、结构简单无损，常用于 HNSW / Glass。
- **RaBitQ**：FAISS v1.14（2026）引入的二进制量化新路径，比 PQ 更省内存。
- **趋势**：量化已成为 2025-2026 的"入场券"——VIBE 基准显示所有 top 算法都依赖量化，图 vs 聚类之争收敛为"压缩策略之争"。代价：高维（>768d，尤其 1536d Transformer embedding）下 PQ 召回**非线性崩溃**，需 rescoring / refinement 补救。

### 2025-2026 进展
- **量化优先共识**：2025-2026 起，图 vs 聚类之争退居次位，压缩策略成为核心工程问题。
- **2025 NeurIPS / OSDI**：SOAR（ScaNN 各向异性残差 spill）在 Big-ANN 流式 / 分布外赛道 SOTA；Quake（OSDI 2025）自动重分区，动态负载下查询延迟降 1.5–13x、更新延迟降 18–126x（论文测试场景，非普适）。
- **2025**：CAGRA（NVIDIA RAFT）GPU 图索引，小批量单查询强，吞吐相较 CPU HNSW 高约 190x；RAFT 成为 Milvus / Redis / FAISS 的 GPU 加速底座。
- **2026-01**：Google Vertex AI Vector Search 2.0 上线 ScaNN 引擎，十亿级 sub-10ms。
- **2026-03**：DiskANN v0.49.1 全量 Rust 重写（C++ 分支弃维护），64GB RAM 跑 10 亿向量、95% recall@1 < 5ms；千机管理 500 亿点。
- **2026 新方法**：PipeANN（SSD 图，延迟约 DiskANN 35%）、SymphonyQG（RaBitQ+图，VIBE 12 数据集夺 5 冠）、Glass（Zilliz，HNSW+NSG+SQ，夺 4 冠）等涌现。
- **可训练 / 自适应索引 + 混合检索**（dense+sparse，如 Qdrant ACORN、Milvus 2.5 混合）成为生产标配。

### 选型指南
- **小规模（<100K）或须完美召回** → Flat 暴力。
- **千万 ~ 2 亿、需实时增删、低延迟** → HNSW（注意内存墙，约 1–2 亿到顶）。
- **十亿级、内存受限、可接受周期重建** → IVF-PQ（FAISS / Milvus）。
- **十亿 ~ 千亿、内存放不下、SSD 为主** → DiskANN。
- **GPU 充足、批量大吞吐优先** → CAGRA / RAFT（IVF-PQ / IVF-Flat）。
- **极低延迟 + 理论保证、规模中等** → LSH（主流已被 HNSW 取代）。
- **高吞吐推荐 / 广告、成本敏感** → ScaNN 系。

## 与其他笔记的连接
- [[向量数据库 学习笔记]]（产品生态 vs 本文算法内核）
- [[RAG 详细学习笔记]]

## 深度留白（待 Ethon 补充）
- [ ] HNSW 的 M / efConstruction / efSearch 如何按数据调参，召回-延迟曲线实测
- [ ] IVF-PQ 的 nprobe、PQ M、码本训练对高维（1536d）召回崩溃的边界在哪
- [ ] DiskANN 单机的 SSD I/O 模型与延迟构成（随机读 vs 缓存命中）
- [ ] 混合检索中 ANN 索引与稀疏 / BM25 的融合与重排接口
- [ ] RaBitQ / 可训练索引在自己 embedding 分布上的 benchmark 验证

## 附：来源清单
- Superteams.ai — ANN Search 术语综述（算法家族对比）
- BestAIWeb — "ScaNN, DiskANN, and Glass: The 2026 ANN-Benchmarks Race"（VIBE / SymphonyQG / Glass / DiskANN Rust 重写）
- BestAIWeb — "Memory Blowup, Recall Collapse..."（HNSW vs IVF-PQ 召回差、PQ 高维崩溃、FAISS v1.14.1）
- NVIDIA Developer Blog — RAFT / cuVS / CAGRA / IVF-Flat GPU 基准
- 公开报道（2026-07 算法全景：PipeANN / SOAR / Quake / CAGRA 等）
- Researcher.life / IJSEKE 2026 — "ANNS on Milvus"（六算法 1.6M 实测：ScaNN·IVF-SQ8 吞吐最高、HNSW 召回最佳、DiskANN 稳定省内存）

## ⚠️ 待核实清单
- ⚠️ DiskANN "64GB RAM 跑 10 亿向量、95% recall@1 < 5ms" 与 "千机 500 亿点" 为厂商 / 综述口径，未独立复现，待查实。
- ⚠️ CAGRA "比 CPU HNSW 快 190x、QPS 72950" 来自 NVIDIA 演讲 PPT 与 RAFT 基准，依赖 H100 等硬件与数据集，移植自有机型需重测。
- ⚠️ HNSW 实际规模上限（1–2 亿）各源口径不一，依维度与内存实例浮动，非硬上限。
- ⚠️ Vertex AI Vector Search 2.0 "sub-10ms / 99% 精度" 为 Google Cloud 官方口径，未第三方背书。
- ⚠️ FAISS 当前版本号（v1.14.x, March 2026）以 PyPI / GitHub 发布为准，待核实最新。

#标签/向量检索 #标签/ANN #标签/RAG #标签/AI-Agent框架 #标签/知识拓展Loop
