---
date: 2026-10-29
tags: [AppIntent, 每日情报, AndroidDevSummit, ConnectedAppsPlatform, MLKitAgenticAPI, GeminiNano4, 端侧Planner, 跨应用Intent工作流, GitHubCopilotFusion, 本地模型路由, LFM3, 无新OS框架(除Android), 来源轴延续]
source: "https://thepromptinsider.com/news/google-connected-apps-platform ; https://news.qq.com/rain/a/20261029A03AZA00 ; https://pivotnews.ai/build/android-studio-opens-to-more-than-40-outside-coding-agents ; https://zendoric.com/en/dia/2026-10-29/12 ; https://github.blog/changelog/2026-10-28-github-copilot-fusion-now-supports-selection-of-local-models ; https://www.rlresearch.ai/benchmarks/bfcl-v4 ; https://xibilus.com/similar/304273 ; https://www.163.com/dy/article/LA9OJ6HD0511CQ7I.html ; WebSearch 直查官方/权威源（无 Horizon MCP，仅 agent-mail 在线）"
importance_score: "★★★☆☆"
intent_category: "系统级意图框架 / Android Dev Summit 2026 / Connected Apps Platform / ML Kit 端侧 Agentic API / 跨应用 Intent 工作流 / 来源轴延续"
---

# AppIntent 每日情报 2026-10-29

> [!abstract] 30 秒速览
> 本窗口（2026-10-28 21:00 → 10-29 21:00，24h）**唯一 OS 级真增量来自 Android Dev Summit（10-28 召开）两项官方公告**：① **Connected Apps Platform（预览，10-28）**——AppFunctions + Android MCP 经 Google Connected Console 注册后，可同时出现在 **Gemini app 与 Search AI Mode**，实现「enable once, run Google-wide」的**跨应用意图工作流发现面**（★7/10，四平台首个把设备侧意图框架直接挂到系统级 AI 入口 Search 的官方能力）；② **ML Kit Agentic API（alpha，Gemini Nano 4）**——OS 提供的**端侧函数调用 + 对话历史管理 + 执行流控**，是端侧 Planner 的一等原语（★6/10）。其余平台零净新增：Apple（27.2 已 10-26/27 GA，框架层 10-28 已复核零变更）、Android（AppFunctions 仍 `1.0.0-beta01`）、HarmonyOS（仅生态/教程复盘）、Windows（无新 OS 执行总线 API，但 GitHub Copilot Fusion 本地模型路由实验预览落地——编码 harness 实现，非 OS bus）、BFCL v4（无新端侧 Planner official entry，但 LFM3-1.7B 端侧模型 BFCL V4 71.39 新出）。**本运行 0 新建 B 节点、3 处 B 既有增补**（[[Android AppFunctions 设备侧意图 2026]] / [[Function Calling 端侧工具调用]] / [[四平台意图 Registry 来源轴与权限模型对比 2026]]），符合去重纪律；最高优先「来源轴四平台全空白」待办延续。

## ① Schema 定义与语义路由（本窗口）

| 平台 | 本窗口 Schema/路由层净新增 | 重要性 | 处置 |
|---|---|---|---|
| Apple | iOS 27.2 已 10-26/27 GA 且框架层零变更（10-28 已 WebFetch 直查 App Intents Updates 页确认仍 June 2026）；本窗口仅 27.2 消费者功能复述（Siri 记忆/Excluded Apps/Messages 建议），**无新 `@AppIntent(schema:)`** | ★★☆☆☆（无净新增） | 已复核·无净新增（10-28 已落档） |
| Android | **① Connected Apps Platform（预览，10-28 Dev Summit）**：AppFunctions + Android MCP 经 Connected Console 注册后，同时可达 **Gemini app + Search AI Mode**；**② ML Kit Agentic API（alpha，Gemini Nano 4）**：端侧函数调用 + 对话历史管理 + 执行流控 | ★★★★☆（Connected Apps ★7 + ML Kit Agentic ★6） | 已捕获·2 处真增量（B 增补） |
| HarmonyOS | 无新 OS 框架 API；CEIC 1024 深圳（10-24）生态复盘（8 万 API / 100+ Kit、70+ SDK Skills、DFX 8 类故障定位 Skill、Core Vision Kit 端侧） | — | 已复核·无净新增 |
| 跨平台 BFCL | 无新端侧 Planner official entry；**LFM3-1.7B（Liquid AI，1.7B，AMD Ryzen AI 定位）BFCL V4 71.39 新出**；BFCL v4 镜像快照 10-25（104 模型，rlresearch 镜像） | ★★☆☆☆（LFM3 端侧模型 ☆5） | 已捕获 LFM3 端侧模型（B 增补） |

