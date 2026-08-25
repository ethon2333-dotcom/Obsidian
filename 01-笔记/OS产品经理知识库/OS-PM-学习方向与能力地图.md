---
title: OS PM 学习方向与能力地图
type: roadmap
status: active
tags: [OS产品经理, 端侧AI, Agent, Android, 学习路线, 能力模型]
aliases: [OS PM 学习路线, AI-Native OS PM 能力地图]
created: 2026-08-06
updated: 2026-08-06
source: Vault 结构分析 + 官方资料核实
related: [OS产品经理知识库 MOC, 端侧意图框架 学习笔记, PM决策层 MOC]
---

# OS PM 学习方向与能力地图

> 这份笔记回答一个问题：作为面向 Android / AI-Native OS / 端侧 Agent 的产品经理，我还需要补什么能力，才能把技术趋势转化为系统架构、平台规则、产品指标和可交付方案。

## 一、先给结论

当前知识库已经覆盖了：

- App Intent、AppFunctions、端侧 Agent 和四平台对比
- AI Runtime、KV Cache、PagedAttention、量化、功耗与内存预算
- Agent 安全、XPIA / ADI、Confirmation UI、隔离和来源分级
- PM Checklist、PRD、竞品观察、Figma 状态机原型
- LangChain、LangGraph、RAG、Loop Engineering 和 Graph Engineering

当前最明显的缺口不是“还缺少哪些概念”，而是以下四个环节还没有完全闭环：

```text
系统底层理解 → 能力/API 设计 → 可运行原型 → 真实任务评测
```

因此下一阶段的学习原则是：

> 每学习一个主题，都要留下一个系统判断、一个可运行实验或一份可以评审的产品交付物。

## 二、OS PM 能力矩阵

| 方向 | 当前基础 | 主要缺口 | 下一步产出 | 优先级 |
|---|---|---|---|---|
| Android / AOSP | 有 OS 架构和 App Intent 概念 | Framework、system_server、Binder、权限、生命周期缺少实践 | AppFunctions 端到端 Demo + 系统架构图 | P0 |
| Agent 评测 | 已有 Intent Router SOP 和 PM Checklist | 没有自己的任务集、评测脚本和故障分类 | 30-50 条任务集 + 指标看板 | P0 |
| 端侧 AI Runtime | 已理解内存、KV Cache、量化等原理 | 缺真实设备上的延迟、内存、功耗实验 | FP16 / INT8 / INT4 对照实验 | P0 |
| 平台 API 与生态 | 已有 App Intent、Registry、竞品分析 | 缺 SDK 生命周期、兼容性、开发者接入和治理设计 | Intent Platform API / SDK 方案 | P1 |
| 安全与隐私 | 概念覆盖较好 | 缺 threat model、红队测试、授权和审计闭环 | Agent 安全测试集 + 权限模型 | P1 |
| Agent UX | 已有 Confirmation UI 和 Figma 状态机思路 | 缺真实用户测试和失败恢复设计 | 可测试原型 + 用户研究结论 | P1 |
| 跨设备与生态 | 已有跨端发散和 A2A 资料 | 缺任务交接、设备发现和责任边界方案 | 手机-车机-IoT 任务流设计 | P2 |
| 编程与工具 | 有 Go / Rust 概览和代码库 | Android / Kotlin 实战缺位 | 选择 Kotlin 为主，Go/Rust按需补 | P1 |

## 三、P0：Android / AOSP 与系统能力边界

### 为什么必须学

OS PM 的关键判断不是“这个功能能不能做”，而是“它应该放在哪一层”：应用、Jetpack、Android Framework、`system_server`、HAL、Runtime 还是芯片平台。

AOSP 官方架构把 Android 分成应用、Framework、系统服务、ART、HAL、原生库和内核等层。你的现有笔记已经能讨论 App Intent 和 AI Runtime，但还需要把这些概念放回真实系统边界中。

### 学习模块

