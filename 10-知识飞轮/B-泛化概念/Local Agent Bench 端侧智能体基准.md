---
type: concept
status: draft
derived_from: "[[OS PM 近一月情报简报 2026-07-31]]"
tags:
  - 端侧LLM
  - 评测
  - AgentBench
  - 基准
---

# Local Agent Bench 端侧智能体基准

> 全新概念（2026-07 检索新增）。聚焦"端到端智能体"而非单点 Function Calling 的评测基准。单点路由评测见 [[Function Calling 端侧工具调用]]；方法学见 [[系统级 Intent 路由评估 SOP]]。

## 一句话定义

**Local Agent Bench** 是在**端侧/本地模型**上跑的**端到端智能体基准**：不只测"选对工具+填对槽"，而是测模型在真实多步任务（规划→调用→观察→再行动）上的整体完成度，是端侧 Planner 从"能路由"走向"能办事"的关键标尺。

## 为什么重要

- **补齐 BFCL 的单点视角**：BFCL 主要测 Tool Choice/参数抽取；Local Agent Bench 测端到端任务成功率，更贴近"Agent 真能把事办成"。
- **小模型端侧可行性的证据**：Round 3 中 **qwen3:1.7b 登顶（得分 0.960）**，说明 1.7B 级模型在端侧已能跑通完整 Agent 循环；functiongemma 以 0.640 / 435ms 展现"小且快"的定位。

## 适用边界

- 基准随版本迭代（Round 3 数据，后续轮次可能变化），引用需标注轮次。
- 与 BFCL 互补：BFCL 看"调用正确性"，Local Agent Bench 看"任务完成度"，二者都应进评估 SOP。

## 证据与例子

- **Local Agent Bench Round 3**（来源 URL 待回填，2026-07 检索）：
  - `qwen3:1.7b` — **#1，得分 0.960**
  - `functiongemma` — **0.640，延迟 435ms**
- 解读：端侧小模型在"端到端 Agent"上已出现可用选手（qwen3:1.7b），但 functiongemma 等 270M 级模型更偏"快路由/分流"而非"重任务"，与 [[Function Calling 端侧工具调用]] 中 58%→85% 的窄域定位一致。

## 可复用启发

- 端侧 Agent 评估应**双轨并行**：BFCL（调用正确性）+ Local Agent Bench（任务完成度），见 [[系统级 Intent 路由评估 SOP]]。
- 选型参考：需要"端到端办事"优先 qwen3:1.7b 级；需要"毫秒级路由/分流"优先 FunctionGemma 级。

## 2026-08-04 增补：BFCL v4 把「端到端 agentic」并入自身，本节点的定位需重述（来源 [[AppIntent 每日情报 2026-08-04]]）

**发生了什么**：BFCL v4 把权重重排为 **Agentic 40% / Multi-Turn 30% / Live 10% / Non-Live 10% / Hallucination 10%**——经典单轮 function calling 只剩 20%。

**对本节点的直接影响（重要，避免以后误用）**：

- 本节点开头写的「补齐 BFCL 的单点视角」**是 v3 时代的判断**。BFCL **v4 已经自己把 70% 权重放到 agentic + multi-turn 上**，与 Local Agent Bench 的定位高度重叠。
- **修正后的分工**：
  - **BFCL v4** = 标准化、AST 可复现、有 Hallucination（abstention）子集的**通用 agentic 评测**——适合横向比模型。
  - **Local Agent Bench** = 端侧本地跑、贴近真实设备算力与延迟的**端到端完成度评测**——适合验证「这台机器上跑不跑得动」。
  - 二者仍应并行，但**理由从「补单点视角」变成「补部署真实性」**。
- **新增该看的一栏**：BFCL v4 的 **Hallucination（10%）测「没有合适工具时正确地不调用」**——这是 Local Agent Bench 现有 Round 3 数据里**没有覆盖**的维度，而它恰是意图 Registry 规模变大后最关键的失败模式。建议自建端侧回归集时补上「空 Registry / 无匹配意图」用例。
- ⚠️ **本节点旧数据的版本标注**：`qwen3:1.7b` 0.960、`functiongemma` 0.640/435ms 为 **Local Agent Bench Round 3**（2026-07 检索，来源 URL 仍**待回填**），与任何 BFCL 分数**不同量纲、不可换算**。

## 关联

- 来源：[[OS PM 近一月情报简报 2026-07-31]] ｜ [[AppIntent 每日情报 2026-08-04]]
- 单点评测：[[Function Calling 端侧工具调用]]
- 方法：[[系统级 Intent 路由评估 SOP]]

#标签/端侧LLM #标签/评测 #标签/AgentBench
