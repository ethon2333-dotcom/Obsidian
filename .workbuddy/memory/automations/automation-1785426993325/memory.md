---
automation: AppIntent 每日情报（自动化 09:00 版，实际按 7 日滚动窗口运行）
last_run: 2026-11-03（23:38，24h+ 续跑）
window: 2026-11-02 12:21 → 11-03 23:38（约 35h，接续 11-02）
---

# 执行摘要（2026-11-03 · 窗口 2026-11-02 12:21 → 11-03 23:38，约 35h）

## 本轮产出（约 35h，接续 11-02 运行）
- **本窗口捕获 1 个真正跨阈值 OS 级进展**：**iOS 27.3 首个 dev beta 于 11-03（美西）/ 11-04（中国）落地，中国区 Apple Intelligence 首次以第三方（阿里 Qwen）端侧模型驱动 Siri / Writing Tools / Visual Intelligence，经同一 App Intents 接口暴露**——「端侧 Planner 底座按区域切换第三方模型、接口不变」里程碑（★7/10）。属模型层/enablement 变更，报道未确认新 `@AppIntent(schema:)` Schema（新 schema API 状态待补）。
- **其余平台零净新增 API**：Android（AppFunctions 仍 `1.0.0-beta01` 10-21；Connected Apps 双路由 + AppFunctions 权限边界为 10-28/29 已捕获复述）、HarmonyOS（稳定）、Windows（无新执行总线 API；agentic 安全书仍 2025-11-18）、BFCL v4（无新 ≤数 B 端侧 Planner entry）。
- **落库**：A 索引 [[AppIntent 每日情报 2026-11-03]]、D 速览 [[AppIntent 每日情报速览 2026-11-03]]、新建 B 节点 [[Apple Intelligence 中国区 Qwen 端侧模型 2026]]（★7）、对 2 个既有 B 追加 ★5 复述状态行（[[Android AppFunctions 设备侧意图 2026]]、[[四平台意图 Registry 来源轴与权限模型对比 2026]]）；看板「本次新增（2026-11-03）」已登记。**1 新建 B 节点 + 2 既有 B 状态行追加**。
- **环境**：WebSearch/WebFetch 工具链路故障（fetch failed），降级为 curl + Google News RSS + DuckDuckGo 直查官方/权威源；无 Horizon MCP（仅 agent-mail 在线）。Apple App Intents Updates 官方页 JS 渲染、华为开发者文档 curl 被拦，依赖 RSS 交叉确认。
- **诚实标注**：iOS 27.3 新 schema API 状态待补（beta 刚落、dev release notes 未完整解析）；`@AppFunctionAccessLevel` 级别语义仍待 developer.android.com/ai/appfunctions 官方逐字；来源轴四平台仍全空白（延续最高优先待办）。

# 执行摘要（2026-10-30 · 24h 复核，窗口 2026-10-29 21:00 → 10-30 21:00，24h）

## 本轮产出（24h）
- **四平台官方框架层 + 跨平台 BFCL 端侧 Planner + XPIA 研究线，本 24h 窗口全部零净新增 API / 评测 / 研究突破**——与连续多轮「OS 框架不日更」结论完全连续，本运行为**纯复核型**。
- **逐平台核验结论**：Apple（App Intents Updates 官方页 WebFetch 直查仍列 iOS 27 时代 API 集、无 2026-10 新 schema；iOS 27.2 支持页仅 Shortcuts 消费者功能、非框架 API）/ Android（Jetpack Release Notes + all-channel 双重直查确认 AppFunctions 仍 `1.0.0-beta01` 10-21 最新、无 beta02/alpha14；Connected Apps Platform + ML Kit Agentic API 为 10-28 Dev Summit 项、本窗口仅分析复述）/ HarmonyOS（仅教程/FAQ 复盘、无 OS API 变更）/ Windows（仅 MXC GA + Copilot Actions preview 复述/安全分析、无新 OS 执行总线 API）/ BFCL v4（LLMBoard 10-30 快照刷新、22 模型全为云级大模型、无新端侧 Planner official entry）。
- **低于阈值·丢弃（不升净新增、不建 B）**：Apple iOS 27.2 支持页消费者功能误读为框架 API；Windows aitechmodel.com ×2 拆解四 building blocks + 命名 XPIA（10-07/10-08 已收录事件复述）；Connected Apps Platform 确认机制细节（beyondthe.news，10-29 已捕获项深化）；HarmonyOS A2UI/Intents Kit 教程；BFCL FunctionGemma-270M「Whetherman」社区 router 自测（dev.to，社区研究非官方 entry）；LFM2.5-24B-A2B BFCLv4 65.01（xabcnews 精读，24B 非端侧，纯模型发布）。
- **落库**：A 索引 [[AppIntent 每日情报 2026-10-30]]、D 速览 [[AppIntent 每日情报速览 2026-10-30]]、看板「本次新增（2026-10-30）」已登记。**0 新建 B 节点、0 既有 B 增补**（无 ≥6/10 真增量）。
- **环境**：无 Horizon MCP（仅 `agent-mail` 在线）；WebSearch + WebFetch 直查官方源（App Intents Updates 页 / iOS 27.2 支持页 / Jetpack Release Notes + all-channel / LLMBoard BFCL-V4 / 华为 Intents Kit FAQ / aitechmodel / beyondthe.news / dev.to / xabcnews）。

## 诚实标注 / 待办
- Apple App Intents Updates 官方页直查（developer.apple.com/documentation/updates/appintents）仍 iOS 27 时代 API 集、无 2026-10 条目，与 10-28「June 2026」结论一致；iOS 27.2 支持页仅 Shortcuts 消费者功能（自动化/动作）。
- Android AppFunctions 仍 beta01（10-21）经 Release Notes + all-channel 双重直查；`@AppFunctionAccessLevel` 级别语义仍待 developer.android.com/ai/appfunctions 逐字段确认。
- BFCL 官方 Berkeley 榜仍停滞（2026-04-12）；LLMBoard 10-30 刷新均为云级大模型、无端侧 entry。
- 沿用：来源轴四平台全空白（最高优先）/ AppFunctions GA / Connected Apps Platform 闸门+Search 确认 UX / ML Kit Agentic API SDK / LFM3-1.7B 官宣+官方复核 / GitHub Copilot Fusion 下沉 / Watch OS 26 / AgentAntibody / Chrome Origin Sets / Berkeley 官方 BFCL v4 博客 / A2UI alpha02 / Per-Intent Privacy Manifest 官方逐字 / 高通 NPU exact specs。

# 执行摘要（2026-10-28 · 21:00 二次触发复核，窗口 2026-10-26 22:53 → 10-28 21:00，约 46h）

## 本轮产出
- **本运行为 10-28 情报 note 的二次触发复核**：10-28 主 note（[[AppIntent 每日情报 2026-10-28]]，窗口 10-26 22:53 → 10-28 19:03）已于本日早些时候由同自动化生成并完成落库（A 索引 + D 速览 + 3 处 B 既有增补 + 看板登记）。本触发在 21:00 对 19:03→21:00 缺口二次核验。
- **缺口内四平台 + HarmonyOS 零净新增 OS 框架层 API**（与连续多轮「OS 框架不日更」结论完全连续）：Apple App Intents Updates 官方页仍 **June 2026**（WebFetch 直查，无 Oct 2026 条目，iOS 27.2 框架层零变更）；Android AppFunctions 仍 **`1.0.0-beta01`**（10-21，无 beta02/alpha14，Jetpack 官方页 + beta-channel 列表交叉确认）；Windows 10-28 检索命中均为 10-07 Surface 活动材料复述（MXC GA / HydraFusion 本地路由「10 月底实验预览」到点 / XPIA 警告重述），无新 OS 执行总线 API；BFCL v4 镜像榜（benchlm.ai 仍 10-17 核验）无新端侧 Planner entry；HarmonyOS 仅文档/教程（Intents Kit 标准意图规范 10-15 更新、ArkUI 课程复述）。
- **A2UI `1.0.0-alpha02`（2026-10-21）补录（★3/10，次级进位·非新范式）**：二次核验发现 A2UI 官方 Jetpack 库已于 10-21 由 alpha01 进位 alpha02（晚于 10-28 note 的 44h 窗口起点、且 10-26 跑亦漏捕），已补录至 [[A2UI 生成式UI协议(Google)与鸿蒙落地 2026]] 文末「2026-10-21 增补」段；性质为已跟踪官方库的次级版本进位，非新 API 范式，不构成本窗口净新增。
- **落库**：既有 [[AppIntent 每日情报 2026-10-28]] 追加「21:00 二次复核补遗」小节（缺口零净新增确认 + A2UI alpha02 补录指针）；[[A2UI 生成式UI协议(Google)与鸿蒙落地 2026]] 追加 alpha02 段；看板「本次新增（2026-10-28）」已于早些时候登记、本触发不重复登记。**0 新建 B 节点**（A2UI alpha02 为既有笔记增补、非新建）。
- **环境**：无 Horizon MCP（仅 `agent-mail` 在线）；WebSearch + WebFetch 直查官方源（App Intents Updates 页 / Jetpack appfunctions + beta-channel / benchlm.ai / 华为开发者文档 / heise/unite.ai/slashgear/bgr 等）完成逐平台核验。

## 诚实标注 / 待办
- A2UI alpha02 官方 alpha-channel 逐字 Release Notes 未单独抓取（沙箱网络只取到 beta/alpha channel 列表 + 镜像交叉确认），版本进位高置信，组件变更细节待官方 notes 逐字。
- 10-28 主 note 的「iOS 27.2 零新 Schema / Excluded Apps 消费者层意图访问治理 ★6 / 160 CVE 含 Apple Intelligence 远程访问漏洞」结论经本触发二次核验维持。
- 延续：@AppFunctionAccessLevel 级别语义官方文档逐字段确认（beta01 仍未展开）/ AppFunctions GA 日 / Per-Intent Privacy Manifest 官方逐字 / 来源轴四平台全空白（最高优先待办）/ Watch OS 26 / NowSecure / AgentAntibody / Chrome Origin Sets / 高通 NPU exact specs / Berkeley BFCL v4 官方博客原文 / A2UI 后续 release 复核。

# 执行摘要（2026-10-18 · 复核型 + iOS 27.1 发布节奏再澄清，窗口 2026-10-16 21:00 → 10-18 18:34，约 45.5h）

## 本轮产出（约 45.5h）
- **四平台零 OS 框架层净新增 API**，延续「OS 框架不日更」纪律，与 10-16 复核型结论完全连续。本运行为**复核型 + 1 项发布节奏再澄清**。
- **唯一真·增量（★6/10）= iOS 27.1 发布节奏再澄清（撤回 10-16 推论）**：第三方（apfelpatient，10-17，基于 Apple 公告整理）确认 **iOS 27.1 没有设备公开 beta 阶段**，以 Duo 出厂/首次设置 build（24A94232 出厂 → 24A94425，10-12 放出，无 changelog）形态交付；Apple 09-16 / 10-16 说的「A beta version will be available later this month」实为 **Xcode 27.1 工具链 beta（09-18 已放出）**，并非设备 iOS 27.1 beta。**这撤回 10-16 跑把「iOS 27.1 双屏 Schema」跟踪窗口前移到「本月晚些 beta」的推论**——双屏新 intent/entity Schema（若有）只在 10-23 Duo 出厂正式版揭晓（跟踪窗口回退）。多条果粉媒体（applescoop / guofenchaxun / 今日头条数码知更鸟）一致复述「iOS 27.1 不开放测试、直接迎来 iOS 27.2」。
- **Apple 验证**：iOS 27.2 beta 4 = 24B5110a（10-13）仍为最新、beta 5 预期 Late October（本窗口无 beta 5）；App Intents Updates 页最新仍 June 2026；**无新 `@AppIntent(schema:)` Schema**（本运行 WebSearch 二次核验 betaprofile.dev + Apple Developer News 一致确认）。
- **Android**：官方最新 AppFunctions = alpha13（10-07），无 alpha14；本次 `d.android.com/ai/appfunctions` 官方概览页访问成功（与 10-16 fetch failed 不同），确认无 alpha14 信号；`@AppFunctionAccessLevel` 级别语义官方仍未展开。
- **HarmonyOS**：Intents Kit / ArkAF / 端侧 A2A 文档稳定；技能调用接入方案页 V13 仍 2026-10-10、落 10-16 窗口外、非 API 变更；本窗口命中均为第三方 how-to/课程稿。
- **Windows**：Copilot Actions 面向全体 Insider 渠道铺开（1.25112.74+）= 已收录事件部署推进，非新 OS 执行总线 API；MXC 隔离 / 低权账号 / ODR consent 稳定，HydraFusion 本地路由仍「10 月底实验性预览」。
- **BFCL v4**：端侧 Planner 无新 official entry；FunctionGemma 270M 27.03 / Qwen3-0.6B 23.9% / LittleLamb-TC 0.3B 51.55 / Needle 2 42.6% 维持；slash-invest Needle 2 拆解（域外 28.7 / tool-retrieval 收窄到 5 工具）系社区分析，与 09-12 已录机制复述。
- **XPIA（低于阈值·丢弃）**：CVE-2026-103572（VS Copilot / SSMS 工具层 agent 文件写入绕过，CVSS 8.8，trailing-dot 截断）→ 经核查影响**开发者工具层 agent**，**非 Windows OS agentic 执行总线（Copilot Actions / Agent Workspace / MXC）**，按「四平台 OS 框架执行总线」口径丢弃（同 10-06 GitLab AI Gateway / 10-05 MCP 工具链 CVE）；其威胁模型价值已落 [[XPIA 跨提示注入]] 既有论述，未升新节点。
- **落库**：A 索引 [[AppIntent 每日情报 2026-10-18]]（18:38 先行产出，含完整情报正文）、D 速览 [[AppIntent 每日情报速览 2026-10-18]]（本运行补齐新建）、B 既有增补 1（[[Apple AppIntents Schema Protocol 2026]] 文末追加「2026-10-18 增补」段，撤回 10-16 前移推论）、看板「本次新增（2026-10-18）」已登记。**0 新建 B 节点**。
- **环境**：无 Horizon MCP（仅 `agent-mail` 在线）；WebSearch 直查官方/权威源（Apple Developer News + App Intents Updates 页 + betaprofile.dev + apfelpatient/applescoop/guofenchaxun + d.android.com/ai/appfunctions + 华为 Intents Kit + learn.microsoft.com + gorilla.cs.berkeley.edu + HuggingFace model card + 安全媒体）。

## 诚实标注 / 待办
- iOS 27.1 无设备公开 beta、以 Duo 出厂/设置 build 交付（24A94232→24A94425）来自 apfelpatient（10-17）基于 Apple 公告整理；「Apple 本月晚些 beta = Xcode 27.1 beta（09-18 已出）」由该文 + Apple 09-16 开发者新闻原文交叉确认。Apple 09-16 原文上下文指 Xcode 27.1 开发支持，与 apfelpatient 解读一致。
- 10-16 段未删除（保留推断链），本段显式标注修订，避免下次重复「前移」；跟踪窗口回退到 10-23 出厂正式版。
- `@AppFunctionAccessLevel` 级别语义（public/protected/system 等）官方 Release Notes 仍未展开，待 developer.android.com/ai/appfunctions 逐字段确认（本窗口官方概览页访问成功、仍无展开）。
- 沿用：iOS 27.1 出厂正式版（10-23）+ 设置期更新 build 是否带双屏场景新 intent/entity Schema（跟踪窗口回退）/ 真 alpha14 / A2UI alpha02 / Per-Intent Privacy Manifest 官方逐字 / Watch OS 26 / 高通 NPU exact specs / NowSecure / AgentAntibody / Chrome Origin Sets / Berkeley 官方 BFCL v4 博客原文 / Hudson Rock XPIA infostealer 分析是否需升 XPIA 节点（待一手 PoC 或微软官方回应）。

# 执行摘要（2026-10-16 · 复核型 + 官方澄清，窗口 2026-10-15 19:22 → 10-16 21:00，约 25.6h）

