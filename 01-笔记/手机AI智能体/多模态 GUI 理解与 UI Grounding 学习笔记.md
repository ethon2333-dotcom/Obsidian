---
title: 多模态 GUI 理解与 UI Grounding 学习笔记
tags:
  - 手机AI智能体
  - GUI理解
  - 端侧Agent
  - 屏幕理解
  - UI Grounding
created: 2026-08-15
source: WebSearch 核实（SeeClick / OS-Atlas / UGround / UI-TARS / OmniParser / Ferret-UI / ScreenSpot-Pro 等论文与官方博客，2025–2026）
---

# 多模态 GUI 理解与 UI Grounding 学习笔记

## 学习定位
本文是「看懂屏幕」这一感知/grounding 算法侧的主题种子笔记，作为 [[工业级 GUI Agent 架构（VLM+无障碍树）]] 的「前置感知层」互补材料。那篇讲「VLM + 无障碍树双引擎如何编排成一个能干活的系统」，本文只聚焦更底层的一件事：如何让模型把一句自然语言指令映射到屏幕上的具体坐标/区域（grounding 本身）。广度优先，深度盲区以 `- [ ]` 列出，留给 Ethon 后续深耕。相关脉络见 [[手机AI智能体知识库]] 与 [[意图框架·跨体系索引 MOC]]。

> **心智模型：UI Grounding 就是把「点那个搜索框」翻译成屏幕上的 (x, y) 或 bounding box——它是所有 GUI Agent 落子的「眼睛」，眼睛不准，脑子再聪明也点错。**

## 一、概念定义（术语铺广度）

| 术语 | 定义（核实口径） | 代表 / 备注 |
|---|---|---|
| Screen Understanding（屏幕理解） | 对 UI 截图的多模态语义理解，涵盖 OCR、布局、元素功能、整屏摘要 | Screen2Words（UIST 2021）做整屏语言摘要 |
| UI Element Detection（UI 元素检测） | 把截图解析成结构化元素列表（可交互区域、图标、文本及其位置） | 偏 CV 检测任务；OmniParser 即「屏幕解析」思路 |
| Grounding（视觉 grounding） | 将自然语言指代表达（referring expression）映射到屏幕上的精确坐标/框 | 本文核心；GUI grounding 区别于通用 REC/RES |
| Referring Expression（指代表达） | 「蓝色的登录按钮」「搜索框右边的图标」这类描述元素的自然语言 | UGround 用 MLLM 大规模合成 RE 做训练数据 |
| VLM-based Grounding | 用视觉语言模型直接从截图输出坐标，不再依赖 HTML/无障碍树 | SeeClick、UGround、OS-Atlas、UI-TARS 主线 |
| DOM / 无障碍树对齐 | 把视觉检测结果与结构化视图树（accessibility tree / view hierarchy）对齐 | 与纯视觉路线相对；见 [[工业级 GUI Agent 架构（VLM+无障碍树）]] |

## 二、核心技术栈（算法侧做法与取舍）

| 技术路线 | 做法 | 优点 | 代价 / 局限 |
|---|---|---|---|
| OCR + 布局分析 | 先抽文字+版面，再定位 | 轻量、可解释、端侧友好 | 看不懂图标/纯图形控件，语义弱 |
| UI 元素检测（检测模型） | YOLO/Det 类模型框出可交互区+图标 | 快、可纯视觉、易上端侧 | 只给框不给语义，需额外 caption |
| Set-of-Mark（SoM） | 用 SAM/SEEM 先分割并打字母/数字标记，再交给 LMM 指认 | 零样本释放 GPT-4V grounding；空间信息显式 | 依赖外部分割模型，标记数受限，多步延迟 |
| VLM-based Grounding（端到端） | 截图 + 指令直接出坐标/框 | 统一、可学、泛化好 | 高分辨率小目标难；算力开销大 |
| DOM / 无障碍树对齐 | 视觉结果与视图树节点对齐，借结构化语义 | 语义精确、可触发原生 API | 需系统权限、跨平台不一致、无障碍树常有缺口 |

## 三、代表模型 / 方法（核实存在与年份）

