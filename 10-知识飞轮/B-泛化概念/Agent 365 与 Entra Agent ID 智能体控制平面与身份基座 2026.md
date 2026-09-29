---
type: concept
status: draft
date: 2026-08-18
derived_from: "[[AppIntent 每日情报 2026-08-18]]"
source:
  - "https://learn.microsoft.com/lb-lu/training/modules/manage-agents-microsoft-agent-365/2-enable-navigate-microsoft-agent-365"
  - "https://learn.microsoft.com/lt-lt/entra/agent-id/agent-registry-convergence"
  - "https://docs.com/is-is/microsoft-agent-365/overview"
  - "https://msftaisecurity.com/agent365"
importance_score: "★★★☆☆（7/10）"
intent_category: "智能体控制平面 / 身份基座 / 治理层（M365·Entra）"
tags: [概念, 智能体治理, 控制平面, 身份基座, Registry, 跨平台参照, 2026-08-18]
aliases: [Agent 365, Entra Agent ID, 智能体控制平面]
---

# Agent 365 与 Entra Agent ID 智能体控制平面与身份基座 2026

## 一句话定义

**Agent 365** 是微软的「智能体控制平面（control plane for AI agents）」——一个统一的智能体注册表 + 治理台，用来发现、审批、管控、审计组织内所有智能体（含 Microsoft、第三方、自定义）；**Entra Agent ID** 是其底层**身份基座**，为每个 agent 提供唯一身份、凭据、权限与条件访问策略。注意：它属于 **M365 / Entra 治理与身份层**，与 Windows OS 执行总线（ODR + Agent Workspace + Copilot Actions）**正交**，不直接等于 OS 级意图框架。

## 为什么重要

- 本库追踪 8 轮的最高优先待办之一是「四平台意图 Registry 来源轴与权限模型对比」，且一直标注 **Windows Entra Agent Identity = 第三方解读、待官方确认**。本期把它**从「待确认」升级为「官方已 GA」**：Agent 365 于 **2026-05-01 正式 GA**，Entra Agent ID 为其身份基座——给 OS PM 设计「统一智能体注册表 + agent 身份」提供了**生产级参照**，而非仅研究/开源设想。
- 它把「治理层已有成熟模型、OS 层全空白」的结论（08-04 起）进一步坐实：微软在**治理/身份层**已量产（统一注册表 + 身份 + 三种运行模式 + Shadow AI 发现），而四平台 **OS intent 总线层**仍不记 provenance（见 [[四平台意图 Registry 来源轴与权限模型对比 2026]]）。
- 对「六方 Registry/权限 Checklist（仍仅 Android 填实）」是直接补强：Agent 365 的「统一注册表 + Agent ID 身份 + 角色分级 + 三种运行模式」可逐条对照进 OS 级 Registry 设计。

## 适用边界

- **层级**：M365 / Entra **治理与身份层**，**不是 Windows OS 内核级执行总线**。它治理「有哪些 agent、谁能调什么、身份与审计」，而 ODR/Agent Workspace 治理「agent 在本机怎么隔离执行」。两者经 MCP connector 衔接，但**不要写成「Windows OS 已内建 agent 注册表」**——那是 08-04 已校正过的层级误读。
- **许可**：Agent 365 GA 需 Microsoft 365 Copilot 许可（E5 最佳）；基础库存查看（AI Reader 角色）不强制许可，但应用 Conditional Access / 身份治理需 Entra Agent ID 许可。
- **时间线**：Agent Registry 已从 Entra 收敛到 Agent 365（2026-05-01 原 Entra 的 Agent Registry / Agent collections 区块退休，完整清单移入 M365 管理中心 Agent 365）；旧 `/beta/agentRegistry/...` Graph API 将被 `/beta/copilot/admin/...` 取代。

## 证据与例子

### ① 统一注册表（Unified Registry）+ 控制平面

- Agent 365 = 「observe / govern / secure」三支柱：实时可见全部 agent、统一生命周期与权限治理、端到端安全（Entra 身份 + Purview 数据 + Defender 运行时防护）。
- 注册表收敛：原先 agent 散落在 Entra 与 M365 管理中心多个入口；现**统一到 Agent 365 作为单一控制平面**。状态含 Available / Blocked / Pending，操作 Publish/Reject/Block，可逆。
- 角色分级：AI Administrator（全量治理）、AI Reader（最小特权只读库存）、Global Reader、Security 系列（监视不可治理）；身份管理员用 Entra 管理中心管 Agent ID、蓝图、权限、Conditional Access。

### ② 身份基座：Entra Agent ID

- 为每个 agent 提供**唯一身份 + 凭据 + 权限**，使 agent 行为与人活动可区分、可审计、可吊销。
- 三种运行模式（govern 的颗粒度参照）：
  1. **Delegated access（代表用户）**：以登录用户身份、按 delegated 权限响应 prompt——最常见。
  2. **Own access / autonomous（自主后台）**：自带凭据，无用户上下文，按计划/事件自主跑。
  3. **Own access / collaborative（协同，预览）**：自带凭据，参与团队频道/会议/共享工作区。
