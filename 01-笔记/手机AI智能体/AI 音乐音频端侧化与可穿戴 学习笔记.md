---
title: AI 音乐音频端侧化与可穿戴
tags: [广度种子, 知识拓展Loop, 端侧AI, 音频生成, 可穿戴]
created: 2026-09-21
source: WebSearch/WebFetch 核实，含待核实项（厂商口径数字、部分 2026 新品上市时间、榜单排名均标「待核实」）
---

一句话心智模型：**AI 音乐/音频正在从「云端大模型生成」下移到「端侧 + 耳戴/眼镜等可穿戴形态」，核心是用蒸馏、量化、存算一体把音频模型塞进毫瓦级设备的功耗与内存预算里。**

## 与已覆盖笔记的差异

本篇聚焦**声音层 + 端侧工程约束**（在手机/耳机/眼镜本地跑音频生成与 TTS、NPU/SoC 推理、功耗延迟预算），区别于 [[AI 音乐与音频生成 学习笔记]] 的**云端产品广度**（Suno/Udio/MusicGen 等）与 [[AI 眼镜与可穿戴意图入口 学习笔记]] 的**视觉/交互层**（眼镜作为意图入口的软硬件形态）。三者互补：云端讲"能生成什么"、眼镜讲"怎么入口"、本篇讲"怎么在端侧/在耳上本地跑"。

## 广度覆盖（BREADTH > DEPTH，点到为止）

| 子领域 | 定义/是什么 | 端侧 vs 云端 | 主流方案（代表模型/产品/SoC） | 2025-2026 关键进展 | 代表玩家 |
|---|---|---|---|---|---|
| 端侧音频/音乐生成 | 在手机/可穿戴本地生成音乐或音频，去云端依赖 | 端侧：零延迟/隐私/离线；云端：质量高但依赖网络 | TinyMusician（蒸馏自 MusicGen）、JUNK 神经合成器、QQ 音乐本地 NPU 作曲 | TinyMusician 2025-09 arXiv:2509.00914，保留 MusicGen-Small 93% 性能、体积 -55%，号称首个可手机部署音乐生成模型 | arXiv 学界、IRCAM、腾讯音乐（AI PC + Core Ultra NPU） |
| 端侧 TTS 轻量化（第 6 代） | 把 GB 级 zero-shot TTS 压到百 MB 内、CPU 可跑 | 端侧：固定音色包 + 轻 vocoder；云端：动态换声/克隆 | Kokoro-82M（82M, StyleTTS2+iSTFTNet, Apache2.0）、Bark（Suno, 含笑声/音效）、Chatterbox（Resemble, 零样本克隆）、KaniTTS、Piper/MeloTTS（ONNX-first） | Kokoro-82M v1.0 2025-01 发布，54 音色 8 语；流式首包延迟可压到 ~50ms 级；ONNX/GGML/RKNN 部署栈成熟 | hexgrad（Kokoro）、Suno、Resemble AI、eSpeak/Piper 社区 |
| 耳戴 AI 音频 SoC/芯片 | TWS/耳机内集成 NPU/DSP/CIM 跑本地音频 AI | 端侧：ANC/通话/空间音频本地化；云端：仅传指令 | Qualcomm Snapdragon Sound S7/S5/S3、Anker Thus™ A1（CIM 存算一体）、Nordic nRF54LM20B、Realtek RTL8773DO、Syntiant AISonic、GreenWaves GAP9 | Anker Thus 2026-05 发布，5G FLOPS（厂商称约传统 30M FLOPS 的 ~150×，仅限 ANC 任务对比），搭 Liberty 5 Pro；Nordic nRF54L 集成 NPU 2026-03 | Qualcomm、Anker/声阔、Nordic、Realtek、Syntiant、Bestechnic、联发科/达发 |
| AI 眼镜声音层 | 眼镜用骨传导/定向扬声器 + 麦克风做"音频优先"交互 | 端侧：本地拾音/放音；云端：Gemini 等 LLM 推理多在手机/云 | Google Android XR Audio Glasses、Ray-Ban Meta（Gen2）、Amazon Echo Frames 3rd Gen | Google I/O 2026 将智能眼镜拆为 Audio Glasses（先发，2026 秋）/Display Glasses 两类；Ray-Ban Meta 2025 出货 6.5M（媒体口径，待核实） | Google/Samsung、Meta/EssilorLuxottica、Amazon |
| NPU/专用硬件跑音频模型 | 用 NPU、Android NNAPI、存算一体加速音频推理 | 端侧 NPU 推理替代云端 API | Intel Core Ultra NPU、Android NNAPI、Thus CIM、骁龙 NPU | 音频模型首次从"GPU 推理"走向"ARM CPU/专用 NPU/存算一体"三元部署 | Intel、Qualcomm、Anker、各 SoC 厂 |

### 端侧三约束（功耗/延迟/内存）— 工程红线
- **内存**：手机 App 音频模块预算 ~100-200MB，耳塞侧 ~20-50MB，嵌入式更低（口径不一，待核实精确值）。
- **首包延迟**：车载导航 <300ms、客服 IVR <100ms、直播 TTS <50ms 才不卡顿；Gen5 云端首包常 >500ms。
- **功耗**：耳塞为毫瓦级（mW-class），always-on 语音需在极小电量预算内；存算一体（CIM）正是为降低"数据搬运能耗"而生。
- 与 [[端侧 AI 功耗与散热约束 学习笔记]] 同源思路，本篇是其在"音频"子场景的具体化。

