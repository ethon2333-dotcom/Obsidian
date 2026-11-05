---
date: 2026-10-28
tags: [AppIntent, 每日情报, iOS27.2, 正式版, 无新Schema, ExcludedApps, 意图访问治理, 160CVE, AppleIntelligence漏洞, Windows, Surface事件, HydraFusion, 无净新增, 复核型]
source: "https://developer.apple.com/news/releases?id=06102024i ; https://www.163.com/dy/article/LA8MH22I05119MAU.html ; https://www.toutiao.com/article/7701049235550028323 ; https://developer.apple.com/documentation/updates/appintents ; https://developer.android.com/jetpack/androidx/releases/appfunctions ; https://www.heise.de/en/news/Microsoft-unveils-agentic-Windows-desktop-and-new-hardware-11479975.html ; https://benchlm.ai/benchmarks/bfcl-v4 ; https://www.llmboard.ai/benchmarks/bfcl-v4-68 ; WebSearch 直查官方/权威源（无 Horizon MCP，仅 agent-mail 在线）"
importance_score: "★★★☆☆"
intent_category: "系统级意图框架 / iOS 27.2 GA / 版本复核 / 意图访问治理 / 来源轴延续 / 无净新增"
---

# AppIntent 每日情报 2026-10-28

> [!abstract] 30 秒速览
> 本窗口（2026-10-26 22:53 → 10-28 19:03，约 44h，衔接上轮 10-26 收尾）**四平台官方框架层仍零净新增 API**，与连续多轮「OS 框架不日更」结论完全连续。**唯一 OS 级治理细化（★6/10）= iOS 27.2 正式版（10-26/27，24B119；Duo 24B91020）新增「排除的 App」（Excluded Apps）统一隐私设置**——用户可统一选择哪些 App **不能被 Siri、搜索（Search）和建议（Suggestions）访问**，是 Apple 侧首个**系统级「意图访问排除清单」消费者层落地**，强化「agent 执行边界 = OS 权限/访问边界」跨平台收敛。**iOS 27.2 框架层零变更**：本运行直查 App Intents Updates 官方页（developer.apple.com/documentation/updates/appintents）确认最新仍 **June 2026（无 Oct 2026 条目）**，27.2 未引入任何新 `@AppIntent(schema:)` Schema/Entity/枚举（与 10-26 已记 RC 无新 Schema 一致，正式版延续）。**重大 OS 安全事件（XPIA 相邻，低于新节点阈值）= iOS 27.2 修复 160+ 漏洞（163 CVE），含一个 Apple Intelligence 远程数据访问漏洞**。Windows 侧「10-26 已跟踪的 late-October 节点」落地：10-28 Surface 活动确认 **HydraFusion 本地/云端路由实验性预览到点** + MXC GA 再确认，**无新 OS 执行总线 API**。Android（beta01 仍最新、无 beta02）/ HarmonyOS（仅教程）/ BFCL 端侧 Planner（无新 official entry）/ XPIA（无新 OS 框架 CVE）均无净新增。**本运行 0 新建 B 节点、3 处 B 既有增补**（[[Apple AppIntents Schema Protocol 2026]] / [[四平台意图 Registry 来源轴与权限模型对比 2026]] / [[Windows Copilot Actions 与 Agent Workspace 2026]]），符合去重纪律；最高优先「来源轴四平台全空白」待办延续。

## ① Schema 定义与语义路由（本窗口）

