---
type: concept
status: draft
derived_from: "[[AI Agent 半月情报简报 2026-07-31]]"
tags:
  - AIAgent
  - 身份
  - 授权
  - 硬件审批
  - 安全
---

# Agent 身份与硬件级审批

> 全新主题（2026-07 检索新增）。聚焦面向自主 Agent 的「**身份优先 + 硬件级动作审批**」安全范式。确认机制见 [[Confirmation UI 安全机制]]；注入风险见 [[XPIA 跨提示注入]]；隔离执行见 [[Agent Workspace 隔离执行]]。

## 一句话定义

当 Agent 能实际「做事」（改库、发消息、执行交易）时，安全从「软件确认弹窗」升级为「**以身份/密码学为底、把授权锚定到具体动作、可硬件确认**」——即 YubiKey 5.8 那样对人类审批的每个 Agent 动作做密码学签名。

## 为什么重要

- **身份 alone 不够**：传统登录态只能证明「谁在调」，不能约束「Agent 能做什么动作」；自主 Agent 需要 action-level 授权。
- **硬件锚定降低误授权**：把审批绑定到物理密钥/密码学签名，使高危动作（改数据库、转账）有不可抵赖的人工确认。
- **与既有机制互补**：[[Confirmation UI 安全机制]] 是软件层确认，本概念是「身份+硬件」的更强一层；二者都服务于 [[XPIA 跨提示注入]] 的缓解。

## 适用边界

- 适用于高权限/高危动作的 Agent（企业 IT、金融、运维），消费级 OS Agent 可用软件确认降配。
- 硬件密钥增加操作摩擦，需按风险分级（低危自动、高危硬件确认）。

## 证据与例子（2026-07 窗口）

- **YubiKey 5.8**（7-21）：CTAP 2.3 + WebAuthn，人类可对**具体 Agent 动作**（如数据库变更）做密码学审批，不止登录。
- **Entrust Agentic AI Trust Accelerator**（7-14）：以身份/授权/密码学控制为核心的 co-dev 计划，助企业把自主 Agent 从试点推到生产。
- **Qoder Security**（7-23）：安全前移到编码会话中（三层防护），误报降约 80%。
- **同期风险事件**：SharePoint CVE-2026-50522 公开利用（数小时盗 machine key）；PyPI `mrmustard` 投毒（import 即窃 SSH/云密钥）；Anthropic 发 Claude Security 插件（多 Agent 审自身代码）。
- **组织 readiness**：ManpowerGroup 称仅 **3%** 领导者准备好领导 AI 化团队（7-22）——落地瓶颈在人与治理，不在模型。

## 可复用启发

- Agent 安全分级：低危动作软件确认（[[Confirmation UI 安全机制]]）、高危动作硬件级/密码学审批（本概念）。
- 任何 Agent 上线前先验：身份归属、action-level 授权、审计轨迹、人类可中断——与 [[Agent Workspace 隔离执行]] 的隔离/ACL 同构。

## 关联

- 来源：[[AI Agent 半月情报简报 2026-07-31]]
- 确认机制：[[Confirmation UI 安全机制]]
- 注入风险：[[XPIA 跨提示注入]]
- 隔离：[[Agent Workspace 隔离执行]]
- 平台治理：[[企业级 Agent 平台与 Agent-as-Asset 2026]]

#标签/AIAgent #标签/身份 #标签/授权 #标签/安全