## 与库内笔记的连接
- [[端侧语音大模型 学习笔记]]（端到端语音 LLM 新范式，与本篇"端侧音频生成"互补：一个偏理解/对话，一个偏生成）
- [[端侧大模型推理 学习笔记]]（TinyMusician 蒸馏+混合精度量化、Kokoro ONNX 导出都属于端侧推理范式）
- [[端侧 AI 功耗与散热约束 学习笔记]]（耳塞 mW 级功耗预算的工程约束对照）
- [[语音交互与端侧 ASR TTS 学习笔记]]（本篇 TTS 轻量化是其"TTS"环节的工程延伸）
- [[AI 音乐与音频生成 学习笔记]]（云端广度，本篇的下移/端侧对照）
- [[AI 眼镜与可穿戴意图入口 学习笔记]]（本篇"眼镜声音层"是其音频维度的补强）

## 深度盲区（留给 Ethon 后续补充）
- [ ] TinyMusician 在真实手机 SoC（骁龙/天玑/麒麟 NPU）上的实测延迟、功耗、MOS 究竟多少？论文是仿真还是真机？
- [ ] CIM（存算一体）在音频推理上的能效比 vs 传统冯·诺依曼 NPU，有无独立第三方 benchmark？
- [ ] 耳戴设备本地跑"音频生成"（而非仅 ANC/TTS）的工程可行性——TinyMusician 真能塞进 20-50MB 耳塞预算吗？
- [ ] Kokoro/Bark 等端侧 TTS 在中文声调、情感、低延迟流式上的真实表现与云端（如 ElevenLabs）差距？
- [ ] AI 眼镜"音频层"与手机 Gemini 的算力分工：哪些在眼镜端、哪些在手机端、哪些上云？延迟如何切分？
- [ ] 端侧音频生成 + 端侧语音大模型的"联合管线"（生成音乐/音效 → 语音对话）在可穿戴上的产品形态？
- [ ] 版权/合规红线：本地生成音乐的训练数据来源、可商用性（Kokoro Apache2.0 vs 厂商闭源模型）？

## 附：来源清单
1. arXiv:2509.00914 (2025-09) — *TinyMusician: On-Device Music Generation with Knowledge Distillation and Mixed Precision Quantization*（TinyMusician 论文，已核实摘要与核心数字）
2. Local AI Master / Analytics Vidhya / 百度百科 — Kokoro-82M 模型卡与发布信息（82M 参数、StyleTTS2+iSTFTNet、Apache2.0、v1.0 2025-01 发布）
3. PMarketResearch — *AI Bluetooth Audio SoC Market* / *AI Chip for Earphone Market*（Qualcomm S7/S5/S3、Nordic nRF54、Realtek RTL8773、Syntiant、GreenWaves GAP9 等，2025-2026）
4. Gizmochina / NewsBreak / 百度百科 — Anker Thus™ A1 CIM 芯片与 Soundcore Liberty 5 Pro（2026-05 发布，厂商口径 150×/5G FLOPS/吉尼斯记录）
5. Google I/O 2026 报道（PhoneBunch / FoneArena / Financial Express）— Android XR Audio Glasses 与 Gemini 音频眼镜路线
6. 百度智能云 / 讯飞 / CSDN — 端侧 TTS 轻量化（Gen6）、FastSpeech2 量化、KaniTTS、LightTTS 等工程综述

## ⚠️ 待核实清单
- Anker Thus「150× AI 算力」「5G FLOPS」：厂商口径，特指 ANC 任务对比上一代规则 DSP，**非通用基准，且 150× 精确含义依赖厂商定义**（已注明限定条件）。
- Soundcore Liberty 5 Pro「吉尼斯通话清晰度纪录」：厂商/第三方测试宣称，对手机型未公开，**需独立复测验证**。
- Ray-Ban Meta「2025 出货 6.5M 台 / $2.15B 营收」：来自 Treeview 2026 报告经媒体转述，**精确数字待核实**。
- Google Android XR Audio Glasses「2026 秋上市」：I/O 2026 公布计划，**实际上市时间/价格/地区待核实**。
- 端侧内存预算（手机 100-200MB / 耳塞 20-50MB）、首包延迟阈值：来自工程综述口径，**不同 SoC/产品差异大，需按具体机型核实**。
- Kokoro 在 TTS Arena 的具体胜率排名（v1.6 88.3% 等）：榜单动态、随版本变化，**当前排名可能已变，待核实**。
- QQ 音乐本地 NPU 作曲的具体模型、是否真全本地（是否部分环节仍上云）：中文科技媒体口径，**技术细节待核实**。
- 「2026-05-22 安克发布会」与「Thus 与知存科技联合研发」：百度百科与媒体一致，但**芯片量产良率/实际装机量待核实**。

#标签/广度种子 #标签/知识拓展Loop #标签/端侧AI #标签/音频生成 #标签/可穿戴 #标签/AI眼镜
