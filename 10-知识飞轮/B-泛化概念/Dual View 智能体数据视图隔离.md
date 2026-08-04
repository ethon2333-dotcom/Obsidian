---
type: concept
status: draft
derived_from: "[[AppIntent 每日情报 2026-08-03]]"
tags: [AppIntent, 安全, 隔离执行, 数据视图, StoredIPI, 概念]
---

# Dual View 智能体数据视图隔离

## 一句话定义

**DualView（双视图隔离）** 是一种 Agent 安全架构原语：同一份数据对 Agent 始终以「符号化/脱敏」形态呈现（AgentView），对用户与普通程序则以「正常原文」形态呈现（HumanView）。**隔离的单位不是进程或账号，而是数据在被不同主体看见时的「可见形态」**。

## 为什么重要

- **它补上了进程/账号隔离的盲区**：[[Agent Workspace 隔离执行]] 隔离的是「执行主体」（低权限账号 + ACL + 独立会话），但一旦 Agent **拥有合法权限读写的文件，其内容本身不可信**，账号隔离就无能为力。DualView 隔离的是数据形态，正好覆盖这一场景。
- **它把「隔离机制的生命周期」问题摆上台面**：传统 Dual LLM 把不可信数据换成符号，Agent 只能引用不能读取——对**即时型**注入有效，但数据**落盘还原**后、被后续任务重读时，符号关系消失，高权限 LLM 直接看到原文。攻击不是绕过了隔离机制，而是绕过了隔离机制的**有效期**。
- **工程可行性高**：作为 OpenClaw 插件、仅用 tool hooks、不改 Agent 的 tool-call 逻辑、不改工具实现即可落地，可用性接近无防护基线。

## 适用边界

- 适用：任何需要 Agent 读写**持久化、会被复用**的产物（文件、记忆、跨会话上下文）的场景。
- 强相关：Stored IPI（存储型间接提示注入）、[[Agent Data Injection 数据注入攻击]]（ADI 伪造元数据让 Agent 自推错误结论）、[[XPIA 跨提示注入]]。
- 不替代：进程/账号隔离（[[Agent Workspace 隔离执行]]）与确认机制（[[Confirmation UI 安全机制]]），三者正交、互补。

## 证据与例子

**A. Stored IPI（存储型间接提示注入）的量化**

- 传统 Dual LLM 对即时型 IPI 的 ASR 可降到**接近 0**，但面对 **Stored IPI 仍达 53.3%**（实测 Claude Haiku 4.5）。
- 失效路径：Agent 把摘要写入文件 → 系统为让人能正常打开，落盘前**还原真实文本** → 真实文本进入普通文件系统、**符号关系消失** → 后续任务重读该文件，高权限 LLM 直接看到原文。

**B. DualView 方案：同一份数据，两套视图**

- **AgentView**：可信内容保原文，不可信内容**恒为符号**——Agent 写文件写的是符号，重读还是同一个符号，**Stored IPI 从根上断掉**。
- **HumanView**：用户和普通程序（编辑器、文件管理器）看到**正常原文**，环境照常工作。
- **视图路由**：工具不需要看原文（如本地文件读写）→ 在 AgentView 执行；工具必须处理原文（如网络请求）→ 路由到 HumanView，调用前**去符号化**、返回后把新产生的不可信内容**重新符号化**。

**C. 实现细节**

- Agent File System 用 **Git Worktrees** 管理，双文件环境（Agent 操作符号化文件，人类访问真实文件）。
- 作为 **OpenClaw 插件**部署，**仅用 tool hooks**，不改 Agent 的 tool-call 逻辑，也不改工具实现。
- **两层策略**：
  - **数据可信策略**（检查工具输出）：schema 规则 / origin 规则（如 `api.github.com/*` 可信、`imports/*.csv` 不可信、`agent:public-chat` 不可信）；
  - **数据使用策略**（检查发往 HumanShell 的命令）：`exec(git status)` 免审批，`exec($web1.text)` **必须人工审批**，并有命令重写规则防 `python -c` 绕过。

**D. 结果（论文口径，未复现）**

- 在 IPI benchmark 与 **PinchBench**（147 任务，114 读文件、121 写文件）上，DualView **阻断了包括 Stored IPI 在内的全部 IPI 攻击**，可用性接近无防护基线。
- 作者强调：因为是**设计层隔离**，防护**不局限于已知攻击模板**。

## 可复用启发

- **OS 该不该把「Agent 视图文件系统」做成一等公民？** 四平台目前均无此设计，DualView 证明插件级可行且可用性近基线——这是本库可以**主动提出**的产品建议，而非被动跟踪的新闻。
- **隔离粒度分层**：进程/账号隔离（[[Agent Workspace 隔离执行]]）→ 数据形态隔离（DualView）→ 确认/授权（[[Confirmation UI 安全机制]]），三者是不同维度的防护，不能互相替代。
- **符号化是「可信/不可信数据分离」的可落地工程形态**：比「加过滤器」更接近参数化查询之于 SQL 注入（呼应 [[Agent Data Injection 数据注入攻击]] 的论断）。

## 关联

- 来源：[[AppIntent 每日情报 2026-08-03]]
- 同源姊妹研究：[[Agent Data Injection 数据注入攻击]]
- 隔离：[[Agent Workspace 隔离执行]] ｜ 注入：[[XPIA 跨提示注入]] ｜ 确认：[[Confirmation UI 安全机制]]
- 写回防护：[[Agent 写回路径 XPIA 风险评估 SOP]] ｜ 读入防护：[[Agent 读入路径可信数据边界 SOP]]
- 平台：[[Windows Copilot Actions 与 Agent Workspace 2026]]

#标签/安全 #标签/隔离执行 #标签/DualView #标签/StoredIPI
