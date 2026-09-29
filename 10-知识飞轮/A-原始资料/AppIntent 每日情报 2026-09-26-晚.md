---
type: raw
status: inbox
source:
  - "https://byteiota.com/microsoft-copilot-home-code-autopilot"
  - "https://codiot.com/blog/copilot-autopilot-vs-aiforce"
  - "https://asumetech.com/2026/09/26/microsoft-redesigns-copilot-app-with-office-integration-and-autopilot-agents"
  - "https://www.163.com/dy/article/L7OPSDMK0550A7YJ.html"
  - "https://k.sina.com.cn/article_7879777299_1d5abdc1306801kzgk.html"
  - "https://so.html5.qq.com/page/real/search_news?docid=70000021_8686aa38e5f10152"
captured: 2026-09-26
tags: [AppIntent, 每日情报, 索引]
---

# AppIntent 每日情报 2026-09-26-晚

> 窗口：2026-09-26 00:17（本日晨间跑结束）→ 09-26 22:07，约 22h。按任务「过去 24 小时」口径，本日晨间（00:17 结束）已覆盖 Snapdragon Summit 收官 + MLPerf Edge Agentic + 鸿蒙 7.0.0.109SP6 + 小艺Work + Windows 26H2；本次晚间跑只记 00:17 之后的净新增，不覆盖晨间成果。环境：仅 `agent-mail` 连接器在线，未调用 Horizon MCP，改用 WebSearch/WebFetch 直查官方/权威源（微软 09-25 官方博文转述多源 / 网易 / 新浪 / 腾讯搜一搜 / 开发者社区）。

## 索引（按重要性）

### 真增量（窗口内命中）
- ★6/10 [[Agent 365 与 Entra Agent ID 智能体控制平面与身份基座 2026]] + [[Agent Workspace 隔离执行]]（微软 09-25 重新设计 Copilot：Home / Code / **Autopilot** 三大面 + **Copilot Managed Runtime** 租户内沙盒托管运行时 + 计费二分 USL/UBB）——Autopilot 是「常驻托管智能体」带**自身身份/记忆/工作区**进入租户（由 Scout 改名、Build 2026 首秀），Managed Runtime 把 Code 生成的 App 跑在**租户内 IT 治理的沙箱**并出现在 M365 管理中心供策略审查。属 M365/企业治理与执行层，**非 Windows OS 执行总线（ODR/Agent Workspace）新 API**；但与本库 [[Agent Workspace 隔离执行]]（沙箱/身份/审计）与 [[隔离执行]] 范式形成**跨厂商范式对照**：微软把「常驻智能体 + 租户级沙盒运行时 + 身份/审计/治理」做成产品级落地）｜ 来源：byteiota / codiot / asumetech / gadgetbond / compsmag（微软 09-25 官方博文 Spataro 转述，多源 corroboration）
- ★5/10 [[HarmonyOS Intents Kit 与 ArkAF 2026]]（9-26 消费者评测/实测补强：CNMO AI 助手智能体评测小艺 V11.13.300 **409 分**登顶、领先荣耀 YOYO 超 30 分；中国电信 7 月《AI 手机场景智能评测》Mate80 Pro Max 社交/学习/影像/办公四项第一；端侧盘古大模型**离线 12 秒处理会议记录**；鸿蒙 A2A 依托 2100+ 系统能力 500+ 伙伴 Skill——消费级实测数据补强，非框架 API 新增）｜ 来源：新浪科技 9-26 / 今日头条 9-26
- ★5/10 [[Function Calling 端侧工具调用]]（端侧 Planner 实测：Qwen3-0.6B Q4_K_M 在 2017 三星 Note8（6GB）上经结构化页面感知层驱动真实桌面 Chrome 完成浏览器 Agent 任务，12 个小模型对比三个可验证任务 **10/10**，且结构化输入 ~500 token/80s 远优于原始 HTML 12k token/22min——社区实验，非 BFCL，但强化「结构化感知 + 极小模型」端侧路由范式）｜ 来源：腾讯搜一搜 / AGI Hunt / prismix（r/LocalLLaMA 镜像，e2llm/edge-browser-agent 仓库）

