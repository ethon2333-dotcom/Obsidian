---
date: 2026-10-10
tags: [AppIntent, 每日情报, Android, AppFunctions, alpha12, 版本复核, 执行安全, 诚实标注]
source: "https://developer.android.com/jetpack/androidx/releases/appfunctions ; https://developer.android.com/reference/androidx/appfunctions/AppFunction ; https://developer.apple.com/ios/whats-new ; https://developer.huawei.com/consumer/en/doc/harmonyos-releases/os-new-feature-2600 ; WebSearch 直查官方/权威源（无 Horizon MCP）"
importance_score: "★★☆☆☆"
intent_category: "执行安全 / 系统级意图框架 / 版本复核"
---

# AppIntent 每日情报 2026-10-10

> [!warning] 本笔记「alpha13 系误记」结论已被 2026-10-13 复核推翻
> 本运行（10-10）称 AppFunctions `1.0.0-alpha13` 为误记、官方最新仍为 alpha12，系当时官方索引快照滞后所致。**2026-10-13 对 Jetpack Release Notes 发布页 + alpha-channel + all-channel 三处官方列表直查确认 `1.0.0-alpha13`（2026-10-07）确为真实发布**（含 `@AppFunctionAccessLevel` 与 `@AppFunction`→`@AppFunctionDeclaration` 重命名）。故本笔记「回退 alpha13」动作错误，相关事实仍以 [[AppIntent 每日情报 2026-10-09]] + [[Android AppFunctions 设备侧意图 2026]] 10-13 复核段为准。

> [!abstract] 30 秒速览
> 本窗口（2026-10-09 21:00 → 10-10 21:00）**四平台均无 OS 框架层净新增**，延续「OS 框架不日更」纪律。本运行的核心价值不在新 API，而在**二次核验纠正了上一轮（10-09）的一条误记**：10-09 笔记称 AppFunctions `1.0.0-alpha13`（2026-10-07）携 `@AppFunctionAccessLevel` 与 `@AppFunction`→`@AppFunctionDeclaration` 重命名——经 2026-10-10 直查官方 Jetpack Release Notes 与 `@AppFunction` / `AppFunctionSchemaDefinition` API Reference，**官方源最新仍为 `1.0.0-alpha12`（2026-09-23），无 alpha13**，`@AppFunction` 仍标「Added in 1.0.0-alpha12」。alpha13 相关记载疑似误记，已回退并更正 A/B 笔记与 dedup 基线。Apple（iOS 27 What's New = 27.0 Beta 既有 Schema，无 27.2 新 Schema API）、HarmonyOS（Intents Kit / ArkAF 稳定）、BFCL v4（端侧 Planner 无新官方 entry）、XPIA（无新 OS 执行总线 CVE）均零净新增。

## ① Schema 定义与语义路由（本窗口）

| 平台 | 本窗口 Schema/路由层净新增 | 重要性 | 处置 |
|---|---|---|---|
| Android | 无新版本（官方最新仍为 **alpha12 09-23**）；10-09 所记 alpha13 经复核不可见、疑似误记 | — | 已复核·无净新增（附版本复核更正） |
| Apple | 无（iOS 27 What's New 列的是 iOS 27.0 Beta **既有** App Intents Schema / Entity Schema / View Annotations / Testing 框架，非 27.2 新 Schema API） | — | 已复核·无净新增 |
| HarmonyOS | 无（Intents Kit 配置式开发指南稳定；ArkAF 概览 / 端侧 A2A 文档稳定；26.0.0 发布说明无窗口内新意图框架 API） | — | 已复核·无净新增 |
| 跨平台 BFCL | 无（端侧 Planner 无新入榜；FunctionGemma 270M / Qwen3-0.6B / LittleLamb 0.3B 数字为已知 model card，无新官方 entry） | — | 已复核·无净新增 |

要点：
- **版本复核更正（本窗口核心）**：10-09 跑据称「直查官方 Release Notes + alpha-channel 确认 alpha13（10-07）」，但 10-10 复核发现官方发布页与 API Reference **均无 alpha13**；`@AppFunction` 未被重命名为 `@AppFunctionDeclaration`。alpha13 可能是 10-09 跑的误记（或短暂发布后撤回且未回填索引），以官方当前可见状态（最新 = alpha12）为准。已回退 10-09 A/B 笔记中 alpha13 相关「已确认事实」记载，并把 Android 侧 dedup 基线重置为「alpha12（09-23）」，避免后续跑以「alpha13 已捕获」为错基漏检真 alpha13 / alpha14。
- Apple / HarmonyOS / BFCL：均无路由 / 评测层净新增，延续「OS 框架不日更」。

