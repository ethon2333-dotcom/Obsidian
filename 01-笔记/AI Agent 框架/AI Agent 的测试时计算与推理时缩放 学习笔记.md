---
title: AI Agent 的测试时计算与推理时缩放 学习笔记
tags: [agent-framework, test-time-compute, inference-time-scaling, reasoning, scaling, LLM, 推理]
created: 2026-11-04
source:
  - https://arxiv.org/abs/2408.03314
  - https://arxiv.org/abs/2502.12215
  - https://arxiv.org/abs/2506.12928
  - https://aclanthology.org/2025.emnlp-main.276/
  - https://arxiv.org/abs/2501.05366
  - https://arxiv.org/pdf/2510.08049
---

# AI Agent 的测试时计算与推理时缩放 学习笔记

> [!info] 🌱 广度种子
> 一句话心智模型：**与其把"聪明"全押在训练时堆参数，不如在推理时给模型更多"思考预算"——长链推理、搜索、采样投票、验证器循环，都是花更多计算换更高质量的同一种范式；而一个会调工具、会自我反思的多步 Agent，本质上就是一团被显式展开的 test-time compute。**

刻意区别于（只做轻度交叉链接，不重复）：[[服务端 LLM 推理引擎生态 学习笔记]]（serving 引擎侧如何实现长推理吞吐）、[[Context Engineering 学习笔记]]（上下文如何组装，本篇关注"算多久 / 怎么算"）、[[端侧大模型推理 学习笔记]]（端侧推理原理，本篇关注推理期计算分配范式）、[[多智能体协作与编排 学习笔记]]（多 agent 编排模式，本篇聚焦"计算即推理"的视角）。

## 1. 定义与心智模型

**Test-time compute / inference-time scaling（测试时计算 / 推理时缩放）**：在**推理阶段**（而非训练阶段）投入更多计算来提升输出质量。核心洞察（Snell et al., 2024，Google DeepMind + UC Berkeley，arXiv:2408.03314）：在匹配计算量下，一个**更小的模型 + 更多推理计算**可以胜过参数多 14× 的模型，效率提升约 **4×（待核实口径）**。

这是继"训练时缩放（pretraining scaling）"之后第二条独立的进步轴。二者是**互补**而非替代：强基座 + 推理期长思考 > 仅用其一。

## 2. 主流方案分类（广度地图）

| 类别 | 机制 | 代表方法 | 适用场景 |
|---|---|---|---|
| 顺序缩放 Sequential | 生成超长内部思维链，逐步推导 / 自我修正 | o1/o3、DeepSeek-R1、Gemini 推理、Claude Thinking 的长思考 | 数学 / 代码 / 科学 / 逻辑多步题 |
| 并行缩放 Parallel | 生成 N 个候选，投票或验证器选优 | Self-consistency（多数投票）、Best-of-N | 易 / 中难度，有一猜即中的可能 |
| 搜索缩放 Search | 借经典搜索分支探索解空间，剪枝弱路径 | Tree-of-Thoughts、MCTS、Beam Search、DVTS | 中高难度，需探索 |
| 验证器循环 Verifier-in-the-loop | 生成→验证→再生，步级打分 | PRM 引导的 beam / MCTS、Revision Chain、Self-Refine | 长程任务、需过程监督 |

### 关键概念

- **Process Reward Model (PRM)**：对**每一步**推理打分（过程监督），vs **Outcome Reward Model (ORM)**：只给最终答案打分。PRM 可在推理期做 early pruning。
- **Best-of-N**：抽样 N 个完整答案，取验证器最高分者；pass@N 随 N 近似 log-linear 提升（Brown et al., 2024）。
- **Self-consistency**：多条推理链多数投票，无需训练验证器。
- **Verifier-in-the-loop**：生成→critic 验证→若错则重生，是 o1 类模型的隐性机制。
- **Compute-optimal allocation**：按题目**难度自适应**分配计算——易题用广度（BoN），难题用深度（迭代修正 / 树搜索）。这是 4× 效率增益的来源。

## 3. 2025-2026 进展（广度速览）

| 主题 | 进展要点 | 待核实 / 注意 |
|---|---|---|
| 基础范式确立 | o1（2024-09）首发长思考；o3（2025）"想得更狠而非更久"——把思考 token 花在真正难处；DeepSeek-R1（2025 初）开源复现，以更低推理成本逼近 o1 | 各厂商 token / 价格口径不一 |
| 计算最优缩放 | Snell 2024 提出 compute-optimal；Liu et al. 2025《Can 1B surpass 405B》把 PRM + 搜索策略纳入优化，3B 在 MATH-500 超 405B | 数字来自论文设定，非通用保证 |
| 过程奖励模型 | PRM 综述（arXiv:2510.08049）梳理从重排器→生成式验证器（GenPRM / ThinkPRM）→搜索集成→自适应步级 | PRM 分布偏移（distribution shift）会选错短答案 |
| 过度思考 Overthinking | 2025-2026 研究发现：对**易题 / 开放题**长思考反而降级或浪费；在不可验证任务上缩放不可靠（arXiv:2502.12215：可验证任务强缩放成立，非可验证任务 erratic / inverts） | "overthinking" 具体阈值暂无统一结论 |
| Agent = Test-time Compute | OPPO《Scaling Test-time Compute for LLM Agents》(arXiv:2506.12928) 首篇系统探索：并行采样 / 序列修正 / 验证器与合并 / 多样 rollout 四类。**list-wise 合并优于打分**；"何时反思"比"每步反思"重要（分数触发的选择性反思）；多模型混合在 GAIA 上达 **74.55（待核实）** | Agent 多步误差累积，naive BoN 易翻车 |
| 检索即计算 Search-as-compute | Search-o1（EMNLP 2025, arXiv:2501.05366）把 agentic RAG 嵌进推理链：遇知识不确定点动态检索 + Reason-in-Documents 精炼后回注，缓解 LRM 知识不足 | 检索噪声需专门模块消化 |
| 软件工程 Agent | SWE-Reasoner（2025）内部 + 外部 TTC，32B 在 SWE-bench Verified 达 46%（待核实）超 R1 671B | 环境延迟主导成本，深度优先更划算 |

