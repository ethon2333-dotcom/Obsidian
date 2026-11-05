---
title: 端侧模型推理可解释性与 saliency 可视化 学习笔记
tags:
  - 可解释性
  - 端侧推理
  - saliency
  - 特征归因
  - XAI
created: 2026-10-15
source: WebSearch / WebFetch 核实（2025-2026），详见文末「附：来源清单」
---

**端侧可解释性 = 在设备本地（不把输入/激活/中间结果上传云端）让模型的决策过程对人类可理解、可验证、可信任。**

> 本文聚焦端侧模型「内部推理」的可解释性 / saliency 技术本身（算法与工程），与 [[AI 产品的可解释性 UX 与归因展示 学习笔记]]（产品 UX 层的归因展示）刻意区分：那篇讲「如何把归因结果呈现给用户」，本篇讲「归因/saliency 是怎么在端侧算出来的」。

## 一、广度速览（表格）

| 维度 | 内容要点 |
| --- | --- |
| **定义** | 端侧可解释性（on-device interpretability）= 在手机/NPU/MCU 等受限硬件上，对模型推理做特征归因、显著性图、概念解释，使「黑盒决策」局部或全局可见。**核心约束：推理与解释都尽量不离开设备**（隐私 + 低延迟 + 离线）。saliency 可视化是其中最直观的一类——把「输入里哪部分驱动了输出」画成热力图。 |
| **分类** | ①**梯度类**：Saliency / Gradient×Input / Integrated Gradients / SmoothGrad（对输入求梯度或路径积分）。②**注意力类**：Transformer 的 attention weights / attention rollout（便宜但未必真 faithful）。③**LIME-SHAP 类**：局部代理模型 / Shapley 值（模型无关，但开销大）。④**概念激活向量 TCAV / 概念瓶颈模型 CBM**：用「人类可理解概念」解释而非单像素。⑤**显著性图 / 类激活图**：Grad-CAM、Layer Grad-CAM、Guided GradCAM（视觉任务最常用）。⑥**特征归因（feature attribution）**：上面 ①⑤ 的统称，也包括 LRP、DeepLIFT、Feature Ablation、Occlusion 等扰动法。 |
| **主流方案与代表工作** | • **Captum**（Meta，构建于 PyTorch）：统一归因库，含 Integrated Gradients、GradCAM、LRP、DeepLIFT、**LLMAttribution / LLMGradientAttribution**（专用于 LLM）、TCAV、NoiseTunnel 等 15+ 算法。• **Grad-CAM / Guided GradCAM**：视觉类判别显著性图事实标准。• **LLM-Attribution / 归因图（attribution graphs）**：大模型 token 级归因、电路追踪（TransformerLens、Circuits 方向）。• **概念瓶颈模型 CBM / Post-hoc CBM / Label-Free CBM**：用 CLIP 自动标注概念，免人工概念标注即可训练可解释模型。• **端侧轻量归因**：LIME > SHAP 的「资源-透明」折中（见进展）；TinyML 上用 KAN 原生可解释激活 + 梯度/SHAP 风格相关性。 |
| **2025-2026 进展** | • **端侧 XAI 综述密集出现**：Neurocomputing 2026《Explainable lightweight neural networks》指出知识蒸馏 KD 是最常用轻量方案，且 KD 与 XAI 的交互是关键开放问题。• **边缘实测基准**：IJECS 2025 在 Raspberry Pi / Jetson Nano / Coral TPU 上实测 SHAP/LIME/Saliency，结论——SHAP 质量高但开销大（适合 Jetson 级），LIME 在低端设备实时性最佳，Saliency 轻但非视觉任务解释力有限。• **量化会破坏 saliency**：arXiv 2512.17515（2025-12）发现 QAT（量化感知训练）在降算力同时仍能保持「稳健的 saliency 解释」，提示端侧部署必须验证归因质量而非只看精度。• **高效 TCAV**：E-TCAV（arXiv 2605.10261, 2026）、α-TCAV（arXiv 2605.15688, 2025）通过「倒数第二层代理 / 统一框架」把 TCAV 计算降到线性加速，朝实时概念解释走。• **TinyML 原生可解释**：TinyKAN-HAR（MDPI MAKE, 2026）用 KAN 可学习样条激活，145KB flash / 4.1ms 延迟下仍可做传感器级+时间级+神经元级解释。• **统一解释框架**：IEEE TPAMI 2026 iERF 框架把局部/全局/机制三层解释统一到「点特征向量 + 有效感受野」。 |
| **关键玩家** | • **Google**：Gemini Nano / AICore 端侧管线；联邦学习 + 差分隐私把「解释/改进」留在设备（隐私向解读，见待核实）；Gboard 早是端侧学习范本。• **Apple**：AIC / Neural Engine 端侧推理 + Private Cloud Compute；可解释性更多是「架构级隐私可信」叙事而非开源归因工具。• **学术/开源**：Meta（Captum）、Kim et al. 的 TCAV（2018 至今持续演进）、CBM 系列（Koh 2020 → Label-Free CBM）、Mechanistic Interpretability（TransformerLens / SAE / 电路追踪）、IoT–XAI 硬件中心评估（CCS/MFR/PUT 指标，MDPI Future Internet 2026）。 |

