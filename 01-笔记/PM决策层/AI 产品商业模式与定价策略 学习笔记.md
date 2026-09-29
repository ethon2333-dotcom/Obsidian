---
title: AI 产品商业模式与定价策略 学习笔记
tags:
  - #PM
  - #商业模式
  - #定价策略
  - #AI产品
  - #monetization
created: 2026-09-17
source: "WebSearch/WebFetch 联网核实"
---

> **本文与 [[数据飞轮与 AI 产品度量 学习笔记]]、[[增长模型 学习笔记]]、[[意图框架开发者生态与平台经济 学习笔记]] 的关系**：这三篇分别讲「怎么度量 AI 产品（指标）」「怎么让用户增长」「平台/开发者怎么被激励」；本文只讲**AI 产品怎么赚钱、怎么定价（商业化与 value capture）**，是它们的「变现」补集——度量回答"值不值"，增长回答"来不来人"，平台经济回答"生态愿不愿玩"，本文回答"钱从哪来、毛利怎么算"。

**一句话心智模型**：AI 产品的核心不同在于——**每服务一个用户都产生真实的推理变动成本（token/算力）**，所以定价必须从"卖功能/卖席位"转向"按消耗或按结果计价"，否则毛利会被重度用户吃穿。

---

## 1. 定义：AI 产品如何变现，与传统软件的差异

传统软件（含 SaaS）的边际成本趋近于零：多一个用户几乎不增加成本，毛利可达 ~77%（云软件平均，Adobe ~88%）。

AI 产品（尤其生成式/推理型）不同：

- **推理成本是变动成本**：每完成一次对话、生成一张图、跑一次 agent，都要消耗 GPU/算力，按 token 或调用计费。
- **重度用户会击穿毛利**：ChatGPT Pro（$200/月）被 OpenAI CEO 公开承认"对超级用户是亏损的"；早期 GitHub Copilot 单用户月成本曾达 $30–80、毛利润为负，倒逼重新定价。
- **结论**：AI 产品的 unit economics 必须让"收入"与"推理成本"挂钩，而非简单照搬席位订阅。

| 维度 | 传统 SaaS | AI 产品 |
|---|---|---|
| 边际成本 | ≈0 | 变动（token/算力） |
| 典型毛利 | ~77% | 受压，重度用户可转负 |
| 定价锚点 | 席位 / 功能 | 消耗 / 结果 / 加成 |
| 成本主体 | 云+人力 | GPU+推理 |

---

## 2. 分类：主流商业模式（表格速查）

| 模式 | 计费单位 | 适用场景 | 代表 |
|---|---|---|---|
| **API 按量计费** | token / 调用 | 开发者、嵌入后端 | OpenAI / Anthropic / Google API |
| **订阅制（月/年）** | 固定费 | 个人生产力工具 | ChatGPT Plus、Claude Pro、Gemini Advanced |
| **席位/分层订阅** | 按席位 + 档位 | 企业协作 | M365 Copilot、Notion AI、GitHub Copilot |
| **用量 + 订阅混合** | 基础订阅 + 超额 | 工具类、有峰谷 | New Relic、Otter.ai、含 AI credits 的方案 |
| **按任务/按结果计费（outcome-based）** | 解决的工单/成交/减损 | 客服、销售、自动化 agent | Intercom Fin、Zendesk、Sierra、Salesforce Agentforce |
| **增值溢价（AI 加成）** | 在原有许可上 +$ | 已有存量客户的软件 | M365 Copilot +$30、Salesforce Einstein、SAP Joule |

**关键区分**：
- 席位制 = 你**有多少人**用（augmentation，增强人）
- 用量制 = 你**用了多少**（consumption）
- 结果制 = 你**拿到什么结果**（automation，替代人）—— Simon-Kucher 的"价格-价值矩阵"：自动化越高 + 价值越可量化，越适合 outcome-based。

---

## 3. 主流方案 / 代表产品定价实践（WebSearch 核实）

### 3.1 底层 API（按 token，per 1M tokens，标准档）

