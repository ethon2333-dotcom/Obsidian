---
title: 端侧模型与 SoC 协同设计 学习笔记
tags:
  - topic/端侧AI
  - anchor/SoC协同设计
  - anchor/软硬协同
  - anchor/模型芯片co-design
created: 2026-10-13
source: 综合高通/联发科/苹果/华为/谷歌 2025–2026 公开资料与厂商发布，经 WebSearch 核实（非厂商口径均已标「待核实」）
---

> 一句话心智模型：这是「为芯片反向定制模型」的软硬协同设计——本质是**让模型结构、数值格式与算子去适应特定 NPU 的微架构约束**，而非把通用模型硬塞进加速器。

本篇与库内 [[端侧 AI 芯片架构谱系 学习笔记]]（硬件微架构对比）、[[端侧大模型推理 学习笔记]]（运行时/推理落地）、[[端侧模型量化 学习笔记]]（量化方法）、[[端侧推理框架生态 学习笔记]]（运行时框架）角度不同——它们是「从模型到芯片」的自上而下落地，本篇是「从芯片到模型」的反向协同设计视角，聚焦**为特定 SoC/NPU 反向定制算子友好、量化友好的网络结构与编译协同**。

## 定义

**端侧模型与 SoC 协同设计（model–chip / hardware–software co-design）**：从目标 NPU 的算力形态（MAC 阵列 / Cube / Vector）、存储层级（片上 SRAM、CIM）、精度支持（INT8/INT4/FP8/1.58-bit）、算子库（原生融合算子 vs 需回退 CPU/GPU 的自定义算子）出发，反向设计网络结构、量化方案与编译策略，使模型在端侧既「跑得动」又「跑得高效」。区别于单纯的「训练后量化 + 推理框架部署」，协同设计在**模型定义阶段**就纳入硬件约束。

## 分类

- **按协同深度递进**：
  1. 算子友好（operator-friendly）—— 选用 NPU 原生高效算子，规避回退；
  2. 量化友好（quantization-friendly）—— 权重/激活对齐 NPU 支持的精度；
  3. 架构搜索（NAS for NPU）—— 在延迟/功耗约束下搜网络；
  4. 芯片–模型联合定义（joint definition）—— 芯片厂直接定义数值格式 / 专用单元，模型按之设计。
- **按驱动方**：芯片厂主导（高通+Nexa、Apple 3B、Google Gemini Nano、MediaTek BitNet）、模型厂适配（Qwen / DeepSeek / 面壁 MiniCPM 端侧化）、框架/编译器桥接（QNN / CANN / Core ML Tools / NeuroPilot）。

## 主流方案

### 协同设计模式对比表

| 协同模式 | 核心做法 | 代表实践 | 主要收益 |
|---|---|---|---|
| 算子友好 | 选用 NPU 原生融合算子（matmul+激活等），避免自定义 kernel 回退 CPU/GPU | Core ML 层 op/shape 约束、QNN EP 兼容 | 不回退、延迟稳、能效可预测 |
| 量化友好 | 权重/激活对齐 NPU 精度，硬件感知量化降 perplexity | NexaQuant、BitNet 1.58-bit、Core ML 8-bit PTQ | 体积/带宽/功耗下降 |
| 架构搜索（NAS for NPU） | 以 NPU 延迟/功耗/面积为约束搜 Pareto 最优网络 | NPU-aware NAS 工具（学术 + 厂商内部） | 精度–延迟最优 |
| 联合定义 | 芯片厂定数值格式/专用单元，模型按之设计 | 高通 Hexagon INT2/FP8、联发科 CIM 超能效 NPU、Apple ANE | 端到端能效跃升 |

### 主流 SoC 厂 co-design 策略表

