---
title: OS PM 资料导航与阶段学习计划
type: curriculum
status: active
tags: [OS产品经理, 资料导航, 学习计划, 端侧AI, Agent]
created: 2026-08-06
updated: 2026-08-06
related: [OS-PM-学习方向与能力地图, OS产品经理知识库 MOC, 知识飞轮看板]
---

# OS PM 资料导航与阶段学习计划

> 使用方式：每个阶段只读“核心资料”，读完必须完成一个产出，再进入下一阶段。其他笔记作为查阅资料，不要求一次性通读。

## 一、资料分层规则

| 层级 | 目录 / 内容 | 用法 |
|---|---|---|
| 核心 | `01-笔记` 中的手写 MOC、学习笔记、PM 决策和实验方案 | 按路线精读，形成自己的判断 |
| 方法 | `10-知识飞轮/C-可复用方法` | 做实验、写 PRD 和评测时调用 |
| 情报 | `10-知识飞轮/A-原始资料`、`B-泛化概念` | 只用于补充事实、发现问题和追踪变化 |
| 输出 | `10-知识飞轮/D-输出内容` | 用来复盘当前阶段是否形成了可交付成果 |
| 项目 | `02-项目` | 保存端到端实践，不要把项目过程拆散回资料库 |

### 情报阅读纪律

- 不从每日情报开始学习；先读核心笔记，再回查原始资料。
- B 层概念只选与当前阶段有关的条目，不追求全部读完。
- 带“待补 / 待核实”的内容不能直接当作平台事实写入 PRD。
- D 层月报和日报用于复盘，不替代官方文档和实验数据。

## 二、总路线

```text
阶段 0 统一心智模型
→ 阶段 1 Android / AOSP 平台契约
→ 阶段 2 Agent 评测与可靠性
→ 阶段 3 端侧 AI Runtime 与设备性能
→ 阶段 4 平台治理与开发者生态
→ 阶段 5 安全 Control Plane
→ 阶段 6 Agent UX 与跨设备
→ 阶段 7 端到端项目交付
```

## 三、阶段 0：统一心智模型

### 学习目标

理解 OS PM 的完整工作对象：系统能力、应用接入、Agent 路由、Runtime、用户控制、评测和生态治理。

### 核心资料

1. [[OS-PM-学习方向与能力地图]]
2. [[OS-PM-概览与四大核心领域]]
3. [[OS-PM-系统架构与底层技术]]
4. [[手机AI智能体知识库]]
5. [[端侧意图框架 学习笔记]]
6. [[PM决策层 MOC]]

### 辅助资料

- [[意图框架·跨体系索引 MOC]]
- [[应用层 Agent 框架 vs 系统级意图框架 对照]]
- [[AI Agent 框架 MOC]]
- [[发散图谱 MOC]]

### 必须产出

- 一张“用户目标 → Intent → Registry → Router → Runtime → App → 结果”的系统图。
- 一页纸说明 App 层 Agent、OS 层 Agent 和模型层能力的边界。

## 四、阶段 1：Android / AOSP 平台契约

### 学习目标

回答：一个 AI 能力应该放在 App、Jetpack、Framework、System Service、Runtime、HAL 还是芯片层？

### 核心资料

1. [[OS-PM-系统架构与底层技术]]
2. [[App Infra 应用基建]]
3. [[App Intent 的核心作用]]
4. [[Android AppFunctions 设备侧意图 2026]]
5. [[端侧意图框架 学习笔记]]
6. [[MCP 与设备侧 MCP]]

### 必查资料

- [[Intent Schema Protocol 意图模式规范]]
- [[Intent Router 语义路由]]
- [[Function Calling 端侧工具调用]]
- [[Agentic OS 意图调度内核]]
- [[System Orchestrator 系统编排]]

### 当前缺口资料

以下主题目前没有形成独立主线，应作为 Android 平台补课：

- Binder / AIDL / System Service
- UID 沙盒、SELinux、导出组件、URI 授权
- WorkManager、JobScheduler、前台服务和进程死亡恢复
- ContentProvider、SAF、AppSearch、Room / DataStore
- API level、CDD、CTS / VTS / GTS、Mainline、APEX、GKI、OTA
- Perfetto、`dumpsys`、bugreport 和系统问题证据链

### 必须产出

- 一个 AppFunctions 能力网关 Demo：查询、创建、修改三个函数。
- 一张 API、权限、生命周期、错误和版本兼容矩阵。
- 一份“哪些能力不能直接走 IPC”的 PM 判断表。

## 五、阶段 2：Agent 评测与可靠性

### 学习目标

从“Agent 能不能调用工具”升级到“在真实设备和真实任务中是否可靠、可解释、可回放”。

### 核心资料