- AOSP 软件栈：Framework、`system_server`、系统服务、ART、HAL、Binder、Linux Kernel
- Android 组件：Activity、Service、BroadcastReceiver、ContentProvider
- IPC：Binder、AIDL、跨进程调用和系统服务通信
- 权限：普通权限、运行时权限、签名权限、特权权限、沙箱
- 任务生命周期：前台 / 后台、WorkManager、后台限制、进程回收
- Android 输入与操作：Intent、Accessibility、UI 自动化和 GUI Agent 的边界
- AppFunctions：函数声明、KDoc Schema、Registry、调用权限、动态可见性和 ADB 调试
- Binder / AIDL / System Service：跨进程调用、线程池、调用身份、超时、进程死亡和版本化
- 安全边界：UID 沙盒、SELinux、导出组件、URI 临时授权和隐式 Intent 劫持
- 后台生命周期：WorkManager、JobScheduler、前台服务、进程被杀、重试、取消和断点恢复
- Context 数据平面：ContentProvider、SAF、AppSearch、Room / DataStore、数据授权和撤销
- 交付体系：API level、CDD、CTS / VTS / GTS、Mainline、APEX、GKI 和 OTA

> AppFunctions 官方页面当前仍标记为实验性预览，API 可能变化。学习它的重点不是把预览 API 当作稳定产品承诺，而是理解“应用能力如何进入 OS Registry、如何授权、如何被调用和测试”。

### 必做实践

做一个“系统级 Agent 最小闭环”项目：

```text
用户请求
→ Intent Router
→ AppFunction Registry
→ 只读 / 写入 / 高风险动作分类
→ Confirmation UI
→ AppFunction 执行
→ 结果回填
→ 审计日志
```

建议至少注册三个函数：

1. 只读函数：查询一个应用内的信息。
2. 可逆写入函数：创建一个待办或草稿。
3. 高风险函数：删除、支付或发送动作的模拟接口，必须二次确认。

### 验收标准

- 能画出请求从 App 到系统服务再到应用的调用边界。
- 能解释一个能力为什么应该是公开 API、系统 API 或 App 内逻辑。
- 能通过 ADB 查看能力注册、调用日志和失败原因。
- 能写出权限、生命周期、撤销和版本兼容规则。
- 能判断能力应该走 Binder、ContentProvider、系统服务还是普通 App API。
- 能把 App 被杀、权限撤销、版本不兼容和系统升级纳入产品状态机。
- 能用 CTS / VTS / 真实设备测试思维定义发布阻断条件。

### 关联笔记

- [[OS-PM-系统架构与底层技术]]
- [[端侧意图框架 学习笔记]]
- [[Android AppFunctions 设备侧意图 2026]]
- [[端侧意图路由选型 PM Checklist]]
- [[GUI Agent vs 原生 API 产品决策树]]
- [[OS-PM-Agent平台治理与开发者生态]]

## 四、P0：Agent 评测、可靠性与可观测性

### 为什么必须学

当前很多 Agent 资料停留在“能力很强”或“benchmark 很高”。对 OS PM 真正有用的问题是：在真实设备、真实应用、真实权限和真实多轮任务中，系统是否可靠。

### 学习模块

- 任务集设计：单轮、多轮、跨 App、槽位缺失、歧义、拒绝和恢复
- 错误分类：路由错误、Schema 错误、参数错误、权限错误、执行错误、结果理解错误
- 评测维度：成功率、完成时间、调用次数、误执行率、拒答率、人工接管率
- 端侧指标：首 Token 延迟、端到端延迟、内存峰值、功耗、温度、网络依赖
- 线上可观测性：Trace、事件日志、工具调用链、状态回放、版本对比
- 可靠性：超时、重试、幂等、熔断、降级、撤销、人工接管

### 必做实践

建立一个自己的 OS Agent 评测集：

| 类别 | 示例 | 必测指标 |
|---|---|---|
| 只读查询 | 查找邮件、日程、文件 | 路由准确率、引用准确率 |
| 单 App 写入 | 新建待办、创建日程 | 参数正确率、完成率 |
| 跨 App 任务 | 从邮件提取信息并加入清单 | 多步完成率、错误恢复率 |
| 歧义请求 | “把它发给他” | 澄清率、误执行率 |
| 高风险动作 | 付款、删除、发送 | 确认覆盖率、越权率 |
| 能力不可用 | App 未安装、权限关闭 | 降级质量、解释清晰度 |