| 厂商 / 模型 | 输入 $/MTok | 输出 $/MTok | 备注 |
|---|---|---|---|
| OpenAI gpt-5 | $1.25 | $10.00 | 官方 2025-08 发布价 |
| OpenAI gpt-5-mini | $0.25 | $2.00 | — |
| OpenAI gpt-5-nano | $0.05 | $0.40 | — |
| Anthropic Claude Sonnet 4.5 | $3.00 | $15.00 | ≤200K 上下文 |
| Anthropic Claude Opus 4.5 | $5.00 | $25.00 | 较前代降价明显 |
| Anthropic Claude Haiku 4.5 | $1.00 | $5.00 | — |
| Google Gemini 3.5 Flash | $1.50 | $9.00 | 2026 默认模型 |
| Google Gemini 3.1 Pro (preview) | $2.00 | $12.00 | >200K 翻倍至 $4/$18 |
| Google Gemini 3.1 Flash-Lite | $0.25 | $1.50 | 高量廉价档 |

> 注：以上为官方/聚合站核实的标准档价；长上下文、Batch（约 5 折）、prompt caching（最高约 9 折）会显著改变实际单价。各厂 2025–2026 价格快速下调、型号迭代频繁，**具体档位与促销价标「待核实」**。

### 3.2 消费者订阅（月费，USD）

| 产品 | 档位 | 价格 | 说明 |
|---|---|---|---|
| ChatGPT | Plus | $20 | GPT-5 访问 |
| ChatGPT | Pro | $200 | 无限推理，重度用户亏损（CEO 公开） |
| ChatGPT | Team | $25–30/用户 | 待核实区间 |
| Claude | Pro | $20 | — |
| Claude | Max | $100 / $200 | — |
| Gemini | AI Plus | $7.99 | 2026 新入门档，待核实 |
| Gemini | AI Pro (原 Advanced) | $19.99 | — |
| Gemini | AI Ultra | $99.99 | 由 $249.99 下调，待核实 |
| Microsoft Copilot | Pro | $20 | 需另购 M365 |
| M365 Copilot | 加购 | $30/用户·月 | 需 E3/E5 许可，≈+50–70% 溢价 |

### 3.3 结果 / 任务计费代表

- **Intercom Fin**：每成功解决一个工单 $0.99；上线 5 个月自主处理占比 15%→45%。
- **Zendesk**：resolution-based pricing（按成功解决的请求计费）。
- **Sierra**（Bret Taylor）：AI 客服按协商费率按结果收费，转人工免费；估值 ~$100 亿、ARR 近 $1 亿（媒体口径）。
- **Salesforce Agentforce**：约 $2/对话（企业按量包）。
- **Chargeflow**：成功追回拒付抽成 25%。

### 3.4 增值溢价（AI 加成）代表

| 厂商 | 加成方式 | 溢价幅度 |
|---|---|---|
| Microsoft | M365 Copilot +$30/用户 | 较基础许可 +50–70% |
| Salesforce | Einstein / Agentforce | $50–75/用户·月 |
| Oracle | AI 入高阶许可 | +30–40% |
| SAP | Joule 需升 S/4HANA Cloud | 迁移/升级驱动 |

> 行业背景：2025 年 SaaS 整体涨价约 11.4%（远超 G7 通胀 2.7%），AI 是主要涨价理由（Saastr 口径，待核实）。

---

## 4. 关键考量（点到为止）

- **Unit economics**：定价 ≥ 推理成本 × 重度系数。输出 token 通常比输入贵 5–10 倍，长上下文/推理 token 是成本主因（Google "thinking tokens" 按输出计费）。
- **毛利保卫战**：用分层 + 用量上限 + 模型路由（简单任务走 cheap 模型）保毛利；纯订阅在重度场景会亏。
- **护城河**：数据（闭环飞轮）、分发（嵌入工作流/Office）、模型（自研 SOTA）、工作流嵌入深度。护城河越深，越能收"加成溢价"而非纯 commoditized token 价。
- **价格歧视与分层**：按安全/合规（SSO、私有数据区）、领域专精、agent 自主度做 fencing，capture 企业高支付意愿。
- **成本转嫁**：算力"烧钱黑洞"最终转嫁用户，是 AI 涨价本质。

