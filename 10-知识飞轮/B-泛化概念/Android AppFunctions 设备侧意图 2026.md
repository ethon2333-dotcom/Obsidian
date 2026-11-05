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

- 「设备侧 MCP」是可迁移范式：任何 OS 都能把 App 能力注册为本地 MCP server，由系统 Broker 路由（见 [[MCP 与设备侧 MCP]]）。
- 高危动作必须「执行前预警 + 用户可接管」，不能静默完成（见 [[Confirmation UI 安全机制]]）。
- **把「工具描述质量」当一等工程指标**：Google 用 `isDescribedByKDoc = true` 直接把 KDoc 升格为工具描述来源，并单列一步 KDoc Refinement。迁移结论：**Registry 的召回率上限由描述文本质量决定，不由 API 数量决定**——所以要给描述配 lint 与评测，而不是只配文档规范。
- **Registry 要在 v1 就设计成「动态视图」**：`setAppFunctionEnabled` 让未登录/未开通的能力实时从工具列表消失，既省 Planner 上下文又降误触发率。任何做意图注册表的团队后补这个开关代价极高。

## 2026-08-02 增补（官方 Agent Skill 四步生命周期，已验证，来源 [[AppIntent 每日情报 2026-08-02]]）

> 08-01 已在「2026-07 增补」高层提及「官方 Agent Skill」。本次用官方文档**验证四步生命周期全貌并补源链接**（developer.android.com/ai/appfunctions + Android 17 博文）。

- **官方确认**：Google「We released an agent skill for AppFunctions」，技能仓位于 AppFunctions skill repository（github.com/android/skills 下 device-ai/appfunctions）。
- **四步生命周期（官方原文）**：
  1. **Discovery**：分析代码库，识别并推荐高价值、适合 AI 编排的功能；
  2. **Implementation & Configuration**：生成 Kotlin 实现，配置系统元数据与 build 依赖；
  3. **KDoc Refinement**：为 AI 智能体与 Android MCP **优化函数/属性文档**，提升 Agent 工具调用准确率（呼应「Schema 越规范，Planner 越小」）；
  4. **Testing & Debugging**：提供 ADB 命令设备端评估调试；另可装 **AppFunctions 测试代理 App** 完整体验端到端工作流。
- **设备侧 MCP 官方澄清（高价值）**：AppFunctions = Android 专属、OS 级、本地执行的 hook；标准 MCP server = 平台无关、依赖云端执行 + 网络往返。开发 AppFunctions 可直接用设备上现有 App 状态，无需在 App 外维护服务。详见 [[MCP 与设备侧 MCP]]。
- **状态**：仍为**实验性 feature**，仅有限 App 与系统智能体走完整 pipeline；EAP（goo.gle/eap-af）；验证 `adb shell cmd app_function list-app-functions`。⚠️ 具体发布日期随 Android 17（2026-06-16 GA）文档在线，本库记为「Android 17 同期（日期待补）」。

## 2026-08-03 增补：alpha10 编译时入口点 + Registry 硬细节 + 安全路线分歧（来源 [[AppIntent 每日情报 2026-08-03]]）

> 本次直取官方文档补齐此前缺失的 API 级细节，并部分推进挂了 5 天的「六方 Registry/权限 Checklist」。

- **架构级变更**：`1.0.0-alpha10` 引入编译时 `@AppFunctionServiceEntryPoint`（替代 `AppFunctionConfiguration.Provider`）。KSP 生成具体 service 类 + `assets/` 下 XML schema——**Schema 从手写变编译产出**；alpha09→alpha10 迁移由官方 agent skill 自动完成。
- **Registry / 权限硬细节（首次入库）**：`compileSdk ≥ API 36`；服务绑定权限 `BIND_APP_FUNCTION_SERVICE`；Intent action `android.app.appfunctions.AppFunctionService`；Manifest 属性 `android.app.appfunctions.v2` / `app_metadata`；`AppFunctionManager` 不支持返回 null（App 无需自检）；预定义异常 `AppFunctionInvalidArgumentException` / `AppFunctionElementNotFoundException`。
- **运行时动态门控（最被低估的一条）**：`@AppFunction(isEnabled = false)` + 编译器生成的 `XxxIds.CREATE_TASK_ID` 常量 + `AppFunctionManager.setAppFunctionEnabled(...)`——**Registry 是随账号状态实时变化的动态视图，非静态清单**。四平台目前唯一有公开 API 的动态可见性机制（Apple/HarmonyOS/Windows 待补）。验证命令：`adb shell cmd app_function list-app-functions`。
- **🔴 两条安全路线分歧信号**：① 官方明示 **「system agents may process user queries on the server」**——修正本库「local-first」表述，准确说法是「执行在端侧 App 进程内」≠「理解在端侧」。② **破坏性动作确认下放给 App 自己实现**，官方甚至建议「多加一步确认」——与 Apple 系统级 Confirmation UI 路线分歧。详见 [[Confirmation UI 安全机制]] 与 [[Agent Data Injection 数据注入攻击]]。

## 最新进展 / 一手来源（2026）

- **官方定位（AppFunctions 概览页，2026-08-06 复核）**：「AppFunctions 是 Android 平台 API，并配有 Jetpack 库，旨在**简化 Android MCP 集成**；它使应用能像**设备端的 MCP 服务器**一样运行」；调用方需 `EXECUTE_APP_FUNCTIONS`，可以是智能体、应用与 Gemini 等助手；**适用于 Android 16 或更高版本**。⚠️ 页面仍挂「Experimental / 实验性预发布，API 面可能变更」横幅——**GA 日期仍待补**。来源：<https://developer.android.google.cn/ai/appfunctions>（canonical `developer.android.com/ai/appfunctions`）
- **Android 17 博文原文复核**：「把应用的独特功能作为可编排的『工具』贡献给 **Android MCP（设备端等同于 MCP）**」；Jetpack 库为 **Alpha**；Gemini 集成为**受信任测试者私测**；示例即 `@AppFunction(isDescribedByKDoc = true) suspend fun createNote(appFunctionContext: AppFunctionContext, ...)`——注意**首参恒为 `AppFunctionContext`**，这是 Registry 注入调用方身份的位置。来源：<https://developer.android.google.cn/blog/posts/android-17-is-here>
- **FAQ 里两条被低估的官方口径**：① 「只有**有限数量**的应用与系统智能体能访问完整 pipeline」——即使实现正确也可能被系统侧挡住；② 官方给的自检路径只有 `adb shell cmd app_function list-app-functions`，**没有面向终端用户的可见性 UI**（对照 Windows 有 `odr agent-info list`，见 [[Windows Copilot Actions 与 Agent Workspace 2026]]）。

## 反例与边界

- **「不受 UI 改版影响」只在已适配的能力上成立**：AppFunctions 覆盖的是开发者主动声明的少数高价值动作；长尾仍靠 UI Automation 兜底，而兜底通道恰恰**完全受 UI 改版影响**。所以「比 GUI 更可靠」的正确表述是「**已适配面更可靠，未适配面反而更脆弱**」（见 [[端侧执行通道 GUI 与 MCP 路线之争]]）。
- **「设备侧 = 隐私」是错的**：官方明示 system agents **may process user queries on the server**。执行在端侧 App 进程内 ≠ 理解在端侧——把 AppFunctions 当隐私论据会误导架构决策（见 [[Agentic OS 意图调度内核]]）。
- **确认下放给 App 是安全反例**：官方建议「破坏性动作可自己多加一步确认」，等于把护栏交给最有动机省略它的一方（转化率与确认步骤天然冲突）。这在 ADI / 提示注入场景下直接失效——攻击者只需选择那些没自加确认的 App（见 [[Agent Data Injection 数据注入攻击]]、[[Confirmation UI 安全机制]]）。
- **生态前提不成立时整个范式失效**：国内 Android 缺 GMS/Gemini 与统一 Registry，AppFunctions 的「系统统一发现」价值归零，只能各厂商自建（见 [[国内安卓厂商做 App Intent 的阻力]]）。