| 厂商 | NPU / 加速单元 | 协同设计策略 | 2025–2026 标志动作（厂商/媒体口径，数字多待核实） |
|---|---|---|---|
| 高通 Snapdragon | Hexagon NPU（QNN 栈） | NPU-aware 模型 + QNN EP + NexaQuant | OmniNeural-4B（号称首个 NPU 感知多模态，2025-09）；第五代骁龙 8 至尊版 Hexagon 支持 INT2/FP8 |
| 联发科 Dimensity | NPU 990（双 NPU）/ NeuroPilot | 数值格式协同（BitNet 1.58-bit）+ CIM 超能效 NPU + 开发者工具链 | Dimensity 9500（2025-09）首搭 CIM 超能效 NPU；MDDC 2025 推 Dimensity Development Studio |
| 苹果 | ANE + GPU 内神经网络加速器 + Core ML | 模型为 ANE op/shape 约束定制 + Core ML PTQ + Metal 4 张量 API | M5（2025-10）每 GPU 核含 NLA；Apple 3B 基础模型走 Core ML/ANE |
| 华为（海思/昇腾） | 达芬奇架构 NPU（麒麟）/ 昇腾（CANN） | 盘古端侧化 + 达芬奇 Cube/Vector 调度 + KV cache 4-bit | 麒麟 9050 Pro 端侧 30B（待核实）；昇腾 CANN 2025-08 开源 |
| 谷歌 | Tensor TPU + AICore | Gemini Nano 为 TPU 结构定制 + AICore 系统级聚合调度 | Gemini Nano v3（Pixel 10 Pro 940 tok/s，待核实） |

## 2025–2026 进展

- **芯片厂自研/联合定制小模型成主流**：高通联合 Nexa AI 推 OmniNeural-4B（"从底层架构就为 Hexagon NPU 本地运行而设计"，多模态文本/语音/视觉），Apple 推 3B 端侧基础模型、Google 推 Gemini Nano、联发科在 NPU 990 落地 BitNet 1.58-bit 端侧大模型运算。
- **数值格式协同**：高通 Hexagon 支持 INT2 与 FP8；联发科 BitNet 1.58-bit（减少端侧存储需求、降功耗）；华为昇腾 950 系列全面支持 HiFP8 / MXFP8 / MXFP4。
- **存算一体（CIM）下沉端侧**：联发科 Dimensity 9500 超能效 NPU 首搭集成 CIM 架构，主打 AI 模型常驻运行（always-on 主动式 AI）。
- **编译器/工具链收口**：QNN（Qualcomm AI Engine Direct）、CANN（华为，2025-08 开源）、Core ML Tools（8.x 系列，9.x beta）、NeuroPilot / Neuron Studio（联发科）成为「芯片算力 ↔ AI 应用」的中间件。
- **厂商生态联动**：联发科 MDDC 2025 联合荣耀/小米/阿里云/微软/面壁智能发起「智能体化体验领航计划」，把"芯片+系统+模型"三方联动作为端侧 Agent 落地路径。

## 代表产品与玩家

- **芯片厂**：Qualcomm、MediaTek、Apple、华为海思、Google（Tensor）、Samsung（Exynos，含 NPU + 与 AMD/新路线传闻待核实）。
- **模型/工具厂**：Nexa AI（OmniNeural / NexaML）、面壁智能（MiniCPM 端侧）、阿里（Qwen 端侧）、DeepSeek（昇腾 Day-0 适配）。
- **学术/工具方向**：NPU-aware NAS、硬件感知量化（HAQ 类）、Triton / PTO-ISA（华为昇腾自定义算子编程范式）、hollance/neural-engine（社区逆向记录 ANE 每代 op 支持，已成为工程师事实参考）。
- **与端侧生命周期衔接**：协同设计产出的定制模型同样经过 [[端侧模型 OTA 更新与生命周期管理 学习笔记]] 的灰度/AB/回滚治理；华为端侧 Agent 与盘古底座见 [[鸿蒙 NEXT 端侧 Agent 与元服务生态 学习笔记]]。

## 待解问题（留给 Ethon 后续深潜）

- [ ] 高通 Hexagon 的 INT2 精度在端侧 LLM 上的真实精度/能效收益如何？厂商口径外的第三方实测在哪？
- [ ] 联发科 BitNet 1.58-bit 相比 INT4 在 NPU 990 上的实测延迟/功耗曲线？是否有可复现 benchmark？
- [ ] Apple ANE 的 op/shape 约束如何系统性映射到模型结构选择（除 Core ML Tools 自动化之外的人工取舍）？
- [ ] 华为达芬奇 NPU 与盘古端侧模型是否真正"联合定义"而非事后适配？证据强弱？
- [ ] NAS-for-NPU 在手机量产项目中的落地率与 ROI？还是主要停留在论文/厂商 demo？
- [ ] CIM（存算一体）NPU 对模型结构（脉动阵列友好 vs 不规则算子）提出哪些新的反向约束？

