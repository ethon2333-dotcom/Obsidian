---
date: 2026-10-09
tags: [AppIntent, 每日情报, Android, AppFunctions, alpha12, 版本复核, 权限模型, 执行安全]
source: "https://developer.android.com/jetpack/androidx/releases/appfunctions ; https://developer.android.com/jetpack/androidx/versions/alpha-channel"
importance_score: "★★★★☆"
intent_category: "执行安全 / 系统级意图框架 / 权限模型"
---

> [!info] 复核确认（2026-10-13 官方源直查推翻 10-10 更正）
> 本笔记正文对 **AppFunctions `1.0.0-alpha13`（2026-10-07）及 `@AppFunctionAccessLevel` / `@AppFunction`→`@AppFunctionDeclaration` 重命名等变更的记载，经 2026-10-13 对官方源再次直查，已获官方 corroboration**：`developer.android.com/jetpack/androidx/releases/appfunctions` 发布页、alpha-channel 与 all-channel 发布列表均明确列出 **`1.0.0-alpha13`（2026-10-07 发布）**，含「Added @AppFunctionAccessLevel / Rename AppFunction→AppFunctionDeclaration / Rename ObserveAppFunctionsEvent→AppFunctionsChangeEvent / Surface AppFunctionMetadata in AppFunctionService」。**即 10-09 跑本正确、10-10 跑的「更正」系误判（其当时索引快照滞后），本笔记 alpha13 记载真实有效。** 10-10 的「⚠️ 更正」段已在 [[Android AppFunctions 设备侧意图 2026]] 与 [[四平台意图 Registry 来源轴与权限模型对比 2026]] 文末由 10-13 复核段推翻。详见 [[AppIntent 每日情报 2026-10-13]]。

# AppIntent 每日情报 2026-10-09

> [!abstract] 30 秒速览
> 本窗口（2026-10-08 21:00 → 10-09 21:00）**核心净新增 = Android AppFunctions `1.0.0-alpha13`（官方 Jetpack Release Notes 标注 2026-10-07 发布）**——这是继 alpha12（09-23）以来的首个版本进位，且**上一轮（10-08）误判「alpha12 无 alpha13」未捕获**，本运行予以纠正。alpha13 在权限模型上落了**首个函数侧访问限制原语 `@AppFunctionAccessLevel`**（access restriction setting），并伴随 `@AppFunction` → `AppFunctionDeclaration` 破坏性重命名、`ObserveAppFunctionsEvent` → `AppFunctionsChangeEvent` 重命名、`AppFunctionMetadata` 在 `AppFunctionService` 中暴露。**其余三平台无 OS 框架净新增**：Apple（iOS 27.2 beta 3 无新 `@AppIntent(schema:)` Schema；AT&T carrier bundle 更新非框架）、HarmonyOS（Intents Kit 官方页稳定）、BFCL v4（端侧 Planner 无新入榜）。Windows 10-07 事件在 10-09 多点媒体复述，补得 3 个非 GA 级新 surface 细节（taskbar Search actions / Entra 本地 agent 身份扩展 / MAI Code 1.1 Flash 本地参数 corroboration），均属已捕获事件的补细节。XPIA 窗口内命中（CVE-2026-26133 M365 / OpenClaw / PraisonAI）经核查为非四平台 OS 框架执行总线，按口径丢弃。

## ① Schema 定义与语义路由（本窗口）

| 平台 | 本窗口 Schema/路由层净新增 | 重要性 | 处置 |
|---|---|---|---|
| Android | **AppFunctions `1.0.0-alpha13`（2026-10-07）**——`@AppFunctionAccessLevel` 函数侧访问限制 + 重命名 + `AppFunctionMetadata` 暴露 | ★★★★☆ | **真增量·已收录（纠正 10-08 漏捕）** |
| Apple | 无（`@AppIntent(schema:)` 无新；iOS 27.2 beta 3 = build 24B5099f，无新 Schema/App Intents Domains API） | — | 已复核·无净新增 |
| HarmonyOS | 无（Intents Kit 官方页 2026-09-14 稳定；ArkAF 2.0 / A2UI 无新 OS API） | — | 已复核·无净新增 |
| 跨平台 BFCL | 无（端侧 Planner 无新入榜；FunctionGemma 270M / LittleLamb 0.3B / Qwen3-0.6B 数字为已知 model card，无新官方 entry） | — | 已复核·无净新增 |

