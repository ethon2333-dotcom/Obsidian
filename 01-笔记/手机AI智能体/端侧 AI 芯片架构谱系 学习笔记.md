---
title: "端侧 AI 芯片架构谱系"
tags: [广度种子, 端侧AI, 芯片架构, NPU]
created: 2026-08-19
source: "WebSearch/WebFetch 联网核实 + 公开资料综述"
---

端侧 AI 算力不是「一个 NPU」，而是 **CPU / GPU / NPU / DSP / ASIC 在 SoC 内协同的异构编队**：NPU 是端侧推理主力，但不是唯一、也并不适合所有负载；一颗端侧 AI 芯片的能力上限由「算力(TOPS) × 内存带宽 × 制程能效 × 工具链成熟度」共同决定。

本篇聚焦**芯片微架构本身**（各计算单元是什么、擅长什么、如何异构共存），编译栈/toolchain 详见 [[移动端 NPU 与推理编译栈 学习笔记]]，功耗与散热预算详见 [[端侧 AI 功耗与散热约束 学习笔记]]。

---

## 1. 定义 / 分类：五类计算单元各是什么、擅长什么

| 单元 | 本质 / 微架构 | 擅长负载 | 不适合 / 短板 | 在端侧 SoC 的角色 |
|---|---|---|---|---|
| **CPU** | 通用冯·诺依曼，控制流强 | 任务调度、控制流、不规则算子、小批量低延迟任务、兜底 | 大规模矩阵乘能效极低 | **指挥官**：调度 + fallback |
| **GPU** | 大规模并行 SIMT，数千精简核心，高带宽显存 | 通用并行、图形渲染、灵活算子、训练 / 科学计算 | 高功耗高发热，移动端长期满载受限 | 并行协处理器（图形 + 部分 AI） |
| **NPU** | 神经网络专用，**MAC 阵列 / 脉动阵列 (Systolic Array)**，数据流驱动，近存 / 本地 SRAM + 权重解码 | 矩阵乘 / 卷积 / 激活等密集推理，低功耗低延迟 | 灵活性弱，模型大幅变动未必支持 | **端侧 AI 主力加速器** |
| **DSP** | 数字信号处理，SIMD / 向量扩展 | 音频 / 信号流、降噪、回声消除、轻量 AI 协处理 | 通用 AI 推理能力有限 | 信号前端 + 低功耗 AI 协处理 |
| **ASIC** | 固定功能硬化（如 TPU、人脸解锁模块） | 特定确定任务，能效比极致 | 无灵活性、开发成本极高、模型迭代易淘汰 | 固定功能加速模块 |

> NPU 内部核心概念：**脉动阵列 / MAC 阵列 (Multiply-Accumulate)**——通过阵列化乘加单元 + 本地 SRAM 缓存 + 权重即时解码，把"数据搬运"压到最低，这是 NPU 能效远高于 CPU/GPU 的根本（数据在逻辑单元与存储间搬运能耗占传统架构 60–80%）。ARM Ethos-U 系列即典型：MAC 可配置（U55: 32–256、U85: 128–2048），Ethos-U85 已支持 transformer 网络。

---

## 2. 主流移动 SoC AI 单元横向表

> ⚠️ 各源对 TOPS 口径（NPU-only vs 整 SoC、INT8 vs 其他精度、峰值 vs 实测）严重不一致，凡冲突处统一标「待核实」，不采信单一营销数字。

| 厂商 / SoC | AI 单元 | 定位 | 算力 (TOPS) | 备注 |
|---|---|---|---|---|
| Apple A18 Pro | 16 核 Neural Engine (ANE) | 端侧生成式 AI（Core ML 深度集成） | **~35 TOPS**（多源一致，待核实） | 软硬一体，Core ML 自动选 ANE/GPU/CPU |
| 高通 Snapdragon 8 Elite | Hexagon NPU | 旗舰安卓主算力 | **45 TOPS**（dataintelo / deepresearch）／**另有源称 73 TOPS**（待核实·口径冲突） | 工具链最成熟（QNN / QAIRT / SNPE） |
| 联发科 Dimensity 9500 | APU（NPU 990） | 峰值算力 / Agent 原生优化 | **100 TOPS**（octomil / ima）／**另有源称 40 TOPS**（待核实·口径冲突） | 天玑智能体引擎 2.0；CIM 架构一说 |
| 三星 Exynos 2500 / 2600 | NPU（Mach-1 架构） | 自研旗舰 | 2500 约 **59 TOPS**（待核实）；2600 为 2nm GAA | 3nm GAA 起步，2600 试水 2nm |
| 华为麒麟 / 达芬奇 | 达芬奇架构 NPU | 自研全栈 | **待核实**（受限制程下 SMIC 7nm 级，约 20 TOPS 一说，待核实） | CANN 工具链，生态相对封闭 |
| Google Tensor G4 / G5 | 内置 TPU 集群 | Pixel 端侧 Gemini Nano | G4 偏低（同 G3）／G5 较 G4 **+60%**（待核实） | 公有 TPU SDK 仍处实验性访问 |
| ARM Ethos-U | 微控制器级 NPU（Cortex-M 配套） | 嵌入式 / IoT | **0.256–4 TOPS**（官方可配置区间） | MAC 32–2048，U85 支持 transformer |

