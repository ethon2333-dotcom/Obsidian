---
type: raw
status: inbox
date: 2026-08-31
source:
  - "https://developer.apple.com/documentation/ios-ipados-release-notes/ios-ipados-27-release-notes"
  - "https://developer.apple.com/documentation/appintents"
  - "https://developer.apple.com/documentation/BundleResources/privacy-manifest-files"
  - "https://developer.android.com/ai/appfunctions?hl=zh-cn"
  - "https://device.harmonyos.com/cn/docs/apiref/harmonyos-guides/intents-introduction"
  - "https://www.sota2.com/research/sota/function-calling-on-bfcl-v4"
  - "https://byteiota.com?p=16284/"
importance_score: "★★★☆☆（6/10，窗口 OS 框架层无净新增；核心产出为最高优先待办「Per-Intent Privacy Manifest」收口）"
intent_category: "系统级意图框架 / 端侧 Agent 执行总线 / 执行安全（XPIA）· 7 日滚动窗口 2026-08-25→08-31"
tags: [情报, AppIntent, 每日情报, PerIntentPrivacyManifest, 来源轴, 四平台对比, 2026-08-31]
---

# AppIntent 每日情报 2026-08-31

> [!abstract] 30 秒速览
> - **核心突破（★8/10 级分析价值，非 OS 新 API）**：悬挂 8+ 天的最高优先待办「Per-Intent Privacy Manifest 是否真实 App Intents API」**本轮经官方文档直查收口为「不存在」**——第三方博客（byteiota）的说法是对 iOS 17 通用 `PrivacyInfo.xcprivacy` 或未来推测的误读。这进一步夯实「来源/溯源轴四平台全空白」结论，并给后续轮次排除一个反复出现的二手噪音源。
> - **关键指标**：Apple iOS 27 Beta 8 Release Notes 的 App Intents 段落（含 `notes.createNote`/`notes.updateNote` 的 `AttributedString` name 参数、appendText 恢复、calendar.deleteEvent 更名、10MB 实体上限）与 08-15 已录的 Beta 5 内容**逐字一致（同 bug 号 173431080 等）**，**无新增 schema API**，故不重复计数。
> - **OS Agent 场景**：做 OS 级意图 Registry 时，来源/溯源轴仍须自行原创（从 `readOrWrite` 声明位起步）；不要被「per-intent 隐私清单」类二手说法带偏。四平台官方框架层在本窗口均无净新增。

## 正文拆解

### ① Schema 定义与语义路由机制

本期窗口内**四平台 OS 级意图 schema 层经逐条复核无净新增**，但完成了一次高价值的**待办收口**：

- **Per-Intent Privacy Manifest 经官方文档直查证伪（★8/10 分析价值）**：WebFetch 官方 App Intents 框架文档 + 官方 Privacy manifest files 文档，确认 Apple **不存在**「按意图粒度声明云/端路由」或「per-intent privacy manifest」的 API；iOS 17 起仅有通用的 `PrivacyInfo.xcprivacy`（数据收集/required-reason API 声明），与 App Intents 路由无关。第三方博客（byteiota 一篇 SiriKit 弃用文）声称「WWDC26 引入 per-intent privacy manifest」属误读/推测。详见 [[四平台意图 Registry 来源轴与权限模型对比 2026]]。
- **Apple iOS 27 Beta 8 Release Notes 复核（无净新增）**：App Intents 段落与 08-15 已录 Beta 5 内容逐字一致（同 bug 号），**不重复计数**；本库 Beta 5 记录已完整覆盖，无新的 schema 能力。详见 [[Apple AppIntents Schema Protocol 2026]]。
- **其余三平台 + 跨平台 benchmark** 经复核无窗口内净新增：Android AppFunctions 守 alpha10、HarmonyOS 7 消费版无新 API、Windows agentic security 四支柱一致；BFCL v4 公开榜（sota2）数字均已在 08-26 入表。详见下方「已复核·无净新增」清单。