- 这一「三模式」是 OS 级意图框架设计时**极少被显式区分**的维度：当前四平台对「agent 是代用户、还是自主、还是协同」多在权限/Workspace 层含糊处理，Agent 365 给出了可操作的分类。

### ③ Shadow AI 发现（"new as of GA"）

- Agent 365 在 M365 管理中心新增 **Shadow AI 页**，发现用户私自安装的本地 agent（OpenClaw、GitHub Copilot CLI、Claude Code）与组织外 SaaS agent——直接回答「OS 层看不见的本地 agent 怎么纳入治理」。这与本库 08-09 晚记的「Chrome Agent Origin Sets」同属「客户端/浏览器层产品化治理」，但 Agent 365 是**组织级**而非单浏览器。

## 可复用启发

1. **OS PM 设计 Registry 时，把「身份 + 注册表 + 运行模式」三件套当默认值**：Agent 365 证明量产控制平面 = 统一注册表（发现/审批/封锁）+ 每 agent 唯一身份（Entra Agent ID）+ 显式三模式（代用户/自主/协同）。四平台 OS 层目前只有 Windows 有 Agent ID 雏形，其余缺失。
2. **治理层与 OS 执行层要分层设计、经 connector 衔接**：Agent 365（治理）↔ ODR（OS 执行）经 MCP connector 打通，但职责不混——这给「OS 原生意图框架要不要自带治理」的答案：**OS 层管执行隔离与权限，治理/身份可下沉到平台级控制平面**（如厂商云侧账号体系）。
3. **Shadow AI 是 OS 层的新盲区**：用户侧的本地/第三方 agent 不被 OS 意图总线纳管。Agent 365 的组织级发现思路可借鉴为「OS 级 agent 清单 + 越权上报告警」。
4. **沿用本库口径纪律**：Agent 365 的「GA 2026-05-01」「三模式」均来自官方 learn.microsoft.com / docs.com 文档；msftaisecurity.com 为第三方镜像站，细节（如 Shadow AI 页、安全覆盖矩阵）以官方文档复核为准。

## 关联

- 索引：[[意图框架·跨体系索引 MOC]]
- 直接对照：[[四平台意图 Registry 来源轴与权限模型对比 2026]]（升级其「Entra Agent Identity 待官方确认」→ 已 GA；补「治理层控制平面」参照）
- 同层治理：[[数据溯源分级与单调棘轮]]（08-04 治理层六类来源/四级密级模型，与 Agent 365 治理层互为印证）
- 身份/隔离：[[Agent 身份与硬件级审批]]（Apple Secure Enclave 硬件级确认，与 Entra 软件级身份基座对照）｜ [[隔离执行]]（Windows Agent Workspace）
- 平台原子：[[Windows Copilot Actions 与 Agent Workspace 2026]]（OS 执行层，与本笔记治理层正交）｜ [[Windows Agent Framework 端侧 Agent 执行框架 2026]]
- 枢纽：[[意图模式规范]] · [[语义路由]] · [[确认机制]] · [[XPIA 跨提示注入]]

#标签/智能体治理 #标签/控制平面 #标签/身份基座 #标签/Registry #标签/跨平台参照

## 2026-09-21 增补：Foundry 托管智能体网络出网控制 public preview（来源 [[AppIntent 每日情报 2026-09-21]]）

> 接续 08-18 的「Agent 365 = 治理/身份层控制平面（与 Windows ODR / Agent Workspace 执行层正交）」。本期补 **Azure 更新批次（09-18，CSDN 09-20 报道）** 在 Agent 365 治理层新增的**第三项出网治理能力**——把「托管智能体运行时能连谁」从「不可控」变为「可写有序规则」。

- **托管智能体的网络出网控制进入公开预览**：管理员可写**一组有序规则，按目标主机匹配**，支持 `*.contoso.com` 这样的 **FQDN 通配**；动作有四种——**允许 / 拒绝 / 改写出站请求头 / 改写目的地**。
- **与既有治理三块拼图构成完整句**：① 从 Foundry 直接把智能体发布到 Microsoft 365 Copilot 与 Teams（正式可用，不再需自建部署流水线，且继续走 Entra + Agent 365 治理）；② Agent 365 治理界面里 Foundry 智能体现有**启用/停用**两个管理员动作（Microsoft 管理中心，提权模式与其他 agent 应用动作一致）；③ 出网控制（public preview）。
- → 对 OS PM 的含义：Agent 365 把「治理层控制平面」从「发现/审批/身份」扩展到「**运行时出网边界**」——这是治理层对 [[XPIA 跨提示注入]]「假定注入必然发生、用边界压爆炸半径」元判断的组织级落地（对照 [[Chrome Agent Origin Sets 与用户对齐评判器 2026]] 的客户端读写源集）。对本库「六方 Registry/权限 Checklist」补强：治理层现含**出网白名单 + 动作改写**维度。
⚠️ 层级纪律：这是 **Azure Foundry + Agent 365 + Entra 治理/身份层**，非 Windows OS 执行总线（ODR / Agent Workspace）；勿写成「Windows OS 已内建出网控制」。来源为 CSDN 微软技术日报（09-20）对 Azure 09-18 更新批次的转述，具体 GA 日期与规则语法**待 learn.microsoft.com 逐字复核**。

