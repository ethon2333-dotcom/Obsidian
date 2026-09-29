---
title: AI 评测红队与对齐 学习笔记
tags: [安全, AI红队, 对齐, 模型安全, 广度种子]
created: 2026-09-14
source: 联网核实（WebSearch / WebFetch，2025-2026 公开资料）
---

> 一句话心智模型：红队是对模型/智能体「主动找茬以暴露危险能力」的对抗测试，对齐是「用人类/AI 偏好把模型调成有用且无害」的训练方法——红队产出攻击样本，对齐拿去微调，二者构成「发现漏洞 → 修补」的安全闭环。

## 广度覆盖

| 维度 | 要点（点到为止，不深挖） |
|---|---|
| **定义** | **红队（Red-teaming）**：借用网安/军事术语，故意诱导 AI 输出有害、偏见或越权行为，在部署前发现漏洞。区别于普通评测（测预期输入表现）、渗透测试（打基础设施）、偏见审计（统计差异）。**对齐（Alignment）**：让模型行为符合 Helpful/Honest/Harmless（HHH）目标的技术集。 |
| **分类** | 红队按主体分：人工 / 自动化（AI 生成对抗输入）/ 领域专家（CBRN、网络、自主 AI 风险）/ 混合 / 智能体红队（多步、工具、浏览、代码）。按攻击面分：越狱（jailbreak）、提示注入（直接+间接）、能力 elicit（危险 capability）、目标漂移、记忆投毒、工具误用。对齐按技术分：RLHF（在线 RL）/ 离线偏好优化（DPO 族）/ RLAIF+宪法 AI / 可验证奖励 RL。 |
| **主流方案** | **红队方法**：人工专家构造；PAIR（LLM 迭代优化提示）；AutoDAN-Turbo（策略组合）；**AutoRedTeamer**（多智能体 + 记忆引导的终身攻击集成，arXiv 2503.15754）；**Active Attacks**（RL 红队 + 周期性安全微调受害者，arXiv 2509.21947）；多代理红队与 MCP 滥用 C2（arXiv 2511.15998）。**对齐方法**：RLHF（PPO/GRPO）；DPO 及其变体（SimPO/KTO/ORPO）；RLAIF + Constitutional AI（Anthropic 自对齐：定宪法→自我批判→RLAIF）；RLVR（可验证奖励）；Online/Iterative DPO。 |
| **2025-2026 进展** | 自动化红队走向「终身进化」：AutoRedTeamer 在 HarmBench 上对 Llama-3.1-70B 的 ASR 较 PAIR 提升约 20%、计算成本降约 46%；Active Attacks 跨攻击成功率由 0.07% 提至 31.28%。智能体红队集中爆发：ART 基准（Gray Swan 大赛，44 场景 / ~180 万提示）报告近 100% ASR；AgentDojo、WASP（NeurIPS 2025）、Agent-SafetyBench、AgentHarm（ICLR 2025）相继发布。前沿实验室：Anthropic Frontier Red Team 置于政策部门、聚焦 CBRN/网络/自主 AI 风险，并与 DOE 国家核安全局联合测试核敏感信息泄露；OpenAI 红队并入 Preparedness 框架；Google DeepMind 自有安全评测。OWASP LLM Top 10（2025）将提示注入列为 #1。 |
| **代表产品·机构** | 实验室：Anthropic（Frontier Red Team / Constitutional AI）、OpenAI（Preparedness）、Google DeepMind、Meta（Llama 对齐）。开源工具：NVIDIA Garak、DeepTeam（2025-11）、Microsoft Azure AI Foundry 红队代理、Promptfoo、Salesforce FuzzAI、SplxAI、AgentFence。基准：HarmBench、AdvBench、ToxiGen、BBQ、JailbreakBench、AILuminate（MLCommons，2025-03）、AgentDojo、ART、WASP、Cybench（ICLR 2025）、CVE-Bench（ICML 2025）。监管锚点：白宫 EO 14110（2023-10）要求双用途基础模型发布前红队；NIST AISI 协调。 |

## 红队与对齐的关系（一句话串联）

红队发现的攻击提示 → 构成「安全微调数据集」→ 通过对齐（尤其是安全 RLHF / DPO）修补 → 模型变强后红队再找新漏洞。Active Attacks 把这个回路做成自动化：周期性用收集到的攻击提示对受害者做安全微调，迫使攻击者探索更难的新漏洞（easy-to-hard 课程）。

