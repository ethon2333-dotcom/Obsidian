---
title: 移动端 AI 基准评测 学习笔记
tags:
  - 种子笔记
  - 广度
  - 端侧
  - 基准评测
  - 跑分
  - NPU
created: 2026-10-09
source: "WebSearch/WebFetch 核实，见文末来源清单"
---

> **心智模型**：移动端 AI「跑分」是一条把「NPU/SoC 硬件算力」翻译成「人能比较的数字」的链条——但端侧 LLM 时代之前，这条链长期被厂商自报数字主导，直到 2026 年 MLPerf Mobile v6.0 才出现真正中立的端侧 LLM 标尺。

本笔记刻意区别于 [[多模态评测基准 学习笔记]]（模型能力基准）与 [[Agent 评测与基准 学习笔记]]（Agent 轨迹评测）：**本篇聚焦「端侧硬件 / 跑分基准体系与厂商对比」，不评模型聪明不聪明，只评「跑得快不快、省不省电、谁家 NPU 强」**。

相关底座笔记：[[端侧 AI 芯片架构谱系 学习笔记]]（NPU 微架构）、[[端侧大模型推理 学习笔记]]（推理本身）、[[端侧推理框架生态 学习笔记]]（运行时）、[[端侧 AI 功耗与散热约束 学习笔记]]（功耗约束）、[[AI 手机与 AI OS 产品竞争格局 学习笔记]]（厂商战略）。

---

## 1. 广度覆盖：基准体系一览

| 分类 | 代表基准 / 产品 | 衡量什么 | 2025-2026 进展 |
|---|---|---|---|
| **中立综合 AI 推理基准** | **MLPerf Mobile**（MLCommons，开源 App，Android/iOS） | 手机跑经典 CV/NLP/生成式任务的延迟与吞吐（单流 90 分位延迟为主指标） | **v6.0（2026-06）新增端侧 LLM 基准**：Llama 3.2 1B / 3B、Llama 3.1 8B，在 TinyMMLU + IFEval 上评性能与精度；并支持 SD 8 Elite Gen 5 上 NPU 加速跑 8B。新增天玑 9500、Exynos 2600 支持 |
| **中立综合 AI 推理基准** | **AI Benchmark（ETH 苏黎世联邦理工，ai-benchmark.com）** | 综合 NPU/GPU/CPU 的 INT8/FP16 CNN 与 Transformer 推理「AI Score」 | 2025-2026 榜单天玑 9500（18306）、骁龙 8 Elite Gen 5（17796）领跑；2026 新榜出现天玑 9600 Pro（22631） |
| **厂商/聚合跑分** | **AnTuTu / AITuTu**（安兔兔 AI 子项）、**鲁大师 AI 排行** | 整机/SoC 综合分与 AI 子项（AITuTu 仅 Inception-V3 + MobileNet-SSD 两模型，偏旧） | AnTuTu v11（2025）旗舰安卓总分破 300 万；鲁大师 2026-09 AI 排行以 iQOO Z11 Turbo 居首（聚合用户均值，**口径待核实**） |
| **SoC NPU 跑分（厂商自报）** | 天玑 9500 / 骁龙 8 Elite Gen 5 / A19 Pro / Tensor G5 / Exynos 2600 / 麒麟 | 各家 NPU 峰值 TOPS 与端侧模型吞吐 | 见下表；**TOPS 与端侧 tokens/s 多为厂商自报，标「待核实」** |
| **端侧 LLM 推理跑分** | 端侧 SLM tokens/s、TTFT（首 token 延迟） | 8B/3B 模型在 CPU/NPU/GPU 上的解码速度、首 token 延迟 | 2025-2026 出现「100 TOPS NPU 时代」；端侧 8B INT4 实测约 8–15 tok/s（CPU 路径常因带宽瓶颈反超 NPU，见待解问题） |
| **端云混合评测** | 厂商自报（Apple Intelligence / Gemini Nano 端云协同） | 端侧小模型 + 云端大模型的动态派发体验 | **目前无统一中立基准**，几乎全是厂商口径，**标「待核实」** |
| **存储/IO 基准（辅助）** | **AndROBench**（开源，存储 I/O） | 顺序/随机读写、SQLite，影响模型加载与 OTA | 非 AI 基准，但与端侧模型加载/差分更新强相关，列此备忘 |

