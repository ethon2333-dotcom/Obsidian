---
date: 2026-11-03
tags: [AppIntent, 每日情报, iOS273中国Qwen, 端侧LLM按区切换, 复核型, 来源轴延续]
source: "https://www.macrumors.com/2026/10/30/apple-says-ios-27-3-beta-coming-next-week/ ; https://dev.to/shivaysinghrajput/apple-intelligence-on-qwen-in-china-what-developers-need-to-test-before-ios-273-328j ; https://www.unite.ai/apple-brings-first-apple-intelligence-features-to-china-in-ios-27-3/ ; https://forkast.news/android-appfunctions-beta-does-not-mean-open-agent-access/ ; https://www.neoteo.com/en/google-opens-a-developer-route-for-connected-apps ; https://developers.google.com/connected-apps ; WebSearch/WebFetch 链路故障，改用 curl + Google News RSS + DuckDuckGo 直查官方/权威源（无 Horizon MCP，仅 agent-mail 在线）"
importance_score: "★★★☆☆（头条 iOS 27.3 中国 Qwen 端侧模型 ≈7/10；其余为复述/边界澄清 ★5）"
intent_category: "系统级意图框架 / 端侧 Planner 模型 / 跨平台对比 / 执行安全（权限边界）"
---

# AppIntent 每日情报 2026-11-03

> [!abstract] 30 秒速览
> 本窗口（2026-11-02 12:21 → 11-03 23:38，接续 11-02 运行）**出现一个真正跨阈值的 OS 级进展**：**iOS 27.3 首个开发者 beta 于 11-03（美西）/ 11-04（中国）落地，首次在中国区以第三方（阿里 Qwen）端侧模型驱动 Apple Intelligence（Siri / Writing Tools / Visual Intelligence）**——这是 Apple 第一次在主力市场用非自研/非 PCC 的第三方端侧 LLM 充当「意图执行总线」的 Planner 底座，且经同一 Siri / App Intents 接口暴露，属「端侧 Planner 模型 + 跨应用编排」范畴（★7/10）。其余平台本窗口**零净新增 API**：Android（AppFunctions 仍 beta01；Connected Apps 双路由 / AppFunctions 权限边界为 10-28+ 已捕获材料的复述，★5）、HarmonyOS（稳定）、Windows（无新执行总线 API；agentic 安全书仍 2025-11-18）、BFCL v4（无新 ≤数 B 端侧 Planner entry）。本运行**新建 1 个 B 概念节点**（iOS 27.3 中国 Qwen 端侧模型），对 2 个既有 B 笔记追加 ★5 复述状态行（无新字段）。

## ① Schema 定义与语义路由机制（本窗口）

| 平台 | 本窗口 Schema/路由层净新增 | 重要性 | 处置 |
|---|---|---|---|
| Apple | **iOS 27.3 beta（11-03 美 / 11-04 中）落地，中国区 Apple Intelligence 由阿里 Qwen 端侧模型驱动**（Siri / Writing Tools / Visual Intelligence）；官方报道未提新 `@AppIntent(schema:)` Schema——属「意图执行底座（Planner/LLM）按地区切换第三方端侧模型」的模型层变更，非新 schema API | ★★★★☆（★7/10，跨阈值） | 新建 B 节点 + A 索引 |
| Android | AppFunctions 仍 `1.0.0-beta01`（10-21）最新、无 beta02/alpha14；Connected Apps「cloud-hosted MCP / Android MCP 双路由」与 AppFunctions「beta≠开放 agent 访问、API 状态与正式发布分离」均为 10-28/10-29 已捕获材料复述，无新字段 | ★★☆☆☆（无净新增；复述 ★5） | 既有 B 追加状态行 |
| HarmonyOS | Intents Kit / ArkAF 稳定，无窗口内新 OS 框架 API | — | 已复核·无净新增 |
| 跨平台 BFCL | FunctionGemma 270M / qwen3-0.6b-tool-router 仍不在精选榜；无新端侧（≤数 B）Planner official entry | ★★☆☆☆ | 已复核·无端侧净新增 |

