---
type: raw
status: inbox
date: 2026-08-03
run: 21:00 晚间增补
window: 2026-07-27 → 2026-08-03（7 天滚动窗口，仅记录 09:00 版之后的净新增）
source:
  - https://huggingface.co/datasets/Manojb/small-llm-tool-use-bench
  - https://gorilla.cs.berkeley.edu/leaderboard.html
  - https://www.cebnet.com.cn/20260803/103160089.html
  - https://developer.apple.com/documentation/appintents
  - https://developer.android.google.cn/ai/appfunctions
captured: 2026-08-03
importance_score: ★★★☆☆（7/10，单条最高：Bonsai 1-bit 评测 7/10）
intent_category: 端侧 Planner 评测 / 意图信任与支付执行
tags: [AppIntent, 端侧Planner, BFCL, 量化, 意图支付, 原始资料]
---

# AppIntent 每日情报 2026-08-03（晚间增补）

> [!abstract] 30 秒速览
> 本次为 **21:00 增补跑**，同日 09:00 已产出完整 7 天窗口简报（[[AppIntent 每日情报 2026-08-03]]），四大 OS 官方渠道在这半天内**无新增可核实动作**，故本篇只记两条净新增：
> ① **Bonsai 1-bit 量化模型（PrismML）BFCL 实测**——1.15GB 的 Bonsai-8B 拿到 **BFCL 73.3%**，反超 FP16 的 Qwen3.5-9B（64.0%）与 Gemma 4 E4B（65.3%），但换到考语义理解的 NexusRaven 只有 **43.8%**（Qwen3.5-9B 75–77.1%）。同族 Bonsai-4B **FP16 仅 25.3% → 1-bit 反而 73.3%**，说明 1-bit 量化感知训练是在「压结构化输出」而非「压知识」。**结论：BFCL 高分 ≠ 会用 API，它测的是格式合规度。**
> ② **银联 APOP/AVOP 智能体支付生态里程碑（08-03）**——40+ 机构接入，新增「支付 Skills 开发技能包」，接入周期从 5–7 天压到分钟级。这是「跨应用 Intent 工作流」里**首个把「意图授权→执行→清算」全链路标准化**的国内协议，直接关联 [[确认机制]] 与 [[意图模式规范]]。

---

## 一、本轮窗口说明与去重声明

