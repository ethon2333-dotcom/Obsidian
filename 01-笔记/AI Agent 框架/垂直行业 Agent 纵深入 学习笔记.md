---
title: 垂直行业 Agent 纵深入 学习笔记
tags: [广度种子, 知识拓展Loop, 行业Agent, 法律AI, 医疗AI, 教育AI]
created: 2026-09-21
source: WebSearch/WebFetch 核实，含待核实项
---

# 垂直行业 Agent 纵深入 学习笔记

> 一句话心智模型：垂直行业 Agent 的本质不是"更会答的通用模型"，而是**把 Agent 嵌进高监管、强责任门槛的行业工作流里**——落地顺序普遍遵循"低风险长流程（copilot-in-workflow）先跑、高风险自主决策（autonomous agent）后探"，胜负手在治理、审计与责任归属而非模型能力本身。

## 与已覆盖笔记的差异

本篇聚焦**通用 Agent 框架之外的行业纵深落地**（法律 / 医疗 / 教育），按"行业 × 部署形态 × 监管责任门槛"组织，刻意不重复 [[多智能体协作与编排 学习笔记]]（通用协作模式）、[[Agent 评测与基准 学习笔记]]（通用基准）、[[数据 Agent 与 Text-to-SQL 学习笔记]]（结构化数据问答）、[[知识库问答与 Enterprise Search 学习笔记]]（企业检索）已覆盖的通用层；本篇只取"行业特异性"这一层，深度留白给 Ethon。

## 广度覆盖

### 1. 法律：AI 合同审查 / 法律研究 Agent

| 维度 | 内容 |
|---|---|
| 定义 / 是什么 | 面向律所与企业法务的专业 Agent：合同审查、尽职调查、法律研究、起草、谈判辅助。**普遍定位 agentic workflow（人把关）而非自主决策**。 |
| 主流方案（横向对比） | **Harvey**：全栈法律 Agent 平台，agentic workflow 基础设施，700+ 律所、50 家 AmLaw 100；**CoCounsel（Thomson Reuters）**：Westlaw/Practical Law 内容锚定、引用可核验研究，超 100 万专业人士；**Legora**：欧陆强、大批量结构化合同审查；**Spellbook**：Word 原生合同起草/审查（中小所）；**EvenUp**：人身伤害专精（诉请书/医疗时间线）；**Robin AI**：AI+人审托管服务；**Leya**：北欧/EU 法覆盖；**Anthropic Claude for Legal**（2026-02，20+ 连接器、12 个执业插件）。 |
| 2025-2026 关键进展 | Harvey 2026-03 以约 $11B 估值融资（待核实具体金额）；Legora 2026-03 完成 $550M Series D、$5.55B 估值（待核实）；EvenUp 2025-10 $150M Series E、$2B+ 估值（待核实）；Anthropic 2026-02 直接进入法律工作流层；LegalWeek 2026 共识：竞争从"模型能力"转向**治理、工作流控制、数据信任**。 |
| 部署形态 | copilot-in-workflow（CoCounsel 在 Word 内交互审查、Harvey playbook 批量跑）为主；自主 agent 仅限低风险批处理（如数千份合同初审）。 |
| 监管与责任门槛 | 律师职业责任（malpractice）、客户保密（ethical walls / matter 级权限）、bar 合规、幻觉风险。**90% 法律费仍按小时计费**（Thomson Reuters 2026 报告，待核实）——效率工具与计费模型的结构性张力。 |

### 2. 医疗健康：临床 / 患者侧 Agent

