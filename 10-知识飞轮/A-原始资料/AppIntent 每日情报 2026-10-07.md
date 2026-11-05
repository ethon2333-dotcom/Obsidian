---
date: 2026-10-07
tags:
  - AppIntent
  - 每日情报
  - 复核型运行
  - 无净新增
source:
  - https://developer.apple.com/news/?id=rfb1rooi
  - https://theapplewiki.com/wiki/Beta_Firmware/iPhone/27.x
  - https://betawiki.net/index.php?title=IOS_27
  - https://developer.android.google.cn/jetpack/androidx/releases/media2
  - https://byteiota.com/android-dev-summit-2026-developer-guide/
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/intents-introduction
  - https://learn.microsoft.com/fil-ph/windows/security/book/operating-system-agentic-security
  - https://www.todaymg.com/a/windows-11-dai-li-shi-aigong-neng-kong-cheng-e-yi-ruan-ti-lou-dong-wei-ruan-ji-fa-jing-gao.html
  - https://benchlm.ai/benchmarks/bfclV4
  - https://threatcluster.io/cluster/critical-vulnerability-in-progress-datadirect-arcgenai-agent-5b73c4bf
  - https://www.f5.com/labs/articles/weekly-threat-bulletin-october-7th-2026
  - https://deniz.in/gitlab-ai-gateway-cve-prompts-fresh-audits-of-ai-agent-permission-enforcement
  - https://cyberrecaps.com/news/cybersecurity-news-october-06-2026
importance_score: "—（复核型运行·无净新增）"
intent_category: "四平台官方框架层 + 跨平台 BFCL + XPIA 复核（2026-10-06 → 10-07）"
---

# AppIntent 每日情报 2026-10-07（窗口 2026-10-06 21:00 → 10-07 21:00，约 24h）

> [!abstract] 30 秒速览
> **核心结论：四大 OS 官方框架层 + 跨平台 BFCL v4 + XPIA 研究线，本 24h 窗口（2026-10-06 21:00 → 10-07 21:00）均无净新增。** 与连续多轮（含 10-05 / 10-06 / 10-06-晚）「OS 框架不日更」结论完全连续一致。
> - Apple：iOS 27.1 beta **仍未发布**（Apple Developer 10-07 公告明确「later this month」即 10 月内稍晚；iPhone Duo 10-23 才上市）；iOS 27.2 beta 3（24B5099f，10-05）为最新 dev beta，无新 `@AppIntent(schema:)` Schema。
> - Android：AppFunctions 仍守 `alpha12`（2026-09-23，前轮直查 Release Notes 确认）无 `alpha13`；Android Dev Summit 2026（10-28~29）为未来事件、Context Engine 公告为 10-05 已收录项复述。
> - HarmonyOS：无新 OS API（Intents Kit 官方页仍为 2026-04-29，HDC2026 / ArkAF 2.0 为既有内容复述）。
> - Windows：Copilot Actions / Agent Workspace / ODR / 连接器策略无新 Registry API；今日台湾媒体「微软急发警告」文章经核查为 learn.microsoft.com agentic security 文档的**中文复述**，无新 API。
> - 跨平台 BFCL v4：端侧 Planner 无新入榜；聚合榜快照仍为 10-01（benchlm），BTL-3 88.5% 现确认为 **Bad Theory Labs 开放权重**（此前库内「疑 Llama 3.1 405B」的歧义已澄清）；MiniCPM5-2B 66.60 / FunctionGemma 27.03 / qwen3-0.6b-tool-router 54.08 维持。
> - XPIA：窗口内命中 CVE-2026-91140（Progress DataDirect，CVSS 9.6，10-06 披露）/ CVE-2026-103956 等（AWS Loom + SageMaker，10-07）/ CVE-2026-90970（GitLab，dev.to 10-06 重提）/ Meta Muse VM escape（Meta，10-06）——**全部经核查为非四平台 OS 框架执行总线（应用/工具链/云厂商产品）或已覆盖项，按筛选规则丢弃**，同 10-06 丢弃 GitLab AI Gateway、10-05 丢弃 MCP 工具链 CVE 的口径。