| 模型 / 方法 | 机构 | 年份 | 定位 | 规模 / 底座 |
|---|---|---|---|---|
| Ferret-UI | Apple | 2024（ECCV 2024） | 移动 UI 理解 MLLM，referring/grounding/reasoning | Gemma-2B / Llama-3-8B，anyres |
| SeeClick | 上海AI Lab 等 | 2024（ACL 2024） | 首个纯截图视觉 GUI Agent + ScreenSpot 基准 | 基于 Qwen-VL |
| UGround | OSU × Orby AI | 2024（ICLR 2025 Oral） | 通用视觉 grounding，"Web→Any" 零样本泛化 | 初版 LLaVA；V1 有 2B/7B/72B（Qwen2-VL） |
| OS-Atlas | 上海AI Lab / SJTU / HKU / MIT | 2024（ICLR 2025 Spotlight） | 基础动作模型，grounding + OOD 泛化 | 7B/4B（Qwen2-VL），1300万+ GUI 元素语料 |
| OmniParser | Microsoft | 2024（V2 于 2025/02） | "屏幕解析"工具：检测+图标语义 caption | YOLO 检测 + BLIP-2/FLARE 描述 |
| UI-TARS | ByteDance Seed | 2025/01（1.5 于 2025/04） | 原生端到端 GUI Agent，感知/动作/推理/记忆一体 | 2B/7B/72B，原生 agent 路线 |
| Ferret-UI Lite | Apple | 2025（arXiv 2509.26539） | 端侧小模型 GUI Agent 经验总结 | 3B，SFT + RLVR（GRPO） |
| AgentCPM-GUI | 清华 THUNLP × 面壁 | 2025（月份待核实） | 端侧中文 APP GUI Agent | 8B，基于 MiniCPM-V，覆盖 30+ 中文 APP |

## 四、代表数据集与基准（核实存在）

| 数据集 / 基准 | 年份 / 会议 | 内容 | 用途 |
|---|---|---|---|
| RICO | 2017（UIST） | 9,772 个 Android App、72,219 屏、含 view hierarchy | 移动 UI 数据驱动研究奠基 |
| Screen2Words | 2021（UIST） | 22,417 屏、112k+ 人类写的整屏摘要 | 屏幕摘要 / screen understanding |
| WebUI | 2023（CHI，Best Paper） | 网页 UI + 语义，41,970 图 | 增强视觉 UI 理解 |
| ScreenSpot | 2024（随 SeeClick） | 移动/桌面/网页 grounding 首基准 | GUI grounding 评测 |
| ScreenSpot-Pro | 2025（arXiv 2504.07981） | 23 App、5 行业、3 OS、1,581 高分辨率指令 | 专业高分辨率 grounding（难） |
| ScreenSpot-V2 / ScreenSpotPro | 2024–2025 | ScreenSpot 增强版 | 小模型 grounding 常用榜 |

## 五、2025–2026 进展（广度速览）

| 进展方向 | 关键事实（核实） | 含义 |
|---|---|---|
| 从「框架」到「原生模型」 | UI-TARS 指出：把 GPT-4o 套 prompt 的框架范式，正被端到端原生 agent 模型取代（感知/推理/动作/记忆一体） | grounding 被内化为模型能力，而非外挂模块 |
| 小目标 / 高分辨率成主战场 | ScreenSpot-Pro 最佳模型仅 18.9%（OS-Atlas-7B）；Ferret-UI Lite(3B) 用 zoom-in 第二遍精修把 ScreenSpot-Pro 做到 53.3% | 端侧 3B 反而能在某些高难榜超 7B，靠的是「视觉工具」而非堆参数 |
| 端侧小模型可行化 | Ferret-UI Lite 3B、AgentCPM-GUI 8B 证明手机端可跑 grounding+导航 | 端侧 GUI 理解从「不可能」到「可用」，但长程任务仍有推理天花板 |
| 「先思考再行动」 | UI-TARS-1.5 加入 System-2 推理 + RL，推理时随步数扩展（inference-time scaling） | grounding 准度提升靠推理闭环，不只是视觉 |
| 专业软件场景被打开 | ScreenSpot-Pro + ScreenSeekeR（分层视觉搜索，无需重训把 18.9%→48.1%） | 纯 direct grounding 不够，需「规划者+定位器」协作 |

## 六、端侧 vs 云端：grounding 可行范围（产品视角）

| 维度 | 端侧可行范围 | 云端更优范围 |
|---|---|---|
| 模型规模 | 3B–8B（Ferret-UI Lite / AgentCPM-GUI 佐证） | 72B+（UGround-V1-72B、UI-TARS-72B） |
| 任务类型 | 单屏元素定位、轻量导航、无障碍辅助 | 长程多步、跨 App、专业软件（ScreenSpot-Pro 类） |
| 精度 | 通用榜接近 7B 云端；高难小目标需 zoom-in 补偿 | 直接出坐标更稳，但延迟/成本/隐私代价高 |
| 隐私 | 截图不出端，天然隐私友好 | 截图上传，敏感屏风险 |
| 触发前置 | 是 GUI Agent 的「眼睛」前置条件，见 [[端侧意图框架 学习笔记]] | 可作为端侧眼睛的云端兜底 |

## 对 OS PM 的意义
对 Android OS PM 而言，UI Grounding 是「系统能否真正看懂用户屏幕」的感知地基：端侧 3B–8B 模型已能在通用榜逼近云端 7B，意味着**把 grounding 放在端侧在功耗/隐私上更优，但专业软件、长程任务等高难场景仍需云端兜底**。落地时要把 grounding 精度当作**触发 GUI Agent 的前置条件**——眼睛不准直接导致误操作，因此需设置信度阈值与确认机制（关联 [[App Intent 的核心作用]] 与 [[Confirmation UI 分级与产品责任边界]] 思路）。端侧推理的工程约束详见 [[端侧大模型推理 学习笔记]]，而 agent 如何组织上下文则可参考 [[Context Engineering 学习笔记]]。

