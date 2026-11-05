---
title: 多模态文档智能 DocAI 学习笔记
tags: [AI模型基础, 多模态, DocAI, 文档智能, OCR-free, 文档解析, RAG上游]
created: 2026-10-05
source: WebSearch/WebFetch 2026-10-05（Qwen3-VL / MinerU / Docling / VisRAG 等公开资料）
---

# 多模态文档智能 DocAI 学习笔记

> 心智模型：DocAI 是把「纸/PDF/扫描件」变成机器可读结构化数据（Markdown/JSON/表格）的能力层；**OCR-free 文档 VLM 用一次看图直接吐结构，传统流水线先检测再识别再拼版**——前者赢在语义与版式，后者赢在成本与规模。

> 本文是「广度种子」：只铺面、不挖深。区别于 [[多模态 GUI 理解与 UI Grounding 学习笔记]]（屏幕/控件理解）与 [[端侧多模态 VLM 学习笔记]]（通用视觉理解），本笔记聚焦**文档/版面/表格/扫描件**这一垂直场景。

## 一、定义与边界

- **DocAI（Document AI）**：对 PDF、扫描件、图片、Office 文档做解析、版式理解、表格抽取、KV 抽取、问答，输出结构化结果。
- **核心子任务**：版面检测（layout detection）、阅读顺序（reading order）、表格结构还原、公式识别、OCR 文本、图表理解、文档问答（DocVQA）。
- **与通用 VLM 的区别**：文档场景对**高密度小字、长上下文、精确版式还原、表格 cell 对齐**要求远高于通用视觉问答，是 VLM 的一个垂直高难子集（见 [[大模型四类型：LLM VLM MLLM LMM]] 中 VLM 定义）。
- **与 GUI Grounding 的区别**：GUI 理解的是「屏幕上的可交互控件」，DocAI 理解的是「静态版面里的语义区块」。

## 二、范式分类（三种路线）

| 范式 | 代表 | 思路 | 优点 | 软肋 |
|---|---|---|---|---|
| ① 规则/模板 + 传统 OCR | Tesseract、早期 ABBYY、模板抽取 | 正则/区域框 + OCR 引擎 | 便宜、可解释、确定 | 换版式即崩、无语义 |
| ② 检测 + 识别 pipeline | LayoutLM 系列、Azure Form Recognizer、AWS Textract、百度/合合/达观 | 先 layout detect，再 OCR/字段识别 | 模块可单独优化、可审计 | 误差累积、表格结构脆弱 |
| ③ OCR-free 文档 VLM（端到端） | Donut、Nougat、Qwen-VL、Gemini Document、GPT-4o 文档、InternVL、GOT-OCR2.0 | 看图直接出 JSON/HTML/Markdown | 保版式与语义、少模块 | 重、长文档贵、需大上下文 |

> 生产现实（2026）：多数系统走「②做便宜批量文本 + ③做语义/结构化抽取」混合；纯 ③ 在复杂/长文档仍贵。

## 三、主流方案与玩家（表格为主）

| 类别 | 代表方案 | 要点（公开口径） |
|---|---|---|
| 开源文档 VLM（OCR-free） | **Donut**(NAVER 2022)、**Nougat**(Meta 2023, LaTeX)、**Pix2Struct**(Google 2023)、**GOT-OCR2.0**(2024) | 去显式 OCR，端到端图像→结构化 |
| 通用 Doc VLM（闭源） | GPT-4o/5.x、Gemini 2.5/3.x、Claude Opus、Kimi | 文档图/PDF 直读，Prompt 出 Markdown/CSV/JSON |
| 通用 Doc VLM（开源） | **Qwen2.5-VL / Qwen3-VL**、**InternVL2.5/3**、MiniCPM-V、mPLUG-DocOwl、Llama 4、DeepSeek-VL2 | 动态分辨率(AnyRes)是关键；Qwen 长期领跑开源文档榜 |
| 开源解析工具链 | **MinerU**(OpenDataLab)、**Marker**(EndlessAI)、Dolphin(字节)、**Docling**(IBM)、MarkItDown(微软)、olmOCR、PDF-Extract-Kit | 版面检测+OCR+表格+公式多模型融合，输出 MD/JSON |
| 传统 Layout 模型 | **LayoutLM / LayoutLMv3**(微软)、DocLayNet、TableFormer(IBM) | 检测+识别两阶段，企业表单主力 |
| 企业 DocAI 平台 | Google Document AI、Azure Document Intelligence(Form Recognizer)、AWS Textract、百度智能云/合合/达观 | 托管 API，表单/发票/KV 抽取，合规与权限内置 |
| 多模态检索（VisRAG） | **ColPali / ColQwen2**、VisRAG(ICLR 2025) | 页面图像直接 embedding，跨模态检索，免 OCR 文本化 |

## 四、2025-2026 进展（点到为止）

