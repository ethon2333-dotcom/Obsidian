---
type: output
status: draft
created: 2026-08-18
method_used: "WebSearch/WebFetch 直取官方源 + 本 Agent 综合（Horizon MCP 连续 17+ 日 disconnected）；7 日滚动窗口 08-12→08-18，本轮净增量限 08-17/18"
derived_from: "[[AppIntent 每日情报 2026-08-18]]"
tags: [速览, AppIntent, 每日情报, Agent365, 治理层, 2026-08-18]
---

# AppIntent 每日情报速览 2026-08-18

## 目标读者与目标

OS 产品经理 / 端侧 Agent 框架设计者。今日目标：在四平台 OS 官方框架层集体「无净新增」的窗口里，定位唯一高价值增量（微软 Agent 365 / Entra Agent ID 治理层控制平面），并把它对接到本库既有的跨平台 Registry 对比与治理层结论。

## 正文（速览）

**唯一净新增（★7/10）— 微软 Agent 365 + Entra Agent ID 控制平面与身份基座**
- 性质：**M365/Entra 治理与身份层**的量产控制平面，**非 Windows OS 执行总线**；2026-05-01 GA，本日经官方 learn.microsoft.com / docs.com 文档核实。
- 三件套：① **统一注册表**（发现/审批/封锁，状态 Available/Blocked/Pending）；② **Entra Agent ID** 每 agent 唯一身份 + 权限 + Conditional Access；③ **三运行模式**（代用户 / 自主后台 / 协同预览）。
- 关键价值：升级本库 08-17 记的「Entra Agent Identity = 第三方解读待确认」→ **已 GA 官方确认**；为 OS PM 设计「统一智能体注册表 + agent 身份 + 运行模式」提供可对照量产范式，直接补强「六方 Registry/权限 Checklist（此前仅 Android 填实）」。
- 延伸：**Shadow AI 发现**页纳入用户私装本地/第三方 agent，对应「OS 层看不见的本地 agent 怎么治理」盲区。
- 深度：[[Agent 365 与 Entra Agent ID 智能体控制平面与身份基座 2026]]

**四大 OS 官方渠道复核 — 无净新增（避免重复检索）**
- Apple：iOS 27 Beta 6（24A5418b，08-17/18，首入一周一更）仅修 Bug + 性能微调，**App Intents 2.0 schema 无新 API**；iOS 26.6.1（21 CVE）为常规安全更新。→ [[Apple AppIntents Schema Protocol 2026]] / [[Trust Insights 意图 coercion 检测框架 2026]]
- Android：AppFunctions 守 **alpha10**（2026-07-21 末次更新），`@AppFunctionServiceEntryPoint` + `EXECUTE_APP_FUNCTIONS` 权限细节维持。→ [[Android AppFunctions 设备侧意图 2026]]
- HarmonyOS：处于 HDD 7-8 月巡回活动期，**无新 API**；2100+ Skill / 1200+ 底层能力口径冲突仍待官方澄清。→ [[HarmonyOS Intents Kit 与 ArkAF 2026]]
- Windows：OS agentic security 四支柱一致；Copilot Actions / Agent Workspace 仍 Insider 预览默认关。**Agent 365 属治理层，非 OS 总线新增**。→ [[Windows Copilot Actions 与 Agent Workspace 2026]] / [[Windows Agent Framework 端侧 Agent 执行框架 2026]]

**上下文（★6/10 · 市场数据·非框架级）**：Counterpoint 称 2026 Q1 鸿蒙中国份额 19% 首超 iOS 17%——竞争感知信号，不建 B 节点。

## 使用的方法

- 7 日滚动窗口（08-12→08-18），因 08-17 已覆盖至当日，本轮仅取 08-17/18 净增量。
- 分类纪律：先判「新事实 vs 口径变化 vs 治理层 vs OS 层」，避免把 Agent 365 误写为「Windows OS 已内建注册表」。
- 诚实纪律：Agent 365 GA 日期与三模式来自官方文档；msftaisecurity.com 为第三方镜像，细节以官方复核。

## 复盘

### 有效的部分
- 把「四平台 OS 层无净新增」显式列成复核表，延续 08-15 起的纪律，避免重复检索。
- 用 Agent 365 收敛了 08-17 的「Entra Agent Identity 待官方确认」悬项，使跨平台 Registry 对比笔记的 Windows 身份项从「待确认」升为「已 GA」。

### 需要改进的部分
- 本库「六方 Registry/权限 Checklist」仍仅 Android 填实，Agent 365 的治理层三模式尚未逐条对照进表（已列入后续动作）。

### 回流到 A 的新问题或素材
- 待核验 Agent 365 与 Windows ODR 的 connector 衔接边界；延续 BFCL v4 官方原文、Watch OS 26 Trust Insights、NowSecure/AgentAntibody 独立核验。

## 关联
- 原子：[[Agent 365 与 Entra Agent ID 智能体控制平面与身份基座 2026]]
- 对比：[[四平台意图 Registry 来源轴与权限模型对比 2026]] ｜ 治理层：[[数据溯源分级与单调棘轮]] ｜ 身份/隔离：[[Agent 身份与硬件级审批]] ｜ [[隔离执行]]
- 平台：[[Apple AppIntents Schema Protocol 2026]] ｜ [[Android AppFunctions 设备侧意图 2026]] ｜ [[HarmonyOS Intents Kit 与 ArkAF 2026]] ｜ [[Windows Copilot Actions 与 Agent Workspace 2026]]
- 枢纽：[[意图框架·跨体系索引 MOC]] · [[语义路由]] · [[确认机制]] · [[XPIA 跨提示注入]]
