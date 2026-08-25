---
title: 移动端 NPU 硬件与推理编译栈
tags:
  - NPU
  - 端侧推理
  - 编译栈
  - 芯片
  - OS产品经理
  - 广度种子笔记
created: 2026-08-09
source:
  - "Android NDK《NNAPI 迁移指南》官方文档（核实日期 2026-08-09）"
  - "PyTorch Blog《Introducing ExecuTorch 1.0》+ Arm 官方新闻稿（核实日期 2026-08-09）"
  - "Google Developers Blog《MediaTek NPU and LiteRT》《Blazing fast on-device GenAI with LiteRT-LM》（核实日期 2026-08-09）"
  - "Google AI Edge · LiteRT / LiteRT-LM 官方文档与 GitHub（核实日期 2026-08-09）"
  - "Android Developers《Gemini Nano / AICore / ML Kit GenAI APIs》官方文档（核实日期 2026-08-09）"
  - "Apple Developer WWDC25 Session 286/360、WWDC26 Session 324/326/339（核实日期 2026-08-09）"
  - "Qualcomm Developer《QAIRT Overview》、Snapdragon 8 Elite Gen 5 Product Brief、AI Hub Workbench 文档（核实日期 2026-08-09）"
  - "MediaTek 天玑 9500 官方新闻稿、Counterpoint Research 分析（核实日期 2026-08-09）"
  - "Google Blog《5 reasons why Google Tensor G5 is a game-changer》（核实日期 2026-08-09）"
  - "Samsung Exynos 2600 官方产品页与 MLPerf 结果媒体报道（核实日期 2026-08-09）"
---

> 学习定位：这是一篇**广度种子笔记**，目标是把「硬件层 + 编译/运行时栈」的版图一次铺开，画出从 `.pt/.gguf` 到手机 NPU 之间的完整地图。**深度一律留白**——算子融合细节、kernel 优化、各家 SDK 的 API 用法都不展开，统一沉到 `## 待解问题`。定位是「跟芯片团队/算法团队开会时能对上暗号的底图」，不是实施手册。

---

## 一句话心智模型

> **模型跑上 NPU，本质是一次「有损的跨语言翻译」：把一张用 Python 写的、假设算力无限的动态计算图，逐层翻译成一块固定形状硅片能吃下的静态指令序列——每翻一层都会丢一点精度、丢一点灵活性、丢一点可移植性，而各家厂商丢掉的东西恰好不一样，这就是碎片化的全部来源。**

推论有三条，后面所有内容都是它的展开：

1. **翻译是分层的** → 所以有「模型格式 / 转换量化 / 编译器 / 运行时 / 驱动 / 硬件」六层栈。
2. **翻译是有损的** → 所以「同一个模型在不同芯片上体验不一致」是结构性的，不是 bug。
3. **翻译在哪一层做，决定了谁承担成本** → 应用做（App 自带引擎）、系统做（AICore / Foundation Models）、还是芯片厂做（QNN / NeuroPilot），是 OS PM 最核心的架构选择，详见 [[OS-PM-系统AI Runtime vs 应用引擎]]。

---

## 一、分层视角：从 `.pt` 到硅片的六层翻译

这一节是全篇的骨架。建议先记住层数和每层的「代表物」，细节留白。

| 层 | 这一层在干什么 | 代表物 | 谁掌控 |
|---|---|---|---|
| ① 模型格式 | 用某种序列化方式描述计算图 + 权重 | `.pt` / `.onnx` / `.tflite` / `.gguf` / `.mlpackage` / `.aimodel` / `.litertlm` | 框架社区 |
| ② 转换 & 量化 | 图重写、算子映射、精度降级、权重打包 | AI Edge Torch、Core AI Python / coremltools、AI Edge Quantizer、QNN converter | 框架 + 芯片厂共同 |
| ③ 编译器 / 委托(delegate) | 把子图切给加速器、做算子融合与内存规划、产出硬件专属二进制 | QNN、NeuroPilot、Arm Vela、XNNPACK/KleidiAI、TOSA、`coreai-build` | **芯片厂**（主战场） |
| ④ 运行时 (runtime) | 加载、调度、分配 buffer、异构回退、会话管理 | LiteRT / LiteRT-LM、ExecuTorch runtime、QAIRT、Core AI、ONNX Runtime | 框架厂 + 芯片厂拉锯 |
| ⑤ 驱动 / HAL | 内核态提交任务、电源与时钟、内存映射 | 各家闭源 NPU 驱动 | 芯片厂（**几乎全闭源**） |
| ⑥ 硬件 | 矩阵/向量/标量单元 + 片上 SRAM + 访存通道 | Hexagon、APU、ANE、TPU、Exynos NPU | 芯片厂 |

### 两个必须记住的分叉

**分叉 A：AOT 编译 vs On-device 编译**（③ 层在什么时候发生）

| | 提前编译 AOT（离线） | 设备端编译（在线） |
|---|---|---|
| 编译时机 | 开发/构建阶段，针对具体 SoC | 用户设备上首次运行时 |
| 首次启动 | 快 | 慢（Google 举例：Gemma 3 270M 在设备端编译可**超过一分钟**） |
| 分发复杂度 | 高，需按 SoC 组合分包 | 低，一包通吃 |
| 适用 | 大模型、目标机型确定 | 小模型、要覆盖长尾机型 |

