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