| 平台 | 本窗口 Schema/路由层净新增 | 重要性 | 处置 |
|---|---|---|---|
| Apple | **iOS 27.2 正式版（10-26/27，24B119；Duo 24B91020）发布**，但 App Intents Schema Protocol **框架层零变更**（App Intents Updates 官方页直查仍 June 2026，无 Oct 条目）；唯一治理细化 = **「排除的 App」统一意图访问排除设置**（消费者层） | ★★★☆☆（GA 发布 + 消费者层意图访问治理细化，非新 Schema API） | 已复核·无新 Schema；捕获 Excluded Apps 治理细化（B 增补） |
| Android | **AppFunctions 仍 `1.0.0-beta01`（2026-10-21）为最新**，无 beta02、无 alpha14；Jetpack Release Notes 直查确认 | ★★☆☆☆（无净新增） | 已复核·无净新增 |
| HarmonyOS | 无新 OS 框架 API；CSDN「ArkUI 进阶/提高练中学」第14/18 课为教程（意图框架/Skill/端侧 A2A 概念复述）；DigitalMate 第三方 agent 应用跑在 HarmonyOS 上（A2UI 声明式渲染） | — | 已复核·无净新增 |
| 跨平台 BFCL | 无新端侧 Planner official entry；镜像榜（benchlm.ai 10-17 / llmboard.ai 10-23）稳定，端侧 LFM2.5-230M 21% / MiniCPM5-2B 66.6% 维持；官方 Berkeley 榜仍停滞（2026-04-12） | — | 已复核·无新端侧 Planner |

要点：
- **iOS 27.2 正式版 = 框架稳定、治理与安全的 GA 大版本（★6/10 唯一真·增量在治理细化）**：Apple 于 2026-10-26/27 推送 iOS 27.2（24B119，Duo 专属 24B91020），距上次正式版 28 天。消费者功能 = Siri AI 记忆此前对话 + 更广个人上下文（信息照片附件/日历参与者/语音留言/Safari 历史）+ 5 种新语言（法/日/韩/葡/西，EU 与中国大陆不可用）+ Messages/Photos/FaceTime 建议动作 + SynthID 水印识别 + Apple Music/Podcasts/Apple TV  redesign。但 **App Intents 框架层零变更**——本运行 WebFetch 直查 `developer.apple.com/documentation/updates/appintents` 确认最新条目仍 **June 2026**（SyncableEntity / OwnershipProvidingEntity / LongRunningIntent 等已录项），**27.2 未在 App Intents 框架层带来任何新 Schema/Entity/枚举**（详见 [[Apple AppIntents Schema Protocol 2026]]）。
- **🔑 「排除的 App」统一意图访问排除设置（★6/10，唯一 OS 级治理细化）**：iOS 27.2 新增**统一隐私设置**，用户可集中选择**哪些 App 不能被 Siri、搜索（Search）和建议（Suggestions）访问**。这是 Apple 侧一个**系统级「意图访问排除清单」**——把「系统 agent（Siri/Search/Suggestions）可调用哪些 App 的能力与数据」的控制权以**消费者隐私开关**形态落地，与 Android `setAppFunctionsPolicy` / `APP_FUNCTIONS_DISABLED`（企业 MDM 层，[[Android AppFunctions 设备侧意图 2026]]）同源，但落在**消费者隐私层**。→ 强化本库长期跟踪的「agent 执行边界 = OS 权限/访问边界」跨平台收敛（详见 [[四平台意图 Registry 来源轴与权限模型对比 2026]]）。⚠️ 属用户隐私开关、非开发者框架 API，不构成 Schema Protocol 新 API；但它是 Apple 在 27.x 周期内对「意图访问治理」最明确的一次消费者层补强，值得落 B。
- **Duo 专属（24B91020）/ 国行专属**：Duo 版新增 Apple Pencil 支持 + 边缘光效（弱光视频通话）；**国行**新增「限制运动数据」遏制「摇一摇」广告跳转（隐私控制，仅中国区账号可见）——均非 App Intents 框架。
- **Android / HarmonyOS / BFCL（端侧 Planner）**：均无路由/评测层净新增，延续「OS 框架不日更」。HarmonyOS 命中为 CSDN 教程（ArkAF 意图框架/Skill/端侧 A2A 概念复述）与第三方 DigitalMate agent（基于 A2UI 声明式渲染），无新 OS API。

## ② 系统安全与 UX（Confirmation / 隔离 / 反注入）

