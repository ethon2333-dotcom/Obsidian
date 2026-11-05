---
type: concept
status: draft
date: 2026-08-17
derived_from: "[[AppIntent 每日情报 2026-08-17]]"
source:
  - "https://developer.apple.com/videos/play/wwdc2026/347/"
  - "https://developer.apple.com/wwdc26/guides/ios"
  - "https://developer.android.google.cn/blog/posts/android-17-is-here"
  - "https://developer.huawei.com/consumer/cn/blog/topic/03220919589498064"
  - "https://developer.microsoft.com/en-nz/windows/agentic/"
importance_score: "★★★★☆（8/10）"
intent_category: "四平台 Registry / 权限模型 / 意图元数据来源轴对比"
tags: [概念, Registry对比, 权限模型, 来源轴, 执行安全, 跨平台, 2026-08-17]
---

# 四平台意图 Registry 来源轴与权限模型对比 2026

## 一句话定义

横向对比 Apple / Android / HarmonyOS / Windows 四大 OS 的**意图 Registry（能力注册表）结构与权限模型**，并单独回答一个追了 8 轮的最高优先问题：**意图元数据是否记录「数据从哪来、可不可信」（来源/溯源轴）**——结论：**四平台 OS intent 层均不记录，属架构性空白（confirmed，非待查）**。

## 为什么重要

- 这是本库追踪 8 天（08-09 → 08-17）的最高优先待办的**收口结论**，不是新假设。它直接决定 OS PM 在设计意图 Registry 时「能抄什么、必须原创什么」。
- 把「意图元数据分级」拆成**两条正交轴**后，副作用轴 Apple 已解、来源轴四平台全空——混淆两者会误判进度（见 [[意图风险元数据与鉴权策略棘轮 2026]]）。
- 对 ADI（[[Agent Data Injection 数据注入攻击]]）防护有直接影响：来源轴空白意味着**当前没有任何 OS 能因「这条意图的数据来自不可信网页/日历」自动降级或加闸**。

## 适用边界

- 仅对比** OS 级 intent / 能力总线层**（App Intents / AppFunctions / Intents Kit+ArkAF / ODR+Agent connectors），不含上层应用自实现的治理层。
- 各平台具体 entitlement / 字段名以官方文档为准；部分以 WWDC26 / Android 17 / HDC2026 公开材料交叉确认。
- **2026-08-18 更新**：Windows 侧 **Entra Agent ID 已由「第三方解读待确认」升级为「官方已 GA」**——微软 **Agent 365（智能体控制平面）2026-05-01 GA**，Entra Agent ID 为其身份基座（唯一身份 + 权限 + Conditional Access），属 **M365/Entra 治理与身份层**，与 ODR/Agent Workspace（OS 执行总线）**正交**。详见 [[Agent 365 与 Entra Agent ID 智能体控制平面与身份基座 2026]]。本表「身份/审计」行的 Windows Agent ID 项现获官方背书。

## 证据与例子

### ① 来源/溯源轴（provenance）：四平台全空白（confirmed）

| 平台 | 意图/实体元数据里有什么 | 有没有「来源 / 可信度」字段 | 结论 |
|---|---|---|---|
| **Apple** | `@AppIntent(schema:)` 自动继承 schema 的**副作用轴**风险元数据 + 默认 `authenticationPolicy`；`.appEntityIdentifier` 是**屏幕感知视图链接**（08-15 证伪为视图链接，非来源） | ❌ 无 | 用「零信任输入处理」回答「数据可不可信」，但 Registry 不记 provenance |
| **Android** | `AppFunctionStaticMetadata`：`functionIdentifier` + schema + KDoc（编译期 `app_function_v2.xml` → AppSearch） | ❌ 无 | `app_metadata` 仅描述功能，无来源/信任 |
| **HarmonyOS** | `insight_intent.json`（`IntentActionInfo` / `IntentEntityInfo`）+ `InsightIntentEntryExecutor` | ❌ 无 | 意图框架注册不记 provenance |
| **Windows** | ODR 注册 MCP Agent connectors；Agent ID（唯一身份 + 审计） | ❌ 无 | connector/tool 元数据无 provenance；隔离靠 Agent Workspace 低权限账号 + ACL |

→ **含义**：四平台对 ADI 的防护都依赖「应用侧自行脱敏/标注」（见 [[数据溯源分级与单调棘轮]] 的治理层六类来源/四级密级模型），**OS intent 总线本身不提供来源分级**。印证 08-04 结论「治理层有成熟模型、OS 层全空白」。

→ **最低成本补丁（沿用 08-16）**：意图 Registry 加 `readOrWrite` 声明位，让 OS 知道某 intent 读的是不可信上下文还是可信数据——但仍非完整 provenance。

### ② 权限 / Registry 模型对比