> Google 的解法是 **Play for On-device AI (PODAI)**：把模型 + runtime 打成 "AI Pack"，由 Play 按用户设备下发匹配版本。Apple 侧对应的是 Core AI 的 `xcrun coreai-build compile` + Background Assets 按需下载。**这是"碎片化不可消除，只能挪到分发层"的典型工程妥协。**

**分叉 B：Prefill vs Decode**（⑥ 层瓶颈完全不同）

- **Prefill（吃 prompt）** → 计算密集，吃 TOPS，NPU 优势大。
- **Decode（吐 token）** → **访存密集**，吃内存带宽，TOPS 基本用不上。

Google 在 LiteRT-LM 官方博客中直接写道："Standard LLM inference is fundamentally memory-bandwidth bound"（标准 LLM 推理本质上是内存带宽受限的）。这条是后面「TOPS 口径陷阱」和「对 OS PM 的意义」两节的地基，也是 [[OS-PM-3B模型内存预算推演]] 的物理依据。

---

## 二、硬件侧版图

### 2.1 各家 NPU 对比（广度铺开，数字口径见下方警告）

| 厂商 / 平台 | NPU 名称 | 代表型号（截至 2026-08） | 官方口径的关键说法 | 数字性质 |
|---|---|---|---|---|
| 高通 Qualcomm | Hexagon NPU（Qualcomm AI Engine 的一部分） | Snapdragon 8 Elite Gen 5（SM8850，2025-09 发布，TSMC 3nm） | 12 标量 + 8 向量 + 1 加速器；支持 INT2/INT4/INT8/INT16/FP8/FP16 混合精度；NPU 性能 +37%、能效 +16%（对比上代） | **厂商口径 · 相对提升 · 官方 Product Brief 未标 TOPS 绝对值** |
| 联发科 MediaTek | APU / NPU 990 + 超能效 NPU（双 NPU） | 天玑 9500（2025-09 发布，3nm） | NPU 990 峰值性能 +111%、峰值功耗 -56%（对比天玑 9400）；生成式 AI 引擎 2.0；率先支持 BitNet 1.58-bit；超能效 NPU 采用**存算一体 (CIM)** 架构做 always-on | 厂商口径 · 相对提升。Counterpoint 称其为「首款 100 TOPS 手机 SoC」——**该 TOPS 为第三方引述，精度口径（INT8? INT4? 双 NPU 合计?）未标明，待核实** |
| Apple | Neural Engine (ANE) + GPU 神经加速器 | A / M 系列 | 官方长期以「Apple Intelligence 端侧模型约 3B 参数」「Core AI 跨 CPU/GPU/ANE 推理」等能力口径宣传 | **Apple 近年在开发者文档中极少给 ANE 的 TOPS，本笔记不填数字** |
| Google | TPU（Tensor 内的 Edge TPU 血统） | Tensor G5（Pixel 10，2025 年，TSMC 3nm） | TPU 算力最高 +60%、CPU 平均 +34%；首款完整运行最新一代 Gemini Nano 的芯片；Gemini Nano 在 Pixel Screenshots / Recorder 场景 2.6× 更快、2× 更省电 | 厂商口径 · 相对提升 · **场景限定**（不是通用推理提速） |
| 三星 Samsung | Exynos NPU | Exynos 2600（2nm GAA，Galaxy S26 / S26+） | NPU 生成式 AI 性能 +113%（三星内部测试）；MLPerf MobileBERT 1199.57 QPS（+2.1×）、Stable Diffusion 0.53 QPS（+2.4×） | MLPerf 属**行业标准基准**（可比性较好）；+113% 为**厂商内部口径**，且不同报道对「前代」是 2400 还是 2500 说法不一，**待核实** |
| 海思 / 紫光展锐 / 玄戒等 | 达芬奇 NPU 等 | — | — | **本次未核实到可靠公开一手资料，留空不臆测** |

### 2.2 TOPS 的口径陷阱（重点）

TOPS 是 OS PM 最容易被带偏的数字。至少有六重口径差异：

| 陷阱 | 说明 | 后果 |
|---|---|---|
| **精度口径** | INT8 TOPS vs INT4 TOPS 通常差 2×，INT2 更夸张 | 同一颗芯片可以合法报出差 4 倍的数字 |
| **峰值 vs 可持续** | 峰值 = 理论 MAC 数 × 频率，忽略散热墙 | 手机是被动散热的玻璃三明治，长任务必降频 |
| **单元口径** | 只算 NPU？还是 CPU+GPU+NPU 合计（"platform TOPS"）？双 NPU 是否合计？ | 天玑 9500 双 NPU 就是典型歧义点 |
| **稀疏 vs 稠密** | 部分口径按 2:4 结构化稀疏计 | 实测模型往往吃不到 |
| **算力 ≠ 吞吐** | Decode 阶段带宽受限，TOPS 富余也跑不动 | **本笔记最想让你记住的一条** |
| **厂商自报 vs 第三方实测** | 前者是设计指标，后者是端到端体验 | 必须分开列，不可混表 |

> **诚实纪律**：本笔记中任何 TOPS / 加速倍数，一律标注来源与性质。凡是厂商发布会 PPT 上的数字，默认视为「峰值 + 有利精度 + 有利场景」，在内部评审中应要求芯片团队补齐口径三件套：**精度、持续时长、测试模型**。