1. [[系统级 Intent 路由评估 SOP]]
2. [[OS-PM-性能与稳定性指标体系]]
3. [[端侧意图路由选型 PM Checklist]]
4. [[OS-PM-Agent平台治理与开发者生态]]
5. [[Loop Engineering 循环工程]]
6. [[Loop Engineering 实战代码库]]

### 评测资料

- [[通用 AI Agent 评测基准 2026]]
- [[Local Agent Bench 端侧智能体基准]]
- [[OSWorld 计算机操作基准]]
- [[Function Calling 端侧工具调用]]
- [[Intent Routing Stack 六方意图路由分层对照 2026]]
- [[Simple Attention Network 无FFN端侧路由]]

### 必须建立的任务集

| 类别 | 任务示例 | 关注指标 |
|---|---|---|
| 只读 | 查邮件、日程、文件 | 路由和引用准确率 |
| 单 App 写入 | 新建待办、创建日程 | 参数正确率、完成率 |
| 跨 App | 从邮件提取内容加入清单 | 多步完成率、恢复率 |
| 歧义 | “把它发给他” | 澄清率、误执行率 |
| 高风险 | 付款、删除、发送 | 确认覆盖率、越权率 |
| 不可用 | 未安装、无权限、网络断开 | 降级质量、解释清晰度 |

### 必须产出

- 30-50 条固定任务和期望结果。
- 错误分类树：路由、Schema、参数、权限、执行、结果理解。
- Metrics Dictionary：事件名、字段、公式、P50 / P95、质量红线。
- 原生 API、GUI Agent、原生 API + GUI 兜底三路对照报告。

## 六、阶段 3：端侧 AI Runtime 与设备性能

### 学习目标

把模型原理转换成真实设备上的延迟、内存、功耗、热和兼容性决策。

### 核心资料

1. [[OS-PM-端侧AI Runtime 实测实验方案]]
2. [[OS-PM-AI Runtime动态调度与降级策略]]
3. [[OS-PM-端侧大模型系统级挑战]]
4. [[OS-PM-3B模型内存预算推演]]
5. [[OS-PM-PagedAttention与KV Cache剪枝]]
6. [[OS-PM-投机采样原理与能效优化]]
7. [[OS-PM-系统AI Runtime vs 应用引擎]]

### 辅助资料

- [[端侧 AI 基建与算力预算]]
- [[端侧大模型推理 学习笔记]]
- [[AI模型类型与架构]]
- [[外挂适配式 vs 原生多模态架构]]
- [[OS-PM-性能与稳定性指标体系]]

### 必须测量

- TTFT、TPOT、P50 / P95 尾延迟；
- FP16、INT8、INT4 的模型体积、质量和 NPU fallback；
- 峰值 PSS、KV bytes/token、workspace 和 OOM 临界点；
- CPU / GPU / NPU 占用、功耗、温度和持续性能；
- App Runtime 与系统 Runtime 的启动、更新、隐私和兼容性。

### 必须产出

- 一份 FP16 / INT8 / INT4 设备实验报告。
- 一张高端 / 中端 / 低端设备能力矩阵。
- 一份温控、低电量、内存压力、网络异常下的降级 PRD。

## 七、阶段 4：平台治理与开发者生态

### 学习目标

从“设计一个 Intent”升级到“设计一套应用愿意接入、系统能够治理的能力平台”。

### 核心资料

1. [[OS-PM-Agent平台治理与开发者生态]]
2. [[App Intent 的核心作用]]
3. [[Intent Schema Protocol 意图模式规范]]
4. [[Android AppFunctions 设备侧意图 2026]]
5. [[意图框架的商业与生态博弈]]
6. [[竞品情报 MOC]]

### 平台对照资料

- [[Apple Intelligence 与 App Intents]]
- [[Apple AppIntents Schema Protocol 2026]]
- [[HarmonyOS 元服务 学习笔记]]
- [[HarmonyOS Intents Kit 与 ArkAF 2026]]
- [[HarmonyOS 意图框架竞品观察]]
- [[Windows Copilot Actions 与 Agent Workspace 2026]]
- [[Windows Copilot Actions 竞品观察]]
- [[企业级 Agent 平台与 Agent-as-Asset 2026]]

### 协议资料

- [[MCP 与设备侧 MCP]]
- [[A2A 端侧智能体协议]]
- [[智能体互联国家标准与 AIP]]
- [[Intent Routing Stack 六方意图路由分层对照 2026]]

### 必须产出

- `Intent Contract v0.1`：Intent、Entity、Result、Error、Permission、Risk、Source、Version。
- `Registry Spec v0.1`：注册、发现、排序、动态启停、撤销和废弃。
- `Developer Conformance Kit`：SDK、Lint、模拟器、测试夹具和 Replay。
- 一份 App 接入成本、开发者收益和平台治理方案。

## 八、阶段 5：Agent Control Plane 安全

### 学习目标

把 XPIA、ADI、确认、来源分级、隔离和审计从概念变成系统闸口。

