---
title: AI 产品 a11y 落地实操
tags:
  - AI产品
  - 无障碍
  - a11y
  - 合规
  - 读屏测试
  - 产品经理
created: 2026-10-08
source:
  - WebSearch
  - WebFetch
---

# AI 产品 a11y 落地实操

> 心智模型：无障碍不是 AI 产品上线前的「合规补丁」，而是 PM 在定义需求时就该写进 PRD 的**可交付清单**——读屏能读、替代模态能出、监管能过、证据能留。

本篇与 [[AI 产品的可访问性 UX for AI 学习笔记]]（基线 UX 概念）和 [[无障碍 Accessibility 与 GUI Agent 同源技术栈 学习笔记]]（技术栈）**刻意差异化**：这里只给「PM 可执行的操作手册」——测试 SOP、产品化清单、合规检查表与 AI 特有的 a11y 坑，**不重述概念，不重述实现原理**。

互补跳转：合规坐标见 [[AI 监管与合规落地 学习笔记]]；RAI 框架见 [[负责任 AI 与 AI 产品伦理落地 学习笔记]]；需求侧基线见 [[AI 产品需求定义与 Agent 设计规范 学习笔记]]；度量侧见 [[数据飞轮与 AI 产品度量 学习笔记]]。

---

## 一、广度覆盖表（BREADTH > DEPTH）

| 主题 | 定义 | 分类 | 主流方案 / 代表产品 | 2025-2026 进展 | 代表产品 |
|---|---|---|---|---|---|
| **读屏兼容测试 SOP** | 用真实辅助技术（AT）验证 AI 界面可被读屏软件导航、播报、操作 | ① 自动化扫描（axe/Lighthouse/WAVE，仅覆盖约 30–50% 问题）② 人工读屏（NVDA/JAWS/VoiceOver/TalkBack/Narrator）③ 键盘-only 走查 | NVDA（Windows 免费·最常用）、JAWS（企业付费·签核基准）、VoiceOver（mac/iOS 内置）、TalkBack（Android 内置）、Narrator（Win 内置）；Playwright+axe、pa11y 流水线 | EAA 合规要求 EN 301 549 第 9/11 章**必须**用真实 AT 测试（功能表现标准，不只是代码属性）；2026 年测试栈普遍把 axe 设为 critical/serious 阻断 CI、moderate/minor 降级为告警 | axe DevTools、Lighthouse、WAVE、pa11y、NVDA、JAWS |
| **语音 / 替代模态产品化** | 把 AI 输出从「单一视觉文本」转为可听、可说、可多模态的替代呈现，服务视障/听障/运动/认知障碍用户 | ① 语音输入（voice mode）② 视觉→语音描述（VLM 看图说话）③ 语音/视频→文字（实时字幕/转写）④ 端侧离线替代模态（隐私敏感场景） | ChatGPT Advanced Voice Mode、Be My AI（Be My Eyes×GPT-4V）、Microsoft Seeing AI、Google Gemini Live「Guided Vision」（2026-09 Android）、Apple Magnifier Live Recognition（iOS 26，2025-09）、Google Lookout、Envision Glasses | 2026 年调研：约 67% 受访残障网民每周用 AI 工具（2024 仅 30.7%）——AI 正成为「默认无障碍层」，页面被读屏读一次、被模型理解一次 | ChatGPT、Be My Eyes、Seeing AI、Gemini、Apple Magnifier |
| **WCAG 2.2 合规基线** | W3C 2023-10 推荐标准，9 条新成功标准；满足 2.2 AA 即自动满足 2.1/2.0 | 新增关键 SC：焦点不被遮挡 2.4.11、目标尺寸≥24×24px 2.5.8、拖拽需单指针替代 2.5.7、一致帮助 3.2.6、冗余输入 3.3.7、无障碍认证 3.3.8 | axe-core wcag22aa 规则集、Lighthouse a11y 审计、语义化 HTML + `:focus-visible` | 2025–2026 成为事实合规基线；「无 AI 豁免」——AI 生成内容与界面同样适用 | WAI-ARIA 1.2（1.3 草案）、axe、Lighthouse |
| **EAA 欧洲无障碍法案** | Directive (EU) 2019/882，私域数字产品/服务强制无障碍；技术基准 EN 301 549（并入 WCAG 2.1 AA） | 产品类（计算机/OS、自助终端、视听终端）· 服务类（电商、电子通信、视听媒体、银行、交通）· 豁免（微型企服、归档内容、不成比例负担） | EN 301 549 符合性 presumption（Art.15）、CE 标志 + EU 符合性声明、无障碍声明 + 投诉渠道 | **2025-06-28 强制实施**；德国 BFSG 上线数周即现律所私法警告函；过渡期至 2030-06-28（既有服务）、2045（长寿命终端）；罚则因成员国而异（部分上限 €10 万或营收 4%） | 各国市场监管机构（西班牙 AESIA、德国 BNetzA、爱尔兰 NAI 等） |
| **EU AI Act 无障碍条款** | Regulation (EU) 2024/1689：Art.16(l) 要求高风险 AI 系统满足指令 2016/2102 与 2019/882 的无障碍要求（经 EN 301 549 → WCAG 2.1 AA） | 高风险系统（Annex III 就业/教育/信贷/公共服务；Annex I 嵌入式产品）· 通用义务（Art.4 AI 素养、Art.50 披露） | 经引用接入既有无障碍法；高风险系统需把无障碍纳入 QMS + 符合性评估 + CE | Digital Omnibus（Reg 2026/1744）把 Art.16 高风险义务**推迟**：Annex III → 2027-12-02，Annex I → 2028-08-02；但 Art.4/Art.50 已于 2026-08-02 全面适用、可执法 | EU AI Act、EN 301 549、各国 AI 监管局 |
| **AI 特有 a11y 问题** | AI 动态/生成内容引入的传统无障碍盲区 | ① 流式输出 aria-live 播报（token 级流式）② 多模态输出替代（图/音/视频需文本等价）③ 合成媒体字幕与描述（AI 视频/音频无 caption/transcript）④ 动态内容可访问性（SPA 路由、live region、loading 状态） | ASR 字幕（Whisper/Deepgram ~95–98% 需人工校）、VLM 批量生成 alt（GPT-4o/Claude/Gemini）、VTT 字幕 + 音频描述 + 可键盘/读屏播放器、`aria-live="polite/assertive"` | 2026 趋势：合成媒体产量暴涨带来「无障碍债」；主流 AI 视频生成器（Veo/Sora/Kling/Runway/Seedance）**默认不带字幕/描述**；把 a11y 检查前移到生成流水线（失败即拒稿） | Whisper、Deepgram、GPT-4o、Claude、Gemini、Be My AI |