要点：
- **🔑 头条 = 端侧 Planner 底座首次按地区切换第三方模型**：Apple 在 10-30 宣布、Alibaba 于 10-31 确认——iOS 27.3 在中国区以 **Qwen** 充当 Apple Intelligence 的底层模型（on-device，已由中国网信办 7 月完成 7 款端侧生成式 AI 服务备案，含 Apple Intelligence）。Siri / Writing Tools / Visual Intelligence 经同一 App Intents 接口连接 Qwen。这是「设备侧 Planner 模型」议题的里程碑：**同一意图接口背后，端侧 LLM 可按监管/地区替换**（dev.to：global AI products are splitting into national versions, with local models behind identical interfaces）。
- **中国区能力边界**：iPhone 15 Pro+ 启用 Writing Tools / Genmoji / Clean Up / Notification Summaries / Priority Notifications / Visual Intelligence / Live Translation（AirPods）；**新版 agentic Siri AI 与多数 WWDC26 Apple Intelligence 能力、Image Playground 本版不进中国**。→ 中国区意图执行总线先以「写作/视觉/摘要」类能力开通，agentic Siri 全量仍待补。
- **诚实标注**：iOS 27.3 是否新增公开 `@AppIntent(schema:)` Schema 在窗口报道中**未确认**（报道聚焦 Intelligence-China 模型层 + Health app 重建）；本笔记按「模型层/enablement 变更」定性，新 schema API 状态**待补**（beta 刚落，dev release notes 尚未完整解析）。
- **Android 成熟度维持 + 复述确认**：AppFunctions beta01（10-21）经 Jetpack Release Notes 复核仍最新；NeoTeo（11-03）与 Forkast（11-01）文章均**复述**既有双路由/权限边界结论（见下列 ②），未引入新 API/字段。

## ② 系统安全与用户体验（Confirmation / 隔离 / 防注入）

### 窗口内命中（边界澄清 / 复述，非新 OS API；按口径 ★5、追加既有 B 状态行）
- **Android AppFunctions 权限边界澄清（Forkast，11-01）**：Android 10-28 beta 公告将 **AppFunctions API 状态与正式生产发布分离**——beta 态**不等于开放/无限制 agent 访问**，生产发布是独立、受闸的下一步。属「Registry/权限模型」澄清，直接承接 [[四平台意图 Registry 来源轴与权限模型对比 2026]] 与 [[Android AppFunctions 设备侧意图 2026]] 既有论述（仍受 `EXECUTE_APP_FUNCTIONS` + `scope` + `@AppFunctionAccessLevel` 三向约束 + OAuth 2.1）。★5/10 —— 边界澄清、非新 API，已在既有 B 笔记追加状态行，不升新节点。
- **Google Connected Apps 双路由复述（NeoTeo，11-03）**：重述 10-28 Connected Apps Platform 的两条集成路径——**cloud-hosted MCP**（触达 Search / Gemini on web·Android·iOS）与 **Android MCP**（触达 Gemini on Android，设备本地）。与 10-29 已捕获的「Remote MCP = 推荐默认跨平台路径 / AppFunctions = client-side 本地路径」完全一致，无新字段。★5/10 —— 复述，已在 [[四平台意图 Registry 来源轴与权限模型对比 2026]] 追加状态行。
- **Apple iOS 27.3 中国区安全/合规含义**：Qwen 以端侧备案模型身份落地，意图执行底座受中国本地监管（备案制）约束；on-device vs model-routed 行为在网络差时分化（dev.to 提示开发者测失败模式）。属新市场的**执行安全/合规变量**，但非 Apple 新增的系统级 Confirmation/隔离机制。

### 去伪 / 丢弃（按口径）
- **Apple 本窗口发新 `@AppIntent(schema:)` Schema / iOS 27.3 新意图 Schema**：不成立——报道聚焦 Intelligence-China 模型层 + Health 重建，无新 schema API 信号。
- **Android 发 AppFunctions beta02 / alpha14**：不成立——官方仍 beta01（10-21）。
- **Windows 新 OS 执行总线 API / XPIA 新 OS 机制**：不成立——Windows agentic 安全书（learn.microsoft.com）最后更新 2025-11-18；Ignite 2026（11-17~20）尚未开幕，仅路线图预告。
- **HarmonyOS 新 Intents Kit / ArkAF API**：不成立——稳定文档，无窗口内变更。
- **BFCL 新端侧 Planner entry**：不成立——FunctionGemma 270M / qwen3-0.6b 仍不在榜。

> [!note] 概念节点双链
> [[意图模式规范]] [[语义路由]] [[端侧工具调用]] [[确认机制]] [[元服务]] [[隔离执行]] [[A2A 端侧智能体协议]] [[XPIA 跨提示注入]]