### 核心资料

1. [[OS-PM-Agent Control Plane 安全与审计]]
2. [[Agent 执行安全（PM视角）]]
3. [[Confirmation UI 分级与产品责任边界]]
4. [[工具调用安全 学习笔记]]
5. [[安全 MOC]]

### 自动情报资料

- [[XPIA 跨提示注入]]
- [[Agent Data Injection 数据注入攻击]]
- [[文档型 XPIA 自传播蠕虫]]
- [[数据溯源分级与单调棘轮]]
- [[带外防御与确定性门控]]
- [[Agent Workspace 隔离执行]]
- [[Agent 身份与硬件级审批]]
- [[Dual View 智能体数据视图隔离]]
- [[Confirmation UI 安全机制]]
- [[意图支付授权协议 APOP]]

### 方法资料

- [[Agent 读入路径可信数据边界 SOP]]
- [[Agent 写回路径 XPIA 风险评估 SOP]]
- [[端侧执行通道选型 SOP]]

### 必须产出

- Typed Intent IR 和 Capability / Policy Broker 方案。
- Confirmation Token 规范：动作摘要、目标、数据范围、策略版本、nonce、TTL。
- Agent Security Evaluation Harness：恶意文档、恶意工具返回值、旧确认重放、权限撤销和数据外泄。
- 审计 Trace：目标、路由、策略、工具、确认、执行、结果。

## 九、阶段 6：Agent UX 与跨设备

### 学习目标

设计 Agent 的状态、责任和恢复，而不是只做一个聊天入口。

### 核心资料

1. [[Figma 学习笔记]]
2. [[安卓系统功能原型规格模板]]
3. [[OS 系统级 Agent PRD 范例]]
4. [[Confirmation UI 分级与产品责任边界]]
5. [[跨端与多设备意图流转]]
6. [[Agent 记忆与个性化意图理解]]

### 参考资料

- [[发散图谱 MOC]]
- [[原型与Figma MOC]]
- [[意图框架的商业与生态博弈]]
- [[HarmonyOS 意图框架竞品观察]]
- [[Windows Copilot Actions 竞品观察]]

### 必须覆盖的状态

```text
待确认 / 执行中 / 等待用户 / 需要接管
成功 / 失败 / 部分完成 / 可撤销
```

### 必须产出

- 一套低、中、高风险确认组件。
- 一个包含失败、降级、撤销和人工接管的可点原型。
- 12 个核心任务的用户访谈和可用性测试记录。
- `Task Envelope v0.1`：跨设备身份、状态、确认、离线、幂等和回滚。

## 十、阶段 7：端到端项目交付

### 推荐项目

做一个“系统级个人任务 Agent”小项目，不追求功能多，追求闭环完整：

```text
自然语言目标
→ Typed Intent
→ Registry 发现
→ 路由决策
→ 权限判断
→ 确认
→ 原生 API 执行
→ 失败 / 降级
→ Trace 回放
→ 评测报告
```

### 项目资料

- [[Codex_Obsidian_自生长知识库]]：记录知识库和自动化工作流，不作为 Agent 产品技术主线。
- [[OS-PM-学习方向与能力地图]]：能力模型和 12 周计划。
- [[OS-PM-Agent平台治理与开发者生态]]：平台契约和生态方案。
- [[OS-PM-端侧AI Runtime 实测实验方案]]：设备性能实验。
- [[OS-PM-Agent Control Plane 安全与审计]]：安全和审计机制。

### 项目验收

- 至少 3 个能力：只读、可逆写入、高风险模拟；
- 至少 30 条评测任务；
- 至少 1 条原生 API 与 GUI 兜底对照；
- 有权限、确认、失败、降级和撤销状态；
- 有可回放 Trace 和指标报告；
- 有一份“是否值得系统级托管”的 PM 结论。

## 十一、当前暂缓资料

这些资料不是无价值，而是暂时不进入主线：

- 每日 AppIntent 情报：只在阶段 4 或竞品评审时查看；
- 泛化 Agent 框架新闻：只在需要选型时查看；
- LangChain / LangGraph / RAG：用于实现项目，不作为 OS PM 主线；
- Go / Rust：先用 Kotlin / Android 支撑平台实践，后续按项目补；
- 过多跨学科发散：保留在发散图谱，不替代阶段产出。

## 十二、每周执行节奏

```text
周一：精读 1 篇核心笔记，写出 3 个问题
周二：查官方文档或源码，补事实证据
周三：做一个小实验或画一张架构图
周四：把实验结果写成指标或 PRD 判断
周五：回链相关笔记，清理待核实项
周末：输出一页复盘，决定下周是否继续该方向
```

## 关联入口

- [[OS产品经理知识库 MOC]]
- [[OS-PM-学习方向与能力地图]]
- [[意图框架·跨体系索引 MOC]]
- [[知识飞轮看板]]

