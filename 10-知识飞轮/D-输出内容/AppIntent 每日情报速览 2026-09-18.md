---
type: output
status: draft
created: 2026-09-18
method_used: "WebSearch/WebFetch 官方源 + 库内去重（窗口 2026-09-17 22:38 → 09-18 21:00，iOS 27 GA 后第 4 日）"
tags: [AppIntent, 速览]
---

# AppIntent 每日情报速览 2026-09-18

## 目标读者与目标
OS PM（Ethon）；30 秒掌握四平台系统级意图框架过去 1 日真增量。本期结论：**四平台官方框架层 + BFCL v4 榜 + XPIA 研究线均无 24h 净新增**，属复核型运行。

## 正文

本期窗口（2026-09-17 22:38 → 09-18 21:00）距 iOS 27 GA（09-14）第 4 日，**四大 OS 官方框架层无净新增 API**——延续 09-13→09-17 连续多轮的「OS 框架不日更」结论。执行安全最新进展仍停在 09-17 的两条（SIR 自改进攻击 + 自修改 Agent 权重级持久化）。

1. **四平台官方框架层均无 24h 净新增（核心结论）**：
   - **Apple**：`developer.apple.com/wwdc26/guides/ios` App Intents 段落自 GA 后未变；搜索命中的 7 篇 iOS 27 文章（TechPillow / Cropsly / ecorpit / byteiota / dev.to / macworld 等）全是 09-14 GA 后的二次复述，无 WWDC 之外新 API。**iOS 27.1 首个 beta 尚未发布**（Macworld 09-18 确认）→ 短期无新 App Intents API 信号。
   - **Android**：AppFunctions 仍 alpha（alpha11，2026-08-26），窗口内无 alpha12；`EXECUTE_APP_FUNCTIONS` + `AppFunctionsManager` + `PROPERTY_SUPPORT_APP_FUNCTION_USER_CONTROL` 为既有稳定文档。Android Police「security cage」为 09-14 媒体复述。
   - **HarmonyOS**：Intents Kit / ArkAF 2.0 / A2UI 同 HDC2026 / 09-07 消费版，无新意图框架 API；命中文多为旧文复述。
   - **Windows**：Copilot Actions / Agent Workspace / ODR / Agent Launchers / Execution Containers / 签名吊销均无新 Registry API；dev.to 的云端 Copilot（SharePoint 技能/Brand Kit）为应用层、丢弃。

2. **BFCL v4 榜 + 端侧 Planner 评测线无 24h 新增**：SOTA 仍 **MiniCPM5-2B 66.6（09-07）/ Spark-X2.5-4B 65.1（09-01）**，窗口内无新端侧 Planner 模型入榜；FunctionGemma / qwen3-0.6b-tool-router 均为旧文。端侧评测表维持 09-13 后稳定态。

3. **XPIA / 执行安全研究线无 24h 净新增（★5/10 状态项，非网罗）**：
   - OWASP Agentic AI Top 10 2026 经多源确认 **2025-12-09 发布**（版本号「2026」指治理年份），属 9 个月前标准、非本期新发布；其 ASI01（Agent Goal Hijack）可作库内 [[XPIA 跨提示注入]] 的标准化映射参考，但不构成增量。
   - Microsoft RAMPART 为 XPIA **测试框架工件**（inline / surface-based / DOCX payloads + 组合 evaluator），非 OS 机制变更，标「参考、待一手发布日期」。
   - 最新研究进展仍停在 09-17：SIR 自改进攻击 + 自修改 Agent 权重级持久化。

4. **唯一低于收录阈值的状态更新（★5/10）— Windows Copilot Actions 向 Insiders 分批推送**：msftnewsnow 报道 Copilot Actions 已随 Copilot app 更新 **1.25112.74+** 向 Insiders「Now Available」——把「预览 / opt-in 默认关」推进为分批可安装。能力清单与此前记录一致，**无新框架 API**；已追加状态行至 [[Windows Copilot Actions 与 Agent Workspace 2026]]，未新建 B 节点。

## 使用的方法
WebSearch/WebFetch 直查 developer.apple.com/wwdc26/guides/ios、developer.android.com/ai/appfunctions、developer.huawei.com harmonyos-guides/arkaf-overview、llmlearner BFCL v4、msftnewsnow / windowsnews.ai / windowsforum、cisoplatform OWASP、microsoft.github.io RAMPART；库内去重：对照 09-17 看板与既有 B 笔记（Apple/Android/HarmonyOS/Windows/BFCL/XPIA 均已覆盖），确认无净新增、不新建重复节点（本日 0 新建 B 节点，仅向 Windows B 笔记追加 1 行部署状态）。未调用 Horizon MCP（环境无此工具，按 fallback 改用 WebSearch/WebFetch）。

## 发布反馈
（待发布后回填）

## 复盘
### 有效的部分
严格按「已复核·无净新增」纪律落档，省去下次重复检索；明确把 OWASP Agentic Top 10（2025-12 发布）与 RAMPART（测试框架）排除在增量之外，避免把旧标准/工件误当 24h 新进展；iOS 27.1 beta 未发布这一事实被显式记录，为后续「iOS 27.1 是否带新 App Intents API」留了对照锚点。

### 需要改进的部分
Windows Copilot Actions app v1.25112.74+「Now Available」报道未给出精确发布日期，无法确认是否严格落在 24h 窗口内，仅作状态更新处理；OWASP / RAMPART 的一手发布时间仍待补。

### 回流到 A 的新问题或素材
- 跟踪 iOS 27.1 beta（预期 10 月）是否引入新 App Intents API / App Intents Domains 细节。
- 跟踪 AppFunctions alpha12 是否落地 `@AppFunctionSignature` 动态注册 + `AppFunctionState` 之外的门控 API。
- 把 OWASP Agentic AI Top 10 2026（ASI01–ASI10）与库内 [[XPIA 跨提示注入]] / [[Confirmation UI 安全机制]] / [[Agent Workspace 隔离执行]] 做一张映射表（待办，非本期增量）。
- 延续既有待办：Berkeley 官方 BFCL v4 榜逐字、Watch OS 26 是否 Trust Insights 类、NowSecure/AgentAntibody 一手复核、Chrome Origin Sets 官方 URL、高通 NPU exact specs、Per-Intent Privacy Manifest 官方文档逐字。