要点：
- **🔑 Connected Apps Platform（★7/10，头号增量）= AppFunctions 第一次被挂到系统级 AI 入口 Search**：Google 在 Android Dev Summit（10-28）发布 Connected Apps Platform（预览，分阶段开放），开发者可经 **cloud-hosted MCP server 或 Android MCP（用 AppFunctions APIs）** 接入，在 **Google Connected Console** 注册并选择「出现在 Search / Gemini app / 两者」；一次接入、跨 Google 全家可用（"enable once, run Google-wide"）。官方称已上线 **50+ Connected Apps**（Adobe、Peloton、Experian、Calm 等），Search 侧先在 US 的 AI Mode（英文）开放。→ 这是四平台里**首个把设备侧意图框架（AppFunctions/Android MCP）直接接入「系统级搜索入口」的官方能力**——把「跨应用 Intent 工作流」从「Gemini app 内编排」扩到「Search 结果页即触发 agentic action」，是 [[Android AppFunctions 设备侧意图 2026]] 与 [[四平台意图 Registry 来源轴与权限模型对比 2026]] 的 discovery-surface 维度补强。⚠️ 仍为 preview + 分阶段开放（US 开发者 waitlist），非 GA；具体 API 名/是否独立 service/是否受 `EXECUTE_APP_FUNCTIONS` 同一闸门约束待 developer.android.com/ai/appfunctions 确认。
- **ML Kit Agentic API（alpha，Gemini Nano 4，★6/10）= OS 提供的端侧 Planner 原语**：Dev Summit 同步宣布 **ML Kit 新增基于 Gemini Nano 4 的 Agentic API（alpha）**，支持**函数调用（function calling）+ 对话历史管理（conversation history management）+ 执行流控（execution flow control）**，供开发者探索**设备端运行的智能体体验**。→ 这与本任务聚焦的「端侧 Planner / 设备侧 MCP」直接对齐：AppFunctions 负责**暴露 App 能力为设备端 MCP 工具**，ML Kit Agentic API 补上**设备端模型与运行时的 agentic 编排**一环，二者共同构成 Android 端侧意图执行总线的「工具层 + 模型层」。⚠️ alpha 阶段、Gemini Nano 4 后端，具体 SDK 形态与权限边界待官方文档。
- **成熟度维持**：AppFunctions 仍 `1.0.0-beta01`（10-21）最新、无 beta02/alpha14（Jetpack Release Notes 直查一致）；A2UI 仍 Alpha（10-28 已补录 alpha02）。Connected Apps Platform 与 ML Kit Agentic API 是 beta01 之上的**生态/能力扩展**，非 AppFunctions 自身版本进位。

## ② 系统安全与 UX（Confirmation / 隔离 / 反注入）

