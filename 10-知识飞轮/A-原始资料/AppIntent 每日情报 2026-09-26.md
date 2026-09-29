---
type: raw
status: inbox
source:
  - "https://www.ctee.com.tw/news/20260925700271-430704"
  - "https://www.digitaltoday.co.kr/en/view/107233/snapdragon-summit-2026-smartphones-can-run-30-billion-parameter-ai-models"
  - "https://www.abiresearch.com/blog/snapdragon-summit-2026-qualcomm-aagentic-ai-strategy"
  - "https://biz.chosun.com/en/en-it/2026/09/24/4FE5F5NLDNGDJMPOQ4XG6BTB64/"
  - "https://github.com/mlcommons/inference/tree/master/language/edge-agentic"
  - "https://new.qq.com/rain/a/20260925A0A4KM00"
  - "https://www.163.com/dy/article/L7N62HLM05503WTT_pdya11y.html"
  - "https://www.pcworld.com/article/3063498/windows-11-26h2-is-coming-meet-all-the-new-features.html"
captured: 2026-09-26
tags: [AppIntent, 每日情报, 索引]
---

# AppIntent 每日情报 2026-09-26

> 窗口：2026-09-25 13:06（上次 re-trigger）→ 09-26 00:17，约 11h。按任务「过去 24 小时」口径，09-25 00:17–13:00 已由 09-25 主运行覆盖，本日真正新增为 09-25 后段~09-26 的 Snapdragon Summit 收官报道 + 鸿蒙 7 正式版信号 + 小艺Work + MLPerf Edge Agentic。环境：仅 `agent-mail` 连接器在线，未调用 Horizon MCP，改用 WebSearch/WebFetch 直查官方/权威源（高通 keynote 多源 / MLPerf GitHub / 华为媒体 / PCWorld）。

## 索引（按重要性）

### 真增量（窗口内命中 / 库内空白补漏）
- ★8/10 [[端侧 Agent 执行总线 NPU 原生 agentic loop 2026]]（Snapdragon Summit 2026 收官：Snapdragon 8 Elite Gen 6 的 Hexagon NPU **首增「面向 Transformer / Agentic AI 的 element-wise accelerator」** + 共享内存 +50% + 端上 32K context + 可跑 **30B+ MoE**（每 token 激活 ~3B，UFS 5.0 直接跑）；Oryon CPU **FlexCache** 作「协调中柢」。关闭 09-16「待 Summit 确认」待办）｜ 枢纽 [[意图框架·跨体系索引 MOC]] ｜ 来源：ctee / digitaltoday / abiresearch / biz.chosun（高通 keynote 9-22~25，多源 corroboration）
- ★6/10 [[Function Calling 端侧工具调用]]（MLPerf Inference 新增 **Edge Agentic** 工作负载，以 **BFCL v4** 为精度门：参考模型 Qwen3.6-27B（Q4_K_M）在 Jetson AGX Thor 单轮 gated **86.23%**（≥83.64% 通过），单轮 non_live 82.59% / live 84.12% / hallucination 97.16%；多轮 optional 非 gated）｜ 来源：github.com/mlcommons/inference
- ★5/10 [[HarmonyOS Intents Kit 与 ArkAF 2026]]（鸿蒙 7.0.0.109SP6 推送 + 反馈助手移除=正式版信号；小艺Work 9-24 上架，跨设备（鸿蒙手机/平板/电脑/手表 + **Windows** 客户端）agentic 办公，云电脑/本地双执行环境 + 100+ 专家 + 钉钉/飞书/华为云空间连接器）——消费/应用层补强，非框架 API 新增）｜ 枢纽 [[意图框架·跨体系索引 MOC]] ｜ 来源：网易 9-25 / 腾讯新闻 9-25
- ★5/10 [[Windows Copilot Actions 与 Agent Workspace 2026]]（Windows 11 26H2 仍以 enablement package 形态于 9 月下旬~10 月初铺开；Ask Copilot 任务栏搜索替代 + File Explorer 内 Copilot 侧栏为 agentic 入口；OS 执行总线四支柱 + 权限治理无新 Registry API）｜ 枢纽 [[意图框架·跨体系索引 MOC]] ｜ 来源：PCWorld / WindowsCentral / windowsforum 9-25

