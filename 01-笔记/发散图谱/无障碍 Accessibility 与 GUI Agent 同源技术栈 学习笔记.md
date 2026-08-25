---
title: 无障碍 Accessibility 与 GUI Agent 同源技术栈
tags:
  - 发散图谱
  - 无障碍
  - GUIAgent
  - 无障碍树
  - 端侧AI
  - 语义UI
created: 2026-08-15
source: 联网检索核实（详见文末「附：来源清单」）
---

## 学习定位

本篇是「发散图谱」下的广度种子笔记，目标不是把某一块挖深，而是把一条容易被忽视的同源性锚点摊开：为视障用户服务的无障碍技术（屏幕阅读器 / 无障碍树 / 语义 UI），与今天火热的 GUI Agent「看懂界面」能力，底层是同一套语义接口。对 OS PM 而言，这意味着「无障碍合规」和「端侧 Agent 基建」在技术上高度同构——本篇只铺面、不钻点，深度盲区用 `- [ ]` 列出待解问题。

**一句话心智模型：无障碍树既是给视障用户的「界面翻译层」，也是 GUI Agent 的「原生 API」——两者共用同一份语义 UI 底座，合规与智能意外地同源。**

---

## 一、核心概念速查（定义铺广度）

| 概念 | 是什么 | 与 GUI Agent 的关系 |
|---|---|---|
| 无障碍树 Accessibility Tree | 浏览器/OS 基于 DOM 与原生控件语义生成的「可交互元素精简映射」，剔除样式噪音，只留 role / name / state / hierarchy | GUI Agent 直接消费这棵树来「看懂」界面，远比截图便宜、稳定 |
| 语义 UI Semantic UI | 用原生语义元素（button / input / landmark）表达意图，而非 div 伪装 | 语义越干净，Agent 与屏幕阅读器越「看得懂」 |
| AT-SPI (AT-SPI2) | Linux/GNOME 的辅助技术接口，D-Bus 实现，Orca 屏幕阅读器依赖 | Linux 桌面 Agent 的读取通道 |
| MSAA / UIA | Windows 旧（MSAA, 1995）与新（UI Automation, Vista 起）无障碍 API | Windows 端 Agent / 自动化读取控件树的标准来源 |
| NSAccessibility (AXAPI) | Apple 平台无障碍协议，AXRole / AXPress 等 | VoiceOver 与 macOS/iOS Agent 共用 |
| AccessibilityService + AccessibilityNodeInfo | Android 系统级辅助服务，可监听事件、读取节点树、模拟点击/输入 | 端侧 Android GUI Agent 的「合法」操控入口（见 [[工业级 GUI Agent 架构（VLM+无障碍树）]]） |
| ARIA | Web 的 WAI-ARIA 属性（role / aria-label / live region），把语义补进 DOM | Agent 与屏幕阅读器都靠它定位「按钮叫什么、现在什么状态」 |

---

## 二、主流平台无障碍技术栈对照（分类铺广度）

| 平台 | 核心 API / 框架 | 代表屏幕阅读器 | GUI Agent 读取通道 | 备注 |
|---|---|---|---|---|
| Windows | MSAA（旧）、UI Automation UIA（新，Vista 起） | JAWS、NVDA | UIA 控件树 / Playwright MCP | Chrome 138（2025-08）起原生支持 UIA，去掉 MSAA→UIA 中间代理层 |
| macOS / iOS | NSAccessibility (AXAPI) | VoiceOver | AX 元素树 | 移动端占比：WebAIM #10 调查 VoiceOver 约 70.6%、TalkBack 约 34.7%（口径为 2023–2024 调查，非 2025，待核实最新值） |
| Android | AccessibilityService / AccessibilityNodeInfo | TalkBack | 无障碍节点树 + ADB | 系统原生支持，但 Play 商店严格限制非无障碍用途 |
| Linux | AT-SPI2 (D-Bus) | Orca | AT-SPI 树 | 非 GNOME 环境采用度偏低 |
| Web | WAI-ARIA + Core AAM 映射（2025-10 更新到 1.2） | 浏览器内嵌 | 浏览器无障碍树（DOM 经 CSS+ARIA 生成） | 同一棵树同时服务屏幕阅读器与 Web Agent |

---

## 三、GUI Agent 为什么复用无障碍树，而非截图（同源关系核心）

| 维度 | 无障碍树（文本/语义） | 截图 + 视觉模型 |
|---|---|---|
| 数据形态 | XML→JSON，1–5 KB | PNG/JPEG→Base64，50–200 KB |
| 所需模型 | 纯文本 LLM 即可 | 多模态 VLM（更贵） |
| 单次成本（移动端示例） | 约 $0.01/动作 | 约 $0.15/动作 |
| 延迟 | <1 秒 | 3–5 秒 |
| 坐标精度 | 解析 bounds，像素级 | OCR 估算，易错 |
| 适用 | 标准控件（按钮/输入框） | Canvas、游戏、视频等无语义内容 |
| 稳定性 | 高（语义不随布局漂移） | 低（布局一变就失效） |

