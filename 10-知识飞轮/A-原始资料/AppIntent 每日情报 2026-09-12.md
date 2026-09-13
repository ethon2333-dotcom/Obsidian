---
date: 2026-09-12
tags: [AppIntent, 情报, 每日]
source: "https://m.mydrivers.com/newsview/1146302.html | https://baike.baidu.com/item/HarmonyOS%207/67704957 | https://baike.baidu.com/item/%E9%B8%BF%E8%92%99%E5%BA%94%E7%94%A8%E7%94%9F%E6%80%81/67746673 | https://aibacon.net/posts/cactus-needle-2-14mb-45m-tool-calling-model-esp32.html | https://petri.com/microsoft-entra-agent-id-preview/ | https://gbhackers.com/agentic-ai-feature/"
importance_score: "★★★★☆"
intent_category: 消费版铺开实测 / 跨平台A2UI落地 / 端侧Planner评测
---

# AppIntent 每日情报 2026-09-12

> [!abstract] 30 秒速览
> 本窗口（**2026-09-04 → 09-12，因自动化 9 天未跑而补跑，非仅 24h**）四大 OS **官方框架层 API 仍无净新增**（Apple iOS 27 守 Beta 5 已录 schema、Android AppFunctions 仍无 alpha12、HarmonyOS 7 框架同 HDC2026、Windows agentic security 四支柱一致）。真增量集中在**消费版铺开后的实测/认证数据 + 一处跨平台落地**：
> ① **HarmonyOS 7（9-7 正式发布后）披露安全与性能实测**——获**信通院增强级端云协同 AI 安全认证**（行业首个）、携手支付宝把欺诈损失率降 **35.8%**、盗用拦截率升 **42.3%**、高频应用流畅度 **+22%**、应用间跳转 **+25%**；
> ② **高德发布鸿蒙首个生成式 UI 开源框架 AGenUI，明确基于 Google A2UI 协议**（C++ 跨平台引擎把大模型生成的界面意图直接渲染成鸿蒙原生组件）——A2UI 首次有跨平台（Google 协议 → 鸿蒙原生）落地样本；
> ③ **Needle 2（45M）BFCL v4 跨模型对照 + attention-only 架构消融**獲第三方（aibacon）独立拆解：单轮 BFCL v4 Apple FM 61.7% / LFM2.5-230M 60.8% / FunctionGemma-270M 46.1% / Needle 2 42.6%；Seal-Tools 域外 Needle 2 **28.7% 居首**（LFM2.5 17.0% / FunctionGemma 15.6%）；well-formed 输出率 93.4%（与 Apple FM 同档）。
> 对 OS PM 的核心含义：四平台框架竞赛进入「**发布后真机实测与可信认证**」阶段，端侧 Planner 的「小模型 + 严格语法约束 + 置信门控」路线被反复独立印证。

## 净新增（索引 → B 笔记）

| 重要性 | 原子笔记 / 落点 | 主题枢纽 | 一手来源 |
|---|---|---|---|
| ★★★★★ | [[HarmonyOS Intents Kit 与 ArkAF 2026]]（补 9-7 后信通院增强级认证 + 支付宝反诈实测 35.8%/42.3% + perf 22%/25%） | [[原子服务]] ｜ [[XPIA 跨提示注入]] | https://m.mydrivers.com/newsview/1146302.html ｜ https://baike.baidu.com/item/HarmonyOS%207/67704957 |
| ★★★★ | [[A2UI 生成式UI协议(Google)与鸿蒙落地 2026]]（**新 B 节点**：高德 AGenUI 基于 Google A2UI 协议，跨平台落地） | [[意图框架·跨体系索引 MOC]] | https://baike.baidu.com/item/%E9%B8%BF%E8%92%99%E5%BA%94%E7%94%A8%E7%94%9F%E6%80%81/67746673 |
| ★★★★ | [[Function Calling 端侧工具调用]]（补 Needle 2 跨模型 BFCL v4 单轮对照 + Seal-Tools 域外 28.7% 居首） | [[Intent Router 语义路由]] | https://aibacon.net/posts/cactus-needle-2-14mb-45m-tool-calling-model-esp32.html |
| ★★★★ | [[端侧 Router 置信度门控与工具可达性收缩 2026]]（补 attention-only 消融 0.47→0.006 nats + grammar-constrained 跳过 98% 词表投影 + well-formed 93.4%） | [[Confirmation UI 安全机制]] | 同上 aibacon / arXiv 2607.18363 |
| ★★★ | [[Windows Copilot Actions 与 Agent Workspace 2026]]（补 build 26200.8313 / 26220.7262 + Settings「Agents」面板 +「@」调 Agent + 悬停监控） | [[Agent Workspace 隔离执行]] | https://petri.com/microsoft-entra-agent-id-preview/ ｜ https://gbhackers.com/agentic-ai-feature/ |