### 已复核·无净新增（避免重复检索）
- **Apple**：iOS 27.1 beta 仍无新 `@AppIntent(schema:)` / App Intents Domains API；搜到的 `app-intents-agent-skill` SKILL.md 描述「27 releases」= iOS 27 cohort 已录于 Apple B 笔记（LongRunningIntent / IndexedEntity / OwnershipProvidingEntity 等），无 27.1 专属 Schema API。
- **Android**：AppFunctions 仍 `alpha12`（09-23，无 alpha13）；A2UI 仍 `alpha01`（无 alpha02）；developer.android.google.cn Release Notes 同 09-25 记录，无进位。
- **HarmonyOS**：框架层 ArkAF 2.0 / Intents Kit / 元服务无新 API；7.0.0.109SP6 为消费版推送信号（已作 ★5/10 入表）。
- **Windows**：26H2 四支柱（Copilot Actions / Agent Workspace / ODR / Execution Containers）+ 代码签名 + 容器隔离无新 Registry API；26H2 为 enablement package 部署推进（已作 ★5/10 状态记）。
- **跨平台 BFCL v4 官方榜**：MiniCPM5-2B 66.60 仍 SOTA（09-07），无新端侧 Planner 模型/分数入官方榜；benchlm 88.5% BTL-3 仍自报、维持待官方复核。
- **XPIA**：无窗口内新 CVE / 新防御机制（windowsnews.ai 2 天前文=微软文档 XPIA 警告消费者复述；Atlassian Rovo 7 月已修；dev.to 9-17 教程）；维持「四平台 OS 意图层来源轴全空白」结论。
- **丢弃**：高通 personal AI 跨设备生态叙事（已在 NPU 笔记以硅底信号承载，不单列）/ Android I/O '26 复述 / iOS 27 二次复述 / Windows 12 虚构 / Copilot 6 个 Office 功能（应用层非 OS 执行总线）。

## 诚实标注 / 待办
- Snapdragon 8 Elite Gen 6 规格为高通 keynote + 多源媒体转述，**具体 TOPS / 峰值功耗 / 量产机型上市日**以高通官方 whitepaper / 量产 SoC 规格为准；「30B MoE 端上跑、每次 token 激活 ~3B、UFS 5.0 直接跑」为高通演示口径。
- MLPerf Edge Agentic 参考模型 Qwen3.6-27B 为 MLPerf 选的**参考实现**（非最小端侧 Planner）；gated 86.23% 为 Jetson AGX Thor 上 Q4_K_M 参考点，设备无关（temp 0 确定性）；多轮为 optional 非 gated（完整 200 条 multi_turn_base = 70.00% parity evalscope）。
- alpha12 `scope` 语义与 `serialize` 元数据是否 provenance 仍**待 developer.android.com/ai/appfunctions 官方文档逐字段确认**（延续 09-25 待办）。
- 鸿蒙 7.0.0.109SP6 是否=正式版、小艺Work 执行机制（是否走元服务/AppFunctions 等价意图回路）待华为开发者文档复核（媒体口径）。
- 沿用：Per-Intent Privacy Manifest 官方逐字 / Watch OS 26 / NowSecure / AgentAntibody / Chrome Origin Sets 官方 URL / 高通 NPU exact TOPS·功耗（whitepaper）/ Berkeley 官方 BFCL v4 博客逐字 / AppFunctions alpha13 / A2UI alpha02 / 26H2 精确 GA 日。

## 后续动作
- [x] 提炼为概念 → 已落 B 既有节点增补 4（NPU / Function Calling / HarmonyOS / Windows），**0 新建 B 节点**
- [ ] 关联已有方法 → [[Agent 读入路径可信数据边界 SOP]]（Snapdragon on-die loop 与「敏感数据不出端」闭环回流）

> [!note] 8 概念节点双链
- [[意图模式规范]] ｜ [[语义路由]] ｜ [[端侧工具调用]] ｜ [[确认机制]] ｜ [[元服务]] ｜ [[隔离执行]] ｜ [[A2A 端侧智能体协议]] ｜ [[XPIA 跨提示注入]]
