---
type: concept
status: draft
derived_from: "[[AppIntent 每日情报 2026-09-16]]"
tags:
  - AppIntent
  - 端侧Agent执行总线
  - NPU
  - 芯片原生agentic loop
---

# 端侧 Agent 执行总线 NPU 原生 agentic loop（2026）

> 全新主题：库内既有节点只覆盖 OS 框架层（App Intents / AppFunctions / Intents Kit / ODR）与端侧 Planner 模型评测（[[Function Calling 端侧工具调用]]）。本节点补「芯片原生 agentic loop」这一**硅底执行总线**层——把端侧 Agent 的规划/路由/工具调用闭环从软件栈假设变成 NPU/APU 原生能力。

## 一句话定义

2026 年旗舰移动 SoC（高通 Hexagon / 联发科 Dimensity）把「端侧 Agent 执行总线」下沉到 NPU/APU 原生能力——芯片内闭环完成 **感知 → 编排（planning / routing / tool call / reflection）→ 异构推理 → 响应**，使 OS Agent 的端侧执行有独立算力底座，敏感数据默认不出端。

## 为什么重要

- **算力底座升级**：端侧 Planner/路由的可用算力从「软件堆在通用 NPU 上」升级为「芯片原生 agentic loop」——32K 长上下文、KV-Cache 硬件加速、端上 30B MoE 直接服务**多步意图路由与长对话编排**，而非只能跑单轮小模型。
- **架构默认形态**：「规划/路由在芯片内闭环、敏感数据不出端」成为 SoC 级默认能力，OS 框架层（App Intents / AppFunctions / ArkAF）的端侧执行可假定该底座存在。
- **与评测表闭环**：与 [[Function Calling 端侧工具调用]] 的端侧 Planner 评测（Needle 2 / FunctionGemma / Apple FM / qwen3-0.6b-tool-router）形成「模型能力 ↔ 芯片算力」双轴，选型不能只看模型 BFCL 分，还要看芯片能否跑其长上下文多步编排。

## 适用边界

- 芯片层，非 OS 框架 API；具体规格（TOPS / 上下文上限 / MoE 规模）以各厂商 Snapdragon Summit / CES 官方文档为准。
- 当前为高端旗舰 SoC（Snapdragon 8 Elite Gen 5 / Dimensity 9500S）能力，中低端与旧设备仍受 NPU 成熟度与内存带宽约束（见 [[端侧 Router 置信度门控与工具可达性收缩 2026]] 的「体积不变下加闸」约束）。

## 证据与例子

- **Qualcomm Hexagon NPU（Snapdragon Summit 2026 前披露，securityexpress.info 转述）**：
  - 新增 **Element Accelerator**（与 Tensor/Vector/Scalar 并列）+ 共享内存 **+50%**，面向 Fast Action Loops、32K 长上下文、KV-Cache 加速。
  - INT4 量化下：预填充效率较前代 **+50%**、TTFT 短至 **1.5s**、端上支持 **30B MoE**。
  - **On-die agentic loop**：Sensing Hub 常驻感知（Ambient Voice In）→ Oryon CPU（5GHz+）中央编排（tokenization / planning / routing / tool calls / reflection / response）→ Hexagon NPU + Adreno GPU 异构推理 → 端上低延迟 Voice Response Out，不上云。
- **MediaTek Dimensity 9500S（CES 2026）**：业界首个 **Compute-in-Memory（CIM）** 架构，原生支持 **BitNet 1.58-bit** 模型，3B 参数模型 50% 更低功耗、128K 上下文。

## 可复用启发

- **选端侧 Planner 模型时，「芯片能否跑其长上下文多步编排」是硬约束，不只是 NPU TOPS 数字**：一个 BFCL 分高但需 128K 上下文多步反思的模型，在只支持 32K 的 NPU 上会退化；选型要把 [[Function Calling 端侧工具调用]] 的模型画像与本节点芯片画像并列看。
- **OS Agent 架构应默认「规划/路由在芯片内闭环、敏感数据不出端」**：端侧 Planner（[[端侧 Router 置信度门控与工具可达性收缩 2026]]）的「未选中工具物理挡在上下文外」等结构闸，未来可在芯片层更廉价实现（NPU 原生 agentic loop 的 Fast Action Loops + Element Accelerator）。
- **「云-端路由」是双轴问题**：模型层（iOS 27 Foundation Models / Firebase Hybrid Inference 的 PREFER_ON_DEVICE 等）与芯片层（on-die loop、CIM 低功耗）共同决定「何时留端、何时上云」，不能只在一层解决（见 [[四平台意图 Registry 来源轴与权限模型对比 2026]]）。

## 关联