## 开放问题 / 未决

- [ ] AppFunctions 何时脱离 experimental / GA？「有限数量的应用与系统智能体」的准入标准是什么？官方未公开（**待补**）。
- [ ] 多个 App 声明语义重叠的 AppFunction 时，`searchAppFunctions` 的排序与裁决规则是什么？官方文档未给（呼应 [[Intent Router 语义路由]] 的冲突裁决缺口）。
- [ ] `AppFunctionContext` 是否携带可验证的调用方身份（签名/包名可信度），使 App 能对不同 Agent 差异化授权？**待一手核实**（关联 [[Agent 身份与硬件级审批]]）。

## 与其他概念的关系

- **上游**：[[Intent Schema Protocol 意图模式规范]]（AppFunctions 是其 Android 实现）｜ [[MCP 与设备侧 MCP]]（AppFunctions 是设备侧 MCP 的 OS 原生特例）｜索引 [[意图框架·跨体系索引 MOC]]、[[Intent Routing Stack 六方意图路由分层对照 2026]]。
- **对立**：[[Apple AppIntents Schema Protocol 2026]]——确认责任「下放 App」vs「系统统一拦截」；Schema 生成「KDoc 自然语言驱动」vs「预定义参数签名驱动」，是两条相反的赌注。
- **互补**：[[工业级 GUI Agent 架构（VLM+无障碍树）]] 与 [[端侧执行通道 GUI 与 MCP 路线之争]]（长尾兜底）｜ [[Function Calling 端侧工具调用]]（`FEATURE_NEURAL_PROCESSING_UNIT` 让端侧 Planner 有了 OS 级权限身份）。
- **特例**：[[Agent Skills 技能范式 2026]]——AppFunctions 官方 agent skill 是「用 Skill 生产 Schema」的反向用法，Skill 在这里是开发期工具而非运行期能力。

## 2026-08-15 增补：AppFunctions-backed Gemini 多步首现真机有限预览（Galaxy S26 + Pixel 10）

> 来源：[[AppIntent 每日情报 2026-08-15]]。

blognone 等报道：Galaxy S26 / Pixel 10 将带来 AppFunctions + 本地 MCP 支撑的多步 Agent 能力有限预览 / beta，区域 US/Korea，隐私口径与既有一致（设备侧处理优先）。Android 17 官方博客 EAP 入口 `goo.gle/eap-af`。

**结论**：这是 AppFunctions 首次出现**真机可用性信号**（而非 GA），标志 Android 端侧意图总线从「API 定义」走向「真机落地验证」。其意义不在能力新增，而在**把"设备侧 MCP 是否真的能跑在用户手机上"从假设推进到可观测**——此前本库所有 AppFunctions 条目都卡在「实验态 / 私测」层面，缺一个真机落点。

## 关联

- 来源：[[AppIntent 跨平台情报简报 2026-07-30]]（上游：一手日报沉淀）
- 索引：[[意图框架·跨体系索引 MOC]]（上游枢纽）
- 生态阻力：[[国内安卓厂商做 App Intent 的阻力]]（对立：官方范式在国内的失效条件）
- 兜底执行：[[工业级 GUI Agent 架构（VLM+无障碍树）]]（互补：未适配长尾）
- 范式：[[MCP 与设备侧 MCP]]（上游）｜ [[Intent Schema Protocol 意图模式规范]]（上游）

## 2026-08-26 增补：Samsung Gallery + Gemini 真机闭环 + UI Automation 兜底框架（来源 [[AppIntent 每日情报 2026-08-26]]）

> 接续 08-15 的 Galaxy S26 / Pixel 10 真机有限预览。本期补**首个公开的真机部署样本**与配套的**非 AppFunctions 兜底通道**。

- **Samsung Gallery + Gemini 真机闭环（Galaxy S26 系列）**：用户可说「显示 Lisa 旅行照片」→ Gemini 处理请求 → 触发 Samsung Gallery 的 AppFunction → 结果直接呈现在 Gemini app 内，**无需切换应用**；语音/文本输入，检索内容可用于后续动作（如把选中图分享到消息）。这是 AppFunctions 首个公开的「真机跑通端到端」样本，标志 Android 端侧意图总线从「API 定义」走向「用户可感知的闭环」。
- **UI Automation 框架（非 AppFunctions 兜底通道）**：对未实现 AppFunctions 的 App，Android 开发**通用 UI 自动化框架**，让 Gemini 在应用内执行多步任务（长按电源键触发，Gemini app 内 beta）；首发支持外卖/生鲜/打车（美韩），如「下单定制餐食 / 协调多段打车 / 重下杂货」；执行前**预警 + 用户可随时接管**，敏感动作（如购买）**执行前确认**。
- **通道分工再确认**：`built-in intents`（拉起履约）/ `AppFunctions`（带类型参数 + 结构化返回）/ `UI Automation`（长尾兜底，失执行控制权）三层并存——「不接入也有覆盖，但失去执行控制权」（见 [[端侧执行通道 GUI 与 MCP 路线之争]]）。

→ **对 OS PM 的含义**：AppFunctions 的价值此前停留在「实验态/私测」假设，Galaxy S26 样本把它推进到「可观测真机闭环」；但覆盖仍限三星 Gallery + 美韩 + 精选类目，**生态广度仍是最大未知数**（呼应 08-03 节「有限数量应用与系统智能体」准入）。UI Automation 兜底则保证「未适配长尾不裸奔」，与鸿蒙 GUI 双轨（[[HarmonyOS Intents Kit 与 ArkAF 2026]]）殊途同归。⚠️ Samsung Gallery 闭环为厂商披露/媒体整理，具体 App 名与成功率**待一手核实**。

## 2026-09-01 增补：alpha11 动态注册 + 门控 API 迁移 + DMA 跨助手开放（来源 [[AppIntent 每日情报 2026-09-01]]）

> 接续 08-03/08-26。本期补 **官方 Jetpack Release Notes 的 `alpha11`（2026-08-26）净新增 API**，并补 **DMA 监管迫使 Registry 跨助手开放** 这一跨平台维度。

**A. `1.0.0-alpha11`（2026-08-26，官方 Release Notes，窗口内净新增）**
- **`@AppFunctionSignature`（experimental public API）**：支持**通过 Jetpack 动态注册 AppFunction**（b/501032667）——此前函数须编译期静态声明，现可在运行时注入签名。Registry 从「编译期 schema」走向「运行时可塑」。
- **`AppFunctionState` + `AppFunctionManager#getAppFunctionStates` 取代 `AppFunctionMetadata#isEnabled`**（b/494238383）：**元数据与状态彻底分离**——本库 08-03 记的 `setAppFunctionEnabled` / `isAppFunctionEnabled` 动态门控**机制仍在，但 API 形态迁移到 state-based 查询**。
- 其余：`getAppFunctionActivityStates`（b/542075714）、`ExtensionsAppFunctionService`（sidecar 支持，b/524941402）、`observeAppFunctions` 对齐平台 API。
- Bug 修复：修复 OOBE 阶段调用 `setAppFunctionEnabled` 因缺运行时元数据崩溃（b/536750020）——印证动态门控已进真机初始化路径。
- ⚠️ alpha11 前的 alpha10（2026-07-01，`AppFunctionServiceEntryPoint`）已录于 08-03；alpha11 为窗口内唯一净新增版本。

