---
title: 端侧 AI 与手机计算摄影 学习笔记
tags:
  - 端侧AI
  - 计算摄影
  - 计算影像
  - 手机影像
  - NPU
  - ISP
created: 2026-10-08
source: WebSearch/WebFetch 核实（Qualcomm / MediaTek 官方稿、Apple 官方对比页、华为 XMAGE 公开资料、NTIRE 2026 学术挑战赛、Android Authority / 媒体综述；部分媒体数字标「待核实」）
---

# 端侧 AI 与手机计算摄影 学习笔记

> **一句话心智模型**：手机计算摄影 = 镜头只负责「收光」，NPU 与 ISP 协同把十几张原始帧「算」成一张你眼睛想看到的照片——AI 不是滤镜，而是相机管线的内建构件。

本文聚焦**相机管线里的 AI 增强（非生成式文生图）**：HDR 融合、夜景降噪、超分、人像分割/虚化、语义感知编辑、端侧照片理解；以及 NPU/ISP 协同的硬件落地。区别于 [[端侧扩散模型与端侧图像生成 学习笔记]]（那是文生图*生成*侧）、[[端侧 AI 芯片架构谱系 学习笔记]]（硬件微架构）与 [[端侧 AI 功耗与散热约束 学习笔记]]（功耗预算）、[[端侧多模态 VLM 学习笔记]]（视觉*理解*本身）。

## 广度覆盖（BREADTH > DEPTH）

| 维度 | 要点 | 主流方案 / 代表产品 | 2025-2026 进展 | 代表产品 |
|---|---|---|---|---|
| **定义** | 用多帧/神经网络在端侧重建影像，而非单帧光学成像 | HDR 融合、夜景多帧降噪、超分、人像分割虚化 | 从「传统 ISP 流水线」走向「神经网络端到端 ISP（Neural ISP）」 | 各厂商旗舰 SoC |
| **分类·能力** | HDR 融合 / 夜景降噪 / 超分 / 人像分割虚化 / 语义感知编辑 / 端侧照片理解 | 语义分割、深度估计、物体识别嵌入 ISP 管线 | 实时语义分割 + 像素级区域处理成为旗舰标配 | Pixel、iPhone、Mate 系列 |
| **代表厂商·Google** | HDR+（burst 对齐融合）+ Night Sight（极低光多帧）+ 语义分割人像虚化 + Tensor 芯片端侧降噪 | Pixel 系列；Tensor 芯片 IPU/专用影像处理 | Night Sight 端侧神经网络降噪提速（待核实具体版本号） | Pixel 8/9 系列 |
| **代表厂商·Apple** | Photonic Engine（更早阶段对未压缩数据做融合）+ Deep Fusion（像素级 ML 纹理）+ Smart HDR + 端侧 ML demosaicing | iPhone 16/17 系列；Neural Engine 实时跑计算摄影栈 | 全系三摄 48MP Fusion、Focus & Depth Control（拍后改虚化）、Clean Up 物体擦除（Apple Intelligence） | iPhone 17 Pro |
| **代表厂商·Qualcomm** | Snapdragon Sight：18-bit 三 ISP + Hexagon NPU 协同（场景识别、降噪、锐化、高光压制、视频虚化） | 骁龙 8 系列旗舰平台 | 旗舰 ISP 持续高吞吐 + AI 深度融合，官方称面向"AI-enhanced camera" | 小米/荣耀/vivo 旗舰 |
| **代表厂商·MediaTek** | Imagiq ISP：RAW 域处理引擎 + NPU 辅助（实时追焦、4K60 电影人像、4K120 双轨防抖） | 天玑 9500 + Imagiq 1190（2025-09 发布） | Imagiq 1190 支持 2 亿像素 AI 降噪直出、NPU 990 存算一体赋能实时追焦（来源：MediaTek 官方稿） | vivo X300 / OPPO Find X9 系列 |
| **代表厂商·华为** | XD Fusion 超清图像引擎 + XMAGE（光机电算底座）+ 红枫原色多光谱镜头 + rNVP 实时神经视频处理 | Mate 70 / Pura 80 / Mate X6/X7 系列 | 150 万多光谱通道、AI 辅助构图、端云结合十大影像趋势（2024 品牌夜公布） | Mate 70 / Pura 80 |
| **代表厂商·Samsung** | ProVisual Engine：AI ISP、Object-Aware 引擎、Expert RAW 虚拟光圈、Generative Edit | Galaxy S25 系列 | 10-bit HDR 视频默认、主体/背景分离降噪；S26 Ultra 前置也用 AI ISP（待核实） | Galaxy S25 Ultra |
| **2025-2026 趋势①** | **扩散模型复原/超分（diffusion SR）下移到端侧**：one-step diffusion + LoRA + 知识蒸馏 | NTIRE 2026 Mobile Real-World SR 挑战赛（MediaTek Dimensity 8400 平台） | 主流方法转向单步扩散、师生蒸馏、GAN-扩散混合，4× 真实退化超分；学界已验证端侧可行 | 学术 benchmark |
| **2025-2026 趋势②** | **端侧分割模型 + 实时神经网络嵌入 ISP 管线**：分割→区域专属处理（天空/皮肤/文本） | 各厂商语义分割引擎；Sony IMX500/501 传感器内 AI（逻辑层集成 NPU） | "AI 向传感器侧下沉"路线（在 CIS 逻辑层直接出元数据/目标跟踪） | Sony IMX500/501 |
| **2025-2026 趋势③** | **端侧大模型赋能影像语义编辑**：自然语言改图、拍后改焦平面/虚化、语义检索相册 | Apple Clean Up、Galaxy Generative Edit、华为 AI 构图；端侧 SLM/VLM 驱动 | 编辑从"工具按钮"走向"语义指令"，依赖 [[端侧大模型推理 学习笔记]] 与 [[端侧多模态 VLM 学习笔记]] 能力底座 | 各 OS 原生 AI 功能（见 [[操作系统原生 AI 功能图谱 学习笔记]]） |

