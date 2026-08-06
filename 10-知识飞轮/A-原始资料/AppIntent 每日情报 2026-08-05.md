---
type: raw
status: processed
source: "WebSearch / WebFetch 直取官方源（Horizon MCP 连续 7 日全部 disconnected）+ 本 Agent 自行综合"
captured: 2026-08-05
tags: [AppIntent, 情报, 2026-08-05]
window: "7 日滚动窗口 2026-07-30 → 2026-08-05"
intent_category: "系统级 Agent 执行总线 / 端侧 Planner 意图路由"
importance_score: "★★★☆☆（7/10，窗口内真增量 2 条 + 1 条口径待办关闭）"
---

# AppIntent 每日情报 2026-08-05（自动化 21:00 版）

> [!abstract]
> 本期 7 日滚动窗口内，**四大 OS 官方渠道经逐条复核无新增可执行 API**（Apple App Intents 2.0 / Android AppFunctions 实验态 / HarmonyOS ArkAF 均为既有记录，无净新增）。窗口内**两条真增量**：① **Windows Agent Launchers** —— 一个此前未被本库记录的系统级 Agent 注册表，基于 App Actions 框架 + ODR，通过 `com.microsoft.windows.ai.agentInfo` AppExtension 与 `odr.exe agent-info add/remove/list` 发布 agent 自身（区别于 ODR 已有的 MCP 连接器注册），直接对标 Apple App Intents / Android AppFunctions / HarmonyOS Intents Kit；② **LFM2.5-2.6B**（Liquid AI，2026-08-04 发布）端侧 agentic 小模型，官方称在 BFCLv4 上可比 4–10× 更大的模型。另**关闭一条延续待办**：BFCL v4 权重公式（Agentic 40% / Multi-Turn 30% / Live+NonLive+Hallucination 各 10%）经 EvalScope 官方文档交叉确认，升级为「已核实口径」。

## ① 窗口内真增量

### 增量 1 · Windows Agent Launchers —— 系统级 Agent 注册表（重要性 7–8/10）

**是什么**：Windows 在 App Actions 框架之上新增一层** agent registry**，让打包应用把「自己提供的 agent」注册到系统，供 M365 Copilot 等宿主发现与调用。这是本库此前在 Windows Copilot Actions 笔记里**未记录**的一类注册表（该笔记此前只覆盖 ODR 的 MCP 连接器注册）。

**已核实技术细节（来源：learn.microsoft.com `/windows/ai/agent-launchers/` 与 `agents-get-started`，官方文档，非博客日期口径）**：

- **AppExtension 名**：`com.microsoft.windows.ai.agentInfo`
- **注册清单 `agentRegistration.json` 字段**：`manifest_version` / `version` / `name` / `display_name` / `description` / `placeholder_text` / `icon` / `action_id`（**必须匹配一个已定义的 App Action id**）
- **ODR 命令**：`odr.exe agent-info add "<path>"` ｜ `odr agent-info remove "<path>"` ｜ `odr agent-info list`
- **底层 = Windows App Actions 框架**：一个 App Action 需要 `agentName` + `prompt` 两个输入，可选 `attachedFile`
- **两种注册时机**：静态（install-time）/ 动态（runtime）
- **已知用户**：M365 Copilot 的 Analyst、Researcher 等 agent 走此机制
- **约束**：动态 ODR 注册要求打包应用具备 package identity；官方文档**未提及需额外 Capability 声明**

**对四平台对比的意义**：这补齐了本库长期「Windows 只有 MCP 连接器注册（ODR）」的认知缺口。现在 Windows 有**两层注册表**——
- ODR 的 MCP 连接器注册（注册「能调什么工具/服务」）
- Agent Launchers 的 agent 注册（注册「系统里有哪些可用的 agent 实体」）

二者叠加后，Windows 的「系统级意图框架」形态与 Apple（App Intents 发布 intent）、Android（AppFunctions 发布 function）、HarmonyOS（Intents Kit 发布 intent/Want）**首次在「应用向系统声明可被调用的能力」这一层对齐**，只是 Windows 的颗粒度目前是 agent 实体而非细粒度 intent/function。

**待补/存疑（诚实标注）**：
- Agent Launchers 的**具体 Insider 预览 build 号与发布日期**待补（官方文档页无日期，博客 URL 经核实为 7522 build 共享贴，非独立发布日）。
- 动态注册的**安全闸口细节**（是否需签名、是否被用户开关管控）官方文档未明示，仅知需 package identity；是否落入 08-02 笔记记的 `Settings > System > AI components > Agent tools > Experimental agentic features` 同一 opt-in 开关**待确认**。
- 与 XPIA 缓解的关系：agent 被注册进系统后，宿主调用它的信任链（谁批准、是否用户可审计）**待补**。

### 增量 2 · LFM2.5-2.6B —— 端侧 agentic 小模型新成员（重要性 7/10）

