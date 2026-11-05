---
title: 开发者态 Agent 评测与 CI 集成 学习笔记
tags:
  - AI Agent
  - 评测
  - Eval
  - CI
  - 效率工具
created: 2026-10-17
source: 综合联网检索（LangSmith / Braintrust / Promptfoo / DeepEval / Giskard / RAGAS / MLflow 等官方与第三方资料，详见文末来源清单）
---

# 开发者态 Agent 评测与 CI 集成 学习笔记

> 心智模型：把"Agent 能力评测"从一次性人工演示，变成**可版本化、可重复、可阻断合并的工程活动（Eval-as-Code / Eval in CI）**——评测集与阈值像代码一样进仓库、进流水线、进门禁。

---

## 1. 定义：什么是「开发者态 Agent 评测」

「开发者态 Agent 评测」指把 Agent 的能力验证前移到开发与合并阶段，使之成为开发者日常可触发的活动：

- **Eval-as-Code**：评测集（golden set）、断言、评分器（scorer）、门禁阈值都以代码/配置形式入库，随 PR 一起评审与演进。
- **Eval in CI**：每次 push / PR 自动跑评测套件，分数不达标即阻断合并（quality gate / regression gate）。
- 与「线上监控」互补：开发者态关注"我这次改动是否让已知能力退化"，线上态关注"真实流量里出现了什么没测到的行为"。

延伸阅读：[[Agent 评测与基准 学习笔记]]、[[Agent 评测自动化与 LLM-as-judge 工程 学习笔记]]。

---

## 2. 分类维度（点到为止）

| 分类轴 | 子类 | 一句话说明 |
| --- | --- | --- |
| 评测时机 | 离线评测（offline eval） | 在 CI / staging 跑固定 golden set，可重复、可阻断 |
| | 在线监控（online monitoring） | 对生产抽样流量异步打分、告警、回收新用例 |
| 评测对象 | 轨迹 / 工具调用评测 | 断言"调了哪个工具、参数对不对、顺序对不对" |
| | 端到端任务评测 | 只看任务是否完成、答案是否正确（含工具最终产出） |
| 写法形态 | 单元测试式（pytest 风格） | 每个 case 一个断言，pass/fail 直接出门禁（DeepEval / Promptfoo） |
| | 端到端式（dataset 级） | 跑一整个数据集再算聚合分，偏看板（RAGAS） |
| 承载形态 | 代码化评测 | 库 + 配置文件，贴着应用代码走（Promptfoo / DeepEval） |
| | 平台式评测 | 托管 UI + 数据集 + 在线打分 + PR 评论（LangSmith / Braintrust） |

> 实践共识（2025-2026）：**"DeepEval for gates, RAGAS for dashboards"**；代码化套件负责门禁，平台负责协作与趋势看板。

---

## 3. 主流方案与工具

| 工具 / 平台 | 类型 | 核心定位 | 与 CI 的关系 | 备注 |
| --- | --- | --- | --- | --- |
| **LangSmith / LangSmith Eval / CI** | 托管平台（LangChain 系） | 链路追踪 + 评测 + 提示词管理一体化 | 原生 GitHub Actions，可依据回归阻断 PR；支持轨迹级 LLM-as-judge | LangChain/LangGraph 用户首选；非 LangChain 栈也可用 `@traceable` |
| **Braintrust** | 托管平台 | 评测 + 在线打分 + 数据集 + CI 门禁 + Loop 改进 | `braintrustdata/eval-action` 跑评测并贴 PR 评论，阈值可阻断合并 | 多 trials 测一致性；生产 trace 一键转回归用例 |
| **Promptfoo** | 开源 CLI（MIT） | YAML 驱动的 prompt 扫描 + 评测 + 红队 | 原生 GitHub Action，回归即 fail build | 红队/安全测试最强（142 个 OWASP 系插件）；本地优先、可自托管 |
| **Giskard** | 开源库（Apache-2.0） | AI 风险扫描 + 红队发现 + RAG 测试集生成 | 适合"周期性/发版扫描"，非逐 PR 轻量门禁 | 偏"发现未知漏洞"，与 DeepEval 互补 |
| **DeepEval** | 开源库（Apache-2.0） | pytest 风格 LLM 评测，14+ 指标 | `deepeval test run` pytest 原生出门禁 | 阈值断言式、CI 最顺手；可选 Confident AI 托管看板 |
| **RAGAS** | 开源库 | RAG 指标（faithfulness / contextual precision…） | 不原生出 pass/fail 退出码，CI 需自行加断言 | 数据集级评分 + pandas，适合检索调参看板 |
| **AgentEval** | 框架/方法（微软系） | 面向 Agent 任务完成度与步骤评测 | 以代码/数据集形式跑，可接 CI | 具体形态与最新版本待核实 |
| **Weights & Biases Weave** | 托管平台 | 追踪 + 评测 + 实验对比 | 可接 CI 跑评测并记录实验 | 与 W&B 实验生态联动 |
| **Helicone** | 代理式可观测 | 零代码改动插在 App 与 LLM API 之间，做成本/延迟/缓存观测 | 偏生产可观测，CI 评测非主职 | 适合"最少改动接入观测"的团队 |
| **CI 集成层** | GitHub Actions / GitLab CI | 触发器（PR / push / 定时）+ 跑 eval suite + 失败阻断 | 所有上述工具的最终执行载体 | 回归门禁（regression threshold）已成为 2026 默认范式 |

