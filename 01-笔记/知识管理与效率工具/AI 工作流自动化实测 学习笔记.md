---
title: AI 工作流自动化实测 学习笔记
tags: [广度种子, 知识拓展Loop, 工作流自动化, 自动化, 效率工具, Agent]
created: 2026-09-21
source: WebSearch/WebFetch 核实，含待核实项
---

工作流自动化的真正分水岭不在"能不能搭出来"，而在"上线后每一步的可靠率乘起来还能不能跑完、以及它到底花了多少钱"。

## 与已覆盖笔记的差异

[[AI 工作流自动化与编排 学习笔记]] 覆盖的是"编排范式 + 平台清单"的广度地图，[[低代码无代码 Agent 搭建平台 学习笔记]] 覆盖的是"怎么低代码把 Agent 搭出来"。本篇不重复这两者，而是把视角拉到**实测层**：真实任务完成率、单位成本、长链路可靠性、企业落地 ROI 与人机协同节点——即"搭完之后到底好不好使、贵不贵、靠不靠谱"。

## 广度覆盖（点到为止）

### 一、三类形态：定义与代表产品

| 形态 | 是什么 / 定义 | 代表产品 / 平台 | 计费与成本特征 | 可靠性特征 | 适用边界 |
|---|---|---|---|---|---|
| 托管 SaaS 自动化 | 云端触发-动作 + 内置 AI 步骤，零运维、开箱即用 | Zapier（含 Zapier Agents / AI by Zapier）、Make（原 Integromat）、Relay.app | 按"任务/操作"计费的订阅制；高量最贵 | 平台级 SLA 高，但 AI 步骤对脏输入敏感 | 非技术、要广度集成、不想碰服务器 |
| 自托管 / 开源 | 自己跑实例，数据不出域，无按次计费 | n8n（社区版开源）、Dify（私有化部署）、FastGPT、Coze 私有化 | 开源免费 + 自有基础设施/运维人力（TCO 转移） | 取决于你自己的运维与故障兜底 | 有合规/数据驻留诉求、高量成本敏感、有技术团队 |
| Agentic workflow | 给目标、接工具，Agent 自己决定步骤与路由 | Zapier Agents、Make AI Agents、Dify Workflow + 子流程、Coze Bot、企业级 Agentforce / Copilot Studio | 混合：SaaS 按动作、私有按 token+算力 | 长链路"复利衰减"是核心风险（见下） | 输入多变、需判断、但需配人工闸门 |

> 注：三者并非互斥——很多团队用 SaaS 验证场景、再迁私有化；或把既有 Zaps 当 Agent 的工具调用。

### 二、2025-2026 关键进展（含待核实）

| 进展 | 事实口径 | 可信度 |
|---|---|---|
| Zapier Agents 走出封闭测试（GA） | 早期 2026 转 GA，新增持久记忆（Zapier Tables）、既有 Zaps 可作 Agent 工具、错误日志+重试 | 二手媒体（hammerautomation.ai）✔；具体 error<2% on ≤7 步 **待核实** |
| Zapier AI Agents 锚点测试 | 某评测（aidemos.com, 2026）称 5 个锚点任务"零失败"全过；免费档把 CRM/邮件/工单动作限为预览 | 单一评测基准 **待核实** |
| n8n AI 化 + 自托管成主流 | 内置 LangChain/向量节点、Ollama 本地 LLM；社区版开源免费 | 多源一致 ✔ |
| Make / Relay.app 人机协同 | Relay.app 主打"AI 建议→人工确认再执行"审批节点（前 Google 团队）；Make 推 AI Agents + 错误处理器 | 多源一致 ✔；Relay 大规模可靠性未验证 **待核实** |
| Coze vs Dify 企业实测 | 中文交付复盘：Coze 渠道最齐/上线最快；Dify 私有化+RAG+Workflow 编排最均衡 | 厂商/交付方内部数据 **待核实** |
| 企业 agentic ROI 进入 P&L | 多报告称 agent 错误率从 2025 初 8-12% 降到 Q4 3-5%；Salesforce Agentforce 8000+ 企业客户、213% ROI | 行业报告聚合 **待核实** |

