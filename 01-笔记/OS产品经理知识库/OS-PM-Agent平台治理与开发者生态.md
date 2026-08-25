---
title: OS PM Agent 平台治理与开发者生态
type: platform-spec
status: draft
tags: [OS产品经理, Agent平台, Registry, SDK, 开发者生态, 治理]
created: 2026-08-06
updated: 2026-08-06
related: [OS-PM-学习方向与能力地图, 意图框架·跨体系索引 MOC, PM决策层 MOC]
---

# OS PM Agent 平台治理与开发者生态

> 从“会设计一个 App Intent”升级到“会定义一个可发现、可执行、可观测、可治理、可商业化的 OS 能力平台”。

## 一、平台闭环

```text
能力声明
→ Registry 注册
→ 审核 / 版本 / 灰度
→ 发现 / 排序 / 路由
→ 权限 / 确认 / 执行
→ Trace / 反馈 / 质量评测
→ 开发者修复与商业激励
→ 生命周期治理
```

## 二、OS Agent Platform Spec v0.1

统一契约至少包含：

- Intent：动作名称、语义描述、触发条件；
- Entity / Enum：实体类型、候选值、别名和本地化；
- Input / Output：类型、必填槽位、可空性、分页和大小限制；
- Error：权限拒绝、能力不可用、参数错误、超时、部分完成；
- Permission：调用方、数据范围、用户授权和运行时撤销；
- Risk：低、中、高风险以及是否可逆；
- Source：能力来源、数据来源、可信级别和 provenance；
- Version：Schema 版本、兼容范围、废弃时间和迁移策略。

## 三、Registry 治理

Registry 不能只是一张静态能力清单，应支持注册、审核、灰度、动态启停和撤销，并记录账号、地区、设备、版本、来源、权限、风险和使用统计。

必须解决：

- 同义能力消歧、排序和冲突处理；
- 误召回、参数缺失、权限拒绝、超时和回滚测试；
- 能力被禁用后的可解释降级；
- App 长期注册但始终 `isEnabled = false` 的形式适配识别；
- 质量、用户选择、开发者付费和生态政策之间的排序冲突。

## 四、Developer Conformance Kit

平台要让第三方 App 低成本接入，至少提供：

1. SDK 和最小 Demo；
2. Schema / KDoc 静态检查；
3. Registry 预览器；
4. ADB / CLI 调试命令；
5. Schema、权限、风险和错误返回模板；
6. 空 Registry、误召回、参数缺失、拒权、超时、撤销测试；
7. 端到端 Trace 和可复现 Replay；
8. 参考 App 和失败案例库；
9. 版本升级、废弃和回滚指南。

### 接入成功标准

- 第三方 App 能在一周内完成首个能力接入；
- 开发者能在本地重现路由和执行失败；
- 平台能解释某个能力为什么被召回或拒绝；
- 破坏性变更有编译期或测试期阻断；
- 线上问题能回放到 Schema、模型、策略或应用实现。

## 五、Runtime / Orchestration 契约

系统级任务不仅是单个 Function Call，还可能是多意图 DAG。平台需要定义并发和串行依赖、超时、取消、重试、幂等键、部分完成、补偿动作、云端升级、端侧降级和每一步的确认策略。

同时明确：

- L1 原生 API、L2 DeepLink / Schema、L3 GUI 兜底的边界；
- 跨设备 handoff、离线队列和恢复；
- 任务取消、回滚和人工接管；
- 每个步骤的权限和数据范围。

## 六、Metrics & Governance Pack

### 任务质量

- 任务完成率、首次成功率、澄清率；
- 误召回率、误执行率、取消率、返工率；
- P50 / P95 延迟、端侧承接率、云端逃逸率、GUI 兜底率；
- 部分完成率、恢复成功率和人工接管率。

### 平台质量

- Registry 新鲜度、能力可见率、禁用率；
- Schema 合规率、版本兼容率、回滚时间；
- Trace 完整率、错误可归因率、策略命中率。

### 开发者生态

- 首次接入时长；
- Schema 通过率；
- 调试失败到修复的时间；
- 能力调用率、禁用率和复用率；
- 开发者留存、接入成本和平台支持工单。

### 安全治理

- Agent 身份覆盖率；
- 授权和撤销成功率；
- 确认绕过率；
- XPIA / ADI 攻击成功率；
- 敏感数据来源分级覆盖率；
- 高风险动作审计闭环率。

## 七、跨设备任务包

跨设备不是简单地把字符串从手机发到车机。建议定义可重放的 Task Envelope：

```text
task_id
principal
intent_ir
required_capabilities
data_scope
current_state
completed_steps
pending_confirmation
expiry
idempotency_key
handoff_policy
rollback_plan
```

必须回答：哪台设备负责理解、执行、确认和结果回显；设备离线时是否排队；多个设备同时响应如何冲突；用户在哪台设备上撤销；身份和权限是否继承。

## 八、用户研究与 UX 资产

Figma 组件应覆盖：

```text
待确认 / 执行中 / 等待用户 / 需要接管
成功 / 失败 / 部分完成 / 可撤销
```

建议用 12 个核心任务做访谈和可用性测试，至少覆盖：用户愿意委托什么、什么时候希望系统主动、是否理解 Agent 身份、是否看懂数据上云和跨 App 调用、失败后是否知道下一步、确认次数和放弃率是否可接受。

## 九、平台商业与治理

需要补齐的不是商业新闻，而是可讨论的机制：OS 入口带来的流量归属、App 开放能力的收益和成本、排序是否影响商业分发、平台费和能力分成、超级 App 的谈判筹码、数据责任，以及公共 Schema 与厂商扩展的边界。

## 十、建议交付顺序

1. `Intent Contract v0.1`：字段、权限、风险、来源和版本。
2. `Registry Spec v0.1`：注册、发现、排序、动态启停和撤销。
3. `Developer Conformance Kit`：SDK、Lint、模拟器、测试夹具和 Replay。
4. `Metrics Dictionary`：事件定义、指标公式、质量红线和埋点表。
5. `Agent UX Kit`：任务卡、计划预览、确认、执行中、接管、失败和撤销。
6. `Task Envelope v0.1`：跨设备任务状态、身份、确认、离线和回滚。

## 十一、权威资料

- [Android AppFunctions 概览](https://developer.android.com/ai/appfunctions)
- [向应用添加 AppFunctions](https://developer.android.com/ai/appfunctions/add-appfunctions)
- [AppFunctionManager API](https://developer.android.com/reference/androidx/appfunctions/AppFunctionManager)
- [Apple App Intents](https://developer.apple.com/documentation/appintents)
- [MCP Specification](https://modelcontextprotocol.io/specification/latest)
- [MCP Registry](https://modelcontextprotocol.io/registry/about)
- [A2A Protocol](https://a2a-protocol.org/latest/)
- [Google People + AI Guidebook](https://pair.withgoogle.com/guidebook/)
- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework)

