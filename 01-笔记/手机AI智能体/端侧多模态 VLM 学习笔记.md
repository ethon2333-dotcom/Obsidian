---
title: 端侧多模态 VLM 学习笔记
tags:
  - 手机AI智能体
  - 端侧多模态
  - VLM
  - 端侧Agent
created: 2026-08-16
source: WebSearch 核实（MiniCPM-V / MobileVLM / Qwen-VL / InternVL / SmolVLM / Apple 端侧多模态 等官方博客与论文，2024–2026）
---

# 端侧多模态 VLM 学习笔记

## 学习定位
本笔记聚焦「能跑在手机上的视觉语言模型（VLM）本身」——它的结构（视觉编码器 + 投影器 + LLM）、代表家族与端侧约束。它是 [[多模态 GUI 理解与 UI Grounding 学习笔记]] 的互补前置：那篇讲「怎么看懂并点中屏幕上的 UI 元素」（grounding 算法），本篇讲「模型凭什么能看懂图」。二者共同服务于 [[端侧意图框架 学习笔记]] 的「感知」环节。同时，VLM = 「语言模型 + 视觉」，与纯语言的 [[端侧小语言模型 SLM 生态 学习笔记]] 是并列能力，架构路线与 [[外挂适配式 vs 原生多模态架构]] 高度相关。更上层的归类见 [[大模型四类型：LLM VLM MLLM LMM]] 与 [[AI模型基础 MOC]]。

> **心智模型：端侧 VLM 是手机看懂世界的眼睛——不用把照片、截图、相机画面上传云端，它就能在设备内理解眼前发生了什么，隐私不出端、响应不离线。**

## 一、概念定义（术语铺广度）
| 术语 | 定义（核实口径） | 代表 / 备注 |
|------|----------------|-------------|
| VLM（Vision-Language Model） | 以图像/视频 + 文本为输入、输出文本的视觉语言模型；典型结构 = 视觉编码器 + 投影器 + LLM | GPT-4V、Qwen-VL 等同族概念 |
| SMM（Small Multimodal Model） | 小型多模态模型，泛指能在端侧跑的小尺寸 VLM | SmolVLM、MiniCPM-V、MobileVLM 都可归入 |
| 视觉编码器（Vision Encoder） | 把图像切成 patch 并编码为视觉 token 的视觉骨干，常基于 CLIP/SigLIP 预训练 | SigLIP、CLIP ViT、InternViT |
| 投影器（Projector / Connector） | 把视觉特征对齐/压缩到 LLM 词嵌入空间的模块 | MLP、Q-Former、LDPv2、Resampler（见下表） |
| 端侧多模态（On-device Multimodal） | 视觉理解在手机/边缘 NPU 上本地完成，不依赖云端往返 | 隐私 + 低延迟 + 离线可用 |
| MoE VLM | 用混合专家替代稠密 FFN，以更少激活参数换吞吐 | 路线见第二节（具体型号待核实） |

## 二、分类与主流架构路线
| 路线 | 做法 | 优点 | 代价 / 局限 |
|------|------|------|-------------|
| 原生多模态 vs 外挂适配式 | 是否在预训练阶段就让视觉与语言统一训练（详见 [[外挂适配式 vs 原生多模态架构]]） | 原生路线跨模态一致性更好 | 训练成本高；外挂（ViT+projector 接现成 LLM）落地快 |
| 稠密（Dense） | 全参数激活的常规 VLM | 结构成熟、易量化部署 | 端侧算力下吞吐受限 |
| MoE（混合专家） | FFN 拆成多专家、按 token 路由 | 总参大但激活参小，提效明显 | 路由开销、显存占用与端侧编译适配更复杂（具体落型号待核实） |
| 视觉 token 压缩 | 用 pixel-shuffle / Resampler / LDPv2 把视觉 token 数压到 1/4~1/16 | 直接降 LLM 计算与 KV Cache | 高分辨率细粒度 OCR 可能丢信息 |

