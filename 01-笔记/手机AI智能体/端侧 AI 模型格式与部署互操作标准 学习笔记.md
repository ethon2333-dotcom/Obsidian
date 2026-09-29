---
title: 端侧 AI 模型格式与部署互操作标准 学习笔记
tags: [知识拓展, 端侧AI, 模型格式, 部署互操作, ONNX, GGUF, ExecuTorch]
created: 2026-09-22
source: WebSearch/WebFetch 核实（见文末来源清单）
---

# 端侧 AI 模型格式与部署互操作标准 学习笔记

> [!note] 一句话心智模型
> 模型格式是「训练产物打包成可落地文件」的契约：一份训练好的模型，靠统一的文件格式与互转工具链，才能一次训练、多端（不同 SoC/NPU/OS）部署，而不被某个运行时或厂商锁死。

## 1. 定义与边界
端侧 AI 模型格式，指把训练好的权重+计算图+元数据序列化成**文件**的规范（ONNX/.onnx、GGUF/.gguf、ExecuTorch/.pte、LiteRT/.tflite、MNN/.mnn、Core ML/.mlpackage 等）。它解决的是「模型产物本身的打包与互通」，属于**部署互操作（interoperability）**层。注意边界：本主题**不是**推理运行时（谁加载执行，见 [[端侧推理框架生态 学习笔记]]），也**不是**量化算法本身（量化是把精度压低的方法，见 [[端侧模型量化 学习笔记]]）；但量化参数常**内嵌**在格式里（如 GGUF 的分块量化信息、.tflite 的量化张量）。

## 2. 主流格式分类（表格）
| 格式 | 主导方 | 典型运行时 | 特点 | 序列化/备注 |
| --- | --- | --- | --- | --- |
| `.onnx` (ONNX) | LF AI & Data 基金会 / 社区 | ONNX Runtime、各 EP | 框架无关中间表示(IR)，>150 算子，跨云/边/Web | Protobuf；Apache 2.0 |
| `.gguf` (GGUF) | ggml-org / llama.cpp | llama.cpp、llama.cpp 衍生 | LLM 专用、自描述 KV 元数据、mmap 友好、量化内嵌 | 二进制；当前版本 v3【待核实】 |
| `.pte` (ExecuTorch) | Meta / PyTorch | ExecuTorch runtime | PyTorch 原生导出、AOT 编译、按后端特化 | 来自 torch.export，常按后端出多份 |
| `.tflite` / `.task` (LiteRT) | Google AI Edge | LiteRT（原 TF Lite） | FlatBuffers，轻量(~300KB 基线)【待核实】；.task 含元数据+标签的任务包 | FlatBuffers；2024 底更名【待核实】 |
| `.mnn` (MNN) | 阿里巴巴 | MNN | FlatBuffers 零拷贝加载，多后端 | 可选分离 `.mnn.weight` |
| `.mlpackage` / `.mlmodel` (Core ML) | Apple | Core ML / ANE | iOS/macOS 原生，Xcode 集成，coremltools 转换 | 苹果私有生态 |

## 3. 互转工具链 / 代表方案（表格）
| 源→目标 | 工具 | 备注 |
| --- | --- | --- |
| PyTorch/TF → ONNX | torch.onnx.export(dynamo=True)、tf2onnx | PyTorch 2.5+ 推荐 dynamo exporter【已核实】 |
| ONNX → .tflite | onnx-tf / TFLite converter | 经 TF 中转，量化在转换期应用 |
| 任意(ONNX/TF/TFLite/Caffe/TorchScript) → .mnn | MNNConvert (mnnconvert) | 支持权重量化 2–8 bit、外部权重分离【已核实】 |
| PyTorch → .pte | torch.export + to_edge + to_executorch | 量化(QAT/LoRA/SpinQuant)在导出期做【已核实】 |
| HF / Safetensors → .gguf | convert_hf_to_gguf.py | llama.cpp 官方转换脚本【已核实】 |
| PyTorch → Core ML | coremltools | 苹果生态专用 |