### 窗口内 OS 级执行安全/UX 真增量（★6–7/10，能力扩展 + 治理视角）
- **Connected Apps Platform 的「入口扩张」带来攻击面扩张（治理视角）**：当 AppFunctions 从「Gemini app 内调用」扩到「Search AI Mode 即触发 agentic action」，调用方/触发面从受控助手扩到更 ambient 的搜索入口；**现有 OS 权限模型仍兜底**——执行仍受 `EXECUTE_APP_FUNCTIONS` caller 闸门 + `scope` 可见性 + 函数侧 `@AppFunctionAccessLevel` 三向约束（[[Android AppFunctions 设备侧意图 2026]]），且用户授权经 **OAuth 2.1** 让 Gemini 代表用户行动（Google 文档明示）。→ 与「agent 执行边界 = OS 权限/访问边界」跨平台收敛一致；但「Search 即触发」比「助手内显式指令」更易产生非预期调用，需观察确认/隔离是否随入口扩张收紧（延续 Android「确认下放 App」路线风险）。
- **ML Kit Agentic API 端侧执行**：函数调用与执行流控运行在设备端（Gemini Nano 4），与本地优先原则一致；执行安全仍依赖 AppFunctions 权限模型（若经 AppFunctions 暴露）或应用自身约束。

### 窗口内状态更新（★5/10，已跟踪节点到点，非新 OS API）
- **GitHub Copilot Fusion 本地模型路由落地实验预览（10-28）= 关闭长期跟踪项「HydraFusion 10 月底实验性预览」**：GitHub 官方 changelog（2026-10-28）宣布 Copilot Fusion 在 Copilot CLI / Copilot app / VS Code 支持**智能本地模型路由（experimental preview）**——可选 MAI Code 1.1 Flash（经 Windows ML 托管下载，Windows 默认开）或 BYO 本地 OpenAI 兼容模型（Qwen3.8 Flash Next 等）。这是 10-07 MXC/HydraFusion 公告中「本地/云端路由实验性预览」承诺的到点交付。**⚠️ 范围标注**：该能力落在 **GitHub Copilot 编码 harness**（coding agent），**非 Windows OS 的 Copilot Actions / Agent Workspace / ODR 执行总线**；且官方明确「routing decisions 仍在云端、本地模型安全保护可能与云模型不同」——按本任务「聚焦四平台 OS 框架执行总线」口径，记为**编码 harness 实现的状态更新（★5）**，不计入 OS 执行总线净新增，但关闭了本库长期跟踪的「HydraFusion 10 月底实验预览」待办。

### 窗口内命中但低于收录阈值（不升净新增、不建 B 节点）
- **XPIA · MCP tool server 命令注入一波（CVE-2026-117558~573，10-27 发布）**：约 9 个 MCP tool server 存在「agent 可调用的工具参数被直接插值进 shell 命令、未 neutralizing」的 OS 命令注入，prompt-injected agent 可借此执行任意命令。→ 经核查为 **MCP 工具链/应用层漏洞（10-27 发布，落本窗口前 ~21h）**，非四平台 OS 框架执行总线，按本任务连续多轮纪律（10-05/10-06 丢弃 MCP 工具链 CVE）**丢弃**；其「agent 的双手（tool server）即靶面」威胁模型价值已落 [[XPIA 跨提示注入]] / [[隔离执行]] 既有论述。
- **Android Studio BYOA / ACP（10-28 Dev Summit）**：Android Studio 经 Agent Client Protocol（ACP）开放 40+ 第三方 coding agent（Claude Agent / Codex / Antigravity），属**开发工具链**智能化，非 OS 意图框架，丢弃。
- **HarmonyOS CEIC 1024 深圳（10-24）生态复盘**：8 万 API / 100+ Kit、70+ SDK Skills、DFX 8 类故障定位 Skill、Core Vision Kit 端侧——均**生态/开发者内容复盘，无新 OS API**（10-24 落本窗口外）；HMAF（HarmonyOS Model-Agent Framework，API 23）为 HarmonyOS 6 开发指南，旧。丢弃。
- **iOS 27.2 消费者功能复述（10-28~29）**：Siri 记忆/Excluded Apps/Messages 上下文建议等均为 10-26/27 GA 已发布内容复述，无新 `@AppIntent` Schema。

