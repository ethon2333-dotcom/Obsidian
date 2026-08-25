---
type: concept
status: draft
derived_from: "[[AppIntent 跨平台情报简报 2026-07-30]]"
tags: [AppIntent, FunctionCalling, 端侧Planner, 评测, 概念]
aliases: [端侧工具调用]
---

# Function Calling 端侧工具调用

> 含「端侧 Planner 模型横向评测表」（2026-07-30 实测）。未实测模型标注「待补」，不臆造数据。

## 一句话定义

**端侧 Function Calling** 是在设备本地用小模型 Planner 完成「Tool Choice（选哪个工具）+ 参数抽取（填槽）」的能力，让意图路由零单查询成本、毫秒级响应。

## 为什么重要

- 实测证明「小模型 + 单应用 Schema 微调」即可在端侧达到可用路由准确率，是压低延迟/成本的关键。
- 与云端大模型形成「本地优先 + 低置信升级」的混合架构。

## 适用边界

- 端侧模型适合窄域 / 单应用 Schema；跨域、多轮、低置信需升级云端。
- 设备算力约束（NPU/内存）决定可跑模型规模（见 [[OS-PM-3B模型内存预算推演]] 相关思路）。

## 证据与例子：端侧 Planner 模型横向评测（2026-07-30）

| 模型 | 规模 | 策略 | 关键指标（实测） | 定位 |
|------|------|------|-----------------|------|
| **FunctionGemma 270M** | 270M | 单应用 Tool Schema 微调 + LiteRT-LM | Mobile Actions 微调 **base 58% → 85%**；BFCL Simple 61.6 / Parallel 39（详见下方 2026-07 增补） | 端侧 Planner（主路由） |
| **qwen3-0.6b-tool-router** | 0.6B | 禁 CoT + 严格 JSON，确定性 edge router | BFCL Multi-Turn Base **90.42%**；Relevance **90.89%** | 确定性边缘路由 |
| **Qwen3-Embedding-0.6B** | 0.6B | 语义缓存学习环 | 降低云端依赖（高频意图留端侧） | 语义缓存 |
| **Gemma 4（QAT）** | E2B / 26B-A4B | QAT 量化 + LiteRT-LM | 内存 **-72%**、质量与 FP16 差数点；**E2B <1GB**（移动格式）；26B-A4B 可上 16GB 笔记本（2026-06-05） | 端侧通用底座（**BFCL 路由分待补**） |
| **Qwen3-Coder-Next** | 80B-A3B | 大规模 agentic RL | SWE-bench Verified **>70%**（SWE-Agent, 2026-03-03）；3B 激活 | ⚠️**编码智能体，非端侧路由**，不可混用 |
| **IBM Granite 4.1** | 8B / 30B-A9B | Mamba 混合，低 KV-cache | **BFCL-v3：8B 68.27% / 30B 73.68%**；Nano 350M/1B 面向受限边缘 | 商用友好边缘 Agent（Apache-2.0） |
| **Phi-4-mini** | 3.8B | 原生 tool template | BFCL v4 **低到中 80 分段**（第三方 ertas 2026-05，**非 Berkeley 官方行**） | MIT 许可的端侧单选 |

> 说明：Gemma 4 / Qwen3-Coder-Next 两项**待补已于 2026-07-31 回填**（来源 [[AppIntent 每日情报 2026-07-31]]）。注意 Gemma 4 目前只有内存/体积数据，**BFCL 路由准确率仍待补**；Qwen3-Coder-Next 是编码基准，**不能当作意图路由证据引用**。

### 2026-07 增补（官方实测，来源 [[OS PM 近一月情报简报 2026-07-31]]）

- **FunctionGemma 官方 BFCL（零样本）**：Simple 61.6 / Multiple 63.5 / Parallel 39 / Parallel-Multiple 29.5 / Live-Simple 36.2 / Live-Multiple 25.7 / Live-Parallel 22.9 / Live-Parallel-Multiple 20.8 / Relevance 61.1 / Irrelevance 73.7。并行/多函数组合场景显著下滑 → 官方强调"必须微调"。
- **S25 Ultra 实测（dynamic_int8, CPU LiteRT XNNPACK 4 线程, ctx 1024）**：Mobile Actions 微调 prefill **1718 tok/s**、decode **125.9 tok/s**、TTFT **0.3s**、模型 **288MB**、峰值 RSS **551MB**。
- **Local Agent Bench Round 3**：qwen3:1.7b **#1（0.960）**、functiongemma **0.640（435ms）** → 详见 [[Local Agent Bench 端侧智能体基准]]。
- **口径说明**：早期简报记 FunctionGemma "46%→90%"（基准未注明），与 Google 官方 "base 58% → Mobile Actions 微调 85%" 口径不同；以 **官方 58%→85%** 为准。