> 心智落点：移动端因「应用商店强制无障碍合规 + UI 相对简单 + 成本/延迟敏感」，Agent 普遍首选无障碍树；桌面端视觉模型仍有价值（图表、设计工具）。两者正走向「树为主、视觉兜底」的混合架构。相关纵深见 [[工业级 GUI Agent 架构（VLM+无障碍树）]]。

---

## 四、2025–2026 进展（同源融合加速）

| 时间/方向 | 进展 | 关键信号 |
|---|---|---|
| 2024-09 | Google 将 Gemini 集成进 Android TalkBack，替代旧模型 Garcon | 端侧 Gemini Nano 离线生成图像描述，Gemini Flash 处理复杂查询（待核实：Nano/Flash 分工细节） |
| 2025-06-28 | 欧盟《欧洲无障碍法案》EAA 正式 enforcement | 数字服务 WCAG 2.1 AA 成法律要求，倒逼语义 UI 普及 |
| 2025-08 | Chrome 138 在 Windows 默认原生 UIA | 辅助技术与 Agent 直接连 Chromium，去中间层、降延迟 |
| 2026 | NVDA 2026 路线图：64 位迁移 + 安全插件运行时 + 端侧 AI 图像描述（2026.1 alpha，键盘快捷键本地处理，不上云） | 屏幕阅读器从「TTS 工具」转向「上下文感知助手」 |
| 2026-02-05 | Google 发布 Natively Adaptive Interfaces (NAI) 框架 | 把无障碍「原生内置」而非事后补丁，用 Gemini 子 Agent 动态调整 UI（字号/语音/布局） |
| 2026 (CHI) | UC Berkeley + U Michigan 发布 A11y-CUA 数据集 | 以 Claude Sonnet 4.5 测：标准 ~78%、仅键盘 ~42%、150% 放大视口 ~28%——注意这是「约束 Agent」而非「约束网站」的结论 |
| 2025–2026 | 端侧视障助手与 GUI Agent 框架融合 | Mobile-Agent-v3 / GUI-Owl 等同时消费 A11y Tree 与截图做 grounding 与训练数据合成 |

---

## 五、代表产品 / 框架（市场铺广度）

| 类型 | 代表 | 平台 | 说明 |
|---|---|---|---|
| 屏幕阅读器 | JAWS / NVDA / VoiceOver / TalkBack | Win / Win / Apple / Android | 无障碍树的「老主顾」，现正被 LLM 增强 |
| 视障视觉助手 | Be My AI（Be My Eyes）、Seeing AI、Google Lookout、Envision Ally | 跨端 / 眼镜 | AI 描述图像，可一键转接真人志愿者 |
| 可穿戴入口 | Ray-Ban Meta / Oakley Meta 智能眼镜 + Be My Eyes | 眼镜 | 摄像头上头、双手解放，与 [[AI 眼镜与可穿戴意图入口 学习笔记]] 高度同源 |
| Android Agent 框架 | Assists、Ctrl.js（均基于 AccessibilityService） | Android | 端侧自动化脚本，低门槛封装无障碍 API |
| 多模态 GUI Agent | Mobile-Agent-v3 / GUI-Owl（阿里通义） | 手机+PC+Web | AndroidWorld 73.3、OSWorld 37.7（开源 SOTA，2025-08） |
| Web Agent | ChatGPT Atlas、Perplexity Comet、Playwright MCP、Project Mariner | Web | 普遍以无障碍树为主接口，视觉兜底 |
| 车机/HMI 入口 | 智能座舱语音+视觉助手 | 车机 | 与 [[智能座舱与车机 HMI 意图入口 学习笔记]] 共享语义 UI 思路 |
| 语音交互 | Gemini Live、端侧 ASR/TTS | 跨端 | 与 [[语音交互与端侧 ASR TTS 学习笔记]] 协同 |

---

## 对 OS PM 的意义

无障碍合规与端侧 Agent 能力在技术上同源：一套干净的语义 UI 与无障碍树，既满足 EAA/WCAG 法律底线，又直接成为 GUI Agent 的「原生 API」，二者不是成本与智能的取舍，而是同一份基建的两种回报。对 Android OS PM，端侧无障碍节点树（AccessibilityNodeInfo）是合规要求也是 Agent 操控的合法入口——把语义 UI 当作系统级 AI 基建而非「无障碍专项」来规划，能在合规、Agent、可穿戴入口（[[端侧意图框架 学习笔记]]）上同时复利。

---

## 待解问题