| 维度 | Apple（App Intents） | Android（AppFunctions） | HarmonyOS（Intents Kit + ArkAF） | Windows（ODR + Agent connectors） |
|---|---|---|---|---|
| 声明方式 | `@AppIntent(schema:)` 编译期生成 schema | `@AppFunction` 编译期 `app_function_v2.xml` | `insight_intent.json` + `InsightIntentEntryExecutor` | MCP server（Agent connector） |
| 发现/注册 | Spotlight 语义索引 + System Orchestrator | OS AppSearch registry | 意图框架注册；元服务 `installationFree` | ODR（On-Device Registry） |
| 调用方权限 | 系统级（Siri/Apple Intelligence） | 调用方须持 `EXECUTE_APP_FUNCTIONS`；每函数可配用户显式授权 | 华为账号统一授权；执行模式（前台/后台 API 20+） | 用户批准查询/动作 + 作用域（scoped authorization） |
| 鉴权/确认 | schema 继承默认 `authenticationPolicy`（**棘轮：只能更严**）+ 锁屏鉴权 + 系统按副作用轴确定性确认 | **下放 App 自实现确认**（08-03） | 上下文充足免二次确认（信任式） | Agent Workspace 隔离 + 用户批准 |
| 身份/审计 | — | — | — | **Agent ID**（唯一、审计轨迹，与用户活动可区分） |
| 隔离 | 锁屏鉴权 + 后台 Neural Engine entitlement 治理 | 动态门控 `setAppFunctionEnabled` / `isAppFunctionEnabled`（08-03） | 端/云 A2A 双模（隐私数据不出端） | **Agent Workspace**：独立会话 + 低权限账号 + ACL |
| 运行时动态可见性 API | ❌ 待补 | ✅ `setAppFunctionEnabled` | ❌ 待补（与 Apple 同） | ODR 注册/注销（公开开发者预览「coming weeks」） |

### ③ 副作用轴（side-effect）状态

- **Apple ✅ 已解**：schema 内置风险元数据（destructive / exfiltration / shared-content），系统按「静态元数据 + 动态状态」确定性触发确认（[[意图风险元数据与鉴权策略棘轮 2026]]）。
- **Android**：破坏性动作确认**下放 App 自实现**（08-03 路线分歧）。
- **HarmonyOS**：上下文充足时**免二次确认**（信任式，非确定性规则）。
- **Windows**：靠 Agent Workspace 隔离 + 用户批准查询/动作。

### ④ 治理层控制平面（Agent 365 / Entra Agent ID，2026-08-18 新增）

> 来源：[[Agent 365 与 Entra Agent ID 智能体控制平面与身份基座 2026]]（[[AppIntent 每日情报 2026-08-18]]）。本条补「OS 执行总线之外，治理层已有量产控制平面」这一对照维度，避免把 OS 层空白误读为「行业也无参照」。

- **统一注册表 + 身份基座 + 三运行模式**：Agent 365 把 agent 入口收敛为单一控制平面（状态 Available/Blocked/Pending）；Entra Agent ID 给每 agent 唯一身份 + 权限 + Conditional Access；三模式 = 代用户（delegated）/ 自主后台（autonomous）/ 协同（collaborative，预览）。
- **分层关系**：Agent 365（治理/身份层）↔ ODR（OS 执行层）经 MCP connector 衔接，**职责不混**——这给「OS 原生意图框架要不要自带治理」的答案是：OS 层管执行隔离与权限，治理/身份可下沉平台级控制平面。
- **对本文对比表的修正**：原「身份/审计」行 Windows = Agent ID 已由「第三方解读待确认」升为「官方 GA 已确认」；且补一条维度——**运行模式分类**（四平台 OS 层目前极少显式区分 agent 是代用户 / 自主 / 协同）。

## 可复用启发

1. **副作用轴可照抄 Apple，来源轴必须原创**：前者是「已被证明可做、且 Apple 已做完」的工程；后者是真空白，OS PM 设计 Registry 时不应再把两者混为一谈。
2. **「后果性标记应由 Schema 承载而非 App 声明」**在四平台里只有 Apple 做到（schema 风险元数据）；其余平台把确认责任转嫁给开发者/应用，一致性与可审计性更弱。
3. **隔离是 Windows 的差异化武器**：Agent Workspace「独立会话 + 低权限账号 + ACL + Agent ID 审计」是四平台里最完整的执行隔离范式；Apple 用「锁屏鉴权 + entitlement 治理」、HarmonyOS 用「端侧 A2A 不出端」、Android 最薄（仅权限 + App 自确认）。
4. **来源轴空白 = ADI 的结构性缺口**：凡涉及「不可信数据喂给端侧 Planner」的场景，当前只能靠应用层/治理层补（[[数据溯源分级与单调棘轮]]），OS 总线层暂无对应物。

## 关联

