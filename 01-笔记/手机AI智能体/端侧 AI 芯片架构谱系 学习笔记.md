---
title: "端侧 AI 芯片架构谱系"
tags: [ai-chip, nPU, soc, 端侧推理]
created: 2026-09-01
source: "厂商白皮书/技术博客/百科综述（2025-2026 联网核实）"
---

端侧 AI 的算力底座不是通用 GPU，而是为矩阵乘法定制的 **NPU 阵列**；NPU / GPU / ASIC / DSP 在 SoC 内异构编队，端侧推理主力是 NPU，但上限由「算力 × 内存带宽 × 制程能效 × 工具链成熟度」共同决定。

> 编译栈 / toolchain 详见 [[移动端 NPU 与推理编译栈 学习笔记]]；功耗与散热预算详见 [[端侧 AI 功耗与散热约束 学习笔记]]。

---

## 1. 四类处理器定位对比（微架构谱系）

| 处理器 | 本质 / 微架构 | 擅长算子 | 能效特征 | 典型端侧用途 |
|---|---|---|---|---|
| **NPU** | 神经网络专用，**MAC / 脉动阵列 (Systolic Array)**，数据流驱动，本地 SRAM + 权重即时解码 | 矩阵乘 / 卷积 / 激活等密集推理 | 极高（比 GPU 高 40–60×） | 端侧生成式 AI、视觉/语音推理主力 |
| **GPU** | 大规模并行 SIMT，数千精简核心 + 高带宽显存 + Tensor Core | 通用并行、图形渲染、灵活算子、训练 | 高功耗高发热，移动端满载受限 | 图形 + 部分 AI（灵活但不省电） |
| **ASIC** | 固定功能硬化（如 TPU 模块、人脸解锁、ISP AI 子模块） | 特定确定任务 | 能效比极致 | 固定功能加速、感知前端 |
| **DSP** | 数字信号处理，SIMD / 向量扩展 | 音频 / 信号流、降噪、回声消除 | 中低功耗 | 低功耗 AI 协处理 + 声学前端 |

> 补：CPU 是「指挥官」——任务调度、控制流、不规则算子兜底。NPU 根本优势在于把数据搬运压到最低（传统架构 60–80% 能耗在搬运），故能效远高于 CPU/GPU；ARM Ethos-U 即典型 MAC 可配置 NPU（U55: 32–256、U85: 128–2048，U85 已支持 transformer）。

---

## 2. 主流移动 SoC AI 加速器布局（NPU 视角）

> ⚠️ TOPS 口径（NPU-only vs 整 SoC、INT8 vs 其他精度、峰值 vs 实测）各源严重不一致，冲突处统一标「待核实」，不采信单一营销数字。

| 厂商 | 芯片系列 | NPU 名称 | 标称算力 (TOPS) | 年份 | 备注 |
|---|---|---|---|---|---|
| 苹果 | A18 Pro | 16 核 Neural Engine (ANE) | ~35（多源一致） | 2024 | Core ML 自动调度 ANE/GPU/CPU |
| 高通 | Snapdragon 8 Elite / Gen 5 | Hexagon NPU | 80（高通发布口径）／Gen 5 约 55 待核实 | 2024/2025 | 工具链最成熟（QNN / SNPE / QAIRT） |
| 联发科 | Dimensity 9500 | NPU 990（双 NPU + CIM） | 100（MediaTek 官方） | 2025 | BitNet 1.58-bit、128K 上下文、Always-on 小 NPU |
| 三星 | Exynos 2600 | Minerva NPU（32K MAC） | 50–59 待核实（45/50/59/100 多源冲突） | 2025/2026 | 全球首款 2nm GAA；仅韩国版 Galaxy S26 |
| 华为 | 麒麟 9030 / 昇腾 | 达芬奇架构 NPU | 麒麟端侧 ~20–40 待核实；昇腾 950 系为云端 | 2025+ | CANN 2025-08 开源；Kirin X90 双达芬奇 40 TOPS |
| Google | Tensor G4 / G5 | 内置 TPU 集群 | 偏低，G5 较 G4 +约 60% 待核实 | 2024/2025 | Pixel 端侧 Gemini Nano |
| ARM | Ethos-U（IP） | 微控制器级 NPU | 0.256–4（官方可配置） | — | MAC 32–2048，U85 支持 transformer |

---

## 3. 端侧 NPU vs 云端 GPU（为何端侧偏好 NPU）

| 维度 | 端侧 NPU（旗舰 SoC） | 云端 GPU（NVIDIA H100 系） |
|---|---|---|
| 峰值算力 | 35–100 TOPS | 3,958 TOPS INT8 / 989 TFLOPS FP16 |
| 内存 | 共享 LPDDR5X，~100 GB/s | 80GB HBM3，3.35 TB/s |
| 功耗 | 4–10 W | 700–1000 W |
| 定位 | 推理（INT4/INT8 量化） | 训练 + 大规模批推理 |
| 优势 | 低延迟、隐私、零云成本、能效高 40–60× | 高吞吐、大显存、CUDA 生态 |

