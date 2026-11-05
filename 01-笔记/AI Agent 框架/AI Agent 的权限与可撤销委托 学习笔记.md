---
title: AI Agent 的权限与可撤销委托 学习笔记
tags: [AI Agent框架, 权限, 授权, 安全]
created: 2026-10-11
source: "WebSearch 核实：AAuth / AAP / OAuth for Agents / MCP scoped auth / A2A / Entra Agent ID / Claude Agent SDK，2025-2026"
---

> 心智模型：把 agent 当成一个"带着临时工牌的实习生"——工牌只开特定门、到点自动失效、随时可被前台注销，且每一步进出都有登记。

## 广度覆盖

本篇聚焦 **agent 能做什么（scope / capability）以及这份授权如何被收放（delegation / revocation）**，刻意区别于 [[智能体身份与信任 学习笔记]]（讲"你是谁 / 怎么证明身份"而非"你能干啥"）、[[工具调用安全 学习笔记]]（讲工具执行层面的鉴权拦截）、[[多智能体协作与编排 学习笔记]]（讲协作拓扑而非授权模型）。审批 UI 长什么样归 [[Confirmation UI 分级与产品责任边界 学习笔记]]（本库暂未建，先留白），本篇只谈授权"机制"不谈"长相"。

### 1. 核心定义

| 术语 | 含义 |
|---|---|
| Scoped permission | 把权限切成 `资源:动作` 细粒度单元（如 `jira:issues:read`），而非整桶给 |
| Capability token | 把"能做什么 + 约束"打包进令牌（AAP 称 capability = action + constraints） |
| Delegated authority | agent 代表用户/上游 agent 行事，"on-behalf-of" 委托 |
| Revocable delegation | 授权可随时吊销（任务结束即销 refresh token、禁用 blueprint 一键关停） |
| Least-privilege | 只给完成当前任务的最小权限，默认 deny-all |
| Session-scoped | 权限绑定到一次会话/任务，过期或退出即失效 |

### 2. 权限模型分类

| 模型 | 思路 | 代表 |
|---|---|---|
| OAuth scopes（角色/动作级） | 标准 OAuth 2.1 scope 字符串 + PKCE | MCP、A2A、AAuth |
| Capability / 结构化声明 | JWT 内嵌 agent/task/capability 声明，可推理 | AAP（draft-aap-oauth-profile） |
| 委托链 / Token Exchange | 用 base token 换更窄、限受众、短命的 ephemeral token | RFC 8693 |
| 即时授权 RAR | 单次动作"恰好读这个文件一次"，而非常驻广授权 | RFC 9396 |
| 身份即权限（IdP 原生） | agent 作为一等身份进入目录，配条件访问/访问包 | Entra Agent ID |
| 本地权限策略 | SDK 内 permission mode + hooks + 声明式规则 | Claude Agent SDK |

### 3. 主流方案（机制层）

| 方案 | 要点 |
|---|---|
| OAuth 2.1 + PKCE | 远程 agent/MCP 强制基线；PKCE 防授权码注入，禁 implicit grant，精确 redirect URI 匹配 |
| Client Credentials | 服务自有 agent：单次 POST 拿短命 JWT（1–4h），无 refresh，到期重认证 |
| Authorization Code + PKCE | 用户委托场景（读日历/发邮件），用户走 consent，agent 拿绑定该用户的委托令牌 |
| Token Exchange (RFC 8693) | 多工具链路里换"窄、限受众、分钟级"的临时令牌，保持最小权限随信任边界传播 |
| RAR (RFC 9396) | just-in-time 单次特定授权，替代常驻广授权 |
| PoP（DPoP / mTLS） | 令牌绑定密钥，防令牌被拿走复用 |
| 401 + Protected Resource Metadata (RFC 9728) | MCP 未认证时返回 401 指向授权服务器，agent 自动发现并走 OAuth |

### 4. 2025-2026 进展（规范/草案）

| 时间 | 进展 | 状态 |
|---|---|---|
| 2025 | Google 发布 A2A 协议（4月），6月移交 Linux 基金会；内置 OAuth 2.0 / mTLS / 能力级 ACL / 审计 | 开放标准 |
| 2025-05-19 | Microsoft Entra Agent ID 公开预览，agent 作为一等身份入目录 | Public Preview |
| 2025-06 / 11 | MCP 授权规范（OAuth 2.1）落定 2025-06-18，后续 2025-11-05 修订 | 规范 |
| 2025 | IETF AAuth（draft-patwhite-aauth）：Agent Authorization Grant，仿 Device Grant，HITL 同意 | 草案（原 2025-11-14 过期） |
| 2026-02 | IETF AAP（draft-aap-oauth-profile-00）：OAuth 2.0 + JWT 的 agent 授权档案，aap_agent/task/capabilities 声明 | 草案 |
| 2026 | IETF Scope Aggregation（draft-jia-oauth-scope-aggregation-00）：多步工作流聚合 scope，单次授权减少疲劳 | 草案（2026-08-14 过期） |

### 5. 代表产品 / 平台

