---
title: 操作系统原生 AI 功能图谱
tags:
  - 知识拓展
  - OS
  - 端侧AI
  - AI功能
created: 2026-09-19
source: WebSearch（Android/Gemini、Apple Intelligence、HarmonyOS NEXT 小艺 公开资料）2026-09-19
---

# 操作系统原生 AI 功能图谱

**心智模型：各 OS 的"原生 AI 功能"是端云协同的产品功能层清单——端侧负责即时/隐私/离线，云侧负责复杂推理与知识广度，产品经理比拼的是"把哪些能力放端侧"的取舍艺术。**

## 1. 定义与边界

"操作系统原生 AI 功能"指由 OS 厂商（Google / Apple / Huawei）**内建在系统层、面向终端用户、开箱即用**的 AI 能力。区别于 [[端侧意图框架 学习笔记]] 讲的"意图总线架构"、[[Apple Intelligence 端侧架构 学习笔记]] 讲的"推理栈架构"——本篇只盘**用户能直接点到的功能**，不重复架构细节。

## 2. 功能分类（四桶）

| 分类 | 核心目的 | 典型功能举例 |
|---|---|---|
| **创作生成类** | 生成文字/图像/表情 | Magic Compose、Pixel Studio、Genmoji、Image Playground、小艺修图、小艺帮写 |
| **理解摘要类** | 读/懂/提炼信息 | Chrome 摘要、通知摘要、相册清理 Clean Up、小艺文档摘要/思维导图、相册清理 |
| **实时交互类** | 当下对话/翻译/感知 | Gemini Live、Circle to Search、通话翻译、实时字幕、小艺看世界、Live Translation |
| **系统智能类** | 融入系统、自动化 | Smart Reply、通话筛查、Siri 屏幕感知、小艺帮接/帮记、A2A 智能体协作、Foundation Models 开放 |

## 3. 主流方案对比表（功能 · 平台 · 端侧/云侧 · 状态）

| 功能 | 平台 | 端侧/云侧 | 状态 |
|---|---|---|---|
| Circle to Search（圈选搜） | Android/Gemini（与三星共研） | 端侧手势+云侧 Lens/AI Mode | 已上线，Android 16 加 AI Mode+游戏助手 |
| Magic Compose（短信改写） | Android/Gemini Nano | 端侧（Nano） | 已上线 Pixel 8 Pro+/S24+ |
| Gemini Live（连续语音对话） | Android/Gemini | 云侧为主，记忆层可选 | 已上线，折叠屏/手表扩展中 |
| Pixel Studio（文生图） | Android/Pixel | 端侧生成 | 已上线 |
| 实时字幕 / 通话翻译 | Android | 端侧 | 已上线多年 |
| Writing Tools（写作工具） | iOS/Apple Intelligence | 端侧为主 + PCC 兜底 | iOS 18.1 起已上线 |
| 通知摘要 / 邮件优先级 | iOS/Apple Intelligence | 端侧为主 | 已上线 |
| Clean Up（相册清理） | iOS/Apple Intelligence | 端侧 | 已上线，iOS 19 增强为 Clean Up Pro |
| 照片/Genmoji/Image Playground | iOS/Apple Intelligence | 端侧生成 + 云增强 | 已上线，iOS 19 开放 API |
| 新架构 Siri（屏幕感知/多步） | iOS/Apple Intelligence | 端侧 LLM + PCC | iOS 19（2026.9 GA）逐步落地 |
| Live Translation（通话实时翻译） | iOS/Apple Intelligence | 端侧 | iOS 19 起（A17 Pro+） |
| 小艺圈选 / 拖给小艺 | HarmonyOS NEXT 小艺 | 端侧 13 亿 + 云侧 124 亿 | 已上线 |
| 小艺看世界（视觉智能体） | HarmonyOS NEXT 小艺 | 端云协同 | 已上线（Pura 80 等） |
| 小艺修图 / 简报 / 帮接 / 帮记 | HarmonyOS NEXT 小艺 | 端云协同 | 已上线 |
| A2A 智能体协作 / HMAF 2.0 | HarmonyOS NEXT 小艺 | 端云协同 | HDC2026 发布，演进中 |

## 4. 2025–2026 进展（公开资料核实）