## 附：来源清单

1. Qualcomm 开发者博客（2025-09）：OmniNeural-4B & NexaML 基于 Hexagon NPU 的多模态创新 — https://www.qualcomm.com/developer/blog/2025/09/omnineural-4b-nexaml-qualcomm-hexagon-npu
2. Qualcomm 开发者博客（2025-08）：Smart routing with Snapdragon X Series NPUs（QNN EP / Phi Silica）— https://www.qualcomm.com/developer/blog/2025/08/smart-routing-snapdragon-x-series-npu-developer-perspective-teknikos
3. MediaTek 新闻室（2025-09）：Dimensity 9500 发布（NPU 990 / BitNet / CIM）— https://www.mediatek.com/press-room/mediatek-dimensity-9500-unleashes-best-in-class-performance-ai-experiences-and-power-efficiency-for-the-next-generation-of-mobile-devices
4. 钛媒体（2025）：联发科天玑 9400+ 与 MDDC 2025 / Dimensity Development Studio — https://www.tmtpost.com/7533804.html
5. Apple Newsroom（2025-10）：Apple 发布 M5 芯片（GPU 内 NLA、ANE、统一内存带宽）— https://www.apple.com.cn/newsroom/2025/10/apple-unleashes-m5-a-big-leap-in-ai/
6. Core ML / ANE 维基（aiwiki.ai）：Core ML 与 Neural Engine op/shape 约束、coremltools 8.x — https://aiwiki.ai/wiki/core_ml
7. 华为昇腾 NPU 百科（达芬奇架构 / CANN / 950 系列精度）— https://baike.baidu.com/item/%E5%8D%8E%E4%B8%BA%E6%98%87%E8%85%BENPU/67703028
8. 老杳吧（2025）：麒麟 9050 Pro 端侧 30B 盘古部署（待核实口径）— https://new.laoyaoba.com/n/1101721

## ⚠️ 待核实清单

- 高通第五代骁龙 8 至尊版 Hexagon NPU「37% 性能提升 / 16% 每瓦性能 / 220 tok/s」等为厂商实验室自报数字，未找到独立第三方复现 → 待核实。
- OmniNeural-4B「世界首个 NPU 感知多模态模型」「NexaQuant 降 10% perplexity / 2× 上下文」为高通+Nexa 联合发布口径 → 待核实。
- 联发科 Dimensity 9500「NPU 990 峰值性能 +111% / 峰值功耗 -56% / BitNet 1.58-bit 降功耗 33%」等为 MediaTek 实验室自报 → 待核实。
- 华为麒麟 9050 Pro「达芬奇 NPU 首次端侧部署 300 亿参数、盘古 30B-A2B 无网运行」来自单一媒体（老杳吧），非华为官方规格书 → 待核实。
- 华为盘古端侧「三级渐进式部署（1B~2B always-on）、KV cache 4-bit 压缩 75%」来自 CSDN 第三方博文 → 待核实。
- Google Gemini Nano「参数上限约 1.8B」「为 TPU 结构定制」来自第三方博客，非 Google 官方明确规格 → 待核实。
- Gemini Nano v3「Pixel 10 Pro 940 tok/s（v2 为 610）」来自 CSDN DevPress 第三方基准，且依赖 Pixel 10 机型真实性 → 待核实。
- Android AICore「跨 App 共享内存降 40%、功耗降 35%」为 Google/媒体口径，缺独立复现 → 待核实。
- Apple M5「GPU 峰值 AI 性能较 M4 提升 4 倍以上、统一内存 153 GB/s」为 Apple 自报（含试生产系统测试） → 待核实。
- 三星 Exynos 端侧 NPU 协同设计具体策略、与 AMD/新路线传闻 → 待核实（本篇暂未展开）。

#标签/手机AI智能体 #标签/端侧推理 #标签/SoC协同设计