## ① Schema 定义与语义路由机制

- 逐一核验四大平台官方源与权威媒体：Apple iOS 27.1、Android AppFunctions `alpha13`、HarmonyOS 新 API、Windows OS 执行总线新 Registry API 均**无本窗口新增**。语义路由 / 意图分发机制停留在既有基线（iOS 27 Schema Protocol / AppFunctions `alpha12` `scope` / ArkAF 2.0 / ODR + Agent Launchers）。
- Apple：Apple Developer 10-07 公告（id=rfb1rooi）确认 iOS 27.2 / iPadOS 27.2 / macOS 27.2 / tvOS 27.2 / visionOS 27.2 beta 已可下载，并说明「iPhone Duo 10-23 上市时将运行 iOS 27.1，Xcode 27.1 稍后本月提供 beta」——即 **iOS 27.1 beta 尚未发布**，无任何 `@AppIntent(schema:)` 新增。TheAppleWiki / BetaWiki 显示最新 dev beta 为 iOS 27.2 beta 3（24B5099f，10-05），iOS 27.1 仅以「24A94401 iPhone Duo Xcode simulator」形式存在（非真机 beta）。
- Android：developer.android.google.cn AndroidX 聚合发布页（media2 镜像）列出的 `appfunctions` 最新行为 `1.0.0-alpha11`（2026-08-26）；该聚合页未按 alpha-channel 刷新，与 09-25 跑直查 Release Notes 的 `alpha12`（09-23）存在**页面级不一致**——本窗口无新 release，维持 alpha12 为最新已确认版本的结论，待 developer.android.com/ai/appfunctions 逐字复核。Android Dev Summit 2026（10-28~29）byteiota 前瞻文提及 AppFunctions「在 Android 18 进入生产就绪信号」「Android Context Engine 作为第三类调用方」——均为 10-05 已收录项的二次传播，非本窗口新 API。
- HarmonyOS：Intents Kit 官方指南（intents-introduction）更新时间仍为 2026-04-29，全页稳定；HDC2026 / ArkAF 2.0 / 小艺 2.0 等均为既有内容复述，无框架 API 增量。

## ② 系统安全与用户体验（Confirmation / 隔离 / 防注入）

- 四平台执行安全机制（Apple FDA 收紧 / Android `EXECUTE_APP_FUNCTIONS` 一次性授权 / HarmonyOS 端云协同安全认证 / Windows 低权账号 + ODR consent + Execution Containers）在本窗口**无新机制发布**。
- XPIA 窗口内 4 组高显著度命中，**无一落在四平台 OS 执行总线**：
  - **CVE-2026-91140**（Progress Software DataDirect ARCGenAI Agents，CVSS 9.6，10-06 披露）：经 OpenAPI/Swagger 文档中 shell 元字符触发任意 OS 命令执行。**攻击面是 Progress 的 AI 网关产品，非四平台 OS 意图执行总线**，按本库一贯口径（MCP 工具链 CVE、应用层 RCE 不计入 OS 框架）丢弃；其价值是「agent 把配置规范当可信输入」趋势的再次印证，已涵盖于 [[隔离执行]] / [[XPIA 跨提示注入]] 既有论述。
  - **CVE-2026-103956 / 103957 / 103958 / 104019**（AWS Loom AI agent orchestration + SageMaker，F5 10-07 周报）：认证绕过 / OAuth SSRF / 命令注入，属 **AWS 开源 agent 编排平台**，非四平台 OS 框架，丢弃。
  - **CVE-2026-90970**（GitLab AI Gateway，CVSS 9.9，dev.to 10-06 长文重提）：与 10-06 跑已丢弃项为**同一 CVE**（dev.to 文给出「权限执行必须落在执行层而非编排层、retry 路径绕过鉴权」的架构教训）——非新事实，按「已覆盖·不重复计数」处理，仅作架构教训复述标注。
  - **Meta Muse VM escape**（cyberrecaps 10-06 引 404 Media）：Meta Muse（内部名 Hatch）发布前 KVM 逃逸，使普通用户突破 per-user VM 抵达内部生产库。属**产品级 agent VM 隔离逃逸**（概念上贴近 [[Agent Workspace 隔离执行]] / [[隔离执行]] 的「VM 作为 agent 隔离边界」），但 Muse 非四平台 OS，按本库「仅纳入四平台 OS 层 agent 隔离逃逸」纪律**丢弃**；若未来 Windows Agent Workspace 容器 / Android 隔离机制出现同类逃逸再纳入。