## 2026-09-25 补捕：Declarative Agents 支持 Skills 转入 GA（来源 [[AppIntent 每日情报 2026-09-25]]）

> 接续 08-18「Agent 365 = 治理/身份层控制平面」与 09-21「Foundry 出网控制」。本期补 **Microsoft 365 Copilot Declarative Agents 支持 Skills（Message Center MC1476977，2026-09-22 公布，9 月中~月底全球 GA）**——把「智能体技能打包 + 安全沙箱执行」补进治理层拼图。

- **Skills = 模块化可复用能力单元**：把指令、脚本、模板、关联资源打包为一个可加进 agent 的模块；按需加载（改善上下文效率与响应质量），跨多个 agent 复用；脚本执行走**安全沙箱**，skill 文件上的 **MIP 敏感度标签保留并生效**，既有治理控制继续适用。
- → 对 OS PM 的含义：微软治理层把「Agent Skill 上架 + 沙箱执行 + 敏感度标签」做成生产级能力，与 HarmonyOS Skills Framework（统一 SKILL.md + 标准化运行时）、Android AppFunctions agent skill（SDK 注释优化 KDoc）形成跨平台「Agent Skill 范式」三足；本库 [[Agent Skills 技能范式 2026]]（09-20 实证 + manifest 签名护栏）与 [[隔离执行]]（沙箱）得到微软侧官方背书。
⚠️ 层级纪律：这是 **M365 / Declarative Agents 治理与扩展层**，非 Windows OS 执行总线（ODR / Agent Workspace）；勿写成「Windows OS 已内建 skill 沙箱」。来源为 MWPro 对 Message Center MC1476977 的转述（2026-09-22），精确 GA 日期与沙箱语法**待 learn.microsoft.com 逐字复核**。

## 2026-09-26 增补：Copilot 重架构——Autopilot 常驻托管智能体 + Managed Runtime 租户沙盒（来源 [[AppIntent 每日情报 2026-09-26-晚]]）

> 接续 08-18「Agent 365 = 治理/身份层控制平面」、09-21「Foundry 出网控制」、09-25「Declarative Agents Skills GA」。本期补 **微软 09-25 官方博文（Jared Spataro）重新设计 Copilot（Home/Code/Autopilot）** 在 Agent 365 治理层新增的**两层拼图**——把「常驻托管智能体」与「租户内沙盒执行总线」产品化。

- **Autopilot = 常驻托管智能体（persistent agent）**：由 Build 2026 内部代号 Scout 改名；给一个 agent 名字、角色、目标，它**云托管、用户离开仍续跑**（watch channels / follow up / 跑 recurring work / days later 续项目）；在租户内拥有**自身身份（identity）、记忆（memory）、工作区（workspace）**，权限/审计/治理在身后——与 08-18 记的 Entra Agent ID「三运行模式」中「Own access / autonomous（自主后台）」一致，但更显式地产品化为「带工位的数位同事」。
- **Copilot Managed Runtime = 租户内沙盒执行总线**：Code 用自然语言生成的 App/仪表盘/自动化**托管运行在 M365 租户内的隔离环境**，由 IT 治理；发布 npm 包 `@microsoft/managed-apps`（核心 SDK）/ `-cli`（scaffold/preview/deploy/version）/ `-vite-plugin`（Vite 8 构建集成），默认模板 React+TS+Vite 8，CLI 生成 typed TypeScript services 直连 Microsoft Graph 数据连接器。
- **计费二分 USL vs UBB**：USL（封顶订阅）含 Chat/Office/Auto 路由（OpenAI+Anthropic）；UBB（按量）含 Cowork/Code/Autopilot 与前沿模型（Astra/Fable）——把「agent 工作负载比聊天贵」显式化，Admin 可用 Graph API 设 tenant/group/user 级预算策略。
- → 对 OS PM 的含义：微软治理层把「**统一注册表（Agent 365）+ agent 身份（Entra Agent ID）+ 租户内沙盒执行总线（Managed Runtime）+ 常驻托管智能体（Autopilot）**」拼成完整句——这是本库「治理层控制平面 ↔ OS 执行层隔离」二分法的 SaaS 侧完整样板，与 [[Agent Workspace 隔离执行]]（Windows OS 容器/账号隔离）形成跨厂商对照；但**层级纪律不变**：这是 M365/Entra 治理与执行层，**非 Windows OS 执行总线（ODR/Agent Workspace）新 API**。
⚠️ 来源为 byteiota/codiot/gadgetbond/compsmag 对微软 09-25 官方博文的转述；Home/Code 经 Frontier 数周内铺开、Autopilot 9 月底私有预览，**均非 GA**；Managed Runtime 沙箱语法/SDK 版本与 GA 日期**待 learn.microsoft.com 逐字复核**；纳德拉「工作 OS」为定位表述，勿写成「Windows 已内建」。
