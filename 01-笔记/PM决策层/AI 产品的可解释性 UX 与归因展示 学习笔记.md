---
title: AI 产品的可解释性 UX 与归因展示 学习笔记
tags: #PM #可解释性 #AI产品UX #透明度 #归因 #引用溯源 #信任校准
created: 2026-10-05
source: NNGroup Explainable AI in Chat Interfaces / accelate.ai Trustworthy AI Agent UI / GitHub AI-Automation-UX Patterns (2026-08) / EU AI Act (2025-03  enforcement) / Perplexity·NotebookLM·ChatGPT Deep Research 公开资料
---

> 心智模型：可解释性 UX 不是"让模型说人话"，而是**把"结论从哪来、凭什么可信、置信多少"做成用户能感知、能核查、能纠偏的界面契约**——目标是"恰当的依赖"（appropriate reliance），而非最大信任。

## 一、广度覆盖（表格为主）

### ① 定义
| 维度 | 要点 |
| --- | --- |
| 是什么 | 把 AI 输出的推理链路、数据来源、置信程度以**用户可感知、可核查**的方式呈现在界面上 |
| 不是什么 | 不是模型内部可解释性（SHAP/注意力权重本身），而是其**产品化呈现层**；也不是伦理框架（见 [[负责任 AI 与 AI 产品伦理落地 学习笔记]]），而是 UX 落地 |
| 核心目标 | appropriate reliance——既不盲信也不弃用；让用户"在行动前就能判断答案是否可信" |
| 与交互范式关系 | 是 [[Agentic UX 交互设计模式 学习笔记]] 中"信任指示 / 透明度 / 控制权"的具体构件 |

### ② 分类 / 范式（四大主轴）
| 范式 | 说明 | 典型手法 |
| --- | --- | --- |
| 来源引用展示 | 把"结论引自哪里"以可点、可验方式呈现 | 文内角标、底部来源清单、悬停预览、句级/claim 级归因 |
| 置信度与不确定性表达 | 区分"文档事实"与"模型推断"，避免一律自信 | High/Med/Low 徽章、hedging 语言、track record（"本任务约 92% 正确"）、多模型一致性 |
| 归因高亮 | 高亮模型实际依据的文本/图像区域（grounding） | RAG 段落高亮、文档 ID/section/timestamp 标注、视觉 Grad-CAM/Score-CAM |
| 决策依据可视化 | 把"为什么是这个结论"结构化呈现 | 逐步推理(CoT)、反事实、特征归因、一句话平白解释 |

### ③ 主流方案（产品与模式）
| 方案 | 代表产品 | 实现要点 |
| --- | --- | --- |
| 文内引文角标 | Perplexity | 数字角标 + 悬停显示来源摘要；首个内置引用功能的生成式 AI（公开报道） |
| 来源 chip + 悬停预览 | Microsoft Copilot | 可点 chip，hover 出预览，"See all" 汇总；来源与正文分离，降低核查成本 |
| 事实断言 100% 引用 | Google Gemini | 公开评测称事实类断言几乎全部带引用（待核实具体口径） |
| 文内域名标注 | ChatGPT Deep Research | 报告正文标出来源域名；Grok 3 在思考过程列 URL |
| 资料溯源代理 | Google NotebookLM | 2025-04 新增"AI 溯源"，可回看资料原始来源（"Im Feeling Curious" 演示入口） |
| 置信度启发式 | RAG Agent 通用模式 | 简单启发式即可覆盖多数信任收益：claim 命中知识库=事实，否则=推断 |
| 多层解释 | XAI 实践（Berger+Team） | 全局（哪些因素通用）/局部（为何此结果）/过程（数据流+管控）/用户层（语言分层） |

### ④ 2025–2026 进展
| 进展 | 状态/时间 | 对 PM 的含义 |
| --- | --- | --- |
| EU AI Act 高风险系统 HITL 强制 | 2025-03 起执行 | 高风险 AI 须有人类介入控制——透明+可解释成为合规项 |
| 美国拟议立法 | 2027 前或强制机器可读 AI 内容标识 | 内容凭证/C2PA 将成标配 |
| 信任=市场 | McKinsey：可信 AI 到 2028 占生成式 AI 市场 65%；无信任机制产品流失率高 83%（待核实原始口径） | 透明度从"伦理加分"变"生存策略" |
| UX 模式库成型 | GitHub AI-Automation-UX Patterns 更新至 2026-08 | Trust Indicators / Explainability / Attribution / Confidence 已是可复用 checklist |
| 拟人化降信任 | NNGroup：清晰机器身份比人形头像信任高 31% | 可解释 UI 应避免拟人话术，保持中性 |
| 渐进式披露 | rruc：技术用户要细节、新手要简单置信指示 | 默认平白摘要，下钻看技术细节 |

