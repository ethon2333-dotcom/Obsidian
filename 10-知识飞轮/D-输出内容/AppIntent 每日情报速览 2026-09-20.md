---
type: output
status: draft
created: 2026-09-20
method_used: "WebSearch/WebFetch 官方源 + 库内去重（窗口 2026-09-18 21:00 → 09-20 21:00，约 48h）"
tags: [AppIntent, 速览]
---

# AppIntent 每日情报速览 2026-09-20

## 目标读者与目标
OS PM（Ethon）；30 秒掌握四平台系统级意图框架过去 2 日真增量。本期结论：**四平台官方框架层 + BFCL v4 榜均无 48h 净新增**，属复核型运行 + 库内空白补漏（捕获两类此前未入库的高价值研究）。

## 正文

本期窗口（2026-09-18 21:00 → 09-20 21:00）距 iOS 27 GA（09-14）第 6 日、**四大 OS 官方框架层无净新增 API**——延续 09-13→09-19 连续多轮的「OS 框架不日更」结论。本期净新增 = 0，价值在把「已复核·无净新增」显式落档，并把两类库内空白补漏补进对应 B 节点（★6/10）。

1. **四平台官方框架层均无 48h 净新增（核心结论）**：
   - **Apple**：`developer.apple.com/wwdc26/guides/ios` App Intents 段落自 GA 后未变；搜索命中的 iOS 27 文章（macworld / braze / byteiota / scand / ecorpit / webpronews）全是 09-14 GA 后二次复述，无 WWDC 之外新 API。**iOS 27.1 首个 beta 截至 09-20 仍「尚未发布」**（Macworld 确认），短期无新 App Intents API 信号。
   - **Android**：AppFunctions 仍 alpha（alpha11，2026-08-26），窗口内无 alpha12；`EXECUTE_APP_FUNCTIONS` + `AppFunctionsManager` + `AppFunctionState` 为既有稳定文档。
   - **HarmonyOS**：Intents Kit / ArkAF 2.0 / A2UI 同 HDC2026 / 09-07 消费版，无新意图框架 API。
   - **Windows**：Copilot Actions / Agent Workspace / ODR / 四安全控件 / 代码签名吊销均无新 Registry API；09-19 仅 Copilot 窗口 UX 调整（丢弃）。

2. **BFCL v4 榜 + 端侧 Planner 评测线无 48h 新增**：官方榜 **Last Updated 仍 2026-04-12**（停滞），SOTA 维持 **MiniCPM5-2B 66.6（09-07）/ Spark-X2.5-4B 65.1（09-01）**，窗口内无新端侧 Planner 模型入榜；Needle 2（14MB ESP32）/ Gemma 4 tool-call patch / Qwen3-4B 手机延迟均为旧文或社区微调。端侧评测表维持 09-13 后稳定态。

3. **库内空白补漏①（★6/10）— 技能层供应链投毒成实证攻击类**：Skill-Inject（arXiv 2602.20156）/ Malicious Agent Skills in the Wild（arXiv 2602.06547，分析 **~100,000 个 skills**）/ SkillJect（arXiv 2602.14211）三篇 2026-02 实证研究，把「恶意 Skill / manifest 注入」从概念警告推为可测攻击类，直接对应 HarmonyOS ArkAF Skills 上架、Android AppFunctions agent skill、A2A 分发层。**OS 级 Skill Registry 若不做来源校验 + 签名，等于把供应链投毒面原样搬进系统层**。补 [[XPIA 跨提示注入]] + [[Agent Skills 技能范式 2026]]。

4. **库内空白补漏②（★6/10）— XPIA 防御侧量化补强**：PromptArmor（ICLR 2026）用现成 LLM 检测/净化注入，AgentDojo 上 **FP/FN <1%**；Zylos 2026 基准显示即便开全部厂侧缓解，间接注入对最强前沿模型仍有 **~32% 成功率**（量化天花板，印证「边界优先于检测」）。补 [[XPIA 跨提示注入]]。

5. **窗口外前瞻（★5/10）— iOS 27.1 beta 在即**：首个 developer beta 预期 **2026-09-21~23**（MacRumors 口径）；公开版随 iPhone Duo 10-23 预装。Messages「加到提醒事项/备忘录」任务建议 = `reminders.createReminder` / `notes.createNote` schema 以零短语主动建议形态入 Messages（App Intents 主动式分发面扩大）。当前报道均未提新 Schema API，预期为 GA 补全 + 本地化，非框架级新增；已登记为下一窗口头号跟踪项。

## 使用的方法
WebSearch/WebFetch 直查 developer.apple.com/wwdc26/guides/ios、developer.android.com/ai/appfunctions、developer.huawei.com harmonyos-guides/arkaf-overview、gorilla.cs.berkeley.edu BFCL v4、msftnewsnow / windowsnews.ai / learn.microsoft.com、vectra.ai / agentmelt（XPIA 防御）、LinkedIn Tal Eliyahu AI Security Feb 2026（skill 投毒 arXiv 索引）；库内去重：对照 09-18 看板与既有 B 笔记（Apple/Android/HarmonyOS/Windows/BFCL/XPIA/ Agent Skills 均已覆盖），确认框架层无净新增、Skills 投毒与 XPIA 防御为库内空白补漏（0 新建 B 节点，向既有 XPIA / Agent Skills / Apple 三节点各追加 1 段）。未调用 Horizon MCP（环境无此工具，按 fallback 改用 WebSearch/WebFetch）。

## 发布反馈
（待发布后回填）

## 复盘
### 有效的部分
严格按「已复核·无净新增」纪律落档，省去下次重复检索；把 2026-02 的 skill 投毒三篇与 ICLR 2026 的 PromptArmor 作为「库内空白补漏」捕获而非漏掉，补齐了本库「Skills 层供应链攻击面」与「XPIA 防御量化天花板」两块长期缺口；iOS 27.1 beta「未发布但临近」状态被显式登记，为下一窗口「27.1 是否带新 App Intents API」留对照锚点。

### 需要改进的部分
Skill-Inject / Malicious Skills / SkillJect / PromptArmor / Zylos 具体 benchmark 数字均来自 arXiv 预印本 / 安全厂商综述转述，未逐字核对一手论文页，先不写精确百分数（避免编造评测数字）；Windows 09-19 Copilot 窗口 UX 调整的细节（已知文件夹 4 vs 6 的不一致）未深究，因其非框架级变更。

### 回流到 A 的新问题或素材
- 跟踪 iOS 27.1 beta（预期 09-21~23）是否引入新 `@AppIntent(schema:)` / App Intents Domains API 与 Messages 主动建议的 schema 映射。
- 跟踪 AppFunctions alpha12 是否落地 `@AppFunctionSignature` 动态注册 + `AppFunctionState` 之外的门控 API。
- 把 Skill-Inject / Malicious Skills / SkillJect 一手论文数字与「OS 级 Skill Registry 签名」机制做映射表（待补）。
- 延续既有待办：OWASP Agentic AI Top 10 2026 与库内 XPIA/Confirmation/Workspace 映射、Berkeley 官方 BFCL v4 榜逐字、Watch OS 26、NowSecure/AgentAntibody 一手复核、Chrome Origin Sets 官方 URL、Per-Intent Privacy Manifest 官方文档逐字、高通 NPU exact specs。