## 已复核·无净新增（避免重复检索）

- **Apple**：iOS 27.1 beta 确认未发布（Apple Developer 10-07「later this month」；iPhone Duo 10-23 上市）；iOS 27.2 beta 3（24B5099f，10-05）为最新 dev beta，无新 App Intents Schema。
- **Android**：AppFunctions 守 `1.0.0-alpha12`（09-23）无 `alpha13`；A2UI 守 `alpha01`；Android Dev Summit 2026（10-28~29）仍为未来事件，Context Engine / Android 18 Intelligence System 为 10-05 已收录项复述。
- **HarmonyOS**：无新 OS API；Intents Kit 官方页稳定（04-29）；HDC2026 / ArkAF 2.0 / 小艺 2.0 为既有内容复述。
- **Windows**：Copilot Actions / Agent Workspace / ODR / 连接器策略治理（`ConfigureAgentConnectors` 等）无新 Registry API；26H2 已 GA（09-29）；今日台湾媒体「微软急发警告」文 = learn.microsoft.com agentic security 文档中文复述（Agentic Workspace / 低权账号 / XPIA 警告 / 四大原则 / Copilot 首发），无新 API。
- **跨平台 BFCL v4**：端侧 Planner 无新入榜；benchlm 快照 10-01（BTL-3 88.5% 居首、22 行全为厂商自报、0 来自榜主）；**BTL-3 现确认为 Bad Theory Labs 开放权重**（此前库内「疑 Llama 3.1 405B 88.5%」歧义已澄清）。MiniCPM5-2B 66.60 / FunctionGemma 27.03 / qwen3-0.6b-tool-router 54.08 维持。Berkeley 官方 BFCL v4 博客原文仍待复核（连续多轮待办）。

## 诚实标注 / 待补

- iOS 27.1 beta 实际发布日（「later this month」= 10 月内稍晚）与是否带新 `@AppIntent(schema:)` Schema（iPhone Duo 折叠屏适配之外）待 Apple 逐字确认。
- **AndroidX 聚合发布页（media2 镜像）列 appfunctions 仍为 `alpha11`（08-26），与 09-25 跑直查 Release Notes 的 `alpha12`（09-23）页面级不一致**——疑似聚合页未按 alpha-channel 刷新；维持 alpha12 为最新已确认版本，待 developer.android.com/ai/appfunctions 官方文档 + alpha-channel 逐字复核闭合该不一致。
- AppFunctions `alpha13` 是否存在、是否引入调用方身份注入新机制（`alpha12` 移除 `AppFunctionContext` 后）待官方文档。
- CVE-2026-91140 / AWS Loom / Meta Muse 均丢弃（非四平台 OS 框架）；CVE-2026-90970 为已覆盖项复述；若未来出现四平台 OS 层 agent 隔离逃逸（如 Copilot Agent Workspace 容器逃逸）再纳入。
- 沿用：Berkeley 官方 BFCL v4 博客原文 / Per-Intent Privacy Manifest 官方逐字 / Watch OS 26 / AppFunctions GA / A2UI alpha02 / 高通 NPU exact specs / NowSecure / AgentAntibody / Chrome Origin Sets。

> [!note] 概念节点双链
> [[意图模式规范]] [[语义路由]] [[端侧工具调用]] [[确认机制]] [[元服务]] [[隔离执行]] [[A2A 端侧智能体协议]] [[XPIA 跨提示注入]]