**B. 通道对比（官方口径补全）**：AppFunctions = 设备内注解 Kotlin 函数 + KDoc（On device，运行在 App 进程内）；Computer Control = 设备内驱动 UI 虚拟窗口（On device，无需改代码）；Remote MCP = 云端 HTTP 服务（Cloud）。三者在「运行位置 / 实现成本 / 平台覆盖 / 权限闸门」四轴正交——AppFunctions 让你把操作变「故意的、类型化、可观测」，Computer Control 让助手无论你是否适配都能操作 UI。选型见 [[端侧执行通道 GUI 与 MCP 路线之争]]。

**C. DMA 强制跨助手开放（监管维度）**：欧盟 DMA 要求 Google 在 **2027-08 前**向竞品助手（ChatGPT/Claude/欧洲本土）开放 11 项 Android AI 能力；AppFunctions Registry 使函数可被**任一认证助手**发现，`EXECUTE_APP_FUNCTIONS` 在 EU 下沉为「认证闸门」。详见新建 [[AppFunctions 跨助手可发现性与 DMA 强制开放 2026]]；具体 11 项清单与官方文本措辞**待补**。

#标签/Android #标签/AppFunctions #标签/设备侧MCP

## 2026-09-16 增补：I/O '26 路由/编排原语库内空白补漏（来源 [[AppIntent 每日情报 2026-09-16]]）

> 接续本笔记 09-01（alpha11）/ 08-26（真机闭环）/ 08-15（真机预览）。本期补 **Android I/O '26（2026-05）官方博客**中三条此前库内未单列为「Android 路由/编排原语」的能力，作库内空白补漏（标真实日期，避免下次检索误判为「新发布」）。

- **① Firebase AI Logic Hybrid Inference（端云推理路由原语）**：新 API 提供 on-device 与云端之间的**显式路由能力**，可设 `PREFER_ON_DEVICE / PREFER_CLOUD / ONLY_ON_DEVICE / ONLY_CLOUD` 等编排模式——与 iOS 27 Foundation Models 多模型路由（[[Apple AppIntents Schema Protocol 2026]]）方向同构，是 Android 侧「端云推理路由」的一等原语。
- **② ADK for Android（跨端+云多智能体编排）**：首版可用，跨 device 与 cloud 模型构建多智能体工作流，管理 orchestration / context handling / sessions between agents——把「跨应用 Intent 工作流」从单 Agent 调用扩展到多 Agent 协作。
- **③ A2UI Jetpack Compose Renderer（生成式 UI 原生渲染）**：新 A2UI 库让 agent「speak UI」，经 Jetpack Compose Renderer 把 A2UI 消息**自动渲染为原生 UI 组件**——与 09-12 高德 AGenUI 基于 Google A2UI（[[A2UI 生成式UI协议(Google)与鸿蒙落地 2026]]）形成框架层呼应，补全「意图→UI」闭环。

→ 对 OS PM：Android 的「系统级意图框架」现在在「语义路由」层有 I/O '26 明示的端云路由原语（Hybrid Inference）+ 多智能体编排（ADK）+ 生成式 UI（A2UI Renderer），与另三家对照更完整；但 AppFunctions 仍守 alpha11、无 GA 日期，路由原语 ≠ Registry API（二者互补不替代）。

⚠️ 层级纪律：上述为 I/O '26（2026-05）已发布内容，非本窗口新 API；本次仅作库内空白补漏，标真实日期。

## 2026-09-17 增补：Android 17 GA 确认 + AppFunctions 进 Android 17 智能系统叙事（compileSdk 37，来源 [[AppIntent 每日情报 2026-09-17]]）

> 接续 09-16 的 I/O '26 原语补漏。本期确认 **Android 17 已正式发布**（developer.android.com/ai/intelligence-system 与 android-17-is-here 官方博客同叙事），并把 AppFunctions 明确纳入 Android 17 的「智能系统」能力栈；同时第三方复核确认 **AppFunctions 仍 `1.0.0-alpha11`（2026-08-26）、无 alpha12**。

- **Android 17 把 AppFunctions 放进「Intelligence System」主线**：官方 `developer.android.com/ai/intelligence-system` 将 AppFunctions 与 Remote MCP server、Computer Control 并列为「让系统 agent（如 Gemini）跨本地应用与 web 服务安全编排」的三条新能力；AppFunctions 仍是「把 App 独特功能作为设备端 MCP 可编排工具」的入口。
- **compileSdk / targetSdk 建议更新**：第三方复核（androidboss，Reviewed 2026-09-06）给出 **compileSdk = 37 / targetSdk = 36** 的当前推荐基线（alpha11 `androidx.appfunctions:appfunctions` + KSP compiler），并提示「alpha 库版本常变、发布前复查 release page」——本库 08-03 记的 `compileSdk ≥ API 36` 现升为 37。
- **API 面无变化**：窗口内**无 alpha12**；alpha11 的 `@AppFunctionSignature` 动态注册 + `AppFunctionState` 取代 `isEnabled` 仍是最新净新增（见本笔记 09-01 增补）；Gemini 集成仍「受信任测试者私测」。
- → 对 OS PM：Android 17 GA 把「设备侧意图框架」从实验叙事正式抬进 OS 主版本，但 **AppFunctions 自身仍是 alpha、未 GA**——「框架进主版本」≠「API 稳定」，开发者仍须按 alpha 节奏跟版本（延续本笔记「AppFunctions 何时 GA 待补」待办）。

⚠️ 诚实标注：Android 17 具体 GA 日期在官方博客为「现已发布」表述，第三方镜像未给精确日；AppFunctions 仍 alpha11 / compileSdk 37 为第三方复核+官方 release page 一致结论，具体 Android 17 GA 日待补。

## 2026-09-21 增补：AppFunctions 无 alpha12 + App Functions Manager 安全护栏信号（来源 [[AppIntent 每日情报 2026-09-21]]）

> 接续 09-17 的「Android 17 GA 确认 + AppFunctions 仍 alpha11、无 alpha12」。本期确认**窗口内 alpha12 仍未发布**，并补一条**低置信的「执行安全」信号**——Google 被报道在 App Functions Manager 框架层嵌入 agent 安全护栏。

- **alpha12 仍未发布**：窗口内 Android AppFunctions 仍守 **`1.0.0-alpha11`（2026-08-26）**，无 alpha12；`@AppFunctionSignature` 动态注册 + `AppFunctionState` 取代 `isEnabled` 仍是最新净新增（见本笔记 09-01）。
- **「安全笼 / Safety Cage」信号（★5/10，低置信，待官方 SDK 注释复核）**：第三方分析（ai.jp.net，09-21）称 Google 已把一套 AI agent 安全框架**深度嵌入 Android OS**，核心组件是 **App Functions Manager framework**，目前**仅开发者文档与 SDK release notes 有暗示**、尚未面向用户；定位是「让自主 agent 规划/预订等任务时不损坏设备」。→ 这与本库已录的 AppFunctions 权限模型（`EXECUTE_APP_FUNCTIONS` 闸门 + `AppFunctionState` 门控）方向一致，但**尚未在官方 SDK release notes 逐字确认「安全笼」是新增机制还是对既有门控的复述**；且它属于**执行安全**（防 agent 越权），不是意图框架 API 新增。
- → 对 OS PM：Android 在「设备侧意图框架」的执行安全上仍走「权限闸门 + 状态门控」路线；若「App Functions Manager safety cage」被官方确认，将是四平台里**又一处 OS 内建 agent 安全护栏**信号（与 Windows ODR / Agent Workspace、Apple Session 347 风险元数据、HarmonyOS 可信协商并列），但当前仅二手分析，**须 learn.microsoft.com / Android 开发者文档逐字复核**后才有收录价值。
⚠️ 诚实标注：「safety cage」来自 ai.jp.net 二次分析（援引开发者文档/SDK 注释暗示），非 Google 官方公告；具体机制、是否等价于既有 `AppFunctionState` 门控、API 名均待补。Android 18（2027）AI-native 传闻（thenextgentechinsider，持续 Canary）属前瞻、低质，已丢弃不收录。

