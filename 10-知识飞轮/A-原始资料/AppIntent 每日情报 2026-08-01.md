---
type: daily-index
status: index
captured: 2026-08-01
window: "24 小时窗口 2026-07-31 09:00 → 2026-08-01 09:00（硬命中 1 条）+ 库内空白补漏 6 条（逐条标真实日期）"
intent_category: "执行安全（自传播 XPIA）/ 端侧 Planner 模型架构 / 意图调度内核 / Apple Schema API / 元服务分发"
importance_score: "★★★★★（9/10，24h 真增量 1 条 + 库内空白补漏 6 条，其中 2 条为范式级转折）"
tags: [AppIntent, 情报, 索引, 2026-08-01]
---

# AppIntent 每日情报 2026-08-01（索引）

> [!abstract]
> 24h 窗口硬命中仅 **1 条**（DroiClaw 登国际媒体），另补 **6 条**库内完全空白但对本主题至关重要的进展。三条主线同时质变：① **执行安全**——Copilot for Word 被证实存在**可自我传播的文档型 XPIA 蠕虫**，MSRC 协调披露 144 天后**漏洞「类别」仍未关闭**，「载荷修了，类别没修」；② **端侧 Planner**——Cactus 开源 Needle（26M / INT4 仅 14MB / **完全无 FFN 层**），论证「工具调用是检索-组装，不是推理」；③ **意图调度内核**——荣耀 AgenticOS、阶跃 Step AOS、卓易 DroiClaw 一个月内先后把 OS **调度对象从「进程/线程」改为「意图/任务」**，四大平台之外冒出第五类玩家。

## 本期条目索引