至少对照三条路径：

```text
原生 AppFunction
GUI Agent
原生 API + GUI 兜底
```

### 验收标准

- 有 30-50 条固定任务和明确的期望结果。
- 每次实验都有模型版本、设备、网络、权限和应用版本记录。
- 能输出失败分类，而不是只报一个总成功率。
- 能根据评测结果给出“原生 API、GUI 兜底或暂不支持”的产品决策。

### 关联笔记

- [[系统级 Intent 路由评估 SOP]]
- [[通用 AI Agent 评测基准 2026]]
- [[OSWorld 计算机操作基准]]
- [[PM决策层 MOC]]
- [[Loop Engineering 实战代码库]]

## 五、P0：端侧 AI Runtime 与设备性能工程

### 为什么必须学

你已经有较好的端侧模型系统知识，但目前主要是原理和 PM 推演。OS PM 需要进一步知道：某个模型或 Agent 能力在什么设备、温度、内存和功耗约束下真正可用。

### 学习模块

- 模型生命周期：加载、预热、推理、卸载、分页和缓存
- CPU / GPU / NPU 调度与异构执行
- FP16、INT8、INT4、量化误差和工具调用格式稳定性
- KV Cache、上下文长度、并发请求和内存峰值
- 首 Token 延迟、每 Token 延迟、吞吐和尾延迟
- 温控、电量、前台负载和动态降级
- Perfetto、Android Studio Profiler、Macrobenchmark、Android Vitals
- Google AI Edge、LiteRT、LiteRT-LM 和真实 Android 设备测试
- Runtime / Delegate：模型转换、图编译、算子覆盖、CPU / GPU / NPU fallback、动态 shape 和异步执行
- 系统 Runtime：App 内置 Runtime 与系统托管 Runtime 的内存、更新、隐私和兼容性边界

### 必做实践

固定一个小模型和一组工具调用任务，比较：

```text
FP16 vs INT8 vs INT4
上下文长度：2K / 8K / 32K
设备状态：空闲 / 前台视频 / 低电量 / 高温
执行方式：云端 / 端侧 / 端云混合
```

记录：

- 峰值 RAM 和模型加载时间
- 首 Token 延迟和端到端任务时延
- 工具调用格式正确率
- CPU / GPU / NPU 占用
- 电量和温度变化
- 降级触发条件及用户可见影响

不要只记录“使用了 NPU”。每次实验至少保留：

```text
model / runtime / SoC / OS / driver / quantization
supported_ops / fallback_ops / compile_time / load_time
TTFT / TPOT P50 / TPOT P95 / prefill_tok_s / decode_tok_s
peak_PSS / thermal_status / energy_per_token
```

特别注意：PagedAttention 的典型收益主要来自服务端多请求吞吐；手机端通常更接近 batch=1 交互场景，产品判断应优先看 TTFT、TPOT、尾延迟、持续性能和每 Token 能耗。

### 验收标准

- 能把模型能力转换为设备规格和产品承诺。
- 能解释为什么某项能力需要云端、端侧或混合架构。
- 能写出温度、内存、电量和网络变化下的降级矩阵。
- 所有性能数字都有设备、模型、量化和测试条件。
- 能识别 NPU 算子 fallback，并解释它如何改变性能、功耗和兼容性。
- 能用 10-30 分钟持续运行结果，而不是峰值结果，定义设备分层和发布门槛。

### 关联笔记

- [[OS-PM-端侧大模型系统级挑战]]
- [[OS-PM-PagedAttention与KV Cache剪枝]]
- [[OS-PM-3B模型内存预算推演]]
- [[OS-PM-AI Runtime动态调度与降级策略]]
- [[端侧 AI 基建与算力预算]]
- [[OS-PM-端侧AI Runtime 实测实验方案]]

## 六、P1：平台 API、Schema、Registry 与开发者生态

### 为什么必须学

OS Agent 的长期竞争力不是一个模型 Demo，而是一套让应用愿意接入、系统能够发现、调用方可以授权、平台能够治理的能力平台。

### 学习模块