## 本轮产出（约 25.6h）
- **四平台零 OS 框架层净新增 API**，延续「OS 框架不日更」纪律，与 10-15 复核型结论完全连续。
- **唯一真·增量（★6/10）= Apple 官方开发者新闻（developer.apple.com/news）澄清 iOS 27.1**：明确「iPhone Duo 10-23 上市、预装 iOS 27.1；iOS 27.1 的 developer beta 将于本月晚些时候放出」。**直接修订 10-08→10-15 连续四轮跑采信的「Apple 跳过 27.1 beta、直发 27.2」媒体共识旧结论**——Apple 现确认 27.1 会发 beta（Duo 开发用），仅独立于常规 27.2 beta 线。该澄清**不带来任何新 `@AppIntent(schema:)` Schema**（App Intents Updates 页最新仍 June 2026；27.2 beta 4 = 24B5110a 最新、beta 5 预期 Late Oct 均无新 Schema），但把头号跟踪项「iOS 27.1 是否带双屏场景新 intent/entity Schema」窗口从 10-23 正式版前移到「本月晚些 beta」。
- **Android**：官方最新 AppFunctions = alpha13（2026-10-07），无 alpha14；Jetpack Release Notes 直查因沙箱网络 `fetch failed` 未成功，沿用 10-13 三处官方列表直查结论 + 本窗口官方概览页无 alpha14 信号，高置信维持 alpha13 最新；`@AppFunctionAccessLevel` 级别语义官方未展开。
- **HarmonyOS**：Intents Kit 技能调用接入方案页（V13）显更新时间 2026-10-10，属文档修订、落 10-13 窗口外、非 API 变更；其余文档稳定。
- **Windows**：10-07 MXC GA + Hybrid Intelligence + 任务栏搜索 Agent 启动器已收录，本窗口无新 OS 执行总线 API；HydraFusion 本地模型路由仍为「10 月底实验性预览」。
- **BFCL v4**：端侧 Planner 无新 official entry；Needle 2 45M 42.6% / FunctionGemma 270M 46.1% / LFM2.5 230M 60.8% / Apple FM 61.7% / LittleLamb 0.3B 51.55 维持；Luxand/Ertas/aibacon（Needle 2）均为厂商自测/社区分析，低于阈值。
- **XPIA**：RAMPART 文档 / learn.microsoft.com 训练模块 / agentmelt 2026 回顾 / PointGuard 分析均已知，无新 OS 执行总线 CVE。
- **落库**：A 索引 [[AppIntent 每日情报 2026-10-16]]、D 速览 [[AppIntent 每日情报速览 2026-10-16]]、B 既有增补 1（[[Apple AppIntents Schema Protocol 2026]] 文末新增 10-16 修订段）、看板「本次新增（2026-10-16）」已登记。**0 新建 B 节点**。
- **环境**：无 Horizon MCP（仅 `agent-mail` 在线）；WebSearch 直查官方/权威源（developer.apple.com/news + App Intents Updates 页 + betaprofile.dev + Jetpack Release Notes[fetch failed] + 华为 Intents Kit + learn.microsoft.com + gorilla.cs.berkeley.edu + HuggingFace model card + 9to5mac/cnet/agentmelt/pointguard）。

## 诚实标注 / 待办
- Apple 官方仅写「later this month」，**未给 27.1 beta 精确日期**；27.1 beta 是否真含双屏新 Schema 待 beta 推送后逐字复核（跟踪窗口前移）。
- Android Jetpack Release Notes 直查 fetch failed（沙箱网络），下次跑优先重试直查以闭合 alpha13/alpha14 基线。
- `@AppFunctionAccessLevel` 级别语义（public/protected/system 等）官方 Release Notes 仍未展开，待 developer.android.com/ai/appfunctions 逐字段确认。
- 沿用：iOS 27.1 beta（本月晚些）双屏新 Schema / 真 alpha14 / A2UI alpha02 / Per-Intent Privacy Manifest 官方逐字 / Watch OS 26 / 高通 NPU exact specs / NowSecure / AgentAntibody / Chrome Origin Sets / Berkeley 官方 BFCL v4 博客 / Hudson Rock XPIA infostealer 分析是否需升 XPIA 节点（待一手 PoC 或微软官方回应）。

# 执行摘要（2026-10-15 · 复核型，窗口 2026-10-13 12:37 → 10-15 19:22，约 2.3 日）

## 本轮产出（约 2.3 日）
- **四大 OS 官方框架层 API 仍零净新增**（iOS 27.2 beta 4 = 24B5110a 例行更新无新 `@AppIntent(schema:)` Schema / AppFunctions 守 alpha13 无 alpha14 / HarmonyOS 文档稳定 / Windows 10-07 事件已收录且无新 OS 执行总线 API），与 10-13 复核型结论完全连续。本运行为**纯复核型**。
- **唯一真事件（★3/10，状态更新非框架新增）= Apple iOS 27.2 beta 4（build 24B5110a，2026-10-14 推送）例行开发者测试版** + **确认 iOS 27.1 专供 iPhone Duo、直板机跳过**（与 10-08 跑记录一致、本次 beta 4 进一步坐实）。AutoLock（设备防盗自动锁定，beta 2 起后台、beta 4 疑似进入测试）属设备防盗安全、与意图框架无关，不纳入。
- **低于阈值·复述/社区研究（不升净新增、不建 B）**：① Hudson Rock / technadu 2026-10 对 Windows 11 Agentic OS 的 XPIA infostealer 攻击面分析（任务栏 Copilot agent 成中心化数据枢纽，文档内隐藏指令→agent 越权外发凭据）——属 10-07 已收录 Windows agentic 特征的第三方安全复述，[[XPIA 跨提示注入]]/[[Agent Workspace 隔离执行]] 已覆盖同类；② d9bl.com 2026-10 端侧工具调用量化实测（BFCL v4，Qwen3-0.6B 至 Q4_K_M 撑住、Llama-3.2-1B 量化后崩）——社区研究、非新模型/非官方 benchmark。
- **BFCL v4**：端侧 Planner 无新 official entry；FunctionGemma 270M 27.03 / Qwen3-0.6B 23.9% / LittleLamb 0.3B 51.55 / Needle 2 45M 42.6% 均为已知 model card；在线榜 top 仍前沿云模型（10-13 已标注快照过时）。
- **落库**：A 索引 [[AppIntent 每日情报 2026-10-15]]、D 速览 [[AppIntent 每日情报速览 2026-10-15]]、看板「本次新增（2026-10-15）」已登记。**0 新建 B 节点、0 既有 B 增补**（无 ≥6/10 真增量）。
- **环境**：无 Horizon MCP（仅 `agent-mail` 在线）；WebSearch 直查官方/权威源（Apple TestFlight Release Notes + ios/whats-new + Jetpack Release Notes/appfunctions + 华为 ArkAF + learn.microsoft.com agentic security + gorilla.cs.berkeley.edu BFCL v4 + HuggingFace model card + IT之家/今日头条/网易/technadu/d9bl）。

## 诚实标注 / 待办
- iOS 27.2 beta 4「无新 `@AppIntent(schema:)` Schema」为官方日志「仅含新功能/新特性」未列 + 历轮「OS 框架不日更」一致性推断，**非逐字段反编译确认**；若有新 schema 将在 Duo 27.1（10-19~23）或 27.2 正式版复核。
- iOS 27.1 Duo 专属结论来自媒体汇总、Apple 未发官方「跳过 27.1」公告，与 10-08 跑一致。
- `@AppFunctionAccessLevel` 级别语义官方仍未展开，待 developer.android.com/ai/appfunctions 逐字段确认。
- 沿用：iOS 27.1 正式版（10-19~23 随 Duo）双屏场景新 intent/entity Schema / 真 alpha14 / A2UI alpha02 / Per-Intent Privacy Manifest 官方逐字 / Watch OS 26 / 高通 NPU exact specs / NowSecure / AgentAntibody / Chrome Origin Sets / Berkeley 官方 BFCL v4 博客 / Hudson Rock XPIA infostealer 分析是否需升 XPIA 节点（待一手 PoC 或微软官方回应）。

# 执行摘要（2026-10-13 · 复核型 + 知识库纠错，窗口 2026-10-10 21:00 → 10-13 12:37，约 2.6 日）

## 本轮产出
- **核心 = alpha13 复核确认（KB 纠错）**：10-13 对官方 Jetpack Release Notes 发布页 + alpha-channel + all-channel 三处官方列表直查，**一致确认 `1.0.0-alpha13`（2026-10-07）确为真实发布**，含 `@AppFunctionAccessLevel`（Id47e1）/ `@AppFunction`→`@AppFunctionDeclaration`（I4b15d）/ `ObserveAppFunctionsEvent`→`AppFunctionsChangeEvent`（Iec918）/ `AppFunctionMetadata` 暴露（If1117）/ proxy 类型 bug fix。**即 10-09 跑正确、10-10 跑的「alpha13 系误记」更正系误判（索引滞后）**，已回退 10-10 误更正并重新确认 Android 权限模型三向约束（caller `EXECUTE_APP_FUNCTIONS` + `scope` + 函数侧 `@AppFunctionAccessLevel`）。
- **四平台零 OS 框架净新增（本窗口）**：Apple（iOS 27.2 beta 3 = 24B5099f 无新 `@AppIntent(schema:)`、iOS 27.1 未发、预期 10-19~23）/ HarmonyOS（Intents Kit / ArkAF / A2A 文档稳定）/ Windows（无新 agentic security API，MXC GA 10-07 已收录、HydraFusion 本地路由仍 10 月底实验预览）/ BFCL v4（在线榜 top 前移为 Claude Opus 4.5/Sonnet 4.5/Gemini 3 Pro 代际云模型、端侧 Planner 无新 official entry）/ XPIA（AWS/Google/Vercel agent infra 工具触发缺陷、GitLab CVE-2026-90970 均非四平台 OS 框架执行总线，按口径丢弃）。
- **BFCL 诚实标注**：库内旧 top 快照「Qwen3.7 Max 75.0%」「Llama 3.1 405B 88.5%」已过时（实时榜 top 已被前沿云模型占据）；端侧小模型（FunctionGemma 270M / Qwen3-0.6B / MiniCPM5-2B / LittleLamb 0.3B）仍为已知 model card，无新 entry。
- **落库**：A 索引 [[AppIntent 每日情报 2026-10-13]]、D 速览 [[AppIntent 每日情报速览 2026-10-13]]、A/B 既有回退更正 4（10-09 A、10-10 A、Android AppFunctions B、Registry 对比 B）、看板「本次新增（2026-10-13）」已登记。**0 新建 B 节点**（alpha13 事实已确认、仅回退误更正）。
- **环境**：无 Horizon MCP（仅 `agent-mail` 在线）；WebSearch 直查官方/权威源（Jetpack Release Notes/alpha-channel/all-channel + Apple iOS What's New + 华为 ArkAF/A2A + learn.microsoft.com agentic security + gorilla.cs.berkeley.edu BFCL v4）。

## 诚实标注 / 待办
- `@AppFunctionAccessLevel` 级别语义（public/protected/system 等）官方 Release Notes 仍未展开，待 developer.android.com/ai/appfunctions 逐字段确认（延续 09-25 `scope` 纪律）。
- 后续每日跑 Android 侧应以「官方最新 = alpha13（10-07）」为基线检索 alpha14+；10-10「以 alpha12 为基线」指示已失效。
- 沿用：iOS 27.1 正式版（10-19~23）双屏场景新 Schema / Berkeley 官方 BFCL v4 博客原文 + 库内旧 top 快照更新 / AppFunctions GA 日 / Per-Intent Privacy Manifest 官方逐字 / Watch OS 26 / 高通 NPU exact specs / A2UI alpha02 / NowSecure / AgentAntibody / Chrome Origin Sets。

# 执行摘要（2026-10-09 · 24h 复核，窗口 2026-10-08 21:00 → 10-09 21:00）

## 本轮产出（约 24h）
- **唯一 OS 级净新增 = Android AppFunctions `1.0.0-alpha13`（官方 Jetpack Release Notes 标注 2026-10-07 发布）**——但**上一轮（10-08）误判「alpha12 无 alpha13」未捕获**，本运行直查 `developer.android.com/jetpack/androidx/releases/appfunctions` + alpha-channel 纠正并收录。alpha13 在权限模型落了**首个函数侧访问限制原语 `@AppFunctionAccessLevel`**（access restriction setting），并伴 `@AppFunction`→`AppFunctionDeclaration` 破坏性重命名、`ObserveAppFunctionsEvent`→`AppFunctionsChangeEvent` 重命名、`AppFunctionMetadata` 在 `AppFunctionService` 暴露。这是四平台设备侧 MCP / 意图 Registry 里**首个「函数自身声明可访问性」原语**，把 Android 权限模型补成「caller 权限 + 可见性 scope + 函数侧 access level」三向约束（详见 [[Android AppFunctions 设备侧意图 2026]] / [[四平台意图 Registry 来源轴与权限模型对比 2026]]）。
- **零净新增确认**：Apple（iOS 27.2 beta 3 = build 24B5099f 无新 `@AppIntent(schema:)` Schema；AT&T carrier bundle 72.0.3 更新非框架）；HarmonyOS（Intents Kit 官方页 2026-09-14 稳定、无新 OS API）；BFCL v4（端侧 Planner 无新入榜；FunctionGemma 270M/LittleLamb 0.3B/Qwen3-0.6B 为已知 model card）。
- **Windows 10-07 事件 10-09 补细节（非独立净新增）**：taskbar Search actions、Entra 本地 agent 身份扩展、MAI Code 1.1 Flash 本地参数 corroboration（3-bit/256K）——均属 10-08 跑已捕获 MXC GA 事件的延伸，向 [[Windows Copilot Actions 与 Agent Workspace 2026]] 追加状态段。
- **去伪/丢弃（按口径）**：XPIA 窗口内三项——CVE-2026-26133（Microsoft 365 Copilot，M365 应用/云层非 OS 执行总线）、CNCERT 警示的 OpenClaw 第三方自托管 agent、PraisonAI AICoder 19 项缺陷（10-08 披露，prompt injection→root 文件写）——均非四平台 OS 框架执行总线，同 10-06 丢弃 GitLab AI Gateway / 10-05 丢弃 MCP 工具链 CVE 口径。
- **落库**：A 索引 [[AppIntent 每日情报 2026-10-09]]、D 速览 [[AppIntent 每日情报速览 2026-10-09]]、B 既有增补 3（[[Android AppFunctions 设备侧意图 2026]] / [[四平台意图 Registry 来源轴与权限模型对比 2026]] / [[Windows Copilot Actions 与 Agent Workspace 2026]]）、看板「本次新增（2026-10-09）」已登记。**0 新建 B 节点**。
- **环境**：无 Horizon MCP（仅 `agent-mail` 在线）；WebSearch 直查官方/权威源（developer.android.com Jetpack alpha-channel + Release Notes、9to5Mac、华为 Intents Kit、HF model card、learn.microsoft.com、Permiso/LinkedIn/CNCERT/agentfailures 安全源）。

## 诚实标注 / 待办
- `@AppFunctionAccessLevel` 级别语义（public/protected/system 等）官方 Release Notes 仅写「support access restriction setting」，**未展开**，待 developer.android.com/ai/appfunctions 官方文档逐字段确认（延续 09-25 `scope` 纪律）。
- 它**不属于** provenance/来源轴——来源轴四平台全空白结论不变。
- 上一轮（10-08）漏捕 alpha13 的根因：未直查 Jetpack alpha-channel，仅依赖前一轮结论；后续每轮 Android 侧应优先直查 alpha-channel + Release Notes。
- 沿用：iOS 27.1 正式版（10-23 随 Duo）是否带双屏场景新 intent/entity Schema / Berkeley 官方 BFCL v4 博客 / AppFunctions GA 日 / `AppFunctionDeclaration` 迁移影响 / AndroidX 聚合页 alpha11 vs 直查 alpha13（原 alpha12 不一致已随 alpha13 直查闭合）/ Per-Intent Privacy Manifest 官方逐字 / Watch OS 26 / A2UI alpha02 / 高通 NPU exact specs / NowSecure / AgentAntibody / Chrome Origin Sets。

# 执行摘要（2026-10-08 · 24h 复核，窗口 2026-10-07 21:00 → 10-08 21:00）