### 2.3 一个具体的「带宽压倒算力」算例（第三方推演，非实测）

有券商研报以骁龙 8 Gen 3 为例做过一次粗算：NPU 约 45 TOPS、内存带宽约 67 GB/s，跑 7B 模型时——算力侧理论上限约 3200 tokens/s，带宽侧理论上限约 4.8 tokens/s，取小者即带宽。

> ⚠️ 这是**第三方研报的简化模型**（未计 KV Cache、未计量化后权重体积、未计实际带宽利用率），**不可作为选型依据**，但作为「数量级直觉」极其有用：**算力和带宽之间可能差两到三个数量级**。这也是为什么 3D DRAM / 近存计算 / 存算一体（天玑 9500 的超能效 NPU 已经走了这条路）会成为 2025-2026 的产业主线。展开见 [[端侧 AI 基建与算力预算]]。

---

## 三、软件侧版图：编译 / 运行时栈

### 3.1 芯片厂自有栈（垂直、最快、最锁定）

| 厂商 | 栈名 | 层次结构 | 关键特征 |
|---|---|---|---|
| 高通 | **QAIRT**（Qualcomm AI Runtime，伞形品牌） | 下有三条路：**SNPE**（简单 API、多处理器）、**QNN / AI Engine Direct**（细粒度控制、按处理器编译）、**GENIE**（在 QNN 之上专做 GenAI/LLM） | 产物是 DLC 或 context binary；官方承诺 DLC 向新版本 SDK 前向兼容；另提供 TFLite Delegate |
| 高通 | **Qualcomm AI Hub / AI Hub Workbench** | 云端托管的编译 + 真机 profiling 服务 | 可提交 `.pt` 直接编译成 QNN DLC / context binary，并在指定真机（如 Galaxy S24 Family）上跑性能分析。**降低了"没有真机就调不动"的门槛** |
| 联发科 | **NeuroPilot** | 编译器 + 运行时 | 2025-12 与 Google 联合推出 **LiteRT NeuroPilot Accelerator**，作为旧 TFLite NeuroPilot delegate 的**从零重写的继任者**，支持 AOT / on-device 双编译路径 |
| Apple | **Core ML** → **Core AI**（WWDC26 新框架） | Core AI = 驱动端侧 Apple Intelligence 的推理框架，现开放给开发者 | Python/PyTorch 侧做转换与优化，Swift 侧做推理；新 `.aimodel` 格式；`xcrun coreai-build compile` 做 AOT；Xcode/Instruments 深度集成；官方 Core AI models repository 提供 Qwen / Mistral / SAM3 等现成 recipe |
| Google | Tensor 的 TPU 栈 | 未完全公开，主要通过 AICore / LiteRT 暴露 | Gemini Nano 与 Tensor G5 是协同设计的（Matryoshka Transformer 等架构选择） |
| 三星 | Exynos NPU SDK | — | 2025 年起以 **ExecuTorch backend** 形式对外（见下） |

### 3.2 跨平台 / 框架侧栈

| 方案 | 出品方 | 定位 | 2025-2026 状态（已核实部分） |
|---|---|---|---|
| **LiteRT**（原 TensorFlow Lite 改名） | Google AI Edge | Android 上事实标准的通用推理运行时 | LiteRT **v2 / "Next"** 于 Google I/O '25 发布，自动加速器选择、异步执行、TensorBuffer 零拷贝；**NPU 加速通过 Early Access Program (EAP) 开放**，覆盖 Qualcomm / MediaTek；GitHub 上 v2 标注为 **Alpha** |
| **LiteRT-LM** | Google AI Edge | LiteRT 之上的 **LLM 编排层**（会话、KV cache、多模态、tool use） | 已在 Chrome / ChromeOS / Pixel Watch 等 Google 产品中生产使用；跨 Android/iOS/Web/Desktop/IoT；支持 Gemma、Llama、Phi-4、Qwen；支持 **MTP（Multi-Token Prediction）投机解码**，官方称最高 2.2× 提速（详见 [[OS-PM-投机采样原理与能效优化]]） |
| **AI Edge Torch** | Google AI Edge | PyTorch → `.tflite` 的转换器 | 经典模型走 AI Edge Torch Converter + AI Edge Quantizer；LLM 走 Torch Generative API → LiteRT-LM |
| **MediaPipe** | Google | 任务级封装（视觉/音频 pipeline） | 仍在，但 GenAI 主线已明显迁移到 LiteRT-LM / ML Kit GenAI |
| **ExecuTorch** | Meta / PyTorch | PyTorch 原生端侧运行时，**不需要转格式** | **1.0 正式版已发布**（Beta 为 2024-10，1.0 由 PyTorch 官方博客与 Arm 新闻稿共同确认）。1.0 新增后端：Arm VGF、NXP eIQ Neutron NPU、**Samsung Exynos NPU/GPU**、Intel OpenVINO；已有 alpha/beta 后端含 Cadence DSP、**MediaTek NPU**、Apple MPS；部分后端从 beta 升为 production-ready |
| **ONNX Runtime Mobile** | Microsoft | 中立 IR + 多 EP（execution provider） | 高通侧可走 QNN EP。**本次未核实到 2026 年最新版本状态，待核实** |
| **llama.cpp / GGUF** | 社区 | CPU 优先、量化生态最活跃 | 社区事实标准之一。**NPU 支持仍是弱项，待核实** |
| **MNN**（阿里）/ **ncnn**（腾讯）/ **MLC-LLM** | 社区/大厂开源 | 中国厂商端侧落地大量在用 | 前述券商算例即引用「小米实测 Qwen3-8B-MNN」。**具体版本与 NPU 后端成熟度待核实** |
| **MLX** | Apple | Apple Silicon 原生数组/训练框架 | WWDC26 增加 Metal 4 与 GPU 神经加速器支持，并支持通过 Thunderbolt RDMA 跨多台 Mac 扩展训练。**偏研究/桌面，不是 iPhone 量产推理主路径** |