- 索引：[[意图框架·跨体系索引 MOC]]
- 平台原子笔记：[[Apple AppIntents Schema Protocol 2026]] ｜ [[Android AppFunctions 设备侧意图 2026]] ｜ [[HarmonyOS Intents Kit 与 ArkAF 2026]] ｜ [[Windows Copilot Actions 与 Agent Workspace 2026]] ｜ [[Agentic OS 意图调度内核]]
- 安全同构：[[意图风险元数据与鉴权策略棘轮 2026]]（副作用轴）｜ [[Confirmation UI 安全机制]]（确认/触发器）｜ [[XPIA 跨提示注入]] ｜ [[Agent Data Injection 数据注入攻击]]（来源轴空白的攻击面）｜ [[数据溯源分级与单调棘轮]]（治理层来源分级，OS 层缺失的对照）｜ [[隔离执行]]（Windows Agent Workspace）
- 枢纽：[[意图模式规范]] · [[语义路由]] · [[端侧工具调用]] · [[确认机制]] · [[元服务]] · [[A2A 端侧智能体协议]] · [[XPIA 跨提示注入]]

## 2026-08-31 增补：Per-Intent Privacy Manifest 待办收口（来源 [[AppIntent 每日情报 2026-08-31]]）

> 接续本笔记「来源轴四平台全空白（confirmed）」结论，与 08-02 起悬挂的「Per-Intent Privacy Manifest 是否为独立 App Intents API」最高优先待办。本期用**官方文档直查 + 多源检索**做最终判定：**该 API 不存在**，第三方博客说法是推测/混淆。

- **判定方法**：① WebFetch 官方 App Intents 框架文档（`developer.apple.com/documentation/appintents`）逐节核对——全文**无任何 per-intent privacy manifest / 按意图声明云-端路由的 API**；② WebFetch 官方 Privacy manifest files 文档——只有 iOS 17 起的通用 `PrivacyInfo.xcprivacy`（声明数据收集类型 / required-reason API / 跟踪域名），**与 App Intents 意图路由无关**；③ 多源检索 "per-intent privacy manifest App Intents cloud on-device routing" 仅命中 iOS 17 通用隐私清单 + 一篇第三方博客（byteiota 的 SiriKit 弃用文称「Apple introduced per-intent privacy manifest declarations at WWDC 2026」），**无任何 Apple 官方文档支撑**。
- **结论**：「Per-Intent Privacy Manifest / 按意图粒度声明云或端路由」**不是真实存在的 App Intents API**。第三方博客疑似把 iOS 17 通用隐私清单机制或对未来能力的推测，误读为「App Intents 新增的 per-intent 路由声明」。本笔记 08-02 节原标注「待官方文档确认」，现升级为**已证伪（confirmed non-existent）**。
- **对来源轴结论的影响**：**不改变**「来源/溯源轴四平台全空白」结论——反而进一步夯实：Apple 意图层既无 provenance 字段（08-17 证伪 `.appEntityIdentifier` 为视图链接），也无 per-intent 路由声明。来源轴空白从「待查」→「架构性空白」→ 现再经本轮排除一个常见误传，**证据更干净**。
- ⚠️ 诚实标注：判定基于 2026-08-31 当日官方文档快照；若 Apple 在 iOS 27 正式版（约 2026-09-14）新增此类 API，需重新评估。当前以「不存在」记录，避免后续轮次被二手说法反复带偏。

## 2026-09-01 增补：DMA 跨助手可发现性维度 + Android 门控 API 迁移（来源 [[AppIntent 每日情报 2026-09-01]]）

> 接续本笔记「来源轴四平台全空白」与 08-31「Per-Intent Privacy Manifest 证伪」结论。本期补两个增量：**① 监管强制的跨助手可发现性维度**；**② Android alpha11 把动态门控 API 从 `setAppFunctionEnabled` 迁到 `AppFunctionState`**。

**① 跨助手可发现性（新增对比维度，受监管强制）**
- 欧盟 DMA 要求 Google 在 2027-08 前向竞品助手开放 11 项 Android AI 能力；AppFunctions Registry 使函数可被**任一认证助手**发现，`EXECUTE_APP_FUNCTIONS` 在 EU 下沉为「认证闸门」。
- 含义：四平台里**仅 Android 侧的 Registry 可发现性被外力（监管）强制横向开放**；Apple/Windows 走平台治理（App Review / Agent ID），HarmonyOS 走小艺单一入口。这是本对比表此前缺的「可发现性是否被强制开放」维度。详见 [[AppFunctions 跨助手可发现性与 DMA 强制开放 2026]]。

**② Android 动态门控 API 迁移（更新「运行时动态可见性 API」行）**
- 原表记 Android 运行时动态可见性 API = `setAppFunctionEnabled` / `isAppFunctionEnabled`（08-03）。**`alpha11`（2026-08-26）起改为 state-based**：`AppFunctionState` + `AppFunctionManager#getAppFunctionStates` 取代 `AppFunctionMetadata#isEnabled`，元数据显示态与状态分离。
- **修正**：Android 仍是四平台里**唯一有公开动态可见性 API** 的平台，但 API 形态已迁移；原「setAppFunctionEnabled」应标注「alpha11 起改为 `getAppFunctionStates` 状态查询」。