要点：
- **alpha13 纠正**：上一轮（10-08）结论「AppFunctions 守 alpha12 无 alpha13」**有误**——alpha13 已于 **2026-10-07** 在 Jetpack alpha-channel 发布。本运行直查 `developer.android.com/jetpack/androidx/releases/appfunctions` 与 alpha-channel 确认。alpha13 落在上一轮窗口边缘（10-07），故以「纠正 + 补捕」处理。
- Apple / HarmonyOS / BFCL：均无路由/评测层净新增，延续「OS 框架不日更」。

## ② 系统安全与 UX（Confirmation / 隔离 / 反注入）

### 🔑 真增量①：Android AppFunctions `1.0.0-alpha13`（★7/10，权限模型首个函数侧访问限制原语，纠正 10-08 漏捕）
- **发布时间与来源**：Jetpack `androidx.appfunctions:appfunctions:1.0.0-alpha13` 于 **2026-10-07** 发布（alpha-channel 与 Release Notes 均标注）；含 `appfunctions` / `appfunctions-compiler` / `appfunctions-testing` 三件套。来源：官方 <https://developer.android.com/jetpack/androidx/releases/appfunctions> + <https://developer.android.com/jetpack/androidx/versions/alpha-channel>。
- **API 变更（逐条，来自官方 Release Notes）**：
  - **`Add @AppFunctionAccessLevel annotation to support access restriction setting` (Id47e1)** —— **本窗口最高价值项**：AppFunctions 首次引入**函数侧声明的访问级别限制**（区别于 alpha12 已有的调用方侧 `EXECUTE_APP_FUNCTIONS` 权限与 `scope` 可见性维度）。这是四平台里设备侧 MCP / 意图 Registry 的**首个「函数自身声明可访问性」原语**，把权限模型从「调用方持权 + 可见性作用域」补了第三块「函数侧访问限制」。
  - **`Rename AppFunction annotation to AppFunctionDeclaration` (I4b15d)** —— **破坏性重命名**：开发者标注从 `@AppFunction` 改为 `@AppFunctionDeclaration`，迁移需注意（与 KSP 编译器插件协同）。
  - **`Rename ObserveAppFunctionsEvent to AppFunctionsChangeEvent` (Iec918)** —— 运行时变更事件重命名。
  - **`Surface AppFunctionMetadata in AppFunctionService` (If1117)** —— 服务侧可获取 `AppFunctionMetadata`，利于执行时按元数据做策略/审计。
  - **Bug Fixes**：`AppFunctionData` 支持全部内建 proxy 类型（LocalDate / LocalTime / Instant / ZoneId）。
- **对端侧意图路由 + 权限模型的含义**：Android 的 AppFunctions 权限模型现由三层构成——① 调用方持 `EXECUTE_APP_FUNCTIONS`（alpha 以来）；② 函数可见性 `scope`（alpha12，09-23）；③ **函数侧访问限制 `@AppFunctionAccessLevel`（alpha13，本窗口）**——形成「谁能调 / 谁能看见 / 函数自身允许谁访问」三向约束。详见 [[Android AppFunctions 设备侧意图 2026]] 10-09 增补 + [[四平台意图 Registry 来源轴与权限模型对比 2026]] 10-09 增补。
- **诚实标注**：`@AppFunctionAccessLevel` 的**具体级别语义**（如 public / protected / same-app / system 等级别）官方 Release Notes 仅写「support access restriction setting」，**未展开级别定义**；确切语义待 `developer.android.com/ai/appfunctions` 官方文档逐字段确认（延续 09-25 `scope` 纪律）。它**不属于**「数据从哪来/可不可信」的来源/provenance 轴——来源轴四平台全空白结论**不因此改变**。