> 注：「AndBench」并非一个公认的 AI 基准，疑似 AI Benchmark / AITuTu / AndROBench 的混淆写法；本笔记按三个真实存在的基准分别收录，**「AndBench」本身存疑，待核实**。

---

## 2. 主流基准详解（点到为止）

### 2.1 MLPerf Mobile（MLCommons，最中立）
- 开源 App（Apache 2.0），Google Play / App Store / GitHub 分发；支持 Android 11+、iOS 13.1+。
- 套件覆盖：图像分类（MobileNetV4）、目标检测、分割、超分（EDSR）、文生图（SD 1.5）、Mobile-BERT，以及 **v6.0 新增的端侧 LLM（Llama 3.2 1B/3B、Llama 3.1 8B）**。
- LLM 评测用 TinyMMLU + IFEval；单流场景主指标为 90 分位延迟。
- **关键事实（已核实）**：v6.0（2026-06）明确支持 Snapdragon 8 Elite Gen 5 的 NPU 加速执行 Llama 3.1 8B；新增天玑 9500、更新 Exynos 2600 支持。v6.0 发布时**尚未公布设备级 LLM 公开成绩**。

### 2.2 AI Benchmark（ETH 苏黎世联邦理工）
- 网站 ai-benchmark.com 持续更新 SoC 排行，是最常被厂商引用的第三方 AI 跑分。
- 已核实的 AI Score 抽样（来自官网排行页）：天玑 9600 Pro 22631（2026）、天玑 9500 18306（2025）、骁龙 8 Elite Gen 5 17796（2025）、骁龙 8 Elite 14459（2024）、骁龙 8 Gen 3 10213（2023）、Google Tensor G4 1301、Exynos 2200 641、麒麟 9000 616。
- 媒体口径：天玑 9500 工程机「接近 15000 分」（2025-09 腾讯新闻），**属媒体/工程机数字，待核实**。

### 2.3 AITuTu / AnTuTu / 鲁大师
- AITuTu 是安兔兔的 AI 专项，仅 Inception-V3 + MobileNet-SSD，**模型老旧**，参考价值有限。
- AnTuTu v11 是综合（CPU/GPU/MEM/UX）跑分，AI 仅是其中一项；月度榜为聚合用户均值。
- 鲁大师 AI 排行（2026-09 更新）以整机 AI 分为口径，**算法与权重未公开，待核实**。

---

## 3. 各 SoC NPU / 端侧 AI 跑分对比（2025-2026）

| SoC（年份） | NPU / AI 单元 | 峰值 TOPS（多为自报） | 端侧 LLM 实测/自报 | 备注 |
|---|---|---|---|---|
| 天玑 9500（2025，MediaTek） | NPU 990 | ~100 TOPS（**自报，待核实**） | ETH AI Benchmark ~15000（工程机，媒体口径**待核实**）；端侧 3B 生成速度较 9400 翻倍（**自报**） | 首发 BitNet 1.58-bit、端侧 128K 上下文（**自报**）；3nm N3P |
| 骁龙 8 Elite Gen 5（2025，Qualcomm） | Hexagon HTP Gen 5 | ~100 TOPS（**自报，待核实**） | 8B INT4（w4a16）~14.9 tok/s、TTFT ~0.11s（Qualcomm AI Hub，**待核实**）；NPU decode 自报 220 tok/s（**待核实**） | 3nm；MLPerf Mobile v6.0 官方支持 NPU 加速 8B |
| Apple A19 Pro（2025） | 16 核 Neural Engine + GPU Neural Accelerator | ~35 TOPS（**估算，待核实**） | 8B INT4（CPU/MLC-LLM）~7–12 tok/s、TTFT ~380ms（第三方）；iPhone 17 Pro AnTuTu ~2.39M | 统一内存带宽 ~76.8 GB/s；12GB 起 |
| 谷歌 Tensor G5（2025，Pixel 10） | 第 4 代 TPU | 非公开 | Gemini Nano 较 G4 快 2.6×（**Google 自报，待核实**）；8B 经 LiteRT CPU ~10 tok/s | 首款 TSMC 代工 Tensor；端侧 LLM 实际多走 CPU |
| 三星 Exynos 2600（2026） | NPU（2nm GAA） | 非公开 | 生成式 AI 较 Exynos 2500 提升 113%（**Samsung 自报，待核实**） | 全球首款 2nm GAA 手机芯片 |
| 华为麒麟 9020/9030（2024-2025） | 达芬奇 NPU | 非公开 | **无公开中立跑分，待核实** | 受制裁影响，第三方基准稀缺 |

