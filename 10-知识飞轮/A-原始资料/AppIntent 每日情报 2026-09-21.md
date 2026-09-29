---
type: raw
status: inbox
source:
  - "https://www.huawei.com/cn/news/2026/9/hc-agentic-era-harmonyos"
  - "https://www.c114.com.cn/news/126/a1317928.html"
  - "https://www.oschina.net/news/502597/hc2026-agentic-era-harmonyos"
  - "https://cybersecuritynews.com/bragjack-ai-agent-hijacking/"
  - "https://www.zeroday.news/article/malicious-extensions-hijack-ai-browser-agents"
  - "https://blog.csdn.net/qq_39427511/article/details/166075976"
  - "https://www.ai.jp.net/article/android-gets-a-safety-cage-google-prepares-smartphones-for-ai-agents-de7477"
  - "https://www.nabamart.com/2026/09/is-apple-enlisting-its-rivals-to-save.html"
  - "https://blakecrosley.com/blog/xcode-27-release"
  - "https://www.unrot.co/blogs/ai-news-this-week-september-20-2026"
captured: 2026-09-21
tags: [AppIntent, 每日情报, 索引]
---

# AppIntent 每日情报 2026-09-21

> 窗口：2026-09-20 21:00 → 09-21 22:00（约 25h）。环境：仅 `agent-mail` 连接器在线，未调用 Horizon MCP，改用 WebSearch/WebFetch 直查官方源与权威媒体。

## 索引（按重要性）

### 真增量（库内空白补漏 / 窗口内命中）
- ★7/10 [[HarmonyOS Intents Kit 与 ArkAF 2026]]（HC2026 鸿蒙智能体框架 2.0 端云混合规划 90%+ 成功率 + 生态规模数字 + Skill/A2A 双层接入 + 端侧文本搜图不出端）｜ 枢纽 [[意图框架·跨体系索引 MOC]] ｜ 来源：华为全联接大会2026 官方通稿，环球网/证券日报/C114/开源中国 09-19~09-21 报道
- ★6/10 [[XPIA 跨提示注入]]（BragJack「Prompt Forcing」：单一恶意浏览器扩展经 Chromium DNR 劫持 5 款 Chromium AI 助手信道，CVE-2026-0628/55945，已修补）｜ 枢纽 [[XPIA 跨提示注入]] ｜ 来源：Forever Security Gal Weizman，zeroday.news / cybersecuritynews.com / techtimes 09-16 公开、09-20 周报覆盖
- ★6/10 [[Agent 365 与 Entra Agent ID 智能体控制平面与身份基座 2026]]（Microsoft Foundry 托管智能体网络出网控制 public preview：FQDN 通配 + 允许/拒绝/改写出站头/改写目的地）｜ 枢纽 [[意图框架·跨体系索引 MOC]] ｜ 来源：CSDN 微软技术日报 09-20（Azure 09-18 更新批次）
- ★5/10 [[Android AppFunctions 设备侧意图 2026]]（Google 被报道在 App Functions Manager 框架层嵌入 agent 安全护栏「safety cage」，低置信，待官方 SDK 注释复核）｜ 枢纽 [[意图框架·跨体系索引 MOC]] ｜ 来源：ai.jp.net 09-21
- ★5/10 [[XPIA 跨提示注入]]（Plugin4Shell：Claude Code/Codex/Copilot/Gemini CLI 零点击 RCE，绕过 SHA pinning 经 Git branch/commit 碰撞，强化 09-20 Skill 供应链投毒主题）｜ 枢纽 [[XPIA 跨提示注入]] ｜ 来源：unrot.co 09-20
- ★5/10 [[Apple AppIntents Schema Protocol 2026]]（iOS 27.1 beta / Xcode 27.1 beta 已放出 = iPhone Duo SDK，无新 App Intents Schema API；代码级 Model Delegation API 反编译信号，非官方）｜ 枢纽 [[Apple AppIntents Schema Protocol 2026]] ｜ 来源：blakecrosley.com / woozad 09-18~09-19、nabamart 09-21

