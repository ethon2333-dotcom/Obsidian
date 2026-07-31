---
tags: [PRD, OS-PM, 系统级, App-Intent]
created: 2026-07-31
---

# OS PM PRD 专项（系统级产品需求文档）

> 配套：[[PRD学习笔记]]、[[PRD写作SOP]]、[[PRD_Template]]。
> 适用：OS / 平台 / 系统级产品经理写"能力暴露与编排"类需求（如系统级 Agent、App Intent、设备端智能）。

## 一、OS PM 的 PRD 与 App PM 有何不同

| 维度 | App PM PRD | OS PM PRD |
| :--- | :--- | :--- |
| 对象 | 单个功能 / 页面 | 一类能力 / 接口面，跨应用生效 |
| 关注 | 交互与业务流程 | 能力定义、编排、权限、生态 |
| 约束 | 技术栈 / 网络 | OEM / 运营商 / 芯片 / 系统版本 / 隐私法规 |
| 用户 | 终端消费者 | 消费者 + 开发者 + 第三方应用 |
| 兼容 | 自身 App 版本 | 多版本系统、多厂商、向后兼容与弃用 |
| 风险 | 功能缺陷 | 生态分裂、隐私越界、系统稳定性 |

## 二、OS 级 PRD 必须补的章节
1. **能力暴露 / 接口面设计**：这个能力以什么形式对外（Intent / API / 系统服务）？参数与返回？
2. **意图 Schema / 协议**：字段、类型、必填、枚举；版本化。
3. **权限与审批流**：默认拒绝；敏感操作需 Confirmation UI 或硬件级审批（见 [[Agent 身份与硬件级审批]]）。
4. **系统编排与 Fallback**：多 App / 多能力如何编排？失败 / 超时如何降级？
5. **生态治理**：Registry / 文档 / 示例 / 审核；质量与一致性门槛。
6. **隐私与安全**：数据最小化、端侧处理优先（见 [[Function Calling 端侧工具调用]] / [[Local Agent Bench 端侧智能体基准]]）。
7. **向后兼容与弃用**：旧版本契约如何保留？弃用窗口与通知。
8. **灰度与 Feature Flag**：系统能力如何按机型 / 地区 / 版本渐进放量。

## 三、实战示例：系统级 Agent / App Intent 类 PRD
以你库中已沉淀的知识为锚点（[[APP INTENTS]]、[[OS产品经理知识库]]、[[手机AI智能体]]、知识飞轮相关笔记）：
- **需求背景**：系统编排者（System Orchestrator）替代 App 两两直连；端侧意图（AppFunctions / Intents Kit / AppIntents）。
- **能力定义**：Intent Schema + 参数 + 确认 UI + 限速；跨平台差异（Apple / Android / HarmonyOS / Windows，见 [[Apple AppIntents Schema Protocol 2026]] 等）。
- **权限与确认**：敏感能力默认 Confirmation UI；高危操作硬件级审批（YubiKey / Entrust 思路）。
- **端侧 vs 云侧**：优先端侧以保隐私与低延迟；复杂任务云侧兜底（链 [[Function Calling 端侧工具调用]]）。
- **开发者生态**：Registry 发布、文档、示例、评测基准（参考 Local Agent Bench）。
- **验收**：跨平台一致的行为、隐私合规、性能 SLA、Fallback 正确性。

## 四、OS PRD 常见陷阱
- 泄漏实现细节（PRD 写"用 XX 框架"，应写"能力契约"）。
- 忽略权限模型与安全默认（默认允许 = 雷）。
- 跨版本 / 跨厂商兼容未定义，导致生态分裂。
- 隐私默认错（应数据最小化、端侧优先）。
- 缺少 Fallback，单点失败拖垮系统编排。

## 五、OS PM PRD 精简检查清单
- [ ] 能力契约（接口面 / 参数 / 返回）已定义且版本化
- [ ] 权限默认拒绝 + 敏感操作有确认 / 审批
- [ ] 编排与 Fallback 明确（超时 / 失败 / 降级）
- [ ] 隐私数据最小化、端侧优先
- [ ] 向后兼容与弃用窗口已规划
- [ ] 开发者生态（Registry / 文档 / 示例）配套
- [ ] 跨平台差异已对齐或显式标注
- [ ] 灰度 / Feature Flag 策略已定

## 相关库内笔记
- [[Apple AppIntents Schema Protocol 2026]] / [[Android AppFunctions 设备侧意图 2026]] / [[HarmonyOS Intents Kit 与 ArkAF 2026]] / [[Windows Copilot Actions 与 Agent Workspace 2026]]
- [[Agent 身份与硬件级审批]] / [[Confirmation UI 安全机制]] / [[Function Calling 端侧工具调用]] / [[Local Agent Bench 端侧智能体基准]]