→ 对来源轴结论无影响：DMA 强制的是「可发现性」而非「provenance」——跨助手开放仍不解决「数据从哪来、可不可信」的来源轴空白（见 [[Agent Data Injection 数据注入攻击]]）；最低成本补丁仍是意图 Registry 加 `readOrWrite` 声明位。

## 2026-10-03 增补：Apple 桌面文件权限层 agent-aware（来源 [[AppIntent 每日情报 2026-10-03]]，详见 [[Apple 桌面 Agent 权限治理 macOS Full Disk Access 2026]]）

> 接续本笔记 09-25「Android alpha12 `scope` + `serialize`」与「Apple 用锁屏鉴权 + entitlement 治理」（行 81）。本期 Apple 在**桌面 OS 权限层**（非意图 Registry 层）发出新治理信号，补齐本对比表「权限模型」维度的 Apple 桌面侧拼图。

- **新增对比维度：Apple 桌面文件权限（FDA）显式动作门控**。Apple 2026-10-02 宣布把 macOS Full Disk Access 改为「仅以非常明确的用户动作授予」，并首次把 AI agent 自主能力增长列为理由。这是 Apple 桌面侧「agent 可达性 = OS 权限边界」的显式表态，**与此前本笔记记的 Apple 移动侧「锁屏鉴权 + entitlement 治理」构成 Apple 全平台权限治理的两层**。
- **四平台「agent 执行边界 = OS 权限/隔离/确认边界」收敛对账**（更新「权限/Registry 模型」对比行的 Apple 列）：
  - **Apple（桌面）**：FDA 显式用户动作门控（forward-looking，未给版本/形态）；移动侧锁屏鉴权 + entitlement。
  - **Windows**：Agent Workspace 低权账号 + ACL + Agent ID 审计；ODR 三档 consent（Ask every time / Allow always / Never allow）。
  - **Android**：`EXECUTE_APP_FUNCTIONS` 仅限可信 caller；`setAppFunctionsPolicy` + `APP_FUNCTIONS_DISABLED` 经 MDM 全局禁用。
  - **Microsoft（跨窗口权威，2026-10-01 Digital Defense Report）**：agent 身份 + 权限 + prompt injection + revoke 四件套。
- **门控颗粒度差异（本笔记新观察）**：Apple=显式动作 / Windows=低权账号+consent 时长 / Android=caller 白名单+MDM 开关 / Microsoft=身份+revoke——方向同构，落点不同。
- **不推翻来源轴结论**：FDA 是桌面文件权限层，与「意图 Registry 来源/provenance 轴四平台全空白（confirmed）」**正交**；本笔记最高优先待办「意图元数据记录数据来源/可信度」结论延续。

#标签/跨平台 #标签/Registry #标签/权限模型 #标签/来源轴 #标签/执行安全 #标签/IntentFramework

## 2026-09-15 增补：Per-Intent Privacy Manifest 待办重开（08-31 证伪结论 GA 后重评估，来源 [[AppIntent 每日情报 2026-09-15]]）

> 接续本笔记 08-31「Per-Intent Privacy Manifest 证伪 + 来源轴待办收口」。iOS 27 正式版（2026-09-14）已落地，按 08-31 自身注明的「若 iOS 27 正式版新增此类 API 需重新评估」，本期重开该待办。

- **重评估结论**：08-31 基于当日官方文档直查判定该 API「confirmed non-existent」；现 GA 后，**WWDC 2026 多源报道（Lushbinary / ByteIota / TechTimes / AlgeriaTech）一致称 Apple 引入 per-intent privacy manifest declarations，让开发者按意图声明「Siri 交互可否上云 / 必须留端」**。但**官方 post-GA「What's New in iOS 27」页（developer.apple.com/ios/whats-new）未逐字列出该 API**（仅列 Entity/Intent schemas、View Annotations、App Intents Testing、Foundation Models 多模型等）。
- **判定**：由「confirmed non-existent」升为 **「GA 后多源一致报道、但官方页未确认 → 待官方文档逐字复核」**——**不推翻**本笔记「意图 Registry 来源/可信度（provenance）轴四平台全空白」结论，因为即便确认，它也是**数据路由目的地（cloud vs on-device）声明**，与本笔记证明的「来源/可信度 provenance」**不同轴**。
- **新增评估维度（若确认）**：Apple 将获得一条**「路由轴」声明**（数据可否离开设备），与 provenance 轴正交——本对比表可补「路由轴」维度，区别于现有「来源/可信度轴」。但**在官方文档确认前不写入对比表正文**，避免再次被二手说法带偏（08-31 的教训）。
- ⚠️ 诚实标注：判定基于 2026-09-15 当日检索；Apple 若在 iOS 27.x 后续或官方隐私清单文档补充该 API，需再次评估。当前以「GA 后待官方复核」记录。

## 2026-09-16 增补：Per-Intent Privacy Manifest 官方页重核（来源 [[AppIntent 每日情报 2026-09-16]]）