> 关键洞察（已核实趋势）：**端侧 LLM 的瓶颈常是内存带宽而非算力**——因此 CPU 路径（llama.cpp / ExecuTorch / MLC-LLM）在 7–8B 上经常不输甚至快于 NPU 路径，因为 NPU 工具链（如 QNN）对 LLM 成熟度滞后。这是 2025-2026 的普遍现象，但各设备差异大。

---

## 4. 端侧 LLM 推理跑分（tokens/s 与首 token 延迟）

| 场景 / 模型 | 设备 / 框架 | 结果 | 可信度 |
|---|---|---|---|
| Llama 3.1 8B INT4（w4a16） | 骁龙 8 Elite Gen 5（Qualcomm AI Hub, GENIE） | ~14.9 tok/s，TTFT ~0.11–3.5s（随 prompt 长度） | 厂商/仓库口径，**待核实** |
| Llama 3.1 8B INT4 | Apple A19 Pro（MLC-LLM, CPU） | ~7–12 tok/s，TTFT ~380ms | 第三方，较可信 |
| Llama 3.1 8B INT4 | 谷歌 Tensor G5（LiteRT CPU/XNNPACK） | ~10 tok/s | 第三方，较可信 |
| 3B 级（Qwen2.5-3B 等） | iPhone 17（A19, PocketPal） | ~14 tok/s，TTFT 0.5–2s | 第三方实测，较可信 |
| 小模型（<1B） | iPhone 17 Pro（第三方） | 高达 ~136 tok/s（量化子 1B） | 第三方，**待核实** |
| NPU decode 上限 | 骁龙 8 Elite Gen 5（Qualcomm 自报） | 220 tok/s | **厂商自报，待核实** |
| 首 token 延迟参考 | MLPerf Inference 5.1（小 LLM 交互上限） | 首 token <0.5s、每输出 token 30ms（Llama 3.1 8B） | MLCommons 规范，较可信 |

---

## 5. 待解问题（留给 Ethon 深挖）

- [ ] 待解问题：MLPerf Mobile v6.0 至今（2026-10）是否已公布设备级 LLM 公开成绩？哪些机型进了榜、排名如何？
- [ ] 待解问题：端侧 LLM「CPU 反超 NPU」是普遍规律还是特定框架/量化下的偶然？能否给出分 SoC、分模型大小、分量化（INT4/w4a16）的对照表？
- [ ] 待解问题：各家 NPU TOPS 的「峰值 / 持续 / 稀疏 / 稠密」口径差异有多大？为什么同是「100 TOPS」体验天差地别？
- [ ] 待解问题：端云混合评测有没有可复现的中立方法（例如按网络/任务难度动态派发的延迟-质量曲线）？还是只能信厂商？
- [ ] 待解问题：华为麒麟因制裁缺第三方基准，能否从开源社区（OpenHarmony / 达芬奇算子覆盖率）侧面补全其端侧 AI 能力画像？
- [ ] 待解问题：AI Benchmark 的「AI Score」权重近年如何随 Transformer 权重上升而变化？它还能代表真实端侧 LLM 体验吗？
- [ ] 待解问题：功耗/散热约束（见 [[端侧 AI 功耗与散热约束 学习笔记]]）如何把「跑分峰值」压成「可持续吞吐」？有无每瓦 tokens/s 的横向数据？