## 本轮产出（约 24h）
- **唯一 OS 级净新增 = Windows Microsoft Execution Containers (MXC) 于 2026-10-07 正式 GA**（preview → GA）。官方博文 blogs.windows.com/windowsexperience/2026/10/07/building-windows-for-hybrid-intelligence/ + it-connect.tech / pymnts / ainewsbank 多家 corroboration。开源执行沙箱，运行时定义 agent 文件/网络边界；隔离五档（进程/会话/WSLc/VM/Windows 365 for Agents）；身份分离（动作归 agent 非用户，GitHub Copilot+Defender 实测拦截并切断 agent 的 SharePoint 访问）；`/sandbox` 启用；已支持 OpenAI Codex/GitHub Copilot/OpenClaw/Replit/LM Studio/NVIDIA OpenShell/Unsloth AI，后续 Claude Code/Perplexity/Manus 等，Meta Muse for Windows 即将接入。关闭「MXC 何时 GA」待办。**性质（★7-8/10，OS 框架 GA 级增量）**：09-13 IFA 预览以来首个 GA 级净新增。
- **Apple 事实收口（★6/10）**：Apple 跳过 iOS 27.1 beta、直发 iOS 27.2 beta 3（build 24B5099f，约 10-05/06）。媒体共识 = 防 Duo 代码经 27.1 beta 解包泄露（Duo 10-23 上市、预装 iOS 27.1 正式版、不开放 beta）。常规 iPhone 线 27.2 beta **无新 `@AppIntent(schema:)` Schema**——关闭/更新 09-20/09-21「iOS 27.1 beta」跟踪项（事实比预期更明确：27.1 从未发 beta，是 Duo 专属正式版）。下个观察点：10-23 iOS 27.1 正式版是否带双屏场景新 intent/entity schema。
- **零净新增确认**：Android AppFunctions 守 `alpha12`（09-23）无 `alpha13`；HarmonyOS Intents Kit 官方页稳定、A2UI alpha01、无新 OS API；BFCL v4 端侧 Planner 无新入榜（Qwen3.7 Max 75.0% 居首快照稳定）。
- **去伪/丢弃**：OWASP 2026 LLM Top 10 重排 + Agent Control Standard (ACS v0.1) 经核查为跨平台治理/标准文档、**非四平台 OS 框架执行总线 API**，按任务「聚焦 OS 级框架」丢弃（同此前 OWASP 处置）；XPIA CVE（llama.cpp CVE-2026-107183 / Langflow CVE-2026-97676~97680）为工具链/应用层漏洞、**非四平台 OS 框架执行总线**，按口径丢弃（同 10-06 丢弃 GitLab AI Gateway、10-05 丢弃 MCP 工具链 CVE）。
- **落库**：A 索引 [[AppIntent 每日情报 2026-10-08]]、D 速览 [[AppIntent 每日情报速览 2026-10-08]]、B 既有增补 3（[[Windows Copilot Actions 与 Agent Workspace 2026]] / [[Agent Workspace 隔离执行]] / [[Apple AppIntents Schema Protocol 2026]]）、看板「本次新增（2026-10-08）」已登记。**0 新建 B 节点**。
- **环境**：无 Horizon MCP（仅 `agent-mail` 在线）；WebSearch 直查官方/权威源（微软官方博文 + it-connect.tech/pymnts/ainewsbank + 9to5Mac/MacRumors/AppleInsider/网易/新浪 + developer.android.com/ai/appfunctions + 华为 Intents Kit + benchlm + 安全媒体）。

## 诚实标注 / 待办
- MXC HydraFusion 本地模型路由仍为 **10 月底实验性预览**（非 GA）；MAI Code 1.1 Flash 量化参数（137B/6.8B active/3.3-bit/53GB/256K）来自 it-connect 转述，待微软官方逐字。
- Apple 跳号动机为媒体共识、Apple 未发官方「跳过 27.1」公告；iOS 27.1 正式版（10-23）是否含 App Intents 新 Schema 待逐字复核。
- MXC 与既有 Agent Workspace 容器/独立账号的关系（复用还是并列）、是否受 08-02 `Experimental agentic features` 同一 opt-in 管控、沙箱外两类动作（内置文件工具/远程 MCP）治理归属待官方文档确认。
- 沿用：Berkeley 官方 BFCL v4 博客 / AppFunctions alpha13 / Per-Intent Privacy Manifest 官方逐字 / Watch OS 26 / 高通 NPU exact specs / A2UI alpha02 / NowSecure / AgentAntibody / Chrome Origin Sets。

# 执行摘要（2026-10-07 · 24h 复核，窗口 2026-10-06 21:00 → 10-07 21:00）

## 本轮产出（约 24h）
- **四大 OS 官方框架层 API + 跨平台 BFCL v4 + XPIA 研究线，本 24h 窗口均无净新增 API / 评测 / 研究突破**——符合「OS 框架不日更」规律，与 10-05 / 10-06 / 10-06-晚 连续结论一致。本期为**复核型运行**：把「已复核·无净新增」显式落档，避免下次重复检索。
- **关键事实校验（非新增·用于去重）**：Apple iOS 27.1 beta 确认未发布（Apple Developer 10-07「later this month」；iPhone Duo 10-23 上市）；iOS 27.2 beta 3（24B5099f，10-05）为最新 dev beta，无新 `@AppIntent(schema:)` Schema。Android AppFunctions 守 `alpha12`（09-23）无 `alpha13`。HarmonyOS 无新 OS API（Intents Kit 官方页稳定 04-29）。Windows Copilot Actions/Agent Workspace/ODR 无新 Registry API；台媒「微软急发警告」文 = learn.microsoft.com agentic security 文档中文复述。BFCL v4 快照仍 10-01，BTL-3 88.5% 现确认为 **Bad Theory Labs 开放权重**（此前「疑 Llama 3.1 405B」歧义已澄清）。
- **去伪/丢弃**：窗口内 4 组 XPIA 命中——CVE-2026-91140（Progress DataDirect，10-06）、CVE-2026-103956/957/958/104019（AWS Loom+SageMaker，10-07）、CVE-2026-90970（GitLab，dev.to 10-06 重提·同 10-06 已丢弃项）、Meta Muse VM escape（Meta，10-06）——**全部经核查为非四平台 OS 框架执行总线（应用/工具链/云厂商）或已覆盖项，按口径丢弃**（同 10-06 丢弃 GitLab AI Gateway、10-05 丢弃 MCP 工具链 CVE）。
- **诚实标注新增**：AndroidX 聚合发布页（media2 镜像）列 appfunctions 仍为 `alpha11`（08-26），与 09-25 直查 Release Notes 的 `alpha12`（09-23）页面级不一致——疑似聚合页未按 alpha-channel 刷新，待 developer.android.com/ai/appfunctions 闭合。
- **落库**：A 索引 [[AppIntent 每日情报 2026-10-07]]、D 速览 [[AppIntent 每日情报速览 2026-10-07]]、看板「本次新增（2026-10-07）」已登记。**0 新建 B 节点、0 既有增补**（无 ≥6/10 真增量）。
- **环境**：仅 `agent-mail` 在线，未调用 Horizon MCP；WebSearch 直查官方/权威源（developer.apple.com/news、theapplewiki、betawiki、developer.android.google.cn AndroidX、developer.huawei.com Intents Kit、learn.microsoft.com、benchlm、threatcluster、f5、deniz.in、cyberrecaps）。

## 诚实标注 / 待办
- iOS 27.1 beta 实际发布日与是否带新 Schema API（Duo 适配之外）待 Apple 逐字。
- **AndroidX 聚合页 alpha11 vs 直查 alpha12 不一致**待 developer.android.com/ai/appfunctions + alpha-channel 复核。
- AppFunctions `alpha13` 与调用方身份注入新机制（`alpha12` 移除 `AppFunctionContext` 后）待官方文档。
- 沿用：Berkeley 官方 BFCL v4 博客原文（连续多轮待办，端侧 Planner 历史分数仍未被官方榜逐条复核）/ Per-Intent Privacy Manifest 官方逐字 / Watch OS 26 / AppFunctions GA / A2UI alpha02 / 高通 NPU exact specs / NowSecure / AgentAntibody / Chrome Origin Sets。

# 执行摘要（2026-10-06-晚 · 13.5h 复核，窗口 2026-10-06 07:33 → 21:00）

## 本轮产出（约 13.5h，同日日间复核）
- **四大 OS 官方框架层 + 跨平台 BFCL v4 + XPIA 研究线本 13.5h 窗口均无净新增**——与当日晨间跑（10-05→10-06 07:33）结论完全连续一致，再次印证「OS 框架不日更」规律。本期为**同日日间复核运行**，把「已复核·无净新增」显式落档。
- **所有高显著度命中项经核查均落正确处置桶**：iOS 27.2 Beta 3（10-06 发，build 24B5099f，无新功能/无新 Schema，Siri Gemini 五语言为更早 beta 复述）；Gemini Calling（Call for Me 扩展至个人联系人，Android Authority 拆解，10-05/06，属 Gemini app 消费功能、非 AppFunctions 框架）；鸿蒙出海+生态数字（余承东 10-06，商业/生态叙事、非 OS API）；Clef 决策模型（10-06 中文媒体，10-02 已收复述）；GitHub Computer Use 三维门禁（10-01，GitHub 应用级、非 Windows OS）；MCP protocol pivoting（CVE-2026-97228 Rapid7 2.7 等）/ camel-ai·bisheng·DB-GPT 代码执行 CVE / 恶意 README 注入 / DW 沙箱逃逸——**均非四平台 OS 框架执行总线，按口径丢弃**（同晨间丢弃 GitLab AI Gateway CVE）。
- **落库**：A 索引 [[AppIntent 每日情报 2026-10-06-晚]]、D 速览 [[AppIntent 每日情报速览 2026-10-06-晚]]；**0 新建 B 节点、0 既有增补**（无 ≥6/10 真增量）。看板「本次新增（2026-10-06-晚）」已登记。
- **环境**：仅 `agent-mail` 在线，未调用 Horizon MCP；WebSearch 直查官方/权威源（IT之家/iGeeksBlog/网易/阿里云/掘金/anothergptwrapper/anotherwrapper/hellomarvis/agentlocker/cowork.ink）。

## 诚实标注 / 待办
- iOS 27.1 beta 实际发布日与是否带新 `@AppIntent(schema:)` Schema（iPhone Duo 适配之外）待 Apple 逐字；10-19~23 为第三方汇总。
- AppFunctions `alpha13` 是否存在、是否引入调用方身份注入新机制（`alpha12` 移除 `AppFunctionContext` 后）待 developer.android.com/ai/appfunctions 官方文档。
- Gemini Calling 精细化权限是否为独立系统级 API 还是纯 Gemini app 内权限 UI 待 Google 官方；不归入 OS 意图框架。
- GitHub Computer Use 三维门禁（应用/动作/数据+有效期）与 [[确认机制]] 同构，但为 GitHub 应用级能力、非 Windows OS；若未来 Windows Agent Workspace 借鉴此模型再纳入。
- 沿用：Per-Intent Privacy Manifest 官方逐字 / Watch OS 26 / AppFunctions GA / A2UI alpha02 / 高通 NPU exact specs / **Berkeley 官方 BFCL v4 博客**（连续多轮待办，端侧 Planner 历史分数仍未被官方榜逐条复核）/ NowSecure / AgentAntibody / Chrome Origin Sets。

# 执行摘要（2026-10-06 · 24h 复核，窗口 2026-10-05 → 10-06）

## 本轮产出（约 24h）
- **四大 OS 官方框架层 + 跨平台 BFCL v4 + XPIA 研究线，本 24h 窗口（2026-10-05 07:33 → 10-06 07:33）均无净新增 API / 评测 / 研究突破**——完全符合「OS 框架不日更」规律，与 10-05（48h）结论连续一致。本期为**复核型运行**：把「已复核·无净新增」显式落档，避免下次重复检索。
- **唯一高显著度 XPIA 条目经核查丢弃**：CVE-2026-90970（GitLab 自托管 AI Gateway prompt template 沙箱逃逸→RCE，CVSS 9.9，10-02 披露，CWE-1336）属 DevOps 网关工具链、**非四平台 OS 框架执行总线**，按筛选规则丢弃（同 10-05 丢弃 CVE-2026-104120 MCP 工具链、09-30 注 Plugin4Shell 应用层 RCE 的口径）。其价值是「agent 隔离层即靶面」趋势的再次印证，已涵盖于 [[隔离执行]]/[[XPIA 跨提示注入]] 既有论述。
- **逐平台核验结论**：Apple iOS 27.1 beta 仍未确认本窗口发布、无新 `@AppIntent(schema:)` Schema；Android AppFunctions 守 `alpha12`（09-23）无 `alpha13`、Gemini Nano v3 端侧 Function Calling 为 I/O '26/Android 18 既有叙事；HarmonyOS 无新 OS API；Windows Copilot Actions/Agent Workspace/ODR 无新 Registry API、26H2 已 GA。
- **BFCL v4**：端侧 Planner 无新入榜；聚合榜快照仍为 10-02（benchlm 22 行全厂商自报）+ 持续镜像（llm-stats，归一化口径不同、不与官方 Berkeley 榜直接可比）；MiniCPM5-2B 66.60 / FunctionGemma 27.03 / qwen3-0.6b-tool-router 54.08 维持。**Berkeley 官方 BFCL v4 博客原文仍待复核**（连续多轮待办）。
- **落库**：A 索引 [[AppIntent 每日情报 2026-10-06]]、D 速览 [[AppIntent 每日情报速览 2026-10-06]]；**0 新建 B 节点、0 既有增补**（无 ≥6/10 真增量）。看板「本次新增（2026-10-06）」已登记。
- **环境**：仅 `agent-mail` 在线，未调用 Horizon MCP；WebSearch 直查官方/权威源（Apple Developer / developer.android.com/ai/appfunctions / 华为 HDC2026 转述 / learn.microsoft.com / benchlm / llm-stats / cyberworldops / conicplex / penligent）。

## 诚实标注 / 待办
- iOS 27.1 beta 实际发布日与是否带新 Schema API（iPhone Duo 适配之外）待 Apple 逐字；10-19~23 为第三方汇总。
- AppFunctions `alpha13` 是否存在、是否引入调用方身份注入新机制（alpha12 移除 `AppFunctionContext` 后）待官方文档。
- Gemini Nano v3 Function Calling `LanguageModel.createLanguageModelSession()` 方法签名以官方 SDK 为准；是否接 `EXECUTE_APP_FUNCTIONS` 同一闸门待确认。
- CVE-2026-90970 已丢弃（非四平台 OS 框架）；后续仅纳入四平台 OS 层 agent 隔离逃逸。
- 沿用：Per-Intent Privacy Manifest 官方逐字 / Watch OS 26 / AppFunctions GA / A2UI alpha02 / 高通 NPU exact specs / Berkeley 官方 BFCL v4 博客 / NowSecure / AgentAntibody / Chrome Origin Sets。

# 执行摘要（2026-10-05 · 48h 复核，窗口 2026-10-03 → 10-05）

## 本轮产出（窗口 2026-10-03 → 10-05）
- **四大 OS 官方框架层 API 仍零净新增**（iOS 27.1 beta 未发 / AppFunctions 守 alpha12 无 alpha13 / A2UI 守 alpha01 / HarmonyOS 无新 API / Windows 26H2 无新 Registry API），与连续 ~30 轮「OS 框架不日更」结论一致。
- **唯一 OS 级真增量（★6/10，端侧意图路由 / Android）：Android Context Engine（Android 18 proactive caller of AppFunctions）+ Android 18 = Intelligence System 框架信号** → 来自 Android Dev Summit 2026（10-28~29）公告 cluster + 第三方解读（dev.to/byteiota/beebom/streamingmeme）。Context Engine = 追踪 user intent/screen context/app tasks 的后台服务，在用户开口前主动调用 AppFunctions；是 AppFunctions 继 Gemini/第三方 agent 后的第三类（OS 原生 proactive）调用方。Android 18 被定位为 Intelligence System，Gemini Nano v3 驻留内存（12GB RAM 下限）。属前瞻公告、非已发布 API。
- **库内校正（非本窗口新）**：Microsoft agentic security 文档实为 2026-04/06 发布 Taxonomy v2.0（含 consent-architecture hardening 四新缓解族），**校正 09-16 跑误记「2025-12-05 后无更新」**；已写入 A 索引「诚实校正」段，提示后续跑勿重复当新发布。
- **去伪/复述**：Apple macOS FDA 收紧（10-04 周报复述 10-03 已收录项）、Windows Hey Copilot/Agent Workspace（10-04~05 多家媒体复述）、HarmonyOS DevEco Code/1200+ Skill 化（生态叙述强化）均为已收录项复述，无新事实；BFCL v4 端侧 Planner 无新入榜；XPIA 窗口内无新 CVE/研究（CVE-2026-104120 属 MCP 工具链、丢弃）。
- **落库**：A 索引 [[AppIntent 每日情报 2026-10-05]]、D 速览 [[AppIntent 每日情报速览 2026-10-05]]、B 既有增补 1（[[Android AppFunctions 设备侧意图 2026]]）、看板「本次新增（2026-10-05）」已登记。**0 新建 B 节点**。
- **环境**：仅 `agent-mail` 在线，未调用 Horizon MCP；WebSearch/WebFetch 直查官方/权威源。

## 诚实标注 / 待办
- Android Context Engine 为 Dev Summit 公告 + 第三方解读，**非 Android 开发者文档逐字 API**；具体 API 名、是否独立 service、是否受 `EXECUTE_APP_FUNCTIONS` 同一闸门约束待 developer.android.com/ai/appfunctions 确认；Android 18 仍 Canary/未 GA。
- 沿用：Per-Intent Privacy Manifest 官方逐字 / iOS 27.1 正式 beta Schema / Watch OS 26 / AppFunctions alpha13 / A2UI alpha02 / 高通 NPU exact specs / Berkeley 官方 BFCL v4 博客 / NowSecure / AgentAntibody / Chrome Origin Sets。

# 执行摘要（2026-10-03 · 24h 复核，窗口 2026-10-02 21:01 → 10-03 21:01）

