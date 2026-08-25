---
type: daily-index
status: index
captured: 2026-08-03
window: "7 日滚动窗口 2026-07-27 → 2026-08-03"
intent_category: "系统级意图框架 / 端侧 Agent 执行总线 / 执行安全（ADI · Stored IPI · 带外防御）/ 端侧 Planner 实测"
importance_score: "★★★★★（9/10，执行安全第三个分水岭 ADI + 4 条库内高价值空白补齐；窗口内真增量仅 1 条）"
tags: [AppIntent, 情报, 索引, 2026-08-03]
---

# AppIntent 每日情报 2026-08-03（索引）

> [!abstract]
> 本期最重的一条是**执行安全的第三个分水岭**：**ADI（Agent Data Injection）证明攻击者不需要注入「指令」**，只要伪造 Agent 视为可信的结构化元数据即可（同环境对照：经典指令注入 0–0.7%，ADI 最高 **100%**），六款商用 Agent 全部中招，唯一归零的 CaMeL Strict 代价是可用性掉到 36.5%。姊妹论文 **DualView** 补刀：隔离机制不是被绕过，是**生命周期被绕过**（Stored IPI 仍 53.3%）。OS 侧两条硬信息：**Android alpha10 `@AppFunctionServiceEntryPoint`** 把 Schema 从手写变编译产出并补齐 Registry / 权限 / 运行时门控 API 级细节；**Google 明示「系统智能体可能在服务器上处理用户查询」**，且把破坏性动作确认下放给 App——与 Apple 系统级 Confirmation 正面分叉。窗口内真增量 1 条：DroiClaw 诸葛中国市场正式发布。

## 本期条目索引