> 接续本笔记 09-15「Per-Intent Privacy Manifest 待办重开（GA 后待官方复核）」。本期用**官方「What's New in iOS 27」页（developer.apple.com/ios/whats-new）**再次直查，做闭环复核。

- **复核结论**：官方 post-GA 页 App Intents 段落仅列 **Entity schemas / Intent schemas / View Annotations API / App Intents Testing / Foundation Models 多模型路由**——**无任何 per-intent privacy manifest / 按意图声明云-端路由的 API**。
- **判定**：维持 09-15「GA 后多源一致报道（Lushbinary/ByteIota/TechTimes/AlgeriaTech）、但官方页未确认 → 待官方文档逐字复核」状态；**不关闭**该待办（因多源报道仍未证伪），但**维持**本笔记「意图 Registry 来源/provenance 轴四平台全空白」结论——即便确认亦属「路由目的地 cloud vs on-device」轴，与 provenance 正交（见 09-15 增补「路由轴 vs 来源轴」区分）。
- **对对比表的影响**：在 Apple 官方文档逐字确认前，**不写入对比表正文**（延续 08-31「不被二手说法带偏」纪律）。当前「来源轴」行 Apple = ❌ 无、结论 = 架构性空白（confirmed）不变。

⚠️ 诚实标注：复核基于 2026-09-16 当日官方页快照；Apple 若在 iOS 27.x 后续或官方隐私清单文档补充该 API，需再次评估。

## 2026-09-25 增补：Android alpha12 加入 `scope` 维度 + `serialize` 元数据信号（来源 [[AppIntent 每日情报 2026-09-25]]）

> 接续本笔记 09-01「Android 动态门控 API 迁移（alpha11）」与 09-15/09-16「Per-Intent Privacy Manifest 维持待复核」。本期由官方 Jetpack Release Notes 确认 **AppFunctions `1.0.0-alpha12`（2026-09-23）** 在 Registry/权限模型上有两个增量，并更新对比表。

**① `scope` 字段加入 `AppFunctionMetadata` 与 `AppFunctionSearchSpec`（更新「权限/Registry 模型」对比行）**
- Android 的 Registry 元数据现新增 **`scope` 维度**——四平台里**首个由官方 Jetpack 显式加入元数据/搜索规格的「作用域」字段**，直接服务「谁能发现这个函数」的可见性/权限模型。
- **修正「运行时动态可见性 API」行**：Android 仍是四平台唯一有公开动态可见性 API 的平台（`getAppFunctionStates` 状态查询 + 现新增 `scope` 维度）；原 `setAppFunctionEnabled` 应标注「alpha11 起改为 `getAppFunctionStates` 状态查询、alpha12 新增 scope」。
- ⚠️ `scope` 具体语义（调用方可见性作用域 vs 功能分类域）**待 developer.android.com/ai/appfunctions 官方文档逐字段确认**，在确认前不写入对比表正文（延续 08-31「不被二手说法带偏」纪律）。

**② `AppFunctionData#serialize` 要求调用方提供元数据（对照「来源/溯源轴」待办）**
- alpha12 起序列化须由调用方附带元数据。**可能是 provenance 信号，但须谨慎**——此处「元数据」更可能是序列化结构元数据，未必等于「数据从哪来/可不可信」的 intent 来源 provenance。
- **结论不变**：本笔记「意图 Registry 来源/可信度（provenance）轴四平台全空白（confirmed）」结论**不因此改变**；即便 `serialize` 元数据被证实含来源语义，也须官方文档逐字段确认后才升级待办。最低成本补丁仍是意图 Registry 加 `readOrWrite` 声明位。

**③ 参数级安全约束补强（更新「权限/Registry 模型」对比行「鉴权/确认」旁注）**
- 新增 `AppFunctionUriValueConstraint` 公共 API，对 Uri 类型参数/返回值施加约束（scheme/路径限制）——是 AppFunctions 约束族（Int/String/Uri）的参数级安全补强，与「最小权限工具作用域」方向一致。

→ 对来源轴结论：alpha12 在「可见性作用域（scope）+ 参数约束（Uri）」上有实质推进，但**仍未触及「数据从哪来、可不可信」的来源轴**——本库最高优先待办的「来源轴四平台全空白」结论延续。

## 2026-10-09 增补（2026-10-13 二次复核确认：alpha13 确为真实发布，10-10 更正段已被推翻）：Android alpha13 引入函数侧访问限制 `@AppFunctionAccessLevel`（来源 [[AppIntent 每日情报 2026-10-09]]，详见 [[Android AppFunctions 设备侧意图 2026]]）

> 接续本笔记 09-25「Android alpha12 `scope` + `serialize`」与「Apple 用锁屏鉴权 + entitlement 治理」（行 81）、10-03「Apple 桌面 FDA agent-aware」。本期由官方 Jetpack Release Notes 确认 **AppFunctions `1.0.0-alpha13`（2026-10-07）** 新增 `@AppFunctionAccessLevel`，在权限模型上补全「函数侧访问限制」维度。