- **Android / Gemini**：Android 15 起把 Gemini 织入核心系统；Android 16 开放第三方 App 直连 Gemini 的 API。Gemini 已取代 Google Assistant 成为旗舰默认体验。Pixel 9+（Tensor G4）跑 Gemini Nano 2 端侧模型，Google 宣称约 68% 常见助手查询可本地完成（待核实）。Circle to Search 在 Android 16 加 AI Mode（对话式深挖）与游戏内辅助；Gemini Live 扩展至折叠屏外屏、相机共享与 Wear OS 6 手表。
- **iOS / Apple Intelligence**：2024-10-28 随 iOS 18.1 首发（仅 iPhone 15 Pro/16 + 美英语言）。iOS 18.4 加 ChatGPT 兜底，iOS 18.6 加 Visual Intelligence。**iOS 19（WWDC 2025 发布、2026.9 GA）把端侧 Apple Foundation Models 开放给第三方开发者**（Foundation Models 框架 + LoRA Adapters + PCC 兜底）——被认为是近年最重要的开发者平台变化之一。EU 因 DMA 延迟，至 2025 年底核心功能全量上线。
- **HarmonyOS NEXT 小艺**：系统级智能体"中控大脑"，端侧 13 亿参数 + 云侧 124 亿参数大模型，接入 DeepSeek-R1（2025.2 Beta）。HDC2026 发布 Harmony Intelligence 向 Agent 架构演进、HMAF 2.0、意图即服务；小艺已接入 2000+ 鸿蒙智能体、2100+ 系统能力、500+ 伙伴 Skills。

## 5. 点到为止（广度留白）

- 各 OS 功能"端侧占比"差异巨大：Apple 主打 on-device-first + PCC，Google 端侧只跑 Nano 轻量，华为端侧 13 亿小模型+云 124 亿——**同样的"AI 功能"背后端云切分策略完全不同**。
- 国内安卓厂商（小米/OPPO/vivo/荣耀）对齐 Google 原生功能到什么程度，本篇未展开（见 [[安卓厂商意图识别破局策略]]）。
- 系统 Agent 平台编排能力另见 [[OS 级系统 Agent 与跨应用自动化 学习笔记]]；端侧推理底座见 [[端侧大模型推理 学习笔记]]、[[端侧多模态 VLM 学习笔记]]；苹果接口层见 [[Apple Intelligence 与 App Intents]]、[[HarmonyOS 元服务 学习笔记]]。

- [ ] 各 OS 原生 AI 功能的**实际端侧推理占比**有没有权威 benchmark（而非厂商宣称）？
- [ ] 国内安卓厂商（小米/OPPO/vivo/荣耀）对 Circle-to-Search / 系统级写作工具的**对齐进度与差异化**？
- [ ] 这些原生 AI 功能的**用户采纳率 / 日活渗透率**公开数据？
- [ ] iOS 19 开放端侧 Foundation Models 后，第三方 App 的**真实调用规模与功耗表现**？
- [ ] 鸿蒙 HMAF 2.0 的 A2A 协作与苹果 App Intents / Google AppFunctions 的**能力边界对照**？

## 附：来源清单

1. SwitchToAndroid — *Google Gemini AI on Android: Everything It Can Do in 2026*（Gemini 端云模型分层、Nano 2 本地占比）
2. The Verge — *Android's Circle to Search gets AI and gaming upgrades*（Android 16 AI Mode、Gemini Live 折叠屏/手表）
3. MakeAnAppLike — *Apple Intelligence in 2026 / iOS 19 Foundation Models*（iOS 19 开放端侧模型给开发者）
4. Mylistingo / StepPhase — *iOS 19 WWDC 2026、Apple Intelligence 2026 落地*（对话式 Siri、Clean Up Pro、EU 进度）
5. 华为开发者联盟 / 中国日报 — *HarmonyOS NEXT 小艺、HDC2026 HMAF 2.0*（小艺端云参数、Agent 架构演进）
6. 百度百科「华为小艺」词条 — 小艺 13 亿端侧 / 124 亿云侧参数、接入 80+ 应用智能体

## ⚠️ 待核实清单

- Google 宣称 Gemini Nano 2 "约 68% 常见查询本地完成" 缺乏独立验证（来源为媒体转述）。
- iOS 19 部分功能（对话式 Siri 多步执行、Live Translation 通话翻译）为发布会演示 / 媒体预测，GA 实际范围**待核实**。
- 个别来源称 Apple 有 "$4.99/月 Pro AI 云增强订阅"，与苹果一贯口径冲突，**存疑待核实**。
- 鸿蒙端侧 13 亿 / 云侧 124 亿参数、接入 2000+ 智能体等为厂商/媒体口径，精确数字以官方为准。
- 部分 EU/iOS 时间线混合了媒体二手报道，DMA 实际落地节奏**待核实**。

#标签/手机AI智能体/操作系统AI功能