| 重要性 | 条目 | 原子笔记（完整内容） | 主题枢纽 | 一手来源 |
|---|---|---|---|---|
| 10/10 | Copilot for Word 文档型 XPIA 蠕虫：披露 144 天、GPT-5.6 上仍可复现，攻击**把自己复制进新生成文档**（2026-07-28/29） | [[文档型 XPIA 自传播蠕虫]] · [[Agent Workspace 隔离执行]] · [[Agent 写回路径 XPIA 风险评估 SOP]] | [[XPIA 跨提示注入]] · [[确认机制]] | [Context Collapse Part 3 原始披露](https://enklypesalt.com/posts/context-collapse-part3-ai-worming-through-word/) · [explainx 拆解](https://explainx.ai/blog/copilot-word-document-ai-worm-xpia-july-2026) · [HN 讨论](https://news.ycombinator.com/item?id=49096188) · [Morris II 先例](https://arxiv.org/abs/2403.02817) |
| 9/10 | Needle：26M 参数 / INT4 14MB / **无 FFN** 的端侧函数调用模型，单次调用跑赢 270M~600M 级（GitHub 提交 2026-05-12~16，7 月底二次扩散） | [[Simple Attention Network 无FFN端侧路由]] · [[Function Calling 端侧工具调用]] | [[端侧工具调用]] · [[Intent Router 语义路由]] | [Cactus 官方公告](https://cactuscompute.com/blog/needle) · [源码与 SAN 架构文档](https://github.com/cactus-compute/needle) · [权重 MIT](https://huggingface.co/Cactus-Compute/needle) · [第三方架构拆解](http://rits.shanghai.nyu.edu/ai/cactus-releases-needle-a-26m-distilled-model-for-on-device-tool-calling) |
| 8/10 | 荣耀 AgenticOS：六层全栈重构，**调度对象从进程/线程升级为意图/任务**；OpenClaw 把 4DoF 云台定义为智能体标准物理执行器（WAIC 2026-07-18） | [[Agentic OS 意图调度内核]] | [[端侧意图框架 学习笔记]] · [[System Orchestrator 系统编排]] | [荣耀官方 WAIC 2026](https://www.honor.com/cn/news/honor-waic-2026) · [黄非演讲实录·全栈技术揭秘](https://mobile.it168.com/a2026/0718/6941/000006941659.shtml) |
| 8/10 | 阶跃 Step AOS：架设在 Android 之上的智能体原生 OS，原子能力引擎 + 统一语义数据层，兼容 MCP/A2A；四维安全首提「**可逆**」（2026-07-13 MWC 上海） | [[Agentic OS 意图调度内核]] · [[Confirmation UI 安全机制]] · [[端侧执行通道 GUI 与 MCP 路线之争]] | [[确认机制]] · [[MCP 与设备侧 MCP]] | [中国经济周刊·Step AOS 发布](https://www.ceweekly.cn/economic/industry/2026/0714/497277.html) · [Step AOS 英文技术要点](https://chinaainews.org/news/stepfun-launches-step-aos-the-first-agent-native-operating-system) |
| 8/10 | Apple WWDC26 Session 345 代码级细节补齐：`ValueRepresentation` / `RelevantEntities` / `EntityCollection` / `SyncableEntity` / `@UnionValue` / `LongRunningIntent` / `ExecutionTargets` 八组 API 用法与性能语义（2026-06） | [[Apple AppIntents Schema Protocol 2026]]（见「2026-08-01 增补」节） | [[Apple Intelligence 与 App Intents]] · [[意图模式规范]] | [WWDC26 Session 345](https://developer.apple.com/cn/videos/play/wwdc2026/345) |
| 7/10 | 跨平台意图路由**六层 × 六方分层矩阵**成型（能力声明 / 发现索引 / 相关性提示 / 路由决策 / 参数填充 / 跨设备），跨设备层三家殊途同归于「上下文归属人而非设备」 | [[Intent Routing Stack 六方意图路由分层对照 2026]]（**本期新建**） | [[意图框架·跨体系索引 MOC]] · [[意图模式规范]] | 本期多源综合（见上列各条一手来源） |
| 6/10 | 鸿蒙负一屏：元服务成为智能体可分发的能力单元，**Today-Task Skill** 让智能体产出物有系统级承载位；MAU 1.9 亿（HDC 2026 + 07-29 报道） | [[HarmonyOS Intents Kit 与 ArkAF 2026]]（见「2026-08-01 增补」节）· [[Atomic Service 元服务]] | [[HarmonyOS 元服务 学习笔记]] · [[Atomic Service 元服务|元服务]] | [格隆汇·鸿蒙负一屏与 Today-Task Skill](https://m.gelonghui.com/p/5248344) |
| 6/10 | DroiClaw 诸葛：第三方 AI 原生 OS **中间层供应商**登国际视野（路透社 / TechCrunch），999 元千元档普惠 AI OS（**24h 唯一硬命中**，07-31 11:26 转载） | [[Agentic OS 意图调度内核]]（见「三家形态对照」节） | [[国内安卓厂商做 App Intent 的阻力]] · [[App Infra 应用基建]] | [TechTimes·DroiClaw 专访](https://www.techtimes.com/articles/321574/20260725/how-droiclaw-building-ai-native-operating-system-agentic-era.htm) · [腾讯云开发者社区转载 07-31](https://cloud.tencent.com/developer/news/4355852) |

> 说明：本笔记为**索引**，不内联分析。每条信息的完整技术细节、字段清单、待补项均在上方「原子笔记」链接中。

## 原报告残留细节（尚未进入任何 B 笔记，暂存于此）

> 以下为原报告中的**厂商口径事实**，因不得改写既有 B 笔记而保留在索引层，待后续并入 [[Agentic OS 意图调度内核]]。

- **荣耀模型侧**：六大自研大模型矩阵；自动执行智能体 / 端侧多模态 / 智能体模型分别登 **MobileWorld、MMBench、ACEBench** 榜单（⚠️ **具体名次与分数官方未公布，待补**）；与阿里千问（达摩院）共创 **端侧 Omni、端侧 VLM、Agentic Pro、Agentic Fast、GUI Agent** 多版本。
- **荣耀四大特征 / 形态**：意图驱动 / 自然交互（声音·手势·眼神·动作**多通道叠加消除歧义**）/ 主动智能 / 天生跨端；「**一主多专、三端协同**」= 随身主智能体 + 海量终端 + 垂域生态 + 云端超算大脑。Robot Phone 云台规格：比主流方案缩小 70%、0.8 秒弹出、360° 追踪、CIPA 5.5 级防抖、步行抖动补偿率 96%。
- **第三方评价**：中国工程院院士**郑纬民**称 AgenticOS「不是在传统 OS 上重做，而是在上面**加了一层认知软件层**，专门管智能体的全流程调度、协作与安全」。
- **Step AOS 厂商口径数字**：记忆称 **PersonalMem / LongMemEval 达 SOTA**，简单查询召回 **10.3ms**、复杂 **800ms**；**Step Edge** 端侧基座简单任务 **<100ms 响应、成功率 >99%**，宣称 **29 项权威基准中位列同类端侧模型第一**（⚠️ 基准清单与对比对象**待补**）；联合上海人工智能实验室发布《新一代智能体系统安全技术白皮书》《端侧大模型网络安全指南》并牵头行业安全国标（⚠️ 标准编号与认证机构**待补**）；首批生态伙伴 **美团、支付宝、滴滴、携程、WPS、剪映**，8 月中旬联合 B 站发起「STEPX 狂想计划」开放 Agent / Skill 共创。

## 已复核·无净新增（避免重复检索）

- **Android**：[AppFunctions 官方文档](https://developer.android.google.cn/ai/appfunctions) 本次无 24h 增量，仍 experimental。
- **Windows**：[Windows 智能体安全文档](https://learn.microsoft.com/windows/security/book/operating-system-agentic-security) 本次无官方文档增量。
- **检索口径**：Horizon MCP 未出现在连接器列表（不可用），改用 WebSearch/WebFetch 直取官方源；合成由本 Agent 完成，未消耗外部分析额度。厂商自述数据一律标注口径，未经独立核验的名次与分数标「待补」。

## 排除项

- **纯流程/元信息不入 B 层**：24h 窗口连续两天硬命中 ≤4 条 → 已采纳「**改为 7 日滚动窗口**」的流程改进（08-05 索引已按 7 日窗口执行，本条闭环）。
- 各条内的营销话术与未标注口径的对比数字已在提炼阶段丢弃，仅保留可核验事实与明确标注的厂商口径。

## 未决问题（→ 各自 B 笔记跟踪，不在本索引展开）

- Needle 的评测集与可复现 eval 脚本？「工具选择头」在数百工具（真实 OS Registry 规模）下是否成立？无 FFN 能否承担多轮 / 多工具串行编排 → [[Simple Attention Network 无FFN端侧路由]]
- Word 蠕虫机制能否平移到 OS Agent（被污染文档 / 日历事件触发 AppFunctions 或 HarmonyOS Skill 非预期调用并写回）？四平台均无类别级评估 → [[文档型 XPIA 自传播蠕虫]]
- **当 OS 把调度单元升级为「意图」，意图本身会否成为被注入对象**（恶意意图注册 / 污染认知记忆沉淀）？三家新 OS 公开材料均未回应 → [[Agentic OS 意图调度内核]] · [[Agent Data Injection 数据注入攻击]]
- 荣耀 / 阶跃 / 卓易改为「意图」调度后，Registry 权限模型是什么？谁能注册、需何审核 → **「四平台 Registry/权限横向 Checklist」应扩展为六方** → [[Intent Routing Stack 六方意图路由分层对照 2026]]
- Step AOS 架在 Android 之上，如何获得跨 App 原子能力调用权（无障碍 / ROM 特权 / 双边协议）？若为双边协议则与 [[国内安卓厂商做 App Intent 的阻力]] 困境一致 → [[Agentic OS 意图调度内核]]
- Apple「2027 年的新版本」对应哪些系统版本号（iOS 28？）官方未明说 → [[Apple AppIntents Schema Protocol 2026]]
- 跟踪 Måløy 系列后续 / 微软是否发布类别级缓解；核验《人工智能终端智能化分级》标准编号与 L3 认证机构；回填荣耀三榜名次；跟踪 Robot Phone 8 月发布会与 AgenticOS 开发者文档；澄清鸿蒙设备数/元服务数两组冲突口径（7000 万台·40 万款 vs 6600 万台·3.5 万款）→ [[HarmonyOS Intents Kit 与 ArkAF 2026]]

> [!note] 关联枢纽
> **MOC**：[[意图框架·跨体系索引 MOC]] ｜ **主题枢纽**：[[App Intent 的核心作用]] · [[Apple Intelligence 与 App Intents]] · [[国内安卓厂商做 App Intent 的阻力]] · [[工业级 GUI Agent 架构（VLM+无障碍树）]] · [[端侧意图框架 学习笔记]] · [[HarmonyOS 元服务 学习笔记]] · [[MCP 与设备侧 MCP]] · [[手机AI智能体知识库]]
> **本期原子笔记**：[[文档型 XPIA 自传播蠕虫]] · [[Simple Attention Network 无FFN端侧路由]] · [[Agentic OS 意图调度内核]] · [[Intent Routing Stack 六方意图路由分层对照 2026]] · [[Apple AppIntents Schema Protocol 2026]] · [[HarmonyOS Intents Kit 与 ArkAF 2026]] · [[Atomic Service 元服务]] · [[Confirmation UI 安全机制]] · [[Function Calling 端侧工具调用]] · [[Agent Workspace 隔离执行]] · [[端侧执行通道 GUI 与 MCP 路线之争]]
> **方法层**：[[Agent 写回路径 XPIA 风险评估 SOP]] · [[系统级 Intent 路由评估 SOP]]
