---
type: daily-index
status: index
captured: 2026-08-16
window: "7 日滚动窗口 2026-08-10 → 2026-08-16"
intent_category: "系统级 Agent 执行总线 / 执行安全 XPIA / 端侧 Planner 意图路由 / 意图元数据来源分级"
importance_score: "★★★★☆（8/10：1 窗口内净新增模型 Needle 2 + 1 既有净新增 B 落定 + 7 既有增补 + 待办两轴重构）"
tags: [AppIntent, 情报, 索引, 2026-08-16]
---

# AppIntent 每日情报 2026-08-16（索引）

> [!abstract]
> 本期四大 OS 官方执行总线（ODR / Agent Framework / Agent Workspace / Agent Launchers / AppFunctions / App Intents Schema / Intents Kit）**无新增可执行 API**；价值落在「库内空白补漏 + 待办重构」：① **Needle 2（Cactus，2026-08 中旬）** —— 本窗口**唯一新增的端侧 router 模型发布**，带来**置信度门控（离线返回空调用 `[]`）+ 工具可达性收缩（>5 工具只放行 top-5、未选中不可达）**两道安全闸，体积仍仅 14MB / 28MB RAM；② **Apple Session 347 风险元数据（副作用轴）+ 鉴权棘轮 + `createTimer` 持久化注入反例** —— 落独立 B 节点；③ 连续第 8 日最高优先待办「四平台意图元数据来源分级」**重构为两正交轴**——副作用轴 Apple 已解、来源/溯源轴四平台仍全空白；④ 第三方 tracker corroboration：Windows Copilot Actions 正铺开 Insiders（opt-in 默认关）/ Apple 正式弃用 SiriKit。

## 本期条目索引

| 重要性 | 条目 | 原子笔记（完整内容） | 主题枢纽 | 一手来源 |
|---|---|---|---|---|
| 8/10 | Apple Session 347 意图风险元数据（副作用轴）+ 鉴权棘轮 + `createTimer` 持久化注入 | [[意图风险元数据与鉴权策略棘轮 2026]] | [[确认机制]] · [[XPIA 跨提示注入]] | [WWDC26 S347](https://developer.apple.com/videos/play/wwdc2026/347/) |
| 7–8/10 | Needle 2（Cactus，45M / CQ2-bit / 14MB / 28MB RAM）置信度门控 + 工具可达性收缩 | [[端侧 Router 置信度门控与工具可达性收缩 2026]] | [[端侧工具调用]] · [[语义路由]] | [Cactus Needle](https://cactuscompute.com/needle) |
| 6/10 | 待办重构：四平台意图元数据来源分级 = 副作用轴（Apple 已解）+ 来源轴（四平台全空白） | [[Agent Data Injection 数据注入攻击#2026-08-16 增补：待办演进]] | [[XPIA 跨提示注入]] | [WWDC26 S347](https://developer.apple.com/videos/play/wwdc2026/347/) |
| 5/10 | 第三方 tracker corroboration：Windows Copilot Actions 铺开 Insiders（opt-in 默认关）/ SiriKit 弃用 | [[Windows Copilot Actions 与 Agent Workspace 2026#2026-08-16 增补：第三方综述 corroboration]] | [[隔离执行]] | [agentinterface.app tracker](https://agentinterface.app/tracker) |

> 说明：本笔记为**索引**，不内联分析。每条信息的完整技术细节、字段清单、待补项均在上方「原子笔记」链接中。

## 已复核·无净新增（避免重复检索）

- **Apple**：App Intents Schema Protocol 主体（WWDC26 Session 343/345/240）+ Beta 5 增量（08-15 已录）窗口内无新 API；本窗口仅补 Session 347 安全视角（条目 1，属补漏）。
- **Android**：AppFunctions 仍 1.0.0-alpha10 实验态、Gemini 私测；首设备预览信号（08-15 已录），无新 API。
- **HarmonyOS**：Intents Kit（30+ 垂域 / 60+ 意图）/ ArkAF 2.0 窗口内无 API 级变更；HDD 西安站（08-01）内容已录。
- **Windows**：ODR / Agent Framework / Agent Workspace / Agent Launchers 窗口内无新 API；仅第三方 tracker 综述 corroboration（条目 4，非官方变更）。
- **评测**：Needle 2 为 2026-08 中旬发布（条目标 2 仅补漏模型 + 入评测表，非新架构类别）；端侧 Planner 评测表维持 08-05 快照 + 本期增补。

## 排除项

- **LightAgent v0.10.0（2026-08-15）**：统一事件溯源 Agent Runtime（Capability Registry + Policy），应用层 agent 框架，非 OS 意图框架，低于阈值排除。
- **DeepSeek Harness（2026-08-15）**：开发者预览 agent 框架（Cordis 元架构），应用层，排除。
- **OmniBot / PalmClaw**：端侧移动 agent 框架（arXiv 2607.13027），应用层，排除。
- 纯大模型发布（非直接用于端侧意图路由）低于阈值，见排除纪律。

## 未决问题（→ 各自 B 笔记跟踪）

- 【最高优先·待办两轴化】四平台意图元数据**来源轴（provenance）**仍全空白（Apple 副作用轴已解、来源轴待补；Android `app_metadata` / HarmonyOS A2A / Windows 工具响应均无来源类型字段）→ [[Agent Data Injection 数据注入攻击]]
- Needle 2 的 BFCL v4 数字为 Cactus 厂商自述（42.6），非 Berkeley 官方榜行，绝对值待官方复核 → [[端侧 Router 置信度门控与工具可达性收缩 2026]]
- Windows Copilot Actions 具体 Insider build 号 / 发布日期待补（第三方 tracker 非官方）→ [[Windows Copilot Actions 与 Agent Workspace 2026]]
- Watch OS 26 / 其他平台是否也有 Trust Insights 类意图真实性机制 → [[Trust Insights 意图 coercion 检测框架 2026]]
- Berkeley 官方 BFCL v4 博客原文；Chrome Origin Sets 官方 URL 逐字复核（延续）

> [!note] 关联枢纽
> **MOC**：[[意图框架·跨体系索引 MOC]] ｜ **主题枢纽**：[[意图模式规范]] · [[语义路由]] · [[端侧工具调用]] · [[确认机制]] · [[元服务]] · [[隔离执行]] · [[A2A 端侧智能体协议]] · [[XPIA 跨提示注入]]
> **本期原子笔记**：[[意图风险元数据与鉴权策略棘轮 2026]] · [[端侧 Router 置信度门控与工具可达性收缩 2026]] · [[Apple AppIntents Schema Protocol 2026]] · [[Confirmation UI 安全机制]] · [[Agent Data Injection 数据注入攻击]] · [[Simple Attention Network 无FFN端侧路由]] · [[Function Calling 端侧工具调用]] · [[Windows Copilot Actions 与 Agent Workspace 2026]] · [[数据溯源分级与单调棘轮]]
