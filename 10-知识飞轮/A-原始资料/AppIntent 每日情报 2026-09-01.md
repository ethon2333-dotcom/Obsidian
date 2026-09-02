---
type: raw
status: inbox
date: 2026-09-01
source:
  - "https://android-dot-devsite-v2-prod.appspot.com/jetpack/androidx/releases/appfunctions"
  - "https://developer.android.google.cn/ai/appfunctions"
  - "https://developer.android.google.cn/blog/posts/android-17-is-here"
  - "https://ecorpit.com/eu-dma-android-ai-assistant-interoperability-plan-2027"
  - "https://huggingface.co/jromarllegue/LittleLamb-ToolCalling-ONNX"
  - "https://aibacon.net/posts/cactus-needle-2-14mb-45m-tool-calling-model-esp32.html"
  - "https://d-central.tech/local-llm-agent-capability/"
importance_score: "★★★★☆（7~8/10：窗口内唯一净新增 OS 框架 API = AppFunctions alpha11；跨平台 BFCL v4 数据 + DMA 跨助手强制开放为增量）"
intent_category: "系统级意图框架 / 设备侧 MCP / 端侧 Planner 评测 / 跨平台 Registry 可发现性 · 7 日滚动窗口 2026-08-25→09-01"
tags: [情报, AppIntent, 每日情报, AppFunctions, alpha11, BFCLv4, DMA, 端侧Planner, 2026-09-01]
---

# AppIntent 每日情报 2026-09-01

> [!abstract] 30 秒速览
> - **核心突破（★7/10·OS 框架净新增）**：Android AppFunctions Jetpack **`1.0.0-alpha11`（2026-08-26 发布）** 是窗口内唯一净新增的 OS 级意图框架 API 变更——引入 `@AppFunctionSignature` 支持**动态注册**，并用 `AppFunctionState` / `AppFunctionManager#getAppFunctionStates` **取代**旧的 `AppFunctionMetadata#isEnabled` 门控（元数据与状态彻底分离）。这把本库 08-03 记为「四平台唯一动态可见性 API」的 `setAppFunctionEnabled` 机制升级为 state-based。
> - **关键指标（跨平台端侧 Planner 评测）**：BFCL v4 公开榜出现两条高信号数据——**Apple 设备端 Foundation Model 首次入榜，单轮 61.7%**（第三方 aibacon 引 Berkeley 榜）；**LittleLamb-ToolCalling-ONNX（0.3B）BFCL v4 51.55%（think）/ 50.51%（no-think）**，以 0.3B 体量逼近 Qwen3-0.6B（54.08%）并碾压 FunctionGemma-270M（27.03%）。**Needle 2（45M）42.6% 获第三方独立确认**，并显式给出「置信度门控→升级云端而非硬猜」的契约。
> - **OS Agent 场景（跨平台/监管）**：欧盟 DMA 要求 Google 在 **2027-08 前**向竞品助手开放 11 项 Android AI 能力，AppFunctions Registry 使函数可被**任一认证助手**（非仅 Gemini）发现，`EXECUTE_APP_FUNCTIONS` 由此成为 EU 语境下的「认证闸门」——意图 Registry 的「跨助手可发现性」首次被监管强制，是四平台对比表的新维度。

## 正文拆解

### ① Schema 定义与语义路由机制

**A. Android AppFunctions alpha11（净新增，官方 Jetpack Release Notes，2026-08-26）**
- **`@AppFunctionSignature`（experimental public API）**：支持**通过 Jetpack 动态注册 AppFunction**（b/501032667）——此前函数须编译期静态声明，现在可在运行时注入签名。这是 AppFunctions 从「编译期 schema」走向「运行时可塑 Registry」的关键一步。
- **`AppFunctionState` + `AppFunctionManager#getAppFunctionStates` 取代 `AppFunctionMetadata#isEnabled`**：元数据与状态**彻底分离**（b/494238383）。本库 08-03 节记的 `setAppFunctionEnabled` / `isAppFunctionEnabled` 动态门控**机制仍在，但 API 形态已迁移到 state-based 查询**——Registry 仍是随账号/功能状态实时变化的动态视图，只是读取入口变了。
- 其余 API 变更：`getAppFunctionActivityStates`（b/542075714）、`ExtensionsAppFunctionService`（sidecar 支持，b/524941402）、`observeAppFunctions` 对齐平台 API。
- Bug 修复：修复 OOBE 阶段调用 `setAppFunctionEnabled` 因缺运行时元数据崩溃（b/536750020）——印证动态门控已在真机初始化路径被调用。
- 详见 [[Android AppFunctions 设备侧意图 2026]]（本次追加 alpha11 小节）｜ 跨平台维度 [[四平台意图 Registry 来源轴与权限模型对比 2026]]（更新「运行时动态可见性 API」行）。