**发布**：Liquid AI，2026-08-04（窗口内）。**参数**：2.6B，定位 on-device agentic。

**官方/厂商自述规格（待第三方复现）**：
- 速度：Apple M5 Max **220 tok/s**、Ryzen AI Max **113 tok/s**、手机约 **30 tok/s**
- 内存占用 **< 2.5GB**
- 架构：LIV convolutions + selective attention
- 厂商称在 **BFCLv4 / ToolSandbox / Claw-Eval** 上可竞争 4–10× 更大的模型

**对库的意义**：本库端侧 Planner 评测表此前有 LFM2.5-8B-A1B（49.7% BFCLv4）、LFM2.5-230M（21.0%）、LFM2.5-VL-450M（21.1%）。新增 2.6B 这一档，使 LFM2.5 家族在「端侧 agentic」形成 **230M / 450M(VL) / 2.6B / 8B-A1B** 的完整规模阶梯，便于讨论「哪些规模适合路由、哪些适合端到端」。

**待补/存疑（诚实标注）**：
- 上述基准数字为**厂商自述**，非 Berkeley 官方榜行，引用需标「厂商口径未复现」。
- 具体 BFCLv4 分数值**待补**（仅知「竞争 4–10× 更大模型」这一相对表述）。

## ② 延续待办关闭：BFCL v4 官方权重确认（重要性 6/10，属「口径」非新事实）

**原待办**：2026-08-04 将「BFCL v4 权重重构」记为核心结论，但当时权重数字来自第三方拆解（基准末次更新 2026-04-12），标注「Berkeley 官方博客原文待补」。

**本期进展**：经 **EvalScope 官方文档**交叉确认，BFCL v4 权重公式为：

| 类别 | 权重 |
|---|---|
| Agentic | **40%** |
| Multi-Turn | **30%** |
| Live | 10% |
| Non-Live | 10% |
| Hallucination | **10%** |

**状态升级**：从「08-04 的二手快照」升为「**已核实（EvalScope 官方文档交叉确认）**」。方向性（v4 = holistic agentic evaluation）进一步坐实。库内历史 BFCL 分数版本标签策略（v3 格式合规分与 v4 不可比）维持不变。

**仍为待补**：Berkeley 官方博客/论文原文逐字表述，以及「该权重是否已是当前全量榜最终版」尚未从一手源闭合——EvalScope 为评测框架文档，非 Berkeley 本体。

## ③ 已复核·无净新增（四大 OS 官方渠道逐条比对，避免下次重复检索）

- **Apple**：逐条比对 WWDC26 / iOS 27 开发者指南，App Intents 2.0（Session 345 的 streaming/富实体/多轮 + Session 343 的 View Annotations/IntentValueQuery/Confirmations+entity ownership）均为既有记录，**窗口内无新增 API 变更**。
- **Android**：AppFunctions 仍处 experimental / private preview（alpha10 编译时入口点 + Registry 硬细节已在 08-03 详录），**窗口内无新 API**。
- **HarmonyOS**：ArkAF / 意图框架相关文章经核实发表日期为 **2026-06-17**，**在 7 日窗口之外**，不记为本期增量（已并入既有 HarmonyOS 笔记，不重复登记）。
- **Windows**：agentic security 官方文档四支柱（隔离/会话/签名/用户中断）与 08-04 记录一致；Agent Launchers 虽为新发现，但属对既有 ODR/App Actions 框架的**补全**而非新安全范式，已在增量 1 单独记录。

## ④ 排除条目（过滤纪律，避免误判阈值）

本期候选池中**无非 OS 级 / 纯营销 / 概念-only 论文**需排除；所有低于 6/10 的窗口内碎片信号（如厂商例行模型更新、泛 AI 新闻）已在检索阶段按既有规则丢弃，未进入本笔记。

---

> [!note]
> 关联概念：
> [[意图模式规范]] · [[语义路由]] · [[端侧工具调用]] · [[确认机制]] · [[元服务]] · [[隔离执行]] · [[A2A 端侧智能体协议]] · [[XPIA 跨提示注入]]

## 后续动作

- [ ] 核实 Agent Launchers 具体 Insider build 号 / 发布日期与 opt-in 开关归属
- [ ] 核实 LFM2.5-2.6B 的 BFCLv4 具体分数（厂商口径未复现）
- [ ] 【连续第 5 日未解，最高优先】四平台是否采纳意图元数据来源分级（Apple `.appEntityIdentifier` 来源绑定/签名仍待补）
- [ ]  Berkeley 官方 BFCL v4 博客原文逐字确认
- [ ] 沿用既有待办：PrismML 技术报告、APOP 协议全文与对接、六方 Registry Checklist（仍仅 Android 填实）、Digital Omnibus 正式文本、HarmonyOS 银行 App 名、Per-Intent Privacy Manifest、荣耀 Robot Phone、Måløy 类别级缓解
