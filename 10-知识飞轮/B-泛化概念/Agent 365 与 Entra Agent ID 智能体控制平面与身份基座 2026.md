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