> 结论：训练与高并发批推理留云端 GPU；端侧 Agent 要的是「小 batch / batch=1、低延迟、省电、数据不出端」→ NPU 是唯一解。

---

## 4. 2025–2026 进展（点到为止）

- **制程**：3nm 旗舰标配，三星 Exynos 2600 试水 **2nm GAA**；摩尔红利收窄，能效转靠架构与封装。
- **存算一体 (CIM)**：联发科天玑 9500 首发集成 CIM 小 NPU（Always-on 轻负载），三星 HBM-PIM、SRAM/ReRAM-CIM 路径推进。
- **Transformer 专用加速**：注意力 / Flash-Attention 硬件单元；Ethos-U85、达芬奇 Cube、联发科 CIM 原生支持 transformer 与低比特（1.58-bit）。
- **端侧 Agent 新需求**：长上下文（128K token 端侧）、always-on AI、动态混合精度、可重构架构（运行时按负载调逻辑）。
- **软件生态**：NNAPI 在 Android 15 弃用，LiteRT + 厂商 delegate 成事实标准（详见 [[移动端 NPU 与推理编译栈 学习笔记]]）。

---

## 5. 代表产品 / 技术（一句话）

- **Hexagon**（高通）：6 矢量 + 8 标量加速器，工具链最成熟。
- **NPU 990 / APU**（联发科）：双 NPU + CIM，BitNet 1.58-bit 先行者。
- **ANE**（苹果）：软硬一体，Core ML 开箱即用调度。
- **达芬奇**（华为）：3D Cube 单元，端边云统一架构，CANN 2025-08 开源。
- **Minerva**（三星）：2nm GAA + 专用 Transformer 加速器。
- **Tensor TPU / Ethos-U**：Google Pixel 端侧 Gemini Nano；ARM 授权 NPU IP。

---

## 待解问题（留给 Ethon 深度补充）

- [ ] 各旗舰 NPU 的「真实可用 TOPS」（非峰值、含内存墙限制）到底多少？行业口径如何统一？
- [ ] 各家 NPU 在稀疏化 / INT4 / 1.58-bit 支持上的差异与量化工具链适配成本？
- [ ] 存算一体 (CIM) 在端侧手机的量产时间表与长期可靠性？
- [ ] 华为达芬奇 NPU 在受限制程下的端侧真实算力与工具链现状（与 [[端侧多模态 VLM 学习笔记]] 的端侧部署强相关）？
- [ ] 端侧 Agent 长上下文（100K+ token）对 NPU 算力与内存带宽的真实需求边界？

---

## 附：来源清单

| 来源 | URL / 说明 |
|---|---|
| Counterpoint Research — MediaTek Dimensity 9500（NPU 990 = 100 TOPS 官方） | https://counterpointresearch.com/en/insights/mediatek-dimensity-9500-powering-powering-next-gen-smartphones |
| 高通骁龙 8 Elite Hexagon 80 TOPS 发布（与非网/新浪） | https://k.sina.cn/article_7857141524_1d452771401902tk8m.html |
| 华为昇腾 / 达芬奇 NPU（含 CANN 2025-08 开源、麒麟达芬奇） | https://baike.baidu.com/item/%E5%8D%8E%E4%B8%BA%E6%98%87%E8%85%BENPU/67703028 |
| DiffStudy 2026 — GPU vs TPU vs NPU 对比（含 H100 数据） | https://diffstudy.com/?p=2278/ |
| 三星 Exynos 2600（2nm GAA，Minerva NPU） | https://www.livemint.com/gadgets-and-appliances/samsung-unveils-exynos-2600-worlds-first-2nm-processor-for-upcoming-flagships-11766146626110.html |
| 虎嗅 — 苹果 ANE 演进（M1→M5 算力） | https://m.huxiu.com/article/4838856.html |

---

## ⚠️ 待核实清单

- **TOPS 口径冲突**：高通 Hexagon 有 80（高通发布）/ 45 / 55（Gen 5 早期）多说；三星 Exynos 2600 NPU 有 45 / 50 / 59 / 100 四说；苹果 M5 有 40 / 50 / 57 / 60 多说。**原因**：各源对「NPU-only vs 整 SoC、INT8 vs 其他精度、峰值 vs 实测」定义不统一，故本笔记不落单点、统一标待核实。
- **华为麒麟端侧算力**：受限制程下真实 TOPS 仅单源估算，缺公开实测，标待核实。
- **CIM 量产时间表**：联发科已落地 Always-on 小 NPU，但主流算力 NPU 的 CIM 量产与可靠性仍待观察。
- **端侧 tok/s 基准**：各「端侧 token 速度」因模型/量化/上下文/测试方法不同不可直接横比，仅作趋势参考。

#标签/AI芯片 #标签/端侧推理 #标签/NPU
