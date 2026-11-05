---
title: AI Agent 评测的对抗鲁棒性持续监控 学习笔记
tags: [broadth-seed, Agent评测, 持续监控, 护栏衰减, 对抗鲁棒性, eval-drift, 在线评估, observability]
created: 2026-10-16
source: 联网核实：WebSearch/WebFetch, 2025–2026 公开资料（厂商工程博客/护栏指南/预印本）
---

# AI Agent 评测的对抗鲁棒性持续监控 学习笔记

> **一句话心智模型**：护栏不是"部署一次就完事"的静态策略，而是运行在对抗、漂移输入分布上的分类器——它的检测质量会随概念漂移、对手适应、基座模型静默更新、真实输入分布偏移而**静默衰减**；必须把护栏当成一个"会过期的模型"来持续评估、漂移监控与回归门禁运维。

## 广度覆盖

| 维度 | 要点（点到为止） |
| --- | --- |
| **定义** | production guardrail eval drift / 在线护栏衰减：输入/输出过滤、注入检测、PII 脱敏、毒性/越狱分类器、LLM-judge 护栏等，在线上运行后因**概念漂移**、**对手针对防御迭代**、**基座模型静默更新**、**真实输入分布偏移**，导致误拒率(FPR)上升 / 漏检率(FNR·ASR)攀升。传统 APM 只监控延迟与可用性，**看不到"检测质量"在掉**——本质是"护栏也是会过期的模型"。 |
| **分类** | ① 漂移类型：数据漂移 / 概念漂移（对手适应）/ 反馈环路漂移；② **失败方向不对称**：误拒(FP)用户会投诉→被迫放宽阈值，漏检(FN)攻击者不报工单→盲区静默扩大；③ 监控对象应是护栏 **verdict 事件**（命中哪个检查、决策、置信度、延迟）而非只看 block-rate；④ 评估形态：离线回归集 / 线上影子评估 / 实时 verdict 漂移告警。 |
| **主流方案** | ① 把护栏当模型运维：维护**定期刷新的留存对抗测试集**（正常/攻击/灰区三类均衡）、对线上采样做**影子重标注**猎杀 FN、版本化"护栏 + 评测集"成对发布；② **verdict 即结构化事件**：每个检查每次请求一条宽表事件，随 trace 入库，按 `check × app_version × model` 聚合；③ 告警用**相对漂移**（如 7 日移动平均的倍数）而非绝对阈值；④ 护栏回归进 CI：PR 触发评测集跑 ASR/FPR，超阈值 block merge；⑤ **agent-native CI/CD 五道门**：静态检查 → 黄金集离线 eval → 成本预算 → 生产 trace 影子评估 → 金丝雀 + 自动回滚。 |
| **2025–2026 进展** | ① 工程界把"护栏衰减"立为名问题（dev.to《Your Guardrails Are Decaying》、ClickHouse 护栏运维文、Unimon 护栏指南）；② **评测即护栏 / 评测即 CI** 成默认：Promptfoo·Braintrust·LangSmith·DeepEval 把 eval 门禁接进 PR；③ **OpenTelemetry GenAI 语义约定**成中立遥测底座（Datadog/New Relic/LangChain 已支持，2026 初仍多为 experimental）；④ 在线 verdict 漂移监控 + LLM-as-judge 持续打分成生产标配；⑤ 预印本基准开始出现（GuardBench 上线前护栏评测、GuardianAgentBench 生产框架对抗基准）；⑥ LLM-judge 自身偏差成新风险（FairJudge 2026 指前沿模型偏差任务错误率 >50%）。 |
| **代表产品** | 评测/监控栈：LangSmith·Langfuse（2026-01 被 ClickHouse 收购）·Arize Phoenix·Braintrust·Helicone·Datadog LLM Observability·Maxim AI·Galileo·Confident AI/DeepEval·Evidently；护栏/红队工具：Guardrails AI·NVIDIA NeMo Guardrails·Azure AI Content Safety·OpenAI Moderation·Giskard·WhyLabs；基准：GuardBench·GuardianAgentBench(GABench)·HarmBench（参考）。 |

## BREADTH > DEPTH：深度盲区（待解问题）

本篇只铺广度，以下问题留给 Ethon 后续深挖：

- [ ] 概念漂移的量化方法：KS / PSI / JS 散度在护栏 verdict 分布上怎么具体落地、阈值怎么定？
- [ ] 影子评估的"慢/贵二阶分类器或人工重标"：样本量、采样策略、标注成本控制？
- [ ] 灰区（允许/拒绝边界附近）样本如何系统性构造与维护，避免评测集偏攻击导致 FPR 盲区？
- [ ] 护栏版本化如何与模型版本、prompt 版本**联合回滚**（feature flag + 护栏指标耦合）？
- [ ] 在线 LLM-judge 自身的衰减/偏差漂移怎么监控（judge-on-judge）？
- [ ] 不同护栏（关键词 / 小模型 / LLM-judge）的延迟预算与关键路径取舍、并行/采样策略？
- [ ] 移动端 / 端侧 Agent 的护栏在线监控如何做（端侧无法回传全量 trace 的隐私约束）？
- [ ] 静态 eval 集"上线即过期"问题：生产失败 → 新 eval 用例的回流闭环如何自动化？