## 深度盲区（留给 Ethon 后续补充）

- [ ] **Neural ISP 的工程边界**：端到端神经网络替代传统 ISP 流水线的真实量产进度如何？哪些环节（demosaic/tonemap/降噪）已全神经网络化，哪些仍需传统模块兜底？（媒体口径偏乐观，待核实）
- [ ] **端侧 diffusion 超分的"幻觉"风险与 C2PA 溯源**：当 80%+ 像素由扩散先验生成，手机影像的司法鉴定/新闻真实性如何保证？各厂商是否默认写 provenance 元数据？（部分媒体数字待核实）
- [ ] **NPU/ISP 协同的算力与带宽账本**：RAW 域多帧缓冲（如 40 帧 4K60）对内存带宽、NPU TOPS、功耗的真实占用是多少？与 [[端侧 AI 功耗与散热约束 学习笔记]] 的预算如何权衡？
- [ ] **国产厂商自研影像芯片/算法路线对比**：vivo V 系列影像芯片、OPPO 20-bit 极端动态范围（媒体称目标 120dB）的具体技术栈与端侧部署方式（待核实具体型号与年份）
- [ ] **端侧照片理解的产品形态**：相册语义检索/回忆生成依赖端侧 VLM 还是端云协同？延迟、隐私、离线可用性如何取舍？
- [ ] **rw 可复现的厂商白皮书对照**：Google HDR+ 原始论文（2014/2018）、Apple Photonic Engine 官方技术文档、华为 XD Fusion 架构图——哪些有公开权威来源，哪些仅媒体转述？

## 附：来源清单