## 2026-09-25 增补：alpha12 净新增 API（scope / activityId / serialize 元数据 / Uri 约束 + 破坏性移除 AppFunctionContext，来源 [[AppIntent 每日情报 2026-09-25]]）

> 接续 09-21「alpha12 仍未发布」与 09-01「alpha11 动态注册」。本期 **官方 Jetpack Release Notes 确认 `1.0.0-alpha12`（2026-09-23）发布**——这是自 alpha11（2026-08-26）以来首个版本号进位，含多项对 Registry/权限/执行上下文有影响的 API 变更。

**A. `1.0.0-alpha12`（2026-09-23，官方 Release Notes，窗口内净新增）**
- **`scope` 字段加入 `AppFunctionMetadata` 与 `AppFunctionSearchSpec`（I4344c）**：Registry 元数据与搜索规格新增 **`scope` 维度**——四平台意图框架里**首个由官方 Jetpack 显式加入元数据/搜索的「作用域」字段**，直接服务 Registry 的**可见性/权限模型**（谁能发现这个函数）。→ 更新 [[四平台意图 Registry 来源轴与权限模型对比 2026]]「运行时动态可见性 API」与「权限/Registry 模型」行：Android 仍是唯一有公开动态可见性 API 的平台，现新增 scope 维度（具体语义待官方文档逐字段确认：是调用方可见性作用域还是功能分类域）。
- **`activityId` 加入 `ExecuteAppFunctionRequest`（I6ac86）**：把函数执行请求**绑定到一个 Activity 上下文**——执行安全相关：把「一次工具调用」锚定到具体的 UI 表面/Activity，便于确认 UI 与执行审计（与 [[Confirmation UI 安全机制]]「执行须绑定可感知上下文」同方向）。
- **`AppFunctionData#serialize` 现要求调用方提供元数据（I61eca）**：序列化须由调用方附带元数据。**可能是来源/可信度轴（provenance）的信号，但须谨慎**——此处「元数据」更可能是序列化结构元数据，未必等于「数据从哪来/可不可信」的 provenance；本库「四平台意图 Registry 来源轴全空白」结论（[[四平台意图 Registry 来源轴与权限模型对比 2026]]）**不因此改变**，待官方文档逐字段确认。
- **`AppFunctionUriValueConstraint` 作为公共 API 加入**：对 Uri 类型参数/返回值施加约束（如限制 scheme/路径），是**参数级安全约束**（防路径穿越/限制可访问 URI 范围），补足此前仅 `IntValueConstraint` / `StringValueConstraint` 的约束族。
- **运行时注册 API 标 `@ExperimentalAppFunctionsApi`（Idb2ca）**：`registerAppFunction` / `registerAppFunctions` / `RegisterAppFunctionRequest` / `CallbackAppFunction` 显式标记 experimental——呼应 09-01 `@AppFunctionSignature` 动态注册走向「运行时可塑 Registry」，但成熟度仍低。
- **破坏性变更：移除 `AppFunctionContext` 与 `AppFunctionConfiguration`（I9dd8f）**：此前 07-31/Android 17 博文示例首参恒为 `appFunctionContext: AppFunctionContext`（Registry 注入调用方身份的位置）、`AppFunctionConfiguration` 承载配置——**两者在 alpha12 被删除**。这是 **alpha→1.0 前的 API 震荡信号**，意味着开发者须改写法；也削弱了本笔记 08-03 开放问题「`AppFunctionContext` 是否携带可验证调用方身份」的追问基础（该对象被移除，身份注入位置待 alpha13+ 重定义）。
- 另：新增内联具体化 `getHandleAppFunctionRequestAdapter` 重载（Ic1b4e）。
- 含义：AppFunctions 仍 **experimental / 无 GA 日期**；alpha12 把 Registry 的**作用域（scope）+ 执行上下文（activityId）+ 参数约束（Uri）+ 序列化元数据**四块同时推进，方向是「更可控的 Registry 与更安全的执行」，但 API 仍在剧烈变动期（破坏性移除首参对象即为证）。

**B. 诚实标注**
- alpha12 的 `scope` 语义、`serialize` 元数据字段定义均**待 developer.android.com/ai/appfunctions 官方文档逐字段确认**；`scope` 是否等于「调用方可见性/权限作用域」、还是「功能分类域」影响搜索召回，须以官方文档为准。
- `AppFunctionContext` / `AppFunctionConfiguration` 移除后，调用方身份注入的新机制（如有）待 alpha13+ 或官方指南。
- 本次为官方 Release Notes 直查确认（developer.android.google.cn/jetpack/androidx/releases/appfunctions），非二手。

## 2026-10-02 晚增补：Android 17 企业策略可关 AppFunctions 数据（setAppFunctionsPolicy / APP_FUNCTIONS_DISABLED，跨平台治理收敛，来源 [[AppIntent 每日情报 2026-10-02]]）

> 接续 09-25「alpha12 净新增 API」。本期补**一个企业/治理层信号**（非框架 API 新增，但属 AppFunctions 执行边界的管控面）——与晨间跑（[[AppIntent 每日情报 2026-10-02]]）的 Windows 连接器策略治理构成跨平台收敛。⚠️ 口径：iseC7 引 Google Android 17 企业页（09-16 更新），非 24h 窗口，作治理面 corroboration。

**① Android 17 企业管控对 AppFunctions / AI 自动化**
- **`setAppFunctionsPolicy` + 标志 `APP_FUNCTIONS_DISABLED`**：管理员可**全局禁用 AppFunctions 数据给 on-device agents**——authorized assistant apps 经 AppFunctions 框架收到的设备级数据，在工作 Profile 默认不返回，企业可一键关。
- **`setNearbyAppStreamingPolicy`**：在 COPE 设备的个人 Profile / 全托管设备**整体关闭 AI 自动化**（Agent 跨 App 工作流编排）。
- 工作 Profile 作天然隔离边界：工作侧数据默认不进 AppFunctions 通道，BYOD 个人侧由用户决定。
- 另：Certificate Transparency 默认开、ACCESS_LOCAL_NETWORK 新运行时权限（API 37）等通用企业加固。

**② 对 OS PM 的含义：跨平台「agent 执行边界可经 MDM 治理」收敛**
- **Google**：用 `APP_FUNCTIONS_DISABLED` 把「AppFunctions 数据给 agent」作为可关闭开关（默认工作 Profile 不返回）。
- **Microsoft**（晨间跑）：用 `ConfigureAgentConnectors` / `AgentConnectorAccessPolicy`（Allow-list）+ `AgentConsentDuration` 把「agent 可用 MCP server」白名单化、授权限时——但**仅企业/教育/IoT 企业版**，家庭/专业版不可控。
- → 二者**方向相反但同构**：都把「agent 能接什么数据/工具」从应用层决策升为**企业管控面**；Google 偏「默认关 + 开关」，Microsoft 偏「白名单 + 限时授权」。这是四平台里 Android/Windows 两支在「agent 执行边界治理」上的首个对照样本，补 [[四平台意图 Registry 来源轴与权限模型对比 2026]]「权限/Registry 模型」行的治理维度。