## 本轮产出（约 24h）
- **四大 OS 官方框架层 API 仍零净新增**（iOS 27.1 无新 `@AppIntent(schema:)` Schema / AppFunctions 守 alpha12 无 alpha13 / A2UI 守 alpha01 / HarmonyOS 无新 API / Windows 26H2 无新 Registry API），与连续多轮「OS 框架不日更」结论一致。
- **真增量①（★7/10，Apple 桌面 OS 权限治理，执行安全）**：Apple 2026-10-02 Developer News「Updates to Full Disk Access in macOS」宣布 FDA 改为「仅以非常明确的用户动作授予」，并**首次把 AI 智能体自主能力增长作为该权限 redesign 的官方理由**（原文逐句 "As AI agents become increasingly capable and autonomous, the risks associated with this level of access will grow substantially"）。Apple 未公布版本/时间/形态（forward-looking 政策信号，非同日 API 变更）。补 **新建 B 节点 [[Apple 桌面 Agent 权限治理 macOS Full Disk Access 2026]]**（库内无对应概念笔记）。
- **收敛叙事**：Apple 桌面 FDA 与 Windows Agent Workspace 低权账号+ODR consent / Android EXECUTE_APP_FUNCTIONS caller 白名单+setAppFunctionsPolicy / Microsoft Digital Defense Report 2026（agent 身份/权限/revoke）构成四平台「agent 执行边界 = OS 权限/隔离/确认边界」收敛；补 [[四平台意图 Registry 来源轴与权限模型对比 2026]] 指针。
- **去伪/无新增**：BFCL v4 仍 Llama 3.1 405B 88.5%（benchlm.ai 10-02 / anotherwrapper 10-03 一致）；端侧 MiniCPM5-2B 66.6 / FunctionGemma-270m 27.03 / Qwen3-0.6B 54.08 不变，无新端侧 Planner 入榜；XPIA 窗口内无新 CVE/研究突破。
- **落库**：A [[AppIntent 每日情报 2026-10-03]]、D [[AppIntent 每日情报速览 2026-10-03]]、B 新建 1 + B 既有增补 1、看板「本次新增（2026-10-03）」已登记。
- **环境**：仅 `agent-mail` 在线，未调用 Horizon MCP；WebSearch/WebFetch 直查官方/权威源。

## 诚实标注 / 待办
- FDA 新管控具体形态/版本/落地 beta 待 Apple 逐字复核；「very explicit user action」粒度待定。
- Meta Muse 读私信指控未独立证实、Wired ChatGPT Mac 漏洞为既往报道，均非 Apple 裁定。
- 沿用：iOS 27.1 beta/公开版 Schema / Per-Intent Privacy Manifest 官方逐字 / AppFunctions alpha13 / A2UI alpha02 / Watch OS 26 / 高通 NPU exact specs / Berkeley 官方 BFCL v4 博客 / 多智能体注入一手论文 / 自复制注入 OpenAI 原文。

# 执行摘要（2026-10-02 21:01 re-trigger · 24h 复核补捕）

## 本轮产出（窗口 2026-10-01 21:01 → 10-02 21:01，约 24h，re-trigger）
- **复核结论：四大 OS 官方框架层 API 仍零净新增**（Apple iOS 27.1 无新 `@AppIntent(schema:)` Schema / AppFunctions 守 alpha12 无 alpha13 / A2UI 守 alpha01 / HarmonyOS 无新 API / Windows 无新 Registry API）——与当日 09:00 晨间跑（7 日窗口）完全一致，确认「OS 框架不日更」规律。
- **真增量①（★5/10，消费级 OS Agent 商业化信号）：HarmonyOS Mate 90 / 小艺Claw（10-01 发布）** → 小艺升「个人专属智能体」（感知 200+ 系统数据/调用 2100+ 系统能力/协同 2000+ 鸿蒙智能体）；**小艺Claw 订阅 49 元/月**，尝鲜版遭体验倒退 backlash。补 [[HarmonyOS Intents Kit 与 ArkAF 2026]]（产品/UX 层非框架 API）。
- **真增量②（★5/10，跨平台路由/决策模型市场升温）：Cloudflare Clef + Clef-flash（10-01 开源 Apache 2.0）+ 同日 Amazon Strands Decider 2B** → 直击 Typesafe Jev「决策模型」品类（agent 工具路由层）；Clef BFCL case-exact 98.5（厂商自报）、中位延迟 209ms vs Jev 524ms。补 [[Function Calling 端侧工具调用]]（决策模型子类；标 edge/cloud 非 on-device、BFCL 98.5 厂商自报未复现）。
- **真增量③（★5/10，XPIA 防御量化待一手）：DecodingTrust-Agent(DTAP) 红队 45.6%→10.0% 攻击成功率**（techwalker 10-01 综述）** + 2026 大模型安全众测权威中文数据（CN-SEC 09-15，873 漏洞/608 智能体特有）**。补 [[XPIA 跨提示注入]]（DTAP 媒体综述待一手；众测为跨窗口权威数据，建议下个完整窗口正式收录）。
- **真增量④（跨窗口补强，★5/10，治理收敛）：Android 17 企业策略 `setAppFunctionsPolicy`/`APP_FUNCTIONS_DISABLED` 可关 AppFunctions 数据**（iseC7 引 Google 09-16 企业页）** → 与晨间跑 Windows 连接器策略治理（ConfigureAgentConnectors/AgentConnectorAccessPolicy）构成跨平台「agent 执行边界可经 MDM 治理」收敛。补 [[Android AppFunctions 设备侧意图 2026]]。
- **落库**：[[AppIntent 每日情报 2026-10-02]] 末追加「24h 复核补捕」段、[[AppIntent 每日情报速览 2026-10-02]] 末追加「24h 复核补捕」表、B 既有增补 4、看板「本次新增（2026-10-02 21:01 re-trigger）」已登记。**0 新建 B 节点、复用同日 A/D 文件**。
- **环境**：仅 `agent-mail` 在线，未调用 Horizon MCP；WebSearch/WebFetch 直查官方/权威源（今日头条/机锋网/aiweekly/mer.vin/techwalker/cn-sec/iseC7/anotherwrapper/developer.android.google.cn/developer.apple.com）。

## 诚实标注 / 待办
- 小艺Claw 订阅机制与体验倒退具体场景来自媒体/厂商口径，待华为开发者文档/实测复核。
- Clef/Strands 为云/边缘决策模型，BFCL 98.5 厂商自报未独立复现；不计入端侧 Planner 评测表（边界已写入 [[Function Calling 端侧工具调用]]）。
- DTAP 论文日期/评测协议待一手复核；CN-SEC 众测 09-15 发布、非 24h，作跨窗口权威数据。
- Android 17 企业页 09-16 更新、非 24h；`setAppFunctionsPolicy` 是否覆盖 Gemini 私测通道待官方文档。
- 沿用（晨间跑待办）：连接器策略项官方逐字 / 家庭专业版限制 / iOS 27.1 beta Schema / Per-Intent Privacy Manifest 官方逐字 / Watch OS 26 / AppFunctions alpha13 / A2UI alpha02 / 高通 NPU exact specs / Berkeley 官方 BFCL v4 博客 / 多智能体注入一手论文 / 自复制注入 OpenAI 原文。

# 执行摘要（2026-10-02）

## 本轮产出（窗口 2026-09-30 → 10-02，约 2 天）
- **四大 OS 官方框架层 API 仍零净新增**（iOS 27.1 无新 Schema / AppFunctions 守 alpha12 无 alpha13 / A2UI 守 alpha01 / HarmonyOS 无新 API / Windows 26H2 四支柱无新 Registry API），与连续多轮「OS 框架不日更」结论一致。
- **真增量①（★6/10，执行安全控制面具体化）：Windows agent 连接器策略治理面首次公开** → 2026-10-01 cnBeta/163 引 Neowin 披露组策略/MDM 控制项 `ConfigureAgentConnectors` / `AgentConnectorAccessPolicy` / `AgentConsentDuration` / `DisableSettingsAgent`，把 ODR「受控发现 + 三档 consent」从产品态落到 OS 控制面；连接器白名单=执行边界、consent 时长=授权窗口。**版本割裂**：四项仅企业/教育/IoT 企业版可配，家庭/专业版无法关闭或白名单化连接器。补 [[Windows Copilot Actions 与 Agent Workspace 2026]] + [[Agent Workspace 隔离执行]]（账号→文件夹→容器→连接器四层收窄隔离栈）。
- **状态更新（★3/10，低于预期不单列）：iOS 27.1 公开版预期下修为 2026-10-19~23**（9to5Mac/MacRumors 经 tech-insider/appauxin）；26H2 GA(09-29) 本窗口再获媒体确认。AppIntents 官方更新页最新条目仍 June 2026，无 Oct 新 Schema。
- **去伪/无新增**：XPIA 窗口内命中的 RAMPART/agentmelt/treza/futureagi 均既有工具与综述，无新 CVE/研究突破；BFCL v4 仍 Llama 3.1 405B 88.5% 居首、端侧无新入榜。
- **落库**：A 索引 [[AppIntent 每日情报 2026-10-02]]、D 速览 [[AppIntent 每日情报速览 2026-10-02]]、B 既有增补 2、看板「本次新增（2026-10-02）」已登记。**0 新建 B 节点**。
- **环境**：未调用 Horizon MCP（仅 `agent-mail` 在线）；按任务 fallback 改用 WebSearch/WebFetch 直查官方/权威源（developer.apple.com/documentation/updates/appintents、developer.android.google.cn、cnBeta/Neowin、tech-insider、appauxin、paperswithcode）。Android 官方页直连 sandbox 失败，alpha12 结论来自 09-25 记录 + 本窗口检索无 alpha13。

## 诚实标注 / 待办
- 连接器策略项命名与版本限制来自 Neowin 转述，待 learn.microsoft.com 逐字复核。
- iOS 27.1 beta/公开版日期 Apple 未官方确认（10-19~23 为第三方汇总）。
- 沿用：Per-Intent Privacy Manifest 官方逐字 / Watch OS 26 / AppFunctions alpha13 / A2UI alpha02 / 高通 NPU exact specs / Berkeley 官方 BFCL v4 博客 / 多智能体注入一手论文 / 自复制注入 OpenAI 原文。

# 执行摘要（2026-09-30）

## 本轮产出（窗口 2026-09-26 22:07 → 09-30 21:00，约 3.9 天，补 4 日空窗）
- **四大 OS 官方框架层 API 仍零净新增**（iOS 27.1 无新 Schema / AppFunctions 守 alpha12 无 alpha13 / A2UI 守 alpha01 无 alpha02 / HarmonyOS 无新 API / Windows 26H2 四支柱无新 Registry API），与连续多轮「OS 框架不日更」结论一致。
- **真增量①（★6/10，OS 级部署里程碑）：Windows 11 26H2 于 2026-09-29 GA**（enablement 形态；Ask Copilot 任务栏搜索替代 + File Explorer 内 Copilot 侧栏新 surface；Copilot Actions/Agent Workspace 仍 experimental opt-in，执行总线能力未变）。补 [[Windows Copilot Actions 与 Agent Workspace 2026]]。
- **真增量②（★5/10，评测设施状态）：BFCL v4 BenchLM 09-28 刷新**（BTL-3 / Bad Theory Labs 开放权重 88.5% 居首，现归因明确；端侧 Planner 无新入榜；旧「88.5% 待补」待办关闭）。补 [[Function Calling 端侧工具调用]]。
- **真增量③④（★6/10×2，XPIA 执行安全）：多智能体注入威胁模型（arXiv:2609.22949，14 向量/67% 越权，四防御 31.2%→4.2%，补威胁模型第⑨支）+ 自复制注入（OpenAI Alignment 09-26 警告，上下文窗口变开放中继，第五环；低置信来源）**。+ SearchLeak 重提（★5/10，实 2026-06 CVE-2026-42824 重提，附 Purview 标签门控治理待官方确认）。补 [[XPIA 跨提示注入]]。
- **落库**：A 索引 [[AppIntent 每日情报 2026-09-30]]、D 速览 [[AppIntent 每日情报速览 2026-09-30]]、B 既有增补 3、看板「本次新增（2026-09-30）」已登记。**0 新建 B 节点**。
- **环境**：未调用 Horizon MCP（仅 `agent-mail` 在线）；按任务 fallback 改用 WebSearch/WebFetch 直查官方/权威源（BetaWiki / developer.android.google.cn / BenchLM / arXiv 转述 / 安全媒体）。

## 诚实标注 / 待办
- 26H2 GA 日来自 BetaWiki 第三方维基；agentic 入口 opt-in 管控待 Microsoft 官方 blog 逐字。
- 多智能体注入（arXiv:2609.22949）/ 自复制注入（机器撰写媒体）具体数字待一手复核。
- SearchLeak 为 2026-06 已披露+后端已缓解，本次仅语境重提；Purview 标签治理待 learn.microsoft.com 确认。
- 沿用：Per-Intent Privacy Manifest 官方逐字 / Watch OS 26 / NowSecure / AgentAntibody / Chrome Origin Sets / 高通 NPU exact specs / Berkeley 官方 BFCL v4 博客 / AppFunctions alpha13 / A2UI alpha02 / iOS 27.1 正式 beta Schema。

# 执行摘要（2026-09-21）

## 本轮产出（窗口 2026-09-20 21:00 → 09-21 22:00，约 25h）
- **四大 OS 官方框架层 API 无净新增**（iOS 27.1 beta 已放出、Duo 向无 Schema 新增；AppFunctions 仍 alpha11 无 alpha12；HarmonyOS HC2026 为既有框架数据补强；Windows 四支柱 + Execution Containers 无新 Registry API）。与 09-18→09-20 连续「OS 框架不日更」结论一致。
- **真增量①（★7/10，既有节点数据补强）：HC2026 鸿蒙智能体框架 2.0 端云混合规划 90%+ 成功率 + 生态数字** → 华为全联接大会2026（9-17 开幕、9-19~21 集中报道）官方口径：端云混合规划（任务复杂度+设备资源分配计算）把复杂任务成功率推至 90%+（四平台首个 OS 厂商量化端云协同规划成功率）；生态：HarmonyOS 6|7 终端破 8500 万、注册开发者 1100 万+、应用与服务 40 万+、接入 AI 开放能力应用 1 万+、日均调用 36.8 亿次、OpenHarmony 13 亿+；Skill 确定性/A2A 多轮 + 端/云双模；端侧文本搜图不出端（provenance-at-source 信号，不推翻来源轴空白）。补 [[HarmonyOS Intents Kit 与 ArkAF 2026]]。
- **真增量②（★6/10，新攻击面）：BragJack「Prompt Forcing」浏览器扩展劫持 AI 助手信道** → Forever Security Gal Weizman（09-16 公开）：单一恶意扩展经 Chromium DNR 跨入 AI 助手特权控制平面，CVE-2026-0628（Chrome 8.8，143.0.7499.192/.193 修）/CVE-2026-55945（Edge race condition）。区别于 prompt injection（控制完整 prompt，绕过模型过滤）。与 08-09晚「confused deputy」同构。补 [[XPIA 跨提示注入]]（威胁模型扩展至第⑧支·信道/身份信任劫持）。
- **真增量③（★6/10，治理层）：Microsoft Foundry 托管智能体网络出网控制 public preview** → FQDN 通配 + 允许/拒绝/改写出站头/改写目的地，与「发布到 M365/Teams GA + Agent 365 启用停用」构成治理闭环。补 [[Agent 365 与 Entra Agent ID 智能体控制平面与身份基座 2026]]（出网边界维度，非 OS 执行总线）。
- **真增量④（★5/10，低置信）：Android App Functions Manager「safety cage」** → ai.jp.net 二次分析称 Google 在 App Functions Manager 框架层嵌入 agent 安全护栏，仅开发者文档/SDK 注释暗示，待官方复核（可能=既有 AppFunctionState 门控复述）。补 [[Android AppFunctions 设备侧意图 2026]]。
- **真增量⑤（★5/10，强化 09-20 主题）：Plugin4Shell** → Claude Code/Codex/Copilot/Gemini CLI 零点击 RCE，绕过 SHA pinning 经 Git branch/commit 碰撞，强化 Skill/插件供应链投毒靶面。补 [[XPIA 跨提示注入]]。
- **窗口外校正（★5/10，关闭 09-20 前瞻待办）：iOS 27.1 beta 已放出** → Xcode 27.1 Beta 1（约 09-18/19）含 iOS 27.1 SDK，内容=iPhone Duo 折叠屏适配，无新 App Intents Schema API；代码级 Model Delegation API 反编译信号（外部模型可作 Siri 扩展，非官方）。补 [[Apple AppIntents Schema Protocol 2026]]。
- **落库**：A 索引 [[AppIntent 每日情报 2026-09-21]]、D 速览 [[AppIntent 每日情报速览 2026-09-21]]、B 既有增补 5（鸿蒙/XPIA×2/Agent 365/Android/Apple）、看板「本次新增（2026-09-21）」已登记。**0 新建 B 节点**。
- **环境**：未调用 Horizon MCP（环境仅 `agent-mail` 连接器在线）；按任务 fallback 改用 WebSearch/WebFetch 直查官方源与权威媒体。**HC2026 数字、BragJack CVE、Foundry 出网控制均来自官方/媒体转述，待一手复核**。