---

## 二、PM 可执行清单（落地 SOP 提炼）

**1. 读屏兼容测试 SOP（每个 AI 功能上线前）**
- [ ] 自动化基线：CI 里跑 axe（wcag2a/2aa/21aa/22aa），critical+serious 阻断合并，moderate/minor 入审计轨迹。
- [ ] 真机读屏三件套：NVDA+Chrome（Windows 主力）、JAWS（企业签核）、VoiceOver（mac/iOS，移动流量高时必测）。
- [ ] 关键走查脚本：Tab 焦点落 skip-link → H 标题层级 → F 表单标签 → 模态 Esc 关闭且焦点回弹 → **动态内容/流式更新用 live region 播报** → 表单错误经 `role="alert"`/`aria-live` 播报。
- [ ] 失败模式红线：图标按钮无 `aria-label`、错误注入 DOM 但无 live region、模态不锁焦点、SPA 路由切换不播报、数据表无行列头。

**2. 语音 / 替代模态产品化清单**
- [ ] 每个 AI 输出通道是否提供「非视觉等价物」（语音播报 / 文本摘要 / 替代描述）。
- [ ] 隐私敏感场景（病历、银行信、证件）优先端侧离线 VLM，避免图像上传。
- [ ] 语音模态需支持打断、免提、与读屏共存（不与 VO/TalkBack 快捷键冲突）。

**3. WCAG 2.2 + EAA + EU AI Act 合规检查表**
- [ ] 产品是否进入欧盟市场 → 触发 EAA（2025-06-28 起新产品即强制）。
- [ ] 是否高风险 AI 系统（Annex III/I）→ 触发 Art.16(l) 无障碍（推迟但 EAA 已先行适用）。
- [ ] 是否通用 AI 功能（聊天/推荐/合成媒体）→ Art.50 披露 + Art.4 AI 素养已可执法。
- [ ] 是否留出「合规证据链」：无障碍声明、扫描报告、读屏测试记录、投诉渠道。