⚠️ 诚实标注：Android 17 企业页 09-16 更新、非 24h；`setAppFunctionsPolicy`/`APP_FUNCTIONS_DISABLED` 具体语义与是否覆盖 Gemini 私测通道待 developer.android.com/ai/appfunctions 官方文档确认；与 Windows 治理面为治理层对照，非 OS 执行总线 API 新增。

## 2026-10-05 增补：Android Context Engine（Android 18 proactive caller of AppFunctions）+ Intelligence System 框架（来源 [[AppIntent 每日情报 2026-10-05]]）

> 接续 09-25「alpha12 净新增 API」与 10-02 晚「企业策略可关 AppFunctions 数据」。本期补 **一个语义路由层的新维度**——AppFunctions 首次出现 **OS 原生的 proactive 调用方**（Android Context Engine），并补 **Android 18 被正式定位为「Intelligence System」** 的框架信号。⚠️ 层级：来自 Android Dev Summit 2026（10-28~29）公告 cluster + 第三方解读，**非 Android 开发者文档逐字 API**，属前瞻信号（★6/10，低于 alpha 级 API 变更）。

**A. Android Context Engine = AppFunctions 的第三类调用方（proactive）**
- **机制**：Android 18 新增**后台服务**，持续追踪 user intent / screen context / app tasks，**在用户开口前就主动行动**（proactive, not reactive）。它是 AppFunctions 的新一类 caller——此前 caller 集 = {Gemini, 持 `EXECUTE_APP_FUNCTIONS` 的第三方 agent}，现加入 **OS 原生 Context Engine** 作 proactive 编排者。
- **例**：notes app 看到购物清单 → 主动提议加购物车；检测到下班发伴侣消息 → 主动提议自动化。这不是 chatbot 响应 prompt，而是「OS 级 agent 看着并行动」。
- **对端侧意图路由的含义**：Android 的「语义路由」从「被动响应用户指令」升级为「OS 主动观测上下文并提议/执行」——与 Apple 主动式 App Intents 分发（Messages「加到提醒事项」）、Windows Copilot Vision、鸿蒙小艺导航条「复制即触发」形成**四平台主动式意图路由收敛**；但 Android 这次由**独立 OS 后台服务（Context Engine）**驱动，而非单层 UI 触发。详见 [[Intent Router 语义路由]]。

**B. Android 18 = Intelligence System 框架**
- Gemini Nano v3 作为 **resident on-device model** 与常驻 App 并列驻内存（**12GB RAM 下限**）；旧 Google Assistant 组件 deprecation，Gemini 成系统服务底层（非上层 App）。
- AppFunctions 声明机制不变（`@AppFunction` + `@AppFunctionSerializable` → KSP 生成 XML → OS 索引 → agent 经 `AppFunctionManager` 发现执行），仅 caller 多出 Context Engine。
- Dev Summit 2026（10-28~29, Bay View）议程**首次把 Android 18 摆上台面**；AppFunctions 被定位为「maturing in Android 18」，summit session 预期 signal **production readiness for Android 18**（非 GA 承诺）。

**C. 权限/确认边界在 proactive 场景下的风险放大（呼应 [[确认机制]] [[Confirmation UI 安全机制]]）**
- `EXECUTE_APP_FUNCTIONS` 仍是「一次性 blanket grant、非 per-function」；在 **proactive-before-ask** 语境下，Context Engine 可能基于上下文发起调用而用户未显式授权该次动作，**确认边界更模糊**——这是 Android「确认下放 App」路线在主动式场景下的风险放大。
- 与 Microsoft Taxonomy v2.0（2026-04/06，非本窗口）consent-architecture hardening 同构：deterministic invocation / compound-action decomposition / semantic summarization of approval / tiered approval。proactive caller 更需要「确定性调用确认」而非「agent 自行决定何时弹窗」。

**D. DMA 时间线 consolidation（已录 [[AppFunctions 跨助手可发现性与 DMA 强制开放 2026]]，本次补具体锚点）**
- 欧盟 2026-07-16 绑定规格决定：11 项 Android AI 能力（含 AppFunctions）须于 **Android 18 前、2027-08-01 前**向第三方认证助手开放；并发 hotword 检测推至 Android 19（2028-08-01）。

⚠️ 诚实标注：Android 18 仍 Canary / 未 GA；Android Context Engine 为 Dev Summit 公告 + 第三方解读（dev.to/byteiota/beebom/streamingmeme），**非 Android 开发者文档逐字 API**；具体 API 名、是否独立系统 service、与 `AppFunctionManager` 调用关系、是否受 `EXECUTE_APP_FUNCTIONS` 同一闸门约束**待 developer.android.com/ai/appfunctions 官方文档确认**；Dev Summit 为 2026-10-28 召开、非已发生发布。

## 2026-10-09 增补（2026-10-13 二次复核确认：alpha13 确为真实发布，10-10 更正段已被推翻）：AppFunctions `1.0.0-alpha13`（函数侧访问限制 `@AppFunctionAccessLevel` + 重命名，纠正 10-08 漏捕，来源 [[AppIntent 每日情报 2026-10-09]]）

> 接续 09-25「alpha12 净新增 API（`scope` + `serialize` + `AppFunctionUriValueConstraint`）」与 10-02 晚「企业策略可关 AppFunctions 数据」、10-05「Context Engine proactive caller」。本期由官方 Jetpack Release Notes 确认 **AppFunctions `1.0.0-alpha13`（2026-10-07 发布）**，上一轮（10-08）误判「alpha12 无 alpha13」未捕获，本运行纠正。

**① 权限模型第三个原语：`@AppFunctionAccessLevel`（access restriction setting）**
- alpha13 新增 `@AppFunctionAccessLevel` 注解，**在「函数侧」声明访问限制**——与既有的「调用方持 `EXECUTE_APP_FUNCTIONS` 权限」（alpha 以来）+「函数可见性 `scope`」（alpha12）构成 AppFunctions 权限模型三向约束：**谁能调（caller 权限）/ 谁能看见（scope 可见性）/ 函数自身允许谁访问（access level）**。
- 这是四平台设备侧 MCP / 意图 Registry 里**首个「函数自身声明可访问性」原语**；此前 Android 仅 caller 侧 + 可见性侧，缺函数侧自声明。
- ⚠️ 级别语义待确认：官方 Release Notes 仅写「support access restriction setting」，**未展开 @AppFunctionAccessLevel 的级别定义**（如 public/protected/same-app/system 等）。确切语义待 `developer.android.com/ai/appfunctions` 官方文档逐字段确认（延续 09-25 `scope` 纪律，不猜测级别）。

**② 破坏性重命名（迁移注意）**
- `@AppFunction` 注解 → **`@AppFunctionDeclaration`**（I4b15d）：开发者标注名变更，需随 KSP 编译器插件同步迁移。
- `ObserveAppFunctionsEvent` → **`AppFunctionsChangeEvent`**（Iec918）：运行时变更事件重命名。
- `AppFunctionService` 现可获取 **`AppFunctionMetadata`**（If1117）：服务侧执行时可按元数据做策略/审计。
- Bug Fixes：`AppFunctionData` 支持全部内建 proxy 类型（LocalDate / LocalTime / Instant / ZoneId）。

