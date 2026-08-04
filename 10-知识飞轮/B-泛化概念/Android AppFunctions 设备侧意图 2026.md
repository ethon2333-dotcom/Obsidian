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

## 2026-07-31 增补（Android 17 正式发布，来源 [[AppIntent 每日情报 2026-07-31]]）

> 修正上节「仅 Android 16+ / 实验预览」的时点：**Android 17 已于 2026-06-16 正式发布**并推送至多数受支持 Pixel，**AOSP 源码已放出**。

- **AppFunctions 正式并入「Android MCP」叙事**：官方表述为「把应用的独特功能作为可编排的**工具**贡献给 **Android MCP**，这是设备端等效于 Model Context Protocol 的功能」；「AI 代理和助理（例如 Google Gemini）可以发现并执行 AppFunctions，以代表用户执行工作流，**并直接访问应用的本地状态**」。
- **Jetpack 库状态：Alpha**（只需为类添加注解 + KDoc 注释）；Gemini 集成仍为**可信测试者私测**。
- **工具链补充**：**测试代理应用**（提供发现/执行 AppFunction 与模拟 AI 智能体集成的界面）；抢先体验计划 `goo.gle/eap-af`；验证命令 `adb shell cmd app_function list-app-functions`。
- **🔑 端侧算力被写进权限模型**：以 Android 17 为目标且需直接访问 NPU 的应用**必须在清单声明 `FEATURE_NEURAL_PROCESSING_UNIT`** —— 端侧 Planner 首次获得 OS 级权限身份（呼应 [[Function Calling 端侧工具调用]]）。
- **系统中介的隐私选择器族（对确认机制意义重大）**：`ACTION_PICK_CONTACTS`（仅临时访问用户选定字段，免 `READ_CONTACTS`）、**系统渲染的位置信息按钮**（仅当前会话授予精确位置）、`ACTION_OPEN_EYE_DROPPER`（系统驱动取色，免屏幕捕获权限）。本质是把敏感授权从「App 长期权限」升级为「**系统代持的一次性确认**」，详见 [[Confirmation UI 安全机制]]。
- **其他安全变更**：`ACCESS_LOCAL_NETWORK` 运行时权限（SDK 37+ 默认禁止本地网络访问）；后量子加密（Keystore 生成 **ML-DSA** 密钥 + **v3.2 混合 APK 签名**）；原生库动态加载须只读（否则 `UnsatisfiedLinkError`）；短信 OTP 延迟（域名不匹配 3 小时 / SDK 37+ 标准短信 3 秒）；证书透明度默认开启；物理键盘不再回显最近输入字符。
- **Gemini 侧落地（Galaxy Unpacked 2026-07-22）**：任务自动化从 2 月 Beta 的少数应用扩至 **40+ App**（购物、餐厅预订、旅行、票务）；同期 Gemini Nano 4；**零代码 UI Automation 早期预览**限 Galaxy S26 与部分 Pixel 10、覆盖外卖/生鲜/打车、**仅美国与韩国**。
- **通道分工明确**：`actions.xml` 已弃用；**built-in intents** 用于「拉起并履约」，**AppFunctions** 用于「带类型参数调用 + 返回结构化结果」，**UI Automation** 只作未适配长尾兜底——「不接入也有覆盖，但失去执行控制权」（见 [[端侧执行通道 GUI 与 MCP 路线之争]]）。

## 可复用启发

- 「设备侧 MCP」是可迁移范式：任何 OS 都能把 App 能力注册为本地 MCP server，由系统 Broker 路由（见 [[DeviceSideMCP 设备侧MCP]]）。
- 高危动作必须「执行前预警 + 用户可接管」，不能静默完成（见 [[Confirmation UI 安全机制]]）。

## 2026-08-02 增补（官方 Agent Skill 四步生命周期，已验证，来源 [[AppIntent 每日情报 2026-08-02]]）

> 08-01 已在「2026-07 增补」高层提及「官方 Agent Skill」。本次用官方文档**验证四步生命周期全貌并补源链接**（developer.android.com/ai/appfunctions + Android 17 博文）。

