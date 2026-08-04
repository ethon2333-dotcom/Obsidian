---
type: output
status: draft
created: 2026-08-03
run: 21:00 晚间增补
method_used: "[[系统级 Intent 路由评估 SOP]]"
tags: [AppIntent, 情报速览, 端侧Planner, 意图支付, 输出]
---

# AppIntent 每日情报速览 2026-08-03（晚间增补）

> [!abstract] 一句话
> 今晚只有两条真新东西：**1-bit 量化模型在 BFCL 上反超 FP16 大模型（但换个基准就崩）**，以及**银联 APOP 把「意图授权」做成了协议层凭证**。四大 OS 官方渠道自今早 09:00 版后无新增。

## 本轮性质

同日 09:00 已跑完整 7 天窗口（[[AppIntent 每日情报 2026-08-03]]，346 行）。本篇为 **21:00 增补**，只记净新增，**不覆盖、不重复**上午成果。

## 两条净新增

### 1️⃣ Bonsai 1-bit：BFCL 高分 ≠ 会用 API（7/10）

| 模型 | 体积 | BFCL v3 | NexusRaven |
|---|---|---|---|
| **Bonsai-8B（1-bit）** | 1.15GB | **73.3%** | **43.8%** |
| Qwen3.5-9B（FP16） | — | 64.0% | **75–77.1%** |
| Gemma 4 E4B（FP16） | — | 65.3% | 待补 |
| Bonsai-1.7B（1-bit） | 0.25GB | 55%（0.4s） | 待补 |
| **Bonsai-4B（FP16）** | — | **25.3%** | 待补 |

**三个结论：**

1. **1-bit QAT 在结构化输出上是增益不是损失**——同族 4B 的 FP16 版只有 25.3%，1-bit 版 73.3%。量化把模型压向「只吐合法 JSON」。
2. **BFCL 和 NexusRaven 测的不是一件事**——前者是格式合规度，后者是 API 语义理解。同一模型差 30 分且排名倒转。**只看 BFCL 会在跨应用编排场景选错模型。**
3. **选型纪律改写**：端侧 Planner 的量化策略不按「保精度」选，按「保 Schema 合规」选；且**必须实测量化版本，不能用 FP16 分数外推**。

⚠️ 第三方个人测评仓，Mac Mini M4 非手机 SoC，BFCL v3 非 v4，不可与 Berkeley 官方榜单并列。PrismML 官方数据待补。

### 2️⃣ 银联 APOP/AVOP：确认机制的下一形态（6/10）

- 协议本体 2026-04-02 发布；**08-03 里程碑：40+ 机构接入 + 支付 Skills 技能包，接入周期 5–7 天 → 分钟级**。
- **为什么它是执行安全而非金融新闻**：四大 OS 的意图框架**全部只解决「Agent 能不能调到这个能力」，没有一个解决「Agent 代替我花钱时这次授权凭什么算数」**。APOP 是首个把意图授权凭证（授权内容/额度/时效/责任主体）标准化的国内协议。
- **可迁移的设计原则**：**确认 UI 的产物应该是数据，不是事件。** 弹窗点确认只产生一个不可核验、可被注入绕过的事件；应产生带意图内容哈希的凭证，Agent 被 XPIA 劫持改单时凭证不匹配即可拦截。
- ⚠️ 协议全文与技术规范待补；是否真做到内容绑定未核实。

## 已复核·无净新增（双链指向既有笔记）

- Apple iOS 27 App Intents / Spotlight 语义索引 / AppIntentsTesting / DMA 延迟 → [[Apple AppIntents Schema Protocol 2026]]
- Android AppFunctions alpha10 / Registry / `EXECUTE_APP_FUNCTIONS` → [[AppIntent 每日情报 2026-08-03]]
- HarmonyOS HMAF 2.0 / Graph Reasoning / A2A / A2UI → [[HarmonyOS Intents Kit 与 ArkAF 2026]]
- Windows Agent 账户 / Agent Workspace 四支柱 → [[Windows Copilot Actions 与 Agent Workspace 2026]]
- FunctionGemma / qwen3-0.6b-tool-router / Needle 26M / LFM2.5-8B-A1B → [[Function Calling 端侧工具调用]]

## 对 OS PM 的两条可执行启发

1. **评测表加一列。** 内部端侧 Planner 选型表若只有 BFCL，立刻补「语义理解分」；否则窄域测得好、跨应用一上线就翻车。
2. **重新审视确认弹窗的设计目标。** 不要再优化「弹窗怎么写更清楚」，改问「这次确认能不能产出一份可核验的凭证」。这是 XPIA 防线从 UI 层下沉到协议层的入口。

## 复盘

- ✅ 增补跑的价值在于**明确区分「今日无事」与「未检索」**——本篇显式列出复核无新增的条目，避免下次重复检索。
- ⚠️ 连续第 2 日未解决的待办：**四平台 ADI（Agent Data Injection）分级评估 / intent-metadata 来源可信度**，官方文档中未见分级定义，需换检索路径（考虑直接查各平台安全白皮书 PDF）。
- 📌 新增待办：追踪 PrismML 官方技术报告，回填 1-bit QAT 训练配方。

---

> [!note] 概念双链
> [[意图模式规范]] ｜ [[语义路由]] ｜ [[端侧工具调用]] ｜ [[确认机制]] ｜ [[元服务]] ｜ [[隔离执行]] ｜ [[A2A 端侧智能体协议]] ｜ [[XPIA 跨提示注入]]

原始资料：[[AppIntent 每日情报 2026-08-03-晚]] ｜ 新概念：[[意图支付授权协议 APOP]]

#标签/AppIntent #标签/情报速览 #标签/端侧Planner