**③ 与来源轴结论的关系**
- `@AppFunctionAccessLevel` 是**访问/权限维度**，非「数据从哪来、可不可信」的来源/provenance 轴——本库最高优先待办「来源轴四平台全空白」结论**不因此改变**。详见 [[四平台意图 Registry 来源轴与权限模型对比 2026]] 10-09 增补。

⚠️ 诚实标注：alpha13 发布于 2026-10-07（落在上轮窗口边缘），由本运行直查官方 Release Notes + alpha-channel 确认；`@AppFunctionAccessLevel` 级别语义待官方文档；`AppFunctionDeclaration` 重命名对既有 `@AppFunction` 标注代码的迁移影响待社区/官方迁移指南确认。

## 2026-10-10 更正：alpha13 记载疑似误记，最新官方版本仍为 alpha12（2026-09-23）

> 来源：[[AppIntent 每日情报 2026-10-10]]。本段纠正本笔记 10-09 增补段（及其引用的 10-09 A 笔记）所载 `1.0.0-alpha13`（2026-10-07）相关记录。

- **二次核验结论（2026-10-10）**：直查官方 `developer.android.com/jetpack/androidx/releases/appfunctions` 发布页 + `@AppFunction` / `AppFunctionSchemaDefinition` API Reference，**最新版本仍为 `1.0.0-alpha12`（2026-09-23）**，**无 alpha13**。`@AppFunction` 注解仍标注「Added in 1.0.0-alpha12」，并未被重命名为 `@AppFunctionDeclaration`；`@AppFunctionAccessLevel` 在官方源不可见。
- **对 10-09 段的影响**：该段所述「`@AppFunctionAccessLevel` 函数侧访问限制原语」「`@AppFunction`→`@AppFunctionDeclaration` 重命名」「`ObserveAppFunctionsEvent`→`AppFunctionsChangeEvent` 重命名」均**未能从官方源 corroboration，疑似误记**，本笔记不再将其作为已确认事实引用。AppFunctions 权限模型的「三向约束（caller 权限 + scope 可见性 + 函数侧 access level）」推论**降级为待官方确认**，当前可确认的权限模型仍维持 alpha12 的「`EXECUTE_APP_FUNCTIONS` 闸门 + `scope` 可见性 + `AppFunctionState` 状态门控」三块（见本笔记 09-01 / 09-25 增补）。
- **当前可确认最新净新增**：仍是 **alpha12（2026-09-23）**（scope / activityId / serialize 元数据 / AppFunctionUriValueConstraint / 移除 AppFunctionContext），已录于本笔记 09-25 增补；**alpha13 及之后版本在 2026-10-10 时点官方源均未出现**。
- **对 dedup / 后续跑的影响**：未来每日跑对 Android 侧应以「官方最新 = alpha12（09-23）」为基线检索 alpha13+，而非以 10-09 误记的「alpha13 已捕获」为基线，避免漏检真正的 alpha13/alpha14 发布。

⚠️ 诚实标注：本更正基于 2026-10-10 对官方发布页与 API Reference 的 WebSearch 直查（WebFetch 直连失败，以搜索索引快照 + API Reference 交叉确认）；若 Google 后续发布 alpha13 并回填发布页，应以新发布页为准，本笔记届时再更新。

## 2026-10-13 复核（推翻本段 10-10 更正）：alpha13 经官方源二次直查确为真实发布

> 来源：[[AppIntent 每日情报 2026-10-13]]。本段二次复核本笔记 10-10 更正段，结论已反转。

- **10-13 官方源直查结论**：`developer.android.com/jetpack/androidx/releases/appfunctions` 发布页、alpha-channel 与 all-channel 发布列表**均明确列出 `1.0.0-alpha13`（2026-10-07 发布）**，API 变更逐字为：① Added `@AppFunctionAccessLevel` annotation, supporting access restriction setting (Id47e1)；② Renamed `AppFunction` annotation to `AppFunctionDeclaration` (I4b15d)；③ Renamed `ObserveAppFunctionsEvent` to `AppFunctionsChangeEvent` (Iec918)；④ Surface `AppFunctionMetadata` in `AppFunctionService` (If1117)；⑤ Bug fix：`AppFunctionData` 支持全部内建 proxy 类型（LocalDate/LocalTime/Instant/ZoneId）。
- **对 10-10 更正段的影响**：该段「最新仍为 alpha12、无 alpha13、`@AppFunctionAccessLevel` 不可见、`@AppFunction` 未重命名」的结论**系当时搜索索引快照滞后导致的误判，已被 10-13 复核推翻**。本笔记 10-09 增补段所述内容（函数侧 `@AppFunctionAccessLevel` 三向约束、`@AppFunction`→`@AppFunctionDeclaration` 重命名等）**真实有效，维持原结论**。
- **当前可确认最新版本**：`1.0.0-alpha13`（2026-10-07），无 alpha14（10-13 时点）。AppFunctions 权限模型三向约束（caller `EXECUTE_APP_FUNCTIONS` 权限 + `scope` 可见性 + 函数侧 `@AppFunctionAccessLevel`）维持成立；`@AppFunctionAccessLevel` 具体级别语义仍待 `developer.android.com/ai/appfunctions` 官方文档逐字段确认（不猜测 public/protected/system 等级别）。
- **对 dedup / 后续跑的影响**：未来每日跑应以「官方最新 = alpha13（10-07）」为基线检索 alpha14+；10-10 跑遗留的「以 alpha12 为基线」指示已失效，请勿沿用。

⚠️ 诚实标注：本复核基于 2026-10-13 对官方 Jetpack Release Notes 发布页 + alpha-channel + all-channel 三处官方列表的 WebSearch 直查交叉确认；`@AppFunctionAccessLevel` 级别语义官方 Release Notes 仍未展开，待官方文档逐字段确认。

## 2026-10-26 增补：AppFunctions 跳到首个 Beta `1.0.0-beta01`（2026-10-21，首个 beta 渠道 + `description`→`instructions` 对齐 MCP 命名，推翻「等待 alpha14」假设，来源 [[AppIntent 每日情报 2026-10-26]]）

> 接续 10-13「官方最新 = alpha13（10-07）、无 alpha14（10-13 时点）」的 dedup 基线。本期由官方 Jetpack Release Notes 确认 **AppFunctions 未发 alpha14、而是跳到 `1.0.0-beta01`（2026-10-21）**——这是自 2026-05 实验性预览以来**首个 Beta 渠道版本**，意味着 API 面从「剧烈变动期（破坏性重命名频发）」迈入「趋于稳定、接近 1.0」的成熟度阶梯。⚠️ 层级：官方 Jetpack Release Notes 逐字确认，非二手。

**① 版本号进位 = 成熟度里程碑（高价值）**
- 自 alpha10（07-01）→ alpha11（08-26）→ alpha12（09-23）→ alpha13（10-07）一路破坏性重命名（`@AppFunction`→`@AppFunctionDeclaration`、`AppFunctionContext` 移除等）后，**beta01 标志 AppFunctions 进入「beta 稳定化」通道**——开发者可预期 API 收敛，不再每版本破坏性迁移。这与 09-17 记的「Android 17 把 AppFunctions 抬进主版本、但 API 仍 alpha」形成对照：**框架进主版本 ≠ API 稳定，但 beta01 是 API 稳定化的真正信号**。
- 对 dedup/后续跑的影响：未来每日跑应以「官方最新 = beta01（10-21）」为基线检索 beta02+，此前 10-13 的「alpha13 为基线」指示仍有效但版本号已进位，请勿沿用「等待 alpha14」的旧假设（10-18 跑曾把 alpha14 列为待办，已被本运行推翻）。

