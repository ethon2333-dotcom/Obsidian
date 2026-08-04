---
type: method
status: active
derived_from: "[[Function Calling 端侧工具调用]] | [[Intent Router 语义路由]]"
tags: [AppIntent, 评估, SOP, 端侧Planner]
---

# 系统级 Intent 路由评估 SOP

> 用途：评估 / 选型「端侧 Intent Planner（OS Agent 路由方案）」。实测数据见 [[Function Calling 端侧工具调用]]。

## 使用场景

- OS / 系统 Agent 团队要选型或验收端侧意图路由方案。
- 判断某小模型能否在目标设备算力下承担「Tool Choice + 参数抽取」。
- 设计「本地优先 + 低置信升级云端」混合架构。

## 输入

- 单应用 / 窄域 Tool Schema 数据集（含参数定义）。
- 多轮对话样本（覆盖槽位缺失、歧义、跨步骤依赖）。
- 目标设备算力预算（NPU 型号、内存上限、可接受延迟）。

## 步骤

1. **明确评估目标**：单应用 vs 跨应用路由；延迟/成本预算（如 Pixel 7 ≥ 2000 tok/s）。
2. **准备 Schema 数据集**：单应用 Tool Schema + 多轮样本，刻意覆盖槽位缺失与歧义。
3. **选型基线**：小模型 Planner（FunctionGemma 270M 类）做本地路由，配「低置信升级云端」兜底。
4. **跑 benchmark（必须双基准，2026-08-03 更新）**：
   - **格式合规度**：BFCL（注明 v3/v4、官方榜单行 or 自测）→ 测「能不能按 Schema 把槽填对」。
   - **语义理解度**：NexusRaven 或等价复杂 API 语义集 → 测「懂不懂这个 API 是干嘛的」。
   - **两者必须同时记录**：实测存在同一模型 BFCL 73.3% / NexusRaven 43.8% 且与对手排名倒转的情况（Bonsai-8B vs Qwen3.5-9B）。**只看 BFCL 会在跨应用编排场景选错模型。**
   - 同时记录：Tool Choice 准确率、参数抽取 F1、延迟、tok/s、**云端逃逸率**。
5. **设检查标准**：本地优先达标线（如准确率 ≥ 85%、延迟达标）；定义低置信升级阈值。
6. **加语义缓存**：Qwen3-Embedding-0.6B 类语义缓存吸收高频意图，降低云端依赖（学习环）。
7. **失败处理**：低置信 → 升级云端；槽位缺失 → Parameter Slot-filling（`requestValue` 反向追问）。

## 完成标准

- 本地 Planner 准确率 / 延迟达标，且升级链路闭环。
- 语义缓存命中后高频意图零上云。
- 跨域 / 低置信样本有明确升级路径，无静默错误。

## 常见失败与处理

| 失败 | 处理 |
|------|------|
| 跨域泛化差、准确率低 | 缩小 Planner 域 + 强化云端升级；或对单应用 Schema 微调（官方口径 **base 58% → 微调 85%**） |
| 设备算力不足、tok/s 不达标 | 降模型规模（270M/0.6B）或量化 |
| **BFCL 高但线上跨应用频繁出错** | 补测 NexusRaven；语义分低说明模型只会填格式不懂 API，**限制其只做窄域固定 Schema 路由**，跨应用编排上移 |
| **FP16 模型填槽准确率反常低** | 试 1-bit/低比特 **QAT** 版本——结构化输出任务上 QAT 是增益而非损失（Bonsai-4B FP16 25.3% → 1-bit 73.3%） |
| 语义缓存污染 | 设 TTL / 置信门槛，定期失效 |
| 槽位缺失导致执行失败 | 强制 Slot-filling 反向追问，禁止静默默认 |

## 2026-08-03 增补：量化选型纪律

**端侧 Planner 的量化策略不按「保精度」选，按「保 Schema 合规」选。** 通用能力强 ≠ 填槽准；量化感知训练把模型表达力压向「只吐合法 JSON」这一窄目标，在意图路由场景反而有利。选型时**必须实测量化版本，不能用 FP16 分数外推**。

## 示例

