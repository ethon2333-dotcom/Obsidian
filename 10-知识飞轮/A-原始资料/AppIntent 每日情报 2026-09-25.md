---
type: raw
status: inbox
source:
  - "https://developer.android.google.cn/jetpack/androidx/releases/appfunctions?hl=zh-cn"
  - "https://developer.android.com/jetpack/androidx/versions/all-channel"
  - "https://developer.android.com/jetpack/androidx/versions/alpha-channel"
  - "https://developer.android.google.cn/jetpack/androidx/releases/compose-material3?hl=pt-br"
  - "https://wpnews.pro/news/and-now-a2ui"
  - "https://www.163.com/dy/article/L7M2BLH80553TKK8.html"
  - "https://www.cbismb.com/harmonyos/article/BpTV82"
  - "https://simoncarter.ai/posts/microsoft-s-unified-copilot-desktop-app-rolls-out-to-commercial"
captured: 2026-09-25
tags: [AppIntent, 每日情报, 索引]
---

# AppIntent 每日情报 2026-09-25

> 窗口：2026-09-21 22:00 → 09-25 13:00（约 3.5 天，距上次跑约 4 天）。环境：仅 `agent-mail` 连接器在线，未调用 Horizon MCP，改用 WebSearch/WebFetch 直查官方源（AndroidX Release Notes / alpha-channel）与权威媒体。

## 索引（按重要性）

### 真增量（窗口内命中 / 库内空白补漏）
- ★7/10 [[Android AppFunctions 设备侧意图 2026]]（AppFunctions `1.0.0-alpha12` 2026-09-23 官方发布：新增 `scope` 字段 / `activityId` / `AppFunctionUriValueConstraint` / `serialize` 需元数据 + 运行时注册标 experimental + **破坏移除 `AppFunctionContext`/`AppFunctionConfiguration`**）｜ 枢纽 [[意图框架·跨体系索引 MOC]] ｜ 来源：developer.android.google.cn/jetpack/androidx/releases/appfunctions（官方 Release Notes）
- ★7/10 [[四平台意图 Registry 来源轴与权限模型对比 2026]]（alpha12 `scope` 维度进入 Registry 元数据/搜索 + `serialize` 元数据信号；Android 仍是唯一有公开动态可见性 API 的平台；来源轴全空白结论不变）｜ 枢纽 [[意图框架·跨体系索引 MOC]]
- ★6/10 [[A2UI 生成式UI协议(Google)与鸿蒙落地 2026]]（A2UI `1.0.0-alpha01` 官方落地 Android Jetpack：a2ui / a2ui.compose / material3-a2ui，JSONL 协议 + Material3 基础 catalog 13+ 组件，原生 Compose 渲染免任意代码）｜ 枢纽 [[意图框架·跨体系索引 MOC]] ｜ 来源：developer.android.com/jetpack/androidx/versions/alpha-channel + compose-material3 release notes + wpnews.pro
- ★6/10 [[HarmonyOS Intents Kit 与 ArkAF 2026]]（9-22 小艺接入淘宝闪购智能体「一句话点外卖」闭环 + 9-25 HarmonyOS 7 公测开放 + 数字 500+ 伙伴 Skills / 2000+ 鸿蒙智能体 / 2100+ 系统能力）｜ 枢纽 [[意图框架·跨体系索引 MOC]] ｜ 来源：网易 9-25 / cbismb HarmonyOS 7 A2A 接入指南
- ★5/10 [[Windows Copilot Actions 与 Agent Workspace 2026]]（统一 Copilot 桌面 app 9 月中旬向商业/消费用户铺开，Chromium 架构、个人/工作账户合一；应用层分发变更，非 OS 执行总线 API 新增）｜ 枢纽 [[意图框架·跨体系索引 MOC]] ｜ 来源：simoncarter.ai（MC1457084 时间线）

### 已复核·无净新增（避免重复检索）
- **Apple**：iOS 27.1 beta 仍无新 `@AppIntent(schema:)` / App Intents Domains API；App Intents 2.0（Streaming / multi-turn / View Annotations / App Schemas / App Intents Domains）为 WWDC26 已录内容，scand/byteiota 等多家 9 月复盘文章复述，**非窗口内新发布**。
- **Android**：AppFunctions `alpha12`（09-23）已入表（★7/10）；A2UI `alpha01`（09-23）已入表（★6/10）；其余组件无净新增。
- **HarmonyOS**：HC2026（9-17）为既有框架数据补强（09-21 已录）；9-25 小艺文章为消费/生态数据补强（已入表）；ArkAF 2.0 三层 / 端侧 Skill 无新 API。
- **Windows**：26H2 仍锚定 9 月下旬~10 月初；四支柱安全（Copilot Actions/Agent Workspace/ODR/Execution Containers）+ Agent 代码签名无新 Registry API；统一 Copilot app 为应用层部署（已作 ★5/10 状态记）。
- **跨平台 BFCL v4**：聚合榜稳定（DataLearner 09-15 快照 MiniCPM5-2B 66.6 居首；BTL-3 88.5% 仍聚合/自报、维持待官方复核）；无新端侧 Planner 模型/分数入榜。
- **XPIA**：无窗口内新研究 / 新 CVE（agentmelt/futureagi/treza 为概念复述；Zylos ~32% 天花板已录于 09-20）。
- **丢弃**：Windows 12 虚构、Android 18 AI-native 前瞻（低质）、Copilot 6 个 Office 功能（应用层非 OS 执行总线）、Shareable skills / Cowork cost controls（Copilot Studio 应用层）。