| 项 | 说明 |
|---|---|
| 本轮性质 | 2026-08-03 **21:00 增补跑**（同日 09:00 已跑过一次完整窗口） |
| 检索窗口 | 2026-07-27 → 2026-08-03（沿用 08-02 起确立的 7 天滚动窗口） |
| 去重基线 | [[AppIntent 每日情报 2026-08-03]]（09:00 版，346 行）+ `01-笔记\手机AI智能体\` 既有笔记 + B 层各概念节点 |
| 信息源 | Horizon MCP **未连接**（连接器状态全为 disconnected）→ 全程 WebSearch / WebFetch 直取官方源，综合由本 Agent 完成 |

**已复核、确认无净新增（不重复记录，直接双链指向既有笔记）：**

- **Apple**：WWDC26 / iOS 27 App Intents 相关（Spotlight 语义索引、`AppIntentsTesting`、Foundation Models、Core AI、Evaluations、欧盟 DMA 延迟上线）→ 已在 [[AppIntent 每日情报 2026-07-31]] 与 [[Apple AppIntents Schema Protocol 2026]] 记录，本次 WebFetch 官方 iOS 26/27 指南**逐条比对无变化**。
- **Android**：AppFunctions `alpha10`、Registry、`EXECUTE_APP_FUNCTIONS` 权限模型 → 已在 09:00 版详录。
- **HarmonyOS**：HMAF 2.0 / Graph Reasoning Engine / A2A 端云双模 / A2UI → 已在 [[AppIntent 每日情报 2026-08-01]]、[[AppIntent 每日情报 2026-08-02]] 与 [[HarmonyOS Intents Kit 与 ArkAF 2026]] 记录。
- **Windows**：Copilot Actions / Agent Workspace / Agent 账户 / ACL → 已在 [[Windows Copilot Actions 与 Agent Workspace 2026]] 记录；本次 WebFetch 微软 agentic security 文档，四大支柱（User Control / Agent accounts / Agent workspace / User Transparency）表述**与既有记录一致**。
- **端侧模型**：FunctionGemma 270M、qwen3-0.6b-tool-router、Needle 26M、LFM2.5-8B-A1B → 均已入 [[Function Calling 端侧工具调用]]。

---

## 二、原始内容

### ① Schema 定义与语义路由：Bonsai 1-bit 量化模型的 BFCL 实测（重要性 7/10）

**来源**：HuggingFace 数据集 `Manojb/small-llm-tool-use-bench`（第三方独立测评，非厂商自述）
**测评环境**：Mac Mini M4 / 16GB 统一内存；BFCL **v3**；另跑 NexusRaven API 评测与 AgentBench OS 子集。

#### A. BFCL v3 结果（格式合规度）

| 模型 | 量化 / 体积 | Simple | Multiple | Parallel | **BFCL 总分** | 单查询延迟 |
|---|---|---|---|---|---|---|
| **Bonsai-8B** | **1-bit（Q1_0）/ 1.15GB** | 68% | 72% | 80% | **73.3%** | 1.8s |
| Gemma 4 E4B | FP16 | — | — | — | 65.3% | 待补 |
| Qwen3.5-9B | FP16 | — | — | — | 64.0% | 待补 |
| **Bonsai-1.7B** | **1-bit / 0.25GB** | — | — | — | **55%** | **0.4s** |
| Bonsai-4B | **FP16** | — | — | — | **25.3%** | 待补 |

> 分项仅 Bonsai-8B 在原表给全，其余模型的 Simple/Multiple/Parallel 拆分**待补**。

#### B. NexusRaven（复杂 API 语义理解）结果 —— 反转出现

| 模型 | NexusRaven |
|---|---|
| Qwen3.5-9B | **75–77.1%** |
| **Bonsai-8B（1-bit）** | **43.8%** |

#### C. 值得保留的点（这条为什么值 7/10）

1. **1-bit 量化不是纯损失，对结构化输出甚至是增益。** 同族 Bonsai-4B **FP16 只有 25.3%**，而 1-bit 版本冲到 73.3%——这不是「量化后掉得少」，是**量化感知训练（QAT）把模型往「只吐合法 JSON」的方向压**。对 OS PM 的意义：**端侧 Planner 的量化策略不该按「保精度」思路选型，而该按「保 Schema 合规」思路选型。**
2. **BFCL 与 NexusRaven 的分裂，是本库口径纪律的又一次实证。** 同一个模型，BFCL 73.3% / NexusRaven 43.8%，差 30 个点。**BFCL 测的是「能不能按格式填对槽」，NexusRaven 测的是「懂不懂这个 API 是干嘛的」。** 一个只会填格式不懂语义的 Planner，在窄域固定 Schema（如单应用 AppIntents）里够用，**在跨应用 Intent 编排里会稳定犯错**。
3. **0.25GB / 0.4s 的 Bonsai-1.7B（55% BFCL）给出了「真能塞进手机」的下限样本**，可与 Needle 26M（14MB）、FunctionGemma 270M（288MB）并列进端侧规模阶梯。
4. ⚠️ **口径警示**：这是**第三方个人测评仓**，硬件为 Mac Mini M4 而非真实手机 SoC，BFCL 用的是 **v3** 而非 v4；**不可与 Berkeley 官方榜单行并列引用**。PrismML/Bonsai 的官方模型卡数据**待补**。

---

### ② 系统安全与体验：银联 APOP / AVOP 智能体支付协议生态里程碑（重要性 6/10）

**来源**：中国电子银行网 2026-08-03 报道；协议本体发布于 **2026-04-02**。

- **APOP（Agentic Payment Open Protocol，智能体支付开放协议）**：定义智能体代替用户发起支付时的**意图管理、身份与授权、风控与清算**链路。
- **AVOP（Agent Value-added service Protocol）**：配套的增值服务协议。
- **08-03 增量**：**40+ 机构接入**；新增「**支付 Skills 开发技能包**」，商户/开发者接入周期从 **5–7 天压缩到分钟级**。
- **⚠️ 边界**：AVOP 细节在 2026-07-27 的报道中已出现，本条属**生态进展**而非协议变更；协议全文与技术规范链接**待补**，未核实其确认 UI（Confirmation）与二次授权的具体形态。

#### 为什么它属于「执行安全」而不是「金融新闻」

四大 OS 的意图框架目前都停在「**执行**」这一层——Apple 的 App Intents、Android 的 AppFunctions、Windows 的 Copilot Actions，都只解决「Agent 怎么调到这个能力」，**没有一个解决「Agent 代替我花钱时，这次授权凭什么算数」**。APOP 是首个把**意图授权凭证**标准化的国内协议：它把「用户授权了什么意图 / 授权额度 / 授权时效 / 谁来担责」从 UI 层的一个确认弹窗，提升成**协议层的可验证凭证**。

对照本库既有概念：
- [[确认机制]]：现有各 OS 的 Confirmation UI 是**一次性、非持久、不可核验**的；APOP 的意图凭证是**可持久、可核验、可追责**的 → 这是确认机制的下一形态。
- [[XPIA 跨提示注入]]：一旦 Agent 被注入劫持发起支付，UI 确认弹窗可被绕过（用户点了但不知道点的是什么）；协议层凭证要求**意图内容与授权凭证绑定**，理论上能把「注入改单」暴露出来。⚠️ 但 APOP 是否真做到这点**待补核实**。

---

## 三、我的问题（待验证）

1. **Bonsai 的 1-bit QAT 是否公开了训练配方？** 如果「1-bit QAT 提升结构化输出」可复现，这对端侧 Planner 选型是范式级结论，需要找到 PrismML 官方技术报告核实（当前**待补**）。
2. **NexusRaven 分数应不应该进本库的评测标准列？** 现有 [[Function Calling 端侧工具调用]] 只记 BFCL。若 BFCL/NexusRaven 的分裂普遍存在，评测 SOP 需要加一列「语义理解分」。
3. **APOP 的意图凭证与 Apple/Android 的 Intent Schema 能否对接？** 即：AppFunctions 调起支付时，能否携带 APOP 凭证？还是必须走各自 SDK？——**待补**。
4. 09:00 版遗留的最高优先待办**仍未解决**：四平台 ADI（Agent Data Injection）分级评估 / intent-metadata 来源可信度核实，官方文档中未见分级定义。

## 四、后续动作

- [x] Bonsai 评测结果 → 追加进 [[Function Calling 端侧工具调用]]（不新建节点）
- [x] APOP/AVOP → 新建 B 概念节点 [[意图支付授权协议 APOP]]（既有节点无法承载，属新概念面）
- [ ] 追踪 PrismML 官方技术报告，回填 1-bit QAT 配方与官方分数（待补）
- [ ] 继续追踪四平台 ADI 分级（跨日待办，已连续 2 日未解）

---

> [!note] 概念双链
> [[意图模式规范]] ｜ [[语义路由]] ｜ [[端侧工具调用]] ｜ [[确认机制]] ｜ [[元服务]] ｜ [[隔离执行]] ｜ [[A2A 端侧智能体协议]] ｜ [[XPIA 跨提示注入]]

#标签/AppIntent #标签/端侧Planner #标签/BFCL #标签/意图支付