## 与库内笔记的连接（防信息孤岛）

- 护栏**设计模式本身**见 [[Agent 安全护栏模式库 学习笔记]]（本篇聚焦"模式上线后如何持续验证其衰减"，与之互补）。
- 评测 harness / CI 门禁 / 在线持续评估的工程方法见 [[Agent 评测自动化与 LLM-as-judge 工程 学习笔记]]（本篇的"护栏回归"是其"持续 eval"的一个特例切面）。
- 线上 tracing / 漂移 / 成本监控底座见 [[Agent 可观测性 LLM Observability 学习笔记]]（verdict 事件即挂在 trace 上）。
- 离线基准 vs 在线监控的方法论分工见 [[Agent 离线评估与偏好数据集 学习笔记]]。

## 附：来源清单（公开可核实）

- dev.to《Your Guardrails Are Decaying and You Aren't Measuring It》——护栏衰减概念、FN 静默盲区、留存对抗测试集 / 影子评估主张。
- ClickHouse《LLM guardrails: what they are and how to run them in production》(2026)——verdict 结构化事件、5 类护栏监控指标、Langfuse 被收购。
- Unimon《AI Guardrails Implementation Guide》——评测集三分类、CI/CD 回归、7 日移动平均相对告警、Dashboard 指标。
- GrowthBook《How to measure "quality" in AI outputs (beyond accuracy)》——静态 eval 失效、Claude Code 2025-01 回归事件、模型/输入漂移。
- Standarity / ChronoInnovation / blocksize 等 2026 Agent Observability 指南——回归 vs 漂移两失败模式、OpenTelemetry GenAI 约定、四信号监控。
- Reactify Solutions《agent evaluation and observability in 2026》——LangSmith/Langfuse/Arize Phoenix/Braintrust/Helicone/Datadog 六平台横向。
- Zylos《Agent-Native CI/CD》(2026-05)——五道部署门禁（含影子评估、金丝雀自动回滚）。
- GuardBench（preprints.org 2026-09 预印本）——上线前护栏评测框架，4200 越狱样本 / 7 类攻击 / ASR·FPR·P95 延迟 / CI 门禁。
- GuardianAgentBench / GABench（arXiv 2607.20982, 2026-07 预印本）——生产框架对抗基准，580 场景 / 5 种对抗模式 / 护栏恢复 19.9% 失败。
- FairJudge（arXiv, 2026-02）——LLM-judge 偏差任务错误率 >50%，偏差类型：位置/冗长/自我偏好/格式/校准漂移。
- inference.net / QASkills / seodatapulse / bestaiweb 等 2026 评测工程指南——Promptfoo 被 OpenAI 收购(2026-03)、回归测试即 CI、judge 校准。

## ⚠️ 待核实清单

- [ ] **Claude Code 2025-01 回归事件**具体日期与影响范围（仅单一厂商博客叙述，未交叉核实）。
- [ ] "约 91% 已部署 ML 模型会随时间性能退化"统计出处（GrowthBook 转引 Encord，原始研究口径待查）。
- [ ] **Langfuse 被 ClickHouse 收购**时间与条款（2026-01，单一厂商文叙述）。
- [ ] **OpenAI 收购 Promptfoo**（2026-03）及"保持开源、并入 Frontier"说法。
- [ ] **GuardBench** 数字（4200 样本、Token Manipulation 残留 ASR 38.8%、G3 的 P95 5799ms）——预印本、未 peer-review，待正式版复核。
- [ ] **GuardianAgentBench** 中出现的模型名（Claude Opus 4.5 / GPT-5.2 Pro / Gemini-3-Pro / DeepSeek-V3.2 / Qwen3-Max 等）属前瞻性命名，**具体型号与评测结论待核实**（预印本，且部分型号命名疑似未来向）。
- [ ] **FairJudge** ">50% 错误率"仅限"偏差特定评估任务"，非通用质量打分，适用范围勿外推。
- [ ] Langfuse v3「2026-03 不可变事件表 3× 内存 / 20× 查询加速」性能数字（厂商口径）。
- [ ] 各评测/监控平台的最新定价、功能边界随版本变动，以官网为准。

#标签/Agent评测 #标签/持续监控 #标签/护栏衰减 #标签/对抗鲁棒性 #标签/在线评估