- **Qwen3-VL**（技术报告 2025-11）：DocVQA ANLS 在 2026-05 达 **97.1%**（235B-A22B，MoE），8B 也到 96.1%；256K 交错上下文，支持推理版 Thinking。
- **Qwen2.5-VL-72B**：DocVQA **96.4%**、ChartQA **89.5%**，仍是自托管默认文档模型（动态分辨率 encoder）。
- **VisRAG（ICLR 2025）**：图像 embedding 检索比传统 TextRAG 端到端高 **20–40%**，保留版式信息。
- **olmOCR-2**（2025-10）：基于 Qwen2.5-VL-7B，高吞吐 PDF→纯文本，保阅读顺序。
- **MinerU 1.3.x（2025）**：移除 layoutlmv3 依赖，6GB 显存可跑，公式解析提速 14 倍+，支持 84 语言、RapidTable/StructTable 表格。
- **Docling + Granite-Docling-258M**：258M 小模型版式/表格/公式接近大模型，适合轻量部署。
- **原生多模态接管**：GPT-4o/Gemini/Claude 均支持 PDF 直读，文档成为 VLM 默认能力而非独立产品（与 [[外挂适配式 vs 原生多模态架构]] 的「原生统一」路线一致）。

## 五、代表产品/玩家速览

| 玩家 | 定位 | 备注 |
|---|---|---|
| 阿里 Qwen | 开源 Doc VLM 标杆 | 连续 18 个月领跑开源文档榜 |
| OpenGVLab InternVL | 开源追赶者 | InternVL3 在多项多模态基准超 Qwen2.5-VL |
| OpenAI / Google / Anthropic | 闭源托管文档理解 | 长上下文 + 多页批处理 |
| IBM Docling | 开源解析+布局 | DocLayNet + TableFormer，37k+ stars，接 LangChain/LlamaIndex |
| 字节 Dolphin / 微软 MarkItDown / EndlessAI Marker | 开源 PDF→MD | 偏结构还原/多格式/易用 |
| Google / Azure / AWS / 百度·合合·达观 | 企业 DocAI 平台 | 表单发票 KV 抽取，权限合规内置 |

## 深度盲区（待解问题）

- [ ] 待解问题：复杂表格（合并单元格、无框线表、跨页表）结构还原的精度上限在哪？
- [ ] 待解问题：低质量扫描件（倾斜、低 DPI、印章遮挡、手写批注）的鲁棒性如何系统提升？
- [ ] 待解问题：长文档（>100 页）多页版式一致性与跨页引用/脚注绑定怎么做？
- [ ] 待解问题：端侧 DocAI 是否可行？（小 VLM + 轻量 layout 模型能否在手机跑，见 [[端侧多模态 VLM 学习笔记]]）
- [ ] 待解问题：OCR-free 与 OCR pipeline 的成本拐点（页数/质量阈值）如何量化决策？
- [ ] 待解问题：VisRAG 跨模态检索的可解释性与误检归责机制？

## 与知识库的连接

- DocAI 是 [[RAG 检索增强生成]] / [[知识库问答与 Enterprise Search 学习笔记]] 的**上游数据供给层**：解析质量直接决定切块与检索上限。
- 能力评测参考 [[多模态评测基准 学习笔记]]（DocVQA/ChartQA/OCRBench/OmniDocBench）。
- 架构选择呼应 [[外挂适配式 vs 原生多模态架构]] 与 [[大模型四类型：LLM VLM MLLM LMM]]。

## 附：来源清单

- WebSearch 2026-10-05：Vision RAG vs OCR 2026；51CTO《文档理解新范式》；Awesome Agents《Best AI for Document Understanding - July 2026》；AI Wiki《Document Question Answering Models》；PromptBench《Working with Document Images》
- WebSearch 2026-10-05：MinerU 官网/GitHub Changelog（1.3.x）；jimmysong.io《开源 PDF 转 Markdown 工具深研》（Marker/MinerU/Dolphin/MarkItDown 对比）

## ⚠️ 待核实清单

- ⚠️ Qwen3-VL 的 97.1% DocVQA ANLS 为 2026-05 第三方榜单口径，以官方技术报告为准，待查实。
- ⚠️ VisRAG「20–40% 提升」来自原论文（ICLR 2025），具体任务分布待核实。
- ⚠️ 各闭源模型文档榜分数来自厂商技术报告/模型卡，SEO 农场有造假数字风险，引用前需回溯源文档。
- ⚠️ MinerU/Marker 的商业许可（GPL/研究许可 vs AGPL）细节以各自仓库 LICENSE 为准，商用前待核实。
- ⚠️ 企业平台（合合/达观/百度）的最新模型名与能力以厂商官网为准，本文仅列类别。

#标签/AI模型基础 #标签/多模态 #标签/DocAI #标签/文档智能
