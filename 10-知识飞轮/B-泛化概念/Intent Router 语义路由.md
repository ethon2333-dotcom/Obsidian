---
type: concept
status: draft
derived_from: "[[AppIntent 跨平台情报简报 2026-07-30]]"
tags: [AppIntent, 语义路由, 端侧Planner, 概念]
aliases: [语义路由]
---

# Intent Router 语义路由

## 一句话定义

**意图路由（Intent Resolution / Routing）** 是把用户自然语言需求映射到「正确的 App 能力 + 正确参数」的过程。2026 的趋势是 **把路由放到端侧小模型 Planner**，由 System Broker 做语义匹配与多 App 编排，而非每请求上云。

## 为什么重要

- 路由延迟与成本直接决定 Agent 体验；端侧路由可做到零单查询成本、毫秒级响应。
- 语义级匹配（IndexedEntity + indexingKey）优于字符串匹配，支持「含义级」消歧。

## 适用边界

- 端侧 Planner 适合单应用 / 窄域 Schema；跨域或低置信场景需升级云端大模型。
- 多 App 声明同类 Intent 时，需 System Broker 的语义冲突裁决优先级（capability / ownership / 用户默认）。

## 证据与例子

- **Apple**：`IndexedEntity` → Spotlight 语义索引，`indexingKey` 标注可检索属性；参数补全走 Parameter Slot-filling，`$label.requestValue("…")` 反向追问缺失槽位。
- **端侧 Planner 架构**：FunctionGemma 270M 本地路由 + 低置信升级 Gemini Flash + Qwen3-Embedding-0.6B 语义缓存学习环，本地优先、随时间降云端依赖（实测见 [[Function Calling 端侧工具调用]]）。
- **跨应用 Chaining**：Siri App Actions / HarmonyOS 意图即服务 / Windows Copilot Actions 均在 Broker 层做多 App 编排。

## 可复用启发

- 采用「**小模型本地路由 + 低置信升级云端**」混合架构，用语义缓存把高频意图留在端侧。
- 路由评估应纳入 SOP（见 [[C-可复用方法/系统级 Intent 路由评估 SOP]]，若未建则补）。

## 深化补充

- **具体路由 API 形态**：Android 侧系统路由由 `AppFunctionManager` 承载——`searchAppFunctions(query)` 做语义检索、`executeAppFunction()` 发起调用，开发者状态用 `APP_FUNCTION_STATE_ENABLED / DISABLED / DEFAULT` 控制可见性，调试可用 `adb shell cmd app_function`；这与 Apple `IndexedEntity` + `indexingKey` 的 Spotlight 语义索引是同一目标的两套机制（见 [[Android AppFunctions 设备侧意图 2026]]、[[Apple AppIntents Schema Protocol 2026]]）。
- **架构级联动**：端侧路由的「小模型 + 语义缓存」范式与 [[Simple Attention Network 无FFN端侧路由]] 的「无 FFN」架构互为印证——路由越规范，Planner 越小。
- **冲突裁决缺口**：多 App 声明同类 Intent 时，目前四平台公开文档均未给出统一的「capability / ownership / 用户默认」裁决 API，仍是各 OS 私有实现。

- [ ] 端侧 Planner（如 SAN）如何处理「低置信 → 升级云端」的握手协议？四平台是否有标准升级接口？
- [ ] 多个 App 抢同一意图（如「订外卖」）时，系统是否向用户暴露选择或默认按 ownership？需一手源核实。
- [ ] 语义路由结果能否被审计留存（呼应 [[数据溯源分级与单调棘轮]] 与 [[Agent Workspace 隔离执行]]）？

## 关联

- 来源：[[AppIntent 跨平台情报简报 2026-07-30]]
- 模式规范：[[Intent Schema Protocol 意图模式规范]] ｜ 执行：[[Function Calling 端侧工具调用]]
- 平台：[[Apple AppIntents Schema Protocol 2026]] ｜ [[HarmonyOS Intents Kit 与 ArkAF 2026]]

#标签/语义路由 #标签/端侧Planner #标签/IntentResolution
