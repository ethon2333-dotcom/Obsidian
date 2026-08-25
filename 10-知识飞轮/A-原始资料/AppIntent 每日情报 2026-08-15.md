---
type: daily-index
status: index
captured: 2026-08-15
window: "7 日滚动窗口 2026-08-09 → 2026-08-15（追平 6 日空窗）"
intent_category: "系统级 Agent 执行总线 / 执行安全 XPIA / 端侧 Planner 意图路由 / 意图元数据来源分级"
importance_score: "★★★★☆（8/10：1 净新增框架节点 + 3 既有增补 + 1 方法论澄清 + 1 观察）"
tags: [AppIntent, 情报, 索引, 2026-08-15]
---

# AppIntent 每日情报 2026-08-15（索引）

> [!abstract]
> 本期四大 OS 官方执行总线（ODR / Agent Framework / Agent Workspace / Agent Launchers / AppFunctions / App Intents Schema / Intents Kit）**无新增可执行 API**；价值落在「库内空白补漏 + 方法论澄清」：① **Trust Insights（Apple WWDC26 S379，iOS 27 官方框架）—— prior runs 全漏录**：检测「用户是否被社会工程胁迫」的 coerced-intent 框架，补齐执行安全第三元（注入指令 / 用户授权 / 意图真实性）；② **Apple iOS 27 Beta 5** 逐字变更（notes Schema 接受 AttributedString name、calendar.deleteEvent 重命名、AppEntity 10MB 上限、后台 Neural Engine 新 entitlement）；③ **Android AppFunctions 首设备落地信号**（Galaxy S26 + Pixel 10，Gemini 多步有限预览）；④ **`.appEntityIdentifier` 澄清**——它是实体-视图链接（Session 343 View Annotations）**非来源校验**，关闭 7 日最高优先待办的错误前提，四平台意图元数据来源分级仍全空白；⑤ **Windows Copilot Vision + 语义文件索引 = XPIA 读路径扩张**（应用层观察）。

## 本期条目索引

| 重要性 | 条目 | 原子笔记（完整内容） | 主题枢纽 | 一手来源 |
|---|---|---|---|---|
| 7–8/10 | Trust Insights（Apple WWDC26 S379，iOS 27 官方框架，库内漏录补漏） | [[Trust Insights 意图 coercion 检测框架 2026]] | [[确认机制]] · [[XPIA 跨提示注入]] | [Apple Trust Insights 文档](https://developer.apple.com/documentation/TrustInsights) · [WWDC26 S379](https://developer.apple.com/videos/play/wwdc2026/379) |
| 6/10 | Apple iOS 27 Beta 5 App Intents / Core AI 逐字变更 | [[Apple AppIntents Schema Protocol 2026#2026-08-15 Beta 5]] | [[Intent Router 语义路由]] · [[端侧工具调用]] | [iOS 27 Beta 5 Release Notes](https://docs.developer.apple.com/documentation/ios-ipados-release-notes/ios-ipados-27-release-notes) |
| 6/10 | Android AppFunctions 首设备落地信号（Galaxy S26 + Pixel 10） | [[Android AppFunctions 设备侧意图 2026#2026-08-15 首设备预览]] | [[端侧工具调用]] · [[语义路由]] | [blognone Galaxy S26/Pixel 10](https://www.blognone.com/node/149867) · [Android 17 is Here](https://developer.android.google.cn/blog/posts/android-17-is-here) |
| 6/10 | `.appEntityIdentifier` 澄清（非来源校验，关闭 7 日待办错误前提） | [[Agent Data Injection 数据注入攻击#2026-08-15 澄清]] | [[XPIA 跨提示注入]] · [[确认机制]] | [NSUserActivity.appEntityIdentifier](https://developer.apple.com/documentation/Foundation/NSUserActivity/appEntityIdentifier) · [SwiftUI .appEntityIdentifier](https://developer.apple.com/documentation/SwiftUI/View/appEntityIdentifier(_:)) |
| 5–6/10 | Windows Copilot Vision + 语义文件索引 = XPIA 读路径扩张（观察） | [[XPIA 跨提示注入#2026-08-15 读路径扩张]] | [[XPIA 跨提示注入]] | [windowsnews 语义搜索](https://windowsnews.ai/article/copilot-pcs-gain-semantic-file-search-as-microsoft-redesigns-copilot-dashboard-for-insiders.378367) |
| 5/10 | FunctionGemma 端侧部署路径（CoreML / LiteRT-LM 端口 + 严格语法） | [[Function Calling 端侧工具调用#2026-08-15 端侧部署路径]] | [[端侧工具调用]] | [soniqo FunctionGemma](https://soniqo.audio/guides/functiongemma) |

> 说明：本笔记为**索引**，不内联分析。每条信息的完整技术细节、字段清单、待补项均在上方「原子笔记」链接中。

## 已复核·无净新增（避免重复检索）

- **Apple**：App Intents Schema Protocol 主体（WWDC26 Session 343/345/240）无新增 API；本窗口仅 Beta 5 增量细节（条目 2）+ 漏录的 Trust Insights 框架（条目 1）。
- **Android**：AppFunctions 仍 1.0.0-alpha10 实验态、Gemini 私测；本窗口仅「首设备预览信号」（条目 3），无新 API。
- **HarmonyOS**：Intents Kit（developer.huawei.com 当前态 30+ 垂域 / 60+ 意图）/ ArkAF 2.0 窗口内无 API 级变更；CSDN 教程非官方发布。
- **Windows**：ODR / Agent Framework / Agent Workspace / Agent Launchers 窗口内无新 API；仅 Copilot 应用层读路径扩张（条目 5）。
- **评测**：FunctionGemma 270M 为 2026-02 发布（条目标 6 仅补漏部署路径，非新模型）；端侧 Planner 评测表维持 08-05 快照。

## 排除项

- 纯大模型发布（非直接用于端侧意图路由）低于阈值，见排除纪律。
- Copilot 应用层语义搜索 / Vision 按「读路径扩张」观察处理（条目 5），不升格为执行总线条目（同 08-01 排除 M365 Copilot 纪律）。
- Trust Insights 的云侧模型 / Feedback Assistant 运营细节不展开，聚焦 API 与威胁模型。

## 未决问题（→ 各自 B 笔记跟踪）

- 【最高优先·前提已纠错】四平台意图元数据来源分级：`.appEntityIdentifier` 非来源校验（已澄清），Apple 侧仍无来源绑定/签名 API → [[Agent Data Injection 数据注入攻击]]
- Trust Insights 是否下沉为系统级 agent 执行总线强制检查（目前仅 App 集成）→ [[Trust Insights 意图 coercion 检测框架 2026]]
- Windows Agent Framework MIT 许可页 / build 号；NowSecure / AgentAntibody 独立核验；Berkeley 官方 BFCL v4 博客 → 各对应 B 笔记

> [!note] 关联枢纽
> **MOC**：[[意图框架·跨体系索引 MOC]] ｜ **主题枢纽**：[[意图模式规范]] · [[语义路由]] · [[端侧工具调用]] · [[确认机制]] · [[元服务]] · [[隔离执行]] · [[A2A 端侧智能体协议]] · [[XPIA 跨提示注入]]
> **本期原子笔记**：[[Trust Insights 意图 coercion 检测框架 2026]] · [[Apple AppIntents Schema Protocol 2026]] · [[Android AppFunctions 设备侧意图 2026]] · [[Agent Data Injection 数据注入攻击]] · [[XPIA 跨提示注入]] · [[Function Calling 端侧工具调用]] · [[Confirmation UI 安全机制]]