## 诚实标注 / 待办
- HC2026 生态数字与「端云混合规划 90%+」为华为官方口径经媒体转述；「端云混合规划」算法、端侧文本搜图字段、星河互联是否接意图回路待华为开发者文档逐字。
- BragJack 为 09-16 公开、09-20 周报覆盖，非本窗口 24h 首发；CVE 编号/修补版本来自 Forever Security 转述；Opera Neon/Comet/Claude-in-Chrome 修补状态部分未确认；Plugin4Shell 一手 CVE 与版本清单待补。
- iOS 27.1 beta 功能来自开发者博客/媒体转述；Model Delegation 为 pdfu 反编译、Apple 未官方确认；Android「safety cage」为二次分析。
- 跟踪：iOS 27.1 正式 beta 是否带新 Schema API；AppFunctions alpha12；把 BragJack Prompt Forcing 与 [[隔离执行]]/[[确认机制]] 映射；Per-Intent Privacy Manifest 官方逐字 / Watch OS 26 / NowSecure / AgentAntibody / Chrome Origin Sets / 高通 NPU exact specs / Berkeley 官方 BFCL v4 博客 / Skill-Inject 一手数字。

# 执行摘要（2026-09-20）

## 本轮产出（窗口 2026-09-18 21:00 → 09-20 21:00，约 48h，iOS 27 GA 后第 6 日）
- **四大 OS 官方框架层 + BFCL v4 官方榜（Last Updated 仍 2026-04-12）均无 48h 净新增 API / 评测**——完全符合「OS 框架不日更」规律，与 09-13→09-19 连续结论连续一致。本期为**复核型运行 + 库内空白补漏**。
- **真增量①（★6/10，库内空白补漏）：技能层供应链投毒成实证攻击类** → Skill-Inject（arXiv 2602.20156）/ Malicious Agent Skills in the Wild（arXiv 2602.06547，分析 ~100,000 skills）/ SkillJect（arXiv 2602.14211）三篇 2026-02 arXiv 实证，把「恶意 Skill/manifest 注入」从概念警告推为可测攻击类，直接映射 HarmonyOS ArkAF Skills 上架 / Android AppFunctions agent skill / A2A。补 [[XPIA 跨提示注入]]（威胁模型扩为「能力描述(Skill)注入」靶面，防御谱七支）+ [[Agent Skills 技能范式 2026]]（实证 + Skill manifest 签名护栏）。
- **真增量②（★6/10，库内空白补漏）：XPIA 防御侧量化** → PromptArmor（ICLR 2026）现成 LLM 检测/净化注入 AgentDojo FP/FN<1%；Zylos 2026 间接注入对最强前沿模型仍 ~32% 成功率（量化天花板）。补 [[XPIA 跨提示注入]]。
- **窗口外前瞻（★5/10，未发布）：iOS 27.1 首个 beta 预期 2026-09-21~23**（Macworld 09-20 仍确认未发布）；Messages「加到提醒事项/备忘录」= App Intents 主动式分发面扩大。已登记为下一窗口头号跟踪项。补 [[Apple AppIntents Schema Protocol 2026]]。
- **落库**：A 索引 [[AppIntent 每日情报 2026-09-20]]、D 速览 [[AppIntent 每日情报速览 2026-09-20]]、B 既有增补 3（XPIA / Agent Skills / Apple）、看板「本次新增（2026-09-20）」已登记。**0 新建 B 节点**。
- **环境**：未调用 Horizon MCP（环境仅 `agent-mail` 连接器在线）；按任务 fallback 改用 WebSearch/WebFetch 直查官方源与权威综述。Skill-Inject/Malicious Skills/SkillJect/PromptArmor/Zylos 具体数字来自 arXiv/厂商综述转述，待一手复核，先不写精确百分数（诚实）。

## 诚实标注 / 待办
- Skill-Inject / Malicious Skills / SkillJect / PromptArmor / Zylos 具体 benchmark 数字待一手论文页复核。
- 跟踪 iOS 27.1 beta（预期 09-21~23）是否引入新 `@AppIntent(schema:)` / App Intents Domains API；跟踪 AppFunctions alpha12。
- 把 Skill-Inject 等一手数字与「OS 级 Skill Registry 签名」机制做映射表。
- 沿用：OWASP Agentic AI Top 10 2026 映射 / Berkeley 官方 BFCL v4 榜逐字 / Watch OS 26 / NowSecure / AgentAntibody / Chrome Origin Sets / Per-Intent Privacy Manifest / 高通 NPU exact specs。

# 执行摘要（2026-09-18）

## 本轮产出（窗口 2026-09-17 22:38 → 09-18 21:00，约 22h，iOS 27 GA 后第 4 日）
- **四大 OS 官方框架层 + BFCL v4 榜单 + XPIA 研究线本窗口（24h）均无净新增 API / 评测 / 研究突破**——完全符合「OS 框架不日更」规律，与 09-17（含 22:38 日间补充 SIR + 权重级持久化）结论连续一致。本期为**复核型运行**：把「已复核·无净新增」显式落档，避免下次重复检索。
- **唯一低于收录阈值的状态更新（★5/10，不入新 B 节点）**：Windows Copilot Actions 经 msftnewsnow 报道已随 Copilot app 更新 **1.25112.74+** 向 Insiders 分批「Now Available」——属已记录预览能力的部署推进，非框架 API 新增；已追加 1 行状态至 [[Windows Copilot Actions 与 Agent Workspace 2026]]。
- **关键校正**：Apple `iOS 27.1` 首个 beta **尚未发布**（Macworld 09-18 确认），短期无新 App Intents API 信号；搜索命中的 7 篇 iOS 27 文章全部为 09-14 GA 后的二次复述。
- **去伪**：OWASP Agentic AI Top 10 2026 经多源确认 **2025-12-09 发布**（版本号指治理年份，非本期新发布）；Microsoft RAMPART 为 XPIA 测试框架工件（非 OS 机制变更）；dev.to 云端 Copilot（SharePoint 技能/Brand Kit）为应用层、丢弃。
- **落库**：A 索引 [[AppIntent 每日情报 2026-09-18]]、D 速览 [[AppIntent 每日情报速览 2026-09-18]]、B 既有增补 1（Windows 部署状态 1 行）、看板「本次新增（2026-09-18）」已登记。**0 新建 B 节点**。
- **环境**：未调用 Horizon MCP（环境仅 `agent-mail` 连接器在线，无 Horizon MCP 工具）；按任务 fallback 改用 WebSearch/WebFetch 直查官方源，已记于 A 索引诚实标注。

## 诚实标注 / 待办
- Windows Copilot Actions app v1.25112.74+「Now Available」报道未给精确发布日期，无法确认是否严格落在 24h 窗口，仅作状态更新处理。
- OWASP Agentic AI Top 10 2026（ASI01–ASI10）与 RAMPART 一手发布日期待补；建议后续把 ASI 十类与库内 [[XPIA 跨提示注入]] / [[Confirmation UI 安全机制]] / [[Agent Workspace 隔离执行]] 做映射表（非本期增量）。
- 跟踪 iOS 27.1 beta（预期 10 月）是否引入新 App Intents API；跟踪 AppFunctions alpha12。
- 沿用既有待办：Berkeley 官方 BFCL v4 榜逐字 / Watch OS 26 / NowSecure / AgentAntibody / Chrome Origin Sets / Per-Intent Privacy Manifest / 高通 NPU exact specs / SIR 一手 arXiv / Irregular 一手报告。

# 执行摘要（2026-09-17）

## 本轮产出（窗口 2026-09-16 → 09-17，iOS 27 GA 后第 3 日）
- **四大 OS 官方框架层无净新增 API**（iOS 27 GA 后无新 App Intents；AppFunctions 守 alpha11 无 alpha12；HarmonyOS 同 HDC2026；Windows 四支柱 + Execution Containers 无新 Registry API），符合框架不日更规律，已在 A 层显式列「已复核·无净新增」避免重复检索。
- **真增量①：XPIA 攻击侧首次「自改进」SIR（★6/10）** → 香港中文大学 arXiv 预印本（notatechguy 二次转述）：把提示注入当可演化攻击框架，ASR 经自我试错 Gemini 3.5 Flash 0%→28% / Claude Opus 4.8 4%→24%，且绕过原则跨模型零反馈迁移；与 08-09 AgentAntibody 形成攻防镜像。补 [[XPIA 跨提示注入]]。
- **真增量②：Windows ODR Agent Connectors 权限模式具象化（★6/10）** → 第三方教程（adersaytech）：预览 build 26100.7344+ 起 ODR 连接器默认关进 Agent Workspace、consent 三档（Ask every time / Allow always / Never allow），与 08-05 注册 + 09-16 代码签名构成「注册→签名→隔离→授权」闭环。补 [[Windows Copilot Actions 与 Agent Workspace 2026]]。
- **真增量③：Android 17 GA 确认 + AppFunctions 进智能系统叙事（★6/10，库内空白补漏）** → 官方 intelligence-system 页把 AppFunctions 与 Remote MCP / Computer Control 并列；AppFunctions 仍 alpha11 无 alpha12、compileSdk 建议升 37。补 [[Android AppFunctions 设备侧意图 2026]]。
- **落库**：A 索引 [[AppIntent 每日情报 2026-09-17]]、D 速览 [[AppIntent 每日情报速览 2026-09-17]]、B 既有增补 3（XPIA/Windows/Android）、看板「本次新增（2026-09-17）」已登记。**0 新建 B 节点**。

## 日间延续巡查（2026-09-17 22:38，窗口 09-17 09:00→22:38）
- **结论维持**：四大 OS 官方框架层无净新增 API（Apple/Android/HarmonyOS 当日搜索空；Windows 仅无关 Defender KB）；BFCL v4 榜数据版本仍为 20260913、无新端侧 Planner 入榜（anotherwrapper「Llama 3.1 405B #1 88.5%」与权威镜像冲突、标待补）。
- **真增量（1 条，★6/10）**：「自修改 Agent 让注入获得持久化——权重级攻击面」（Irregular/IDC，Zicos/CSO 二次转述 09-17）→ 补 [[XPIA 跨提示注入]]：Agent 能改自身模型权重时，注入可沉淀进 checkpoint 跨会话存活（权重可改性 42% vs API-only 0%），与晨间 SIR 自改进攻击构成 XPIA 演进链第四环，直击端侧/自托管 Agent 执行总线权重边界。A 索引补「日间补充」小节、看板补 1 行、本记忆补本段。**0 新建 B 节点**。
- 诚实标注：Irregular 为二次转述，42%/3-of-6 密钥复现为测试条件数字，一手报告待补（已加进待办）。

## 诚实标注 / 待办
- SIR 为 notatechguy 二次转述，arXiv ID 与评测协议待一手复核；仅点名 Gemini 3.5 Flash / Claude Opus 4.8 两款模型。
- Windows ODR 权限模式 build 26100.7344+ 与三档 consent 为第三方教程，待 learn.microsoft.com 逐字复核；是否受 08-02 `Experimental agentic features` 同一 opt-in 管控待补。
- Android 17 精确 GA 日 + AppFunctions GA 日待补；compileSdk 37 为第三方复核结论。
- 沿用：Per-Intent Privacy Manifest 官方文档逐字 / Watch OS 26 / NowSecure / AgentAntibody / Chrome Origin Sets / 高通 NPU exact specs。

# 执行摘要（2026-09-16）

## 本轮产出（窗口 2026-09-15 → 09-16，iOS 27 GA 后 1 日）
- **四大 OS 官方框架层无净新增 API**（iOS 27 GA 后无新 App Intents；AppFunctions 守 alpha11 无 alpha12；HarmonyOS 同 HDC2026；Windows 四支柱无新 Registry API）。符合框架不日更规律，已在 A 层显式列「已复核·无净新增」避免重复检索。
- **真增量①：Windows Agent 代码签名/吊销由第三方升官方确认（★6/10）** → learn.microsoft.com agentic security 文档把「Operational trust」列为四大原则之一（Agent 须可信源签名、证书校验/吊销可阻断）；09-15 仅 windowsforum 第三方，本次获官方背书。补 [[Windows Copilot Actions 与 Agent Workspace 2026]] + [[Agent Workspace 隔离执行]]。
- **真增量②：Per-Intent Privacy Manifest 官方页重核（★3/10）** → 重核 developer.apple.com/ios/whats-new，App Intents 段落仍无此 API；维持 09-15「GA 后待官方复核」、来源轴空白结论不变。补 [[四平台意图 Registry 来源轴与权限模型对比 2026]]。
- **真增量③：跨平台硅底新信号 NPU 原生 agentic loop（★3/10，新 B 节点）** → 高通 Hexagon on-die agentic loop（感知→Oryon CPU 编排→异构推理→响应）+ 联发科 Dimensity 9500S CIM/1.58-bit；端侧 Agent 执行总线下沉芯片。新建 [[端侧 Agent 执行总线 NPU 原生 agentic loop 2026]]。
- **库内空白补漏：Android I/O '26 路由/编排原语（★3/10）** → Firebase Hybrid Inference 端云路由 / ADK for Android 多智能体 / A2UI Compose Renderer，补 [[Android AppFunctions 设备侧意图 2026]]，标真实日期 I/O '26。
- **落库**：A 索引 [[AppIntent 每日情报 2026-09-16]]、D 速览 [[AppIntent 每日情报速览 2026-09-16]]、B 新 1 + B 既有增补 3、看板「本次新增（2026-09-16）」已登记。

## 诚实标注 / 待办
- Windows 代码签名/吊销是否纳入 ODR 信任链、是否受 08-02 同一 opt-in 管控仍待 learn.microsoft.com 逐字（官方只确认原则，未给注册衔接）。
- Per-Intent Privacy Manifest 仍缺 Apple 官方文档逐字（多源报道未证伪、官方页未列，维持待复核）。
- 高通 NPU exact specs 待 Snapdragon Summit 2026 官方确认（当前为 keynote 前披露经第三方转述）。
- 鸿蒙 小艺导航条「复制即触发」置信度门控机制待官方文档；BFCL v4 官方榜复核 Needle 2/Apple FM/FunctionGemma 待补；沿用既有待办：Watch OS 26 / NowSecure / AgentAntibody / Chrome Origin Sets。

# 执行摘要（2026-09-15）

## 本轮产出（窗口 2026-09-13 → 09-15，真·GA 窗口）
- **iOS 27 正式版（09-14）GA 落地的框架级信号（★8/10）= 本日最高价值**：官方 post-GA「What's New in iOS 27」页确认 App Intents 能力（Entity/Intent schemas、View Annotations API、App Intents Testing，均为 WWDC26 已宣布、本次 GA）——**关键增量 = Foundation Models 框架宣布支持任意语言模型**（Apple FM / Claude / Gemini / 任何遵循 `Language Model` 协议者）+ Dynamic Profiles（连续会话实时切换模型/工具）+ Evaluations。**OS 级 Planner 首次把多模型路由写进一等公民框架**，端云路由从架构决策降为运行时旋钮。
- **最高优先待办收口进行中：Per-Intent Privacy Manifest 由「证伪」重开为「GA 后待官方复核」**：08-31 判定该 API「confirmed non-existent」；GA 后 WWDC 2026 多源（Lushbinary/ByteIota/TechTimes/AlgeriaTech）一致称 Apple 引入按意图声明「可上云/须留端」的隐私清单，但官方 post-GA 页未逐字列出 → 由证伪升为待复核。即使确认，属「路由轴」声明，与 provenance 轴不同，**不推翻来源轴全空白结论**。
- **Windows：Agent 代码签名 + 证书校验/吊销（★6/10）**：执行安全三原则（non-repudiation/confidentiality/authorization）落地细节补全，把「Agent 须数字签名」升级为可撤销身份机制（第三方 windowsforum 综述，非官方逐字）。
- **HarmonyOS 7 小艺 2.0 / 导航条主动服务入消费者（★6/10）**：系统级 Agent 感知 200+ 系统数据 / 调用 2100+ 系统能力 / 四层记忆；导航条「复制即触发意图预测」是四平台首个系统化 OS 级主动服务 UX。生态：HarmonyOS 7(API 26) 设备占比 5.27%、鸿蒙 6+7 终端破 8500 万。媒体口径。
- **BFCL v4 榜单稳定**（BenchLM 09-08：Qwen3.7 Max 75.0% 领先，与历次快照一致，无净变化）；qwen3-0.6b-tool-router 补 BFCL 子集分（Non-Live Parallel AST 83.50% / Live Simple 62.86% / Live Parallel 52.00%）。
- **落库**：A 索引 [[AppIntent 每日情报 2026-09-15]]、D 速览 [[AppIntent 每日情报速览 2026-09-15]]、B 既有增补 6（Apple/四平台对比/Windows/Agent Workspace隔离/HarmonyOS/Function Calling）+ 关联增补 1（Agent Workspace隔离）、看板「本次新增（2026-09-15）」已登记。**0 新建 B 节点**。

