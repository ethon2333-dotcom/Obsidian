---
type: raw
status: inbox
date: 2026-08-18
source:
  - "https://learn.microsoft.com/lb-lu/training/modules/manage-agents-microsoft-agent-365/2-enable-navigate-microsoft-agent-365"
  - "https://learn.microsoft.com/lt-lt/entra/agent-id/agent-registry-convergence"
  - "https://docs.com/is-is/microsoft-agent-365/overview"
  - "https://msftaisecurity.com/agent365"
  - "https://9to5mac.com/2026/08/17/ios-27-beta-6/"
  - "https://developer.android.com/ai/appfunctions/add-appfunctions"
  - "https://developer.huawei.com/consumer/cn/forum/topic/0202218387931162352"
  - "https://learn.microsoft.com/fil-ph/windows/security/book/operating-system-agentic-security"
importance_score: "★★★☆☆（7/10）"
intent_category: "智能体控制平面 / 身份基座（治理层）· 四平台官方渠道复核"
tags: [情报, AppIntent, 每日情报, Agent365, EntraAgentID, 治理层, 跨平台, 2026-08-18]
---

# AppIntent 每日情报 2026-08-18

> [!abstract] 30 秒速览
> - **核心突破**：微软 **Agent 365（智能体控制平面）+ Entra Agent ID（身份基座）** 已正式 GA（2026-05-01），本日经官方文档核实为**生产级统一智能体注册表 + agent 身份**，含**三种运行模式**（代用户 / 自主后台 / 协同预览）与 **Shadow AI 发现**。它属 **M365/Entra 治理与身份层**，与 Windows OS 执行总线（ODR + Agent Workspace）**正交**——直接升级本库 08-17 记的「Entra Agent Identity = 第三方解读待确认」为「官方已 GA」。
> - **关键指标**：GA 日期 2026-05-01；注册表收敛（原 Entra 注册表退休，统一到 Agent 365）；角色分级（AI Administrator / AI Reader 最小特权）；三模式治理。
> - **OS Agent 场景**：为 OS PM 设计「统一意图/智能体注册表 + agent 身份 + 运行模式分类」提供量产参照，直接补强「六方 Registry/权限 Checklist（此前仅 Android 填实）」。
> - **四大 OS 官方框架层经逐条复核无新增可执行 API**（Apple iOS 27 Beta 6 仅修修补补、Android AppFunctions 守 alpha10、HarmonyOS 处于 HDD 7-8 月巡回活动期无新 API、Windows OS agentic security 四支柱一致）。

## 正文拆解

### ① Schema 定义与语义路由机制（治理层视角）

本期窗口内**四平台 OS 级意图 schema 层无新增**（详见下方「已复核·无净新增」）。新增的 Agent 365/Entra Agent ID 落在**治理层**而非 schema 层，但其「统一注册表」机制本质是对**智能体能力发现**的治理化封装——与 OS 层意图 Registry（Apple schema / Android AppFunctions / HarmonyOS insight_intent.json / Windows ODR）形成「治理层注册表 ↔ OS 层执行总线」双层结构：

- **统一注册表 + 身份基座**：Agent 365 把散落在 Entra 与 M365 管理中心的 agent 入口收敛为单一控制平面；Entra Agent ID 为每个 agent 提供唯一身份、凭据、权限与 Conditional Access。
- **三模式分类**（OS 层极少显式区分，值得借鉴）：① Delegated access（代用户、delegated 权限）；② Own access / autonomous（自主后台）；③ Own access / collaborative（协同，预览）。
- 深层含义：四平台 OS intent Registry 只管「能力怎么声明/发现/调用」，而「agent 是谁、能不能跨组织、以什么身份运行」目前只有 Windows 有 Agent ID 雏形——Agent 365 给出可操作的全套范式。详见 [[Agent 365 与 Entra Agent ID 智能体控制平面与身份基座 2026]]。

### ② 系统安全与用户体验（Confirmation / 隔离 / 防注入）