### 已复核·无净新增（避免重复检索）
- **Apple**：iOS 27.1 beta / Xcode 27.1 Beta 1 已于约 09-18/19 放出（早于 09-20 估计的 09-21~23），内容为 **iPhone Duo 折叠屏适配 SDK**（size classes + 保留区域 `reservedRegions` API），**无新 `@AppIntent(schema:)` / App Intents Domains API**；关闭 09-20「iOS 27.1 beta 尚未发布」待办 → 改为「已放出、Duo 向、无 schema 新增」。
- **Android**：AppFunctions 仍 **`1.0.0-alpha11`（2026-08-26）**，窗口内**无 alpha12**；`@AppFunction` / KDoc 机制无变化。
- **HarmonyOS**：HC2026（9-17 开幕）为既有 HarmonyOS 7 / ArkAF 2.0 的**消费/生态数据补强**，非新 API，已并入既有节点。
- **Windows**：Copilot Actions / Agent Workspace / ODR 四支柱 + Execution Containers 无新 Registry API；本期增量在治理层（Foundry 出网控制），非 OS 执行总线。
- **跨平台 BFCL v4**：聚合榜稳定（Qwen3.7 Max 75% 领先；端侧 LFM2.5-2.6B 56.9% 为最佳 sub-3B），**无新端侧 Planner 模型/分数**；该数字为 AnotherWrapper 聚合（非官方 Berkeley 榜），维持 09-15 待办。
- **丢弃**：Windows 12（dev.to 虚构/低质）、Android 18 AI-native（2027 前瞻、低质猜测）、Exaforce 第三方 SOC 产品（非 OS 机制）、EU Cyber Resilience Act（监管、非框架）。

## 诚实标注 / 待办
- HC2026 生态数字（8500 万终端 / 1100 万开发者 / 1 万应用 / 36.8 亿日均调用 / 2000+ 系统能力）来自华为官方 HC2026 主题演讲（卢鑫刚），经媒体转述；「端云混合规划 90%+ 成功率」「端侧文本搜图不出端」为华为口径，待华为开发者文档逐字复核。
- BragJack 为 09-16 公开、09-20 周报覆盖，非本窗口 24h 首发；CVE-2026-0628（Chrome 8.8，Chrome 143.0.7499.192/.193 修）/ CVE-2026-55945（Edge race condition，150.0.4078.48 前）已确认修补；Opera Neon / Comet / Claude-in-Chrome 修补状态部分未确认。
- iOS 27.1 Model Delegation API 经开发者 pdfu 反编译发现（nabamart 转述），Apple 未官方宣布外部模型可选；与 09-15「Foundation Models 多模型路由」互为印证但仍是代码级证据。
- 跟踪：iOS 27.1 正式 beta 是否带新 Schema API（已放出但 Duo 向）；AppFunctions alpha12；鸿蒙 端侧文本搜图 / 星河互联是否接意图回路（官方文档）；把 BragJack Prompt Forcing 与 [[隔离执行]] / [[确认机制]] 做映射；Plugin4Shell 一手 CVE 与受影响版本清单。
- 沿用：Per-Intent Privacy Manifest 官方逐字 / Watch OS 26 / NowSecure / AgentAntibody / Chrome Origin Sets / 高通 NPU exact specs / Berkeley 官方 BFCL v4 博客。

## 后续动作
- [x] 提炼为概念 → 已落 B 既有节点增补（鸿蒙 / XPIA×2 / Agent 365 / Android / Apple 共 5 处，0 新建 B 节点）
- [ ] 关联已有方法 → [[Agent 读入路径可信数据边界 SOP]]（BragJack 回流读路径/信道靶面）

> [!note] 8 概念节点双链
- [[意图模式规范]] ｜ [[语义路由]] ｜ [[端侧工具调用]] ｜ [[确认机制]] ｜ [[元服务]] ｜ [[隔离执行]] ｜ [[A2A 端侧智能体协议]] ｜ [[XPIA 跨提示注入]]
