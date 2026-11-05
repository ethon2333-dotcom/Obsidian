---
date: 2026-10-06
tags:
  - AppIntent
  - 每日情报
  - 复核型运行
  - 无净新增
source:
  - https://developer-rno.apple.com/cn/news
  - https://appauxin.com/ios-27-1-release-date
  - https://tech-insider.org/ios-27-release-date-siri-ai-features-2026/
  - https://developer.android.com/ai/appfunctions
  - https://byteiota.com/android-dev-summit-2026-developer-guide/
  - https://dev.to/artemgarazha/android-18-is-turning-into-an-intelligence-system-im-not-sure-whether-to-be-excited-or-worried-28d0
  - https://juejin.cn/post/7663089074582634538
  - https://benchlm.ai/benchmarks/bfcl-v4
  - https://llm-stats.com/benchmarks/bfcl-v4
  - https://cyberworldops.eu/en/gitlab-fixes-ai-gateway-sandbox-escape-enabling-command-execution
  - https://conicplex.com/blog/gitlab-patches-a-critical-ai-gateway-flaw-that-let-attackers-run-commands-on-self-hosted-servers-cve-2026-90970
  - https://mallory.ai/stories/019ac22e-b299-7761-b9b6-e48ad12125d9
importance_score: "—（复核型运行·无净新增）"
intent_category: "四平台官方框架层 + 跨平台 BFCL + XPIA 复核（2026-10-05 → 10-06）"
---

# AppIntent 每日情报 2026-10-06（窗口 2026-10-05 07:33 → 10-06 07:33，约 24h）

> [!abstract] 30 秒速览
> **核心结论：四大 OS 官方框架层 + 跨平台 BFCL v4 + XPIA 研究线，本 24h 窗口（2026-10-05 → 10-06）均无净新增。** 与连续多轮「OS 框架不日更」结论连续一致。
> - Apple：iOS 27.1 beta 仍未确认在本窗口发布、无新 `@AppIntent(schema:)` Schema API（Apple Developer 9-16 仅称「本月底推出」；第三方预测公开版 10-19~23）。
> - Android：AppFunctions 仍守 `alpha12`（2026-09-23）无 `alpha13`；Gemini Nano v3 端侧 Function Calling 为 I/O '26 / Android 18 既有叙事延续，非本窗口新 API。
> - HarmonyOS：无新 OS API（HDC2026 / ArkAF 2.0 为既有内容复述）。
> - Windows：Copilot Actions / Agent Workspace / ODR / 连接器策略治理无新 Registry API；26H2 已 GA（09-29）。
> - 跨平台 BFCL v4：端侧 Planner 无新入榜；聚合榜快照仍为 10-02（benchlm）/ 持续镜像（llm-stats），数字与历次一致。
> - XPIA：窗口内命中 CVE-2026-90970（GitLab 自托管 AI Gateway 沙箱逃逸 RCE，CVSS 9.9，10-02 披露）经核查为 DevOps 网关工具链、**非四平台 OS 框架执行总线**，按筛选规则丢弃（同 10-05 丢弃 CVE-2026-104120 MCP 工具链、09-30 注 Plugin4Shell 应用层 RCE 的口径）。

## ① Schema 定义与语义路由机制

- 逐一核验四大平台官方源与权威媒体：Apple iOS 27.1、Android AppFunctions `alpha13`、HarmonyOS 新 API、Windows OS 执行总线新 Registry API 均**无本窗口新增**。语义路由 / 意图分发机制停留在既有基线（iOS 27 Schema Protocol / AppFunctions `alpha12` `scope` / ArkAF 2.0 / ODR + Agent Launchers）。
- Gemini Nano v3 端侧 Function Calling（经 `android.app.ai` AICore `LanguageModel.createLanguageModelSession()`）属 Android 18 设备端「轻量决策层 + 本地执行」叙事的延续，是 AppFunctions / Context Engine 的底层模型能力，**非本窗口新 API 发布**；仅在第三方中文开发者博客（稀土掘金）有解读文，标「SDK 早期开放阶段、以官方指南为准」。

## ② 系统安全与用户体验（Confirmation / 隔离 / 防注入）