- FunctionGemma 270M 经单应用 Tool Schema 微调 + LiteRT-LM，Mobile Actions **base 58% → 85%**（Google 官方口径）；S25 Ultra 实测 prefill 1718 tok/s / decode 125.9 tok/s（详见 [[Function Calling 端侧工具调用]]）。
- 混合栈：FunctionGemma 本地 + 低置信升级 Gemini Flash + Qwen3-Embedding-0.6B 语义缓存。
- 双基准反例：Bonsai-8B（1-bit, 1.15GB）BFCL **73.3%** 却 NexusRaven **43.8%**，Qwen3.5-9B 恰好相反（64.0% / 75–77.1%）→ 详见 [[AppIntent 每日情报 2026-08-03-晚]]。

## 深化补充（2026-08-04）：步骤 4 的「双基准」应升级为「三基准 + 版本号」

> 触发：BFCL 已发布 v4 并**重构评分权重**，上面步骤 4 写的「双基准」成文于 08-03，当时默认 BFCL 指 v3。**v3 与 v4 测的不是同一件事，分数不可同栏比较**，本节为该步骤打补丁。概念侧全表见 [[Function Calling 端侧工具调用]]。

### A. 官方口径核实结果（2026-08-04 检索，部分解决库内挂起待办）

- **已由官方页确认**：`gorilla.cs.berkeley.edu/leaderboard.html` 自述 BFCL **V4** 为 "**holistic agentic evaluation**"，榜单列结构为 **Agentic（Format Sensitivity / Web Search / Memory）+ Multi Turn + Single Turn（Non-live AST / Live AST）+ Hallucination Measurement**，与库内记录的类目一致；评分沿用 **AST + 状态转移**判定（非 LLM judge），故可复现。
- **权重公式已交叉确认（非孤证）**：`Overall = Agentic×40% + Multi-Turn×30% + Live×10% + Non-Live×10% + Hallucination×10%`，由 **EvalScope 官方 `bfcl_v4` 实现文档**明确写出（实现依赖 `bfcl-eval` 包），与库内此前的第三方拆解数字一致。
- ⚠️ **仍标「待核实」**：Berkeley **官方博客原文**对该权重表的直接表述本轮未取到（官方 v4 博客分 Web Search / Memory / Format Sensitivity 三篇，其「Full Leaderboard Score Composition」段落未抓全）。当前状态从「单一二手快照」升级为「**官方确认结构 + 独立实现确认权重，官方原文表述待核**」。
- ⚠️ **榜单时效**：第三方注明榜单末次更新 **2026-04-12**；本轮官方页所见条目也集中在 2025 年底—2026 年初的模型，**2026 年中后期新模型未入表**。库内 08-04 记录的 `benchlm.ai` 镜像站那批分数（LFM2.5-8B-A1B 49.7% 等）在本轮官方页**未见对应行**，因此仍为**镜像站口径，不可当官方榜单行引用**。

### B. 官方榜单端侧规模档实测行（2026-08-04 检索所见，BFCL v4 Overall Acc）

| 模型 | 类型 | v4 Overall |
|---|---|---|
| Claude-Opus-4-5 (FC) | 闭源，榜首 | **77.47** |
| Claude-Sonnet-4-5 (FC) | 闭源 | 73.24 |
| Gemini-3-Pro-Preview (Prompt) | 闭源 | 72.51 |
| xLAM-2-3b-fc-r (FC) | 3B 工具专用 | **41.22** |
| Qwen3-4B-Instruct-2507 (FC) | 4B 通用 | 35.68 |
| Arch-Agent-3B | 3B 工具专用 | 35.36 |
| Arch-Agent-1.5B | 1.5B | 32.14 |
| xLAM-2-1b-fc-r (FC) | 1B 工具专用 | 30.44 |
| Qwen3-1.7B (FC) | 1.7B 通用 | **28.41** |
| Hammer2.1-1.5b (FC) | 1.5B 工具专用 | 27.88 |

**这张表直接改写选型预期**：在 v3 时代靠窄域微调能刷到 90%+ 的规模档（1–4B），到 v4 只剩 **28–41 分**，与榜首差 **35 分以上**。注意 `xLAM-2-3b`（41.22）反而高于 `Qwen3-4B`（35.68）——**工具专用微调在这一档仍然有效，但抬不动 Agentic/Multi-Turn 那 70% 的权重**。