> 关联：[[AI Agent 评测的对抗鲁棒性持续监控 学习笔记]]（Giskard / Promptfoo 红队与对抗鲁棒性部分）、[[AI 编程助手与 Agentic Coding 工具生态 学习笔记]]（评测与 coding agent 工程化衔接）。

---

## 4. 2025-2026 进展（广度速览）

| 进展点 | 含义 | 状态 |
| --- | --- | --- |
| eval 套件代码化 | 评测集、断言、scorer、阈值进仓库，与 PR 同评审 | 已成主流实践 |
| 回归测试门禁 | 不以固定分数线，而以"相对 main 基线下降 X%"阻断合并（默认约 3% 下降为常见起点，待核实） | 2026 默认范式 |
| LLM-as-judge 进 CI | 用独立强模型按 rubric 给开放式输出打分，进流水线 | 广泛落地，但需校准 |
| 对抗鲁棒性纳入流水线 | prompt injection / jailbreak / 数据泄露扫描进 CI 或发版门禁 | 安全敏感团队标配 |
| 评测集版本管理 | 数据集带版本/快照/标签，git 元数据关联实验，支持"生产 trace→回归用例"回流 | 平台式工具已支持 |
| 多 trials + 方差报告 | 非确定性 Agent 每 case 跑多次，报均值与方差而非单点 | 成熟团队实践 |
| 三层评测栈 | 断言单测（每 PR）+ LLM-as-judge（golden trace）+ 异步线上打分（5–10% 抽样） | 2026 推荐模板（默认值待核实） |

> 关联：[[Agent 评测自动化与 LLM-as-judge 工程 学习笔记]]（judge 校准、自偏好偏差、rubric 工程）、[[AI 编程的上下文工程与代码检索增强 学习笔记]]（RAG 评测指标衔接）。

---

## 5. 代表产品 / 平台横向对比

| 维度 | Promptfoo | Braintrust | LangSmith | DeepEval | RAGAS | Giskard |
| --- | --- | --- | --- | --- | --- | --- |
| 开源 | ✅ MIT | ❌ SaaS | ❌（有限免费层） | ✅ Apache-2.0 | ✅ | ✅ Apache-2.0 |
| 主职 | 发门前评测+红队 | 发门后观测+评测+门禁 | LangChain 系追踪+评测 | pytest 风格门禁 | RAG 指标看板 | 风险扫描/红队发现 |
| CI 门禁 | ✅ 原生 GH Action | ✅ 原生 GH Action + PR 评论 | ✅ 原生 Action | ✅ pytest 原生 | ⚠️ 需自写断言 | ⚠️ 偏周期扫描 |
| 红队/安全 | ✅ 最强（OWASP 系插件） | ⚠️ 自定义 scorer | ⚠️ 有限 | ✅ 有 | ❌ | ✅ 扫描式 |
| 生产可观测 | ❌ | ✅ 在线打分 | ✅ | ⚠️ 经 Confident AI | ❌ | ⚠️ Hub 企业版 |
| 自托管 | ✅ 完全 | ⚠️ 企业混合 | ❌ | ✅ | ✅ | ✅ |
| 非 LangChain 友好 | ✅ 通用 | ✅ 框架无关 | ⚠️ 深度绑定 LangChain | ✅ | ✅ | ✅ |