**B. 跨平台端侧 Planner 评测增量（BFCL v4，第三方来源，标待补）**
- **Apple on-device Foundation Model 61.7%**（aibacon 引 Berkeley 榜，单轮 3,641 行）：Apple 自家设备端 FM 首次出现在公开工具调用榜，高于 LFM2.5-230M（60.8%）、FunctionGemma-270M（46.1%）、Needle 2（42.6%）——**首次拿到「Apple 自家本地 Planner vs 开源小模型」的公开可比分**。⚠️ 第三方引述，待 Berkeley 官方榜复核。
- **LittleLamb-ToolCalling-ONNX 0.3B**：BFCL v4 51.55%（think）/ 50.51%（no-think），Qwen3-0.6B（think）54.08%、FunctionGemma-270M 27.03%（think=no-think，因其无 thinking 模式）。0.3B 体量逼近 0.6B 且碾压 270M——**再次印证「<1B + 微调 + 严格约束」可承担主路由**（呼应本库 07-31 纪律）。⚠️ 数字来自 HF 模型卡（jromarllegue），第三方。
- **FunctionGemma 270M BFCL v4 全量 = 27.03**（think=no-think）：与其单轮 46.1% 拉开近 20 点，正是 v4 把 70% 权重压在 agentic+multi-turn 的体现（与 08-04 权重结论一致）。
- **Gemma 4 native tool tokens**（d-central 第三方）：Google 借 FunctionGemma-270M 与 Gemma 4 tokens 修复 Gemma 2/3「无原生工具模板、只能 grammar-constrain」的短板。⚠️ 待官方确认许可与 API。
- 详见 [[Function Calling 端侧工具调用]]（本次追加 2026-09-01 评测小节）。

**C. HarmonyOS / Windows / Apple：窗口内无净新增，见「已复核·无净新增」表**
- Apple（iOS 27 Beta 5 已录，Beta 8 与 08-15 逐字一致）、HarmonyOS（7 消费版秋季待发，无新 API）、Windows（Copilot Vision 已于 2026-05 GA、官方文档 2025-12-05 后再无更新）均无窗口内净新增。

### ② 系统安全与用户体验（Confirmation / 隔离 / 防注入）

**A. AppFunctions 跨助手可发现性与 DMA 强制开放（★7/10·跨平台监管）**
- 欧盟 DMA 决策要求 Google 在 **2027-08 前**向 ChatGPT / Claude / 欧洲本土助手等竞品开放 11 项 Android AI 能力；AppFunctions Registry 使函数**可被任一认证助手发现，而非仅 Gemini**，`EXECUTE_APP_FUNCTIONS` 权限边界在 EU 语境下沉为「认证闸门」。
- 含义：意图 Registry 的「跨助手可发现性」首次被**监管强制**——OS PM 设计 Registry 时，「谁可发现我的能力」从产品选择变成合规义务；也意味着 Android 端「单一 Gemini 集成」假设须改为「 plural assistants」。
- ⚠️ 来源为 ecorpit 对 DMA 决策的分析 + 厂商披露；**具体 11 项能力清单与官方 DMA 文本措辞待补**。
- 详见新建节点 [[AppFunctions 跨助手可发现性与 DMA 强制开放 2026]]。

**B. Needle 2 置信度门控的「升级契约」再确认（安全机制层面）**
- aibacon 第三方确认 Needle 2 BFCL v4 = 42.6%，并显式给出设计契约：**置信分趋零 → 返回空调用 `[]` 而非硬编一个函数**，把「端侧→云端升级」做成确定性旋钮（而非模型自决）。这与 [[带外防御与确定性门控]] 同构，也补全了 [[Confirmation UI 安全机制]] 的「触发器应由系统确定性判定」主张。
- 许可干净（MIT 代码 / Apache-2.0 权重），可编译到 RISC-V / MIPS32el，落到 ESP32（28MB RAM）、树莓派 5（500+ tok/s）、Meta Quest 3S。
- 详见 [[端侧 Router 置信度门控与工具可达性收缩 2026]]（本次追加 aibacon  corroboration 小节）。