| 维度 | 内容 |
|---|---|
| 定义 / 是什么 | 嵌进临床与运营工作流的 Agent：环境录音文书（ambient scribe）、患者外联语音、临床决策支持、诊断研究系统。**落地铁律：先攻低风险长流程、再碰高风险诊断**。 |
| 主流方案（横向对比） | **环境录音文书**：Abridge（独立龙头，$100M+ ARR@2025-05、$5.3B 估值@2025-06、KLAS 连续第一 2025/2026，待核实数字）、Microsoft Dragon Copilot（DAX+Dragon Medical One 于 2025-03 合并，150+ 医疗系统、10 万+ 医师日活，厂商口径）、Suki / Freed / Heidi / DeepScribe / Augmedix(Commure)；**患者语音 Agent**：Hippocratic AI（Polaris 3.0@2025-03，22 个 LLM、非诊断外联，1.8 亿+ 次交互，待核实）；**临床决策支持**：OpenEvidence（75.7 万+ 认证医师、月 2000 万+ 次咨询@2026-01，非营利免费）、Epic Art/Penny/Emmie；**诊断研究系统**：Google AMIE（Nature 2025，研究系统不产品化）、Microsoft MAI-DxO（2025-07，多智能体诊断编排）、Healthcare Agent Orchestrator（2025-05，明确"按现状不用于临床部署"）。 |
| 2025-2026 关键进展 | Dragon Copilot 由"写笔记"向"临床推理/建议"演进（HIMSS 2026）；McKinsey 2026 调研：50% 机构已实施 genAI、19% 达 agentic 成熟度；Deloitte 2026：80%+ 健康系统优先把 agentic AI 用于临床运营与收入周期（非自动诊断）；FDA 截至 2026-01 已授权 1300 个 AI 医疗设备（厂商/监管口径）。 |
| 部署形态 | copilot-in-workflow 绝对主流（文书、外联、编码、事前授权）；autonomous agent 仅限研究/专病（如 BAAI Cardiac Agent、WiseClaw 2.0 等中国案例，待核实证据强度）。 |
| 监管与责任门槛 | **责任归属核心矛盾**：现行仍以医疗过失（malpractice）为框架，医师为责任焦点（"说 AI 错了"通常不成抗辩）；直接-to-患者路径（无医师中介）责任转向厂商，尚缺定论（Nature 2026、Chambers 2026）。WHO Europe 2025-11 调查：法律不确定性是 AI 采用头号障碍，<10% 国家有明确责任标准。需 human-in-the-loop、审计追踪、HIPAA、FDA 变更控制。 |

### 3. 教育：自适应学习 / AI 导师 Agent

| 维度 | 内容 |
|---|---|
| 定义 / 是什么 | 面向 K-12 / 高教 / 职业的个性化学习 Agent：苏格拉底式辅导、自适应路径、语言陪练、行政答疑。**定位"人类教师的放大器"而非替代**。 |
| 主流方案（横向对比） | **Khanmigo（可汗学院）**：GPT-4 起家，2026-02 接入 Google Gemini 做读写，1800 万+ 活跃用户@2025 末（待核实），$4/月、教师免费，苏格拉底式；**Duolingo Max / AI Max**：GPT-4o，2025-05 推 AI Max，5 亿+ 注册（待核实），Roleplay / Explain My Answer，$29.99/月；**Coursera Coach**：2024 推、2025 升级，企业 ARR $300M+（待核实）；**Squirrel AI（中国）**：3000+ 学习中心、2400 万学生、微知识点自适应；**MagicSchool AI**：教师侧，500 万+ 教育用户@2025；**Ivy.ai（高校）**：IvyQuantum 高校学生服务 chatbot，"仅用你校内容"回答招生/资助/注册查询，现为 Gravyty "Ivy & Ocelot"，报价制、按 FTE 与学生数计费。 |
| 2025-2026 关键进展 | 多District 实测：AI 导师+人类教师组合优于单用任一方；Khanmigo 2026-02 与 Google 结盟扩至读写；Duolingo AI 加速 148 门新课产出（人工监修）；教师角色从"知识源"转向"学习架构师"。 |
| 部署形态 | copilot-in-workflow（教师备课/批改/分析 dashboard）为主；学生侧多为 guided tutor（不给直接答案）。真正 autonomous 学情诊断 + 路径生成在 Squirrel AI / MATHia 等自适应引擎中已较成熟。 |
| 监管与责任门槛 | 相对最轻：无医疗级过失责任，但涉**未成年人数据隐私（FERPA/COPPA）、学术诚信、幻觉误导**。责任落在机构与教师（内容准确性、合规使用），而非"AI 担责"。 |

### 跨行业共性（点到为止）

- **落地顺序一致**：copilot-in-workflow（低风险、长流程、可审计、能回收 ROI）先规模化；autonomous agent（高风险决策）后探或限研究/专病。
- **胜负手一致**：从"模型能力"竞争转向**治理、工作流控制、数据信任、责任归属**（LegalWeek 2026 / Microsoft NEJM AI 2026 成熟度曲线）。
- **与通用 Agent 的关系**：行业 Agent 多建立在通用编排/记忆/检索/协议之上（见 [[多智能体协作与编排 学习笔记]]、[[知识库问答与 Enterprise Search 学习笔记]]），差异在行业知识、合规护栏与责任模型。

## 深度盲区（待 Ethon 补充）