### 3.3 NNAPI 的弃用：这是 Android 端侧 AI 的分水岭

**已核实事实**（来源：Android NDK 官方《NNAPI 迁移指南》）：

- NNAPI 于 **Android 8.1 (API 27)** 引入，目标是「为端侧 ML 提供硬件加速推理的统一接口」。
- **NNAPI 已于 Android 15 弃用（deprecated）。**
- Google 给出的官方理由：ODML 领域演进太快（Transformer、扩散模型），开发者需要**可频繁更新**的工具和基础设施，而 NNAPI 作为 NDK 中随 OS 版本走的 API 做不到。
- **官方推荐迁移路径**：迁移到 **Google Play 服务中的 TensorFlow Lite（即 LiteRT）**，硬件加速可选用 **TFLite GPU delegate**；GenAI 基础模型走 **AICore**。

**为什么这对 OS PM 是大事：**

Google 用一个"随 OS 版本走的 NDK C API"换成了两个"可独立更新的模块"——**Play 服务里的 LiteRT** + **系统服务 AICore**。这本质上是承认：

> **统一硬件抽象层（HAL 式的 NNAPI）在 AI 时代失败了。** 因为算子集演进速度远快于 OS 发版速度，任何冻结在 OS 版本里的算子抽象，出厂即过时。

替代方案不是"更好的统一抽象"，而是**把抽象上移到可更新层**（Play 服务 / 系统服务）+ **把差异化下沉回芯片厂 SDK**（QNN / NeuroPilot），再由 LiteRT 用 EAP 的方式一家一家去对接。这正是 [[OS-PM-系统AI Runtime vs 应用引擎]] 讨论的边界问题的现实答案。

> ⚠️ **待核实**：NNAPI 在 Android 16 / 17 中是否已从 NDK 中**移除**（removed）而非仅仅弃用；旧 App 的运行时兼容策略。官方迁移指南只明确写到「在 Android 15 中废弃」。

---

## 四、系统级 API 趋势：从「给你算力」到「给你模型」

这是 2025-2026 最大的范式转变：**平台方不再只提供加速接口，而是直接把端侧基础模型作为系统能力开放给第三方 App。**

| 维度 | Android 阵营 | Apple 阵营 |
|---|---|---|
| 系统模型 | **Gemini Nano** | Apple 端侧 Foundation Model（官方口径「约 3B 参数级」） |
| 承载服务 | **AICore**（Android 系统服务） | 系统内置，通过 Foundation Models framework 暴露 |
| 第三方 App 入口 | **ML Kit GenAI APIs**（高层封装：Prompt / Summarization / Proofreading / Rewriting / Image Description / Speech Recognition） | **Foundation Models framework**（WWDC25，iOS 26 起） |
| 质量一致性手段 | 每个 API 配专属 **LoRA adapter** + 调优过的推理参数 + 评测 pipeline | 内置专用 adapter（如内容标签 adapter）；官方建议开发者自建 "eval set" 黄金样本集 |
| 隐私架构 | 遵循 **Private Compute Core** 原则：包绑定受限、**无直接联网**（所有网络请求经开源的 Private Compute Services APK 中转）、请求间隔离、不留存输入输出 | 端侧执行 + **Private Cloud Compute (PCC)** 作为算力升档选项 |
| 模型分发 | AICore 统一管理下载与更新，**多 App 共享同一份权重** | 随 OS 更新同步，官方明确「模型与 OS 更新同步演进」 |
| 硬件门槛 | 需设备具备 AICore 与兼容 Nano 版本；已知支持含 Pixel 9/10 系列、Galaxy S25、小米 15 等；**Google 未公开完整支持清单** | 支持 Apple Intelligence 的机型与地区 |
| 上下文窗口 | Tensor G5 上 Gemini Nano 被报道为 32K token（**第三方整理口径，待核实**） | WWDC25 Group Lab 明确：**4,096 tokens**，输入输出共享 |

### Apple 在 WWDC26 的两个关键动作（已核实）

1. **Core AI 框架**：Apple 把「驱动端侧 Apple Intelligence 的那套推理框架」开放给开发者。覆盖模型部署全生命周期（Python 转换/优化 → Swift 推理 → Xcode/Instruments 调试），跨 CPU/GPU/Neural Engine，支持 AOT 编译与「模型特化（specialization）」缓存以降低首次加载延迟。
2. **Foundation Models framework 开放给第三方 LLM 提供方**：引入公共的 `LanguageModel` 协议，System Model / PCC / Core AI / MLX / 社区模型统一同一套调用方式；Anthropic (Claude) 与 Google (Gemini) 将各自提供 Swift 包接入。