> 选购 heuristic（2026 口径）：**"Promptfoo 进 CI + 一个可观测平台（LangSmith / Braintrust / Langfuse）"** 是两件套默认组合；Giskard 负责发现、DeepEval 负责回归关门。

---

## 6. 深度盲区：待解问题

- [ ] 待解问题：**非确定性 Agent 如何用断言**——同一输入多次运行轨迹/答案不同，门禁该用硬阈值、均值阈值、还是方差容忍带？
- [ ] 待解问题：**评测集漂移治理**——golden set 长期不更新会"被刷分（eval saturation）"，如何周期性从生产轨迹抽新 case、淘汰失效 case？
- [ ] 待解问题：**CI 成本与耗时权衡**——LLM-as-judge 每 case 多次调用，全套跑完可能超时；PR 子集 smoke run vs 合并后全量 run 的切分点如何定？
- [ ] 待解问题：**门禁阈值设定**——相对基线下降 3% 是经验值，业务不同是否应有差异化 cutoff？谁来拍板"发布红线"？
- [ ] 待解问题：**LLM-as-judge 自偏好与漂移**——生成模型与判定模型同族会引入偏差；judge 模型升级后历史分数不可比，如何做校准集（calibration set）常态化重跑？

---

## 附：来源清单

1. LangChain 官方 / 示例仓库：Continuous evaluation pipeline for LLM agents (LangSmith + GitHub Actions) — https://github.com/langchain-samples/offline-evals-cicd
2. Braintrust 官方：How to test AI agents（回归测试、CI 门禁、生产监控）— https://braintrust.dev/articles/how-to-test-ai-agents
3. Promptfoo vs Braintrust vs LangSmith 2026 对比（含定价、CI、红队）— https://bearplex.com/compare/promptfoo-vs-braintrust-vs-langsmith
4. MLflow：AI Agent Evaluations: A Developer's Practical Guide（回归门禁、judge 校准）— https://mlflow.org/articles/tags/agent-performance-assessment/
5. DeepEval vs Giskard 2026（pytest 门禁 vs 风险扫描）— https://aicoolies.com/comparisons/deepeval-vs-giskard
6. Continuous LLM Evaluation in Production: 7 Patterns, Costs, and Gates (2026) — https://genalphai.com/continuous-llm-evaluation-in-production-7-patterns
7. Maxim：The 5 Leading Platforms for AI Agent Evals in 2025 — https://getmaxim.ai/articles/the-5-leading-platforms-for-ai-agent-evals-in-2025/

---

## ⚠️ 待核实清单

- **Promptfoo 被 OpenAI 收购（2026-03-09 宣布，承诺保持开源与模型无关）**：仅见于单一对比站（bearplex），未见官方一手确认，**待核实**。
- **LangChain / LangGraph 于 2025-10 达到稳定 1.0**：来自对比站口径，**待核实**版本号与时间。
- **GAIA 2026 年 SOTA Agent 约 55–60%、GPT-4o 在 Level 2 约 36%（2025）**：基准数字来自社区博文，**未定数字，待核实**。
- **SWE-bench Verified 上 Claude Sonnet 4 + 脚手架约 49%**：社区口径，**待核实**。
- **2026 默认工程参数**（回归门禁约 3% 下降、judge 与人类一致性 85–90% 下限、线上抽样 5–10%、canary 窗口 48–72h）：均为"实践建议/起点值"，**非标准，需按自身业务校准，待核实**。
- **Star 数（DeepEval ~16K、Giskard ~5.4K）与用户数（Promptfoo 30 万+）**：随时间变动，**未定数字，待核实**。
- **AgentEval 最新形态与版本、W&B Weave / Helicone 的 CI 评测具体集成方式**：未做一手深挖，**细节待核实**。

---

## 关联笔记

- [[Agent 评测与基准 学习笔记]]
- [[Agent 评测自动化与 LLM-as-judge 工程 学习笔记]]
- [[AI Agent 评测的对抗鲁棒性持续监控 学习笔记]]
- [[AI 编程的上下文工程与代码检索增强 学习笔记]]
- [[AI 编程助手与 Agentic Coding 工具生态 学习笔记]]

#标签/AI Agent 框架 #标签/评测 #标签/CI #标签/效率工具