### 2026-07-31 增补：端侧规模边界与口径纪律（来源 [[AppIntent 每日情报 2026-07-31]]）

**A. TinyLLM 全量 BFCL 对照（arXiv 2511.22138，通用 Prompt/FC 模式，未做窄域微调）**

| 模型 | Overall | Live | Non-live | **Multi-turn** |
|---|---|---|---|---|
| xLAM-2-3b-fc-r (FC) | **65.74%** | 81.03% | 88.22% | **55.62%** |
| Qwen3-4B (Prompt) | 62.04% | 75.52% | 82.58% | 35.25% |
| Qwen3-1.7B (Prompt) | 55.49% | 63.48% | 80.03% | 16.88% |
| xLAM-2-1b-fc-r (FC) | 53.97% | 61.57% | 72.42% | 8.38% |
| **Qwen3-0.6B (Prompt)** | 45.76% | 58.86% | 67.78% | **1.38%** |
| TinyLlama-1.1B / TinyAgent-1.1B | ~19.7% | ~39% | 20.00% | 0.00% |

**规模边界结论**：BFCL 上 **1–3B 是端侧单轮工具调用的甜点区**；**<1B 在 multi-turn / parallel / nested 上可靠失败**，只适合抽取与分类，**不要拿去跑 Agent 循环**。7–20B 经微调可追平闭源（如 ToolACE-8B）。

**B. 🔴 关键口径冲突（必须记住，否则会误判选型）**

本表「Qwen3-0.6B（Prompt）Multi-turn **1.38%**」与上表「qwen3-0.6b-**tool-router** BFCL Multi-Turn Base **90.42%**」**并不矛盾，但绝不可互换引用**：

| | qwen3-0.6b-tool-router | Qwen3-0.6B (Prompt) |
|---|---|---|
| 是否微调 | **窄域 N 工具微调** | 否，原始 prompt |
| 输出约束 | 禁 CoT + **严格 JSON** | 自由生成 |
| 评测子集 | **Multi-Turn Base**（子集） | 全量 multi-turn |
| 结果 | 90.42% | 1.38% |

→ **结论：<1B 模型只有在「窄域 + 微调 + 严格约束输出」三条件同时满足时，才可承担端侧主路由；任一条件缺失即退回 1.7–3B。**

**C. ⚠️ 基准污染警示（prism-coder 系列）**

prism-coder 8b/14b/32b 宣称「**BFCL 100%**」，实为**自建 6-tool 路由基准**（102 用例 × 3 seed，12 个自定义类别），**不是 Berkeley 官方 BFCL**，不可与官方分数并列。引用第三方模型卡的 BFCL 数字前，先确认是官方榜单行还是自建同名基准。

其**真正可借鉴处是级联结构**（与本笔记「本地优先 + 低置信升级」一致，且给出了流量分布实测）：

- 级联 14b → 32b → Claude Opus：**14b 承担 99% 流量**，1% 升级 32b，**0% 打到云端**；
- 级联整体准确率 100.0% vs Opus-solo 98.3%（**在其自建基准上**）；
- 启示：**衡量端侧路由成功与否的核心指标不是准确率，而是「云端逃逸率」**——本地承接比例越高，成本与延迟优势才成立。

## 可复用启发

- 选型顺序：先小模型本地路由（FunctionGemma 类）→ 低置信升级云端 → 语义缓存吸收高频。
- **把「云端逃逸率」列为一等指标**：本地承接率 / 升级率 / 上云率，与准确率并列上报。
- **引用外部 BFCL 数字必须三问**：官方榜单还是自建同名基准？微调还是零样本？全量还是子集？（本笔记已因此校准过两次口径）
- 评估必须上 BFCL / 内部 benchmark，记录准确率、参数抽取 F1、延迟、tok/s（见 [[系统级 Intent 路由评估 SOP]]）。