## 与本库已有笔记的区分

- 与 [[端侧模型安全与越狱 学习笔记]] 区分：该篇聚焦「端侧小模型被攻击」的风险面；本篇站在「红队测试方法学 + 对齐技术 + 安全评测基准 + 实验室实践」的方法层，不限定端侧。
- 与 [[AI 监管与合规落地 学习笔记]] 区分：该篇讲监管框架（EU AI Act 等）；本篇讲技术侧的评测/对齐方法，监管仅作锚点提及。
- 与 [[Agent 评测与基准 学习笔记]] 区分：该篇侧重 agent「能力」评测基准；本篇侧重 agent「安全/对抗」红队（提示注入、工具误用、越权动作）。

## 深度盲区·待 Ethon 补充

- [ ] 对齐税（Alignment Tax）到底有多大？在端侧小模型上做安全对齐，能力与安全的 trade-off 实测如何？
- [ ] AutoRedTeamer / Active Attacks 这类自动化红队，对「中文 + 国内主流模型（如 Qwen/DeepSeek/Kimi）」的迁移效果是否打折？
- [ ] 红队 ASR 数字高度依赖「裁判模型」：不同 judge（规则 / 分类器 / LLM-judge）给出的 ASR 差异有多大，产品口径该如何对齐？
- [ ] 宪法 AI 的「宪法」由谁定？不同厂商宪法原则冲突时（如言论自由 vs 内容安全），对齐结果差异几何？
- [ ] 智能体红队里的「间接提示注入」（检索文档/工具输出藏恶意指令）在 Android 端侧 agent 场景如何落地评测？
- [ ] 红队发现的「危险能力」是否应分级披露？前沿实验室公开红队报告与 NDA / 出口管制的边界在哪里？

## 附：来源清单

1. AutoRedTeamer 论文解读（secrss）：https://www.secrss.com/articles/77499
2. Active Attacks 论文（arXiv 2509.21947）：https://arxiv.org/pdf/2509.21947
3. AI 模型对齐与 RLHF 综述（Artificial Intelligence Wiki）：https://www.artificial-intelligence-wiki.com/natural-language-processing/large-language-models/model-alignment-and-rlhf
4. LLM 安全基准 HarmBench/AdvBench/JailbreakBench（AI Wiki Agent Evaluation）：https://aiwiki.ai/wiki/Agent_Evaluation
5. Agent Red Teaming 基准 ART（Gray Swan 大赛，arXiv 2507.20526）：https://ar5iv.arxiv.org/html/2507.20526
6. Anthropic Frontier Red Team 报道（Fortune, 2025-09-04）：https://fortune.com/2025/09/04/anthropic-red-team-pushes-ai-models-into-the-danger-zone-and-burnishes-companys-reputation-for-safety/

## ⚠️ 待核实清单

- AutoRedTeamer 在 HarmBench 上「ASR 0.82（Llama-3.1-70B）、0.28（Claude-3.5-Sonnet）」「较 PAIR 提升 22%/20%、成本降 46%」——来自论文/媒体转述，具体数字以原论文 arXiv 2503.15754 为准，待 Ethon 复核。
- Active Attacks「跨攻击成功率 0.07% → 31.28%（相对增益 >400×）」——来自预印本，待正式发表版复核。
- ART 基准「近 100% ASR」「~180 万提示 / 44 场景 / 22 个前沿模型」——来自大赛论文，为作者口径，实际泛化待核实。
- 红队服务市场「2033 年达 55 亿美元」——市场预测/媒体口径，非技术事实，待核实。
- OWASP LLM Top 10（2025）提示注入 #1、过度代理 #6、系统提示泄露 #7——版次与排序以 OWASP 官方发布为准，待核实。
- Anthropic 与 DOE 国家核安全局合作、Claude 4 / GPT-5 第三方测试——来自 Fortune 报道，具体范围与结论待核实。
- WASP（NeurIPS 2025）「攻击部分成功最高 86%」——论文口径，待核实。
- 各模型（Claude 4、GPT-5、Llama 4 等）的具体对齐技术栈（如是否用 GRPO/RLVR）——厂商未完全公开，待核实。

#标签/安全 #标签/AI红队 #标签/对齐 #标签/模型安全