---

## 附：来源清单

- MLCommons 官方：MLPerf Mobile v6.0 发布（2026-06）— https://mlcommons.org/2026/06/mlperf-mobile-v6/
- MLCommons：MLPerf Inference: Mobile 基准套件与指标 — https://mlcommons.org/en/inference-mobile-10/
- MLCommons GitHub Releases（v6.0 / v6.0.1，支持 SoC 列表）— https://github.com/mlcommons/mobile_app_open/releases
- AI Benchmark（ETH 苏黎世联邦理工）SoC 排行 — https://ai-benchmark.com/ranking_processors
- AnTuTu / AITuTu 信息汇总 — https://grokipedia.com/page/AnTuTu ；AITuTu 版本页 — https://apkvenus.com/aitutu-benchmark/
- 鲁大师 AI 排行（2026-09 更新，聚合口径）— https://www.ludashi.com/rank/aiRanking.html
- 天玑 9500 媒体评测（ETH AI Benchmark 登顶、工程机跑分）— https://news.qq.com/rain/a/20250922A07B8F00 ；品玩 — https://www.pingwest.com/a/307821
- 端侧 LLM 推理汇总（含 SoC tokens/s、TOPS 对照）— https://docs.octomil.com/blog/on-device-llm-inference-2025-2026
- Qualcomm AI Hub 模型性能（Llama 8B on SD 8 Elite Gen 5）— https://huggingface.co/qualcomm/Llama-v3-8B-Instruct ；ModelScope — https://www.modelscope.cn/models/qualcomm/Llama3-TAIDE-LX-8B-Chat-Alpha1
- 移动端 CPU 推理与 SoC 跑分对照 — https://github.com/ranjithrajv/awesome-cpu-first-ai/blob/master/docs/mobile-cpu-inference.md
- iPhone 17 本地 LLM 实测（PocketPal）— https://sahilsatralkar.com/ios/ai/running-local-llm-on-iphone
- AndROBench（开源存储 I/O 基准）— https://www.ddooo.com/softdown/217037.htm
- VoxBooster 2026 端侧 SLM 统计（MLPerf Mobile 进入 LLM 时代综述）— https://voxbooster.com/blog/small-language-models-mobile-statistics-2026

---

## ⚠️ 待核实清单

- ⚠️ **「AndBench」** 是否为真实独立基准尚无定论，疑似 AI Benchmark / AITuTu / AndROBench 混淆，待核实。
- ⚠️ 天玑 9500 工程机「接近 15000 分」（ETH AI Benchmark）为媒体/工程机口径，非官网稳定榜，待核实。
- ⚠️ 各 SoC 的「峰值 TOPS」（天玑 ~100、骁龙 ~100、A19 ~35 等）多为厂商自报或估算，口径不一，待核实。
- ⚠️ 骁龙 8 Elite Gen 5 的 NPU decode 220 tok/s、8B ~14.9 tok/s 来自 Qualcomm AI Hub / 厂商口径，待第三方复现核实。
- ⚠️ 谷歌 Tensor G5「Gemini Nano 快 2.6×」、三星 Exynos 2600「生成式 AI 提升 113%」均为厂商自报，待核实。
- ⚠️ iPhone 17 Pro 小模型「136 tok/s」为第三方单点测试，条件未明，待核实。
- ⚠️ 鲁大师 / AnTuTu AI 排行的算法权重与采集方式未公开，整机 AI 分不可直接等同于端侧 AI 能力，待核实。
- ⚠️ 华为麒麟 9020/9030 无公开中立 NPU 跑分，所有端侧能力推断均待核实。

#标签/手机AI智能体/端侧/基准评测/广度种子