---

## 3. 异构计算与任务调度

**为什么需要调度器在 CPU/GPU/NPU/DSP 间分配负载**：不同子任务适配不同单元——
- 视频超分：CPU 解析元数据 → NPU 特征提取 → GPU 后处理渲染（异构比纯 GPU 能效提升约 40%，媒体口径，待核实）。
- 语音交互：DSP 声学前端（回声消除 / 降噪）→ NPU ASR 推理 → CPU 业务逻辑。

**Android 调度栈趋势（已核实）**：
- **NNAPI 已在 Android 15 正式弃用**（Google 官方迁移指南），未来多数设备回退 CPU 后端。
- 推荐迁移路径：**LiteRT（即 TensorFlow Lite Runtime）+ 硬件 delegate**。
- 但 NPU 访问高度碎片化：各厂商自研栈（高通 QNN、联发科 NeuroPilot、三星 ENN、Google Tensor 仍实验性），LiteRT 的 NPU delegate「patchy、厂商锁定」，导致多数 App 实际 fallback 到 CPU/GPU。
- 趋势方向：向 **NPU 原生 delegate** 收敛，但短期内 Android 端侧 AI 调度仍显著落后于 iOS 的"开箱即用"统一栈。

---

## 4. 2025–2026 进展（点到为止）

- **制程**：4nm 已成旗舰标配，3nm（N3P/N3E）普及，三星 Exynos 2600 试水 **2nm GAA**；摩尔红利收窄，能效提升转向架构与封装。
- **存算一体 (CIM) 加速落地**：三星 HBM-PIM、近存计算、SRAM-CIM（后摩智能 160 TOPS/10W 一说待核实）、ReRAM/RRMA 路径，目标消除"存储墙"带来的 90%+ 数据搬运能耗。
- **Transformer 专用加速**：注意力机制加速单元、重构脉动阵列；Ethos-U85、联发科 CIM（BitNet 1.58-bit 三值权重）等原生支持 transformer。
- **端侧 Agent 新需求**：长上下文（128K token 端侧一说，待核实）、always-on AI、动态混合精度、可重构架构（运行时按负载调逻辑）。

---

## 5. 代表产品 / 玩家

- **手机 SoC 主咖**：高通、联发科、苹果、三星、华为、Google。
- **NPU IP 供应商**：ARM Ethos、CEVA-NeuPro（授权 30+ 厂商）、Synopsys / Cadence NPU IP。
- **新兴 CIM / RISC-V**：后摩智能、知存科技、微纳核芯（全球首个 RISC-V 存算一体标准一说）。
- **边缘 / 汽车外溢**：NVIDIA Jetson、地平线、寒武纪等把端侧 NPU 思路推向更高算力域。

---

## 6. 对 OS PM 的意义（Android 系统 PM 视角）

作为安卓系统 PM，理解芯片谱系不是"懂硬件"，而是直接服务于三件事：

1. **端侧 Agent 能力规划**：NPU TOPS、内存带宽（LPDDR5X）、制程共同决定"能跑多大的端侧模型、支持多长上下文"。规划新 Agent 能力前，先对齐目标机型芯片档位（详见 [[端侧大模型推理 学习笔记]]）。
2. **降级策略设计**：当某厂商 NPU 不支持某算子 / 量化格式 → 自动 fallback GPU/CPU（但功耗与延迟上升）。PM 需定义**能力分级矩阵**（满血 NPU / 降级 GPU / 兜底 CPU），而非一刀切。
3. **厂商对齐与碎片化治理**：NNAPI 弃用后，LiteRT + 厂商 delegate 路线成为事实标准，但各厂商 QAT / 算子覆盖差异巨大。PM 应维护「机型—NPU 能力—工具链」特性矩阵，避免"芯片能跑、App 跑不了"的落差（参见 [[Apple Intelligence 端侧架构 学习笔记]] 中苹果统一栈的对照）。
4. **与功耗/散热联动**：NPU 虽高能效，满载仍受 thermal budget 约束，能力规划须与 [[端侧 AI 功耗与散热约束 学习笔记]] 联动。
5. **跨端一致性预期管理**：iOS Core ML 自动选 ANE/GPU/CPU"开箱即用"，Android 碎片化严重 → PM 需为 Android 额外设计厂商适配与体验降级，管理产品承诺。