- **治理层安全三支柱**：observe（实时可见）/ govern（统一生命周期与权限）/ secure（Entra 身份 + Purview 数据 + Defender 运行时防护）。与 08-04 本库结论「治理层有成熟数据溯源模型、OS 层全空白」互为印证；Agent 365 把它量产化。
- **Shadow AI 发现**：M365 管理中心新增 Shadow AI 页，纳入用户私装本地 agent（OpenClaw / GitHub Copilot CLI / Claude Code）与组织外 SaaS agent——对应「OS 层看不见的本地 agent 怎么治理」这一新盲区（与 08-09 晚 Chrome Agent Origin Sets 同属客户端/浏览器层产品化治理，但 Agent 365 是组织级）。
- **与 OS 执行隔离的关系**：Agent 365 管「身份与审批」，ODR/Agent Workspace 管「本机隔离执行」；两者经 MCP connector 衔接，**不可混写为「Windows OS 已内建 agent 注册表」**（层级纪律见 [[四平台意图 Registry 来源轴与权限模型对比 2026]]）。
- **四大 OS 官方安全机制经复核无变化**：Apple（Trust Insights + Confirmation UI + 锁屏鉴权）、Android（权限下放 App 自确认）、HarmonyOS（信任式免二次确认 + 端侧 A2A 不出端）、Windows（Agent Workspace 隔离 + XPIA 警示）均维持既有状态。

### 已复核·无净新增（避免下次重复检索）

| 平台 | 复核对象 | 结论 |
|---|---|---|
| Apple | iOS 27 Beta 6（build 24A5418b，08-17/18 发布，首入「一周一更」节奏） | 收尾期仅修 Bug（快捷指令健康数据记录、信息置顶遮挡等）+ 性能微调；**App Intents 2.0 schema 无新 API**（Siri AI / 屏幕感知 / 独立 Siri App 均为 WWDC 已知特性）。iOS 26.6.1（21 CVE 修复）为常规安全更新，非框架级。 |
| Android | AppFunctions（Jetpack 1.0.0-alpha10，2026-07-21 末次更新） | alpha10 稳定，无新发布；`@AppFunctionServiceEntryPoint` 编译期架构与 `EXECUTE_APP_FUNCTIONS` / `BIND_APP_FUNCTION_SERVICE` 权限细节维持 08-03/08-16 记录。Gemini 集成仍私有预览。 |
| HarmonyOS | Intents Kit / ArkAF / A2UI（HDC2026 06-12 发布，7-8 月 HDD 巡回） | HDD 为开发者活动，**无新 API**；2100+ Skill / 1200+ 底层能力 Skill 化口径与 08-17 一致（2100+ vs 1200+ 冲突仍标待官方澄清）。 |
| Windows | OS agentic security 四支柱 + ODR + Agent Workspace | 官方 learn.microsoft.com agentic security 文档四支柱（distinct agent accounts / limited privileges / operational trust / privacy-preserving）与既有记录一致；Copilot Actions / Agent Workspace 仍 Insider 预览、默认关。Agent 365 属治理层，非 OS 总线新增。 |

> [!note] 概念节点双链
> [[意图模式规范]] [[语义路由]] [[端侧工具调用]] [[确认机制]] [[元服务]] [[隔离执行]] [[A2A 端侧智能体协议]] [[XPIA 跨提示注入]]

## 值得保留的点（索引）

- **★7/10 · 净新增**：Microsoft Agent 365 + Entra Agent ID 控制平面与身份基座（GA 2026-05-01，治理层）—— 原子笔记 → [[Agent 365 与 Entra Agent ID 智能体控制平面与身份基座 2026]] ｜ 主题枢纽 → [[意图框架·跨体系索引 MOC]]
- **★6/10 · 上下文（市场数据·非框架级）**：Counterpoint 数据称 2026 Q1 鸿蒙中国智能手机系统份额 19% 首超 iOS 17%（08-18 多家媒体转载）。属市场信号，非框架/API 变更，供 OS PM 竞争感知，不建 B 节点。
- **★0/10 · 已复核无净新增**：Apple iOS 27 Beta 6 / Android AppFunctions alpha10 / HarmonyOS HDD 巡回 / Windows OS agentic security 四支柱 —— 见上表，下次不再重复检索。

## 后续动作

- [ ] 将 Agent 365 三模式 + 统一注册表 + Agent ID 对照进「六方 Registry/权限 Checklist」（当前仅 Android 填实）
- [ ] 核验 Agent 365 与 Windows ODR 的 connector 衔接细节（治理层 ↔ OS 执行层边界）
- [ ] 延续：Berkeley 官方 BFCL v4 博客原文；Watch OS 26 是否 Trust Insights 类；NowSecure / AgentAntibody 独立核验；Chrome Origin Sets 官方 URL 逐字复核