⚠️ 榜单为定期更新的活数据，引用时**必须同时记录检索日期**（本表：2026-08-04）。

### C. 步骤 4 的替换版：三基准并列，每列标版本号

| 列 | 基准 | 测什么 | 对应的线上失败模式 |
|---|---|---|---|
| ① 格式合规 | **BFCL v3**（或 v4 的 Non-Live 子项） | 能不能按 Schema 把槽填对 | 参数类型错、JSON 不合法 |
| ② API 语义 | **NexusRaven** 或等价复杂 API 语义集 | 懂不懂这个 API 是干嘛的 | 跨应用编排选错工具 |
| ③ 多轮 + 拒答 | **BFCL v4** | 跨轮持状态；**无合适工具时会不会硬凑一个** | 槽位追问断裂；**误召回** |

**验收硬规则**：选型表里每个分数后面必须跟 `(基准名 + 版本 + 官方/第三方 + 微调/零样本 + 全量/子集 + 检索日期)`。缺任一项的数字，评审时按「不可用」处理。

### D. 对 OS 意图路由最该看的一栏：Hallucination（v4 占 10%）

它测的是「**当系统里没有任何 AppIntent / AppFunction 能满足用户这句话时，模型会不会硬编一个函数去调**」。这正是真机上最高频、也最难被用户察觉的失败模式——**Registry 越大，误召回代价越高**。而工具微调过的模型系统性偏向「调点什么」，恰恰是这一项的弱项。

→ **落地建议**：内部评测集必须**主动构造「无解意图」样本**（用户说的事本机确实没有对应能力），单独统计拒答率；不要只用有解样本算准确率。这一项不达标的模型，**不允许承担开放域路由，只能做窄域固定 Schema 路由**。

### E. 失败表增补两行

| 失败 | 处理 |
|---|---|
| **拿 v3 分数论证 v4 时代的选型** | 全表加版本列；v3 高分只能证明"格式会填"，不能证明"多轮能办事" |
| **只测有解意图，误召回在线上才暴露** | 评测集补「无解意图」子集，单列拒答率；对齐 v4 Hallucination 口径 |

## 关联

- 概念底座：[[Function Calling 端侧工具调用]]（端侧 Planner 全量评测表 + 口径纪律）｜ [[Intent Router 语义路由]]
- 新架构变量：[[Simple Attention Network 无FFN端侧路由]]（26M 无 FFN 路由器，"工具调用本质是检索不是推理"）
- 基准邻居：[[Local Agent Bench 端侧智能体基准]]（补部署现实）｜ [[OSWorld 计算机操作基准]]（GUI 侧能力）｜ [[通用 AI Agent 评测基准 2026]]
- 下游方法：[[端侧执行通道选型 SOP]]（路由完之后走哪条通道执行）
- 安全交叉：[[Agent 读入路径可信数据边界 SOP]]（路由输入若来自不可信源，准确率再高也会被劫持）
- 平台落点：[[Android AppFunctions 设备侧意图 2026]] ｜ [[Apple AppIntents Schema Protocol 2026]] ｜ [[Agentic OS 意图调度内核]]

## 待解问题

- [ ] **Berkeley 官方 v4 博客原文的权重表述仍未取到**（本轮只拿到官方类目结构 + EvalScope 实现公式）。下轮直接抓 `gorilla.cs.berkeley.edu/blogs/15_bfcl_v4_web_search.html` 的「Full Leaderboard Score Composition」段落原文。
- [ ] 官方 v4 榜单未见 1B 以下条目，本库关注的 Needle 26M / Bonsai-1.7B / FunctionGemma 270M **全部不在官方表内**。这一档要么自建回归集，要么承认"没有可比的公开基准"——该选哪条？自建集又如何避免变成第二个 `prism-coder` 式自证？
- [ ] v4 的 Agentic 40% 里含 Web Search（需 SerpAPI）与 Memory，**这两项与端侧离线意图路由的相关性存疑**。是否应该对 OS 场景重新加权（例如只取 Multi-Turn + Hallucination + Non-Live 三项做内部口径），并把这个自定义加权明确写进选型模板？

#标签/评估 #标签/SOP #标签/端侧Planner
