---
title: AI 产品的可访问性 UX for AI 学习笔记
tags:
  - accessibility
  - inclusive-design
  - a11y
  - ai-product-ux
  - pm-decision
  - wcag
  - regulatory-baseline
created: 2026-10-06
source: "WebSearch/WebFetch 核实 + 公开资料"
---

> 一句话心智模型：**对 AI 产品来说，可访问性（a11y）不是上线后的合规补丁，而是"AI 输出是否人人可用"的基线 UX 责任——读屏能读、替代模态能补、包容设计能兜底、监管能达标。**

区别于 [[无障碍 Accessibility 与 GUI Agent 同源技术栈 学习笔记]]（那是 a11y tree / AT-SPI / TalkBack 的**技术栈广度**）；本篇只站在 **PM 视角**：AI 功能如何做到人人可用，是产品责任而非工程细节。与 [[负责任 AI 与 AI 产品伦理落地 学习笔记]]（RAI 框架）、[[AI 产品的可解释性 UX 与归因展示 学习笔记]]（可解释性这一专门维度）、[[AI 产品需求定义与 Agent 设计规范 学习笔记]]（PRD 一级基线需求）互补。

## 广度覆盖

| 主题 | 定义 | 分类 | 主流方案 | 2025-2026 进展 | 代表产品（厂商 / 规范） |
|---|---|---|---|---|---|
| 什么是 AI 产品可访问性 | AI 功能（生成文本/图像/语音/自主 Agent）对残障与情境受限用户同样可用；把无障碍作为 AI 产品的**基线 UX** 而非补丁 | — | 在生成管线内嵌 a11y 检查，而非发布后补救 | WCAG 2.2（2023-10 W3C 推荐）已成 2025-2026 事实基线；AI 流式输出/生成图表/自主 Agent 尚无现成 WCAG 条款 | WCAG 2.2；EN 301 549 v3.2.1 |
| 障碍分类（四维） | 按 WCAG 四原则（可感知/可操作/可理解/健壮）重排为 AI 专属场景 | 视觉（盲/低视力）· 听觉（聋/重听）· 肢体运动 · 认知（阅读障碍/ADHD/脑损伤） | 多模态输入输出、可预测交互、简化语言 | 认知可访问性被 WCAG 2.2 重点补强（目标尺寸、专注不遮挡、一致帮助） | — |
| 输出可读屏（AI 文本/图像对读屏兼容） | 读屏解析 DOM 而非视觉；AI 流式文本、AI 生成图、canvas/自定义组件常对 VoiceOver/NVDA 静默 | 流式文本、AI 图像、动态注入 UI | 语义 HTML + ARIA live regions 播报动态内容；VLM 生成 alt text；键盘焦点管理 | WCAG 2.2 新增 2.4.11 Focus Not Obscured（最小）、2.5.8 Target Size（最小 24×24px） | Google Gemini in TalkBack（"Ask Gemini" 读屏图像描述）；Apple VoiceOver；NVDA/JAWS |
| 替代模态输出（语音/字幕/文本互转） | 同一信息以多种模态可达：文本↔语音↔字幕↔转录 | 实时字幕、实时转录、语音合成、可朗读 UI | 实时字幕/转录管线；视觉转录可调字号/语速；上下文感知模态建议（嘈杂环境提示用文本） | 2025-2026 厂商实时字幕/转录成标配，并向"情绪/语气标注"演进（Expressive Captions 类） | Google Live Caption / Live Transcribe；Otter.ai；Zoom/Teams 字幕 |
| 包容性 / 认知可访问设计 | 为"想象中的标准用户"以外的人设计核心交互；简化语言、渐进披露、透明解释建立信任 | 简化模式、渐进披露、清晰反馈、输入替代（文本/手势/语音） | "Simplify" 模式重跑 prompt 用 Plain Language；并行输出流（文本同时给音频）；说话人/置信度标签 | WCAG 2.2 强调认知可访问（一致帮助 3.2.6）；XAI 与 a11y 交汇：屏幕阅读器用户也需能核心理由 | Microsoft Immersive Reader；Inclusive Design Patterns（Uxcel/Incluu 类指南） |
| 监管基线（合规即 UX） | 无障碍从"合规勾选"变为 AI 合规的硬约束 | WCAG 2.2 AA · EAA · EU AI Act · ADA/Section 508 · UK EqA | 把 a11y 检查写入 CI/CD；合规率作 KPI；真实残障用户参与测试 | EAA 2025-06-28 生效；EU AI Act Art.16(l) 把可访问性接入 AI 监管；Digital Omnibus 延后高风险至 2027/2028 | EAA(Dir.2019/882)·EN 301 549；EU AI Act Reg.2024/1689；ADA Title III；Section 508 |

### 厂商 AI 无障碍实践速览（2025-2026）
- **Google**：Live Caption / Live Transcribe / Look to Speak；Project Euphonia（多样语音识别）；Gemini 接入 Android TalkBack（"Ask Gemini" 读屏图像描述 + 追问）；Project Astra（实时视觉解读，面向智能眼镜）。
- **Microsoft**：Seeing AI（33 语言，描述世界/读文本/识别物体，iOS+Android）；Immersive Reader（读写障碍辅助）；"AI for Accessibility" 项目扶持初创。
- **Apple**：VoiceOver / Magnifier / Braille Access（盲文记事）；2025-05 发布 **Accessibility Nutrition Labels**（App Store 标注支持的无障碍特性）；Accessibility Reader（阅读模式）。
- **Be My Eyes**：Be My AI（接 OpenAI GPT-4，拍照即获视觉描述，免等志愿者）。
- **其他**：OrCam（可穿戴视觉辅助）、Ray-Ban Meta 眼镜（Detailed Responses 实时描述）、Proloquo2Go（AAC 沟通）。