### 2026-08-01 增补：Needle 26M 与「无 FFN」架构（来源 [[AppIntent 每日情报 2026-08-01]]）

- **Needle（Cactus Compute，GitHub 提交 2026-05-12~16，7 月底经聚合媒体二次扩散）**：从 **Gemini 3.1 Flash Lite 蒸馏**出的 **26M 参数** 单次函数调用模型，**MIT 全开源**；INT4 量化后 **仅 14MB**，可放进桌面 CPU 的 L3 缓存。
- **Simple Attention Network（SAN）架构**：整个模型**没有任何 MLP/FFN 层**，只有注意力与门控——编码器 **12 层（无 FFN）** + 解码器 **8 层**；`d=512`、8 头/4 KV 头（GQA）、BPE 词表 8192、RoPE、编码器与输出投影共享嵌入；一个 **CLIP 式对比学习工具选择头**先从大工具集筛出相关工具；去掉 MLP 砍掉约 **2/3 参数量**。详见 [[Simple Attention Network 无FFN端侧路由]]。
- **设计论断（对 OS PM 最关键的一句）**：**「工具调用本质是检索与组装，不是推理」**——事实已在输入里（工具 schema 就在 prompt 中），模型不需要用 FFN 权重记忆世界知识。该结论据称可推广到任何「模型能访问外部结构化知识」的任务（RAG、检索增强生成），实验结果将随后发表（待补）。
- **性能**：**6000 tok/s prefill、1200 tok/s decode**；单次函数调用**优于 FunctionGemma-270M、Qwen-0.6B、Granite-350M、LFM2.5-350M**（这些模型大一个数量级）。训练：预训练 200B token / 16×TPU v6e / 27h；后训练 2B token 合成 FC 数据 / 45min。
- **🔴 口径纪律（延续本库规矩）**：上述对比为 **Cactus 自述、single-shot 场景，非官方 BFCL 榜单行**，不可与 BFCL 分数并列（具体测试集与数值待补）；团队自认更大模型在对话场景 scope/capacity 更强，Needle 是窄域专才，「小模型会挑食（finicky）」，建议在自有工具集实测并微调。**「无 FFN」仅论证 single-shot 路由；多轮 / 多工具串行编排由云端大模型承担。**

## 2026-08-03 增补：LFM2.5-8B-A1B + LocalCowork 端侧 Agent 循环齐备样本（来源 [[AppIntent 每日情报 2026-08-03]]）

> 库内评测表此前止于 TinyLLM/BFCL 与 Needle 26M，**缺「端侧模型真的跑完整 Agent 循环」落地样本**。本条补齐。

- **LFM2.5-8B-A1B（Liquid AI，2026-05-28）规格**：8.3B 总参 / **1.5B 激活**（MoE）；128K 上下文；词表 128K；预训练 38T tokens + 大规模 RL；reasoning-only 模式。
- **📊 分数（厂商自述 / 第三方转载，未复现）**：**BFCLv3 64.36**、**IFEval 91.84**、**Tau2 Telecom 13.60 → 88.07**；AIME25 42.53（推理深度是短板）。速度：M5 Max 253 tok/s、Ryzen AI Max+ 395 146 tok/s、内存 <6GB、手机约 30 tok/s。
- **🔑 LocalCowork 实证（本条真正价值）**：开源桌面 Agent demo 在**一台笔记本**上跑 **13 个 MCP server 的 67 个工具**，**无云、无 API key、数据不出机**，循环 `ask-propose-confirm-run`、**每次 dispatch 远低于 1 秒**、保有**完整审计轨迹**。首次拿到「端侧 Planner + 数十工具 + 确认环 + 审计日志」齐备样本，同时回答两问题：(a) 67 工具菜单，1.5B 激活端侧模型选得动；(b) 「确认 + 审计」在亚秒级 dispatch 下不必然破坏交互感。⚠️ 厂商自家 demo，无第三方复现，不可据此推断端侧已可替代云端 Planner。

## 2026-08-03 增补（晚）：1-bit 量化反直觉结果 + BFCL/NexusRaven 分裂（来源 [[AppIntent 每日情报 2026-08-03-晚]]）

> 本条推翻了本笔记此前的一个隐含假设：「量化是精度换体积的单向妥协」。**在结构化输出任务上不成立。**