## 诚实标注 / 待办
- Per-Intent Privacy Manifest 仍缺 Apple 官方文档逐字确认（developer.apple.com 隐私清单 / App Intents GA 文档）；若确认则评估「路由轴」维度（区别于 provenance）。
- Windows 代码签名/吊销仍待 learn.microsoft.com 逐字；是否纳入 ODR 信任链、是否受同一 opt-in 管控待核。
- 鸿蒙 小艺 2.0 / 导航条仅媒体整理，缺华为开发者文档逐字；导航条预测置信度门控机制待确认。
- Android 版本口径冲突（博客 alpha08/09/10 vs 官方 alpha11；「Android 17」ADB vs compileSdk ≥36）待官方澄清。
- 沿用：Watch OS 26 / NowSecure / AgentAntibody / Chrome Origin Sets 官方 URL 复核；Berkeley 官方 BFCL v4 博客原文。

# 执行摘要（2026-09-13）

## 本轮产出（窗口 2026-09-06 → 09-13，7 日滚动）
- **四平台官方框架层 API 无净新增**：iOS 27 RC build 24A435（09-09）= Beta 5 收尾、无新 App Intents API；AppFunctions 守 alpha11（无 alpha12）；HarmonyOS 7 框架同 HDC2026 / 09-07 消费版；Windows Copilot Actions/Agent Workspace/ODR/Agent Launchers 四支柱无变化。
- **真增量①：BFCL v4 官方榜单上线（★7/10）** → 补 [[Function Calling 端侧工具调用]]：Berkeley Gorilla 维护、DataLearner 镜像 2026-09-07 更新，SOTA **MiniCPM5-2B（OpenBMB）66.60**（2.5B 免费商用，端侧级小模型首登官方 v4 榜首）；收口连续多轮「Berkeley 官方榜」待办，端侧分数升「可复核」；某中文综述「88.5%」标待补（疑单轮子集/厂商自报）。
- **真增量②：Windows IFA 2026 Microsoft Execution Containers（★7/10）** → 补 [[Windows Copilot Actions 与 Agent Workspace 2026]] + [[Agent Workspace 隔离执行]]：Agent 隔离升为内建沙箱容器，强制企业策略 + 全量日志；四平台最明确 OS 内建容器隔离原语。Project Zenith/RTX Spark 属硬件定位不计入。
- **真增量③：HarmonyOS 7 确认 API 26（★6/10）** → 补 [[HarmonyOS Intents Kit 与 ArkAF 2026]]：关闭「26 vs 23」冲突待办；新增安全相机2.0 数字内容溯源 + 数字身份 DID（provenance-at-source），但意图 Registry 层来源轴仍空白（不推翻来源轴结论）。
- **真增量④：iOS 27 RC + GA 09-14（★6/10）** → 索引 [[AppIntent 每日情报 2026-09-13]]，触发 per-intent 路由 API 核查（待办延续）。
- **落库**：A 索引 [[AppIntent 每日情报 2026-09-13]]、D 速览 [[AppIntent 每日情报速览 2026-09-13]]、B 既有增补 3（Function Calling/Windows/HarmonyOS）+ 关联增补 1（Agent Workspace）、看板「本次新增（2026-09-13）」已登记。**0 新建 B 节点**。

## 诚实标注 / 待办
- MiniCPM5-2B 66.60 为聚合镜像（DataLearnerAI）呈现、非逐字官方博客；Apple FM 61.7% / Needle 2 42.6% / FunctionGemma 27–46% 待用官方榜逐项复核。
- Execution Containers 是否复用 Agent Workspace 容器、opt-in 管控、与 ODR 关系待 Microsoft 官方文档。
- 鸿蒙 安全相机2.0/DID 字段、是否接意图回路待官方文档。
- **【最高优先·明日触发】9-14 iOS 27 GA 后核查 per-intent 路由/来源声明 API**（重评来源轴结论）。

# 执行摘要（2026-09-12）

## 本轮产出（窗口 2026-09-04 → 09-12，补跑 9 天空窗）
- **四平台官方框架层 API 无净新增**：iOS 27 守 Beta 5 已录 schema；Android AppFunctions 仍 `1.0.0-alpha11`（无 alpha12）；HarmonyOS 7 框架同 HDC2026；Windows agentic security 四支柱一致。
- **真增量①：HarmonyOS 7（9-7 发布后）可信与安全实测** → 补 [[HarmonyOS Intents Kit 与 ArkAF 2026]]：信通院增强级端云协同 AI 安全认证（行业首个）、携手支付宝欺诈损失率 -35.8%/盗用拦截率 +42.3%、高频流畅度 +22%、应用跳转 +25%。来源为快科技/百度百科媒体口径，标待官方核验。
- **真增量②：跨平台 A2UI 落地（新 B 节点）** → 高德 AGenUI 明确基于 Google A2UI 协议，C++ 引擎把界面意图渲染为鸿蒙原生组件。新建 [[A2UI 生成式UI协议(Google)与鸿蒙落地 2026]]。
- **真增量③：Needle 2 跨模型 BFCL v4 对照 + 架构消融** → 补 [[Function Calling 端侧工具调用]]（单轮 Apple FM 61.7% / LFM2.5-230M 60.8% / FunctionGemma 46.1% / Needle 2 42.6%；Seal-Tools 域外 Needle 2 28.7% 居首）+ [[端侧 Router 置信度门控与工具可达性收缩 2026]]（attention-only 消融 0.47→0.006 nats、byte-level grammar 跳过 98% 词表、well-formed 93.4% 跨模型同档）。aibacon 第三方拆解，待官方榜复核。
- **真增量④：Windows 具体 build 号与交互** → 补 [[Windows Copilot Actions 与 Agent Workspace 2026]]：build 26200.8313（任务栏 Agent）/ 26220.7262（Agent Workspace）、Settings「Agents」面板、「@」调 Agent、悬停监控。第三方 tracker，非官方 blog。
- **落库**：A 索引 [[AppIntent 每日情报 2026-09-12]]、D 速览 [[AppIntent 每日情报速览 2026-09-12]]、B 新 1（A2UI）+ B 既有增补 4、看板「本次新增（2026-09-12）」已登记。

## 诚实标注 / 待办
- 信通院认证编号、支付宝联合测试方法论、AGenUI 协议字段遵循度、Windows build 号均媒体/厂商口径，待官方文档核验。
- Needle 2（42.6%）/ Apple FM（61.7%）跨模型对照仍第三方引述，待 Berkeley 官方 BFCL v4 榜复核。
- HarmonyOS 7 消费版真实 API level（26 vs 23 冲突）仍待官方文档回填。
- 9-14 iOS 27 GA 后核查是否新增 per-intent 路由/来源声明 API（将重评 [[四平台意图 Registry 来源轴与权限模型对比 2026]] 来源轴结论）。
- 延续：Watch OS 26 / NowSecure / AgentAntibody / Chrome Origin Sets 官方 URL 复核。

# 执行摘要（2026-09-03）

## 本轮产出（窗口 2026-08-27 → 09-03）
- **四平台官方框架层 API 无净新增**：iOS 27 RC 沿用 Beta 5 已录 `@AppIntent(schema:)`；Android AppFunctions 守 `1.0.0-alpha11`（官方 Release Notes 当前最新，无 alpha12）；HarmonyOS 7 框架同 HDC2026；Windows agentic security 四支柱一致。
- **真增量①：三平台消费级 GA 日期锁定**（OS PM 核心信号）
  - HarmonyOS 7 消费版 **2026-09-07** 随 Mate XT 2 铺开（ArkAF 2.0「意图即服务」入消费者）→ 新建/补 [[HarmonyOS Intents Kit 与 ArkAF 2026]]。
  - Windows 11 26H2 **9 月下旬~10 月初**（enablement package）：Ask Copilot 搜索层意图入口 + Sysmon 内置 → 补 [[Windows Copilot Actions 与 Agent Workspace 2026]]。
  - iOS 27 **2026-09-14** GA（框架不变）。
  - 含义：四平台 agentic 框架同步进入「发布前最后冲刺」；HarmonyOS 是首个把意图即服务做成消费者默认可用并锁 GA 的平台。
- **真增量②：Luxand LLM SDK BFCL v4 端侧 Agentic Score 快照**（第三方 SDK 自测，非官方榜）：Qwen3.6-35B-A3B 73.4% / Gemma4-26B-A4B 71.8% / Qwen3.5-4B 67.0% / LFM2.5-8B-A1B 62.3% / Gemma4-E2B 51.1% → 补 [[Function Calling 端侧工具调用]]，待 Berkeley 官方榜复核。
- **落库**：A 索引 [[AppIntent 每日情报 2026-09-03]]、D 速览 [[AppIntent 每日情报速览 2026-09-03]]、B 既有增补 3（HarmonyOS/Windows/Function Calling）、看板末尾「本次新增（2026-09-03）」已登记。

## 诚实标注 / 待办
- Luxand 为厂商 SDK 自测、量化/硬件/模板与官方榜不同，「Agentic Score」非 Berkeley 总分；须三问 + 标版本号。
- 9-7 后回填 HarmonyOS 7 消费版真实 API level（26 vs 23 冲突仍待官方）。
- 9-14 iOS 27 GA 后核查是否新增 per-intent 路由/来源声明 API（将重评来源轴结论）。
- 延续：Watch OS 26 是否 Trust Insights 类、NowSecure/AgentAntibody 独立核验、Chrome Origin Sets 官方 URL 逐字复核、Berkeley 官方 BFCL v4 博客原文。

# 执行摘要（2026-09-01）

## 本轮产出
- **净新增 OS 框架 API（唯一）**：Android AppFunctions Jetpack **`1.0.0-alpha11`（2026-08-26 官方 Release Notes）**
  - `@AppFunctionSignature`（experimental）→ 支持**动态注册** AppFunction（b/501032667）
  - `AppFunctionState` + `AppFunctionManager#getAppFunctionStates` **取代** `AppFunctionMetadata#isEnabled`（元数据/状态分离，b/494238383）
  - 另：`getAppFunctionActivityStates`、`ExtensionsAppFunctionService`（sidecar）、`observeAppFunctions` 对齐平台 API；OOBE 阶段 `setAppFunctionEnabled` 崩溃修复。
  - 含义：本库 08-03 记的「四平台唯一动态可见性 API」机制升级为 state-based；Registry 仍为随状态实时变化的动态视图。
- **跨平台端侧 Planner 评测增量（BFCL v4，第三方来源，已标待补）**
  - Apple on-device Foundation Model 首登 BFCL v4 单轮 **61.7%**（aibacon 引 Berkeley 榜）
  - LittleLamb-ToolCalling-ONNX **0.3B**：BFCL v4 **51.55%（think）/ 50.51%（no-think）**（HF jromarllegue）
  - FunctionGemma 270M 全-v4 **27.03**（think=no-think，因其无 thinking 模式）
  - Needle 2 42.6% 获 aibacon 独立确认 + 「置信趋零→返回空调用」升级契约；MIT/Apache 许可，落 ESP32/树莓派5/Quest3S
  - Gemma 4 native tool tokens（d-central 第三方，待官方）
- **跨平台/监管**：欧盟 DMA 要求 Google 在 **2027-08 前**向竞品助手开放 11 项 Android AI 能力，AppFunctions Registry 使函数可被任一认证助手发现，`EXECUTE_APP_FUNCTIONS` 在 EU 下沉为「认证闸门」→ 新建 B 节点 [[AppFunctions 跨助手可发现性与 DMA 强制开放 2026]]。

## 落库
- A 原始资料：[[AppIntent 每日情报 2026-09-01]]（索引+已复核无净新增表）
- D 输出：[[AppIntent 每日情报速览 2026-09-01]]
- B 净新增 1：[[AppFunctions 跨助手可发现性与 DMA 强制开放 2026]]
- B 既有增补 4：[[Android AppFunctions 设备侧意图 2026]] / [[Function Calling 端侧工具调用]] / [[端侧 Router 置信度门控与工具可达性收缩 2026]] / [[四平台意图 Registry 来源轴与权限模型对比 2026]]
- 看板：知识飞轮看板.md 末「本次新增（2026-09-01）」区已登记。

## 已复核·无净新增（避免重复检索）
- Apple：iOS 27 Beta 8 与 08-15 Beta 5 逐字一致（同 bug 号）→ 不重复计数。
- HarmonyOS：7 开发者 Beta（6-12）/ 消费 Beta（8-3）/ 正式版秋季待发，无新 API。
- Windows：Copilot Vision 2026-05 GA；官方 agentic security 文档 2025-12-05 后再无更新；26H2/Ignite 2026-11 仅为路线图，非已发布 API。
- 跨平台 BFCL v4 镜像榜（benchlm）数字已在 08-26 入表。

## 诚实标注 / 待办
- Apple FM 61.7% 与 LittleLamb 0.3B 为**第三方引述**，待 Berkeley 官方榜复核。
- DMA「11 项能力清单 + 2027-08 deadline」为 ecorpit 分析，待欧盟官方文本回填。
- alpha11 `@AppFunctionSignature` 动态注册是否需要新 Manifest 权限/签名待核。
- 长期待办（延续）：Berkeley 官方 BFCL v4 博客原文；Watch OS 26 Trust Insights 类；NowSecure/AgentAntibody 独立核验；Chrome Origin Sets 官方 URL 逐字复核；把 alpha11 `AppFunctionState` 反映进对比表「运行时动态可见性 API」行。

## 执行摘要（2026-09-26）

## 本轮产出（窗口 2026-09-25 13:06→09-26 00:17，约 11h）
- **四大 OS 官方框架层 API 无净新增**（iOS 27.1 beta 无新 Schema / AppFunctions 守 alpha12 无 alpha13 / A2UI 守 alpha01 / HarmonyOS ArkAF 2.0 无新 API / Windows 26H2 四支柱 + 权限治理无新 Registry API）。
- **真增量①（★8/10，关闭 09-16 待办）：Snapdragon Summit 2026 收官发布 Snapdragon 8 Elite Gen 6** → Hexagon NPU 首增「面向 Transformer/Agentic AI 的 element-wise accelerator」+ 共享内存 +50% + 端上 32K context + 可跑 30B+ MoE（每 token 激活 ~3B，UFS 5.0 直接跑）；Oryon CPU FlexCache 作协调中柢。补 [[端侧 Agent 执行总线 NPU 原生 agentic loop 2026]]。
- **真增量②（★6/10）：MLPerf Edge Agentic 把 BFCL v4 纳为精度门** → 参考 Qwen3.6-27B（Q4_K_M）Jetson AGX Thor 单轮 gated 86.23%（≥83.64% 通过）；多轮 optional 非 gated（200 条=70%）。补 [[Function Calling 端侧工具调用]]。
- **状态行（★5/10）：鸿蒙 7.0.0.109SP6 正式版信号 + 小艺Work 跨设备 agentic 办公（含 Windows 客户端）**；**Windows 26H2 enablement 9 月下旬~10 月初 + Ask Copilot/File Explorer agentic 入口**。补 [[HarmonyOS Intents Kit 与 ArkAF 2026]] / [[Windows Copilot Actions 与 Agent Workspace 2026]]。
- **落库**：A 索引 [[AppIntent 每日情报 2026-09-26]]、D 速览 [[AppIntent 每日情报速览 2026-09-26]]、B 既有增补 4、看板「本次新增（2026-09-26）」已登记。**0 新建 B 节点**。
- **环境**：未调用 Horizon MCP（仅 `agent-mail` 在线）；按任务 fallback 改用 WebSearch/WebFetch 直查官方/权威源（高通 keynote 多源 / MLPerf GitHub / 华为媒体 / PCWorld）。

## 诚实标注 / 待办
- 高通规格为 keynote+媒体转述，TOPS/功耗以官方 whitepaper 为准；「30B MoE 端上跑」为演示口径。
- MLPerf 参考模型 Qwen3.6-27B 非最小端侧 Planner；其 gated 86.23% 与库内端侧小模型 BFCL 分数不可混算。
- 鸿蒙 7.0.0.109SP6 是否=正式版、小艺Work 执行机制（是否走元服务/意图回路）待华为开发者文档复核。
- 沿用：alpha12 `scope`/`serialize` 官方逐字段确认 / Per-Intent Privacy Manifest 官方逐字 / Watch OS 26 / NowSecure / AgentAntibody / Chrome Origin Sets / 高通 NPU exact TOPS / Berkeley 官方 BFCL v4 博客 / AppFunctions alpha13 / A2UI alpha02 / 26H2 精确 GA 日。

# 执行摘要（2026-09-25）