| 重要性 | 条目 | 原子笔记（完整内容） | 主题枢纽 | 一手来源 |
|---|---|---|---|---|
| 10/10 | **ADI 数据注入攻击**：攻击不再需要「指令」，伪造结构化元数据即可；概率性分隔符注入；三类场景（任意点击 / RCE / 供应链）；六款商用 Agent 全中；Anthropic·OpenAI·Google 已确认 | [[Agent Data Injection 数据注入攻击]] | [[XPIA 跨提示注入]] · [[MCP 与设备侧 MCP]] | [arXiv 2607.05120](https://arxiv.org/abs/2607.05120) ｜ [CSA 研究简报 2026-07-18](https://labs.cloudsecurityalliance.org/research/csa-research-note-agent-data-injection-attack-class-20260718) |
| 9/10 | **Android AppFunctions 1.0.0-alpha10**：编译时 `@AppFunctionServiceEntryPoint` 替代 `AppFunctionConfiguration.Provider`；KSP 生成 service 类 + XML schema；Registry/权限硬细节（`BIND_APP_FUNCTION_SERVICE`、`android.app.appfunctions.v2`/`app_metadata`）；`isEnabled=false` + `setAppFunctionEnabled` 运行时动态门控；官方 agent skill 自动迁移 | [[Android AppFunctions 设备侧意图 2026]] | [[App Intent 的核心作用]] · [[MCP 与设备侧 MCP]] · [[Intent Schema Protocol 意图模式规范]] | [developer.android.com · add-appfunctions](https://developer.android.com/ai/appfunctions/add-appfunctions)（末次更新 2026-07-21）｜ [AppFunctions agent skill](https://github.com/android/skills/tree/main/device-ai/appfunctions) |
| 9/10 | **确认机制路线分歧 + 第四维「确认内容完整性」**：Android 把破坏性动作确认下放给 App（并建议多加一步）vs Apple 系统级 Confirmation + entity ownership；叠加 AIMS「本地点击 ≠ 授权」，得出三档判据，四平台均在 1–2 档 | [[Confirmation UI 安全机制]] · [[Agent 身份与硬件级审批]] | [[Apple Intelligence 与 App Intents]] · [[安卓厂商意图识别破局策略]] | [developer.android.com · add-appfunctions](https://developer.android.com/ai/appfunctions/add-appfunctions) ｜ [arXiv 2606.26479](https://arxiv.org/abs/2606.26479) |
| 8/10 | **DualView / Stored IPI**：传统 Dual LLM 对即时注入 ASR≈0 但存储型仍 **53.3%**（Claude Haiku 4.5）；AgentView 恒符号 / HumanView 保原文；Git worktrees + OpenClaw 插件 + 仅 tool hooks；PinchBench 147 任务全阻断、可用性近基线 | [[Dual View 智能体数据视图隔离]] | [[Agent Workspace 隔离执行]] · [[XPIA 跨提示注入]] | [arXiv 2607.03821](https://arxiv.org/abs/2607.03821) ｜ [secrss 中文详解](https://www.secrss.com/articles/92279) |
| 8/10 | **带外防御系统化「门不能是模型」**（🆕 本期新建节点）：参考监视器移出模型、确定性门控；in-band 无保证（Nasr >90% 攻破 12 种）；ASR 25.8%→2.6% 但可用性 ~45%→~26%、调用 **~15×**；AIMS「LLM MUST NOT hold credentials」 | [[带外防御与确定性门控]] | [[XPIA 跨提示注入]] · [[Context Engineering 学习笔记]] | [arXiv 2606.26479](https://arxiv.org/abs/2606.26479) |
| 8/10 | **LFM2.5-8B-A1B + LocalCowork**：8.3B 总参/1.5B 激活 MoE、128K 上下文、BFCLv3 64.36 / IFEval 91.84 / Tau2 Telecom 88.07（厂商口径）；单笔记本 13 MCP server / 67 工具、`ask-propose-confirm-run` 亚秒级 dispatch + 完整审计轨迹、数据不出机 | [[Function Calling 端侧工具调用]] | [[端侧意图框架 学习笔记]] · [[MCP 与设备侧 MCP]] | [Liquid AI · LFM2.5-8B-A1B](https://www.liquid.ai/blog/lfm2-5-8b-a1b)（2026-05-28） |
| 7/10 | **「执行在端侧」≠「理解在端侧」**：Google 官方明示 `system agents may process user queries on the server`；修正本库 local-first 表述，端云边界三问判据（理解在哪 / 执行在哪 / 数据落哪） | [[Android AppFunctions 设备侧意图 2026]] | [[MCP 与设备侧 MCP]] · [[Apple Intelligence 与 App Intents]] | [developer.android.com · add-appfunctions](https://developer.android.com/ai/appfunctions/add-appfunctions) |
| 6/10 | **窗口内真增量：DroiClaw 诸葛中国市场正式发布**（08-03）：新华社发文；架构口径首次明确——本地小模型 + 云端大模型端云协同、「无 App 交互」Agentic OS、需求理解/规划/调度融入 OS 底层、开放模型接入、用户可创建 AI Skill；首批预装酷派小方块（2026-06） | [[Agentic OS 意图调度内核]] | [[国内安卓厂商做 App Intent 的阻力]] · [[App Infra 应用基建]] | [chinaz 2026-08-03](https://www.chinaz.com/2026/0803/1768702.shtml) |

> 说明：本笔记为**索引**，不内联分析。每条信息的完整技术细节、字段清单、数字表格、待补项均在上方「原子笔记」链接中。

## 已复核·无净新增（避免重复检索）

- **检索口径**：延续 08-02 确立的 **7 日滚动窗口（2026-07-27 → 2026-08-03）**，严格窗口内 OS 级硬命中仅 **1 条**（DroiClaw）。其余 5 条为**库内空白补漏**，均标真实一手日期（ADI/DualView 发表于 07-06、CSA 简报 07-18；带外防御 2026-06；LFM2.5 2026-05-28；Android 文档末次更新 07-21），**未冒充当日新闻**。
- **信息源纪律**：Horizon MCP 全部 disconnected，改用官方源与 arXiv 一手页直取；ADI / DualView / 带外防御数字**未复现**，LFM2.5 分数为厂商自述 + 第三方模型库转载，**非实测**，一律标口径。
- **跨日待办部分推进**：挂了 5 天的「四平台 Registry/权限横向 Checklist」——**Android 一列已用官方文档填实**（权限 / manifest 属性 / 动态门控 / 验证命令 / 错误语义），Apple / HarmonyOS / Windows 三列仍待补 → [[Android AppFunctions 设备侧意图 2026]]。
- **合规交叉信号**：Apple 因 **DMA** 在欧盟延迟发布 iOS 27 / iPadOS 27 的 Siri AI（Apple Newsroom 2026-06-08），与 08-02 记录的 **EU AI Act Article 15 已生效**方向相反——**DMA 要开放互操作、AI Act 要可控可举证**，可能是 2026 下半年 OS Agent 区域化分裂的起点 → [[Apple AppIntents Schema Protocol 2026]]、[[Windows Copilot Actions 与 Agent Workspace 2026]]。
- **同期参考**：Liquid AI 2026 发布节奏 LFM2.5-350M（03-31）→ 8B-A1B（05-28）→ Retrievers（06-18）→ 230M（06-25），非本期重点 → [[Function Calling 端侧工具调用]]。

## 排除项

- **荣耀 Robot Phone / AgenticOS**（07-18 WAIC，8 月发售）：AgenticOS 本身 08-01 已入库；Robot Phone 截至本期仍为预约状态未实际发售，无新 OS 级 API/Registry 信息。**保留为待办跟踪**。
- **Microsoft Project Polaris / GitHub Copilot 换引擎**（2026-08）：编码模型替换，非 OS 级意图框架 / 执行总线变更，低于阈值。
- **M365 Copilot UI 统一 / 经典版 Outlook 加 Copilot 入口**（2026-08）：应用层 SaaS，延续 08-02 同类排除判定。
- **HalluSquatting 僵尸网络式注入**（07-08 Ars Technica）：目标为 AI 编码助手而非 OS Agent 执行总线，威胁模型已被 [[文档型 XPIA 自传播蠕虫]] 覆盖，仅作旁证。
- **Apple iOS 27 Siri AI 候补名单 / SiriKit 弃用时间线**（06-08 起）：07-31 / 08-01 / 08-02 已覆盖，唯一新点（DMA 欧盟延迟）已记入上节。

## 未决问题（→ 各自 B 笔记跟踪，不在本索引展开）

- 【本期最高优先】四平台意图元数据（`AppFunctionMetadata` / `AppEntity` 标识符 / A2A 消息格式）是否做来源校验与完整性保护？有无 ADI 类别评估？→ [[Agent Data Injection 数据注入攻击]]
- Apple `.appEntityIdentifier` 是否有签名 / 来源绑定，还是纯字符串信任？→ [[Apple AppIntents Schema Protocol 2026]]
- Apple / HarmonyOS / Windows 是否有等价于 `setAppFunctionEnabled` 的 Registry 动态可见性 API（填满六方 Checklist）→ [[Android AppFunctions 设备侧意图 2026]]
- Android 把破坏性动作确认下放给 App，是否会有 Play 审核层强制要求？App 不做确认时系统兜底吗？→ [[Confirmation UI 安全机制]]
- OS 该不该把「Agent 视图文件系统」做成一等公民？系统级实现阻力是什么？→ [[Dual View 智能体数据视图隔离]]
- CaMeL Strict 的 36.5% 可用性能否优化，还是「ADI 归零」与「Agent 可用」当前架构下不可兼得？→ [[Agent Data Injection 数据注入攻击]]
- 带外门 ~15× 调用在端侧是否有更省等价物（TEE / 安全芯片内的确定性门）？GCG 白盒攻击能否攻破？→ [[带外防御与确定性门控]]、[[Agent 身份与硬件级审批]]
- 自动生成的工具描述（Agent 写 KDoc）若有歧义导致误执行，责任在谁？→ [[Intent Schema Protocol 意图模式规范]]
- 跟踪 Anthropic / OpenAI / Google 对 ADI 的**类别级**缓解；评估是否用作者公开的 AgentDojo 扩展版自建端侧 ADI 回归集 → [[Agent Data Injection 数据注入攻击]]
- 延续待办：Digital Omnibus 正式文本；HarmonyOS 银行 App 名与 1000+ 意图清单；Per-Intent Privacy Manifest 是否真实 API；Android Agent Skill 发布日期；荣耀 Robot Phone 实际发售；Måløy Word 蠕虫类别级缓解

> [!note] 关联枢纽
> **MOC**：[[意图框架·跨体系索引 MOC]] ｜ **主题枢纽**：[[App Intent 的核心作用]] · [[Apple Intelligence 与 App Intents]] · [[MCP 与设备侧 MCP]] · [[国内安卓厂商做 App Intent 的阻力]] · [[安卓厂商意图识别破局策略]] · [[端侧意图框架 学习笔记]] · [[App Infra 应用基建]]
> **本期原子笔记**：[[Agent Data Injection 数据注入攻击]] · [[Dual View 智能体数据视图隔离]] · [[带外防御与确定性门控]] · [[Android AppFunctions 设备侧意图 2026]] · [[Confirmation UI 安全机制]] · [[Agent Workspace 隔离执行]] · [[Function Calling 端侧工具调用]] · [[Agentic OS 意图调度内核]] · [[XPIA 跨提示注入]] · [[Agent 身份与硬件级审批]]
> **方法（C 层）**：[[Agent 读入路径可信数据边界 SOP]] ｜ [[Agent 写回路径 XPIA 风险评估 SOP]]
