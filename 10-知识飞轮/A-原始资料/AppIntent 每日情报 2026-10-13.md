---
date: 2026-10-13
tags: [AppIntent, 每日情报, Android, AppFunctions, alpha13, 版本复核, 知识库纠错, 执行安全, 诚实标注]
source: "https://developer.android.com/jetpack/androidx/releases/appfunctions ; https://developer.android.com/jetpack/androidx/versions/alpha-channel ; https://developer.android.com/jetpack/androidx/versions/all-channel ; https://developer.apple.com/ios/whats-new ; https://developer.huawei.com/consumer/en/doc/HarmonyOS-Guides/arkaf-overview ; https://learn.microsoft.com/windows/security/book/operating-system-agentic-security ; https://gorilla.cs.berkeley.edu/leaderboard.html ; WebSearch 直查官方/权威源（无 Horizon MCP）"
importance_score: "★★★☆☆"
intent_category: "执行安全 / 系统级意图框架 / 版本复核 / 知识库纠错"
---

# AppIntent 每日情报 2026-10-13

> [!abstract] 30 秒速览
> 本窗口（2026-10-10 21:00 → 10-13 12:37，约 2.6 日）**四平台均无 OS 框架层净新增 API**，延续「OS 框架不日更」纪律。本运行的核心价值不在新 API，而在**对官方源二次直查，确认 AppFunctions `1.0.0-alpha13`（2026-10-07 发布）确为真实发布**——即 **10-09 跑正确、10-10 跑的「alpha13 系误记」更正系误判**（其当时官方索引快照滞后），已回退 10-10 更正并重新确认 alpha13 的 `@AppFunctionAccessLevel` 函数侧访问限制 + `@AppFunction`→`@AppFunctionDeclaration` 重命名 + `AppFunctionMetadata` 暴露。其余：Apple（iOS 27.2 beta 3 = 24B5099f 无新 `@AppIntent(schema:)` Schema、iOS 27.1 仍未发）、HarmonyOS（Intents Kit / ArkAF 文档稳定）、Windows（无新 agentic security API）、BFCL v4（榜单快照前移、top 已变前沿云模型，端侧 Planner 无新 official entry）、XPIA（无新 OS 执行总线 CVE）均零净新增。

## ① Schema 定义与语义路由（本窗口）

| 平台 | 本窗口 Schema/路由层净新增 | 重要性 | 处置 |
|---|---|---|---|
| Android | 无新版本进位（官方最新仍为 **`1.0.0-alpha13`（2026-10-07）**，无 alpha14）；**10-13 复核确认 alpha13 真实有效**，`@AppFunctionAccessLevel` + 重命名 + `AppFunctionMetadata` 暴露均为真 | ★★★☆☆（复核确认，非本窗口新发） | **已复核·alpha13 经官方三处列表确认真实**（推翻 10-10 误更正） |
| Apple | 无（iOS 27.2 beta 3 = build 24B5099f 无新 `@AppIntent(schema:)` Schema；iOS 27.1 仍未发、预期 10-19~23 随 Duo；What's New in iOS 27 = WWDC26 既有框架） | — | 已复核·无净新增 |
| HarmonyOS | 无（Intents Kit 配置式开发 / ArkAF 概览 / 端侧 A2A 文档稳定；A2A 协议 API 末次更新 2026-09-04、Intents Kit 页 2026-09-14，无窗口内新意图框架 API） | — | 已复核·无净新增 |
| 跨平台 BFCL | 无新端侧 Planner official entry；**榜单快照前移**：Berkeley BFCL v4 在线榜 top 已变为 Claude-Opus-4-5（77.47）/ Claude-Sonnet-4-5（73.24）/ Gemini-3-Pro（72.51）/ GLM-4.6（72.51）等前沿云模型，库内此前引用的「Qwen3.7 Max 75.0%」「Llama 3.1 405B 88.5%」top 快照**已过时** | — | 已复核·无新端侧 Planner；榜单快照标注待更新 |

要点：
- **alpha13 复核确认（本窗口核心）**：2026-10-13 对 `developer.android.com/jetpack/androidx/releases/appfunctions`（发布页）+ alpha-channel + all-channel 三处官方列表直查，**均明确列出 `1.0.0-alpha13`（2026-10-07 发布）**，API 变更逐字为：① Added `@AppFunctionAccessLevel` annotation, supporting access restriction setting (Id47e1)；② Renamed `AppFunction` annotation to `AppFunctionDeclaration` (I4b15d)；③ Renamed `ObserveAppFunctionsEvent` to `AppFunctionsChangeEvent` (Iec918)；④ Surface `AppFunctionMetadata` in `AppFunctionService` (If1117)；⑤ Bug fix：`AppFunctionData` 支持全部内建 proxy 类型（LocalDate/LocalTime/Instant/ZoneId）。**10-09 跑对、10-10 跑错**（10-10 当时官方索引快照滞后，误判「最新仍 alpha12」）。
- Apple / HarmonyOS / BFCL（端侧 Planner）：均无路由 / 评测层净新增，延续「OS 框架不日更」。
- **BFCL 榜单快照前移（诚实标注）**：库内多轮引用的「Qwen3.7 Max 75.0% 居首」「Llama 3.1 405B 88.5%」是早期快照，2026-10-13 实时榜 top 已被 Claude Opus 4.5 / Sonnet 4.5 / Gemini 3 Pro 代际模型占据；端侧小模型（FunctionGemma 270M / Qwen3-0.6B-tool-router / MiniCPM5-2B / LittleLamb 0.3B）未进入可见 top 段，仍为已知 model card，无新 official entry。