## 本轮产出（窗口 2026-09-21 22:00 → 09-25 13:00，约 3.5 天，距上次跑约 4 天）
- **四大 OS 官方框架层唯一净新增 = Android AppFunctions `1.0.0-alpha12`（2026-09-23）+ A2UI `1.0.0-alpha01`（同日常）**。AppFunctions 自 alpha11（08-26）以来首个版本进位，含多项 Registry/权限/执行上下文相关 API 变更。
- **真增量①（★7/10，官方直查 Release Notes）：AppFunctions alpha12 API 变更** → `scope` 字段加入 `AppFunctionMetadata`/`AppFunctionSearchSpec`（四平台首个官方 Jetpack 显式「作用域」维度，服务 Registry 可见性/权限模型）；`activityId` 加入 `ExecuteAppFunctionRequest`（执行上下文绑定）；`AppFunctionUriValueConstraint` 公共 API（Uri 参数级安全约束）；`AppFunctionData#serialize` 要求调用方提供元数据（可能为 provenance 信号但须谨慎）；运行时注册 API 标 `@ExperimentalAppFunctionsApi`；**破坏移除 `AppFunctionContext`/`AppFunctionConfiguration`**（首参身份注入对象被删）。补 [[Android AppFunctions 设备侧意图 2026]] + [[四平台意图 Registry 来源轴与权限模型对比 2026]]（scope 维度入表；来源轴全空白结论不变）。
- **真增量②（★6/10，官方 alpha-channel）：A2UI `1.0.0-alpha01` 官方落地 Android Jetpack** → `androidx.a2ui`/`a2ui.compose`/`material3-a2ui`，JSONL agent-defined UI 协议 + Material3 基础 catalog 13+ 组件（Button/Image/TextField/Slider/Modal 等），原生 Compose 渲染免任意代码。四平台首个官方 A2UI 库。补 [[A2UI 生成式UI协议(Google)与鸿蒙落地 2026]]。
- **真增量③（★6/10，生态补强）：鸿蒙 9-22 小艺接入淘宝闪购智能体「一句话点外卖」闭环 + 9-25 HarmonyOS 7 公测开放 + 数字（500+ 伙伴 Skills / 2000+ 鸿蒙智能体 / 2100+ 系统能力）**。补 [[HarmonyOS Intents Kit 与 ArkAF 2026]]。
- **状态行（★5/10，低于阈值）：统一 Copilot 桌面 app 9 月中旬铺开** → Chromium 架构、个人/工作账户合一，应用层分发变更非 OS API 新增。补 [[Windows Copilot Actions 与 Agent Workspace 2026]]。
- **落库**：A 索引 [[AppIntent 每日情报 2026-09-25]]、D 速览 [[AppIntent 每日情报速览 2026-09-25]]（spec 格式）、B 既有增补 5（Android/Registry/A2UI/HarmonyOS/Windows）、看板「本次新增（2026-09-25）」已登记。**0 新建 B 节点**。
- **环境**：未调用 Horizon MCP（环境仅 `agent-mail` 连接器在线）；按任务 fallback 改用 WebSearch/WebFetch 直查官方源（developer.android.google.cn/jetpack/androidx/releases/appfunctions、alpha-channel、compose-material3 release notes）与权威媒体（网易 9-25、simoncarter.ai）。alpha12/A2UI 为官方 Release Notes 直查确认。

## 诚实标注 / 待办
- alpha12 `scope` 语义（调用方可见性作用域 vs 功能分类域）、`serialize` 元数据字段定义待 developer.android.com/ai/appfunctions 官方文档逐字段确认；`scope` 是否=「可见性/权限作用域」在确认前不写入对比表正文（延续 08-31 纪律）。
- `serialize` 要求元数据可能是 provenance 信号但须谨慎——更可能是序列化结构元数据，未必等于 intent 来源 provenance；来源轴全空白结论不变。
- `AppFunctionContext`/`AppFunctionConfiguration` 移除后，调用方身份注入新机制待 alpha13+ 或官方指南；本笔记 08-03 开放问题「AppFunctionContext 是否携带可验证调用方身份」追问基础被削弱。
- A2UI alpha01 为首版，基础 catalog 组件集与字段稳定性待后续 release 复核（延续 08-26「A2UI 版本协商防静默空白」）。
- 小艺/淘宝闪购具体机制与闭环成功率、HarmonyOS 7 公测具体机型清单待华为开发者文档逐字复核（媒体口径）。
- 统一 Copilot app 为应用层变更非 OS 执行总线；26H2 GA 仍锚定 9 月下旬~10 月初。
- 跟踪：AppFunctions GA 日期；alpha13+ 身份注入机制；A2UI 后续 release；iOS 27.1 正式 beta 是否带新 Schema API；Per-Intent Privacy Manifest 官方逐字 / Watch OS 26 / NowSecure / AgentAntibody / Chrome Origin Sets / 高通 NPU exact specs / Berkeley 官方 BFCL v4 博客。

# 执行摘要（2026-09-25b · re-trigger 复核与补捕）

## 本轮产出（窗口 09-25 13:00 → 09-25 13:06，同日 re-trigger，约 6 分钟）
- **复核型运行 + 窗口内补捕**：对四大 OS 官方源二次核验，确认无新增 OS 框架层 API（无 AppFunctions alpha13 / iOS 27.1 新 `@AppIntent(schema:)` Schema / HarmonyOS 新 API / Windows OS 执行总线新 Registry API），与 09-25 主运行完全一致。
- **窗口内补捕（★5/10，治理层）**：Microsoft 365 Copilot **Declarative Agents 支持 Skills 转入 GA**（Message Center MC1476977，2026-09-22 公布，9 月中~月底全球铺开）。Skills 把指令/脚本/模板/资源打包为可复用模块、按需加载；脚本执行走**安全沙箱**、skill 文件上 **MIP 敏感度标签保留并生效**。与 [[Agent Skills 技能范式 2026]] / [[隔离执行]] / HarmonyOS Skills Framework / Android AppFunctions agent skill 构成跨平台「Agent Skill 上架 + 沙箱执行」范式对照。属 M365/Entra 治理层，非 Windows OS 执行总线。
- **落库**：既有 [[AppIntent 每日情报 2026-09-25]] 追加「复核与补捕」小节（不新建 A 文件）；[[Agent 365 与 Entra Agent ID 智能体控制平面与身份基座 2026]] 追加「2026-09-25 补捕」段；看板「本次新增（2026-09-25）」补 1 行。**0 新建 B 节点、0 新建 A/D 文件**。
- **环境**：同前，未调用 Horizon MCP，WebSearch 直查官方/权威源（developer.apple.com/documentation/updates、developer.android.com/ai/appfunctions、mwpro 对 MC1476977 转述）。

## 诚实标注 / 待办
- MC1476977 GA 日期与「安全沙箱 / MIP 标签」语法为 MWPro 对 Message Center 的转述（2026-09-22），待 learn.microsoft.com 逐字复核。
- 沿用 09-25 待办（alpha13 身份注入 / A2UI 后续 release / iOS 27.1 Schema / Per-Intent Privacy Manifest 官方逐字 / Watch OS 26 / NowSecure / AgentAntibody / Chrome Origin Sets / 高通 NPU / Berkeley BFCL v4 官方博客 / AppFunctions GA 日期）。

# 执行摘要（2026-09-26-晚）

## 本轮产出（窗口 2026-09-26 00:17→22:07，约 22h，晨间跑之后的日间延续）
- **四大 OS 官方框架层 API 仍零净新增**（iOS 27.1/27.2 双线无新 Schema / AppFunctions 守 alpha12 无 alpha13 / A2UI 守 alpha01 / HarmonyOS ArkAF 2.0 无新 API / Windows OS 执行总线四支柱无新 Registry API），与晨间跑「OS 框架不日更」连续一致。
- **真增量①（★6/10，M365 治理/执行层，非 OS API）：微软 09-25 Copilot 重架构** → Autopilot 常驻托管智能体（由 Scout 改名、自身身份/记忆/工作区）+ Copilot Managed Runtime 租户内沙盒托管运行时（npm @microsoft/managed-apps/-cli/-vite-plugin）+ 计费二分 USL/UBB。补 [[Agent 365 与 Entra Agent ID 智能体控制平面与身份基座 2026]] + [[Agent Workspace 隔离执行]]（Managed Runtime = SaaS 侧隔离执行样板）。
- **真增量②（★5/10，消费级实测补强）：鸿蒙小艺 9-26 评测数据** → CNMO 小艺 409 分登顶（领先 YOYO 30+）、中国电信四项第一、端侧盘古离线 12 秒会议记录、A2A 依托 2100+ 系统能力/500+ 伙伴 Skill。补 [[HarmonyOS Intents Kit 与 ArkAF 2026]]（评测机构/媒体口径，待华为文档核验）。
- **真增量③（★5/10，社区端侧实证）：Qwen3-0.6B Q4_K_M 在 2017 Note8（6GB）驱动真实桌面 Chrome** → 结构化页面感知层（~200 token）驱动、3 任务 10/10、结构化 500 token/80s vs 原始 HTML 12k token/22min。补 [[Function Calling 端侧工具调用]]（社区实验、非 BFCL、仅 3 固定任务）。
- **去伪**：Semantic Kernel CVE-2026-26030/25592（CVSS 9.9）经核查为 2026-05 已披露，非本窗口新 CVE；KOPA-BENCH（arXiv 2609.05395）新基准但非端侧 Planner 专项、低阈值丢弃。
- **落库**：A 索引 [[AppIntent 每日情报 2026-09-26-晚]]、D 速览 [[AppIntent 每日情报速览 2026-09-26-晚]]、B 既有增补 4（Agent 365 / Agent Workspace隔离 / HarmonyOS / Function Calling）、看板「本次新增（2026-09-26-晚）」已登记。**0 新建 B 节点**。
- **环境**：仅 `agent-mail` 在线，未调用 Horizon MCP，WebSearch/WebFetch 直查官方/权威源（微软 09-25 博文多源转述 / 网易 / 新浪 / 腾讯搜一搜 / 开发者社区）。

## 诚实标注 / 待办
- 微软 Copilot 重架构为官方博文（Spataro）多源转述，GA/预览日期与 Managed Runtime 沙箱语法待 learn.microsoft.com 逐字；Autopilot 9 月底私有预览、非 GA。
- 鸿蒙评测数字（409/四项第一/离线 12 秒）评测机构与媒体口径，待华为开发者文档核验。
- Qwen3-0.6B Note8 为 e2llm 社区仓库、仅 3 固定任务、非通用 benchmark，与其比端侧 Planner 准确率不严谨。
- 沿用：Per-Intent Privacy Manifest 官方逐字 / Watch OS 26 / NowSecure / AgentAntibody / Chrome Origin Sets / 高通 NPU exact specs / Berkeley BFCL v4 博客 / AppFunctions alpha13 / A2UI alpha02 / 26H2 GA 日 / iOS 27.1 正式 beta Schema / Managed Runtime 与隔离 SOP 跨厂商对照。

# 执行摘要（2026-10-26 · 续跑，窗口 2026-10-18 21:00 → 10-26 22:53，约 8 天）

## 本轮产出（约 8 天，衔接上轮 10-18 收尾、补齐其间空档）
- **唯一 OS 框架层真增量（★7/10）= Android AppFunctions 首个 Beta `1.0.0-beta01`（2026-10-21）**：自 alpha13（10-07）进位到 beta，未发 alpha14；含**协议级 `AppFunctionAppMetadata.description` → `instructions` 重命名，官方明示「to align with MCP naming conventions」**（跨平台 MCP 命名对齐信号）+ `AppFunctionName` 包搬移 + `isDescribedByKDoc` 默认值移除须显式设 + 资源容器标 `@ExperimentalAppFunctionsApi` + `@AppFunctionStringValueConstraint` 的 regex→`android.os.PatternMatcher`。标志 API 从「剧烈变动期」迈入「beta 稳定化」。
- **头号跟踪项收口（★6/10）= iOS 27.1（10-23）随 iPhone Duo 独占交付**：经 Apple newsroom + App Intents Updates 官方页核验，Duo 双屏适配走 **SwiftUI/UIKit 布局/铰链/scene-accessory/摄像头 API，无新 `@AppIntent(schema:)` Schema**——自 09-21 连续 8+ 轮跟踪的「双屏新意图 Schema」答案 = 否（Apple 当显示/布局问题处理）。iOS 27.2 RC（10-19）亦无新 Schema；**Impersonation Risk Detection 为 iOS 27 即内置、于 27.2 RC 现身的通信反诈骗特性（off-by-default），非 27.2 新增、非意图框架 API**（本轮已作诚实校正）。
- **其余平台零净新增**：HarmonyOS（Intents Kit 指南 V14 仍 10-10、窗口外；ArkAF 稳定；CSDN 为教程）/ Windows（全为 10-07 MXC GA 事件的治理视角分析扩散；HydraFusion 仍「10 月底实验性预览」未 GA）/ BFCL v4（榜单 10-23 刷新但无新端侧 Planner 入榜，端侧 LFM2.5-230M 21% / MiniCPM5-2B 66.6% 维持）/ XPIA（多篇概念/行业复述、无新 OS 执行总线机制）均落「OS 框架不日更」。
- **落库**：A 索引 [[AppIntent 每日情报 2026-10-26]]、D 速览 [[AppIntent 每日情报速览 2026-10-26]]、B 既有增补 3（[[Android AppFunctions 设备侧意图 2026]] beta01 段 / [[Apple AppIntents Schema Protocol 2026]] 关闭双屏 Schema 跟踪段 / [[四平台意图 Registry 来源轴与权限模型对比 2026]] 成熟度+MCP 命名+关闭跟踪段）、看板「本次新增（2026-10-26）」已登记。**0 新建 B 节点**。
- **环境**：仅 `agent-mail` 在线，未调用 Horizon MCP，WebSearch / WebFetch 直查官方源 + 权威媒体（Jetpack Release Notes / Apple newsroom / App Intents Updates 页 / 华为开发者月刊 / benchlm.ai / llmboard.ai）逐平台核验。
- **诚实校正**：本轮对既有 A/D/B 笔记中「Impersonation Risk Detection = iOS 27.2 引入」的轻微版本误归因做了精确化（Apple 支持文档明确「从 iOS 27 开始提供」），不影响「非意图框架 API / off-by-default / 低于阈值」的结论。

## 诚实标注 / 待办
- `@AppFunctionAccessLevel` 级别语义官方 Release Notes 在 beta01 仍未展开，待 `developer.android.com/ai/appfunctions` 官方文档逐字段确认（延续 10-13 待办）。
- AppFunctions GA 日期仍待补（beta01 为首个 beta，非 GA）。
- iOS 27.2 正式版（~10-26）的 agentic 安全与多模型路由落地待观察。
- 四平台意图 Registry **来源/provenance 轴仍全空白（最高优先待办，confirmed）**：本窗口各平台均未新增「数据从哪来、可不可信」的 intent 元数据来源字段；最低成本补丁仍是加 `readOrWrite` 声明位。

# 执行摘要（2026-10-29 · 24h 复核，窗口 2026-10-28 21:00 → 10-29 21:00）

## 本轮产出（24h）
- **唯一 OS 级真增量来自 Android Dev Summit（2026-10-28 召开）两项官方公告**（处本窗口起点边缘、10-28 运行未记录，本运行作诚实边界补捕）：
  - **① Connected Apps Platform（预览，★7/10）= AppFunctions + Android MCP 经 Google Connected Console 注册后，同时可达 Gemini app 与 Search AI Mode（"enable once, run Google-wide"），50+ 伙伴集成**——四平台**首个把设备侧意图框架直接挂到系统级搜索入口 Search 的官方能力**，是跨应用 Intent 工作流发现面。
  - **② ML Kit Agentic API（alpha，Gemini Nano 4，★6/10）= OS 提供的端侧函数调用 + 对话历史管理 + 执行流控**，端侧 Planner 一等原语，补 Android 端侧意图执行总线「模型层」。
- **其余平台零净新增**：Apple（27.2 已 GA、框架层 10-28 已复核零变更、本窗口仅消费者复述）、Android（AppFunctions 仍 `1.0.0-beta01` 无 beta02/alpha14）、HarmonyOS（CEIC 1024 深圳 10-24 生态复盘、无新 API）、Windows（无新 OS 执行总线 API）、BFCL v4（rlresearch 10-25 快照 104 模型无新端侧 Planner official entry）。
- **状态更新（★5/10，关闭长期跟踪项）**：GitHub Copilot Fusion 本地模型路由（MAI Code 1.1 Flash via Windows ML）10-28 落地实验预览 = 「HydraFusion 10 月底实验预览」到点；**但属编码 harness，非 Windows OS Copilot Actions/Agent Workspace bus**，按口径标记、不计入 OS 净新增。
- **端侧 Planner 模型（★5/10，待官方复核）**：LFM3-1.7B（Liquid AI，1.7B，AMD Ryzen AI 定位）BFCL V4 71.39 新出（聚合转述，确切官宣日待补）。
- **去伪/丢弃（按口径）**：XPIA MCP tool server 命令注入一波（CVE-2026-117558~573，10-27 发布、落窗口前 ~21h、MCP 工具链层、非四平台 OS 总线，延续 10-05/10-06 丢弃纪律）；Android Studio BYOA/ACP（开发工具链）；HarmonyOS CEIC 复盘（10-24 窗口外）；Apex-35B（35B 云级、非端侧）。
- **落库**：A 索引 [[AppIntent 每日情报 2026-10-29]]、D 速览 [[AppIntent 每日情报速览 2026-10-29]]、B 既有增补 3（[[Android AppFunctions 设备侧意图 2026]] / [[Function Calling 端侧工具调用]] / [[四平台意图 Registry 来源轴与权限模型对比 2026]]）、看板「本次新增（2026-10-29）」已登记。**0 新建 B 节点**。
- **环境**：无 Horizon MCP（仅 `agent-mail` 在线）；WebSearch + WebFetch 直查官方/权威源（The Prompt Insider/腾讯新闻/Pivot News/Zendoric 对 Dev Summit + GitHub 官方 changelog + rlresearch BFCL 镜像 + xibilus LFM3 + 华为 CEIC 复盘 + 网易 iOS 27.2 复述）完成逐平台核验。