### ② 系统安全与用户体验（Confirmation / 隔离 / 防注入）

- **来源轴空白再夯实（与 ADI 防护缺口一致）**：Apple 意图层既无 provenance 字段（08-17 证伪 `.appEntityIdentifier` 为视图链接）、也无 per-intent 路由声明（本轮收口）；四平台来源/溯源轴仍全空白。凡「不可信数据喂给端侧 Planner」场景，当前仍只能靠应用/治理层补（[[数据溯源分级与单调棘轮]]），OS 总线层无对应物。详见 [[Agent Data Injection 数据注入攻击]]。
- **其余安全面（XPIA / Confirmation UI / Agent Workspace 隔离）** 各平台无窗口内净新增，均指向既有笔记：[[XPIA 跨提示注入]] ｜ [[Confirmation UI 安全机制]] ｜ [[Windows Copilot Actions 与 Agent Workspace 2026]]。

### 已复核·无净新增（避免下次重复检索）

| 平台 | 复核对象 | 结论 |
|---|---|---|
| Apple | iOS 27 Beta 8 Release Notes（App Intents 段，2026-08 末） | 与 08-15 已录 Beta 5 逐字一致（同 bug 号 173431080 等），无新增 schema API；不重复计数。 |
| Android | AppFunctions（Jetpack 1.0.0-alpha10，2026-07-21 末次更新） | alpha10 稳定，无新发布；Galaxy S26/Pixel 10 真机有限预览已录。 |
| HarmonyOS | Intents Kit / ArkAF 官方文档 + 社区反馈 | 官方文档稳定；端侧 Skill 同名冲突/3 秒超时/A2UI 静默失败（08-26 已录）；无新 API。 |
| Windows | OS agentic security 四支柱 + ODR + Agent Workspace | 官方文档一致；Copilot 超级应用整合（8 月下旬，应用层/产品层）非 OS 意图框架，低于阈值排除。 |
| 跨平台 | BFCL v4 公开榜（sota2 / benchlm） | 端侧模型分数（LFM2.5-2.6B 56.9% / Needle 2 42.6% / Nexus-TinyFunction-1.2B 94.25%）均已在 08-26 入表；无窗口内新模型发布。 |

> [!note] 概念节点双链
> [[意图模式规范]] [[语义路由]] [[端侧工具调用]] [[确认机制]] [[元服务]] [[隔离执行]] [[A2A 端侧智能体协议]] [[XPIA 跨提示注入]]

## 值得保留的点（索引）

- **★8/10 · 待办收口（分析价值）**：Per-Intent Privacy Manifest 经官方文档直查证伪为非真实 App Intents API（第三方博客误读 iOS 17 通用隐私清单 / 未来推测）—— 原子笔记 → [[四平台意图 Registry 来源轴与权限模型对比 2026]] ｜ 主题枢纽 → [[意图框架·跨体系索引 MOC]]
- **★0/10 · 已复核无净新增**：iOS 27 Beta 8 / AppFunctions alpha10 / HarmonyOS 7 / Windows 四支柱 / BFCL v4 公开榜 —— 见上表，下次不再重复检索。

## 后续动作

- [ ] 若 Apple 在 iOS 27 正式版（约 2026-09-14）新增 per-intent 路由/来源声明 API，重新评估来源轴结论（当前以「不存在」记录）。
- [ ] 把本轮「来源轴空白 + Per-Intent Privacy Manifest 证伪」回流至 [[Agent 读入路径可信数据边界 SOP]]（作为「勿误信 per-intent 隐私清单类二手说法」的判据）。
- [ ] 延续待办：Berkeley 官方 BFCL v4 博客原文；Watch OS 26 是否 Trust Insights 类；NowSecure / AgentAntibody 独立核验；Chrome Origin Sets 官方 URL 逐字复核。