## 三、代表模型 / 家族（核实存在与年份，用表格）
| 名称 | 机构 | 年份 | 定位 | 规模 / 备注 |
|------|------|------|------|-------------|
| MobileVLM / V2 | 美团 · 浙江大学 | 2024（V2 为 2 月） | 首个面向移动端设计的 VLM 系列 | V2 含 1.7B / 3B / 7B；Jetson Orin 上 1.7B 达 51.6 tok/s |
| InternVL2（书生·万象） | 上海 AI 实验室 OpenGVLab | 2024-07 | 1B~108B 全谱系，1B 主打边缘 | InternVL2-1B ≈ 0.9B（938M），可在端侧芯片（AX650N 等）部署 |
| Qwen-VL / Qwen2-VL / **Qwen2.5-VL** | 阿里巴巴 | Qwen2.5-VL：2025-01 | 3B/7B/72B（后增 32B） | 原生动态分辨率 ViT；训练数据 4.1T token；可作视觉智能体 |
| MiniCPM-V 系列 | 面壁 OpenBMB / 清华 | 2.6（2024）→ 4.0（2025-08）→ 4.6 | 手机端 GPT-4V 级 MLLM | 2.6 ≈ 8B；4.0 = 4.1B（SigLIP2-400M + MiniCPM4-3B）；4.6 = 1.3B；MiniCPM-o 为全模态（含语音） |
| SmolVLM | Hugging Face | 2B（2024-11）→ 256M/500M（2025-01） | 极小型 VLM，可浏览器/手机跑 | 256M 号称世界最小 VLM；用 93M SigLIP base；iPhone 15 实测实时摄像头推理 |
| Apple 端侧多模态 | Apple | 2024–2026 | OS 级视觉智能 | Visual Intelligence（相机/屏幕理解）、Foundation Models 框架开放端侧基座模型 |

> 区分提醒：[[多模态 GUI 理解与 UI Grounding 学习笔记]] 讲「看懂屏幕并定位可点元素」的 grounding 算法；本表只列 VLM「理解图像/视频内容」的能力本身。

## 四、2025–2026 进展（广度速览）
| 方向 | 关键事实（核实） | 含义 |
|------|----------------|------|
| 更小更多模态 | SmolVLM 压到 256M；MiniCPM-V 4.6 进一步到 1.3B | 端侧 VLM 尺寸门槛持续下探，千元机可及 |
| 视觉 token 压缩成共识 | SmolVLM pixel-shuffle（16× 压缩）、MiniCPM 3D-Resampler、MobileVLM LDPv2 | 决定端侧能否实时跑通的关键工程杠杆 |
| Apple 端侧多模态落地 | iOS 26 Visual Intelligence 扩展至「屏幕内容」理解；Foundation Models 框架向第三方 App 开放端侧基座模型 | 多模态从「App 内能力」升级为「OS 一等公民」 |
| 端侧视觉理解进入产品 | Pixel Gemini Nano（<3B 多模态，Pixel 9+）、各厂商相册/相机理解 | 隐私内处理成为旗舰卖点 |
| MoE 提效 | 小型 VLM 用 MoE 提效的讨论与探索增多（如 MoE-LLaVA 思路） | 具体 2025–2026 端侧 MoE VLM 量产型号待核实 |

## 五、端侧约束与对 OS PM 的意义
在手机上跑 VLM，硬件约束远比云端严苛：**内存带宽**决定视觉编码器与 LLM 间搬运特征的瓶颈；**NPU 吞吐**上限了每秒 token；**KV Cache** 随上下文线性增长，长截图/多图会迅速吃满内存（见 MiniCPM-V CookBook 对设备内存的建议，6–8GB 起步）；**分辨率/视觉 token 数**则直接拖慢首响时间（详见 [[移动端 NPU 与推理编译栈 学习笔记]] 与 [[端侧大模型推理 学习笔记]]）。量化是端侧落地的硬门槛，见 [[端侧模型量化 学习笔记]]。

对 OS PM 而言，端侧 VLM 不该只是「某个 App 的模型」，而应被当作**系统级感知能力**来规划：屏幕理解、相册检索、相机实时助手、无障碍读屏都能共用同一套本地视觉理解。它和 [[Apple Intelligence 端侧架构 学习笔记]] 的端侧基座模型、[[Apple Intelligence 与 App Intents]] 的动作闭环、以及 [[端侧意图框架 学习笔记]] 的「感知→意图」链路天然咬合。把视觉理解放到端侧，意味着隐私数据（照片、截图、摄像头）不出设备，也意味着无网络可用时能力不降级——这是 OS 级体验差异，而非功能点差异。

