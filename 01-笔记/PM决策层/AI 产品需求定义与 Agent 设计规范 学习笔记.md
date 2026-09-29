---
title: AI 产品需求定义与 Agent 设计规范 学习笔记
tags: [知识拓展, PM, Agent, 需求工程, AI产品需求]
created: 2026-09-19
source: 公开资料整理（WebSearch 2026-09-19：Traversaal/AGI Tech/Groto/Anthropic/Braintrust/Thoughtworks/agentruntime 等）
---

# AI 产品需求定义与 Agent 设计规范

**AI 产品的 PRD 不是「写功能清单」，而是「把评测标准、失败边界和权限闸门写进需求」——需求工程优先于交互设计。**

> 本文聚焦「需求定义 / PRD 规范」，与 [[Agentic UX 交互设计模式 学习笔记]]（交互范式）、[[数据飞轮与 AI 产品度量 学习笔记]]（上线后度量）、[[智能体身份与信任 学习笔记]]（身份信任）、[[AI 产品商业模式与定价策略 学习笔记]]（变现）互补，专门补「需求前置」这一环。

## 一、定义：AI 产品需求定义的特殊性

| 维度 | 传统软件 PRD | AI / Agent PRD |
|---|---|---|
| 输出确定性 | 同输入 = 同输出（确定性） | 同输入 ≠ 同输出（非确定性，需概率化验收） |
| 验收语言 | 二进制「满足 / 不满足」 | 概率化「通过率 ≥X% / 失败率 ≤Y% / 置信阈值」 |
| 核心 artifact | 功能规格 + 验收用例 | 规格 + **eval 数据集 + 护栏规范 + 权限边界** |
| 失败处理 | 异常分支 | 失败是常态，需降级、HITL、可撤销设计前置 |
| 漂移 | 需求冻结 | 模型/提示/数据漂移，需持续 eval 与活文档 |

> 一句话：AI PRD 把「怎么算做好」写进需求，而不是上线后靠体感判断。

## 二、分类：AI 特有的五类需求维度

| 类型 | 关注点 | 需求写法要点 |
|---|---|---|
| **eval 前置型** | 把评测标准当验收门槛 | 指定测试集规模/标注法/最低通过率（如「≥88% 准确率才进 shadow mode」） |
| **HITL 型** | 人在回路的确认/接管 | 定义升级触发（置信度/数据敏感度/意图歧义）+ 交接 SLA |
| **降级型** | 出错时安全兜底 | 指定 fallback 路径、auto-throttle 阈值（如 48h 滚动失败率超限自动暂停） |
| **权限可撤销型** | 动作可逆性与授权 | 动作按可逆性分级（只读/草稿/不可逆），不可逆动作需显式确认 |
| **成功标准模糊型** | 模糊任务如何定义成功 | 用 HEART/目标–信号–指标（GSM）把「好」拆成可量化子指标 |

## 三、主流方法 / 框架对比

| 方法 / 框架 | 适用场景 | 要点 |
|---|---|---|
| **Google HEART（for AI）** | AI 功能日常 KPI 设定 | Happiness/Engagement/Adoption/Retention/Task Success；配 GSM 把目标转信号再转指标；Task Success 为核心运营指标 |
| **Anthropic agent 评估实践** | Agent / 工具调用质量 | 每任务配可验证的 prompt-response 对；追踪准确率+工具调用数+token+耗时；end-state 评估（多轮改状态看终态而非逐步） |
| **eval-driven development** | Agent 迭代（TDD 的等价物） | 定义 eval case → 构建 → 跑分 → 分析失败 → 改 prompt/工具 → 循环；含 outcome/trajectory/safety 三类 eval |
| **spec-driven（spec-kit / Cursor specs）** | AI 辅助编码的需求规范化 | Specify→Plan→Tasks→Implement；Constitution 定原则；规格即「活文档」与真源；机器可读规格降低幻觉 |
| **PRD 模板演化（含 [AI] 专节）** | 非确定性功能立项 | 新增 Eval 框架 / 护栏规范 / 模型策略 / 数据要求 / 负责任的 AI / 不确定性 UX 等专节 |
| **成功标准设计（概率化验收）** | 模糊 / 高风险任务 | 用最小通过率 + 每类失败上限 + 自主行动置信下限替代「应准确」式空话 |

## 四、2025–2026 进展（WebSearch 核实）