### 窗口内唯一 OS 级执行安全/UX 治理细化（★6/10，消费者层权限/访问边界）
- **Apple iOS 27.2「排除的 App」统一意图访问排除设置**：用户可统一控制哪些 App 不被 Siri/Search/Suggestions 访问——把「系统 agent 对 App 能力与数据的访问」以**消费者隐私开关**形态纳入 OS 治理，是 Apple 侧对「意图访问边界」最明确的消费者层补强。与 Windows Agent Workspace 独立账号 + ODR 三档 consent（[[Confirmation UI 安全机制]] / [[Agent Workspace 隔离执行]]）、Android `setAppFunctionsPolicy` 企业层关闭 AppFunctions 数据（[[Android AppFunctions 设备侧意图 2026]]）构成「agent 执行边界 = OS 权限/访问边界」跨平台收敛的**消费者层拼图**。

### 窗口内重大 OS 安全事件（XPIA 相邻，低于新节点阈值）
- **iOS 27.2 修复 160+ 漏洞（163 CVE，★5/10·安全事件非框架）**：含一个 **Apple Intelligence 漏洞（远程攻击者可能访问敏感数据）** 与「隐藏邮件地址（Hide My Email）」真实邮箱泄露缺陷；30+ WebKit、约 15 个内核漏洞。Apple Intelligence **远程数据访问类漏洞**属 **agentic 数据安全相邻面**（agent/OS 智能层把敏感数据暴露给非预期远程方），与 [[XPIA 跨提示注入]] 及 [[Agent Data Injection 数据注入攻击]] 主题相邻，但为 **CVE 修复而非新框架机制**，低于新节点阈值，仅作关联观察（延续 0 新建 B 节点纪律）。

### 窗口内命中但低于收录阈值（不升净新增、不建 B 节点）
- **Windows 10-28 Surface 活动（★5/10，状态更新·非新 OS API）**：heise.de / blockbeats / nerova / bigchange / anywherexchange 报道微软「Windows and Surface October 2026 News」活动——混合智能/agentic Windows 愿景的**硬件+软件正式亮相（RTX Spark PCs 等）**。本窗口无新 OS 执行总线 API，但两个已跟踪节点**落地状态更新**：① **HydraFusion 本地/云端路由实验性预览到点**（10-07 称「later in October」，本次活动确认 by end of October 在 GitHub Copilot app/CLI/VS Code 落地——本地模型 MAI Code 1.1 Flash 3-bit/53GB/256K、NVIDIA Nemotron 2-bit/20GB、DeepSeek V4 Flash 1.6-bit/60GB 与云端自动路由）；② **MXC GA 再确认 + 身份集成「即将到来」**（agents 以独立用户身份+独立访问限制运行，Entra 身份归因「to follow shortly」）。均属 10-07 已捕获事件的硬件+落地延伸，**非新 API**。
- **Windows XPIA 警告重述（低于阈值·已知重述）**：rottenwifi / sekin / ctmanga / aitechmodel 均为「Securing AI agents on Windows」+ Experimental Agentic Features 支持页的重述（XPIA 风险、off-by-default、per-agent 文件夹控制、agent 独立账号、需 26H1 build 28000.3079+ 进程隔离强制执行层、agent 标识符为 preview），无新 OS-framework 机制，不升新节点。
- **BFCL / 端侧 Planner 社区分析（低于阈值）**：cheesecat 对 LFM2.5-24B-A2B（24B MoE，BFCLv4 65.01）的边界部署深读——属 24B 级边缘模型社区分析，**非官方端侧 Planner（0.3~2B 类）新 entry**，且非 0.x B 级小模型，低于本任务聚焦的「端侧 Planner 实测」阈值，仅作关联观察。

### 去伪 / 丢弃（按口径）
- **iOS 27.2 带新 `@AppIntent(schema:)` Schema**：经核验不成立——App Intents Updates 官方页（本运行 WebFetch 直查）最新仍 June 2026，无 Oct 条目；iOS 27.2 消费者功能清单无新意图 Schema 域（见 ①）。
- **Android 发 beta02 / alpha14**：不成立——Jetpack Release Notes 直查确认 beta01（10-21）仍为最新。
- **Windows 10-28 活动有新 OS 执行总线 API**：不成立——均属 10-07 MXC GA 事件的硬件+落地状态延伸与 XPIA 警告重述，无新 API。