| 产品 | 权限与委托机制 |
|---|---|
| **MCP（Anthropic）** | 远程 server 用 OAuth 2.1；推荐 **per-tool scope**；STDIO 不跑 OAuth（用环境变量凭据）；DCR 自动注册 |
| **A2A（Google）** | Agent Card（`/.well-known/agent.json`）声明认证方式；身份在 HTTP 传输层；能力级 ACL + 审计日志 |
| **Entra Agent ID（Microsoft）** | 最小权限 JIT 作用域令牌；Conditional Access；Access Packages（限时、可审计）；sponsor/owner/manager 治理模型；不能赋特权管理员角色；blueprint 模板一键关停一类 agent |
| **Claude Agent SDK（Anthropic, 2025-09-29）** | 6 种 permission mode（default/acceptEdits/bypassPermissions/plan/delegate/dontAsk）+ canUseTool 回调 + PreToolUse/PostToolUse Hooks + settings.json 声明式 allow/deny 规则 |
| **OpenAI agent 权限** | 待核实（未找到 2025-2026 公开"agent permissions"独立机制表述，疑似以 API key / 平台级管控为主） |

### 6. 可撤销委托的关键抓手

- **过期即失效**：高风险的 ephemeral token 1–5 分钟，只读 1 小时，长命 client token 小时到天级。
- **任务完成即吊销**：任务结束撤销 refresh token，agent 不在无关任务间保留委托令牌。
- **Refresh 轮换 + 绝对过期**：每次刷新发新 refresh 并立即使旧失效；设硬上限寿命，绑定原 client_id。
- **委托链可审计**：AAP 的 delegation 声明 + 各层审计日志，能回溯"谁 delegated 给谁、为哪个 task、哪些 capability"。

## 心智锚点（与相邻主题的关系）

- 身份 vs 权限：[[智能体身份与信任 学习笔记]] 解决"agent 是谁、怎么被认证"，本篇解决"它被允许做什么、能收回吗"。
- 工具执行拦截：[[工具调用安全 学习笔记]] 在工具调用边界做鉴权，本篇在令牌/委托层做裁剪。
- 协作拓扑：[[多智能体协作与编排 学习笔记]] 讲 A→B 如何分工，本篇讲 A 把权限 delegate 给 B 时怎么不越权。
- 协议底座：[[Agent 协议生态 学习笔记]] 列 MCP/A2A/AGP 等协议，本篇是其中"授权"这一面的切片。

# 深度盲区（待 Ethon 补充）

- [ ] AAuth 草案过期（2025-11-14）后是否已被 AAP 或 OAuth WG 吸收？当前最新状态？
- [ ] Entra Agent ID 的"scope/permission"具体表达是不是就是标准 OAuth scope，还是私有扩展？
- [ ] A2A 在协议层没定义授权怎么做（Red Hat 指出"authorization creep"风险），业界最佳实践是什么？
- [ ] Token Exchange 在跨组织 A2A 场景下，下游如何信任上游换发的窄令牌？（受众/签名链）
- [ ] Anthropic 的 Hooks vs OAuth scope，两者在权限模型上是互补还是重叠？生产怎么组合？
- [ ] 移动端 / 端侧 agent（Android OS PM 视角）如何做 session-scoped 权限？与 AppOps / runtime permission 怎么映射？
- [ ] 审计"委托授予"的最小合规字段集是哪些？（GDPR / 等保视角）

## 附：来源清单

- IETF AAuth draft：http://auth.ietf.org/doc/html/draft-patwhite-aauth （访问 2026-10-11）
- IETF AAP draft：https://www.ietf.org/archive/id/draft-aap-oauth-profile-00.html （访问 2026-10-11）
- IETF Scope Aggregation draft：https://datatracker.ietf.org/doc/html/draft-jia-oauth-scope-aggregation-00 （访问 2026-10-11）
- MCP Authorization 规范：https://modelcontextprotocol.io/specification/2025-06-18/basic/authorization （访问 2026-10-11）
- OAuth for Agents 实践：https://agentsurface.dev/docs/authentication/oauth-for-agents （访问 2026-10-11）
- OAuth for AI Agents 指南：https://securew2.com/blog/oauth-for-ai-agents （访问 2026-10-11）
- A2A 协议（百度百科综述）：https://baike.baidu.com/item/Agent2Agent%E5%8D%8F%E8%AE%AE/67474290 （访问 2026-10-11）
- Red Hat 增强 A2A 安全：https://developers.redhat.com/articles/2025/08/19/how-enhance-agent2agent-security （访问 2026-10-11）
- Microsoft Entra Agent ID 公告：https://techcommunity.microsoft.com/blog/microsoft-entra-blog/announcing-microsoft-entra-agent-id-secure-and-manage-your-ai-agents/3827392 （访问 2026-10-11）
- Entra Agent ID 用户账户权限模型：https://learn.microsoft.com/ka-ge/entra/agent-id/agent-users （访问 2026-10-11）
- Claude Agent SDK 权限：https://docs.claude.com/en/docs/agent-sdk/permissions （经第三方博文转述，访问 2026-10-11）

## ⚠️ 待核实清单

- ⚠️ "OpenAI agent 权限"独立机制：未找到 2025-2026 公开权威表述，标记为待核实，疑似以 API key / 平台级管控为主。
- ⚠️ AAuth 草案是否已过期失效或被合并：原始 draft 标注 2025-11-14 过期，最新状态未核实。
- ⚠️ MCP 2025-11-05 修订版的具体差异：来源为二手博客转述，未直接核对官方 2025-11-05 规范文本。
- ⚠️ Claude Agent SDK 6 种 permission mode 名称（default/acceptEdits/bypassPermissions/plan/delegate/dontAsk）：来自社区 Go SDK 示例转述，官方命名以 docs.claude.com 为准，待核实。

#标签/AI Agent框架/权限/授权