- [ ] 法律 Agent 的"幻觉"与通用 chatbot 幻觉在后果量级上有何本质差异？有无行业专属评测（如合同抽取准确率基准）？
- [ ] 医疗责任"shared multi-actor liability"（开发者/部署方/医师三方）在具体司法判例里如何分摊？有无首案？
- [ ] autonomous 诊断 Agent（MAI-DxO / AMIE）走向产品化的监管路径与时间表是什么？
- [ ] 教育自适应引擎（Squirrel AI / MATHia）的"知识追踪"底层算法（BKT / DKT / 大模型）孰优？
- [ ] 各行业 Agent 的真实 ROI 度量口径（小时节省 vs 计费模型冲突 vs 临床结局）如何统一？
- [ ] 中国医疗/法律/教育 Agent 的监管沙盒与合规边界（对比欧美 FDA / bar / FERPA）有何差异？
- [ ] 行业 Agent 的"自主度梯度"如何分级（建议对照 [[Agent 协议生态 学习笔记]] 的协议层）？
- [ ] 垂直 Agent 是否正在演成"行业 OS"（如 WiseClaw 医疗 Agent OS、Epic 内嵌三 Agent）？平台化临界点在哪？

## 与库内笔记的关联

- 通用协作/编排底座：[[多智能体协作与编排 学习笔记]]
- 评测与验收口径（行业 Agent 仍缺专属基准）：[[Agent 评测与基准 学习笔记]]
- 结构化数据问答（医疗/教育运营分析侧）：[[数据 Agent 与 Text-to-SQL 学习笔记]]
- 企业级权限感知检索（律所/医院知识库）：[[知识库问答与 Enterprise Search 学习笔记]]

## 附：来源清单

1. Harvey / 法律 AI 横向对比与融资：https://ai2.work/blog/harvey-raises-200m-at-11b-as-legal-ai-becomes-infrastructure
2. Harvey vs CoCounsel 合同审查（2026 架构对比）：https://lawr.io/knowledge/harvey_vs_cocounsel_for_contract_review_which_ai_legal_tool_is_better_in_2026.php
3. 医疗 AI 全景（ambient scribe / Hippocratic / OpenEvidence / AMIE）：https://aiwiki.ai/wiki/health
4. 2026 医疗 AI 代理实践清单（含中国案例 BAAI/WiseClaw/温州）：https://fast.io/resources/best-ai-for-healthcare-2026
5. Microsoft Dragon Copilot agentic 演进与 NEJM AI 成熟度曲线：https://healthtechauthority.com/beyond-ambient-scribes-microsofts-agentic-ai-push-and-what-it-means-health-care-it
6. 教育 AI 自适应学习（Khanmigo / Duolingo / Coursera / Squirrel AI）：https://aiwiki.ai/wiki/ai_in_education
7. 医疗 AI 责任框架（Chambers 2026 / Becker's Pillay Framework / Nature 2026）：https://practiceguides.chambers.com/practice-guides/comparison/1370/19823/ 、https://www.beckershospitalreview.com/healthcare-information-technology/ai/ai-liability-a-framework-for-health-systems/ 、https://nature.com/articles/s41746-026-02854-5
8. Ivy.ai 高校 chatbot：https://ivy.ai/ 、https://www.eesel.ai/blog/mio-alternatives

## ⚠️ 待核实清单

- Harvey 2026-03 融资 $200M / $11B 估值、Legora $550M / $5.55B、EvenUp $150M / $2B+ 等具体金额与日期（厂商/二级源，未逐一交叉核验）。
- Abridge $100M+ ARR、$5.3B 估值、KLAS 连续第一 2025/2026；Microsoft Dragon Copilot "150+ 医疗系统 / 10 万+ 日活"为厂商口径。
- Hippocratic AI "1.8 亿+ 次交互 / 99.38% 临床准确率"为厂商自评数据。
- Khanmigo "1800 万+ 活跃用户"、Duolingo "5 亿+ 注册"、Coursera "企业 ARR $300M+" 为二级市场研究/厂商口径。
- "90% 法律费仍按小时计费"（Thomson Reuters 2026 报告）、医疗 AI"50% genAI / 19% agentic"等为调研口径，方法论未复核。
- 中国案例（BAAI Cardiac Agent、WiseClaw 2.0、温州城市级）公开证据强度参差，WiseDiag-v2 "全球第一"源自 2026 新上线 DoctorBench 榜单，宜视为待独立验证信号。
- Ivy.ai 具体客户数、定价、WCAG 合规性以厂商口径与个别 G2 评价为主，未独立核实。
- FDA"1300 个 AI 设备授权"为截至 2026-01 的监管口径，随更新变动。

#标签/广度种子 #标签/知识拓展Loop #标签/行业Agent #标签/法律AI #标签/医疗AI #标签/教育AI