- **eval 成为需求一等公民**：2026 年 CTO 指南强调「评估应先于 prompt / 厂商 / 架构定稿」，评估写成验收门槛而非研究笔记（AGI Tech 2026）。
- **spec-driven 进入主流**：GitHub Spec Kit（开源）、Amazon Kiro、Cursor specs 普及；Thoughtworks 明确「spec 提升清晰度与确定性、省 token、降幻觉」，但「尚无系统化的 spec 评估方法」仍开放。
- **Agent 任务 SLA 四维化**：传统可用性 SLA 不足，新增 Quality（群体输出质量承诺）、Consistency（同输入变异边界）两维；强调「违反无后果的 SLA 只是建议」（agentruntime）。
- **护栏进代码而非 prompt**：2025–2026 多起企业事故证实 prompt-only 安全指令会被边界输入绕过，禁止操作清单 / 速率限制必须写成硬约束（Traversaal）。
- **shadow mode 前置**：不可逆动作必须并行运行（输出只记录不执行）再晋级，晋级门槛写进 PRD（Traversaal / Your AI Consultant）。

## 五、代表实践（点到为止）

- **Traversaal AI Agent PRD 模板**：可量化验收三数（最小通过率 / 每类失败上限 / 自主置信下限）+ 禁止操作清单 + 不可逆分级 + 升级 SLA。
- **Groto AI PRD 模板**：把经典验收替换为「[AI] Eval 框架 / 护栏 / 模型策略 / 数据 / 负责任的 AI / 不确定性 UX」专节。
- **Anthropic 多 Agent 研究系统**：end-state 评估 + 长程对话压缩/记忆 + 子 agent 产物落到文件系统减少「传话」失真。
- **AGI Tech 30 天 PRD Sprint**：W1 结果&流程 → W2 数据&系统 → W3 评估&风险 → W4 架构&交付，先消未知再写代码。

## 待解问题（BREADTH > DEPTH，留白）

- [ ] 模糊任务（如「帮我规划一次旅行」）的成功标准如何量化、如何设不需人工逐条判定的自动 grader？
- [ ] eval 数据集与 PRD 的绑定流程：谁拥有测试集、何时更新、漂移如何触发 PRD 修订？
- [ ] 非确定性需求的评审机制：PM/引擎/安全如何就「概率化验收」达成共同 sign-off 口径？
- [ ] 跨应用 OS 级 Agent（见 [[OS 级系统 Agent 与跨应用自动化 学习笔记]]）的权限可撤销性在系统层如何统一表达？
- [ ] 护栏「进代码」与「prompt 灵活度」的张力：硬约束过多是否会扼杀 Agent 泛化能力？

## 库内关联

- 交互范式 → [[Agentic UX 交互设计模式 学习笔记]]
- 上线后度量 → [[数据飞轮与 AI 产品度量 学习笔记]]
- 身份与授权闸门 → [[智能体身份与信任 学习笔记]]
- 变现与成本 → [[AI 产品商业模式与定价策略 学习笔记]]
- 人类确认 UX 与责任边界 → [[Confirmation UI 分级与产品责任边界]]
- 系统级自动化权限 → [[OS 级系统 Agent 与跨应用自动化 学习笔记]]

## 附：来源清单

1. Traversaal.ai — *AI Agent PRD: A Section-by-Section Template for Non-Deterministic Features*（概率化验收、护栏进代码、shadow mode）
2. AGI Tech Consultants — *AI Product Requirements Document: CTO Guide for 2026*（评估前置、30 天 PRD Sprint、风险分级治理）
3. Groto — *PRD Template Guide: What Changes for AI Products*（AI 专节 PRD 模板）
4. Anthropic Engineering — *Writing tools for agents / Multi-agent research system*（eval 任务设计、end-state 评估）
5. Thoughtworks — *Spec-driven development unpacking 2025*（SDD 实践、spec 漂移与幻觉、与 waterfall 区别）
6. AgentRuntime — *SLA Design for AI-Powered Products*（AI SLA 四维：可用性/延迟/质量/一致性）

## ⚠️ 待核实清单

- [ ] Google HEART 是否有官方「for AI」变体，还是业界自行延展（HEART 原框架由 Kerry Rodden/Google 提出，AI 适配为二手归纳）——待核实。
- [ ] 「78% 组织 2024 已用 AI」（Stanford HAI 2025 AI Index）具体口径与年份——待核实。
- [ ] Spec Kit 当前支持的 AI 助手列表（claude/copilot/gemini/cursor/qwen）是否随版本变化——待核实。
- [ ] Agent SLA「违反无后果即建议」是否已有行业通用落地范式（如自动暂停阈值标准）——待核实。

#标签/PM决策层/AI产品需求 #标签/需求工程 #标签/Agent