## 诚实标注 / 待办
- alpha12 `scope` 具体语义（调用方可见性作用域 vs 功能分类域）、`serialize` 元数据字段定义均**待 developer.android.com/ai/appfunctions 官方文档逐字段确认**；`scope` 是否等于「可见性/权限作用域」在确认前不写入对比表正文（延续 08-31 纪律）。
- `serialize` 要求元数据**可能是 provenance 信号但须谨慎**——更可能是序列化结构元数据，未必等于 intent 来源 provenance；来源轴全空白结论不变，待官方确认。
- `AppFunctionContext`/`AppFunctionConfiguration` 移除后，调用方身份注入新机制（如有）待 alpha13+ 或官方指南；本笔记 08-03 开放问题「AppFunctionContext 是否携带可验证调用方身份」追问基础被削弱。
- A2UI alpha01 为首版，基础 catalog 组件集与字段稳定性待后续 release 复核（延续 08-26「A2UI 版本协商防静默空白」）。
- 小艺/淘宝闪购具体机制与闭环成功率、HarmonyOS 7 公测具体机型清单均**待华为开发者文档逐字复核**（媒体口径）。
- 统一 Copilot app 为应用层变更，非 OS 执行总线；26H2 GA 仍锚定 9 月下旬~10 月初。
- 沿用：Per-Intent Privacy Manifest 官方逐字 / Watch OS 26 / NowSecure / AgentAntibody / Chrome Origin Sets / 高通 NPU exact specs / Berkeley 官方 BFCL v4 博客 / AppFunctions GA 日期。

## 后续动作
- [x] 提炼为概念 → 已落 B 既有节点增补 5（Android / Registry / A2UI / HarmonyOS / Windows），**0 新建 B 节点**
- [ ] 关联已有方法 → [[Agent 读入路径可信数据边界 SOP]]（alpha12 `serialize` 元数据 / `scope` 回流读路径与 Registry 维度）

## 复核与补捕（09-25 13:06 re-trigger，窗口内补捕）

> 本日为同日 re-trigger（距本文件主运行 09-25 13:00 仅约 6 分钟），属**复核型运行**。已对四大 OS 官方源二次核验：

- **复核结论：四大 OS 官方框架层无新增 API** —— Android AppFunctions 仍 `alpha12`（无 alpha13）、iOS 27.1 beta 仍无新 `@AppIntent(schema:)` / App Intents Domains API（搜到均为 iOS 27.0 Beta 文档复述）、HarmonyOS ArkAF 2.0 无新 API、Windows OS 执行总线（ODR/Agent Workspace/Copilot Actions/Execution Containers）无新 Registry API。与 09-25 主运行结论一致，无需重写。
- **窗口内补捕（★5/10，治理层，落在 09-25 窗口但主运行未覆盖）**：Microsoft 365 Copilot **Declarative Agents 支持 Skills 转入正式可用（GA）**（Message Center MC1476977，2026-09-22 公布，9 月中~月底全球铺开）。Skills = 把指令/脚本/模板/资源打包为可复用模块，按需加载；**脚本执行走安全沙箱、MIP 敏感度标签在 skill 文件上保留并生效**。这是微软智能体生态的「技能打包 + 安全沙箱执行」治理信号，与 [[Agent Skills 技能范式 2026]]（09-20 实证 + manifest 签名护栏）、[[隔离执行]]（沙箱）直接呼应，亦与 HarmonyOS Skills Framework / Android AppFunctions agent skill 构成跨平台「Agent Skill 上架 + 沙箱执行」范式对照。属 M365/Entra 治理层（非 Windows OS 执行总线），沿用 08-18 层级纪律。已补 [[Agent 365 与 Entra Agent ID 智能体控制平面与身份基座 2026]]。
  - 来源：MWPro 对 Microsoft Message Center MC1476977 的转述（2026-09-22）；精确 GA 日期与沙箱语法**待 learn.microsoft.com 逐字复核**。

> [!note] 8 概念节点双链
- [[意图模式规范]] ｜ [[语义路由]] ｜ [[端侧工具调用]] ｜ [[确认机制]] ｜ [[元服务]] ｜ [[隔离执行]] ｜ [[A2A 端侧智能体协议]] ｜ [[XPIA 跨提示注入]]