**A. Bonsai 系列（PrismML）实测 —— 第三方仓 `Manojb/small-llm-tool-use-bench`，Mac Mini M4 16GB，BFCL v3**

| 模型 | 量化 / 体积 | Simple | Multiple | Parallel | **BFCL 总分** | 延迟 |
|---|---|---|---|---|---|---|
| **Bonsai-8B** | **1-bit（Q1_0）/ 1.15GB** | 68% | 72% | 80% | **73.3%** | 1.8s |
| Gemma 4 E4B | FP16 | — | — | — | 65.3% | 待补 |
| Qwen3.5-9B | FP16 | — | — | — | 64.0% | 待补 |
| **Bonsai-1.7B** | **1-bit / 0.25GB** | — | — | — | **55%** | **0.4s** |
| Bonsai-4B | **FP16** | — | — | — | **25.3%** | 待补 |

**B. 🔴 反直觉结论：1-bit 量化感知训练（QAT）在结构化输出上是「增益」而非「损失」**

同族 Bonsai-4B **FP16 仅 25.3%**，而 1-bit 版本冲到 **73.3%**。这不是「量化后掉得少」，而是 **QAT 把模型的表达力压向「只吐合法 JSON」这一窄目标**。

→ **选型纪律更新：端侧 Planner 的量化策略不按「保精度」选，按「保 Schema 合规」选。** FP16 通用能力强 ≠ 填槽准。

**C. 🔴 BFCL ≠ 会用 API：新增「语义理解分」维度**

| 模型 | BFCL v3（格式合规） | NexusRaven（复杂 API 语义） |
|---|---|---|
| **Bonsai-8B（1-bit）** | **73.3%** | **43.8%** |
| Qwen3.5-9B（FP16） | 64.0% | **75–77.1%** |

**同一模型两个基准差 30 个点，且排名完全倒转。** 二者测的根本不是一件事：

- **BFCL** = 能不能**按格式把槽填对**（格式合规度）
- **NexusRaven** = 懂不懂**这个 API 是干嘛的**（语义理解）

→ **一个只会填格式、不懂语义的 Planner，在窄域固定 Schema（单应用 AppIntents / AppFunctions）里够用；在跨应用 Intent 编排里会稳定犯错。** 本笔记此前所有仅凭 BFCL 的选型建议，均需补一句「跨域编排另测语义分」。

**D. ⚠️ 口径警示（延续本库规矩）**：第三方个人测评仓，硬件 Mac Mini M4 **非手机 SoC**，用 BFCL **v3 非 v4**，**不可与 Berkeley 官方榜单行并列**。PrismML/Bonsai 官方模型卡数据与 1-bit QAT 训练配方**待补**。

**E. 端侧规模阶梯更新**（体积维度，可塞进手机的下限样本）：Needle 26M（INT4 **14MB**）→ Bonsai-1.7B（1-bit **0.25GB**，55% BFCL，0.4s）→ FunctionGemma 270M（**288MB**）→ Bonsai-8B（1-bit **1.15GB**，73.3% BFCL，1.8s）。

## 2026-08-04 增补：BFCL v4 换了评价标准，本笔记全部旧分数需标版本（来源 [[AppIntent 每日情报 2026-08-04]]）

> ⚠️ **全笔记级口径修正**：以下所有历史分数——Bonsai-8B 73.3% / Bonsai-1.7B 55% / Bonsai-4B 25.3%（BFCL **v3**）、qwen3-0.6b-tool-router 90.42%（**v3 时代窄域微调**）、Granite 4.1 68.27%/73.68%（**BFCL-v3**）、Phi-4-mini「80 分段」（第三方）——**均产生于「单轮格式合规」为主的评价体系**。BFCL v4 已把权重迁走，**新旧分数不可同栏比较**。

**A. v4 权重结构（经典 function calling 只剩 20%）**

| BFCL v4 类别 | 权重 | 实际测什么 |
|---|---|---|
| **Agentic**（web search / memory / format sensitivity） | **40%** | 取外部信息、持有持久状态、抗 Schema 与格式变动 |
| **Multi-Turn** | **30%** | 跨轮正确用工具（Base / Missing Functions / Missing Parameters / Long Context，约 800 例） |
| Live | 10% | 真实用户贡献的单轮调用 |
| Non-Live | 10% | 精选单个/多个/并行调用（**这才是「经典 BFCL」**） |
| **Hallucination** | **10%** | **无合适工具时正确地拒绝调用**（abstention） |