## ② 系统安全与 UX（Confirmation / 隔离 / 反注入）

### 🔑 本窗口唯一实质处置：版本复核更正（Android AppFunctions 权限模型回退）
- **复核动作**：直查 `developer.android.com/jetpack/androidx/releases/appfunctions` 发布页 + `@AppFunction` / `AppFunctionSchemaDefinition` API Reference（2026-10-10）。
- **结论**：官方最新版本 = **`1.0.0-alpha12`（2026-09-23）**，`@AppFunction` 注解仍标注「Added in 1.0.0-alpha12」，无 `@AppFunctionDeclaration` 重命名，`@AppFunctionAccessLevel` 在官方源不可见。
- **权限模型回退**：AppFunctions 可确认的权限模型回到 alpha12 的「`EXECUTE_APP_FUNCTIONS` 闸门 + `scope` 可见性 + `AppFunctionState` 状态门控」三块（见 [[Android AppFunctions 设备侧意图 2026]] 09-25 / 10-10 更正段）；10-09 推的「函数侧 `@AppFunctionAccessLevel` 第四块」**降级为待官方确认**。
- **影响范围**：已更正 ① 10-09 A 笔记（加更正横幅 + 改 tag）② 10-09 D 笔记 tag ③ [[Android AppFunctions 设备侧意图 2026]] 10-09 段标 ⚠️ 更正 + 文末 10-10 更正段 ④ [[四平台意图 Registry 来源轴与权限模型对比 2026]] 10-09 段标 ⚠️ 更正 + 降级「三向约束」为「待确认」。

### 窗口内无新安全机制（按口径复核）
- **Apple**：iOS 27.2 多渠道仍为「Gemini-Siri 扩 5 语言（法 / 日 / 韩 / 葡 / 西）」等功能 / 本地化扩展，**非新 `@AppIntent(schema:)` Schema API**，亦无新 Confirmation UI / entitlement 机制。
- **HarmonyOS**：所有命中均为稳定框架文档（arkaf-overview、insight-intent 配置式开发、26.0.0 发布说明），无新隔离 / A2A 安全 API。
- **Windows**：2026-10-07 MXC GA 事件已在 10-08 / 10-09 收录；本窗口仅媒体复述，无新 surface / 机制。
- **XPIA**：无窗口内新 OS 执行总线 CVE；CVE-2026-26133（M365）/ OpenClaw / PraisonAI 仍属 M365 / 第三方工具链，按「非四平台 OS 框架执行总线」口径丢弃（同 10-06 / 10-09）。

### 去伪 / 丢弃（按口径）
- **BFCL v4**：Qwen3.5 家族分数（0.8B 25.3 / 2B 43.6 / 4B 50.3 / 9B 66.1）为新模型族，但**未进入 Berkeley 官方 BFCL v4 榜单**（最后官方更新 2026-04-12），按「非官方 entry」不升净新增，标**待补**；社区 Qwen3-0.6B（think 54.08 / no-think 29.17）等为已知 model card。
- **XPIA 框架层**：RAMPART / Microsoft DDR 2026 / agentmelt 等均为既有或非 OS 框架层，无窗口内新 OS 执行总线 CVE。

> [!note] 概念节点双链
> [[意图模式规范]] [[语义路由]] [[端侧工具调用]] [[确认机制]] [[元服务]] [[隔离执行]] [[A2A 端侧智能体协议]] [[XPIA 跨提示注入]]

---

> [!warning] 诚实标注
> - alpha13 是否在 10-09 → 10-10 间曾被短暂发布又撤回，无法从公开索引确认；10-10 结论基于官方发布页 + API Reference 的 WebSearch 直查（WebFetch 直连失败，以搜索索引快照 + API Reference 交叉确认），以「官方当前可见 = 最新 alpha12」为准。若 Google 后续回填 alpha13，本库再更新。
> - Qwen3.5 BFCL 分数来自社区 / 厂商口径，未经 Berkeley 官方榜单确认，标「待补」。
> - 本运行未使用 Horizon MCP（仅 agent-mail 在线），全部以 WebSearch / WebFetch 直查官方源完成逐平台核验。