## 4. 代表产品与模型

| 模型 / 产品 | 厂商 | 长思考机制 | 备注 |
|---|---|---|---|
| o1 / o3 | OpenAI | 隐藏 CoT + RL，o3 加工具调用 / 更高预算 | 单 query 可耗 10–100× token（待核实） |
| DeepSeek-R1 | DeepSeek | 开源 GRPO 式 RL 长链推理 | 推理成本显著低于 o1 口径 |
| Gemini 推理 / Claude Thinking | Google / Anthropic | 推理调优长思考 | 各厂"思考预算"参数 |
| QwQ / Qwen-Math-PRM | 阿里 | 开源推理 + PRM | Search-o1 以 QwQ-32B 为骨干 |
| Kimi k1.5 | Moonshot | 长上下文 + RL 纯 test-time scaling | 2025 |

## 5. 与 Agent 视角的咬合

- **Agent 本身就是 test-time compute**：多步循环（观察→思考→行动→工具调用）等于把"思考预算"显式展开成轨迹；rollout 多样性、反思、验证器合并都是 TTS 在 agentic 设定下的翻版。
- 与 [[多智能体协作与编排 学习笔记]]：多 agent 协作采样（不同 inductive bias）本质是多模型 Pass@K 的多样性来源。
- 与 [[服务端 LLM 推理引擎生态 学习笔记]]：长思考把每 query 的 token / 延迟 / 成本拉高一个数量级，serving 层（KV cache、batching、prefix sharing）必须为此重新设计。
- 与 [[端侧大模型推理 学习笔记]]：端侧算力紧缺，test-time compute 的"算得更久"与端侧延迟 / 能耗硬约束直接冲突，是端侧推理性价比的核心张力。
- 与 [[Context Engineering 学习笔记]]：长思考链 / 检索回注 / 验证轨迹，最终都要落到"给模型喂什么上下文"，二者在工程上汇合。

## 6. 待解问题（留给 Ethon 深挖，BREADTH 盲区）

- [ ] PRM 的分布偏移（distribution shift）如何在生产环境量化与缓解？离线 PRM 在 in-domain 外为何会奖赏"短错答案"？
- [ ] "计算最优分配"在真实 Agent 任务（非 MATH）上如何做难度预估？是否需要单独的 difficulty estimator？
- [ ] o3 "thinks harder not longer" 的具体机制（RL 奖励塑形？）公开资料到哪一步？——**待核实**
- [ ] 不可验证任务（开放写作 / 创意）上 test-time scaling 不可靠，那么 agentic 长程任务的"可验证性"如何人造（reward hacking 风险）？
- [ ] Search-o1 的 Reason-in-Documents 与 [[Context Engineering 学习笔记]] 的"检索裁剪"是否同一件事？值得对照。
- [ ] 端侧能否跑"轻量 PRM + 短思考"的 test-time compute 折中？与 [[端侧大模型推理 学习笔记]] 的量化 / 蒸馏如何配合？

## 附：来源清单

1. Snell, Lee, Xu, Kumar (2024). *Scaling LLM Test-Time Compute Optimally Can Be More Effective Than Scaling Model Parameters*. arXiv:2408.03314. https://arxiv.org/abs/2408.03314
2. *Revisiting the Test-Time Scaling of o1-like Models* (2025-02). arXiv:2502.12215. https://arxiv.org/abs/2502.12215
3. OPPO AI Agent Team (2025-06). *Scaling Test-time Compute for LLM Agents*. arXiv:2506.12928. https://arxiv.org/abs/2506.12928
4. Li et al. (EMNLP 2025). *Search-o1: Agentic Search-Enhanced Large Reasoning Models*. https://aclanthology.org/2025.emnlp-main.276/ （arXiv:2501.05366 https://arxiv.org/abs/2501.05366）
5. *A Survey of Process Reward Models* (2025-10). arXiv:2510.08049. https://arxiv.org/pdf/2510.08049
6. Liu et al. (2025). *Can 1B LLM Surpass 405B LLM? Rethinking Compute-Optimal Test-Time Scaling*. https://papers.lunadong.com/paper/16715
7. 综合科普 / 口径交叉验证：OpenAI o1/o3 释义、test-time compute 综述（aiwiki）、teachaitools 2026 综述、long-horizon agent survey。

## ⚠️ 待核实清单

- o1/o3 单 query 10–100× token、o1 比 GPT-4 贵 5–10× 等**具体倍数**为媒体 / 厂商口径，未统一，标"待核实"。
- OPPO 混合模型在 GAIA 的 **74.55** 分数来自单篇论文设定，需复核基准版本。
- SWE-Reasoner 32B 在 SWE-bench Verified 的 **46%** 来自论文摘要，需复核。
- Snell 的 **4× 效率 / 14× 参数**对比为论文设定（easy / medium 题、特定基座），非通用保证。
- o3 "thinks harder not longer" 的**内部机制**公开资料有限，未深究。
- "overthinking / ACL 2026" 论文的具体结论（阈值、任务类型边界）未在本文展开，留待深挖。

#标签/AIAgent框架/推理时计算/推理缩放
