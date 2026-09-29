---
date: 2026-09-26
tags: [AppIntent, 每日情报, 速览, 2026-09-26-晚]
source: "https://byteiota.com/microsoft-copilot-home-code-autopilot ; https://k.sina.com.cn/article_7879777299_1d5abdc1306801kzgk.html ; https://so.html5.qq.com/page/real/search_news?docid=70000021_8686aa38e5f10152"
importance_score: "★★★☆☆（6/10）"
intent_category: "微软 Copilot 重架构（Autopilot 常驻托管智能体 + Managed Runtime 租户沙盒）+ 鸿蒙小艺消费者评测数据 + 端侧 Qwen3-0.6B 实测"
---

# AppIntent 每日情报速览 2026-09-26-晚

> [!abstract] 30 秒速览
> - **核心突破**：**微软 09-25 重新设计 Copilot**（Home / Code / Autopilot 三大面 + **Copilot Managed Runtime** 租户内沙盒托管运行时）。其中 **Autopilot = 常驻托管智能体**——带自身**身份 / 记忆 / 工作区**进入组织租户，云托管、用户离线仍续跑；**Managed Runtime** 把自然语言生成的 App 跑在**IT 治理的沙箱**内、出现在 M365 管理中心供策略审查。这是本库追踪的「常驻托管智能体 + 隔离执行 + 身份/审计治理」范式首次被厂商做成产品级落地（对照 [[Agent Workspace 隔离执行]] / [[隔离执行]]）。
> - **关键指标**：Autopilot 由 Build 2026 内部代号 Scout 改名、9 月底进私有预览；计费二分——USL（封顶订阅，含 Chat/Office/Auto 路由）vs UBB（按量，含 Cowork/Code/Autopilot/前沿模型如 Astra/Fable）；端侧小模型实测——Qwen3-0.6B Q4_K_M 在 2017 三星 Note8（6GB）上驱动真实桌面 Chrome，**结构化输入 ~500 token/80s 完成命名匹配任务，原始 HTML 同任务需 12k token/22min**。
> - **OS Agent 场景**：本窗口四大 OS 官方框架层（Apple/Android/HarmonyOS/Windows OS 执行总线）**API 零净新增**，符合「OS 框架不日更」规律；真增量集中在 M365 治理/执行层的产品化（微软）+ 鸿蒙消费者评测数据补强 + 端侧 Planner 社区实证。

## ① Schema 定义与语义路由机制

- **（M365 治理/执行层·非 OS API）微软 Copilot 重架构**：Home 合并 Chat + Cowork 并把 Word/Excel/PowerPoint 直接嵌进 Copilot 界面；**Code** 用自然语言生成 App/仪表盘/自动化，基于 GitHub Copilot 同款技术，**运行在 Copilot Managed Runtime——租户内的沙盒托管环境，由 IT 治理**，并发布 npm 包 `@microsoft/managed-apps` / `-cli` / `-vite-plugin`（React+TS+Vite 8）；**Autopilot** 由 Scout 改名，是具备**自身身份、记忆、工作区**的常驻智能体，运行在云、用户离开仍续跑。这与 [[Agent 365 与 Entra Agent ID 智能体控制平面与身份基座 2026]]（治理/身份层控制平面）构成「治理层控制平面 + 租户内沙盒执行总线」的上下层拼接，但与 [[Windows Copilot Actions 与 Agent Workspace 2026]]（OS 执行总线四支柱）**层级正交**——勿写成「Windows OS 已内建托管运行时」。
- **（OS 框架层·无净新增）**：Apple iOS 27.1/27.2 双版本并行、Xcode 27.1 beta 1 为 iPhone Duo 折叠屏开发工具、Siri 多语言 10 月——**无新 `@AppIntent(schema:)` API**；Android AppFunctions 守 `alpha12`（无 alpha13）、A2UI 守 `alpha01`；HarmonyOS ArkAF 2.0 / Intents Kit / 元服务无新 API；Windows OS 执行总线四支柱 + 权限治理无新 Registry API。
- **（端侧 Planner 实测·方法学）Qwen3-0.6B 在 2017 Note8 驱动真实 Chrome**：社区仓库 e2llm/edge-browser-agent 让 0.6B 模型只接收 ~200 token 的**结构化页面表示**（命名链接/字段），按名选链接、把事实抄成 JSON，外围栈完成点击/验证；三个可验证任务 10/10。对比实验显示**结构化感知远优于原始 HTML**（沙盒任务 500 token/80s vs HTML 12k token/22min；维基页 46.7 万字符 HTML 在 16k 上下文只装下 9%、0/3）。这强化 [[端侧 Router 置信度门控与工具可达性收缩 2026]] 与 [[Function Calling 端侧工具调用]] 长期结论：「端侧路由吃结构化输入、不吃原始页面」是更小模型堪用的前提。见 [[Function Calling 端侧工具调用]]（诚实：社区实验、非 BFCL、仅 3 固定任务）。

## ② 系统安全与用户体验（Confirmation / 隔离 / 防注入）

- **托管运行时 = 企业级「隔离执行」的云侧样板**：Copilot Managed Runtime 把 Code 生成的 App 跑在**租户内沙箱、由 IT 治理、出现在 M365 管理中心供策略审查**，是 [[Agent Workspace 隔离执行]]「隔离 + 身份 + 审计」范式在 SaaS 层的产品化对照；Autopilot 自身带身份/记忆/工作区 + 权限/审计/治理，呼应 [[Agent 365 与 Entra Agent ID 智能体控制平面与身份基座 2026]] 的「统一注册表 + agent 身份 + 三运行模式」。与四平台 OS 执行总线形成**跨厂商范式映射**：OS 层（Windows Agent Workspace 容器 / Android 系统特权签名 / HarmonyOS 芯片级可信根）与 SaaS 层（M365 Managed Runtime）殊途同归地在解决「agent 在哪跑、权限多大、能否被审计/吊销」。
- **计费二分是 agent 成本治理新信号**：USL（封顶订阅）vs UBB（按量，含 Cowork/Code/Autopilot/前沿模型）把「agent 工作负载比聊天贵得多」显式化，是企业采用常驻智能体前的**成本控制闸门**——与 [[Agent Workspace 隔离执行]]「agent 一旦越权后果需可审计」同源，属治理层配套。
- **鸿蒙消费者评测数据补强（生态 UX）**：CNMO 评测小艺 409 分登顶、端侧盘古大模型**离线 12 秒处理会议记录**、依托鸿蒙 A2A 2100+ 系统能力 500+ 伙伴 Skill——是 HarmonyOS 「意图即服务」消费级兑现的第三方实测背书（见 [[HarmonyOS Intents Kit 与 ArkAF 2026]]），非框架 API，标注待官方核验。
- **XPIA 无窗口内新披露**：Semantic Kernel CVE-2026-26030 / CVE-2026-25592（CVSS 9.9）经核查为 **2026-05 已知漏洞**，ravoid.com 为年度综述，**非本窗口新 CVE**；维持「四平台 OS 意图层来源轴全空白」结论，见 [[XPIA 跨提示注入]]。

> [!note] 8 概念节点双链
> - [[意图模式规范]] ｜ [[语义路由]] ｜ [[端侧工具调用]] ｜ [[确认机制]] ｜ [[元服务]] ｜ [[隔离执行]] ｜ [[A2A 端侧智能体协议]] ｜ [[XPIA 跨提示注入]]
