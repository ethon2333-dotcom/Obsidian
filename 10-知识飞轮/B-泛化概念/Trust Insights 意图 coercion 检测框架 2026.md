---
type: concept
status: draft
derived_from: "[[AppIntent 每日情报 2026-08-15]]"
tags: [AppIntent, Apple, TrustInsights, 执行安全, Coercion, 概念]
aliases: [Trust Insights, 意图胁迫检测]
---

# Trust Insights 意图 coercion 检测框架（2026）

> 库内空白补漏：Apple WWDC26 Session 379 引入、iOS 27 官方框架，prior runs（07-31→08-09 共 7 期）均未收录。与 [[XPIA 跨提示注入]]（注入指令）和 [[Confirmation UI 安全机制]]（用户授权）正交——它解决的是第三类问题：**用户本人是否被胁迫做出这个意图**。

## 一句话定义

**Trust Insights** 是 Apple 在 iOS 27 推出的客户端框架，用隐私保护式机器学习检测「用户是否正被社会工程胁迫（coaching/coercion）去执行一个本不愿做的高风险动作」，为 App 在支付、改账户、授权等**关键操作前**增加一道「行为真实性」摩擦。

## 为什么重要

- **补全了意图安全的三元模型**：① XPIA 防「注入的假指令」；② Confirmation UI 管「用户授权」；③ Trust Insights 管「用户意图是否真实自由」—— 前两者都默认用户是自愿的，只有它专门处理「用户自愿但被操控」这一长期被忽视的威胁（MFA/生物识别在此场景失效，因为操作人就是本人）。
- **OS 级可用构件**：entitlement `com.apple.developer.trustinsights.base` + 标准 Swift API，意味着任何 iOS 27 App 都能在关键操作前挂这道检查，是 OS 给「高危意图执行」提供的现成安全原语之一。
- **隐私范式清晰**：只处理必要信号、即时丢弃、设备源数据不出端；分析交互模式/时序/上下文/基础传感器，**绝不读 Photos/Messages/Mail 内容**；用户可关（含防被胁迫关闭的冷却期）。

## 适用边界

- 仅 iOS 27+（Apple 生态），非跨平台；Android/HarmonyOS/Windows 无对等框架（见 [[XPIA 跨提示注入]] 四平台状态）。
- Apple **明确不建议**仅凭 Trust Insights 直接阻断（blocking）；它产出 `.medium/.high` 信号，App 应「加警告 + 延时 + 人工复核」，不作为唯一决策因子。
- 目前**限定 App 集成**，未下沉为系统级 agent 执行总线的强制检查——对 OS Agent 是可集成构件，非内建安全原语。
- 判定有延迟（请求需数秒、需联网可达性），须嵌在已有动画/插屏时机，不能裸调。

## 证据与例子

- **核心 API**：`IsLikelyBeingCoachedInsight` 单一请求类型；`InsightEvaluator` + `InsightContext(operationCategory:)`；outcome 取值 `.unknown / .medium / .high`。
- **5 类 operationCategory**：`payment`（资产/内容/金钱交换）、`account`（注册/登录/改账户安全）、`resourceUse`（昂贵或受限资源如 AI 推理）、`communication`（群发消息/建连）、`other`（兜底，需 Feedback Assistant 反馈）。
- **授权与反馈**：须先 `requestAuthorization`；每次评估**强制**调 `reportConsumption`（否则限流）；可选离线欺诈标签经 Apple Business Register server-to-server 回传（含隐私脱敏要求）。
- **Apple 自带范例**：大额转账给「自称亲属医生」的人 → `.medium` 触发 App 显示警告 + 交易延时。
- 一手来源：[Apple Trust Insights 文档](https://developer.apple.com/documentation/TrustInsights) ｜ [WWDC26 Session 379](https://developer.apple.com/videos/play/wwdc2026/379)。

## 可复用启发

- **OS Agent 高危意图执行前**，可挂钩 Trust Insights 类「行为真实性」信号（尤其 payment/account/resourceUse），与 Confirmation UI 组成双层护栏；但需作为**可集成构件**而非「系统强制」，且**绝不单独据此阻断**。
- **确认机制设计新增一维**：除「内容三档 / 触发器三档」外，补「意图真实性」—— 系统/App 应能在高危动作前鉴别「用户是否在被操控」。
- **隐私红线**：行为信号分析**不碰内容**（Photos/Messages/Mail），只用量级/时序/传感器—— 这是端侧意图安全可落地的隐私下限。

## 关联

- 索引：[[意图框架·跨体系索引 MOC]]
- 正交互补：[[Confirmation UI 安全机制]]（用户授权 vs 意图真实性，双层护栏）｜ [[XPIA 跨提示注入]]（注入指令 vs 胁迫真人，威胁模型互补）
- 上位：[[确认机制]]
- 平台：[[Apple AppIntents Schema Protocol 2026]]（同属 iOS 27 官方框架）
- 方法：[[Agent 写回路径 XPIA 风险评估 SOP]]（coerced-intent 是写回路径的另一类风险源）

#标签/Apple #标签/TrustInsights #标签/执行安全 #标签/Coercion