## 4. 2025-2026 进展（表格 + 简短说明）
| 时间/阶段 | 进展 | 备注 |
| --- | --- | --- |
| 2025 | ONNX 强化 LLM/Transformer 支持、动态形状与控制流 | 社区持续演进【已核实】 |
| 2025-10 | ExecuTorch 达 v1.0 GA | 第三方称 18 Oct 2025 GA【待核实，来源 lablab.ai】 |
| 2025-2026 | LiteRT V2：LiteRT-LM(端侧 LLM)、LiteRT.js(WebGPU/WASM)、Compiled Model API、LiteRT NPU 统一 NPU 加速 | 官方仓库 README【已核实】 |
| 2025-2026 | GGUF K-quants(IQ 系列)成社区主流量化命名 | 社区实践【待核实具体采用率】 |
| 2026 | MNN 强调端侧 LLM/Edge AI 支持 | 仓库定位更新【待核实】 |

互操作为何对端侧关键：①**一次训练多端部署**——同一模型导出多份 .pte/.tflite 适配不同后端；②**SoC 厂商运行时差异**——骁龙(NNAPI/Hexagon)、天玑(APU)、Exynos(NPU)、苹果(ANE)各自加速路径不同，统一 IR(ONNX)或按 backend 特化(.pte)可降低返工。

## 5. 广度盲区 · 待 Ethon 补充
- [ ] `.task` 与 `.tflite` 的精确包含关系与 Task Library 元数据 schema 边界（官方文档未细读）
- [ ] GGUF v3 具体相对 v2 的字段变更清单（版本年份考据）
- [ ] ExecuTorch v1.0 官方 GA 公告与性能基准数字（第三方来源需交叉验证）
- [ ] ONNX Runtime Mobile 与 ONNX Runtime 服务端是否共用同一份 .onnx（含 NPU EP 覆盖矩阵）
- [ ] MNN 在端侧 LLM(KV cache/流式)的实测支持度与最新版本号
- [ ] Core ML .mlpackage 与 .mlmodel 兼容性及转换链路在 2025-2026 的变更
- [ ] 各格式「量化参数内嵌」的精度可逆性：能否从 GGUF/.tflite 反量化回 FP16 做二次部署

## 附：来源清单
- ONNX 互操作/格式：https://www.artificial-intelligence-wiki.com/deep-learning/deep-learning-frameworks/onnx-model-interoperability
- ONNX 导出(dynamo)：https://www.onegen.ai/project/enhancing-ai-with-onnx-an-open-source-project-to-accelerate-model-compatibility/ （stars 数待核实）
- GGUF 规范：https://deepwiki.com/unslothai/llama.cpp/6.1-gguf-format
- ExecuTorch 导出：https://docs.pytorch.org/executorch/0.7/export-overview.html （官方）
- ExecuTorch GA/性能：https://lablab.ai/tech/meta/meta-executorch （第三方，数字待核实）
- LiteRT 官方仓库/特性：https://github.com/google-ai-edge/litert
- LiteRT 更名/选型（2026-08 实测 star 数）：https://ithome.me/post/2026/08/11/edge-ai-inference-framework-guide （媒体，数字待核实）
- MNN 转换流水线：https://leeroopedia.com/index.php/Workflow:Alibaba_MNN_Model_Conversion_Pipeline ；https://deepwiki.com/yeyupiaoling/ClassificationForAndroid/3.4-mnn-implementation

⚠️ 待核实清单
- ExecuTorch v1.0 GA 日期「18 Oct 2025」及 40/50.2 tokens/s、2.5x 提速等性能数字——来源为 lablab.ai 第三方汇总，需官方博客(pytorch.org/blog)交叉验证。
- LiteRT 基线运行时「~300KB」、2024 年底更名具体月份——官方仓库未给出精确数字，媒体口径待核实。
- 各框架 GitHub star 数（Core ML 5.4k / ONNX Runtime 2.1万 / NCNN 2.4万 / MNN 1.6万 等）——ithome 2026-08 实测，时效性待核实。
- ONNX「>21k stars」「>150 算子」——单源(onegen)声明，待核实。
- GGUF「当前版本 v3」「GGML_QUANT_VERSION 2」——deepwiki 文档，版本年份待核实。
- 「MNN 2026 强调端侧 LLM/Edge AI」——仓库定位描述，待核实最新 release note。
- `.task` 格式 schema 与元数据字段边界——未读官方 Task Library 文档，待核实。

#标签/端侧AI #标签/模型格式 #标签/部署互操作 #标签/ONNX #标签/GGUF