- API / SDK 的稳定性和版本策略
- Intent Schema 的字段、类型、语义描述和错误码
- Registry 的注册、发现、排序、动态启用和撤销
- 权限与调用方身份
- App 接入流程、测试工具、调试工具和开发者文档
- 兼容性、迁移、灰度和回滚
- 第三方激励、流量分配、数据边界和商业责任
- 预定义 Schema 与开发者自由声明 Schema 的取舍

### 必做实践

写一份“安卓系统级 Intent Platform v0.1”方案，至少包括：

- Intent / Function Schema
- Registry 数据模型
- 能力发现和排序规则
- 只读、可逆写入、高风险动作的权限模型
- 调用超时、重试、幂等和错误码
- 动态启用 / 禁用机制
- App 接入测试清单
- 版本兼容和废弃策略
- 平台指标和开发者指标

### 验收标准

- 一个第三方 App 能在一周内完成接入。
- 一个调用方能知道能力的来源、权限、风险和版本。
- 平台能撤销能力、回滚版本和追踪调用结果。
- 方案同时考虑用户价值、开发者成本和平台治理。

### 关联笔记

- [[App Intent 的核心作用]]
- [[Intent Schema Protocol 意图模式规范]]
- [[Intent Router 语义路由]]
- [[MCP 与设备侧 MCP]]
- [[意图框架的商业与生态博弈]]
- [[竞品情报 MOC]]

## 七、P1：Agent 安全、隐私、身份与责任

### 当前判断

你的安全笔记已经覆盖 XPIA、ADI、确认、隔离和来源分级。下一步不要继续横向堆概念，而要把安全问题写成可执行的系统机制：谁授权、授权什么、作用于哪一份内容、如何审计、如何撤销。

建议把目标架构收敛为一个 Agent Control Plane：

```text
用户目标
→ Typed Intent IR
→ Capability / Policy Broker
→ Confirmation Token
→ 沙箱执行
→ OpenTelemetry Trace / Provenance 审计链
```

模型和工具都不能直接拥有 OS 副作用权限。所有外部副作用都必须经过 Broker，Broker 根据调用者、目标、数据等级、作用域、过期时间和可逆性做默认拒绝的策略判断。

### 学习模块

- Threat Modeling：资产、攻击面、信任边界、滥用案例
- Capability-based Security：给 Agent 最小能力，而不是给完整 App 权限
- 工具和 Agent 身份：调用方、代理、应用、用户和系统的区分
- 数据来源：用户输入、工具返回、文件、网页、模型生成内容
- Provenance：来源标记、敏感度升级、不可降级规则
- 确认机制：确认内容绑定、风险分级、二次确认和撤销
- 审计：谁在什么时间以什么权限执行了什么动作
- 隔离：低权限账号、工作区、沙箱和网络边界
- Android 安全边界：UID 沙盒、SELinux、导出组件、Intent redirection、隐式 Intent 劫持和点按劫持
- 可观测性：任务 Trace、策略版本、工具调用、确认结果、执行结果和错误回放

### 必做实践

创建一个“Agent 安全测试实验室”：

1. 恶意文档：把指令伪装成检索资料。
2. 恶意工具返回值：诱导 Agent 修改后续动作。
3. Schema 污染：注册一个描述相似但权限更高的工具。
4. 确认篡改：确认后修改参数，验证内容绑定是否失效。
5. 权限撤销：执行中关闭权限，验证系统是否停止。

每个案例都记录：攻击前提、攻击路径、预期拦截点、实际结果、修复机制和残余风险。

确认不应只是“是否继续？”对话框，而应绑定到规范化动作摘要、目标 App / 账户、数据范围、策略版本、nonce 和短 TTL。参数、目标、账户或页面状态变化后，原确认必须失效。

建议每个副作用任务记录以下事件链：

```text
user_goal → intent_candidate → policy_decision → tool_call
→ confirmation_request → confirmation_result
→ os_execution → side_effect_result
```

核心安全指标：