> **PM 视角的解读**：Apple 在做的是"**把模型层也变成 OS 的一等公民 API**"——`LanguageModel` 协议之于 LLM，约等于当年 `AVFoundation` 之于媒体。这比 Android 侧 ML Kit GenAI 的"任务级封装"抽象层级更高、更通用。两条路线的赌注不同：Google 赌**任务封装能保证跨机型质量一致**，Apple 赌**统一协议 + 自家硅片能保证性能一致**。参考 [[Apple Intelligence 端侧架构 学习笔记]]。

---

## 五、2025-2026 的三条进展主线

### 主线 1：碎片化被承认，抽象层上移

- NNAPI 弃用是官方承认「OS 层统一硬件抽象」失败。
- 新方案是**可更新的中间层**：LiteRT（Play 服务）+ AICore（系统服务）+ PODAI（分发层适配）。
- Google 与联发科的原话：NPU 空间「有数百种 SoC 变体」，现有端侧 ML 基础设施「主要为 CPU/GPU 设计，缺乏与专用 NPU SDK 及其独特编译需求的深度集成」。
- Arm 侧的解法是 **TOSA**（Tensor Operator Set Architecture）：把模型转成硬件无关的标准化描述，再落到 Arm GPU / Ethos-U NPU。这是「用标准算子集对抗碎片化」的另一条思路。
- **但注意**：LiteRT 的 NPU 加速目前仍以 **EAP（早期访问计划）** 形式提供，v2 API 在 GitHub 上标注 Alpha。**统一抽象层还在半路上，不是已完成时。**

### 主线 2：瓶颈从算力转向带宽与内存

- Google 官方博客直陈 LLM 推理"fundamentally memory-bandwidth bound"。
- 学界/工业界 2025 年的多份研究（NVIDIA Research、IBM "Mind the Memory Gap" 等）指向同一结论：**prefill 计算受限、decode 访存受限**。
- 产业应对：**存算一体 / 近存计算**（天玑 9500 超能效 NPU）、**3D DRAM 堆叠**（多家在推，量产时间表待核实）、**更激进的量化**（天玑 9500 支持 BitNet 1.58-bit；高通支持 INT2）、**投机解码**（LiteRT-LM 的 MTP）。
- 对应库内深度笔记：[[端侧模型量化 学习笔记]]、[[OS-PM-PagedAttention与KV Cache剪枝]]、[[OS-PM-3B模型内存预算推演]]。

### 主线 3：端侧模型「服务化」，App 不再自带引擎

- Android：AICore 统一持有权重，多 App 共享，App 只调 ML Kit GenAI 高层 API。
- Apple：Foundation Models framework，三行代码调用系统模型，且 Apple 明确说明「对开发者和用户**不产生任何请求费用**」。
- **结果**：App 侧的 APK/IPA 体积压力、模型更新压力、硬件适配压力，**大部分被 OS 接走了**。这既是 OS 厂商的机会（掌控入口），也是责任（体验一致性变成 OS 的 KPI）。

---

## 六、对 OS PM 的意义

### 6.1 碎片化如何影响系统级 AI 功能排期

| 碎片化来源 | 具体表现 | 对排期的影响 |
|---|---|---|
| **编译栈按 SoC 分叉** | 同一模型要为 N 个 SoC 各编一次（AOT），或牺牲首启体验（on-device） | 每增加一个在售平台，就多一条**独立的模型交付流水线**；测试矩阵是乘法不是加法 |
| **SDK 版本与 OS 版本解耦** | QNN SDK / NeuroPilot 版本节奏 ≠ 你的 OS 发版节奏 | 芯片厂 SDK 的 bug 修复窗口可能对不上你的封版节点，**需要提前锁版本** |
| **驱动闭源** | ⑤ 层出问题只能提单给芯片厂 | 缺陷定位周期不可控，必须在排期里留**外部依赖 buffer** |
| **算子覆盖不一致** | 某算子在 A 家 NPU 上被支持、B 家 fallback 到 CPU | 同一功能在不同机型上可能是「NPU 秒回」和「CPU 卡三秒」的天壤之别 |
| **模型分发绑定商店/服务** | PODAI 依赖 Google Play；国内无 GMS | **国内 ROM 必须自建 AI Pack 分发通道**，这是一个独立的基建项目，见 [[端侧 AI 基建与算力预算]] |
| **系统模型的机型门槛** | Gemini Nano 只在部分机型可用，且清单不公开 | 功能可用性成为**机型分层**问题，营销口径必须与技术口径对齐 |

### 6.2 为什么「同一个模型在不同芯片上体验不一致」

按六层栈逐层归因，这不是玄学：

1. **② 量化不同** → 各家推荐的量化方案/校准集不同，输出分布就不同（同一 prompt 可能一家答对一家答错）。
2. **③ 图切分不同** → 编译器把哪些子图给 NPU、哪些回落 CPU，各家策略不同，**未支持的算子一旦落在中间就产生多次跨 IP 数据搬运**，延迟塌方。
3. **③ 融合策略不同** → 融合得多则中间张量不出片上 SRAM，融合得少则反复读写 DRAM。
4. **⑤ 驱动调度不同** → 与 ISP、Modem 共享热区时的降频策略、优先级仲裁各不相同。
5. **⑥ 带宽不同** → decode 速度几乎线性绑定有效内存带宽，而带宽由 LPDDR 代次 + 通道数 + 封装决定，**跟 NPU TOPS 没有直接关系**。
6. **热预算不同** → 同一 SoC 装在不同厚度/散热方案的整机里，持续性能可以差一大截。**这一层完全在整机厂手里，也是 OS PM 唯一能自己使劲的地方。**