**C. 其余安全面（XPIA / Confirmation UI / Agent Workspace 隔离）各平台无窗口内净新增**，指向既有笔记：[[XPIA 跨提示注入]] ｜ [[Confirmation UI 安全机制]] ｜ [[隔离执行]] ｜ [[Agent Data Injection 数据注入攻击]]。

### 已复核·无净新增（避免下次重复检索）

| 平台 | 复核对象 | 结论 |
|---|---|---|
| Apple | iOS 27 Beta（08-15 已录 Beta 5 逐字内容；Beta 8 同 bug 号 173431080 等） | 无新增 schema API；不重复计数。 |
| Android | AppFunctions `1.0.0-alpha10`（2026-07-01）→ **alpha11（2026-08-26）已录为本轮净新增**；Android 17 GA（2026-06-16）已录 | 仅 alpha11 为窗口内净新增。 |
| HarmonyOS | Intents Kit / ArkAF 官方文档 + HDC2026（7 开发者 Beta 6-12、消费 Beta 8-3、正式版秋季） | 无新 API；Skill 同名冲突/3 秒超时/A2UI 静默失败（08-26 已录）。 |
| Windows | OS agentic security 四支柱 + ODR + Agent Workspace（官方文档 2025-12-05 后再无更新）；Copilot Vision 2026-05 GA | 无净新增；26H2/Ignite 2026-11 仅为路线图/承诺，非已发布 API。 |
| 跨平台 | BFCL v4 公开榜（benchlm 镜像站） | Apple FM 61.7% / LittleLamb 0.3B 51.55% 等已在 [[Function Calling 端侧工具调用]] 入表；Gemma 4 tokens / Needle 2 升级契约已补。 |

> [!note] 概念节点双链
> [[意图模式规范]] [[语义路由]] [[端侧工具调用]] [[确认机制]] [[元服务]] [[隔离执行]] [[A2A 端侧智能体协议]] [[XPIA 跨提示注入]]

## 值得保留的点（索引）

- **★7/10 · 净新增（OS 框架 API）**：AppFunctions `alpha11` 动态注册 `@AppFunctionSignature` + `AppFunctionState` 取代 `isEnabled`——原子笔记 → [[Android AppFunctions 设备侧意图 2026]] ｜ 主题枢纽 → [[四平台意图 Registry 来源轴与权限模型对比 2026]]
- **★7/10 · 净新增（跨平台评测）**：Apple FM 61.7% / LittleLamb 0.3B 51.55% / FunctionGemma 全-v4 27.03% / Needle 2 升级契约——原子笔记 → [[Function Calling 端侧工具调用]] ｜ [[端侧 Router 置信度门控与工具可达性收缩 2026]]
- **★7/10 · 净新增（监管）**：DMA 2027-08 强制 AppFunctions 跨助手开放——原子笔记 → [[AppFunctions 跨助手可发现性与 DMA 强制开放 2026]] ｜ 主题枢纽 → [[意图框架·跨体系索引 MOC]]
- **★0/10 · 已复核无净新增**：iOS 27 Beta / HarmonyOS 7 / Windows 四支柱 / Copilot Vision GA —— 见上表，下次不再重复检索。

## 后续动作

- [ ] 核实 AppFunctions `alpha11` 的 `@AppFunctionSignature` 动态注册是否要求新的 Manifest 权限或签名（b/501032667 仅记为 experimental）。
- [ ] 用 Berkeley 官方 BFCL v4 榜复核 Apple FM 61.7% 与 LittleLamb 0.3B 51.55%（当前为第三方引述）。
- [ ] 抓取欧盟 DMA 决策官方文本，确认「11 项 Android AI 能力」清单与 2027-08  deadline 措辞；回填 [[AppFunctions 跨助手可发现性与 DMA 强制开放 2026]]。
- [ ] 把 alpha11 的 `AppFunctionState` 取代 `isEnabled` 反映进 [[四平台意图 Registry 来源轴与权限模型对比 2026]] 的「运行时动态可见性 API」行（原记 `setAppFunctionEnabled` 现应标注「alpha11 起改为 state-based 查询」）。
- [ ] 延续待办：Berkeley 官方 BFCL v4 博客原文；Watch OS 26 是否 Trust Insights 类；NowSecure / AgentAntibody 独立核验；Chrome Origin Sets 官方 URL 逐字复核。