## 待解问题（深度留白）
- [ ] 端侧 VLM 与 grounding 模型（[[多模态 GUI 理解与 UI Grounding 学习笔记]]）是共用一个 VLM 还是独立小模型？功耗/延迟如何权衡？
- [ ] 2025–2026 真有量产落地的「端侧 MoE VLM」吗？具体型号、激活参数量、NPU 适配方案是？（待核实）
- [ ] 各模型「手机可跑」的精确门槛（RAM / NPU TOPS / 量化位宽）口径不一，哪个数字可信？见下方待核实清单（待核实）
- [ ] 高分辨率长截图下，视觉 token 压缩会不会丢 UI 细节？与 [[Context Engineering 学习笔记]] 如何配合？
- [ ] 端侧 VLM 的「知识密度定律（Densing Law）」能否持续？小模型能力上限在哪？
- [ ] Apple 端侧多模态与第三方 App（[[Apple Intelligence 与 App Intents]]）的调用边界、隐私沙箱如何设计？
- [ ] 视觉理解 + 语音（[[语音交互与端侧 ASR TTS 学习笔记]]）+ 意图框架三者如何编排成端侧 Agent？见 [[端侧意图框架 学习笔记]]
- [ ] 多模态与纯语言 SLM（[[端侧小语言模型 SLM 生态 学习笔记]]）是否应共享同一套端侧推理栈？

## 附：来源清单
| 来源名 | 类型 | 日期 | 真实 URL |
|--------|------|------|----------|
| MiniCPM-V iOS 部署（CookBook） | 官方文档 | 2024–2025 | https://opensqz.github.io/MiniCPM-V-CookBook/site/zh/v4.6/demos/ios.html |
| MiniCPM-V 4.0 开源公告 | 博客（阿里云开发者） | 2025-08 | https://developer.aliyun.com/article/1676186 |
| SmolVLM 256M/500M 发布 | 官方博客 | 2025-01 | https://www.huggingface.co/blog/zh/smolervlm |
| SmolVLM 技术报告 | 论文 arXiv:2504.05299 | 2025 | https://arxiv.org/abs/2504.05299 |
| Qwen2.5-VL 发布（央广网） | 新闻 | 2025-01-28 | https://tech.cnr.cn/techph/20250128/t20250128_527056299.shtml |
| Qwen2.5-VL 家族技术解析 | 博客 | 2025 | https://blog.csdn.net/m0_47999117/article/details/158849558 |
| InternVL2 官方博客 | 官方博客 | 2024-07-02 | https://internvl.github.io/blog/2024-07-02-InternVL-2.0 |
| InternVL2-1B 模型卡 | 模型卡 | 2025-04 更新 | https://modelscope.cn/models/OpenGVLab/InternVL2-1B |
| MobileVLM V2 论文 | 论文 arXiv:2402.03766 | 2024-02 | https://arxiv.org/abs/2402.03766 |
| MobileVLM 代码仓库 | GitHub | 2024 | https://github.com/Meituan-AutoML/MobileVLM |
| Apple iOS 26 / Apple Intelligence | 官方新闻室 | 2025-06 | https://www.apple.com/newsroom/2025/06/apple-elevates-the-iphone-experience-with-ios-26/ |
| Apple Intelligence 新能力（含 Foundation Models 框架） | 官方新闻室 | 2025 | https://nr.apple.com/DW5c5S0Oy8 |

## ⚠️ 待核实清单
- **MiniCPM-V 2.6 参数量口径不一**：有来源称「约 2.6B」，官方 GGUF 标注为「8B」——本笔记采用官方 GGUF 的 8B（含视觉编码器与投影器）。若仅指 LLM 部分则约 2.6B，待核实。
- **端侧可跑门槛数字冲突**：不同测评的 RAM 最低值、量化位宽、tok/s 差异很大（如 MiniCPM-V 4.0 有「4GB RAM 可跑」与「≥6GB 推荐」两种说法），本笔记未采信具体跑通数字，需以具体机型的实测为准。
- **2025–2026 端侧 MoE VLM 量产型号**：MoE 提效是明确趋势，但具体已落地机型/型号未在本轮搜索中确认到可靠一手来源，标「待核实」。
- **Apple 端侧多模态基座模型的具体参数量/模态范围**：官方以「端侧 foundation model」统称，未公开细粒度规格，本笔记只确认「Visual Intelligence + 屏幕理解 + 开放给第三方」的事实，不留编造数字。
- **Qwen2.5-VL 规格**：原始发布 3B/7B/72B，32B 于 2025-03 增补；各源对「总参数量」写法不一（如 3B 实为 3.75B），以官方模型卡为准。

#标签/手机AI #标签/端侧多模态 #标签/VLM