> 直接推论：**验收指标必须是「持续场景下的端到端体验」，不能是单次跑分。** 建议对齐 [[OS-PM-性能与稳定性指标体系]]，并把降级策略显式产品化（[[OS-PM-AI Runtime动态调度与降级策略]]）。

### 6.3 选型时该问芯片团队的问题清单

拿去开会用。分四组：

**A 组 · 拆穿 TOPS**
1. 这个 TOPS 的**精度口径**是什么？INT8 / INT4 / INT2？稀疏还是稠密？
2. 是**纯 NPU** 还是 CPU+GPU+NPU 合计？双 NPU 是否合并计数？
3. **持续 5 分钟**满负载后还剩多少？降频曲线能不能给？
4. 有没有 **MLPerf Mobile** 或其他第三方标准基准的成绩？（比自报数字可信）

**B 组 · 带宽与内存（往往比 A 组更决定体验）**
5. LPDDR 代次、通道数、**理论峰值带宽**是多少？NPU 实际可用带宽占比是多少？
6. 跑一个 3B / 4-bit 模型，**decode 速度**实测多少 token/s？prefill 多少？（要求给测试模型和上下文长度）
7. 片上 SRAM 多大？KV Cache 放哪里？长上下文时的带宽退化曲线？
8. 有没有存算一体 / 近存计算单元？覆盖哪些算子？

**C 组 · 软件栈与交付**
9. 支持哪些前端框架？LiteRT 的 NPU 加速是 **GA 还是 EAP**？ExecuTorch backend 是什么状态（alpha / beta / production-ready）？
10. 算子覆盖清单在哪？**不支持的算子的 fallback 行为**是什么（回 CPU？报错？）？
11. 编译产物的**前向兼容性**承诺是什么？（高通对 DLC 有明确承诺，其他家呢？）
12. SDK 发版节奏？我们封版前最后一个可用版本是哪个？
13. 有没有**云端编译 + 真机 profiling** 服务（类似 Qualcomm AI Hub）？没有的话真机测试成本谁承担？

**D 组 · 系统集成与并发**
14. NPU 与 ISP / Modem 是否共享热区、共享带宽？相机场景与 AI 场景**并发**时怎么仲裁？
15. NPU 支持**多任务并发 / 抢占**吗？系统级常驻模型（意图识别、唤醒）与前台 App 模型如何共存？参考 [[端侧意图框架 学习笔记]]。
16. 模型加密 / 安全执行环境支持到什么程度？（8 Elite Gen 5 提到 GenAI 模型加密）
17. 权重能否多进程共享？还是每个 App 各占一份内存？

---

## 七、代表产品速查

| 场景 | Android 主路径 | iOS 主路径 | 跨平台/社区路径 |
|---|---|---|---|
| 传统 CV / 音频小模型 | LiteRT（+ GPU delegate / NPU EAP） | Core ML → Core AI | ExecuTorch、ONNX Runtime、ncnn / MNN |
| 端侧 LLM（自带模型） | LiteRT-LM（+ PODAI 分发） | Core AI + `CoreAILanguageModel` | ExecuTorch、llama.cpp、MLC-LLM、MNN |
| 端侧 LLM（用系统模型） | ML Kit GenAI APIs → AICore → Gemini Nano | Foundation Models framework | — |
| 榨干特定芯片 | QNN / GENIE（高通）、NeuroPilot（联发科） | MLX（桌面/研究）、Metal | — |
| 云端兜底 | Firebase AI Logic SDK → Gemini Pro/Flash | Private Cloud Compute / 第三方 Swift 包 | 各家 API |

---

## 八、库内关联

- [[端侧模型量化 学习笔记]] —— 本笔记第 ② 层「转换 & 量化」的深度展开；INT4/INT2/BitNet 的精度-带宽权衡在那里算细账。
- [[端侧大模型推理 学习笔记]] —— prefill/decode 二分、吞吐与延迟指标的深度版。
- [[端侧 AI 基建与算力预算]] —— 带宽瓶颈、3D DRAM、以及「国内无 GMS 时 AI Pack 自建分发」的基建视角。
- [[OS-PM-端侧大模型系统级挑战]] —— 本笔记第六节的问题在系统架构层面的完整版。
- [[OS-PM-系统AI Runtime vs 应用引擎]] —— 「抽象层放在哪一层」这个核心决策的专题；NNAPI 弃用是它最好的现实案例。
- [[OS-PM-AI Runtime动态调度与降级策略]] —— NPU→GPU→CPU 回退、热降级分级的产品化设计。
- [[OS-PM-3B模型内存预算推演]] —— 带宽算例的严谨版本。
- [[OS-PM-投机采样原理与能效优化]] —— LiteRT-LM 的 MTP 属于这一类技术。
- [[OS-PM-PagedAttention与KV Cache剪枝]] —— 长上下文时 KV Cache 成为新带宽瓶颈的应对。
- [[OS-PM-性能与稳定性指标体系]] —— 「不能只看跑分」的指标定义方法论。
- [[Apple Intelligence 端侧架构 学习笔记]] —— Apple 侧 Core AI / Foundation Models / PCC 的深度版。
- [[AI模型类型与架构]] —— 模型侧的分类底图。
- [[端侧意图框架 学习笔记]] —— always-on 小模型与存算一体 NPU 的结合点。
- [[手机AI智能体知识库]] —— Agentic AI 落地的整体视角。
- [[OS产品经理知识库 MOC]] —— 总入口。