评分仍用 **AST + 状态转移**判定（非 LLM judge），因此确定可复现——但也正因如此，它历史上测的是「调用格式对不对」而非「该不该调」。
⚠️ 权重数字来自第三方拆解（注明榜单末次更新 2026-04-12），**Berkeley 官方博客原文表述待补**；方向性（v4 = holistic agentic evaluation）已由官方榜单页确认。

**B. 2026-08-03 榜单快照（镜像站 benchlm.ai，仅 9 个模型，非全量）**

| 模型 | 类型 | **BFCL v4** |
|---|---|---|
| Qwen3.7 Max（Alibaba） | 闭源 | **75.0%** |
| Qwen3.7 Plus（Alibaba） | 闭源 | 72.9% |
| **LFM2.5-8B-A1B（LiquidAI）** | 开源权重 | **49.7%** |
| Mellum2-12B-A2.5B-Thinking（JetBrains） | 开源权重 | 45.6% |
| Mellum2-12B-A2.5B-Instruct（JetBrains） | 开源权重 | 44.2% |
| ZAYA1-8B（Zyphra） | 开源权重 | 39.2% |
| **MiniCPM5-1B（OpenBMB）** | 开源权重 | **25.1%** |
| LFM2.5-VL-450M（LiquidAI） | 开源权重 | 21.1% |
| **LFM2.5-230M（LiquidAI）** | 开源权重 | **21.0%** |

⚠️ `benchlm.ai` 为**镜像/聚合站**（自述 mirrors the published score view），仅 9 个模型且自标「display only」，**不等同 Berkeley 官方全量榜**。注意 LFM2.5-8B-A1B 此处 49.7% 与 08-03 记录的厂商自述口径不同，**以基准版本区分，勿混用**。

**C. 三条结论（直接影响选型）**

1. **端侧模型的短板恰在 v4 加权最重处。** 亚 1B（21.0%/21.1%）与 1B 级（25.1%）都在 20% 出头，8B MoE 也只 49.7%——**v4 重的是 Agentic + Multi-Turn（合计 70%），正是小模型最弱的部分**。与本库 07-31 已确立的「<1B 通用 multi-turn 1.38%、1–3B 甜点区」相互印证。
2. **Hallucination 那 10% 是四大 OS 意图框架最该看的一栏。** 它测的是「系统里没有任何 AppIntent / AppFunction 能满足用户这句话时，模型会不会硬凑一个来调」——这正是跨应用意图路由在真机上最高频的失败模式，**Registry 越大误召回代价越高**；而工具微调模型系统性偏向「调点什么」，恰是其弱项。
3. **三基准三件事，单基准必然选错**：BFCL **v3** 测格式合规 → NexusRaven 测 API 语义理解（同模型差 30 分且排名倒转）→ BFCL **v4** 测多轮 + 该不该调。选型表必须三列并存，且**每个分数都标版本号**。

## 2026-08-05 增补：LFM2.5-2.6B 入表 + BFCL v4 权重获官方文档确认 + 08-05 快照（来源 [[AppIntent 每日情报 2026-08-05]]）

> 本期两件事：① 端侧 Planner 评测表补 **LFM2.5-2.6B** 这一档，使 LFM2.5 家族规模阶梯完整；② **BFCL v4 权重公式经 EvalScope 官方文档交叉确认**，将 08-04 的「二手快照」升级为「已核实口径」（Berkeley 原文仍待补）。

**A. LFM2.5-2.6B（Liquid AI，2026-08-04 发布，窗口内增量）**

- 参数 **2.6B**，定位 on-device agentic；架构 LIV convolutions + selective attention。
- 速度（厂商自述，未复现）：M5 Max **220 tok/s** / Ryzen AI Max **113 tok/s** / 手机约 **30 tok/s**；内存 **< 2.5GB**。
- 厂商称在 **BFCLv4 / ToolSandbox / Claw-Eval** 上可竞争 4–10× 更大的模型；**具体 BFCLv4 分数待补**（仅相对表述，未公布绝对值）。
- **LFM2.5 家族规模阶梯更新**：LFM2.5-230M（21.0%）→ LFM2.5-VL-450M（21.1%）→ **LFM2.5-2.6B（待补）** → LFM2.5-8B-A1B（49.7%）。便于讨论「路由档 vs 端到端档」的取舍。