**② `AppFunctionAppMetadata.description` → `instructions`（对齐 MCP 命名惯例，跨平台信号）**
- beta01 把 `AppFunctionAppMetadata.description` 及其 XML 属性 `description` **重命名为 `instructions`**，官方明确「to align with MCP naming conventions」。
- **含义**：AppFunctions 是设备端 MCP 的 OS 原生特例（本笔记开篇定义），现在连**元数据字段名都向标准 MCP 收敛**——`description`→`instructions` 正是 Anthropic/标准 MCP server 工具定义里「`instructions` 描述工具如何被使用」的惯用字段名。这是四平台里**首个明确把设备侧意图框架的元数据语义对齐到通用 MCP 命名**的案例，强化「AppFunctions = 设备端 MCP」的身份（呼应 [[MCP 与设备侧 MCP]]）。
- 对 OS PM：做意图 Registry 元数据规范时，可参考这一「向通用 MCP 命名对齐」的收敛方向，减少跨体系迁移的认知成本。

**③ 其余 beta01 API 变更（Release Notes 逐字）**
- `AppFunctionName` 从 `androidx.appfunctions.metadata` 包**迁移到 `androidx.appfunctions`** 包（Iec624）——包结构收敛，与「进入 beta、清理 experimental 命名空间」一致。
- **移除 `isDescribedByKDoc` 的默认值**（AppFunctionDeclaration / AppFunctionSerializable / AppFunctionSignature，Idcfd2）：此前 KDoc 驱动工具描述是默认行为，现**必须显式设置**——对「KDoc 即工具描述」的工程约定（见本笔记「可复用启发」）是收紧：开发者须主动声明「此函数描述来自 KDoc」，而非默认。可能意味着 Google 在 beta 期把「描述来源」从隐式升为显式决策点（与来源轴待办有微妙呼应，但仍是描述来源、非数据 provenance）。
- `AppFunctionServiceEntryPoint` 支持进入 `AppFunctionTestRule`（I12e01）——测试代理/集成测试能力补强（呼应 08-02 官方 Agent Skill 四步生命周期的 Testing 步）。
- `AppFunctionResourceContainer` / `AppFunctionTextResource` 标 `@ExperimentalAppFunctionsApi`（If9469）——资源型描述仍 experimental，未进稳定面。
- `@AppFunctionStringValueConstraint` 的 regex 替换为 `patternMatchers`（基于 `android.os.PatternMatcher`，I7c7cc）——参数级约束从「正则字符串」升级为「OS 原生 PatternMatcher」，约束表达力与安全性增强（延续 09-25 alpha12 的 Uri 约束补强方向）。
- Bug Fixes：`java.time` 参数类型在启用 Java 库脱糖时反序列化失败、生成文件名在部分 OS 含非法符号、SDK37+ 上 URI 权限被双重授予——均为 beta 期工程稳定性修复。

→ **对 OS PM 的含义**：AppFunctions 在 2026-10-21 跨过「首个 beta」门槛，**成熟度 + 跨平台命名对齐**双信号同时到位；但 beta01 仍属 pre-stable，**GA 日期仍待补**（延续本笔记「AppFunctions 何时 GA 待补」开放问题）。`@AppFunctionAccessLevel` 级别语义（10-13 段）在 beta01 Release Notes 仍未展开，仍为待补项。

⚠️ 诚实标注：beta01 发布于 2026-10-21，由本运行直查官方 Jetpack Release Notes 发布页（developer.android.com/jetpack/androidx/releases/appfunctions）逐字确认；`description`→`instructions` 的 MCP 命名对齐为官方 Release Notes 原文；`@AppFunctionAccessLevel` 级别语义在 beta01 仍未展开，待 `developer.android.com/ai/appfunctions` 官方文档逐字段确认。

## 2026-10-29 增补：Connected Apps Platform（预览，10-28 Dev Summit）+ ML Kit Agentic API（alpha，Gemini Nano 4，来源 [[AppIntent 每日情报 2026-10-29]]）

> 接续 10-26「AppFunctions 进首个 Beta `1.0.0-beta01`（10-21）」。本期由 Android Dev Summit（2026-10-28 召开）官方公告捕获 **AppFunctions 生态的两层扩展**：① 一个把 AppFunctions 挂到系统级 AI 入口的 **discovery/registration surface**（Connected Apps Platform）；② 一个 OS 提供的**端侧 agentic 运行时**（ML Kit Agentic API，Gemini Nano 4）。两者均非 AppFunctions 自身版本进位（仍 beta01），而是「工具层 + 模型层」的能力补强。

**① Connected Apps Platform（预览，10-28 Dev Summit，★7/10，跨应用 Intent 工作流发现面）**
- **机制**：开发者经 **cloud-hosted MCP server 或 Android MCP（用 AppFunctions APIs）** 接入，在 **Google Connected Console** 注册并选择「出现在 Search / Gemini app / 两者」；一次接入、跨 Google 全家可用（"enable once, run Google-wide"）。官方称已上线 **50+ Connected Apps**（Adobe、Peloton、Experian、Calm 等），Search 侧先在 US 的 AI Mode（英文）开放。
- **对 AppFunctions 的含义**：这是四平台里**首个把设备侧意图框架（AppFunctions/Android MCP）直接接入「系统级搜索入口 Search」的官方能力**——把「跨应用 Intent 工作流」从「Gemini app 内编排」扩到「Search 结果页即触发 agentic action」。AppFunctions 的 Registry 发现面从「Gemini 助手内」扩到「系统级搜索」，是 [[Intent Router 语义路由]] 与 [[四平台意图 Registry 来源轴与权限模型对比 2026]] 的 discovery-surface 维度补强。
- **执行仍受既有 OS 权限模型兜底**：调用方经 `EXECUTE_APP_FUNCTIONS` 闸门 + `scope` 可见性 + 函数侧 `@AppFunctionAccessLevel` 三向约束（见本笔记 09-25/10-09 增补）；用户授权经 **OAuth 2.1** 让 Gemini 代表用户行动（Google 文档明示）。但「Search 即触发」比「助手内显式指令」更易产生非预期调用，需观察确认/隔离是否随入口扩张收紧（延续本笔记「确认下放 App」路线风险）。
- ⚠️ 层级纪律：仍为 **preview + 分阶段开放**（US 开发者 waitlist），非 GA；具体 API 名、是否独立 service、是否受 `EXECUTE_APP_FUNCTIONS` 同一闸门约束**待 developer.android.com/ai/appfunctions 官方文档确认**。

**② ML Kit Agentic API（alpha，Gemini Nano 4，★6/10，OS 提供的端侧 Planner 原语）**
- **机制**：ML Kit 新增基于 **Gemini Nano 4** 的 Agentic API（alpha），支持**函数调用（function calling）+ 对话历史管理（conversation history management）+ 执行流控（execution flow control）**，供开发者探索**设备端运行的智能体体验**。
- **对 AppFunctions 的含义**：AppFunctions 负责**暴露 App 能力为设备端 MCP 工具**，ML Kit Agentic API 补上**设备端模型与运行时的 agentic 编排**一环，二者共同构成 Android 端侧意图执行总线的「工具层 + 模型层」。这与本库 [[Function Calling 端侧工具调用]] 聚焦的「端侧 Planner / 设备侧 MCP」直接对齐——是把「端侧路线图」从「工具声明」补到「端侧推理+编排」的关键一块。
- ⚠️ 层级纪律：alpha 阶段、Gemini Nano 4 后端；具体 SDK 形态、调用 AppFunctions 的方式、权限边界**待官方文档确认**。