> [!note] 概念节点双链
> [[意图模式规范]] [[语义路由]] [[端侧工具调用]] [[确认机制]] [[元服务]] [[隔离执行]] [[A2A 端侧智能体协议]] [[XPIA 跨提示注入]] [[MCP 与设备侧 MCP]] [[意图框架·跨体系索引 MOC]]

---

> [!warning] 诚实标注
> - iOS 27.2 无新 App Intents Schema 的判定依据：本运行 **WebFetch 直查 `developer.apple.com/documentation/updates/appintents`** 确认最新条目仍 **June 2026**（无 October 2026 或之后条目），27.2 未在 App Intents 框架层引入任何新 Schema/Entity/枚举；消费者功能清单（IT之家/网易/环球网 10-27~28）亦无新意图 Schema 域——属「官方页未列新 Schema」确认（较 10-26 的 RC 推断升级为正式版发布后的官方页逐字确认）。
> - 「排除的 App」统一意图访问排除设置来自 iOS 27.2 媒体功能清单（IT之家 10-27「新增统一设置，可选择哪些 App 不能被 Siri、搜索和建议访问」）；Apple 未单独发框架文档，视为消费者隐私开关（非 `@AppIntent` API），其是否影响开发者侧 intent 注册可见性待 Apple 开发者文档逐字确认（标注为治理细化、非 Schema API）。
> - iOS 27.2 160+ CVE / Apple Intelligence 远程数据访问漏洞来自网易 TechWeb 10-27 报道（163 个可追踪 CVE、Apple Intelligence 远程访问敏感数据、Hide My Email 泄露）；CVE 编号与 Apple 安全通告逐条对应待补（Apple 10-27 安全响应）。
> - Windows 10-28 Surface 活动与 HydraFusion 本地路由预览到点来自 heise.de（2026-10-28 报道）+ 多家媒体复述；HydraFusion「by end of October」为 10-07 官方博文已预告、本次活动确认落地，属已跟踪节点到点交付；MXC GA 与 Entra「to follow shortly」与 10-09 捕获一致。
> - Android beta01 仍为最新、HarmonyOS 仅教程、BFCL 端侧 Planner 无新 official entry 均经官方页 / 镜像榜直查确认；cheesecat LFM2.5-24B-A2B 为社区分析、非端侧小模型新 entry。
> - 本运行未使用 Horizon MCP（仅 agent-mail 在线），全部以 WebSearch + WebFetch 直查官方源 + 权威媒体完成逐平台核验；0 新建 B 节点、3 处 B 既有增补。

## 21:00 二次复核补遗（自动化二次触发，窗口缺口 10-28 19:03 → 21:00）
- **缺口内零净新增**：对 19:03→21:00 约 2h 缺口二次核验——App Intents Updates 官方页仍 **June 2026**（无 Oct 条目）、Android AppFunctions 仍 **`1.0.0-beta01`**（无 beta02/alpha14）、Windows 无新 OS 执行总线 API（10-28 检索命中均为 10-07 Surface 活动材料复述）、BFCL v4 镜像榜（benchlm.ai 仍 10-17 核验）无新端侧 Planner entry、HarmonyOS 仅文档/教程。本 note 结论维持，无需修订。
- **A2UI `1.0.0-alpha02`（2026-10-21）补录**：二次核验发现 A2UI 官方 Jetpack 库已于 10-21 由 alpha01 进位 alpha02（晚于本 note 44h 窗口起点 10-26 22:53，故不计入本窗口净新增），已补录至 [[A2UI 生成式UI协议(Google)与鸿蒙落地 2026]] 文末「2026-10-21 增补」段；性质为次级版本进位、非新范式，★3/10。