## 待解问题（深度留白）
- [ ] ScreenSpot-Pro 上 3B 端侧模型（53.3%）为何能超过部分 7B？zoom-in 第二遍精修的工程成本在手机 NPU 上是否可接受？
- [ ] 纯视觉 grounding 与「无障碍树对齐」两条路线，在 Android 真实碎片设备上谁的召回更稳？无障碍树缺口（研究指 60% 屏有未标注元素）如何补？
- [ ] 端侧 8B（AgentCPM-GUI）的中文 APP grounding，跨 App 泛化与隐私边界如何权衡？
- [ ] grounding 置信度如何量化并作为 GUI Agent 的「可操作阈值」？谁来担误点责任？
- [ ] Set-of-Mark 的标记数上限（字母/数字有限）在密集 UI 上是否成为瓶颈？有无替代空间编码？
- [ ] 2025–2026 各家 ScreenSpot-Pro 数字口径差异大（18.9% vs 61.6%），是否因模型规模/版本不同？如何横向可比？
- [ ] grounding 模型训练数据高度依赖网页合成（Web→Any），移动端原生控件（Compose/Flutter/游戏引擎渲染）是否分布外？
- [ ] 端侧 grounding 与「原生平权 API（App Intent）」是互补还是竞争？何时该走原生 API 而非截图点按（见 [[GUI Agent vs 原生 API 产品决策树]]）？

## 附：来源清单

| 来源名 | 类型 | 日期 | 真实 URL |
|---|---|---|---|
| SeeClick (ACL 2024) | 论文 | 2024-01-17 / 2024-08 | https://aclanthology.org/2024.acl-long.505/ |
| OS-Atlas (ICLR 2025 Spotlight) | 论文 / OpenReview | 2024-10-30 / 2025-01 | https://www.openreview.net/forum?id=n9PDaFNi8t |
| UGround (ICLR 2025 Oral) | 论文 / arXiv | 2024-10-07 | https://arxiv.org/abs/2410.05243 |
| UI-TARS (ByteDance Seed) | 论文 / arXiv | 2025-01-21 | https://arxiv.org/abs/2501.12326 |
| UI-TARS-1.5 官方博客 | 官方博客 | 2025-04-17 | https://seed.bytedance.com/zh/blog/bytedance-seed-agent-model-ui-tars-1-5-open-source-achieving-sota-performance-in-various-benchmarks |
| RICO (UIST 2017) | 数据集 / 论文 | 2017 | https://dl.acm.org/doi/10.1145/3126594.3126651 |
| WebUI (CHI 2023) | 数据集 / 论文 | 2023 | https://doi.org/10.1145/3544548.3581158 |
| Screen2Words (UIST 2021) | 论文 | 2021 | https://dl.acm.org/doi/10.1145/3472749.3474765 |
| Set-of-Mark (SoM, arXiv) | 论文 | 2023-10-17 | https://arxiv.org/abs/2310.11441 |
| OmniParser (Microsoft) | 技术报告 / GitHub | 2024（V2 2025-02） | https://arxiv.org/abs/2408.00203 |
| ScreenSpot-Pro (arXiv 2504.07981) | 论文 | 2025-04-04 | https://arxiv.org/abs/2504.07981 |
| Ferret-UI (ECCV 2024) | 论文 | 2024-04-08 | https://arxiv.org/abs/2404.05719 |
| Ferret-UI Lite (arXiv 2509.26539) | 论文 | 2025-09-30 | https://arxiv.org/abs/2509.26539 |
| AgentCPM-GUI (清华×面壁) | 媒体报道 | 2025（月份待核实） | https://news.aibase.com/tw/news/18046 |

## ⚠️ 待核实清单
- ScreenSpot-Pro 准确率口径冲突：论文原文称最佳模型 OS-Atlas-7B 仅 **18.9%**；而 UI-TARS-1.5 博客称其 ScreenSpotPro 达 **38.1%(72B) / 49.6%(1.5-7B) / 61.6%(1.5)**。差异大概率来自**模型规模/版本不同**，此处不给单一数字，需以「规模+版本」对照阅读。
- UGround 的 ScreenSpot 平均准确率有 **73.3%（初版 LLaVA）** 与 **86.3%（V1-7B, Qwen2-VL）** 两档，系不同版本，非矛盾。
- AgentCPM-GUI 的确切发布月份未在可检索来源中确认，标注为 2025（月份待核实）。
- OmniParser V2 具体发布日（2025-02）来自 GitHub 动态，非正式论文，按动态口径记录。
- 「Web→Any 零样本泛化」在移动原生/游戏渲染控件上的分布外表现，未见系统性公开评测，留作待解。

#标签/手机AI #标签/GUI理解 #标签/端侧Agent