---

## 待解问题

- [ ] **NNAPI 的最终归宿**：Android 16 / 17 的 NDK 中 NNAPI 是仅「弃用」还是已「移除」？既有依赖 NNAPI 的三方 App 在新版本上的运行时行为是什么？（官方迁移指南只写到「Android 15 中废弃」）
- [ ] **LiteRT NPU 加速何时 GA**：EAP 到正式发布的时间线？GA 后是否覆盖 Google Tensor 与三星 S.LSI（GitHub 上这两项标注为 coming soon）？LiteRT v2 从 Alpha 到 Stable 的路径？
- [ ] **算子覆盖差异的量化方法**：有没有可复用的「跨芯片算子支持矩阵」工具或社区维护清单？如何在选型阶段快速摸清某个目标模型在 A/B 两家芯片上的 fallback 率？
- [ ] **持续性能的标准化测量**：MLPerf Mobile 之外，是否存在被行业接受的「持续 N 分钟 AI 负载」基准？热降级曲线应该怎么定义和验收？
- [ ] **Core AI 与 Core ML 的关系**：Core AI 是取代 Core ML 还是并存？既有 `.mlpackage` 资产的迁移成本？`.aimodel` 与 Core ML 格式的关系？
- [ ] **算子融合与内存规划的具体机制**（本笔记刻意留白的深度）：编译器如何决定子图边界？片上 SRAM 的 tiling 策略（如高通的 Micro Tile Inferencing）具体怎么工作？
- [ ] **存算一体 NPU 的真实边界**：天玑 9500 的 CIM NPU 能跑哪些算子、多大模型？能效优势在什么工作负载下才成立？3D DRAM 堆叠方案的量产时间表与成本影响？
- [ ] **国内生态的替代路径**：没有 GMS 的情况下，AI Pack 式的「按 SoC 分发模型」如何自建？各家 ROM 厂商（含海思 / 展锐 / 玄戒平台）的公开栈现状？

---

## 附：来源清单