**B. BFCL v4 权重获官方文档确认（关闭 08-04 待办）**

EvalScope 官方文档交叉确认 08-04 记的权重公式无误：

| BFCL v4 类别 | 权重 | 实际测什么 |
|---|---|---|
| Agentic | **40%** | 取外部信息、持持久状态、抗 Schema/格式变动 |
| Multi-Turn | **30%** | 跨轮正确用工具（约 800 例） |
| Live | 10% | 真实用户单轮调用 |
| Non-Live | 10% | 精选单/多/并行调用（经典 BFCL） |
| Hallucination | **10%** | 无合适工具时正确拒绝调用 |

→ 状态：从「第三方快照」升为「**已核实（EvalScope 官方文档）**」。库内全部历史分数版本标签（v3 格式合规分 vs v4 不可比）维持。Berkeley 官方博客原文逐字表述仍**待补**。

**C. 2026-08-05 榜单快照（镜像站 benchlm.ai，12 模型非全量，⚠️ 不等同官方榜）**

| 模型 | 类型 | **BFCL v4** |
|---|---|---|
| Qwen3.7 Max（Alibaba） | 闭源 | **75.0%** |
| Ling 3.0 Flash（Alibaba） | 闭源 | 73.0% |
| Qwen3.7 Plus（Alibaba） | 闭源 | 72.9% |
| Pokee-Isaac 28B（Pokee AI） | 开源权重 | 70.9% |
| **LFM2.5-2.6B（LiquidAI）** | 开源权重 | **56.9%** |
| **LFM2.5-8B-A1B（LiquidAI）** | 开源权重 | 49.7% |
| Mellum2-12B-A2.5B-Thinking（JetBrains） | 开源权重 | 45.6% |
| Mellum2-12B-A2.5B-Instruct（JetBrains） | 开源权重 | 44.2% |
| ZAYA1-8B（Zyphra） | 开源权重 | 39.2% |
| **MiniCPM5-1B（OpenBMB）** | 开源权重 | 25.1% |
| LFM2.5-VL-450M（LiquidAI） | 开源权重 | 21.1% |
| **LFM2.5-230M（LiquidAI）** | 开源权重 | 21.0% |

⚠️ `benchlm.ai` 为**镜像/聚合站**（自述 mirrors the published score view），**12 模型非全量、不等同 Berkeley 官方榜**。LFM2.5-2.6B 此处 **56.9%** 与 A 节厂商「竞争 4–10× 更大模型」的相对表述一致，但**绝对值仍属镜像站口径，需以官方榜复核**。

**D. 沿用结论（无变化）**：v4 加权最重的 Agentic+Multi-Turn（70%）恰是端侧小模型最弱处；选型表必须 BFCL v3 / NexusRaven / BFCL v4 三列并存且每分标版本。

## 2026-08-15 增补：FunctionGemma 类端侧 router 的部署路径（CoreML / LiteRT-LM，库内补漏）

> 来源：[[AppIntent 每日情报 2026-08-15]]。FunctionGemma 270M 本身为 2026-02 发布（已录其 BFCL/base→85% Mobile Actions），本条补漏的是**「它怎么真正跑在手机上」的部署路径**，此前本笔记只记评测未记部署。

- **soniqo.audio 指南**给出两端官方友好端口：Apple 侧 **CoreML（~283MB，跑 Neural Engine）**、Android / Linux / Windows 侧 **LiteRT-LM（~283MB）**；明文称「small enough to load alongside an ASR + TTS pipeline on phone-class hardware」，即作为**把用户话语转成工具调用的 router**。
- **严格语法**：训练产出 `call:NAME{...}` 哨兵语法，SDK 直接解析为类型化 `FunctionCall`（Swift Codable / Kotlin @Serializable），**无需 JSON repair、无需 schema-mode prompting**。
- → 对本笔记「端侧 Planner 选型」的补充：**可部署性**（CoreML for Apple NE + LiteRT-LM for Android）与**语法可靠性**（受限 grammar 免 JSON 修复）是选型的第 4、第 5 维度，与准确率/BFCL/云端逃逸率并列。FunctionGemma 在「小体积 + 严格语法 + 双端可部署」上是最接近「生产可用端侧 router」的样本之一（厂商/社区端口，非 Google 官方发布声明，标待补）。