- 四平台执行安全机制（Apple FDA 收紧 / Android `EXECUTE_APP_FUNCTIONS` 一次性授权 / HarmonyOS 端云协同安全认证 / Windows 低权账号 + ODR consent + Execution Containers）在本窗口**无新机制发布**。
- XPIA 窗口内仅 CVE-2026-90970 一个高显著度条目，但其攻击面落在 GitLab 自托管 AI Gateway（Duo Agent Platform 的 prompt template 沙箱，CWE-1336 服务端模板注入 → 逃逸 → RCE），**本质是 AI 编码 / 网关工具链的隔离层失守，与四平台 OS 意图执行总线无直接关系**。按本库一贯口径（MCP 工具链 CVE、应用层 RCE 均不计入 OS 框架）丢弃；其真正价值是「agent 隔离层已成为攻击靶面」这一趋势的再次印证，已在历史 B 笔记（[[隔离执行]] / [[XPIA 跨提示注入]]）的「隔离层即靶面」论述中涵盖，无需新建节点。

## 已复核·无净新增（避免重复检索）

- **Apple**：iOS 27.1 beta 未确认本窗口发布（Apple Developer 9-16「本月底推出」；appauxin 预测公开版 10-19~23；Macworld 10-05 仍未确认 beta 已发）；无新 App Intents Schema API。iOS 27 GA 的 App Intents Domains / Schema Protocol（Sauce Labs changelog 转述）为 GA 内容复述，非新。
- **Android**：AppFunctions 守 `1.0.0-alpha12`（09-23）无 `alpha13`；A2UI 守 `alpha01`；Gemini Nano v3 Function Calling 为既有叙事。Android Dev Summit 2026（10-28~29）仍为未来事件，Context Engine 公告集群为 10-05 已收录项复述。
- **HarmonyOS**：无新 OS API；小艺 / ArkAF 2.0 / HDC2026 为既有内容复述（tbreak / bridgingchina / pcd / clauday 均为 HDC2026 转述）。
- **Windows**：Copilot Actions / Agent Workspace / ODR / 连接器策略治理（`ConfigureAgentConnectors` 等）无新 Registry API；26H2 GA 09-29 已记录；Entra ID 登录 CSP 收紧（mallory.ai 记 10-01「10 月下旬生效」）属身份认证加固、非 OS agentic 意图框架，且为已收录 Entra / Copilot 安全叙事的延伸。
- **跨平台 BFCL v4**：端侧 Planner 无新入榜；benchlm 快照 10-02（BTL-3 88.5% 居首、22 行全为厂商自报）；llm-stats 聚合榜（Atria Dawn Preview 0.770 居首）为不同归一化口径，不与官方 Berkeley 榜直接可比；MiniCPM5-2B 66.60 / FunctionGemma 27.03 / qwen3-0.6b-tool-router 54.08 维持。Berkeley 官方 BFCL v4 博客原文仍待复核（连续多轮待办）。

## 诚实标注 / 待补

- iOS 27.1 beta 实际发布日与是否带新 `@AppIntent(schema:)` Schema（iPhone Duo 折叠屏适配之外）待 Apple 逐字确认；10-19~23 为第三方汇总。
- AppFunctions `alpha13` 是否存在、是否引入调用方身份注入新机制（`alpha12` 移除 `AppFunctionContext` 后）待 developer.android.com/ai/appfunctions 官方文档。
- Gemini Nano v3 Function Calling 的 `LanguageModel.createLanguageModelSession()` 具体方法签名 / 参数以官方 SDK 文档为准（第三方博客标「早期开放」）；是否接 AppFunctions / Context Engine 同一 `EXECUTE_APP_FUNCTIONS` 闸门待确认。
- CVE-2026-90970 已丢弃（非四平台 OS 框架）；若未来出现四平台 OS 层 agent 隔离逃逸（如 Copilot Agent Workspace 容器逃逸）再纳入。
- 沿用手柄：Per-Intent Privacy Manifest 官方逐字 / Watch OS 26 / AppFunctions GA 日期 / A2UI alpha02 / 高通 NPU exact specs / Berkeley 官方 BFCL v4 博客 / NowSecure / AgentAntibody / Chrome Origin Sets。

> [!note] 概念节点双链
> [[意图模式规范]] [[语义路由]] [[端侧工具调用]] [[确认机制]] [[元服务]] [[隔离执行]] [[A2A 端侧智能体协议]] [[XPIA 跨提示注入]]
