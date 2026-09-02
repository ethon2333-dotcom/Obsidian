---
type: output
status: draft
created: 2026-09-01
method_used: "WebSearch/WebFetch 直取官方源（Apple/Android/HarmonyOS/Microsoft 官方 + Jetpack Release Notes）+ 第三方评测交叉（aibacon/LittleLamb/HF/d-central/ecorpit）；7 日滚动窗口 08-25→09-01"
derived_from: "[[AppIntent 每日情报 2026-09-01]]"
tags: [速览, AppIntent, 每日情报, AppFunctions, alpha11, BFCLv4, DMA, 端侧Planner, 2026-09-01]
---

# AppIntent 每日情报速览 2026-09-01

## 目标读者与目标

OS 产品经理 / 端侧 Agent 框架设计者。今日目标：在四平台官方框架层普遍「无净新增」的窗口里，定位并**收录三条真增量**——① Android AppFunctions `alpha11`（唯一净新增 OS 框架 API）② 跨平台 BFCL v4 端侧 Planner 评测新数据 ③ 欧盟 DMA 强制 AppFunctions 跨助手开放——并把「已复核·无净新增」显式列出避免下次重复检索。

## 正文（速览）

**① Android AppFunctions `alpha11`（★7/10，唯一净新增 OS 框架 API）**
- 性质：Jetpack `1.0.0-alpha11`（2026-08-26）引入 `@AppFunctionSignature`（experimental）支持**动态注册**；`AppFunctionState` + `AppFunctionManager#getAppFunctionStates` **取代** `AppFunctionMetadata#isEnabled`，元数据显示态与状态分离。
- 价值：本库 08-03 记为「四平台唯一动态可见性 API」的 `setAppFunctionEnabled` 机制升级为 state-based；Registry 仍是随状态实时变化的动态视图，只是读取入口迁移。
- 深度：[[Android AppFunctions 设备侧意图 2026]] ｜ [[四平台意图 Registry 来源轴与权限模型对比 2026]]

**② 跨平台端侧 Planner 评测新数据（★7/10，BFCL v4）**
- **Apple on-device FM 61.7%**（单轮，第三方引 Berkeley 榜）：Apple 自家本地 Planner 首次公开可比，高于 LFM2.5-230M（60.8%）/ FunctionGemma（46.1%）/ Needle 2（42.6%）。
- **LittleLamb-ToolCalling-ONNX 0.3B 51.55%（think）/ 50.51%（no-think）**：0.3B 体量逼近 Qwen3-0.6B（54.08%）、碾压 FunctionGemma-270M（27.03%），再证「<1B+微调+严格约束」可担主路由。
- **FunctionGemma 270M 全-v4 = 27.03**（think=no-think）：与单轮 46.1% 拉开近 20 点，正是 v4 把 70% 权重压在 agentic+multi-turn 的体现。
- **Needle 2 42.6% 获第三方确认 + 升级契约**：置信趋零→返回空调用而非硬编；MIT/Apache 许可，落 ESP32/树莓派 5/Quest 3S。
- 深度：[[Function Calling 端侧工具调用]] ｜ [[端侧 Router 置信度门控与工具可达性收缩 2026]]

**③ 欧盟 DMA 强制 AppFunctions 跨助手开放（★7/10，监管/跨平台）**
- 性质：DMA 要求 Google 在 2027-08 前向 ChatGPT/Claude/欧洲助手开放 11 项 Android AI 能力；AppFunctions Registry 使函数可被任一认证助手发现，`EXECUTE_APP_FUNCTIONS` 在 EU 下沉为「认证闸门」。
- 价值：意图 Registry 的「跨助手可发现性」首次被监管强制，OS PM 须把「plural assistants」写入设计前提。
- 深度：[[AppFunctions 跨助手可发现性与 DMA 强制开放 2026]]

**④ 执行安全延伸（无窗口内净新增，指向既有笔记）**
- 来源轴空白 → ADI 防护缺口一致（[[Agent Data Injection 数据注入攻击]]）；XPIA / Confirmation UI / Agent Workspace 隔离各平台无新动作。
- 深度：[[XPIA 跨提示注入]] ｜ [[Confirmation UI 安全机制]] ｜ [[隔离执行]]

## 使用的方法

- 7 日滚动窗口（08-25→09-01），取窗口内净增量 + 库内空白补漏。
- 分类纪律：先判「新事实 vs 已覆盖 vs 第三方误传」——alpha11 经官方 Jetpack Release Notes 直查确认；Apple FM 61.7% / LittleLamb 标第三方来源、标待补；Windows 26H2/Ignite 仅为路线图非已发布 API，排除。
- 诚实纪律：显式标注「alpha11 为窗口唯一净新增 OS API」「Apple FM/LittleLamb 为第三方引述」「DMA 为分析、待官方文本」。

## 复盘

### 有效的部分
- 延续「无净新增显式列表」避免重复检索；延续「官方 Release Notes 直查」判定净新增而非轻信二手。
- 本日三条真增量均落在「OS 框架 API / 跨平台评测 / 监管」三个互补面，比前几轮「仅收口待办」信息密度更高。

### 需要改进的部分
- 第三方 BFCL 数字（Apple FM / LittleLamb）尚未经 Berkeley 官方榜复核，下一轮须优先花检索预算专攻官方源，避免长期停留在第三方引述。
- alpha11 的 `@AppFunctionSignature` 动态注册权限边界未明，需补 Manifest/签名要求。

### 回流到 A 的新问题或素材
- 待把 alpha11 `AppFunctionState` 取代 `isEnabled` 反映进 [[四平台意图 Registry 来源轴与权限模型对比 2026]] 的「运行时动态可见性 API」行。
- 待抓 DMA 官方文本回填 [[AppFunctions 跨助手可发现性与 DMA 强制开放 2026]]。
- 延续：Berkeley 官方 BFCL v4 博客原文、Watch OS 26 Trust Insights 类、NowSecure/AgentAntibody 复核、Chrome Origin Sets 官方 URL。

## 关联
- 平台：[[Android AppFunctions 设备侧意图 2026]] ｜ [[Apple AppIntents Schema Protocol 2026]] ｜ [[HarmonyOS Intents Kit 与 ArkAF 2026]] ｜ [[Windows Copilot Actions 与 Agent Workspace 2026]] ｜ [[Function Calling 端侧工具调用]]
- 安全：[[XPIA 跨提示注入]] ｜ [[Confirmation UI 安全机制]] ｜ [[隔离执行]] ｜ [[Agent Data Injection 数据注入攻击]] ｜ [[端侧 Router 置信度门控与工具可达性收缩 2026]]
- 跨平台：[[四平台意图 Registry 来源轴与权限模型对比 2026]] ｜ [[AppFunctions 跨助手可发现性与 DMA 强制开放 2026]]
- 枢纽：[[意图框架·跨体系索引 MOC]] · [[语义路由]] · [[确认机制]] · [[XPIA 跨提示注入]]