> [!info] 复核确认（2026-10-13 官方源直查推翻 10-10 更正）：经 2026-10-13 对 Jetpack Release Notes 发布页 + alpha-channel + all-channel 三处官方列表直查，`1.0.0-alpha13`（2026-10-07）**确为真实发布**，含 `@AppFunctionAccessLevel` 与 `@AppFunction`→`@AppFunctionDeclaration` 重命名；10-10 复核因索引滞后误判「最新仍 alpha12、alpha13 不可见」，其「降级为待官方确认」结论**已被推翻**。本段「Android alpha13 引入函数侧访问限制」**真实有效**，Android 权限模型「三向约束（caller 权限 + scope + 函数侧 `@AppFunctionAccessLevel`）」维持成立。详见 [[AppIntent 每日情报 2026-10-13]] 与 [[Android AppFunctions 设备侧意图 2026]] 10-13 复核段。

**① 权限/Registry 模型对比行更新（Android 列）**
- Android AppFunctions 权限模型现三向：① 调用方持 `EXECUTE_APP_FUNCTIONS`（caller 权限）；② 函数 `scope`（可见性作用域，alpha12）；③ **`@AppFunctionAccessLevel`（函数侧访问限制，alpha13）**。
- 与「调用方权限」对比行（行 56）互补：此前 Android 列仅「调用方须持 `EXECUTE_APP_FUNCTIONS`；每函数可配用户显式授权」，现补「函数可自声明访问级别」——**权限从单向（caller）扩展为 caller + 可见性 + 函数侧三段**。
- ⚠️ `@AppFunctionAccessLevel` 级别语义（public/protected/system 等）官方未展开，待 `developer.android.com/ai/appfunctions` 逐字段确认；在确认前仅记录「函数侧访问限制原语已就位」，**不写入具体级别对照**。

**② 不推翻来源轴结论**
- `@AppFunctionAccessLevel` 是访问/权限维度，与「意图元数据记录数据来源/可信度（provenance 轴）」**正交**——本笔记最高优先待办「来源轴四平台全空白（confirmed）」结论延续。Android 仍是四平台里**权限模型最厚**的平台（caller 权限 + 可见性 scope + 函数侧 access level + 企业 `APP_FUNCTIONS_DISABLED` 总开关），但仍**不记录 intent 来源 provenance**。

## 2026-10-26 增补：Android 进首个 Beta（成熟度）+ `description`→`instructions` 对齐 MCP 命名；iOS 27.1/Duo 双屏无新 Schema（来源轴待办维持，来源 [[AppIntent 每日情报 2026-10-26]]，详见 [[Android AppFunctions 设备侧意图 2026]] 与 [[Apple AppIntents Schema Protocol 2026]]）

> 接续 10-09/10-13「Android alpha13 引入函数侧 `@AppFunctionAccessLevel`」与 10-18「iOS 27.1 无设备 beta、跟踪窗口回退 10-23」。本期有两个对比表相关增量，并**关闭 iOS 27.1/Duo 双屏是否带新意图 Schema 的跟踪项**（不影响来源轴结论）。

**① 「成熟度/版本状态」对比行更新（Android 列）**
- AppFunctions 自 alpha10→alpha13 一路破坏性重命名后，于 **2026-10-21 跳到首个 `1.0.0-beta01`**（未发 alpha14）——这是四平台设备侧意图框架里**首个进入 Beta 稳定化通道**的实现，标志 Android 的 Registry/权限 API 面从「剧烈变动期」迈入「趋于稳定、接近 1.0」。
- 对照：Apple（27.x 稳定维护期，无新 Schema 域）、HarmonyOS（ArkAF 提供意图框架/Skill/端侧 A2A 三机制、稳定）、Windows（ODR 连接器注册 + 实验性 Agent Launchers，pre-GA）——Android 在「API 面成熟度里程碑」上本窗口领先（首个进 beta），但 **GA 日期仍待补**。

**② 「命名惯例 / 跨平台对齐」对比行更新（Android 列，跨平台信号）**
- beta01 把 `AppFunctionAppMetadata.description` 重命名为 **`instructions`**，官方明确「to align with MCP naming conventions」——Android 设备端 MCP 的元数据字段名**显式向标准 MCP 收敛**，强化「AppFunctions = 设备端 MCP 特例」身份（详见 [[MCP 与设备侧 MCP]]）。这是四平台里**首个把意图框架元数据语义对齐到通用 MCP 命名**的案例，对做跨体系 Registry 规范有参考价值。