- **官方确认**：Google「We released an agent skill for AppFunctions」，技能仓位于 AppFunctions skill repository（github.com/android/skills 下 device-ai/appfunctions）。
- **四步生命周期（官方原文）**：
  1. **Discovery**：分析代码库，识别并推荐高价值、适合 AI 编排的功能；
  2. **Implementation & Configuration**：生成 Kotlin 实现，配置系统元数据与 build 依赖；
  3. **KDoc Refinement**：为 AI 智能体与 Android MCP **优化函数/属性文档**，提升 Agent 工具调用准确率（呼应「Schema 越规范，Planner 越小」）；
  4. **Testing & Debugging**：提供 ADB 命令设备端评估调试；另可装 **AppFunctions 测试代理 App** 完整体验端到端工作流。
- **设备侧 MCP 官方澄清（高价值）**：AppFunctions = Android 专属、OS 级、本地执行的 hook；标准 MCP server = 平台无关、依赖云端执行 + 网络往返。开发 AppFunctions 可直接用设备上现有 App 状态，无需在 App 外维护服务。详见 [[DeviceSideMCP 设备侧MCP]]。
- **状态**：仍为**实验性 feature**，仅有限 App 与系统智能体走完整 pipeline；EAP（goo.gle/eap-af）；验证 `adb shell cmd app_function list-app-functions`。⚠️ 具体发布日期随 Android 17（2026-06-16 GA）文档在线，本库记为「Android 17 同期（日期待补）」。

## 2026-08-03 增补：alpha10 编译时入口点 + Registry 硬细节 + 安全路线分歧（来源 [[AppIntent 每日情报 2026-08-03]]）

> 本次直取官方文档补齐此前缺失的 API 级细节，并部分推进挂了 5 天的「六方 Registry/权限 Checklist」。

- **架构级变更**：`1.0.0-alpha10` 引入编译时 `@AppFunctionServiceEntryPoint`（替代 `AppFunctionConfiguration.Provider`）。KSP 生成具体 service 类 + `assets/` 下 XML schema——**Schema 从手写变编译产出**；alpha09→alpha10 迁移由官方 agent skill 自动完成。
- **Registry / 权限硬细节（首次入库）**：`compileSdk ≥ API 36`；服务绑定权限 `BIND_APP_FUNCTION_SERVICE`；Intent action `android.app.appfunctions.AppFunctionService`；Manifest 属性 `android.app.appfunctions.v2` / `app_metadata`；`AppFunctionManager` 不支持返回 null（App 无需自检）；预定义异常 `AppFunctionInvalidArgumentException` / `AppFunctionElementNotFoundException`。
- **运行时动态门控（最被低估的一条）**：`@AppFunction(isEnabled = false)` + 编译器生成的 `XxxIds.CREATE_TASK_ID` 常量 + `AppFunctionManager.setAppFunctionEnabled(...)`——**Registry 是随账号状态实时变化的动态视图，非静态清单**。四平台目前唯一有公开 API 的动态可见性机制（Apple/HarmonyOS/Windows 待补）。验证命令：`adb shell cmd app_function list-app-functions`。
- **🔴 两条安全路线分歧信号**：① 官方明示 **「system agents may process user queries on the server」**——修正本库「local-first」表述，准确说法是「执行在端侧 App 进程内」≠「理解在端侧」。② **破坏性动作确认下放给 App 自己实现**，官方甚至建议「多加一步确认」——与 Apple 系统级 Confirmation UI 路线分歧。详见 [[Confirmation UI 安全机制]] 与 [[Agent Data Injection 数据注入攻击]]。

## 关联

- 来源：[[AppIntent 跨平台情报简报 2026-07-30]]
- 生态阻力：[[国内安卓厂商做 App Intent 的阻力]]
- 兜底执行：[[工业级 GUI Agent 架构（VLM+无障碍树）]]
- 范式：[[DeviceSideMCP 设备侧MCP]] ｜ [[Intent Schema Protocol 意图模式规范]]

#标签/Android #标签/AppFunctions #标签/设备侧MCP
