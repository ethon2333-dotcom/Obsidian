---
type: concept
status: draft
derived_from: "[[AppIntent 跨平台情报简报 2026-07-30]]"
tags:
  - AppIntent
  - Android
  - AppFunctions
  - 设备侧MCP
---

# Android AppFunctions 设备侧意图（2026）

> 本文聚焦 **Google 官方 AppFunctions 框架（设备端 MCP）**。关于「国内厂商为何难落地类似能力」，见 [[国内安卓厂商做 App Intent 的阻力]]；关于其兜底执行技术，见 [[工业级 GUI Agent 架构（VLM+无障碍树）]]。

## 一句话定义

Android AppFunctions 把 App 的核心能力暴露为 **设备端 MCP（Model Context Protocol）服务器** 的工具，注册进 Android OS 内置 Registry；Gemini 等端侧/云侧智能体经 `EXECUTE_APP_FUNCTIONS` 权限调用，实现「App 退化为 headless 工具、系统 Agent 直接编排」。

## 为什么重要

- **官方设备端 MCP**：比 GUI Agent 点击更可靠（直接调用结构化 API，不受 UI 改版影响）。
- **系统级 Registry**：发现与路由由 OS 统一负责，开发者只需声明工具。
- **接入成本下探**：Agent Skill 可自动产出 Kotlin 胶水代码，降低适配门槛。

## 适用边界

- 需用户授予 `EXECUTE_APP_FUNCTIONS` 权限；敏感动作受系统约束。
- 国内安卓厂商因生态博弈（[[国内安卓厂商做 App Intent 的阻力]]）未必直接采用 Google AppFunctions，多自建军标准或用 GUI Agent 兜底（[[工业级 GUI Agent 架构（VLM+无障碍树）]]）。

## 证据与例子

- **设备端 MCP 模型**：AppFunction = MCP tool，运行在设备侧，由 Android OS Registry 托管发现。
- **权限**：调用需 `EXECUTE_APP_FUNCTIONS`；未授权 App 不出现在智能体工具列表。
- **自动化兜底**：Android UI Automation 通用框架对购买等敏感动作「执行前预警」，用户可经通知或 live view 监控并随时接管（与 GUI Agent 架构互补）。
- **代码生成**：Agent Skill 自动产出 Kotlin 适配代码，呼应「声明式 + AI 辅助生成」趋势。

## 2026-07 增补（实验预览 / Gemini 私测，来源 [[OS PM 近一月情报简报 2026-07-31]]）

- **状态与版本**：实验性预览，API 面可能变动；**自 2026-05 起与 Gemini 集成向可信测试人员私测**；适用 **Android 16+（API 36）**。
- **声明式接入**：`@AppFunction(isDescribedByKDoc = true)` 以 KDoc 驱动工具描述；注解处理器构建期生成 XML Schema，OS 索引；Agent 经 `AppFunctionManager` 查询、`isAppFunctionEnabled(packageName, functionId)` 校验后执行。
- **流程**：Declare → Schema 生成 → OS 索引 → Agent 经 AppFunctionManager 执行。
- **开发提效**：官方 Agent Skill 分析关键工作流生成 Kotlin、优化 KDoc、给 ADB 调试命令；另有**测试智能体**可在模拟智能体环境实验调试；开放抢先体验计划。
- **Google I/O '26 关联**：发布 **Gemma 4** 与 **Gemini Nano 4（Nano 4）** 开发者预览（经 AICore），ML Kit GenAI 将推 Structured Output API。

## 可复用启发

- 「设备侧 MCP」是可迁移范式：任何 OS 都能把 App 能力注册为本地 MCP server，由系统 Broker 路由（见 [[DeviceSideMCP 设备侧MCP]]）。
- 高危动作必须「执行前预警 + 用户可接管」，不能静默完成（见 [[Confirmation UI 安全机制]]）。

## 关联

- 来源：[[AppIntent 跨平台情报简报 2026-07-30]]
- 生态阻力：[[国内安卓厂商做 App Intent 的阻力]]
- 兜底执行：[[工业级 GUI Agent 架构（VLM+无障碍树）]]
- 范式：[[DeviceSideMCP 设备侧MCP]] ｜ [[Intent Schema Protocol 意图模式规范]]

#标签/Android #标签/AppFunctions #标签/设备侧MCP
