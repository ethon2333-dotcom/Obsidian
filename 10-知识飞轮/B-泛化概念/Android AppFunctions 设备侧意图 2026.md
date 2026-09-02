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