### ⑤ 代表产品速查
| 产品 | 强项 | 可解释性短板 |
| --- | --- | --- |
| Perplexity | 主动引文、答案引擎定位 | 偶含低质来源（Reddit 等），需交叉验证 |
| ChatGPT (Deep Research) | 文内域名、深度研究 | 引用仍可能幻觉/404；需用户主动点 |
| Copilot | 来源 chip + 预览，分离清晰 | 来源质量参差 |
| Gemini | 事实断言高引用率 | 具体口径待核实 |
| NotebookLM | 多源溯源、原文回链 | 限定自有语料，非开放检索 |
| Claude | 推理步骤披露 | 解释准确性本身受限（NNGroup 指出 LLM 解释常不准确/隐藏/混乱） |

## 二、深度盲区（待解问题）
- [ ] 待解问题：**置信度误用导致过度信任**——显示 Low/Medium 徽章，用户仍照单全收；如何设计"可行动的不确定性"而非装饰性标签？
- [ ] 待解问题：**引用伪造检测**——LLM 幻觉引用（404、不存在 URL、张冠李戴），UX 层如何在不控模型的前提下降低虚假可靠感（NNGroup：用户极少主动点引文）？
- [ ] 待解问题：**移动端小屏如何展示归因**——角标/悬停预览在窄屏失效，句级引用与高亮如何压缩而不丢失可核查性？
- [ ] 待解问题：**可解释性与转化率的权衡**——展示来源/不确定性是否拖慢决策、降低"丝滑感"；与 [[数据飞轮与 AI 产品度量 学习笔记]] 的采纳率/信任衰减指标如何联动建模？
- [ ] 待解问题：**解释本身的准确性边界**——LLM 给出的"推理步骤"可能也是生成物而非真实链路，如何避免"展示即背书"的二次误导？
- [ ] 待解问题：**归因高亮与版权/数据 lineage 的耦合**——标注文档 ID/section 需要检索系统原生带 citation schema（accelate：事后 retrofit 极难），端侧/原生 API 场景如何落地？

## 三、库内连接
- 与 [[负责任 AI 与 AI 产品伦理落地 学习笔记]]：伦理框架（RAI/可解释性）→ 本文是其 UX 落地层；透明披露、红队发布闸门共用。
- 与 [[Agentic UX 交互设计模式 学习笔记]]：本文是其中"信任指示 / 透明度 / 控制权"轴的产品化构件。
- 与 [[AI 产品需求定义与 Agent 设计规范 学习笔记]]：可解释性应作为 PRD 一级需求（eval 前置、HITL、降级），而非上线后补丁。
- 与 [[数据飞轮与 AI 产品度量 学习笔记]]：幻觉率、信任衰减、采纳率可直接度量可解释性 UX 的成效。

## 附：来源清单
1. NNGroup — *Explainable AI in Chat Interfaces*（Megan Chan）：引文/逐步推理/免责声明三类解释的现状与风险，用户极少点引文。
2. accelate.ai — *How to Design a Trustworthy AI Agent UI: Sources, Confidence, and Labeling*：claim 级引用、可见置信信号、明确 AI 标识三要素。
3. GitHub vasilyu1983/AI-Agents-public — *AI & Automation UX Patterns (2025–2026)*，更新 2026-08：Trust Indicators / Explainability / Attribution / Confidence 模式库。
4. berger.team — *Transparency and traceability of AI*：多层 XAI、RAG 强制引用、数据 lineage、C2PA/Content Credentials。
5. rruc.org — *Designing Trustworthy Generative AI UX*：透明度>早期准确性、拟人化降信任 31%、渐进式披露、HITL 合规趋势。
6. 腾讯新闻 / 网易 / 搜狐 公开报道（2025）：Perplexity 引文模式、NotebookLM 2025-04 溯源功能、ChatGPT Deep Research 文内域名。
7. EU AI Act：2025-03 高风险系统 HITL 强制（监管背景，公开资料）。

## ⚠️ 待核实清单
- [ ] Gemini "100% 事实断言引用"的具体评测口径与时间点（rruc 引用，未溯原始来源）。
- [ ] McKinsey "可信 AI 占市场 65% / 无信任机制流失高 83%" 原始报告与统计方法。
- [ ] GitHub AI-Automation-UX Patterns 仓库的权威性（社区仓库，非官方标准）。
- [ ] NotebookLM 溯源功能上线确切日期与功能边界（二手报道）。
- [ ] 各产品置信度/引用能力的 2026 最新版本差异（产品迭代快，本文为 2026-10 快照）。

#标签/PM #标签/可解释性 #标签/AI产品UX #标签/透明度