## ② 系统安全与 UX（Confirmation / 隔离 / 反注入）

### 🔑 本窗口核心处置：回退 10-10 误更正，重新确认 alpha13 的权限模型价值
- **复核动作**：2026-10-13 直查官方 Jetpack Release Notes 发布页 + alpha-channel + all-channel 三处列表。
- **结论**：`1.0.0-alpha13`（2026-10-07）真实发布，含首個函数侧访问限制原语 `@AppFunctionAccessLevel`。AppFunctions 权限模型三向约束成立：**① 调用方持 `EXECUTE_APP_FUNCTIONS`（caller 权限）；② 函数可见性 `scope`（alpha12）；③ 函数侧 `@AppFunctionAccessLevel`（alpha13）**——「谁能调 / 谁能看见 / 函数自身允许谁访问」。
- **影响范围（已回退 10-10 更正）**：① [[AppIntent 每日情报 2026-10-09]] 顶部「⚠️ 更正」横幅改为「✅ 10-13 复核确认」；② [[AppIntent 每日情报 2026-10-10]] 顶部加「10-13 复核推翻」警示；③ [[Android AppFunctions 设备侧意图 2026]] 10-09 增补段标题去除误「⚠️ 更正」前缀、文末新增 10-13 复核段推翻 10-10 更正；④ [[四平台意图 Registry 来源轴与权限模型对比 2026]] 10-09 增补段标题去误前缀、10-10 更正 callout 改为「✅ 复核确认」。
- **待确认项（仍有效）**：`@AppFunctionAccessLevel` 具体级别语义（public/protected/same-app/system 等）官方 Release Notes 仍未展开，待 `developer.android.com/ai/appfunctions` 官方文档逐字段确认（延续 09-25 `scope` 纪律，不猜测级别）。该原语属访问/权限维度，与「意图来源 provenance 轴」正交，来源轴四平台全空白结论不变。

### 窗口内无新安全机制（按口径复核）
- **Apple**：iOS 27.2 beta 3 多渠道仍为功能/本地化扩展（如 Gemini-Siri 扩语言），论坛仅见一条 App Shortcut phrase 调用失败的 bug 报告（非新 Schema API），无新 Confirmation UI / entitlement 机制。
- **HarmonyOS**：所有命中均为稳定框架文档（arkaf-overview、insight-intent 配置式开发、agent-overview 端侧 A2A、A2A 协议 API），无新隔离 / A2A 安全 API。
- **Windows**：agentic security 文档（learn.microsoft.com 四大构建模块：用户控制 / 代理账户 / Agent Workspace / 用户透明度）与 2026-10-07 MXC GA 事件稳定，本窗口无新 surface / 机制；HydraFusion 本地模型路由仍为「10 月底实验性预览」（非 GA）。
- **XPIA**：无窗口内新 OS 执行总线 CVE。命中的 AWS/Google/Vercel agent 基础设施「工具可在不经模型轮次下被触发」（AgentCore InvokeHarness / Google ADK / Vercel AI SDK harness）属**云/工具链 agent 基础设施**，非四平台 OS 框架执行总线，按口径丢弃（同 10-06 丢弃 MCP 工具链 CVE、10-09 丢弃 M365/OpenClaw/PraisonAI）；GitLab CVE-2026-90970（10-02 披露）已在 10-09 收为丢弃项。

### 去伪 / 丢弃（按口径）
- **BFCL v4 榜单前移**：非「新端侧 Planner 入榜」，仅榜单快照随时间推进、top 被代际云模型刷新；库内旧 top 快照标注待更新，不升净新增。
- **XPIA 框架层**：AWS/Google/Vercel agent infra 三处工具触发缺陷、TeamCity CVE-2026-63077、Paperclip CVE-2026-41679 等均为云/应用/工具链层，无窗口内新 OS 执行总线 CVE。

> [!note] 概念节点双链
> [[意图模式规范]] [[语义路由]] [[端侧工具调用]] [[确认机制]] [[元服务]] [[隔离执行]] [[A2A 端侧智能体协议]] [[XPIA 跨提示注入]]

---

> [!warning] 诚实标注
> - alpha13 真实性基于 2026-10-13 对官方 Jetpack Release Notes 发布页 + alpha-channel + all-channel 三处官方列表的 WebSearch 直查交叉确认；`@AppFunctionAccessLevel` 级别语义官方仍未展开，标待确认。
> - 10-10 跑的「alpha13 系误记」结论已明确判定为**索引滞后误判**，本运行已回退其更正；后续每日跑对 Android 侧应以「官方最新 = alpha13（10-07）」为基线检索 alpha14+。
> - BFCL v4 在线榜 top 已变前沿云模型，库内旧「Qwen3.7 Max / Llama 3.1 405B」top 快照过时；端侧小模型无新 official entry。
> - 本运行未使用 Horizon MCP（仅 agent-mail 在线），全部以 WebSearch 直查官方源完成逐平台核验。