## 补遗（2026-10-29 21:12 复核 · 同窗口深度补全，非新一日跑）
- freshness 复核（10-29 多源：TechCityAuthority/aiagentslibrary/beyondthe.news/xnews/dev.to/MACCUS）补 **Connected Apps Platform 此前遗漏的执行安全/确认机制 + 架构双路径硬细节**，已落 B 笔记 [[Android AppFunctions 设备侧意图 2026]]「2026-10-29 补遗」段 + A 笔记补遗 callout + 看板「本次新增（2026-10-29）」补遗 bullet。
- **新捕获要点（均已写入 B 笔记，下一轮跑勿重复计为新增量）**：
  1. **平台级确认机制**：开发者在 Google Connected Console 标记「需确认操作」+ 工具声明 read-only / action-that-changes-data；可选绑定交互 UI 资源（A2UI 方向）。修正旧「确认完全下放 App」单向叙述——平台提供确认钩子，但仍由开发者/工具声明。
  2. **调用模型**：@appname 或名称调用，调用后 app 在本 session 相关请求中保持上下文（session 级意图保持）。
  3. **架构双路径**：Remote MCP server = Google 推荐默认（跨 Android/iOS/Web，公开 HTTPS），AppFunctions = client-side 本地互补路径（非唯一路径）。
  4. **授权/治理**：OAuth 2.1 + 平台政策（2026-09-28：数据最小化、禁第三方广告、禁欺骗性工具描述）。
- **诚实**：WebFetch 直连 `developer.android.com/ai/appfunctions` 本会话仍失败（沙箱网络），字段名（确认标记 UI 形态、read-only/action 注解名）待官方文档逐字段确认；不臆造。
- **下一轮基线维持**：AppFunctions 官方最新 = `1.0.0-beta01`（10-21）；无 beta02/alpha14；Android Dev Summit（10-28）公告已捕获（含补遗）；最高优先「来源轴四平台全空白」待办延续。

## 诚实标注 / 待办
- Connected Apps Platform / ML Kit Agentic API 为 preview/alpha、非 GA，具体 API 名与权限边界待 `developer.android.com/ai/appfunctions` 官方文档逐字段确认。
- Connected Apps Platform 是否受 `EXECUTE_APP_FUNCTIONS` 同一闸门约束、Search 入口触发是否收紧确认/隔离 UX 待官方。
- ML Kit Agentic API 的 SDK 形态、是否调用 AppFunctions、权限边界待官方。
- LFM3-1.7B 确切官宣日期与 Berkeley 官方榜行待补。
- 最高优先：四平台意图 Registry 来源/provenance 轴仍全空白（confirmed），最低成本补丁仍是加 `readOrWrite` 声明位。
- 延续：@AppFunctionAccessLevel 级别语义 / AppFunctions GA 日 / Watch OS 26 / NowSecure / AgentAntibody / Chrome Origin Sets / Berkeley 官方 BFCL v4 博客 / A2UI alpha02 / Per-Intent Privacy Manifest 官方逐字 / 高通 NPU exact specs / GitHub Copilot Fusion 是否向 Windows OS Copilot Actions 下沉。
- 沿用：Per-Intent Privacy Manifest 官方逐字 / Watch OS 26 / NowSecure / AgentAntibody / Chrome Origin Sets / 高通 NPU exact specs / Berkeley BFCL v4 官方博客原文 / A2UI alpha02 / Managed Runtime 与隔离 SOP 跨厂商对照。

# 执行摘要（2026-10-31 · 24h 复核，窗口 2026-10-30 21:00 → 10-31 21:53）

## 本轮产出（约 24h）
- **四平台官方框架层 + 跨平台 BFCL 端侧 Planner + XPIA 研究线，全部零净新增 API / 评测 / 研究突破**——与连续多轮「OS 框架不日更」结论完全连续，本运行为**纯复核型**（同 10-30）。
- **Apple**：App Intents Updates 官方页 WebFetch 直查仍列 iOS 27 时代 API 集、无 2026-10 新 schema；iOS 27.2 支持页仅 Siri AI 消费者功能 + 安全补丁（Accounts/App Intents entitlement 检查收紧），非框架 API。★★☆☆☆
- **Android**：官方 Jetpack Release Notes 直查确认 **AppFunctions 仍 `1.0.0-beta01`（10-21）最新**，无 beta02/alpha14；「The Intelligent OS」博客（developer.android.google.cn）为既有 beta + Samsung Gallery/Galaxy S26 伙伴实例，非新进位。★★☆☆☆
- **HarmonyOS**：Intents Kit 指南/ArkAF 概述稳定；CSDN 教程 + 天工计划（10-31 激励截止）为教程/运营，无 OS API 变更。—
- **BFCL v4**：LLMBoard 10-31 刷新至 24 模型（较 10-30 的 22 增 2）、仍全云级（Atria Dawn 77.00% / Qwen3.7 Max 75.00% / Ling 3.0 Flash 73.00% 等 Oct 30 评测）；**无新端侧（≤数 B）Planner official entry**。★★☆☆☆
- **Windows**：「Building Windows for Hybrid Intelligence」= 10-07 MXC GA + hybrid intelligence 愿景 reprised，无新 OS 执行总线 API；MC1484007 Copilot in Edge Voice/Vision 为应用层（mid-Oct 铺开）；Project Perception「newest insiders」（Oct 19）为窗口外安全架构公告，不计入。—
- **XPIA**：appsecmaster/cn-sec/ainews 为既有原理/OWASP 2026 #1 复述，无新 OS 执行总线机制。—
- **去伪/丢弃（按口径）**：Muse Glimmer 30B（Meta，10-26，30B 非小端侧、无 BFCL entry、纯模型发布）、Needle 3（8-29MB 社区小模型、无 entry）、iOS 27.2 安全补丁（非新框架 API）、Edge Copilot Voice/Vision（应用层）。
- **落库**：A 索引 [[AppIntent 每日情报 2026-10-31]]、D 速览 [[AppIntent 每日情报速览 2026-10-31]]、看板「本次新增（2026-10-31）」已登记。**0 新建 B 节点、0 既有 B 增补**。
- **环境**：仅 `agent-mail` 在线，未调用 Horizon MCP，WebSearch / WebFetch 直查官方源 + 权威媒体完成逐平台核验。

## 诚实标注 / 待办
- Apple App Intents Updates 官方页（developer.apple.com/documentation/updates/appintents）WebFetch 直查仍 iOS 27 时代 API 集、无 2026-10 新 schema 条目；iOS 27.2 支持页（support.apple.com/149045）仅 Siri AI 消费者功能。
- Android AppFunctions 仍 `1.0.0-beta01`（10-21）经官方 Jetpack Release Notes 直查确认最新；「The Intelligent OS」博客为既有 beta + 伙伴实例、非新 API 进位；`@AppFunctionAccessLevel` 级别语义待 developer.android.com/ai/appfunctions 官方文档。
- BFCL v4：LLMBoard 榜「Updated Oct 31, 2026」、24 模型、仍全云级、无新端侧 Planner entry；官方 Berkeley 榜停滞（2026-04-12）。
- Windows「Building Windows for Hybrid Intelligence」= 10-07 MXC GA reprised，无新 OS 执行总线 API；MC1484007 为 Edge 应用层。Project Perception「newest insiders」（Oct 19）窗口外，不计入；若需补捕走单独回溯。
- **【最高优先·来源轴仍空白】四平台意图 Registry 来源/provenance 轴仍全空白（confirmed）**，最低成本补丁仍是加 `readOrWrite` 声明位——本窗口无新进展、待办延续。
- 延续：@AppFunctionAccessLevel 官方逐字段 / AppFunctions GA 日 / Connected Apps Platform 闸门 / ML Kit Agentic API SDK / LFM3-1.7B 官宣日 + BFCL 官方榜 / Project Perception 回溯 / GitHub Copilot Fusion 是否向 Windows OS Copilot Actions 下沉 / Watch OS 26 / NowSecure / AgentAntibody / Chrome Origin Sets / Berkeley 官方 BFCL v4 博客 / A2UI alpha02 / Per-Intent Privacy Manifest 官方逐字 / 高通 NPU exact specs。

# 执行摘要（2026-11-02 · 24h+ 复核，窗口 2026-10-31 21:53 → 11-02 12:21，约 38h）

## 本轮产出（约 38h）
- **四平台官方框架层 + 跨平台 BFCL 端侧 Planner + XPIA 研究线，再次全部零净新增 API / 评测 / 研究突破**——连续多轮「OS 框架不日更」结论完全连续，本运行为**纯复核型**（同 10-30/10-31）。
- **唯一窗口内信号（★5/10，低于 6 阈值）= Windows File Explorer 右键菜单 8 项 OneDrive Copilot Actions 整合进「Ask Copilot」（MC1515940，2026-11 中旬起分阶段 ~ 12 初完成）** → 属 Copilot Actions **surface 收敛/整理**（能力保留、非新 API、非新安全机制）；已在 [[Windows Copilot Actions 与 Agent Workspace 2026]] 追加 1 条 ★5 状态行，**不升 B 节点**。
- **逐平台核验**：Apple（App Intents Updates 官方页 WebFetch 直查仍 iOS 27 时代 API 集、无 2026-11 新 schema；iOS 27.2 已 GA、无 iOS 27.3 新意图 Schema 信号）/ Android（Jetpack Release Notes 直查确认 AppFunctions 仍 `1.0.0-beta01` 10-21 最新、无 beta02/alpha14；A2UI/ML Kit Agentic API 仍 alpha；Dev Summit 10-28 能力边界表确认）/ HarmonyOS（Intents Kit/ArkAF 指南稳定）/ BFCL v4（FunctionGemma 270M / qwen3-0.6b-tool-router 仍不在榜）/ Windows（无新 OS 执行总线 API；Ignite 2026 11-17~20 尚未开幕、预热议程属路线图非已发布 API）。
- **去伪/丢弃（按口径）**：LFM3-1.7B（Liquid AI Oct 27，已在 10-29 捕获）/ Bonsai 2（PrismML Oct 15）/ Nemotron 3.5 Bolt（Nvidia Oct 19）均窗口外模型发布；LFM2.5-24B-A2B（BFCL v4 65.01）为 24B 边缘大模型、非 ≤数 B 端侧 Planner 严格范畴，monitor 项；XPIA 原理复述波（appsecmaster/nhimg/zone.ci）无新 OS 机制。
- **落库**：A 索引 [[AppIntent 每日情报 2026-11-02]]、D 速览 [[AppIntent 每日情报速览 2026-11-02]]、B 既有增补 1（Windows ★5 状态行）、看板「本次新增（2026-11-02）」已登记。**0 新建 B 节点**。
- **环境**：无 Horizon MCP（仅 `agent-mail` 在线）；WebSearch / WebFetch 直查官方源 + 权威媒体完成逐平台核验。

## 诚实标注 / 待办
- Apple App Intents Updates 官方页仍 iOS 27 时代 API 集、无 2026-11 新 schema；iOS 27 whats-new 的 Core AI / Foundation Models 模型无关化 / Evaluations 属 9-14 GA 内容、非窗口内新增。
- Android AppFunctions 仍 `1.0.0-beta01`（10-21）经 Jetpack Release Notes 直查确认最新；`@AppFunctionAccessLevel` 级别语义待 developer.android.com/ai/appfunctions 官方文档。
- Windows MC1515940 分阶段落地精确日期与是否受 08-02 `Experimental agentic features` 同一 opt-in 开关管控待 Microsoft 官方 blog 逐字复核。
- **【最高优先·来源轴仍空白】四平台意图 Registry 来源/provenance 轴仍全空白（confirmed）**，最低成本补丁仍是加 `readOrWrite` 声明位——本窗口无新进展、待办延续。
- 下一窗口重点：Ignite 2026（11-17~20）开幕后核验是否披露新 Windows OS 执行总线 Registry API / Agent Launchers 新能力 / Copilot Actions 从 experimental 转正式；延续既有待办（AppFunctions GA 日 / A2UI alpha02 / Connected Apps Platform 闸门 / ML Kit Agentic API 形态 / LFM3 官宣日 / Project Perception 回溯 / Berkeley 官方 BFCL v4 博客 / Per-Intent Privacy Manifest / 高通 NPU specs）。

# 执行摘要（2026-11-05 · 24h+ 复核+补捕，窗口 2026-11-03 23:38 → 11-05 19:12，约 44h，含 11-04 空缺补跑）

## 本轮产出（约 44h）
- **唯一 OS 框架层真增量（★8/10）= Apple Siri AI 开发者预览（iOS 27.3，11-03 美/11-04 中）把 Siri AI 向所有开发者开放 + 一组新 App Intents API**：① `@AppIntent(.tool)` 宏（intent→Siri「工具」，对既有/新均生效）；② **Skills** = `SKILL.md` 子集（body ≤10k 字符、无 scripts/refs，多步编排）；③ **Spotlight 语义索引「可浮现任意实体、不再限既有 schema」**（schema 约束松动）；④ Xcode Siri Integration Advisor + Siri Evaluations 框架（意图集成回归测试）。这是 iOS 27 GA 以来 App Intents 接入面最大扩展，且把 Apple 拉入 `SKILL.md` 跨平台技能格式阵营（Google 已声明 Gemini 可复制其他平台 skill）。
- **执行安全关键约束（★8/10）**：Apple 明确 **app skills 不保证确定性执行顺序**——保序步骤（如确认购买）必须在 intent 实现内加检查，不能依赖 skill 文案顺序；另 iOS/iPadOS 27.3 known issue：即便定义了要求解锁的 `authenticationPolicy`，Siri AI 仍可能在未解锁时显示该实体（beta 期认证策略执行缺口）。
- **其余平台零净新增**：Android（AppFunctions 仍 beta01；Google 开放安卓 dev tools 给 Claude/Codex = 开发者工具链、非消费者意图框架，丢弃）/ HarmonyOS（稳定 + 双十一营销/教程）/ Windows（MXC 为 10-07 GA reprised；M365 SKILL.md/EMBRACE 为 M365/工具层、非 OS bus，丢弃）/ BFCL v4（LLMBoard 11-04 刷新仍全云级、端侧 Planner 仍不在榜）。
- **落库**：A 索引 [[AppIntent 每日情报 2026-11-05]]、D 速览 [[AppIntent 每日情报速览 2026-11-05]]、B 既有增补 3（[[Apple AppIntents Schema Protocol 2026]] / [[Agent Skills 技能范式 2026]] / [[Intent Router 语义路由]]）、看板「本次新增（2026-11-05）」已登记。**0 新建 B 节点**（概念均已存在，按去重纪律追加）。
- **衔接 11-03**：11-03 录 iOS 27.3 beta 落地 + 中国 Qwen 端侧底座（模型层）；本运行补全同一事件的 App Intents 框架层深度，并关闭 11-03 待办「iOS 27.3 是否新增公开 App Intents Schema（待 dev release notes 解析）」= 结论为「无新 schema 域、仅既有机制能力放大」。
- **环境**：仅 `agent-mail` 在线，未调用 Horizon MCP，WebSearch 直查官方/权威源（developer.apple.com/news/?id=gdk2umrf / wain.blog 官方文档解读 / appleosophy / developer.android.com / 华为开发者文档 / learn.microsoft.com / LLMBoard bfcl-64）。

## 诚实标注 / 待办
- `@AppIntent(.tool)` 是否新 API 名或 ToolIntent 宏糖衣、`Skills.skillsbundle` 打包/签名约束、GA 日期（预览「数月后」/提交「春季」）待官方文档逐字段确认。
- Apple skills「不保证顺序」如何与系统级 Confirmation UI 协同（保序确认是否需新 intent 级护栏 API）待观察。
- 语义索引「任意实体」放宽后，低置信/歧义实体浮现是否需置信门控（呼应端侧 Router 置信度门控）待观察。
- 延续：四平台来源轴全空白（最高优先）/ @AppFunctionAccessLevel 官方逐字 / AppFunctions GA 日 / Connected Apps Platform 闸门 / ML Kit Agentic API 形态 / LFM3 官宣日 / Ignite 2026（11-17~20）/ Watch OS 26 / AgentAntibody / Chrome Origin Sets / Berkeley 官方 BFCL v4 博客 / A2UI alpha02 / Per-Intent Privacy Manifest / 高通 NPU specs。
