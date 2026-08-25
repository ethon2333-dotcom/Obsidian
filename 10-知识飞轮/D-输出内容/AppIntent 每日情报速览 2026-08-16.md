---
type: output
status: draft
derived_from: "[[AppIntent 每日情报 2026-08-16]]"
captured: 2026-08-16
tags: [AppIntent, 速览, 2026-08-16]
---

# AppIntent 每日情报速览 2026-08-16

> 30 秒概览：本期四大 OS 官方执行总线**无新增 API**；重心在「端侧 router 安全闸样本 + 最高优先待办两轴重构」。

## 三条最该记住的结论

1. **端侧 router 首次自带「安全闸」产品化**——[[端侧 Router 置信度门控与工具可达性收缩 2026]]：Needle 2（Cactus，45M / 14MB / 28MB RAM）带来**置信度门控**（离线返回空调用 `[]`）+ **工具可达性收缩**（>5 工具只放行 top-5、未选中不可达）。它把「端侧→云端升级」从启发式变成显式阈值，且「体积不变下加闸」是体积约束下的稀缺样本。

2. **Apple 的「意图风险」是系统级强制层，且写进了 Schema 协议**——[[意图风险元数据与鉴权策略棘轮 2026]]：Session 347 确认 `@AppIntent(schema:)` 自动继承 schema 的**副作用轴**风险元数据（destructive / exfiltration / shared-content），`authenticationPolicy` 只能**更严不能更松**（棘轮）；`createTimer` 的持久化注入反例坐实「可信字段回流污染」。

3. **连续第 8 日最高优先待办「四平台意图元数据来源分级」被重构为两正交轴**——[[Agent Data Injection 数据注入攻击]]：① **副作用轴（动作多危险）：Apple 已解**；② **来源/溯源轴（数据从哪来、可不可信）：四平台仍全空白**。待办不关闭，但收窄为「来源轴」。最低成本补丁仍是意图 Registry 加 `readOrWrite` 声明位。

## 横向对照速记

| 维度 | 本期状态 |
|---|---|
| 端侧 Planner 安全闸 | Needle 2 给出「结构性不可达 + 置信阈值」样本（[[端侧 Router 置信度门控与工具可达性收缩 2026]]） |
| 确认触发器归属 | Apple 用副作用轴做**系统确定性触发**（[[Confirmation UI 安全机制]]），Android 仍下放 App |
| 数据来源分级 | 四平台 OS intent 层**仍全空白**（[[数据溯源分级与单调棘轮]] 近亲是 Apple 鉴权棘轮，但补不了来源轴） |
| Windows 动态 | Copilot Actions 铺开 Insiders、opt-in 默认关（第三方 tracker，非官方 API 变更，[[Windows Copilot Actions 与 Agent Workspace 2026]]） |

## 落库导航

- **净新增 B（2）**：[[意图风险元数据与鉴权策略棘轮 2026]] ｜ [[端侧 Router 置信度门控与工具可达性收缩 2026]]
- **既有增补 B（7）**：[[Apple AppIntents Schema Protocol 2026]] ｜ [[Confirmation UI 安全机制]] ｜ [[Agent Data Injection 数据注入攻击]] ｜ [[Simple Attention Network 无FFN端侧路由]] ｜ [[Function Calling 端侧工具调用]] ｜ [[Windows Copilot Actions 与 Agent Workspace 2026]] ｜ [[数据溯源分级与单调棘轮]]
- **索引**：[[AppIntent 每日情报 2026-08-16]]
- **枢纽**：[[意图框架·跨体系索引 MOC]]

⚠️ 口径：Needle 2 的 BFCL v4 42.6 为 Cactus 厂商自述、非 Berkeley 官方榜行；Windows 第三方 tracker 非 OS 官方文档，须以 Microsoft 官方源复核。