### 关键监管节点（核实）
- **WCAG 2.2**：W3C 推荐于 2023-10，仍为 2025-2026 事实基线；新增 9 条成功标准（含 2.5.8 目标尺寸、2.4.11 专注不遮挡、3.2.6 一致帮助）。
- **EAA（Directive 2019/882）**：2025-06-28 起适用于欧盟 B2C 数字产品/服务；通过 EN 301 549 v3.2.1 映射到 WCAG 2.1 AA。
- **EU AI Act（Reg. 2024/1689）**：Art.16(l) 要求高风险 AI 系统符合 EAA + Web Accessibility Directive（2016/2102）——把既有无障碍法"拉进"AI 监管；AI 素养 Art.4 自 2025-02-02 生效。
- **Digital Omnibus（Reg. 2026/1744）**：将 Annex III 独立高风险系统的 Art.16 可访问性义务延至 **2027-12-02**，Annex I 产品嵌入式延至 **2028-08-02**；但 Art.50(5) AI 披露的可访问性自 **2026-08-02** 已适用。
- **美国**：ADA Title III（法院延展至网站/应用）、Section 508（联邦）、CVAA；DOJ 要求政府网站 2026 前达 WCAG 2.1 AA（行业事实基准）。

## 深度盲区（留给 Ethon 补充）

- [ ] WCAG 2.2 没有覆盖流式 AI 文本 / AI 生成图表无预生成 alt / 自主 Agent / 概率性输出——在没有既定标准时，PM 如何定内部验收基线？
- [ ] "AI 生成内容的可访问性"责任归属：模型方、平台方、还是产品方？在端侧 OS（如 Android）上责任边界怎么划？
- [ ] 用 VLM 自动生成 alt text / 字幕能否作为正式合规交付物，还是只能作 draft 需人工复核？（幻觉与准确率风险）
- [ ] 认知可访问性如何量化进 AI 功能度量体系（简化模式采纳率？可读性评分？），与 [[数据飞轮与 AI 产品度量 学习笔记]] 怎么接？
- [ ] 厂商 AI 无障碍能力（Gemini in TalkBack、Be My AI 等）多为闭源；作为 OS PM 如何纳为端侧产品能力而不绑死单一厂商？
- [ ] EU AI Act Art.16(l) 延后到 2027/2028，但 EAA 已 2025 生效——是否在 EU 出货的产品应现在就按"双重合规"做，而非等？

## 附：来源清单
1. Mintec — Synthetic Media, Real Accessibility Gaps: Auditing AI-Generated Content for WCAG 2.2（2026 合规框架）
2. Institute of Product Management — AI Product Accessibility: Building AI Features Everyone Can Use
3. Incluu — Inclusive Design Patterns for AI Interfaces
4. Atos — Top ten steps to embrace accessible Gen AI at the workplace
5. Level Access — AI and Assistive Tech: Key Advancements in Accessibility
6. MyVision Oxfordshire — AI Accessibility Features for Visually Impaired People
7. Connsense Report — Accessible Innovations in Technology – 2025 Updates（Apple/Microsoft 2025 更新）
8. wcagc.com — AI Act accessibility rules: how they connect to the EAA（Art.16(l)、Digital Omnibus 时间点）
9. Mintec — The EU AI Act Is Now Enforceable: Why Accessibility Became an AI Compliance Issue（2026-08-02 通用阶段）
10. sota.io — European Accessibility Act + EU AI Act Dual Compliance Guide（EAA 范围与 WCAG 2.1 AA 映射）
11. Web Developer Guide — Accessibility for AI-Built Sites（WCAG 2.2 AA、axe-core in CI、prompt contract）
12. Uxcel — Conversational UX & Multimodal Interfaces（读屏兼容对话界面）

## ⚠️ 待核实清单
- 多家博客引用的行业软数字（"94.8% 网站不达标""70% 新 AI 聊天机器人有障碍""2022→2026 无障碍诉讼 +300%""2024 年 8,800+ ADA 诉讼""合成媒体 2024 年 $5B → 2033 年 $48B，AI 视频占 34%"）均来自单一厂商博客，**待核实**第三方权威数据。
- "WHO 全球 13 亿残障人士 / 美国成人 26%"为广泛引用的官方口径，但本篇未逐条溯源，**待核实**原始出处。
- "WCAG 3.0 工作草案 2026 流通"见于部分来源，W3C 进度以官方为准，**待核实**。
- 各厂商功能清单（如 Seeing AI "33 语言"、Apple 2025-05 发布 Accessibility Nutrition Labels）取自二手汇总，发布时间与范围**待核实**官方公告。
- EU AI Act / Digital Omnibus 的具体生效日期（2026-08-02 通用阶段、2027-12-02 / 2028-08-02 高风险延后）依监管文本，落地口径随成员国执行可能变化，**待核实**最新官方文本。

#标签/可访问性 #标签/包容性设计 #标签/AI产品UX #标签/WCAG #标签/监管基线
