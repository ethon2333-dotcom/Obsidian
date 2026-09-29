---
date: 2026-09-25
tags: [AppIntent, 每日情报, 速览, 2026-09-25]
source: "https://developer.android.google.cn/jetpack/androidx/releases/appfunctions?hl=zh-cn ; https://developer.android.com/jetpack/androidx/versions/alpha-channel ; https://www.163.com/dy/article/L7M2BLH80553TKK8.html"
importance_score: "★★★★☆（7/10）"
intent_category: "Android AppFunctions alpha12 API 变更 + A2UI 官方落地 + 鸿蒙 agent 生态补强"
---

# AppIntent 每日情报速览 2026-09-25

> [!abstract] 30 秒速览
> - **核心突破**：Android AppFunctions 终于进位到 **`1.0.0-alpha12`（2026-09-23）**——本窗口唯一净新增 OS 框架 API，重点在 Registry 的 **`scope` 作用域** + 执行请求绑定 **`activityId`** + 参数级 **`AppFunctionUriValueConstraint`** + 序列化要求调用方提供**元数据**；同时**破坏性移除 `AppFunctionContext`/`AppFunctionConfiguration`**（首参身份注入对象被删）。另 **A2UI `1.0.0-alpha01`** 官方落地 Android Jetpack，四平台里 Android 率先给出 agent-defined UI 的官方 OS 级库。
> - **关键指标**：alpha12 = AppFunctions 自 alpha11（08-26）以来首个版本号进位；A2UI alpha01 基础 catalog 含 13+ 组件（Button/Image/TextField/Slider/Modal 等）；鸿蒙 9-22 小艺接入**淘宝闪购智能体**实现「一句话点外卖」闭环。
> - **OS Agent 场景**：Android 把 Registry 从「编译期 schema」推向「带作用域的可塑 Registry + 更安全的执行上下文绑定」；A2UI 让 agent 产出 UI 走「结构化 intent + 原生受限渲染」而非生成可执行前端代码，压低注入面。

## ① Schema 定义与语义路由机制

- **AppFunctions alpha12 的 Registry 演进**：`AppFunctionMetadata` 与 `AppFunctionSearchSpec` 新增 **`scope`** 字段——这是四平台意图框架里首个由官方 Jetpack 显式加入元数据/搜索规格的「作用域」维度，直接服务「谁能发现这个函数」的可见性/权限模型；Android 仍是四平台唯一有公开动态可见性 API 的平台（alpha11 的 `getAppFunctionStates` 状态查询 + 现新增 `scope`），详见 [[四平台意图 Registry 来源轴与权限模型对比 2026]]。
- **执行上下文绑定**：`ExecuteAppFunctionRequest` 新增 **`activityId`**，把一次工具调用锚定到具体 Activity/UI 表面，利于确认 UI 与执行审计（与 [[确认机制]] 同方向）。
- **运行时注册仍 experimental**：`registerAppFunction(s)` / `RegisterAppFunctionRequest` / `CallbackAppFunction` 标 `@ExperimentalAppFunctionsApi`，呼应 alpha11 `@AppFunctionSignature` 动态注册走向「运行时可塑 Registry」，但成熟度低、无 GA 日期。
- **A2UI 协议落地**：A2UI 是 Google 自家的 **agent-defined UI 规范（JSONL 文档）**，模型只生成 UI intent、不生成像素/HTML，宿主原生渲染；Android `material3-a2ui` 给出 Button/Image/TextField/Slider/Modal/ChoicePicker 等 13+ 基础组件，原生 Compose 渲染**无需执行任意代码**——四平台里首个明确跨平台（非厂商锁定）的 UI 层协议，见 [[A2UI 生成式UI协议(Google)与鸿蒙落地 2026]]。

## ② 系统安全与用户体验（Confirmation / 隔离 / 防注入）

- **参数级安全约束补强**：alpha12 新增 **`AppFunctionUriValueConstraint`** 公共 API，对 Uri 类型参数/返回值施加 scheme/路径约束，是 AppFunctions 约束族（Int/String/Uri）的参数级安全补强，与「最小权限工具作用域」一致（对照 [[端侧工具调用]] 的端侧 Planner 工具可达性收缩）。
- **序列化元数据信号（谨慎对待）**：`AppFunctionData#serialize` 现要求调用方提供元数据——**可能是 provenance 信号，但更可能是序列化结构元数据**，未必等于「数据从哪来/可不可信」的 intent 来源 provenance；本库「四平台意图 Registry 来源轴全空白（confirmed）」结论**不因此改变**，待官方文档逐字段确认，见 [[四平台意图 Registry 来源轴与权限模型对比 2026]]。
- **破坏性移除的隐含安全影响**：alpha12 **删除 `AppFunctionContext` 与 `AppFunctionConfiguration`**——此前 `AppFunctionContext` 是 Registry 注入调用方身份的位置，其移除削弱了「App 能否对不同 Agent 差异化授权」的追问基础（本笔记 08-03 开放问题），新身份注入机制待 alpha13+ 重定义。
- **鸿蒙 agent 生态补强（UX 侧）**：9-22 小艺接入**淘宝闪购智能体**实现「一句话点外卖」闭环；HarmonyOS 7 公测开放，小艺可调用 2100+ 系统能力、桌面底部 AI 快捷导航条主动服务（复制即触发）——与 [[语义路由]] 端侧 Planner 预测用户意图的主动服务形态一致，但属消费级 UX 非框架 API，见 [[HarmonyOS Intents Kit 与 ArkAF 2026]]。
- **Windows 无 OS 层净新增**：统一 Copilot 桌面 app 9 月中旬铺开属**应用层分发变更**（Chromium 架构、个人/工作账户合一），非 OS 执行总线 API 新增；Copilot Actions/Agent Workspace/ODR/Execution Containers/代码签名自 09-17 以来无变化，见 [[Windows Copilot Actions 与 Agent Workspace 2026]]。

> [!note] 8 概念节点双链
> - [[意图模式规范]] ｜ [[语义路由]] ｜ [[端侧工具调用]] ｜ [[确认机制]] ｜ [[元服务]] ｜ [[隔离执行]] ｜ [[A2A 端侧智能体协议]] ｜ [[XPIA 跨提示注入]]