**③ 关闭 iOS 27.1/Duo 双屏 Schema 跟踪项（不影响来源轴）**
- iOS 27.1 于 2026-10-23 随 iPhone Duo 正式发布；经核验 Duo 双屏适配走 **SwiftUI/UIKit 布局/铰链/scene-accessory API**，**未引入任何新的 `@AppIntent(schema:)` Domain 或 Entity**；App Intents Updates 官方页最新仍 June 2026。
- → 自 09-21 连续 8+ 轮跟踪的「iOS 27.1 双屏是否带新意图 Schema」问题**最终答案 = 否**，Apple 把折叠屏当作**显示/布局问题**而非**意图语义问题**处理（详见 [[Apple AppIntents Schema Protocol 2026]] 10-26 增补）。

**④ 来源/溯源轴（provenance）结论延续（最高优先待办不关闭）**
- 本窗口 Android（`scope`/`@AppFunctionAccessLevel`/beta01 `instructions`）、Apple（27.1 布局 API/27.2 RC）、HarmonyOS（稳定）、Windows（稳定）**均未新增「数据从哪来、可不可信」的 intent 元数据来源字段**。
- **结论不变**：四平台 OS intent Registry 层**来源轴仍全空白（confirmed）**，最低成本补丁仍是意图 Registry 加 `readOrWrite` 声明位（或 Android 式 scope 扩展为来源声明的变体）。Android 虽在权限/可见性/命名上最厚，但其 `instructions`/`serialize` 元数据仍属「描述来源/序列化结构」而非「数据 provenance」——不推翻空白结论。
- 横向参考（非 OS 意图层）：标准 MCP 本身也不强制 provenance；Chrome Origin Sets（[[Chrome Agent Origin Sets 与用户对齐评判器 2026]]）是浏览器层 source-of-truth 白名单、未下沉到 Android AppFunctions Registry——来源轴的 OS 级解法仍是本库最高优先未解项。

## 2026-10-28 增补：Apple「排除的 App」统一意图访问排除（消费者层）+ 来源轴结论延续（来源 [[AppIntent 每日情报 2026-10-28]]，详见 [[Apple AppIntents Schema Protocol 2026]] 10-28 增补）

> 接续 10-26「Android 进首个 Beta + `instructions` 对齐 MCP 命名」与「iOS 27.1/Duo 双屏无新 Schema（关闭跟踪项）」。本期补一个**消费者层意图访问治理**的对比维度增量，并**再次确认来源轴结论不变**。

**① 「意图访问边界」对比行扩展（Apple 列，消费者层）**
- iOS 27.2（10-26/27）新增**「排除的 App」（Excluded Apps）统一隐私设置**——用户可集中选择**哪些 App 不能被 Siri、搜索（Search）和建议（Suggestions）访问**。这是 Apple 侧一个**系统级「意图访问排除清单」**，把「系统 agent 对 App 能力与数据的访问」以**消费者隐私开关**形态纳入 OS 治理。
- 对照：Android 此前已在**企业 MDM 层**提供 `setAppFunctionsPolicy` / `APP_FUNCTIONS_DISABLED`（关闭 AppFunctions 数据，[[Android AppFunctions 设备侧意图 2026]] 10-02 增补）；Windows 在**企业/治理层**提供 ODR 连接器策略 + Agent Workspace 独立账号（[[Windows Copilot Actions 与 Agent Workspace 2026]]）。→ Apple 本期补的是**消费者隐私层**的意图访问排除，与 Android/Windows 的**企业/治理层**互为镜像，共同坐实本库长期主张：**agent 执行边界 = OS 权限/访问边界**（跨平台收敛在消费者层也成立）。
- ⚠️ 属用户隐私开关、非开发者框架 API，不构成 Registry/权限模型的新 API 维度；是否影响开发者侧 intent 注册可见性待 Apple 开发者文档逐字确认。

**② 来源/溯源轴（provenance）结论延续（最高优先待办不关闭）**
- 本窗口 Apple（27.2 无新 Schema、仅 Excluded Apps 消费者层开关）、Android（beta01 稳定）、HarmonyOS（稳定）、Windows（Surface 活动无新 API）**均未新增「数据从哪来、可不可信」的 intent 元数据来源字段**。
- **结论不变**：四平台 OS intent Registry 层**来源轴仍全空白（confirmed）**，最低成本补丁仍是意图 Registry 加 `readOrWrite` 声明位（或 Android 式 scope 扩展为来源声明的变体）。Apple 的 Excluded Apps 是「访问排除」而非「来源声明」，不补来源轴空白——来源轴的 OS 级解法仍是本库最高优先未解项。

**③ 成熟度/版本状态对比行（确认）**
- Apple：27.x 周期 App Intents Schema Protocol 已确认进入**稳定维护期**（App Intents Updates 官方页直查仍 June 2026，无 Oct 条目），无新增 Schema 域；跟踪重点转向 agentic 安全与消费者层意图访问治理。
- Android：AppFunctions 仍 `1.0.0-beta01`（10-21）为最新，无 beta02 / alpha14，维持「首个进 Beta」的成熟度领先（GA 日期仍待补）。

## 2026-10-29 增补：Connected Apps Platform 扩 AppFunctions 发现面到 Search + 来源轴结论延续（来源 [[AppIntent 每日情报 2026-10-29]]，详见 [[Android AppFunctions 设备侧意图 2026]]）