## 二、深度盲区（待 Ethon 自行补充）

- [ ] 端侧 saliency / 归因的**真实功耗与延迟开销**：归因常需多次前向/反向（如 Integrated Gradients 几十步积分），在 NPU 上是否值得？有无「一次前向出归因」的端侧特化算子？
- [ ] **隐私约束下的归因可见性**：输入不出端，但中间激活/归因图是否也算敏感数据？归因结果回显给用户时有没有新的隐私泄露面？
- [ ] 与 **AI 产品的可解释性 UX 与归因展示** 的边界：算法层归因（哪些像素/token 重要） vs 产品层展示（用户要的是「为什么」而非热力图）——端侧算出来的归因如何被 UX 正确消费而不误导？
- [ ] **量化（INT8/W8A8）对归因 faithful 度的影响**：端侧必量化，但多数归因方法在 FP32 验证；QAT 保 saliency（arXiv 2512.17515）是否普适？PTQ 呢？
- [ ] **端侧多模态 VLM 的归因**：图像 grounding + 文本输出联合归因怎么做？saliency 在 VLM 上是否仍有效，还是退化成 attention 可视化？
- [ ] **端侧 LLM（SLM）的 token 级归因能否实时**：LLMAttribution 在手机 SLM 上跑一次解释要多少 token / 多少延迟？是否只能离线调试而非在线展示？

## 三、库内关联（防孤岛）

- 端侧推理底座与本文「在设备上算归因」的算力前提：[[端侧大模型推理 学习笔记]]
- 端侧 VLM 的 saliency / grounding 归因落点：[[端侧多模态 VLM 学习笔记]]
- SoC 与 NPU 协同设计影响归因算子能否硬件加速：[[端侧模型与 SoC 协同设计 学习笔记]]
- 端侧归因质量/开销的可量化评测接口：[[移动端 AI 基准评测 学习笔记]]
- 与产品层的分界（算法归因 vs UX 归因展示）：[[AI 产品的可解释性 UX 与归因展示 学习笔记]]（注：该篇经 Glob 验证当前库内尚不存在，仅作概念对照，未建立真实 wikilink）

---

## 附：来源清单

真实检索到的来源（含可信与待核实，已按可信度标注）：