---

## 5. 2025–2026 进展（联网核实）

- **AI 功能作为加成溢价**：Microsoft / Adobe / Google / Salesforce 把 AI 嵌入既有订阅并提价，AI 成为"涨价筹码"（国内：腾讯会议、飞书、1688 诚信通 AI 版均借 AI 涨价）。
- **Agent 按任务计费探索**：Intercom Fin、Zendesk、Sierra、Salesforce Agentforce 把"按结果付费"从咨询业搬到 AI 产品；2026 被称为企业 AI "求实之年"，CFO 要求可量化 ROI。
- **企业 AI 采购模式**：年承诺（committed token / 席位）+ 试点（pilot）→ 验证（POV）→ 年化；平台+服务打包，实施费常达首年订阅 50–100%。
- **价格战与降本**：API 单价 2025 年大幅下探（部分模型降约 83%），DeepSeek 等以近零价施压；Google 把 Ultra 从 $249.99 砍到 $99.99。
- **调查数据**：Simon-Kucher（2025-09）调研约 39% 预期 outcome-based、36% usage-based、39% hybrid；Gartner 预测 2025 年 >30% 企业 SaaS 含 outcome 组件（2022 约 15%）。

---

## 6. 广度留白（待 Ethon 深挖）

- [ ] 待解问题：AI 产品如何设计"用量上限 + 超额"而不引发用户反感？缓冲/提醒机制？
- [ ] 待解问题：outcome-based 的"结果"如何无争议定义与归因（避免 Zendesk 式争议）？
- [ ] 待解问题：中小团队如何做模型路由（cheap model 兜底）来控制 unit cost？
- [ ] 待解问题：AI 加成溢价在国内市场的付费意愿 vs 海外的差异（视频平台 AI 救场乏力案例）？
- [ ] 待解问题：agent 按任务计费下，厂商如何对冲"任务失败但仍耗算力"的成本风险？

---

## 附：来源清单

- OpenAI — Introducing GPT-5 for developers（官方定价，2025-08）
- OpenAI — API Fast mode / Priority processing pricing page（2026-07 改名）
- Anthropic — Claude Opus 4.5 / Sonnet 4 / 1M context 官方定价页
- Google — Gemini API pricing guide 2026（curlscape / cloudzero，2026-07 核实）
- Simon-Kucher — AI Agent 定价讲座综述（2025-09，stactize 转述）
- Intercom / Zendesk / Sierra — outcome-based pricing 公开资料与媒体报道
- The Negotiation Experts — Embedded AI Licensing（Microsoft/Salesforce/SAP/Oracle 加成溢价）
- Monetizely — AI Pricing 2025（成本 vs 定价、毛利对比）
- 界面新闻 — 《AI时代，用户终于愿意为软件付费了？》（国内 AI 加成涨价案例）
- 华信设计院（数智咨询研究院）— 2026 智能体按效果付费（RaaS）报告综述
- 各比价站（modelcosts / modelpricewatch / prompt-pricing）聚合价，部分标待核实

## ⚠️ 待核实清单

- [ ] 各消费订阅具体档位价（ChatGPT Team $25–30、Gemini AI Plus $7.99、Ultra $99.99 由 $249.99 下调）——多为聚合站/媒体口径，随时间波动。
- [ ] Anthropic Claude 4.8 / Fable 5、OpenAI GPT-5.6 等 2026 新型号价——来自单一页面，需以官方页为准。
- [ ] 2025 SaaS 整体涨价 11.4%、传统 SaaS 毛利 ~77%——行业报告口径。
- [ ] Sierra 估值/ARR、Salesforce Agentforce 精确 $/对话——媒体/厂商口径。
- [ ] Google "thinking tokens"、Batch 5 折、prompt caching 9 折等实际折扣——以各厂文档实时为准。
- [ ] 所有 API 单价会随型号迭代频繁变动，落库时请复核对官方页。

#标签/PM #商业模式 #定价策略 #AI产品