| 事实 | 来源 | 性质 |
|---|---|---|
| NNAPI 在 Android 15 中弃用；官方迁移到 Play 服务中的 TFLite/LiteRT + TFLite GPU delegate；GenAI 走 AICore | Android NDK《NNAPI 迁移指南》 developer.android.com | **官方一手文档** |
| ExecuTorch 1.0 正式发布；新增 Arm VGF / NXP eIQ Neutron / Samsung Exynos NPU+GPU / Intel OpenVINO 后端；MediaTek NPU、Cadence DSP、Apple MPS 为已有 alpha/beta；Beta 版为 2024-10 | PyTorch Blog《Introducing ExecuTorch 1.0》 | **官方一手** |
| ExecuTorch 1.0 GA 与 Arm KleidiAI / TOSA / CMSIS-NN / Vela 集成 | Arm 官方新闻稿（2025-11） | 厂商官方（合作方视角） |
| LiteRT NeuroPilot Accelerator 发布；NPU 碎片化「数百种 SoC 变体」表述；AOT vs on-device 编译；PODAI / AI Pack 分发；Gemma 3 270M 设备端编译超过一分钟 | Google Developers Blog《MediaTek NPU and LiteRT》 | **官方一手** |
| LiteRT v2 为 I/O '25 发布、状态 Alpha；NPU 加速为 EAP；各平台 NPU 支持矩阵 | LiteRT GitHub README | 官方一手（仓库） |
| LiteRT-LM 定位、跨平台、支持模型、MTP 最高 2.2× 提速、"LLM 推理本质上内存带宽受限"、在 Chrome/ChromeOS/Pixel Watch 生产使用 | Google AI Edge LiteRT-LM 官方文档 + Developers Blog | **官方一手** |
| AICore 架构、Private Compute Core 原则（受限包绑定 / 无直连网络 / 不留存输入输出）、ML Kit GenAI 六项能力、LoRA adapter 方案 | Android Developers《Gemini Nano》《AICore》官方文档 | **官方一手** |
| ML Kit GenAI 支持机型举例（Pixel 9、Galaxy S25、小米 15 等）、Google 未公开完整清单 | InfoQ（2025-06）、iThome 报道 | 第三方媒体 |
| Foundation Models framework（iOS 26）、上下文窗口 4096 tokens、模型随 OS 更新、建议自建 eval set | Apple Developer WWDC25 Session 286/360 + WWDC25 Group Lab 论坛纪要 | **官方一手** |
| Core AI 框架（WWDC26）：驱动端侧 Apple Intelligence、跨 CPU/GPU/ANE、`.aimodel`、`xcrun coreai-build compile`、模型特化、Core AI models repository | Apple Developer WWDC26 Session 324/326 | **官方一手** |
| Foundation Models 开放第三方 LLM 提供方、`LanguageModel` 协议、Anthropic/Google 将提供 Swift 包、MLX 的 Metal 4 与 RDMA 支持 | Apple Developer WWDC26 Session 339 + Apple ML 新功能页 | **官方一手** |
| QAIRT 伞形结构（SNPE / QNN / GENIE）、DLC 前向兼容承诺、TFLite Delegate | Qualcomm Developer《QAIRT Overview》 | **官方一手** |
| AI Hub Workbench 可将 `.pt` 编译为 QNN DLC / context binary 并在指定真机 profiling | Qualcomm AI Hub Workbench 文档 | **官方一手** |
| Snapdragon 8 Elite Gen 5 规格：12 标量+8 向量+1 加速器、INT2~FP16 混合精度、Micro Tile Inferencing、GenAI 模型加密 | Qualcomm 官方 Product Brief PDF | **官方一手（厂商口径）** |
| 8 Elite Gen 5 的 NPU +37% 性能 / +16% 能效、2025-09 发布、TSMC 3nm | Qualcomm 发布信息 + 多家科技媒体转述 | 厂商口径 + 媒体转述 |
| 天玑 9500：NPU 990 峰值 +111%、峰值功耗 -56%、生成式 AI 引擎 2.0、BitNet 1.58-bit、超能效 NPU 存算一体 | MediaTek 官方新闻稿 | **官方一手（厂商口径，相对值）** |
| 天玑 9500「首款 100 TOPS 手机 SoC」 | Counterpoint Research 分析文章 | **第三方分析引述厂商数据，精度口径未标明** |
| Tensor G5：TPU 最高 +60%、CPU 平均 +34%、TSMC 3nm、首款完整跑最新 Gemini Nano、特定场景 2.6× 更快 / 2× 更省电 | Google Blog《5 reasons why Tensor G5...》 | **官方一手（厂商口径，场景限定）** |
| Gemini Nano 在 G5 上 32K token 上下文 | 第三方整理（Jon Peddie Research 引述 / 媒体） | **第三方转述，待核实** |
| Exynos 2600：2nm GAA、NPU 生成式 AI +113%、MLPerf MobileBERT 1199.57 QPS / Stable Diffusion 0.53 QPS | 三星官方产品页 + 三星公布的 MLPerf 结果（媒体报道） | 厂商内部测试 + **MLPerf 行业基准**（后者可比性较好） |
| 「算力限制 3215 tokens/s vs 带宽限制 4.8 tokens/s」骁龙 8 Gen 3 算例、小米 Qwen3-8B-MNN 实测 7.04 tokens/s | 券商研报（新浪财经/东方财富转载） | **第三方研报简化推演，非实测，仅供数量级直觉** |
| prefill 计算受限 / decode 访存受限；NVIDIA Research 2025、IBM "Mind the Memory Gap" 2025 | 技术博客综述引用 | 第三方综述（原始论文本次未直接核实） |

---

## ⚠️ 待核实清单

- **所有 TOPS 绝对值**：高通官方 Product Brief 未标 TOPS；天玑 9500 的「100 TOPS」为第三方引述且未标精度口径（INT8/INT4/双 NPU 合计均未知）；Apple ANE、Tensor G5 的 TOPS 本笔记未填。**引用任何 TOPS 前必须回查原始口径。**
- **NNAPI 是否在 Android 16/17 被移除**：官方文档只明确「Android 15 弃用」。移除时间表、旧 App 兼容策略均未核实。
- **LiteRT v2 / LiteRT NPU 加速的当前状态**：GitHub 标注 Alpha + EAP，但仓库 README 可能滞后于实际发布。**Google Tensor 与三星 S.LSI 的 NPU 支持标注为 "coming soon"，是否已落地未核实。**
- **LiteRT-LM 版本号混乱**：本次检索中同时看到 v0.8.0 / v0.13 / v0.15.0 的 changelog（含镜像仓库），**具体最新稳定版本待以 google-ai-edge/LiteRT-LM 官方仓库为准**。
- **Exynos 2600 的 +113% 基准代次**：不同报道分别写作「对比 Exynos 2400」与「对比 Exynos 2500」，需回查三星原始表述。
- **ONNX Runtime Mobile / llama.cpp / MNN / ncnn / MLC-LLM 的 2026 年状态**：本次未核实到一手资料，表格中相关行仅为定位描述，版本与 NPU 后端成熟度均待核实。
- **海思 / 紫光展锐 / 玄戒等平台**：本次未核实到可靠公开一手资料，笔记中留空未填，避免臆测。
- **Core AI 与 Core ML 的取代关系**：WWDC26 材料中 Core AI 被称为「next evolution」，但未明确 Core ML 是否弃用，待核实官方迁移说明。
- **「Gemini Nano 32K 上下文」「2.6× / 2× 提升」的完整测试条件**：Google 博客给出的是场景限定数据（Pixel Screenshots / Recorder），非通用推理指标。
- **券商研报算例**：简化模型，未计 KV Cache、量化后权重体积、实际带宽利用率，**不可作为选型或立项依据**。
- **prefill/decode 学术论文原文**：NVIDIA Research 与 IBM 的两篇 2025 年论文本次仅通过第三方综述获知，未直接查阅原文。

---

#标签/NPU #标签/端侧推理 #标签/编译栈 #标签/芯片 #标签/OS产品经理 #标签/广度种子笔记