- Unauthorized Action Block Rate：越权动作拦截率
- Confirmation Bypass Rate：无有效确认却完成副作用的比例，目标为 0
- Stale Approval Acceptance Rate：旧确认被复用的比例，目标为 0
- Capability Overreach Rate：实际使用权限超出声明范围的比例
- Trace Completeness：有完整开始、策略、执行、结果闭环的动作比例
- Provenance Coverage：有来源引用和责任主体的输入 / 输出比例
- Sensitive Log Leakage Rate：日志中的明文敏感数据比例
- Duplicate Side-effect Rate：重试造成重复发送、支付或修改的比例
- Recovery Success Rate：失败后回滚或进入可控恢复状态的比例

### 验收标准

- 能画出 Agent 从用户请求到执行结果的信任边界。
- 每个高风险能力都有明确授权主体和审计记录。
- 安全要求能转化为 API 字段、系统闸口和测试用例。
- 能把“安全风险”写成发布 blocker 或可接受风险，而不是泛泛提醒。
- 所有外部副作用都经过 Broker；高影响动作没有确认绕过；审计 Trace 能闭环回放。

### 关联笔记

- [[安全 MOC]]
- [[Agent 执行安全（PM视角）]]
- [[Confirmation UI 分级与产品责任边界]]
- [[XPIA 跨提示注入]]
- [[Agent Data Injection 数据注入攻击]]
- [[数据溯源分级与单调棘轮]]
- [[Agent Workspace 隔离执行]]
- [[OS-PM-Agent Control Plane 安全与审计]]

## 八、P1：Agent UX、用户研究与失败恢复

### 学习重点

Agent UX 不等于做一个聊天框。OS PM 要设计的是一套状态和责任交互：系统什么时候理解了、什么时候在等待、什么时候需要用户确认、失败后谁负责。

- 意图识别状态：已理解、部分理解、无法理解
- 执行状态：排队、执行中、等待权限、等待用户、已完成
- 失败状态：参数错误、权限不足、应用不可用、网络失败、部分完成
- 风险表达：为什么需要确认、确认的具体对象是什么
- 可逆性：撤销、回滚、补偿和人工接管
- 主动性：推荐、预测和自动执行的边界
- 多设备交接：任务状态、确认设备、结果回显和责任归属

### 必做实践

用 Figma 做一个包含四种状态的 Agent 任务卡：

```text
待确认 → 执行中 → 已完成
             ↘ 失败 / 降级 / 人工接管
```

分别设计低、中、高风险策略，并进行至少 5 人的可用性测试。测试重点不是“好不好看”，而是用户能否回答：

- Agent 准备做什么？
- 它为什么需要这个权限？
- 现在做到哪一步？
- 失败后发生了什么？
- 我能否撤销？

### 关联笔记

- [[Figma 学习笔记]]
- [[安卓系统功能原型规格模板]]
- [[Confirmation UI 安全机制]]
- [[OS-PM-性能与稳定性指标体系]]

## 九、P2：跨设备 Agent 与生态协同

这一方向值得学习，但不应早于 Android 基础、评测和端侧 Runtime。

重点包括：

- 手机、车机、PC、手表、音箱和 IoT 的设备发现
- 任务状态迁移和上下文压缩
- 哪台设备负责理解、执行、确认和结果展示
- 多设备并发时的冲突处理
- 离线、断网和设备离线时的降级
- A2A、MCP 和系统级 Intent 的边界
- OEM、应用、云服务和用户之间的责任划分

最终产出一份“手机作为意图中枢”的跨设备任务协议草案，而不是继续做平台新闻汇总。

## 十、语言与工具选择

### Kotlin / Android：优先级最高

这是你作为 Android / OS PM 最应该补的工程语言。目标不是成为 Android 工程师，而是能读懂系统 API、写出最小 Demo、理解生命周期和调试日志。

### Rust：第二优先级

适合继续理解系统组件、内存安全、Runtime、底层服务和高性能模块。先围绕一个真实项目学习，不要单独扩展成语言收藏。

### Go：按需学习

适合工具服务、测试平台、Agent 后端和并发服务。如果你的评测平台或内部工具使用 Go，再深入即可。

### LangChain / LangGraph / RAG