- 上游/互补：[[Function Calling 端侧工具调用]]（端侧 Planner 评测表）｜ [[Agentic OS 意图调度内核]]（OS 级意图调度）｜ [[端侧 Router 置信度门控与工具可达性收缩 2026]]（结构闸）｜ [[四平台意图 Registry 来源轴与权限模型对比 2026]]（跨平台对照）
- 索引：[[意图框架·跨体系索引 MOC]]

## 2026-09-26 增补：Snapdragon 8 Elite Gen 6 官方落地（关闭 09-16「待 Summit 确认」待办，来源 [[AppIntent 每日情报 2026-09-26]]）

> 接续 09-16 的「高通 NPU 原生 agentic loop（前 keynote 披露，exact specs 待 Summit 确认）」。Snapdragon Summit 2026（9-22~25，Maui）高通正式发布 **Snapdragon 8 Elite Gen 6 / Extreme Gen 6**（2nm），把 09-16 记录的「前披露信号」升级为**已发布平台规格**（多源 corroboration：工商时报 ctee 9-25 / DigitalToday 9-22 / ABI Research / 朝鲜日报 biz.chosun 9-24）。

**① Hexagon NPU 为 Agentic AI 重新设计（本节点核心增量）**
- 配置：**12 个 scalar cores + 8 个 vector cores + 升级 matrix cores**，并**首增「element-wise accelerator」——专为 Transformer 与 Agentic AI 设计**（09-16 记录的「Element Accelerator」获官方命名与定位确认）。
- **NPU 共享内存 +50%**，支持**端上 32K context** 与 **MoE 模型**；KV-Cache 留 NPU 内减少外访 DDR、降延迟。
- 演示：直接跑在 NPU 上的本地语言模型分析 ~500 段影片，自动按食物/器材/场景归档并产出脚本——全程端上、CPU/GPU 负责影音处理。

**② 端上 30B+ MoE（改写「端侧能跑多大」上限）**
- 高通称新平台可跑 **30B+ 参数 MoE**（HBM 近存 + UFS 5.0 智能闪存管理，只把 needed parts 从闪存载入、频繁数据留 NPU）。
- 每个 token 步**仅激活 ~3B 参数**；演示 agent 读 summit 邀请、识别日期/航班/场馆并规划 3 天行程（理解→推理→执行阶段激活不同 expert）——这是「端侧多步意图编排」而非单轮小模型的硬件底座。
- ABI Research：新 NPU 较前代 **最快 +35%、性能/瓦特 +33%**；高通把数据中心的 **High-Bandwidth Compute（HBC）** 引入 Snapdragon 线（手机/AI PC/穿戴），MWC27 再细化。

**③ Oryon CPU 作「协调中柢」（Fast Action Loop 的编排层）**
- Snapdragon 8 Elite Gen 6 引入 **FlexCache**：跨 8 核共享 L2 池、按需动态分配；高通原话——「今日 AI agent 要 reason、找 context、call tools、把工作跨 CPU 推进，FlexCache 让切换更快」。
- 与 09-16 记录的 on-die agentic loop（Sensing Hub 常驻感知 → Oryon 中央编排 → Hexagon/Adreno 异构推理 → 响应）构成**完整芯片级执行总线**画像。

**④ 跨设备 personal AI 生态（day 2，9-23 Ziad Asghar）**
- 手机为 AI hub，眼镜/手表/耳塞/AI pin 共享用户 context 与 intent 并代为执行；AI 眼镜 demo 端上跑模型、飞行模式可用；Snapdragon Sound Elite Gen 2 耳塞算力/AI 翻倍、功耗 -40%、直连云/agent。
- → 这是「端侧 Agent 执行总线」从单设备向**多设备意图共享**延伸的生态信号（非 OS 框架 API）。

→ **对 OS PM 的含义**：09-16 提出的「芯片原生 agentic loop」从假设变为**已发布旗舰平台能力**；OS 框架层（App Intents / AppFunctions / ArkAF）的端侧执行可假定「32K 上下文 + 30B MoE + 芯片内多步编排」底座存在——端侧 Planner 选型（[[Function Calling 端侧工具调用]]）的「芯片能否跑其长上下文多步编排」硬约束被具体化。

⚠️ 诚实标注：上述为高通 keynote + 多源媒体转述，**具体 TOPS / 峰值功耗 / 量产机型上市日**以高通官方 whitepaper / 量产 SoC 规格为准；「30B MoE 端上跑、每次 token 激活 ~3B、UFS 5.0 直接跑」为高通演示口径；本节点仍为「跨平台端侧执行总线硅底信号」，非 OS 框架 API 增量。

#标签/端侧Agent执行总线 #标签/NPU #标签/芯片原生agentic loop
