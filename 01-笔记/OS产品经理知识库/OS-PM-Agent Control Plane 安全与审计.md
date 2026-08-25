---
title: OS PM Agent Control Plane 安全与审计
type: architecture
status: draft
tags: [OS产品经理, Agent安全, ControlPlane, 权限, 审计, Provenance]
created: 2026-08-06
updated: 2026-08-06
related: [OS-PM-学习方向与能力地图, 安全 MOC, Agent 执行安全（PM视角）]
---

# OS PM Agent Control Plane 安全与审计

> 目标：把 XPIA、ADI、确认、来源分级和执行安全，从原则与 SOP 推进为可测试的系统控制面。

## 一、目标架构

```text
用户目标
→ Typed Intent IR
→ Capability / Policy Broker
→ Confirmation Token
→ 沙箱执行
→ OpenTelemetry Trace / W3C PROV 审计链
```

模型和工具不能直接拥有 OS 副作用权限。所有发送、支付、删除、账户变更、网络请求和跨 App 写入都必须经过 Broker。

## 二、Capability Token

一个短时、可撤销的能力令牌至少包含：

```text
actor
verb
target
data_class
scope
expiry
reversibility
principal
policy_version
nonce
```

默认拒绝以下情况：无令牌、令牌过期、跨 App 或账户使用、目标变化、数据等级超出授权、策略版本不匹配、重复提交。

## 三、Confirmation Token

确认不能只是一个不可追踪的“确认事件”，应绑定规范化动作：

```text
confirmation = H(
  canonical_action,
  target_package,
  target_account,
  data_scope,
  policy_version,
  nonce,
  expiry
)
```

确认页至少展示：具体动作和目标 App、目标账户或设备、将读取或发送的数据、不可逆后果、费用和外部通信、是否会上云或跨设备执行。

必须测试：确认后参数被修改、目标 App 或账户变化、过期或重复使用、Overlay 和 Accessibility 诱导、执行中权限撤销。

## 四、Typed Intent IR

将自然语言和模型输出转换成确定性中间表示，避免每一步重新解释原始文本：

```text
principal
verb
target
arguments
data_scope
risk_level
reversibility
required_permissions
source_refs
```

解析器应做 URI 规范化、显式包名绑定、调用者身份验证、敏感操作拒绝隐式 Intent 和防止重解析劫持。

## 五、审计 Trace

每个任务建立一条完整事件链：

```text
user_goal
  → intent_candidate
  → policy_decision
  → tool_call
  → confirmation_request
  → confirmation_result
  → os_execution
  → side_effect_result
```

建议字段：

```text
trace_id, task_id, principal, model_version, policy_version,
intent_hash, tool_id, target_package, args_hash, data_class,
permission_state, confirmation_id, provenance_refs, result,
error, timestamp
```

分工：OpenTelemetry 负责运行时 Trace、Span、日志和指标；W3C PROV 表达实体、活动、责任主体和来源关系；C2PA 负责文档、图片等内容来源，不能替代 Agent action audit；SLSA / in-toto 负责模型、Agent、Tool 和插件供应链来源。

审计日志默认不保存敏感原文，而保存哈希、类型和受控引用。生产日志、训练日志和调试日志必须隔离。

## 六、安全回归场景

| 场景 | 攻击方式 | 预期结果 |
|---|---|---|
| 恶意文档 | 将指令伪装成检索资料 | 不得升级为用户意图 |
| 恶意工具返回值 | 修改后续动作 | Broker 重新检查策略 |
| Schema 污染 | 相似名称注册更高权限工具 | 明确来源和权限差异 |
| 确认篡改 | 确认后修改参数 | Confirmation hash 失效 |
| 旧确认复用 | 重放过期或其他任务令牌 | 拒绝执行 |
| 隐式 Intent 劫持 | 第三方 App 截获调用 | 使用显式目标或阻断 |
| 权限撤销 | 执行中关闭权限 | 停止、回滚或人工接管 |
| 敏感数据外泄 | 通过日志、剪贴板、通知或工具传出 | 脱敏并记录阻断原因 |

## 七、核心指标与发布门禁

- XPIA-ASR：攻击导致有害动作的比例；
- Exfiltration Success Rate：敏感数据成功外泄比例；
- Unauthorized Action Block Rate：越权动作拦截率；
- Policy False Deny Rate：正常任务被错误拒绝比例；
- Capability Overreach Rate：实际权限超出声明范围比例；
- Confirmation Bypass Rate：无有效确认却完成副作用比例，目标为 0；
- Stale Approval Acceptance Rate：旧确认被接受比例，目标为 0；
- Trace Completeness：完整闭环 Trace 比例；
- Provenance Coverage：有来源和责任主体的输入 / 输出比例；
- Sensitive Log Leakage Rate：日志明文敏感数据比例；
- Duplicate Side-effect Rate：重试造成重复副作用比例；
- Recovery Success Rate：失败后回滚或进入可控恢复比例。

P0 发布门禁：100% 外部副作用经过 Broker；高影响动作不存在确认绕过；旧确认接受率为 0；所有副作用有完整 Trace；生产日志不含明文密钥和高敏数据。

## 八、官方资料

- [Android Security Checklist](https://developer.android.com/privacy-and-security/security-tips)
- [Intent Redirection](https://developer.android.com/privacy-and-security/risks/intent-redirection)
- [Implicit Intent Hijacking](https://developer.android.com/privacy-and-security/risks/implicit-intent-hijacking)
- [Tapjacking](https://developer.android.com/privacy-and-security/risks/tapjacking)
- [Android Application Sandbox](https://source.android.com/docs/security/app-sandbox)
- [OWASP Agentic AI Threats and Mitigations](https://genai.owasp.org/resource/agentic-ai-threats-and-mitigations/)
- [OWASP LLM Top 10](https://genai.owasp.org/llm-top-10/)
- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework)
- [W3C PROV Overview](https://www.w3.org/TR/prov-overview/)
- [OpenTelemetry Specification](https://opentelemetry.io/docs/specs/otel/)
- [AgentDojo](https://arxiv.org/abs/2406.13352)
- [InjecAgent](https://arxiv.org/abs/2403.02691)
- [ToolSandbox](https://arxiv.org/abs/2408.04682)

