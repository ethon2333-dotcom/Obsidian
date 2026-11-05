---
type: concept
status: draft
derived_from: "[[AppIntent 每日情报 2026-11-03]]"
tags: [Apple, AppleIntelligence, Qwen, 端侧LLM, 区域化模型, 意图执行总线, Planner, 2026-11-03]
---

# Apple Intelligence 中国区 Qwen 端侧模型（2026）

## 一句话定义
iOS 27.3 起，Apple 在中国大陆以**阿里 Qwen 端侧模型**替代自研/云（PCC）底座来驱动 Apple Intelligence（Siri / Writing Tools / Visual Intelligence），且经**同一 Siri / App Intents 接口**暴露——即「意图执行总线（Planner 层）的端侧 LLM 可按监管/地区切换第三方模型，接口不变」。

## 为什么重要
- **首次在主力市场用第三方端侧 LLM 充当系统级意图执行底座**：此前 Apple Intelligence 的 Planner/生成底座是 Apple 自研 on-device 模型 + Private Cloud Compute（PCC）；中国区改用 Qwen，是「端侧 Agent 执行总线」底座**可替换、可区域化**的先例。
- **呼应跨平台「端侧 Planner 模型」议题**：直接关联本库 [[Function Calling 端侧工具调用]] / [[端侧执行通道 GUI 与 MCP 路线之争]]——设备侧到底跑谁家的 Planner/LLM，在监管市场成为硬约束而非纯技术选择。
- **对 OS PM 的方法论启示**：统一的意图/助手接口（App Intents / Siri）可以「换引擎不换接口」地适配本地监管，是跨市场 OS 智能体架构的可复用范式。

## 适用边界
- **仅中国区（iOS 27.3，iPhone 15 Pro+）先行**：写作/视觉/摘要类能力（Writing Tools / Genmoji / Clean Up / Notification Summaries / Priority Notifications / Visual Intelligence / Live Translation）开通；**新版 agentic Siri AI、多数 WWDC26 Apple Intelligence 能力、Image Playground 本版不进中国**。
- **模型层/enablement 变更，非新 schema API**：窗口报道未确认 iOS 27.3 新增 `@AppIntent(schema:)` Schema；属 Intelligence 底座替换 + Health app 重建。**新 schema API 状态待补**。
- **需本地备案**：中国网信办 7 月已完成 7 款端侧生成式 AI 服务备案（含 Apple Intelligence），Qwen 以「端侧备案模型」身份落地。

## 证据与例子
- Apple（10-30）宣布 iOS 27.3 首个 dev beta「下周」落地并启用中国区部分 Apple Intelligence 功能；与 Alibaba 合作在 Siri / Writing Tools / Visual Intelligence 内加入 Qwen。
- Alibaba（10-31）确认 Qwen 将为中国用户驱动 Apple Intelligence；iOS dev beta 11-04 起测试，iOS 27.3 于 12 月正式推送。
- dev.to（11-01）开发者视角：on-device vs model-routed 行为在网络差时分化，需测失败模式；结论「global AI products are splitting into national versions, with local models behind identical interfaces」。
- beta 时间：中国 11-04（周三）/ 美西 11-03（周二，时差）。

## 可复用启发
- **「接口-引擎解耦」是跨市场监管的架构刚需**：OS 级意图框架应把 Planner/LLM 底座设计为可插拔、按区域绑定合规模型，而非写死单一家族。
- **端侧备案模型 → 监管即架构约束**：在强监管市场，端侧生成式 AI 须先备案才能进系统级入口；这把「合规」前置为意图执行总线的准入条件（与 [[确认机制]] / 权限治理同层）。
- **失败模式测试**：同一意图接口在「本地模型路由」与「云/PCC 路由」间行为可能分化，开发者须按弱网/降级路径验证。

## 关联
- 来源：[[AppIntent 每日情报 2026-11-03]]
- 方法/对照：[[Apple AppIntents Schema Protocol 2026]]（同框架、不同底座层）、[[Function Calling 端侧工具调用]]、[[端侧执行通道 GUI 与 MCP 路线之争]]、[[四平台意图 Registry 来源轴与权限模型对比 2026]]（区域化模型对 Registry/权限模型的影响）、[[意图模式规范]]
