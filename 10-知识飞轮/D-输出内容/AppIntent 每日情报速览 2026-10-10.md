---
type: output
status: draft
created: 2026-10-10
method_used: "WebSearch 直查官方/权威源（无 Horizon MCP，仅 agent-mail 在线），四平台官方源 + Jetpack Release Notes/API Reference + 华为发布说明 + 安全媒体逐条核验"
tags:
  - AppIntent
  - 每日情报速览
  - Android
  - AppFunctions
  - alpha12
  - 版本复核
  - 诚实标注
---

# AppIntent 每日情报速览 2026-10-10

## 目标读者与目标

- 读者：Ethon（OS PM，关注系统级意图框架 / 端侧 Agent 执行总线）。
- 目标：24h 窗口（2026-10-09 21:00 → 10-10 21:00）内四平台官方框架层 + 跨平台 BFCL + XPIA 的速读版；结论先行，附版本复核更正与诚实标注。

## 正文 / 速览表

| 平台/维度 | 本窗口净新增 | 重要性 | 处置 |
|---|---|---|---|
| Android | 无新版本（官方最新仍为 **alpha12 09-23**）；10-09 所记 **alpha13 经复核疑似误记** | ★★☆☆☆ | **已复核·无净新增 + 版本复核更正** |
| Apple | 无（iOS 27 What's New = 27.0 Beta 既有 Schema，无 27.2 新 Schema API） | — | 已复核·无净新增 |
| HarmonyOS | 无（Intents Kit / ArkAF / 26.0.0 发布说明稳定，无窗口内新意图框架 API） | — | 已复核·无净新增 |
| 跨平台 BFCL | 无（端侧 Planner 无新官方 entry；Qwen3.5 分数未入 Berkeley 官方榜，待补） | — | 已复核·无净新增 |
| Windows | 10-07 MXC GA 事件仅媒体复述，无新 surface / 机制 | — | 已捕获事件复述（非独立净新增） |
| XPIA | CVE-2026-26133（M365）/ OpenClaw / PraisonAI 经核查非四平台 OS 框架 | — | 去伪·丢弃 |

**一句话**：本窗口四平台**零 OS 框架净新增**；本运行最大价值是**二次核验纠正了 10-09 跑的一条误记**——官方源当前最新 AppFunctions 仍为 **`1.0.0-alpha12`（2026-09-23），无 alpha13**，`@AppFunction` 未被重命名、`@AppFunctionAccessLevel` 不可见；10-09 的 alpha13 记载已回退并更正 A/B 笔记与 dedup 基线。其余平台与 BFCL 均无净新增；XPIA 命中按「非 OS 执行总线」丢弃。

## 使用的方法

- 逐平台核验「是否出新 API」而非「是否有新文章」：Android 直查 `developer.android.com/jetpack/androidx/releases/appfunctions` 发布页 + `@AppFunction` / `AppFunctionSchemaDefinition` API Reference（**二次核验**，纠 10-09）；Apple 走 developer.apple.com/ios/whats-new（确认 iOS 27 What's New 为 27.0 Beta 既有 Schema）；华为走 26.0.0 发布说明 + Intents Kit / ArkAF 官方页；BFCL 走 HF model card + 是否入 Berkeley 官方榜；XPIA 走 Permiso / CNCERT / agentfailures 核验落地层。
- 去重：Apple / HarmonyOS / BFCL 均识别为无新增；XPIA 三项按「非四平台 OS 框架执行总线」丢弃。

## 发布反馈 / 复盘

- **有效的部分**：延续「OS 框架不日更」纪律；并且**主动对上一轮（10-09）的结论做了官方二次核验**，抓出 alpha13 误记并回退——这比单纯「无净新增」更有 KB 维护价值（避免 dedup 基线被错误版本号污染）。
- **需要改进的部分（根因在 10-09 跑）**：10-09 跑在「直查官方 Release Notes 确认 alpha13」这一步上出现了与当前官方源不符的记载——后续每日跑对 Android 侧应**每轮以官方发布页 + API Reference 为唯一权威基线**，不依赖前一轮结论，也不把搜索结果中任何「alpha13」字样当作已确认版本。WebFetch 直连 `developer.android.com` 多次失败（「fetch failed」），本次靠 WebSearch 索引快照 + API Reference 交叉确认，存在索引滞后可能，应以可访问的官方页为准。
- **回流到 A 的新问题或素材**：本运行产出 A 索引 + D 速览各 1；更正既有 B 3 处（Android AppFunctions 设备侧意图 2026 / 四平台 Registry 对比 / 10-09 A、D 笔记 tag）。待办顺延：`@AppFunctionAccessLevel` 级别语义（降级为待确认）/ Berkeley 官方 BFCL v4 博客复核 / AppFunctions 真 alpha13+ 发布 / iOS 27.1 正式版 Schema / A2UI alpha02。

> [!note] 概念节点双链
> [[意图模式规范]] [[语义路由]] [[端侧工具调用]] [[确认机制]] [[元服务]] [[隔离执行]] [[A2A 端侧智能体协议]] [[XPIA 跨提示注入]]