> 接续 10-28「Apple Excluded Apps 消费者层意图访问排除对照 Android 企业层 + 来源轴仍全空白延续 + 成熟度确认」。本期由 Android Dev Summit（10-28）官方公告补一个**发现/注册面（discovery surface）维度**增量，并再次确认来源轴结论不变。

**① 「发现/注册面」对比行扩展（Android 列，跨应用 Intent 工作流）**
- **Connected Apps Platform（预览，10-28 Dev Summit）**：开发者经 cloud-hosted MCP server 或 Android MCP（AppFunctions APIs）接入，在 Google Connected Console 注册并选择「出现在 Search / Gemini app / 两者」——AppFunctions 的 Registry 发现面从「Gemini 助手内」扩到**系统级搜索入口 Search**（"enable once, run Google-wide"）。官方称 50+ Connected Apps 已上线（Adobe/Peloton/Experian/Calm 等），Search 侧先在 US AI Mode（英文）开放。
- **对比含义**：这是四平台里**首个把设备侧意图框架（AppFunctions/Android MCP）直接接入「系统级搜索入口」的官方能力**——把「跨应用 Intent 工作流」从「助手内编排」扩到「搜索即触发 agentic action」。此前本表「发现/注册」行 Android = 「OS AppSearch registry」，现补一个**系统级 AI 入口层的二级发现面**（Gemini app + Search AI Mode）。⚠️ 仍为 preview + 分阶段开放，非 GA；是否受 `EXECUTE_APP_FUNCTIONS` 同一闸门约束待 developer.android.com/ai/appfunctions 确认。
- **权限兜底不变**：Search 入口触发的执行仍受 caller 权限（`EXECUTE_APP_FUNCTIONS`）+ 可见性 `scope` + 函数侧 `@AppFunctionAccessLevel` 三向约束（见本笔记 10-09 增补）；用户授权经 OAuth 2.1。但「Search 即触发」比「助手内显式指令」更易非预期调用——入口扩张使确认/隔离的 UX 约束更关键（与 [[确认机制]] / [[Confirmation UI 安全机制]] 同方向）。

**② 来源/溯源轴（provenance）结论延续（最高优先待办不关闭）**
- 本窗口 Android（Connected Apps Platform preview + ML Kit Agentic API alpha + beta01 稳定）、Apple（27.2 框架零变更、10-28 已复核）、HarmonyOS（稳定）、Windows（无新 OS API、仅 GitHub Copilot Fusion 本地路由实验预览落地·编码 harness）**均未新增「数据从哪来、可不可信」的 intent 元数据来源字段**。
- **结论不变**：四平台 OS intent Registry 层**来源轴仍全空白（confirmed）**，最低成本补丁仍是意图 Registry 加 `readOrWrite` 声明位（或 Android 式 `scope` 扩展为来源声明的变体）。Connected Apps Platform 是「发现面扩张」而非「来源声明」——它让 AppFunctions 更容易被系统入口发现，但**不记录意图数据的 provenance**，不补来源轴空白。来源轴的 OS 级解法仍是本库最高优先未解项。
- 横向参考（非 OS 意图层）：标准 MCP 本身不强制 provenance（Connected Apps Platform 同时支持 cloud MCP server 接入，亦未引入 provenance）；Chrome Origin Sets（[[Chrome Agent Origin Sets 与用户对齐评判器 2026]]）是浏览器层 source-of-truth 白名单、未下沉到 Android AppFunctions Registry。

**③ 成熟度/版本状态对比行（确认）**
- Apple：27.x 周期 App Intents Schema Protocol 已确认进入**稳定维护期**（App Intents Updates 官方页直查仍 June 2026，无 Oct 条目）。
- Android：AppFunctions 仍 `1.0.0-beta01`（10-21）为最新、无 beta02/alpha14；但 10-28 Dev Summit 补「Connected Apps Platform（preview）+ ML Kit Agentic API（alpha）」两层生态扩展，AppFunctions 从「工具声明 API」向「端侧意图执行总线完整栈」生长（均非 GA）。
- HarmonyOS / Windows：均稳定、无窗口内新 OS API。

## 2026-11-03 复核增补：Connected Apps 双路由再确认（NeoTeo 11-03，★5 复述、无新字段）

> 接续本笔记 10-29 增补（Connected Apps Platform 扩 AppFunctions 发现面到 Search + 双路径）。NeoTeo（11-03）重述 10-28 公告的两条集成路径——**cloud-hosted MCP**（触达 Search / Gemini on web·Android·iOS）与 **Android MCP**（设备本地、触达 Gemini on Android）——与既有「Remote MCP = 推荐默认跨平台路径 / AppFunctions = client-side 本地路径」完全一致，**无新字段/新 API**。来源轴结论不变（仍全空白）。来源 [[AppIntent 每日情报 2026-11-03]]。