---

## 待解问题（留给 Ethon 深度补充）

- [ ] 各旗舰 SoC NPU 的「真实可用 TOPS」（非峰值、含带宽/内存墙限制）到底是多少？行业口径如何统一？
- [ ] Android 弃用 NNAPI 后，LiteRT + 厂商 delegate 何时能在主流 App 稳定调度 NPU（而非 fallback CPU）？
- [ ] 存算一体 (CIM) 在端侧手机的量产时间表与长期可靠性如何？
- [ ] 各家 NPU 内 Transformer / Attention 专用加速单元的实现差异与适配成本？
- [ ] 端侧 Agent 长上下文（100K+ token）对 NPU 算力与内存带宽的真实需求边界？
- [ ] 华为达芬奇 NPU 在受限制程下的真实算力与工具链现状（与 [[端侧多模态 VLM 学习笔记]] 的端侧多模态部署强相关）？

---

## 附：来源清单

| 来源 | URL / 说明 |
|---|---|
| ARM Ethos-U 硬件架构（官方） | https://developer.arm.com/documentation/109267/0103/Arm-Ethos-U-NPU/Ethos-U-hardware-architecture |
| Android NNAPI 迁移指南（官方，已弃用声明） | https://developer.android.com/ndk/guides/neuralnetworks/migration-guide |
| Sina 财经：边缘处理器如何组合与演进 | https://finance.sina.com.cn/cj/2025-08-20/doc-infmqrun0594898.shtml |
| AI 芯片技术架构详细对比表 (CSDN) | https://aiot.csdn.net/69bcf4f00a2f6a37c598d91e.html |
| NPU 与 GPU 差异解析 (Baidu Cloud) | https://cloud.baidu.com/article/4614956 |
| Mobile AI Accelerator Market (Dataintelo) | https://dataintelo.com/report/mobile-ai-accelerator-market |
| On-Device AI：Android vs iPhone 碎片化实测 (Beebom) | https://gadgets.beebom.com/stories/i-tested-on-device-ai-on-android-and-iphone-results-not-even-close |
| 2026 边缘 AI 年中趋势报告 (HQWC) | https://www.hqwc.cn/a/814665.html |
| 2026 全球半导体 10 大技术趋势（含存算一体） | https://new.qq.com/rain/a/LNK2025123006739900 |
| On-Device LLM Inference 2025–2026 Guide (Octomil) | https://docs.octomil.com/blog/on-device-llm-inference-2025-2026 |
| WAIC 2026 国产边缘 AI 芯片 (EEFocus) | https://www.eefocus.com/article/2054967.html |

---

## ⚠️ 待核实清单

- **TOPS 数字口径冲突**：骁龙 8 Elite Hexagon 有 45 TOPS（dataintelo/deepresearch）与 73 TOPS（ima）两说；天玑 9500 APU 有 40 TOPS（deepresearch）与 100 TOPS（octomil/ima）两说；Exynos、华为、Google 部分数字仅单源或缺失。**原因**：各源对"NPU-only vs 整 SoC、INT8 vs 其他精度、峰值 vs 实测"定义不统一，故本笔记不采信任何单一数字，统一标待核实。
- **能效比 (TOPS/W) 数字**：各源给 NPU 40–100、ASIC 100–1000 等宽泛区间，且测试方法不同，未能量化到具体机型，故仅给范围不落单点。
- **CIM 芯片具体指标**：后摩智能 160 TOPS/10W、迈特芯 7B 模型 80 tps/5W 等均来自行业稿/会议报道，缺厂商量产实证，标待核实。
- **on-device tok/s 基准**：各"端侧 token 速度"因模型、量化、上下文、测试方法不同不可直接横比，仅作趋势参考。

#标签/端侧AI #标签/芯片架构 #标签/手机AI智能体