### 三、代表玩家速查（广度优先）

| 产品 | 形态 | 实测亮点 / 边界（公开口径） |
|---|---|---|
| Zapier | SaaS + Agents | 集成 6000+；AI 步骤算 2 任务/步；长链路对脏输入敏感，建议加人工复核 |
| Make | SaaS | 可视化分支/循环/错误处理器最强；1,000+ 集成；纯云、数据过其服务器 |
| n8n | 自托管/云 | 开源免费；生产需 Postgres+Redis+反代；中等规模 TCO 远低于 SaaS |
| Relay.app | SaaS（人机协同） | 审批闸门一流；集成少于 Zapier/Make；社区小、规模可靠性未验证 |
| Dify | 私有化/云 | 私有部署+RAG+Workflow 编排均衡；企业 RBAC/审计强；需技术投入 |
| Coze（扣子） | SaaS/私有化 | 渠道适配最齐、零代码最快；云端托管有合规顾虑、深度定制受限 |
| 企业级 | Agentforce / Copilot Studio / ServiceNow | 绑定大厂生态、合规/审计完备；单价高、迁移成本大 |

## 长链路可靠性：本篇的核心认知

多步 agentic workflow 的致命问题是**错误复利衰减**——这是数学事实，不是模型能力问题：

- 每步 95% 可靠 → 20 步仅 **36%** 端到端成功；10 步约 59%。
- 每步 99% 可靠 → 20 步仍仅 **82%**。
- 生产级通常要求 99.9%+（即 20 步需每步 ≥99.86%）。

实操共识（cio.works、pingax 等多源）：把长链路拆成 **3-5 个可独立验证的原子操作 + 显式回滚点 + 关键节点人工确认**，而非试图一次性自主跑完 20 步。失败模式主要有六类：工具误用、上下文丢失、目标漂移、重试死循环、多 Agent 级联错误、静默质量退化。

> ⚠️ 行业报告口径（agentstatus.dev 汇总 vaza.ai / HB-Eval / Arize）：2025 年"95% 的 AI Agent 未达生产要求"、理想 86.9% → 扰动下 44.0%——此类数字来自具名报告但口径不一，**待核实**。

## 成本实测（公开估算，均待核实）

| 场景（月执行量） | Zapier | Make | n8n Cloud | n8n 自托管 |
|---|---|---|---|---|
| 轻量（数百~数千） | 免费~$20 | 免费~$9 | $20 起 | $8-25 (VPS) |
| 中等（日数千） | Pro $49.99* | Core $9-16 | Pro ~$50 | $20-40 (2vCPU/4GB) |
| 高量（50 万操作） | ~$1,200** | ~$340** | ~$50 | ~$20 (服务器)** |

- *Zapier 报价有 $49.99/mo 与 $49/mo 两种口径，且"Agent 跑 3 步=3 任务"会快速吃额度，**待核实**。
- ** 规模数字来自第三方评测（aiskillnav / mohasoftware）的建模估算，非官方价目，**待核实**。
- n8n 自托管真正成本 = 服务器 + Postgres/Redis + 备份 + 监控 + **运维人力**，开源≠零成本。

## 人机协同节点（HITL）

- Relay.app 把"人工审批"做成一等公民（AI 起草邮件→总监批→自动发）。
- 通用做法：凡触碰发邮件、改 CRM 阶段、动账单的动作，强制加 human review 步骤。
- 落地纪律（pingax）：先 5% → 20% → 100% 灰度；人工兜底率 >15% 即暂停；捕获 prompt/工具输出/最终动作/兜底率全程日志。

## 企业落地案例（公开口径，待核实）

- Salesforce Agentforce：2026-01 称 8000+ 企业客户，某 Service Cloud 案例 213% ROI、自助效率 +40%。
- 某制造企业（1200 人）：私有化知识库选型 FastGPT 命中率 92% / 幻觉率 3%，Dify 85% / 7%。（交付方内部复盘）
- 连锁服饰电商：Coze 2 周上线、满意度 84%，渠道适配最齐、业务可自改话术。
- 通用 SaaS 内容生产：Dify 在一个 Workflow 串 Claude + 通义 + 豆包做多端内容，编排灵活度最强。