- [ ] 移动端 GUI Agent 用无障碍树时，对非标准控件（Canvas / 游戏 / 自定义 View）的兜底策略到底是什么？VLM 视觉补充的成本临界点在哪里？
- [ ] Android AccessibilityService 的 `takeScreenshot`（Android 12+）与节点树读取，在工程上如何分工与降级？
- [ ] EAA（2025-06-28 生效）对 OS 层「系统应用语义结构」的具体合规边界是什么？PM 的可交付清单长什么样？
- [ ] Google NAI 框架宣称「原生自适应」，它和现有 App 的 ARIA/语义标记如何衔接？是否会催生新的系统级接口？
- [ ] CHI 2026 A11y-CUA 的「键盘/放大约束」结论，能否反向用于评估 GUI Agent 的鲁棒性基准？
- [ ] Gemini Nano 端侧图像描述在 TalkBack 的真实离线覆盖率与功耗代价？有无公开数据？
- [ ] 端侧小模型（SLM）做「屏幕理解」时，无障碍树 token 化与视觉 token 的融合架构孰优？
- [ ] iOS 比 Android 更封闭（沙盒/App Store 政策），这是否会让端侧 GUI Agent 在 iOS 上长期弱于 Android？

---

## 附：来源清单

| 来源名 | 类型 | 日期 | 真实 URL |
|---|---|---|---|
| Why Accessibility Trees Over Screenshots (DeepWiki) | 技术文档 | 2025 | https://deepwiki.com/actionstatelabs/android-action-kernel/5.1-why-accessibility-trees-over-screenshots |
| Computer accessibility (Grokipedia) | 百科/综述 | 2025 | https://grokipedia.com/page/Computer_accessibility |
| Screen Reader – Sitecockpit | 科普 | 2025 | https://www.sitecockpit.com/en/lexicon/screenreader |
| VoiceOver vs TalkBack (Auditsu) | 开发者指南 | 2025 | https://auditsu.com/resources/voiceover-vs-talkback |
| Chromium Windows UIA 原生支持 (Chrome 开发者) | 官方博客 | 2025-08-14 | https://developer.chrome.com/blog/windows-uia-support-update?hl=zh-cn |
| Accessibility Tech Converges on AI (Machine Herald) | 行业综述 | 2026-03 | https://machineherald.io/article/2026-03/22-accessibility-technology-converges-on-ai-wearables-and-regulation-as-ada-and-eaa-deadlines-loom |
| AI Accessibility Features (MyVision) | 综述 | 2025–2026 | https://www.myvision.org.uk/ai-accessibility-features-for-visually-impaired |
| 2026 盲人辅助技术创新综述 (Disability World) | 综述 | 2026 | https://t.cj.sina.com.cn/articles/view/7879849871/1d5acf78f01901pobs |
| Mobile-Agent-v3 (arXiv 2508.15144) | 论文 | 2025-08-21 | https://papers.cool/arxiv/2508.15144 |
| Mobile-Agent-v3 (ModelScope) | 项目页 | 2025 | https://modelscope.cn/learn/1773 |
| Accessibility Is Business-Critical in Age of AI Agents | 观点/行业 | 2026 | https://www.htmlelements.com/accessibility-is-business-critical-in-the-age-of-ai-agents |
| AI agents can't buy what they can't read | 观点 | 2026 | https://blog.tsd.digital/ai-agents-cant-buy-what-they-cant-read |
| Computer Use and GUI Agents in 2026 (Zylos) | 研究综述 | 2026-02 | https://zylos.ai/zh/research/2026-02-08-computer-use-gui-agents |
| Google Natively Adaptive Interfaces (EasyAuthor) | 行业解读 | 2026-02 | https://easyauthor.ai/blog/index.php/2026/02/06/google-natively-adaptive-interfaces-ai-accessibility-4 |
| Not every skill is a capability / A11Y.md (dev.to) | 观点 | 2026 | https://dev.to/fecarrico/not-every-skill-is-a-capability-43n9 |
| Android 系统中实现 GUI Agent 要点解析 | 技术博客 | 2025 | https://blog.coderfan.org/?p=5384 |

---

## ⚠️ 待核实清单

- 屏幕阅读器占比（VoiceOver 70.6% / TalkBack 34.7%）来自 WebAIM Screen Reader Survey #10（2023–2024），非 2025 数据，需补最新调查。
- Google TalkBack + Gemini 的「Nano 端侧 / Flash 云端」分工为媒体口径，Google 官方未给出精确拆分，待核实。
- CHI 2026 A11y-CUA 的 78% / 42% / 28% 数字：这是「约束 Agent 操作条件」测得，不等同「网站不可访问就会让 Agent 失败」，引用时勿曲解。
- WebAIM Million 2026「95.9% 首页有 WCAG 失败」来自第三方博客转述，原始报告年份与口径待核实。
- Mobile-Agent-v3 的 AndroidWorld 73.3 / OSWorld 37.7 为论文自报开源 SOTA，闭源/商用系统数字未公开对比，勿当绝对领先。
- EAA enforcement 日期「2025-06-28」为多源一致，但各成员国 transposition 细节与 OS 级系统应用适用范围待法律口径核实。

#标签/发散图谱 #标签/无障碍 #标签/GUIAgent