## 关联

- 来源：[[AppIntent 跨平台情报简报 2026-07-30]] ｜ [[AppIntent 每日情报 2026-08-01]] ｜ [[AppIntent 每日情报 2026-08-03-晚]] ｜ [[AppIntent 每日情报 2026-08-04]] ｜ [[AppIntent 每日情报 2026-08-05]]
- 路由：[[Intent Router 语义路由]] ｜ 新架构：[[Simple Attention Network 无FFN端侧路由]]
- 方法：[[系统级 Intent 路由评估 SOP]]
- 路由：[[Intent Router 语义路由]] ｜ 方法：[[系统级 Intent 路由评估 SOP]]
- 算力：[[OS-PM-3B模型内存预算推演]]（跨库参考）

## 2026-08-16 增补：Needle 2 入表（体积阶梯 + BFCL v4，来源 [[AppIntent 每日情报 2026-08-16]]）

> 端侧 Planner 评测表补 **Needle 2（Cactus，2026-08 中旬）** 这一档。完整机制见 [[端侧 Router 置信度门控与工具可达性收缩 2026]]。

**A. 规模/体积阶梯更新（手机可塞下限样本）**

| 模型 | 规模 | 量化/体积 | 关键指标（厂商自述，非官方榜） |
|---|---|---|---|
| Needle 26M | 26M | INT4 / 14MB | single-shot 优于 270M~600M（Cactus 自述） |
| **Needle 2** | **45M** | **CQ2-bit / 14MB / ~28MB RAM** | **BFCL v4 42.6**；Mobile Actions 63.7；函数名准确率 98.3%；格式良好率 93.4%（BFCL 3,641 行） |
| Bonsai-1.7B | 1.7B | 1-bit / 0.25GB | BFCL v3 55%（第三方仓，非手机 SoC） |
| FunctionGemma 270M | 270M | CoreML/LiteRT-LM / ~283MB | Mobile Actions 微调 85% |
| Bonsai-8B | 8B | 1-bit / 1.15GB | BFCL v3 73.3% |

→ Needle 2 在「**同等 14MB 体积**」下把参数翻倍并加安全闸，是体积约束下「加闸不增体积」的样本；其 BFCL v4 42.6 低于 LFM2.5-230M（21.0% 为镜像站 v4，不可直接比——Needle 2 的 42.6 是 Cactus 自报、归因于消费设备语料偏向）。

**B. 口径纪律（延续）**：Needle 2 的 BFCL 数字为 **Cactus 厂商自述、非 Berkeley 官方榜行**；Cactus 自承语料偏消费设备动作、非通用/企业 API，故 v4 总分偏低**不反映窄域能力**。引用前仍须三问（官方榜 or 自建？微调 or 零样本？全量 or 子集？）。

## 2026-08-17 增补：FunctionGemma 270M BFCL v4 第三方聚合分（标待补，来源 [[AppIntent 每日情报 2026-08-17]]）

> 接续本笔记 08-15 的 FunctionGemma 部署路径。本期补一个第三方评测给出的 **BFCL v4 聚合分**，但须严标口径。

- 第三方 LittleLamb 评测（MultiverseComputingCAI，EvalScope 推理）引 Google 模型卡给出 **functiongemma-270m-it BFCL v4 聚合分 27.03**（Simple 61.6 / Multiple 63.5 / Parallel 39.0 / Live Simple 36.2 / Relevance 61.1 / Irrelevance 73.7 等分项，与 07-31 节 Google 自报分项一致）。
- ⚠️ **口径冲突警示**：该聚合分 27.03 与 Google 自报分项（Simple 61.6 等）**不在同一口径**——聚合分疑似把 Live/Parallel 等多轮/并行类（权重在 v4 占 70%）拉低整体；且来源标注模型卡日期 **09/04/2026**（晚于本运行日，待官方复核）。**不可与官方 BFCL v4 榜单行并列**，引用前仍须三问（官方榜 or 自建？微调 or 零样本？全量 or 子集？）。
- 沿用结论：本笔记 08-04 起建立的「每个分数标版本号」纪律不变；端侧 Planner 选型仍以 **BFCL v3（格式合规）/ NexusRaven（语义）/ BFCL v4（多轮+该不该调）三列并存**为准。

#标签/FunctionCalling #标签/端侧Planner #标签/评测