## 深度盲区

- [ ] Zapier Agents / AI 在真实多步业务流中的"端到端完成率"基准到底是多少？（媒体 <2% error、5/5 anchor pass 均为二手或厂商基准，缺独立大样本）
- [ ] n8n 自托管在中等规模（日 1-5 万执行）下的真实 TCO：含运维人力、备份、监控、故障恢复，而不只是 VPS 账单
- [ ] 长链路（>10 步）agentic workflow 在 Ethon 自身场景（PM 周报/需求流转）的失败模式与兜底机制怎么设计
- [ ] Make / Relay.app 的"人机协同审批"节点在中文企业生态（企微/飞书）的落地成本与可用性
- [ ] Coze vs Dify 私有化 RAG 在中文语料（SOP/制度库）的命中率与幻觉率对照（现有数字均来自厂商/交付方内部复盘，待独立验证）
- [ ] 企业 agentic ROI 的可信度：213% ROI / "88% 已用 AI" 等数字的方法学（样本、归因口径、是否含隐性成本）
- [ ] 各平台"AI 步骤计费"随模型切换（GPT-5.6 / Claude Opus 4.8 / Gemini 3.5 Flash）的真实单价波动

## 附：来源清单

1. hammerautomation.ai —《Zapier Agents leave beta: what small teams can actually do now》（早期 2026 GA、error<2% on ≤7 步、任务计费口径）
2. aidemos.com —《Zapier AI Agents Review: 5 Anchor Tasks Tested (2026)》（锚点任务基准、免费档限制）
3. n8nhost.io / hostingqa.com / logicworkflow.com — n8n 自托管 2025 成本、系统要求、Cloud vs 自托管对比
4. aiskillnav.com / mohasoftware.com / savedelete.com — Zapier vs Make vs n8n 2025 横向（含规模成本建模、延迟测试）
5. sgpjbg.com —《2025 AI 工作流程编排工具对比：Zapier vs Make vs n8n vs Relay》（Relay 人机协同定位）
6. agentstatus.dev —《State of AI Agent Reliability 2026》（vaza.ai / HB-Eval / Arize 汇总口径）
7. ai2.work —《From Pilot to Production: Enterprise Agentic AI Delivers Real ROI》（Agentforce / 错误率下降 / 企业 ROI）
8. toutiao / csdn / wsisp — 2026 企业级 Coze·Dify·FastGPT 实测横评（中文交付方内部复盘）
9. cio.works —《Why I'm Betting Against AI Agents in 2025》（错误复利衰减数学、原子化+人工闸门架构）
10. pingax.com — real world AI agent applications 2025（function calling 准确率、HITL 灰度纪律）

## ⚠️ 待核实清单

- Zapier Agents "error <2% on ≤7 步"——单一二手媒体口径。
- Zapier 报价 $49.99 vs $49/mo，及"Agent 跑 N 步 = N 任务"的精确计费。
- 规模成本建模数字（50 万操作：Zapier ~$1,200 / Make ~$340 / n8n Cloud ~$50 / 自托管 ~$20）——第三方估算非官方。
- n8n vs Zapier 延迟（2.2s vs 5.1s median）——单一测试，样本与条件未公开。
- Coze/Dify/FastGPT 内部基准（命中率 92%/85%/78%、幻觉率 3%/7%/10%、满意度 84%）——厂商/交付方数据，非独立验证。
- 行业可靠性报告（95% 未达生产、HB-Eval 86.9%→44.0%、Arize 失败成本 $5k-50k）——具名报告但口径不一。
- 企业 agentic 错误率 8-12%→3-5%、Agentforce 213% ROI / 8000+ 客户、Anthropic 占企业 LLM 支出 40%——行业报告聚合。
- Zapier "97% builder 每日用 AI"、AutomationBench 各模型分数（GPT-5.6 Sol 等）——Zapier 自有营销/汇总口径。
- "88% 公司已在用 AI、仅 6% 高绩效"等 McKinsey/ surveys 的采样与归因。

#标签/广度种子 #标签/工作流自动化 #标签/自动化 #标签/效率工具 #标签/Agent