保持“够用”即可。它们是实现和验证 Agent 方案的工具，不应成为你的主学习方向。已有内容足够支撑原型和评测：[[AI Agent 框架 MOC]]、[[RAG 详细学习笔记]]。

## 十一、12 周执行路线

| 周期 | 学习重点 | 必须留下的产出 |
|---|---|---|
| 第 1-2 周 | Kotlin、Android 组件、Intent、权限、Binder 心智模型 | Android 系统级 Agent 分层架构图 |
| 第 3-4 周 | AppFunctions、Registry、KDoc Schema、ADB | 三个 AppFunction 的最小 Demo |
| 第 5-6 周 | 任务集、路由评测、错误分类、日志回放 | 30-50 条 OS Agent 评测集 |
| 第 7-8 周 | LiteRT / LiteRT-LM、量化、Perfetto、性能指标 | FP16 / INT8 / INT4 性能对照表 |
| 第 9-10 周 | 权限、确认、来源、隔离、红队测试 | Agent 安全测试实验室记录 |
| 第 11 周 | Figma 状态机、失败恢复、用户测试 | 可测试 Agent 任务卡原型 |
| 第 12 周 | 平台 API、生态接入、发布治理 | Intent Platform v0.1 方案和 PM 评审稿 |

## 十二、每周学习笔记模板

```markdown
---
type: learning-log
topic:
direction: OS PM / Android / Agent / Runtime / Security / UX
status: learning
source:
experiment:
decision:
updated:
---

# 主题

## 我想解决的产品问题

## 技术事实

## 对 OS PM 的影响

## 我的判断

## 实验或验证

## 指标

## 风险与待核实项

## 关联笔记
```

## 十三、暂时不要优先做的事

- 不要继续无上限收集 Agent 框架和模型新闻。
- 不要同时把 Go、Rust、Kotlin 都学成完整工程师路线。
- 不要只看 benchmark 数字，不记录设备、模型、版本和测试条件。
- 不要把 Figma 做成纯视觉练习，要绑定状态机和产品决策。
- 不要在没有任务集和实验的情况下继续扩写“评测方法论”。
- 不要把未经一手核实的行业结论写成平台事实。

## 十四、官方资料入口

### Android / AOSP

- [AOSP 架构概览](https://source.android.com/docs/core/architecture)
- [Android AppFunctions 概览](https://developer.android.com/ai/appfunctions)
- [Android Intent 和 Intent Filter](https://developer.android.com/guide/components/intents-filters)
- [Android 权限概览](https://developer.android.com/guide/topics/permissions/overview)
- [Android 后台任务与 WorkManager](https://developer.android.com/topic/libraries/architecture/workmanager)
- [Android Vitals](https://developer.android.com/topic/performance/vitals)
- [Perfetto 文档](https://perfetto.dev/docs/)
- [Macrobenchmark](https://developer.android.com/topic/performance/benchmarking/macrobenchmark-overview)

### 端侧 AI

- [Google AI Edge](https://ai.google.dev/edge)
- [LiteRT](https://developers.google.com/edge/litert)
- [LiteRT-LM](https://developers.google.com/edge/litert-lm)
- [Android AI](https://developer.android.com/ai)

### Agent / 安全 / 评测

- [OWASP Top 10 for LLM Applications](https://owasp.org/www-project-top-10-for-large-language-model-applications/)
- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework)
- [NIST Generative AI Profile](https://www.nist.gov/itl/ai-risk-management-framework/generative-ai-profile)
- [OSWorld](https://os-world.github.io/)
- [Berkeley Function-Calling Leaderboard](https://gorilla.cs.berkeley.edu/leaderboard.html)
- [Model Context Protocol](https://modelcontextprotocol.io/specification)
- [A2A Protocol](https://a2a-protocol.org/latest/)

> 资料使用规则：官方文档用于确认 API、架构和约束；论文用于确认方法；厂商博客用于了解路线；媒体和二手榜单只能作为线索。所有性能数字必须回到自己的设备和任务集复测。

## 关联入口

- [[OS产品经理知识库 MOC]]
- [[手机AI智能体知识库]]
- [[意图框架·跨体系索引 MOC]]
- [[PM决策层 MOC]]
- [[知识飞轮看板]]