### 真增量②（状态/补细节，低于净新增阈值，已捕获事件延伸）：Windows 10-07 事件在 10-09 多点复述补 3 个 surface 细节
- 2026-10-07 微软「Hybrid Intelligence」活动（MXC GA 等）已在本库 10-08 跑作为**唯一 OS 级净新增**完整收录。10-09 多家媒体（foxvector / my2cents.ai / 163 / toutiao-InfoQ / testingcatalog）复述并补得 3 个此前未单列的细节：
  - **Windows Search taskbar actions**：Insiders 可从任务栏搜索直接触发动作（切换设置、管理窗口、发消息）——新增一个 agentic 入口 surface（属 10-07 事件叙事延伸）。
  - **Entra agent identity 扩展至本地 agent**：微软称将用 **Microsoft Entra 区分 agent 活动与用户活动**，并把 **Agent 365 控制扩展到本地 agent**（my2cents.ai 10-09）——把「agent 身份隔离」从云端 M365/Entra 层下沉到本地 Windows agent。
  - **MAI Code 1.1 Flash 本地参数 corroboration**：3-bit 量化（尺寸近乎 -80%）、256K 本地上下文（my2cents.ai / Microsoft AI 推文 corroborate 10-08 跑「待补」项）；`llama.cpp` 进 Windows ML（GPU/NPU/CPU）；GitHub HydraFusion 本地模型路由 10 月底实验性预览。
- **处置**：均属 10-07 已捕获事件的补细节/复述，**非本窗口独立净新增**；仅向 [[Windows Copilot Actions 与 Agent Workspace 2026]] 追加 10-09 状态段（taskbar Search actions + Entra 本地身份扩展 + MAI Code 本地参数 corroboration），不升新 B 节点。

### 去伪/丢弃（按口径）
- **Apple**：iOS 27.2 beta 3（24B5099f）无新 `@AppIntent(schema:)`；9to5mac 10-08「Apple rolls out AT&T carrier update for iPhone 18 Pro Max on iOS 27.2 beta」为**运营商配置包更新（carrier bundle 72.0.3）**，**非 App Intents 框架变更**，丢弃。开发者论坛「iOS 27.2 beta App Shortcut phrase fails」为 bug 报告，非框架 API。
- **HarmonyOS**：Intents Kit 官方页最后更新 2026-09-14、ArkAF 文档稳定、无新 OS API，丢弃。
- **BFCL v4**：FunctionGemma 270M（BFCL v4 27.03）、LittleLamb 0.3B（think 51.55 / no-think 50.51）、Qwen3-0.6B（think 54.08）数字来自 HF model card，**均为已知数据、无新官方 entry**；社区 QuantCall 量化实测（dev.to/d9bl，测 Qwen3-0.6B 在 Q4_K_M 下工具调用不显著退化）**日期未确认、且为第三方研究非 OS 框架**，作低置信补充、不升净新增。
- **XPIA（按「非四平台 OS 框架执行总线」丢弃）**：CVE-2026-26133（Microsoft 365 Copilot AI command injection，Permiso P0 Labs）——属 **M365 应用/云层** XPIA，非 Windows OS 执行总线（同此前 EchoLeak/ForcedLeak/CamoLeak 处置）；CNCERT 警示的 **OpenClaw** 第三方自托管 agent、PraisonAI AICoder 19 项缺陷（10-08 披露，prompt injection → root 文件写）——**均第三方工具链、非四平台 OS 框架**，同 10-06 丢弃 GitLab AI Gateway / 10-05 丢弃 MCP 工具链 CVE 口径。

> [!note] 概念节点双链
> [[意图模式规范]] [[语义路由]] [[端侧工具调用]] [[确认机制]] [[元服务]] [[隔离执行]] [[A2A 端侧智能体协议]] [[XPIA 跨提示注入]]