→ 对 OS PM 的含义：Android 在 10-21 进 beta01（API 稳定化）后，10-28 Dev Summit 又补「discovery 面（Connected Apps Platform）+ 端侧模型运行时（ML Kit Agentic API）」——AppFunctions 从一个「工具声明 API」正在长成「端侧意图执行总线的完整栈」。但三者成熟度不同（beta01 / alpha / preview），均**非 GA**，落地广度仍受准入约束（延续本笔记「有限数量应用与系统智能体」开放问题）。

⚠️ 诚实标注：Connected Apps Platform 与 ML Kit Agentic API 来自 Android Dev Summit（2026-10-28）官方公告，经 The Prompt Insider（"Google announced it on October 28, 2026"）/ 腾讯新闻（2026-10-29）/ Pivot News / Zendoric 多方一致复述；均处 preview/alpha，非 GA，具体 API 名与权限边界待 developer.android.com/ai/appfunctions 官方文档逐字段确认。Dev Summit 公告（10-28）处本窗口起点边缘、10-28 运行未记录，本运行作诚实边界补捕。

## 2026-11-03 复核增补：AppFunctions beta 权限边界澄清（Forkast 11-01，★5 复述、无新字段）

> 接续本笔记 10-29 增补（Connected Apps 双路径 + OAuth 2.1 + `EXECUTE_APP_FUNCTIONS`/`scope`/`@AppFunctionAccessLevel` 三向约束）。Forkast（11-01）报道 Android 10-28 beta 公告将 **AppFunctions API 状态与正式生产发布分离**——beta 态不等于开放/无限制 agent 访问，生产发布为独立受闸步骤。此为本笔记既有「权限/Registry 约束」论述的**媒体复述**，未引入新 API/字段；无新净新增。AppFunctions 版本仍 `1.0.0-beta01`（10-21）最新。来源 [[AppIntent 每日情报 2026-11-03]]。

## 2026-10-29 补遗：Connected Apps Platform 执行安全/确认机制 + 架构双路径（21:12 复核，来源 [[AppIntent 每日情报 2026-10-29]] + 多源 freshness 复核）

> 接续本笔记 10-29 增补（Connected Apps Platform 预览 + ML Kit Agentic API）。本次以 freshness 复核（多源：TechCityAuthority / aiagentslibrary / beyondthe.news / xnews / dev.to / MACCUS，均 10-29 发布）补 **此前遗漏的「执行安全 / Confirmation UI」与「架构双路径」硬细节**——这些直接命中本任务聚焦轴「执行安全（Confirmation UI）/ 语义路由」，之前仅笼统记为「确认下放 App」风险，未抓到平台已提供的确认机制原语与调用模型。

**A. 平台级确认机制（Execution Safety / Confirmation UI，★7 维度补强）**
- **工具读写分类**：开发者须把每个工具声明为 **read-only（只读）或 action-that-changes-data（改变数据的动作）**——这是 Connected Apps 的**工具级数据安全风险标注**，直接服务「哪些动作需要确认」。
- **控制台确认标记**：开发者可在 **Google Connected Console** 中**显式标记「需要确认的操作（operations that require confirmation）」**——这是平台提供的**确认 UI 钩子**，非纯靠 App 自加弹窗。→ 修正本笔记 10-05/10-09「确认完全下放 App」的单向叙述：现在 Google 在**平台层提供了确认标记能力**，但**仍由开发者/工具声明是否需确认**（非系统按风险自动拦截，对照 Apple 系统级 Confirmation UI 仍分歧）。见 [[Confirmation UI 安全机制]]。
- **可选绑定交互 UI 资源**：工具可**可选地绑定到交互式 UI 资源**（与 A2UI 渲染原生 UI 同方向）——确认/结果呈现可走原生 UI 而非纯文本，呼应 [[A2UI 生成式UI协议(Google)与鸿蒙落地 2026]]。

**B. 调用模型（语义路由 / session 维度）**
- **@ 调用 + 名称调用**：用户可用 **"@appname"** 或**在请求中提及 App 名**显式触发；一旦调用，**该 app 在本 session 的相关请求中保持上下文（remains in context）**——这是**会话级意图保持**机制，影响 Planner 的路由召回（无需每轮重述目标 App）。
- **工具 schema 驱动选择**：Google 产品读取 App 发布的**工具 schemas** 决定哪个工具适配请求——schema 质量直接决定路由准确率（延续本笔记「KDoc 即工具描述」的「描述质量=召回上限」论点，见 08-02/10-09 可复用启发）。

**C. 架构双路径（修正/补强「AppFunctions = Android MCP 唯一路径」的旧表述）**
- **Remote MCP server = Google 推荐默认路径**：官方称其为「foundational, cross-platform capabilities 的推荐默认」，因同一 server 可跨 **Android / iOS / Web** 扩展；须部署到**公开 HTTPS 端点**，可复用既有 Web API 或远程 MCP server。
- **AppFunctions = client-side 本地路径**：官方定位为「client-side integration path」，**尤其适合希望工具执行发生在 Android 设备本地**的场景——是 remote MCP 的**互补项而非竞争项**。
- → 对 OS PM 的含义：Google 的「系统级意图框架」实际是**混合模型**——跨平台能力走云端 remote MCP（推荐默认），设备端能力走 AppFunctions（本地子集）。这**修正本笔记此前将 AppFunctions 表述为 Android 唯一 MCP 路径的简化**；也说明 Connected Apps Platform 把「设备端意图框架（AppFunctions）」与「云端 MCP 工具」统一到一个开发者入口，但二者执行位置/权限模型不同（AppFunctions 受 `EXECUTE_APP_FUNCTIONS` + `scope` + `@AppFunctionAccessLevel` 三向约束，remote MCP 走 OAuth 2.1 + 工具 schema 注解）。详见 [[MCP 与设备侧 MCP]]、[[四平台意图 Registry 来源轴与权限模型对比 2026]]。

**D. 授权与治理底线**
- **OAuth 2.1**：作为「安全授权 Gemini app 与你的服务交互」的机制，用户**一次性链接账号**后 Gemini/Search 可触达其账户数据与执行授权动作。
- **平台政策（dated 2026-09-28）**：要求**数据最小化、处理透明、安全数据处理**，禁止在 Connected App 工具内投放**第三方广告/促销内容**、禁止欺骗性工具描述、隐藏功能、无授权 API 包装。→ 这是**平台层治理约束**，与 10-02 晚 Android 17 企业策略（`APP_FUNCTIONS_DISABLED`）的「agent 执行边界可经治理面管控」形成互补（开发者政策 + 企业 MDM 双保险）。
- **验证方式**：MCP Inspector 校验、HTTPS 托管、Gemini Developer Mode 实测执行后再提交审核。

⚠️ 诚实标注：上述细节来自 10-29 freshness 复核的多源媒体复述（均引用 Google 开发者文档 / Dev Summit 公告），具体字段名（如「require confirmation」标记在 Console 的精确 API/UI 形态、`read-only`/`action` 的声明注解名）**待 developer.android.com/ai/appfunctions 或 Connected Apps Platform 开发者文档逐字段确认**；WebFetch 直连官方文档在本会话仍失败（沙箱网络限制），故以多源交叉确认 + 诚实标注处理，不臆造字段名。