**相对可信（期刊/会议/预印本/官方）：**
1. Mohammed AlNusif, *Explainable AI in Edge Devices: A Lightweight Framework for Real-Time Decision Transparency*, IJECS, Vol.14 No.07, 2025. DOI:10.18535/ijecs.v14i07.5181 — https://ijecs.in/index.php/ijecs/article/view/5181
2. *Resource-efficient medical image classification for edge devices* (含 QAT 对 saliency 影响), arXiv:2512.17515, 2025-12 — https://arxiv.org/pdf/2512.17515
3. *Explainable Kolmogorov–Arnold Networks for Zero-Shot HAR on TinyML Edge Devices* (TinyKAN-HAR), MDPI MAKE 8(3):55, 2026 — https://www.mdpi.com/2504-4990/8/3/55
4. Yearim Kim et al., *From Local to Global to Mechanistic: An iERF-Centered Unified Framework for Interpreting Vision Models*, IEEE TPAMI, 2026 — https://www.computer.org/csdl/journal/tp/2026/09/11498646
5. Captum 官方文档（Meta/PyTorch 归因库，含 LLMAttribution、TCAV） — https://captum.ai/ 与 https://captum.ai/docs/attribution_algorithms
6. Hasib Aslam et al., *E-TCAV: Formalizing Penultimate Proxies for Efficient Concept Based Interpretability*, arXiv:2605.10261, 2026 — https://scholar.google.com/citations?citation_for_view=...
7. *α-TCAV: A Unified Framework for Testing with Concept Activation Vectors*, arXiv:2605.15688, 2025 — https://arxiv.org/abs/2605.15688
8. *Concept-based explanations for neural language classifiers* (TCAVq), Procedia CS / ACM, 2026 — https://doi.org/10.1016/j.procs.2026.01.007
9. *Beyond Input Attribution: A Hands-On Tutorial to Concept-Based XAI and Mechanistic Interpretability*, KDD 2025 Tutorial — https://iris.polito.it/.../KDD_2025___Hands_on.pdf
10. Malaika Mushtaq et al., *Explainable lightweight neural networks: A survey*, Neurocomputing 700:134504, 2026 — https://doi.org/10.1016/j.neucom.2026.134504
11. Aristeidis Karras et al., *Next-Gen XAI for Federated and Distributed IoT Systems: A Survey*, Future Internet 18(2):83, 2026 — https://www.mdpi.com/1999-5903/18/2/83

**待核实（媒体/聚合站，具体数字与引语未获一手佐证，仅作线索）：**
12. USA Business Times, *Apple Intelligence vs. Google Gemini: Who Wins the On-Device AI War?* — 含 WWDC 2026 / Private Cloud Compute 审计 / Gemini Ultra 2.0 等表述，存疑。https://usabusinesstimes.com/...
13. TechReader Magazine, *How Apple's On-Device AI Is Redefining Trust* (2026-07) — 含「PrismML 27B」「iPhone 17 Pro」等，疑似推测/虚构。https://www.techreadermagazine.com/...
14. Telectronichub, *Gemini Nano Vs Apple Intelligence privacy* — 细节对比偏 AI 生成风格，存疑。https://telectronichub.com/...
15. VectMag / SGSI, *Advances and Challenges in Deep Learning: Efficient, Explainable...* — 含「可解释性提升 up to 40%」等未注明实验的数字，存疑。https://vectmag.com/...

## ⚠️ 待核实清单

1. **Apple / Google 端侧可解释性的官方工具与数字**：上述媒体关于「Private Cloud Compute 2026 审计」「Gemini Ultra 2.0 跑分」「PrismML 27B」「iPhone 17 Pro Neural Engine」等均为媒体口径，未获 Apple/Google 官方文档一手佐证，本笔记未采纳为事实。
2. **「LIME 在低端设备实时性最佳、SHAP 开销大」**：来自 IJECS 2025 单一论文在 Raspberry Pi/Jetson/Coral 上的实测，是否普适到手机 NPU 需另测。
3. **QAT 保 saliency 稳健性**：仅 arXiv 2512.17515 在医学图像 CNN 上验证，端侧 LLM/VLM、PTQ 情形未覆盖。
4. **E-TCAV / α-TCAV 的「线性加速」**：来自作者自报，缺第三方复现与端侧部署实测。
5. **TinyKAN-HAR 的 145KB / 4.1ms / 0.32mJ**：来自 MDPI 论文在 Cortex-M4F 上实测，手机端 NPU 迁移收益待核实。
6. **VectMag「混合 XAI 可解释性 +40%」**：无引用、无实验细节，视为未证实数字。
7. **端侧归因的功耗/延迟真实开销**：本文未找到手机 NPU 上归因方法的系统实测，列为深度盲区，待 Ethon 补。

#标签/手机AI智能体 #标签/端侧推理 #标签/可解释性