### 去伪 / 丢弃（按口径）
- **Apple 本窗口发新 `@AppIntent(schema:)` Schema**：不成立——iOS 27.2 已于 10-26/27 GA 且 10-28 运行已 WebFetch 直查 App Intents Updates 页确认仍 June 2026；本窗口仅消费者功能复述。
- **Android 发 AppFunctions beta02 / alpha14**：不成立——Jetpack Release Notes 直查确认 beta01（10-21）仍最新。
- **Windows 本窗口有新 OS 执行总线 API**：不成立——仅 GitHub Copilot Fusion 本地路由（编码 harness，非 OS bus）；Copilot Actions/Agent Workspace/ODR 无新 Registry API。
- **Apex-35B（Tsinghua，BFCL V4 84.0）**：35B 云级模型，非端侧 Planner，超出本任务「端侧」聚焦，丢弃。

> [!note] 概念节点双链
> [[意图模式规范]] [[语义路由]] [[端侧工具调用]] [[确认机制]] [[元服务]] [[隔离执行]] [[A2A 端侧智能体协议]] [[XPIA 跨提示注入]] [[MCP 与设备侧 MCP]] [[意图框架·跨体系索引 MOC]]

---

> [!warning] 诚实标注
> - Connected Apps Platform 与 ML Kit Agentic API 来自 **Android Dev Summit（2026-10-28 召开）**官方公告，经 The Prompt Insider（"Google announced it on October 28, 2026"）/ 腾讯新闻（2026-10-29）/ Pivot News / Zendoric 多方一致复述；两能力均处 preview/alpha，**非 GA**，具体 API 名与权限边界待 developer.android.com/ai/appfunctions 官方文档逐字段确认。
> - 该 Dev Summit 公告（10-28）处于本窗口起点（10-28 21:00）边缘；10-28 运行（窗口至 21:00）未记录此二项，故本运行作为近边界捕获落档，属诚实补捕而非重复计数。
> - GitHub Copilot Fusion 本地模型路由来自 GitHub 官方 changelog（2026-10-28）；明确为 Copilot coding harness 能力、routing 决策仍在云端，非 Windows OS 执行总线，按口径记为编码 harness 状态更新（★5）。
> - XPIA MCP tool server 一波（CVE-2026-117558~573）来自 eyeon.ai（2026-10-27 发布），为 MCP 工具链层漏洞、落本窗口前 ~21h，按本任务「非四平台 OS 框架执行总线」纪律丢弃。
> - LFM3-1.7B（Liquid AI）BFCL V4 71.39 来自 xibilus 聚合转述（LFM3 系列 benchmark 表），**确切官宣日期待补**；1.7B 端侧 agentic 模型、AMD Ryzen AI 定位，标待官方榜复核。
> - BFCL v4 镜像快照（rlresearch，Snapshot October 25, 2026，104 模型）无新端侧 Planner official entry；官方 Berkeley 榜仍停滞（2026-04-12）。
> - 本运行未使用 Horizon MCP（仅 agent-mail 在线），全部以 WebSearch + WebFetch 直查官方源 + 权威媒体完成逐平台核验；0 新建 B 节点、3 处 B 既有增补。

> [!note] 补遗（10-29 21:12 复核 · freshness 复核补强，非新窗口）
> 经 freshness 复核，Connected Apps Platform 另有**执行安全/确认机制**与**架构双路径**硬细节此前未捕获，已补入 [[Android AppFunctions 设备侧意图 2026]]「2026-10-29 补遗」段：① 平台级确认标记（Console 标记需确认操作 + 工具 read-only/action 声明）+ 可选绑定交互 UI（A2UI 方向）；② @/名称调用 + session 上下文保持；③ **Remote MCP = 推荐默认（跨 Android/iOS/Web），AppFunctions = 本地互补路径**（修正「AppFunctions 唯一路径」旧表述）；④ OAuth 2.1 + 平台政策（2026-09-28，禁第三方广告/数据最小化）。均待 developer.android.com 官方文档逐字段确认（WebFetch 直连本会话仍失败）。此补遗属同窗口（10-28 21:00→10-29 21:00）深度补全，不计入新一日跑。