- Qualcomm, Snapdragon Sight 技术概览与骁龙 8 平台产品简报：https://www.qualcomm.com/smartphones/features ；https://www.qualcomm.com/content/dam/qcomm-martech/dm-assets/documents/snapdragon-8-gen-1-mobile-platform-product-brief.pdf
- MediaTek 天玑 9500 官方发布稿（Imagiq 1190、NPU 990、4K60 人像/4K120 防抖）：https://www.mediatek.com/zh-cn/press-room/mediatek-dimensity-9500-unleashes-best-in-class-performance-ai-experiences-and-power-efficiency-for-the-next-generation-of-mobile-devices
- Google Camera / HDR+ / Night Sight 技术说明：https://www.androidauthority.com/google-camera-3365224/
- Apple iPhone 17/16 相机与芯片官方对比页（Photonic Engine / Deep Fusion / Smart HDR / Neural Engine）：https://www.apple.com/iphone/compare/?modelList=iphone-17,iphone-16
- 华为 XMAGE 公开资料与十大影像趋势（IT之家整理，2024 品牌夜）：https://digi.ithome.com/archiver/769/978.htm ；XMAGE 百度百科（含 2025 Mate 70 / Pura 80 红枫原色）：https://baike.baidu.com/item/%E5%8D%8E%E4%B8%BA%E5%BD%B1%E5%83%8FXMAGE/61683763
- Samsung ProVisual Engine / Galaxy S25 AI 相机开发者访谈：https://www.imaginepro.ai/blog/2025/5/behind-the-scenes-of-developing-the-galaxy-s25-series-camera ；Samsung 官方 Galaxy AI 页：https://www.samsung.com/si/galaxy-ai/
- NTIRE 2026 Mobile Real-World Image Super-Resolution 挑战赛综述（one-step diffusion / LoRA / 蒸馏，MediaTek Dimensity 8400）：https://lacuna.tiptreesystems.com/paper/the-first-challenge-on-mobile-real-world-image-super-resolution-at-ntire-2026/art_db705c0a0a0bde90663381cbfa506729
- AI-ISP 架构演进综述（OPPO 20-bit、Sony IMX500/501 传感器内 AI、华为 rNVP 等）：https://www.toutiao.com/article/7686047450699678243/
- 参考性/观点性长文（含大量推测性数字，仅作趋势参考，具体数值标待核实）：https://www.gurdeep.net/blog/computational-photography-how-ai-is-redefining-cameras ；https://frameandfocal.com/photography-tips/apple-iphone-17-pro-first-impressions-huge-upgrades-for-photo-and-video

## ⚠️ 待核实清单

1. Google Pixel「Night Sight 3.0 / 双阶段光子计数 / 12-bit RAW / Photon Processing Unit」等具体版本与硬件细节来自 frameandfocal 媒体稿，与 Android Authority 等保守描述不一致，**版本号与规格待核实**。
2. Apple「Photonic Engine 4.0 / Deep Fusion 5 / Smart HDR 6 / A18 Pro 12 核 ISP 16-bit 处理」等命名与数字来自第三方媒体，**Apple 官方从未公开版本号**，待核实。
3. Samsung「Galaxy S26 Ultra 前置相机也用 AI ISP」来自斯洛文尼亚三星区域站页面，**是否为全球通用规格待核实**。
4. OPPO「20-bit 极端动态范围、目标 120dB」来自中文媒体综述，无官方一手出处，**待核实**。
5. gurdeep.net 系列长文中的具体指标（如 2026 旗舰 16.8 档 DR、shutter lag 3ms、94% 像素为生成等）属观点性/推测性内容，**不作为事实引用，待核实**。
6. 「vivo V 系列影像芯片具体型号与端侧部署方式」未在本次检索中获得权威一手来源，**待核实**。
7. 各厂商「端侧 diffusion 超分」是否已量产落地到消费旗舰，还是仅停留在学术/演示阶段，**待核实**（NTIRE 2026 仅证明学术可行）。

#标签/端侧AI #标签/计算摄影 #标签/手机影像