### 已复核·无净新增（避免重复检索）
- **Apple**：iOS 27.1 beta 仍无新 `@AppIntent(schema:)` / App Intents Domains API；窗口内检索命中 iOS 27.1/27.2 双版本并行（iPhone Duo 出厂预装 iOS 27.1，iOS 27.2 10 月面向所有机型）+ Xcode 27.1 beta 1（Duo 折叠屏开发工具）+ Siri AI 多语言（法语/日语/韩语/葡萄牙语/西班牙语）10 月——均为折叠屏适配与版本线，**无新 App Intents Schema API**。
- **Android**：AppFunctions 仍 `alpha12`（09-23，无 alpha13）；A2UI 仍 `alpha01`（无 alpha02）；developer.android.google.cn Release Notes 同 09-25 记录，无进位。
- **HarmonyOS**：框架层 ArkAF 2.0 / Intents Kit / 元服务无新 API；9-26 为消费者评测/实测数据补强（已作 ★5/10 入表）。
- **Windows**：OS 执行总线四支柱（Copilot Actions / Agent Workspace / ODR / Execution Containers）+ 代码签名 + 容器隔离无新 Registry API；09-25 重新设计 Copilot 为 M365 应用/治理层重架构（已作 ★6/10 入表），非 OS 执行总线。
- **跨平台 BFCL v4 官方榜**：MiniCPM5-2B 66.60 仍 SOTA（09-07），无新端侧 Planner 模型/分数入官方榜；anotherwrapper 仍标「Llama 3.1 405B 88.5%」与库内「疑厂商自报」标注一致、维持待官方复核；benchlm 9-24 更新列 Atria Dawn Preview 92.5 实为 Terminal-Bench 2.0/OSWorld 类 agentic 评测、非 BFCL v4 端侧 Planner。
- **XPIA**：窗口内检索命中的 Semantic Kernel CVE-2026-26030 / CVE-2026-25592（CVSS 9.9，prompt injection → RCE）经核查为 **2026-05 已知漏洞**（PDF 标注 2026/05，ravoid.com 为 2026 年综述文），**非本窗口新披露**，不计入新增量；维持「四平台 OS 意图层来源轴全空白」结论。
- **丢弃**：KOPA-BENCH（arXiv 2609.05395，Sept 2026 多步工具调用基准，覆盖韩语公开 API + BFCL 子集）为**新基准但非端侧 Planner 专项**，且论文日期 9 月、窗口内仅作引用、未提供端侧小模型新分，★3/10 低于收录阈值，作参考标注不入库；Salesforce AIforce（9-15）/ 苹果 Siri 不可靠旧闻 / 鸿蒙消费者营销稿等不计入。

## 诚实标注 / 待办
- Microsoft 09-25 Copilot 重新设计为**微软官方博文（Jared Spataro）转述多源**（byteiota/codiot/gadgetbond/compsmag），具体 GA/预览日期与 Managed Runtime 沙箱语法/SDK 版本以 learn.microsoft.com 逐字复核；Home/Code 经 Frontier 计划数周内铺开、Autopilot 9 月底私有预览，**均非 GA**；纳德拉「工作 OS」为定位表述，勿写成「Windows OS 已内建」。
- 鸿蒙 9-26 评测数字（409 分 / 四项第一 / 离线 12 秒会议记录）来自 CNMO / 中国电信 **评测机构与媒体口径**，端侧盘古大模型离线 12 秒为厂商/媒体表述，具体基准与机型待华为开发者文档核验。
- Qwen3-0.6B Note8 实验为 **e2llm 社区仓库（r/LocalLLaMA 镜像）**，仅 3 个固定任务、名称匹配与抄写，**非通用 benchmark、非 BFCL**；「结构化感知远优于原始 HTML」为方法学洞察，与其直接比端侧 Planner 准确率不严谨。
- 沿用：Per-Intent Privacy Manifest 官方逐字 / Watch OS 26 / NowSecure / AgentAntibody / Chrome Origin Sets 官方 URL / 高通 NPU exact TOPS·功耗（whitepaper）/ Berkeley 官方 BFCL v4 博客逐字 / AppFunctions alpha13 / A2UI alpha02 / 26H2 精确 GA 日 / iOS 27.1 正式 beta 是否带新 Schema API。

## 后续动作
- [x] 提炼为概念 → 已落 B 既有节点增补 4（Agent 365 + Agent Workspace 隔离执行 / HarmonyOS / Function Calling），**0 新建 B 节点**
- [ ] 关联已有方法 → 把「Managed Runtime 租户沙盒」与 [[Agent 读入路径可信数据边界 SOP]] / [[系统级 Intent 路由评估 SOP]] 做跨厂商对照

> [!note] 8 概念节点双链
- [[意图模式规范]] ｜ [[语义路由]] ｜ [[端侧工具调用]] ｜ [[确认机制]] ｜ [[元服务]] ｜ [[隔离执行]] ｜ [[A2A 端侧智能体协议]] ｜ [[XPIA 跨提示注入]]
