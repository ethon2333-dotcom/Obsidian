---
type: output
status: draft
created: 2026-08-31
method_used: "WebSearch/WebFetch 直取官方源 + 本 Agent 综合（Horizon MCP 连续 20+ 日 disconnected）；7 日滚动窗口 08-25→08-31"
derived_from: "[[AppIntent 每日情报 2026-08-31]]"
tags: [速览, AppIntent, 每日情报, PerIntentPrivacyManifest, 来源轴, 四平台对比, 2026-08-31]
---

# AppIntent 每日情报速览 2026-08-31

## 目标读者与目标

OS 产品经理 / 端侧 Agent 框架设计者。今日目标：在四平台 OS 官方框架层集体「无净新增」的窗口里，定位并**收口一个悬挂 8+ 天的最高优先待办**（Per-Intent Privacy Manifest 是否为真实 API），把「来源/溯源轴四平台全空白」的结论证据链补到干净，并显式记录「已复核·无净新增」避免下次重复检索。

## 正文（速览）

**① Per-Intent Privacy Manifest 待办收口（★8/10，核心产出）**
- 性质：经**官方文档直查 + 多源检索**判定为「**不存在**」的 App Intents API。Apple 官方 App Intents 框架文档无任何 per-intent 隐私/路由声明接口；iOS 17 起的 `PrivacyInfo.xcprivacy` 是通用数据收集清单，与意图路由无关；第三方博客（byteiota）说法系误读。
- 价值：进一步夯实「来源/溯源轴四平台全空白（confirmed）」，并给后续轮次排除一个反复出现的二手噪音源。
- 深度：[[四平台意图 Registry 来源轴与权限模型对比 2026]]

**② Apple iOS 27 Beta 8 复核（★0/10，无净新增）**
- 性质：Beta 8 Release Notes 的 App Intents 段落与 08-15 已录 Beta 5 **逐字一致**（同 bug 号 173431080 等），无新增 schema API，不重复计数。
- 深度：[[Apple AppIntents Schema Protocol 2026]]

**③ 其余三平台 + 跨平台 benchmark（★0/10，已复核无净新增）**
- Android AppFunctions 守 alpha10；HarmonyOS 7 消费版无新 API；Windows agentic security 四支柱一致；BFCL v4 公开榜端侧分数均已在 08-26 入表。
- 深度：[[Android AppFunctions 设备侧意图 2026]] ｜ [[HarmonyOS Intents Kit 与 ArkAF 2026]] ｜ [[Windows Copilot Actions 与 Agent Workspace 2026]] ｜ [[Function Calling 端侧工具调用]]

**④ 执行安全延伸（无窗口内净新增，指向既有笔记）**
- 来源轴空白 → ADI 防护缺口一致（[[Agent Data Injection 数据注入攻击]]）；XPIA / Confirmation UI / Agent Workspace 隔离各平台无新动作。
- 深度：[[XPIA 跨提示注入]] ｜ [[Confirmation UI 安全机制]] ｜ [[隔离执行]]

## 使用的方法

- 7 日滚动窗口（08-25→08-31），因 08-26 已覆盖至当日，本轮取窗口内净增量 + 库内待办收口。
- 分类纪律：先判「新事实 vs 已覆盖内容 vs 第三方误读」——把 Beta 8 与 08-15 Beta 5 同 bug 号内容比对，确认非新；把第三方「per-intent privacy manifest」说法送官方文档直查，证伪而非收录。
- 诚实纪律：明确标注「Beta 8 无净新增」「Per-Intent Privacy Manifest 已证伪」「BFCL v4 公开榜数字已在 08-26 入表」。

## 复盘

### 有效的部分
- 延续「无净新增显式列表」避免重复检索；延续「官方文档直查」判定待办，而非轻信二手博客。
- 把「待办收口」作为薄窗口下的核心产出，比强行编造净新增更符合本库「诚实」铁律。

### 需要改进的部分
- 初检时一度把 Beta 8 的 `notes` schema 变更误判为净新增，比对 08-15 记录后才发现同 bug 号已覆盖——今后遇到「Beta N 新功能」应先与库内既有 Beta 记录按 bug 号去重。

### 回流到 A 的新问题或素材
- 待把「来源轴空白 + Per-Intent Privacy Manifest 证伪」回流至 [[Agent 读入路径可信数据边界 SOP]]（判据：勿误信 per-intent 隐私清单类二手说法）。
- 延续：Berkeley 官方 BFCL v4 博客原文、Watch OS 26 Trust Insights 类、NowSecure/AgentAntibody 复核、Chrome Origin Sets 官方 URL。

## 关联
- 原子：[[四平台意图 Registry 来源轴与权限模型对比 2026]]（待办收口主笔记）｜ [[Apple AppIntents Schema Protocol 2026]]（Beta 8 复核）
- 安全：[[Agent Data Injection 数据注入攻击]] ｜ [[XPIA 跨提示注入]] ｜ [[Confirmation UI 安全机制]] ｜ [[数据溯源分级与单调棘轮]] ｜ [[隔离执行]]
- 平台：[[Android AppFunctions 设备侧意图 2026]] ｜ [[HarmonyOS Intents Kit 与 ArkAF 2026]] ｜ [[Windows Copilot Actions 与 Agent Workspace 2026]] ｜ [[Function Calling 端侧工具调用]]
- 枢纽：[[意图框架·跨体系索引 MOC]] · [[语义路由]] · [[确认机制]] · [[XPIA 跨提示注入]]