**4. AI 特有 a11y 问题对策**
- [ ] 流式输出：用 `aria-live` 区域承载增量内容，避免逐 token 刷屏式播报（可节流/整段播报）。
- [ ] 合成媒体：生成即跑 a11y 检查，无字幕/alt/transcript 直接拒稿；ASR 字幕人工校首尾 10 秒（AI 转写最易错处）。
- [ ] 多模态输出：任何图/音/视频都配文本等价与音频描述。

---

## 三、深度盲区（待解问题）

- [ ] **流式 token 级播报的「最佳粒度」是什么？** 逐字 `aria-live` 会淹没读屏用户，整段播报又牺牲实时感——有没有行业公认节流/聚合模式？
- [ ] **AI 生成 alt/caption 的「准确性」如何验收？** 自动工具能抓缺失，但语境准确性靠人审，规模化下人力成本怎么压？能否用 eval 指标量化？
- [ ] **EU AI Act Art.16 推迟后，EAA 与 AI Act 的「双重合规」边界在哪？** 一个嵌入 AI 的电商/银行界面，到底按哪条举证最省？
- [ ] **AI overlay（自动无障碍补丁）的真实风险边界？** 多家报告称装了也不防诉，但中小团队仍依赖——哪些坑是 overlay 绝对补不了的？
- [ ] **「AI 作为默认无障碍层」对产品经理意味着什么？** 当盲人用户直接让模型总结页面，页面本身的语义结构（DOM/ARIA）是否仍需为读屏达标？两者证据如何取舍？
- [ ] **语音/多模态替代模态的「可度量采纳率」怎么设？** 参照 [[数据飞轮与 AI 产品度量 学习笔记]] 的采纳/信任衰减指标，a11y 专属北极星该是什么？

---

## 四、来源清单（2025–2026 公开资料）

- WebSearch/WebFetch 核实：European Accessibility Act（Directive (EU) 2019/882，2025-06-28 实施；EN 301 549 并入 WCAG 2.1 AA）—— gov.ie / Central Bank of Ireland / oneaccessibility.com / etrlab.cn / caict.ac.cn
- WebSearch/WebFetch 核实：EU AI Act（Reg (EU) 2024/1689）Art.16(l) 无障碍引用；Digital Omnibus（Reg (EU) 2026/1744）推迟高风险义务；AI Act Service Desk 官方条文
- WebSearch/WebFetch 核实：WCAG 2.2（W3C 2023-10 推荐，9 新 SC）、EAA 测试栈 2026（sota.io）、读屏测试 SOP（mapagam / skillmd / wppoland / lobehub）
- WebSearch/WebFetch 核实：AI 合成媒体 a11y 框架与 WCAG 1.1.1/1.2.1/1.2.2（mintec.co 2026）、生成式 AI 产品的 WCAG 合规（leapnonprofit 2026）
- WebSearch/WebFetch 核实：AI 无障碍工具格局 2025–2026（Be My AI / Seeing AI / Gemini Live Guided Vision / Apple Magnifier iOS 26 / Lookout / Envision Glasses）—— readsignal.io / andrew.ooo / olderfriends.org / digitaldigest.com
- 互补笔记（已存在，本篇差异化）：[[AI 产品的可访问性 UX for AI 学习笔记]]、[[无障碍 Accessibility 与 GUI Agent 同源技术栈 学习笔记]]、[[AI 监管与合规落地 学习笔记]]、[[负责任 AI 与 AI 产品伦理落地 学习笔记]]、[[AI 产品需求定义与 Agent 设计规范 学习笔记]]、[[数据飞轮与 AI 产品度量 学习笔记]]

---

## ⚠️ 待核实清单

- 各成员国 EAA 罚则具体金额（德国/意大利上限 €10 万、法国 €7.5 万或营收 4%、日罚 €1000 等）因国而异，**具体数值待逐国核实**。
- 2026 年「约 67% 受访残障网民每周用 AI」来自 Signal 2026 从业者调研（n=1,140），**样本与方法待核实**。
- 合成媒体市场规模（$5B 2024 → $48B 2033）、AI 视频占合成内容 34% 等市场数字，**出处与口径待核实**。
- ASR 准确率 95–98%、「WebAIM 2026 百万站 95.9% 可检测问题（较上年 94.8% 升）」等统计，**年度扫描结论待核实**。
- EU AI Act 各阶段日期（2025-02-02 / 2025-08-02 / 2026-08-02 / 2027-12-02 / 2028-08-02）与 Digital Omnibus 推迟范围，**以 EUR-Lex 官文为准，待复核**。

#标签/AI产品 #标签/无障碍 #标签/a11y #标签/合规 #标签/读屏测试