## 正文拆解

**① Schema 定义与语义路由机制**
- 本窗口**无新 Schema 协议级变更**。HarmonyOS 侧新增的「可迁移」进展在**执行层渲染**：高德 AGenUI 把「大模型生成界面意图 → 鸿蒙原生组件」做成开源框架，本质是 A2UI（Google 协议）在鸿蒙的落地，补全了「意图即服务」里「动态 UI 渲染」这一环（详见 [[A2UI 生成式UI协议(Google)与鸿蒙落地 2026]]）。
- 端侧 Planner 路由侧，Needle 2 的跨模型 BFCL v4 单轮对照（Apple FM 61.7% 居首）再次证明：**<1B 模型在 v4 加权最重的 agentic+multi-turn 上系统性落后，但在「窄域 + 严格语法约束」上可逼近大模型的 well-formed 率**（93.4%）。

**② 系统安全与用户体验（Confirmation / 隔离 / 防注入）**
- **HarmonyOS 把「意图即服务」的可信度从口号变成认证**：行业首个信通院增强级端云协同 AI 安全认证 + 支付宝反诈联合实测（损失率 -35.8% / 拦截率 +42.3%），是四平台里**首个把端侧 AI 反诈做成可量化第三方认证样本**的。
- **Windows** 仍是隔离执行标杆：新披露 build 26200.8313（Release Preview）把 Agentic 体验落进任务栏、build 26220.7262 进 Agent Workspace，「@」调 Agent + 悬停监控进度，把「用户始终在环」做成可感知交互。
- 端侧 Planner 的**结构性不可达**（Needle 2 工具可达性收缩）+ **低置信返回空而非硬猜**（93.4% well-formed 靠 byte-level grammar 约束）被第三方独立拆解印证，是防 ADI 的低成本双闸。

## 已复核·无净新增（避免重复检索）

- **Apple**：iOS 27 框架与 08-15 Beta 5 逐字一致；SiriKit 弃用 / App Intents 2.0 / Foundation Models / Core AI / Evaluations / App Intents Testing 均已录（见 [[Apple AppIntents Schema Protocol 2026]]），本窗口仅二手综述复述，无新 API。
- **Android**：AppFunctions 仍为 `1.0.0-alpha11`（2026-08-26 官方 Release Notes 当前最新），**无 alpha12**；`EXECUTE_APP_FUNCTIONS` 权限模型同 09-01 已录；Android 17（API 37）/ AppFunctions 私有预览均为 6 月材料，非窗口内新增。
- **HarmonyOS**：9-7 为消费版铺开档期（已录 09-03）；本窗口新增为**铺开后的实测/认证数据**（非新 API），已落入 [[HarmonyOS Intents Kit 与 ArkAF 2026]]。
- **Windows**：agentic security 官方文档四支柱（Agent accounts / Agent Workspace / Scoped file / MCP-ODR）与 08-09 以来一致；本窗口新增为第三方 tracker 披露的具体 build 号与交互细节（非官方 API 变更）。

## 我的问题 / 后续动作

- [ ] 用 Berkeley 官方 BFCL v4 榜复核 Needle 2（42.6%）与 Apple FM（61.7%）跨模型对照表；aibacon 为第三方引述。
- [ ] 9-7 后回填 HarmonyOS 7 消费版真实 API level（26 vs 23 冲突仍待官方文档）。
- [ ] 9-14 iOS 27 GA 后核查是否新增 per-intent 路由/来源声明 API（将重评 [[四平台意图 Registry 来源轴与权限模型对比 2026]] 来源轴结论）。
- [ ] 补查高德 AGenUI 是否真的遵循 Google A2UI 协议字段（当前为百度百科媒体口径，待官方仓库/文档核验）；AGenUI 的开源协议与鸿蒙原生组件映射表待补。
- [ ] 延续既有待办：Watch OS 26 / NowSecure / AgentAntibody / Chrome Origin Sets 官方 URL 复核。

> [!note] 概念节点双链
> [[意图模式规范]] ｜ [[语义路由]] ｜ [[端侧工具调用]] ｜ [[确认机制]] ｜ [[元服务]] ｜ [[隔离执行]] ｜ [[A2A 端侧智能体协议]] ｜ [[XPIA 跨提示注入]]
