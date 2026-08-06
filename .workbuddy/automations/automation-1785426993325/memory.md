# 自动化执行记忆 · automation-1785426993325
# AppIntent 每日情报 → 知识飞轮（每日 09:00，hy3）

> 本文件记录高层执行摘要，供后续运行读取。不存放完整交付物正文。

## 角色与范围
系统级 Agent 与 OS 意图框架前沿情报官。每日检索过去 24h 内 Apple / Android / HarmonyOS / Windows 在「系统级意图框架 / 端侧 Agent 执行总线 / 设备侧 Planner 意图路由 / 跨应用 Intent 工作流 / 执行安全（XPIA、ODR、Confirmation UI）」的新进展，落库 Obsidian 知识飞轮。

## 落库分层约定
- A 原始资料：`10-知识飞轮/A-原始资料/`（用 `_模板/原始资料.md`）
- B 泛化概念：`10-知识飞轮/B-泛化概念/`（用 `_模板/概念蒸馏.md`；已存在则**追加**不新建）
- C 可复用方法：`10-知识飞轮/C-可复用方法/`（用 `_模板/方法SOP.md`）
- D 输出内容：`10-知识飞轮/D-输出内容/`（用 `_模板/输出复盘.md`）
- 收尾：在 `10-知识飞轮/知识飞轮看板.md` 末尾「本次新增（日期）」区登记链接。

## 运行记录

### 2026-07-31（09:00 版，本次）
- 状态：完成（含 A/B/C/D 四层落库 + 看板登记）。
- 严格 24h 真增量 4 条：① OSWorld 首破 90.2% ② 豆包手机二代弃 GUI 转 MCP ③ 华为小艺 GUI 实测"微信未接入" ④ 智能体互联 7 项国标。
- 库内空白补漏 5 条（均标真实日期，不冒充当日新闻）：Android 17 GA（2026-06-16）/ HarmonyOS 7 HMAF 2.0 / iOS 27 beta 3 第三方实测 / 端侧 Planner 评测补齐 / Gemini 40+ App / 国内支付边界。
- 产出文件：A `AppIntent 每日情报 2026-07-31`；B 净新增 3（OSWorld 计算机操作基准 / 智能体互联国家标准与 AIP / 端侧执行通道 GUI 与 MCP 路线之争）、B 既有增补 5（Android AppFunctions / HarmonyOS Intents Kit / Apple AppIntents Schema / Confirmation UI / Function Calling）；C 净新增 1（端侧执行通道选型 SOP）；D 净新增 1（AppIntent 每日情报速览 2026-07-31）。
- 口径纪律（高价值）：qwen3-0.6b-tool-router 90.42% ≠ Qwen3-0.6B Prompt 1.38%；prism-coder "BFCL 100%" 实为自建基准，非官方 BFCL；回填 Gemma 4 / Qwen3-Coder-Next 评测。
- 待办：核验 OSWorld 官方榜单与 7 项国标标准号；四平台 Registry/权限横向 Checklist（已挂多日）；跟踪 iOS 27 正式版（9-14）第三方覆盖；24h 窗口偏薄，评估是否改 7 日滚动。
- 已知局限：二手媒体占比偏高（HarmonyOS 7 / iOS 27 细节），均标注"待官方文档确认"。

### 2026-08-01（09:00 版，本次）
- 状态：完成（含 A/B/C/D 四层落库 + 看板登记）。
- 严格 24h 真增量仅 **1 条**：DroiClaw（卓易「诸葛」AI 原生 OS）登路透社/TechCrunch 等国际媒体（腾讯云开发者社区 07-31 11:26 转载）。**连续第二天 24h 窗口过薄**，已在 A 笔记与看板明确建议改 **7 日滚动窗口**（保留首次入库存量判定做去重）。
- 库内空白补漏 **6 条**（均标真实日期，不冒充当日新闻）：① Copilot for Word 文档型 XPIA 自传播蠕虫（Måløy，2026-07-28）② Needle 26M / 无 FFN 架构（Cactus，GitHub 05-12~16，7 月底二次扩散）③ 荣耀 AgenticOS（WAIC 07-18）④ 阶跃 Step AOS（07-13）⑤ Apple WWDC26 Session 345 代码级细节（06）⑥ 鸿蒙负一屏元服务/Today-Task Skill（HDC + 07-29）。
- 产出文件：A `AppIntent 每日情报 2026-08-01`；B 净新增 3（Simple Attention Network 无FFN端侧路由 / Agentic OS 意图调度内核 / 文档型 XPIA 自传播蠕虫）、B 既有增补 5（XPIA 跨提示注入 / Function Calling 端侧工具调用 / Apple AppIntents Schema Protocol 2026 / Confirmation UI 安全机制 / HarmonyOS Intents Kit 与 ArkAF 2026）；C 净新增 1（Agent 写回路径 XPIA 风险评估 SOP，含三问判据）；D 净新增 1（AppIntent 每日情报速览 2026-08-01）。
- 最高价值条目：Word 文档型 XPIA 蠕虫——威胁模型从「一次注入」升级为「注入会自我复制」，MSRC 协调披露 144 天后类别仍未关闭；提炼出「写回路径三问判据」写入 C 层。
- 口径纪律：Needle 对比为 Cactus 自述、single-shot、非官方 BFCL，标「具体测试集待补」；厂商自述名次（荣耀榜单、Step Edge 29 项第一）均标待补；鸿蒙设备数/元服务数两组口径冲突（7000万/40万 vs 6600万/3.5万）标待官方澄清。
- 待办：改 7 日滚动窗口；四平台 Registry/权限 Checklist 扩为六方（+AgenticOS/Step AOS）；核验 Needle 评测集；跟踪 Måløy 系列/微软类别级缓解；澄清鸿蒙口径冲突；跟踪荣耀 Robot Phone 8 月发布。
- 已知局限：Horizon MCP 不可用（全部 disconnected），改用 WebSearch/WebFetch 直取官方源；Word 蠕虫/Needle 部分来源为聚合媒体二次扩散，已标真实一手来源与日期。

## 经验沉淀（跨运行）
- 去重：先读 `01-笔记/手机AI智能体/` 既有笔记，双链指向而非改动用户原文件。
- 诚实：未核实数据标「待补」，绝不编造评测数字。
- 口径：区分官方 BFCL 行 vs 自建同名基准；窄域微调 router 与通用 Prompt 不可互换。

### 2026-08-02（09:00 版，本次）
- 状态：完成（含 A/B/D 三层落库 + 看板登记）。**本日正式从 24h 切换为 7 日滚动窗口（2026-07-26→08-02）**，依 08-01 记忆建议，保留首次入库存量判定做去重。
- 7 日窗口内真增量 2 条：① **EU AI Act Article 15（准确性/鲁棒性/网络安全）今日（08-02）正式生效**，第 15(5) 条点名 prompt injection / 对抗样本 / 投毒为高风险系统须抵御攻击面，罚则 €15M/3%——OS Agent 执行安全从「产品选择」变「法律义务」（第二处分水岭，第一处为 08-01 Word 蠕虫）② **HarmonyOS HDD 西安站（08-01）**：小艺升 Agentic 自演进系统级大脑，小艺开放平台 **A2A 端侧/云侧双模**，头部银行端侧 A2A 覆盖 1000+ 意图隐私不出端、O2O 云侧 A2A 走完端到端闭环。
- 库内空白补漏 2 条（标真实日期）：③ **Apple WWDC26 Session 343 深入**（View Annotations / IntentValueQuery / Confirmations+entity ownership；App Intents 2.0 streaming/富实体/多轮）④ **Android AppFunctions 官方 Agent Skill 四步生命周期**（发现/实现/KDoc 优化/测试，官方文档验证）。
- 排除 1 条（展示过滤纪律）：M365 Copilot Agentic 模式扩大可用（08-01）属应用/M365 层，非 OS 级执行总线，低于阈值排除。
- 产出文件：A `AppIntent 每日情报 2026-08-02`；B **既有增补 5**（HarmonyOS Intents Kit / A2A 端侧智能体协议 / Apple AppIntents Schema Protocol / Android AppFunctions / Windows Copilot Actions）；D `AppIntent 每日情报速览 2026-08-02`。
- **纪律要点**：本日**未新建独立 B 节点 / C 层 SOP**，全部「既有 B 追加」避免重复；厂商口径（银行 1000+ 意图、O2O 闭环）标「待补」；「Per-Intent Privacy Manifest」未从一手源独立确认，不记为已确认 API；Digital Omnibus 拟推迟但截至本日未正式通过，按现行 08-02 生效日记录。
- 待办：跟踪 Digital Omnibus 正式文本；理清四平台对 Article 15 合规触发条件；核验 HarmonyOS 银行 App 名与意图清单；确认 Per-Intent Privacy Manifest 是否为真实 API；回填 Android Agent Skill 发布日期；六方 Registry/权限 Checklist（+AgenticOS/Step AOS）仍未入表；跟踪荣耀 Robot Phone 8 月发布、Måløy Word 蠕虫类别级缓解。

### 2026-08-03（09:00 版，本次）
- 状态：完成（含 A/B/C/D 四层落库 + 看板登记）。沿用 7 日滚动窗口（2026-07-27→08-03）。
- 窗口内真增量 1 条：DroiClaw 诸葛（卓易）中国市场正式发布（08-03，新华社发文），首次拿到架构口径（本地小模型+云端大模型端云协同、无 App 交互、安全/可控/可观测）。
- 库内空白补漏 4 条（标真实日期）：① Android AppFunctions 1.0.0-alpha10 编译时 `@AppFunctionServiceEntryPoint` + Registry/权限硬细节（BIND_APP_FUNCTION_SERVICE / app_metadata / 动态门控 / 验证命令）+ Google 明示「理解可能在云端」与确认下放 App ② ADI（arXiv 2607.05120，CSA 07-18）改写注入定义，同环境对照 0–0.7% vs 最高 100%，CaMeL Strict 唯一归零但可用性 81→36.5% ③ DualView（arXiv 2607.03821）Stored IPI 53.3% + AgentView/HumanView 双视图 + 带外防御「门不能是模型」~15× 调用 ④ LFM2.5-8B-A1B + LocalCowork 端侧 Agent 循环齐备样本（13 MCP/67 工具/亚秒 dispatch/审计）。
- 产出文件：A `AppIntent 每日情报 2026-08-03`；B 净新增 2（Agent Data Injection 数据注入攻击 / Dual View 智能体数据视图隔离）、B 既有增补 6（Android AppFunctions / XPIA / Confirmation UI / Agent Workspace / Function Calling / Agentic OS）；C 净新增 1（Agent 读入路径可信数据边界 SOP，与 08-01 写回路径 SOP 双向闭环）；D 净新增 1（AppIntent 每日情报速览 2026-08-03）。
- 最高价值：ADI = 执行安全第三个分水岭（前两个为 08-01 Word 蠕虫、08-02 EU AI Act Article 15），且其性质不同——威胁定义变了，非威胁变强/约束变硬；直接给出 PRD 判据：四平台意图元数据是否做来源校验（均待补）。
- 口径纪律：ADI/DualView 数字标「论文/CSA 口径未复现」；LFM2.5 分数标「厂商自述/第三方转载」；厂商三性声明（DroiClaw 安全/可控/可观测）标「待补」；二手报道机构口径冲突以 arXiv/CSA 为准。
- 待办：追四平台 ADI 类别评估/意图元数据来源校验（最高优先级）；补 Apple/HarmonyOS/Windows Registry 动态可见性 API（六方 Checklist 仅 Android 填实）；跟踪 Anthropic/OpenAI/Google 类别级缓解；Digital Omnibus/HarmonyOS 银行 App/Per-Intent Privacy Manifest/荣耀 Robot Phone/Måløy 延续待办。

## 2026-08-03（21:00 晚间增补跑）

- **性质**：同日 09:00 已跑完整 7 日窗口，本轮为**增补跑**。确认了一个重要运行模式：**同日二次触发时不重跑全窗口，只记 09:00 版之后的净新增，并显式列出「已复核·无净新增」清单**（避免下次重复检索、也避免让用户误以为漏检）。文件名加 `-晚` 后缀，不覆盖上午成果。
- **信息源**：Horizon MCP 仍全部 disconnected（连续 5 日），继续 WebSearch/WebFetch 直取官方源 + 本 Agent 自行综合，未调外部 gemini，无 429。
- **窗口内四大 OS 官方渠道无新增**：Apple（WebFetch WWDC26/iOS 27 指南逐条比对无变化）、Android（alpha10 已在 09:00 版详录）、HarmonyOS、Windows（WebFetch agentic security 文档四支柱与既有记录一致）。
- **真增量 2 条**：① Bonsai 1-bit 量化模型 BFCL 实测（7/10，第三方仓 `Manojb/small-llm-tool-use-bench`）② 银联 APOP/AVOP 生态里程碑（6/10）。
- **两条方法论级结论**（已写入 C 层 SOP，未来选型直接引用）：**BFCL 测格式合规 ≠ NexusRaven 测语义理解**（同模型差 30 分且排名倒转）；**1-bit QAT 在结构化输出任务上是增益不是损失**（同族 FP16 25.3% → 1-bit 73.3%）。
- **落库**：A 1（晚间增补）｜ B 净新增 1（意图支付授权协议 APOP）｜ B 既有增补 1（Function Calling 端侧工具调用）｜ C 既有修订 1（系统级 Intent 路由评估 SOP，顺手修正残留旧口径 46%→90% → 官方 58%→85%）｜ D 1｜看板已登记。
- **⚠️ 连续第 2 日未解待办**：四平台 ADI 分级评估 / 意图元数据来源校验。常规 WebSearch 路径已证明无效，**下轮改查各平台安全白皮书 PDF**。
- **新增待办**：PrismML 官方技术报告（回填 1-bit QAT 配方与官方分数）；APOP 协议全文 + 是否做到「意图内容与凭证绑定」+ 能否与 AppFunctions/App Intents 对接。
- **数据质量提醒（延续）**：intelliparadigm.com 的 FunctionGemma 文章含可疑说法，不可引用；本轮 Bonsai 数据同为第三方个人测评（Mac Mini M4 非手机 SoC、BFCL v3 非 v4），已在笔记内标注不可与 Berkeley 官方榜单并列。

## 2026-08-04（21:00 版，本次）

- **状态**：完成（A/B/C/D 四层落库 + 看板登记）。7 日滚动窗口 2026-07-29→08-04。Horizon MCP 仍全部 disconnected（**连续 6 日**），继续 WebSearch/WebFetch 直取官方源 + 本 Agent 自行综合，未调外部 gemini，无 429。
- **本期最重两条（并列 8/10）**：
  - **① BFCL v4 权重重构 —— 性质是「口径变化」不是新事实**。Agentic 40% / Multi-Turn 30% / Live 10% / Non-Live 10% / Hallucination 10%，经典单轮从几乎全部压到 20%。**后果：库内所有历史 BFCL 分数（Bonsai 73.3%、qwen3-0.6b-tool-router 90.42% 等）均为 v3 时代「格式合规分」，与 v4 不可比**，已在两个 B 节点集中打版本标签。
  - **② 三日待办有实质进展但仍未解**：微软 Agent Governance Toolkit（开源治理层）给出成熟数据溯源模型——六类来源枚举 / 四级密级 / 单调棘轮（只升不降）/ post_tool + pre_output 两阶段闸口，对齐 EU AI Act Article 10。但**已 WebFetch 复核 Windows 官方 agentic security 文档，确认 OS 层无来源分级**。结论从「没人做」精化为「治理层有成熟模型、OS 层全空白」。
- **第三条（7/10）**：Project Perception 公开预览（08-03），Defender for Endpoint 检查 agent loop 三段流量（用户提示/工具调用/工具响应）并在执行前阻断——防线从「隔离」延伸到「检查」。
- **四大 OS 官方渠道经复核无新增可执行 API**，已在 A 层显式记「已复核·无净新增」，避免下次重复检索。
- **排除 4 条（过滤纪律）**：钉钉 Agent OS、TOS 7、PilotDeck、Windows Patch Tuesday —— 非 OS 级意图框架/端侧路由/执行安全，或属常规安全更新。
- **落库**：A 1（AppIntent 每日情报 2026-08-04）｜ B 净新增 1（数据溯源分级与单调棘轮）｜ B 既有增补 4（Function Calling 端侧工具调用 / Local Agent Bench 端侧智能体基准 / Agent Data Injection 数据注入攻击 / Windows Copilot Actions 与 Agent Workspace 2026）｜ C 既有修订 1（Agent 读入路径可信数据边界 SOP，**步骤 2 由二元可信判断升级为六类来源 + 四级密级 + 棘轮的可执行分级判据**，完成标准同步改三问式）｜ D 1｜看板已登记。
- **运行模式收获**：本轮最有价值的判读动作是**先分类「新事实 vs 口径变化」**。BFCL v4 若按常规「又一个 benchmark 更新」处理，就会漏掉「库内十几条分数集体失效」这个真正后果。建议固化为日常判读第一步。
- **层级校准纪律（新增）**：治理层/应用层的成熟方案容易被误写成「OS 已支持」。本轮 AGT 就险些如此，靠 WebFetch 官方文档反查才校正。**凡涉及「某平台已具备 X 能力」的结论，必须回官方文档验证层级**。
- **⚠️ 待办**：
  - **【最高优先，本期新增】核实 Berkeley 官方 BFCL v4 权重原文** —— 本期核心结论建立在二手快照上，下轮优先花检索预算专攻官方源。
  - **【连续第 4 日未解】四平台是否采纳意图元数据来源分级**（Apple `.appEntityIdentifier` 来源绑定/签名仍待补）。08-03 定的「改查安全白皮书 PDF」本轮未执行完，下轮继续。
  - Project Perception 口径统一：CyberGym 95.95% vs 96%、MAI-Cyber-1-Flash vs MAI-Cyber-Flash-1（两处并存，待官方）。
  - **新问题回流**：若 OS 不提供来源分级，应用侧自行打标能否防住 ADI？打标器本身会否成为新靶面（谁给打标器提供来源信息）？
  - 延续：PrismML 技术报告、APOP 协议全文与对接方式、六方 Registry Checklist（仍仅 Android 填实）、Digital Omnibus 正式文本、HarmonyOS 银行 App 名、Per-Intent Privacy Manifest、荣耀 Robot Phone（8 月发布）、Måløy 类别级缓解。

## 2026-08-05（00:18 手动续跑 · 非情报采集）
- 性质：手动续跑（非 21:00 情报窗口）。用户问"读取 obsidian 看知识图谱还能往哪学"，对全库做双链图体检（校正后实测 117 篇 / 9 MOC / 7 孤立 / 21 断链），产出 `01-笔记/知识图谱体检与学习路线.md`。
- 顺带完成上一轮两条发散笔记的 MOC 注册（LLM 跨学科发散 → 新建 AI 工程 MOC + 交叉进 AI Agent 框架 MOC；PM 需求定义 跨学科发散 → OS产品经理知识库 MOC D 节）。
- 核心结论：多数断链是缩写别名未对上枢纽笔记（确认机制/隔离执行/语义路由等），修法=加 aliases；真白点= MCP/设备侧MCP、Context Engineering、元服务、缺失的 OS-PM-AI Runtime动态调度与降级策略 笔记、PRD MOC、编程语言 MOC。
- 未做情报采集；下一次 21:00 情报跑不受影响，7 日窗口照常。

## 2026-08-05（竞品情报 NDA 整理 · 续 00:30）

- 性质：接续 00:25 整理收口后的 00:30 竞品情报请求，**非情报采集跑**。用户披露：own-words 竞品观察大量写在公司（NDA 无法带出），要求「帮我整理相关的」——即只整理库内公开/自动情报侧。
- 核查结论：竞品情报层（`竞品情报 MOC` + HarmonyOS/Windows 两篇子笔记）**已完整且全连通**——结构与你贴的意图逐条一致；12 个出链全部命中（0 断链）；3 个父索引（手机AI智能体知识库 / 意图框架·跨体系索引 MOC / PM决策层 MOC）均已回链；库内 6 篇 B 层技术笔记 + 安卓对比/安全笔记均存在可支撑对标。
- 产出：`01-笔记/竞品情报整理任务清单.md`（agent 审批用结构化清单，非自然语言报告，沿用 00:25 偏好）。含：A 结构核验 / B 双链审计 / C 公开底座按对标轴盘点 / D 缺口（Apple 第三轴待定、B 层「可复用启发」未显式引用、标签约定不统一、NDA 不入库已固化）/ E 安全脚手架模板 / F 待审批。
- 未改主库笔记（用户 own-words 内容不替写、不替改）。下一步情报跑（21:00）不受影响。

## 2026-08-05（21:00 版，本次）

- **状态**：完成（A/B/D 三层落库 + 看板登记）。7 日滚动窗口 2026-07-30→08-05。Horizon MCP 仍全部 disconnected（**连续 7 日**），继续 WebSearch/WebFetch 直取官方源 + 本 Agent 自行综合，未调外部 gemini，无 429。
- **窗口内两条真增量（均 ≥7/10）**：
  - **① Windows Agent Launchers（7–8/10）** —— 本库此前未记录的系统级 Agent 注册表。基于 App Actions 框架 + ODR，通过 `com.microsoft.windows.ai.agentInfo` AppExtension 与 `odr.exe agent-info add/remove/list` 发布 agent 实体（区别于 ODR 既有的 MCP 连接器注册）。补齐 Windows 与 Apple/Android/HarmonyOS 在「应用向系统声明可被调用能力」层的对齐缺口；当前颗粒度是 agent 实体而非细粒度 intent/function。**已 WebFetch 官方 learn.microsoft.com 页核实行为口径**，无发布日期（博客 URL 经核实为 7522 build 共享贴）。
  - **② LFM2.5-2.6B（Liquid AI，2026-08-04，7/10）** —— on-device agentic 小模型，2.6B、<2.5GB、手机约 30 tok/s；使 LFM2.5 家族规模阶梯（230M/450M/2.6B/8B-A1B）完整。具体 BFCLv4 分数厂商自述 + 镜像站 benchlm.ai 56.9%，**待 Berkeley 官方榜复核**。
- **延续待办关闭（口径）**：**BFCL v4 权重公式经 EvalScope 官方文档交叉确认**（Agentic 40% / Multi-Turn 30% / Live+NonLive+Hallucination 各 10%），将 08-04 的「二手快照」升级为「已核实口径」（Berkeley 原文逐字仍待补）。
- **四大 OS 官方渠道经逐条复核无新增可执行 API**，已在 A 层显式列「已复核·无净新增」清单（Apple App Intents 2.0 / Android AppFunctions 实验态 / HarmonyOS ArkAF 06-17 窗口外 / Windows agentic security 四支柱一致）避免重复检索。
- **落库**：A 1（AppIntent 每日情报 2026-08-05）｜ B 既有增补 3（Windows Copilot Actions / Function Calling 端侧工具调用 / Local Agent Bench，追加不重复）｜ D 1（AppIntent 每日情报速览 2026-08-05）｜ 看板已登记「本次新增（2026-08-05）」。
- **运行纪律延续**：同日不重跑全窗口，只补净新增 + 显式列无净新增；新事实 vs 口径变化分类；未复现数字标「待补」，镜像站≠官方榜；双链指向既有 B 节点不新建重复。
- **⚠️ 待办**：
  - **【连续第 5 日未解，最高优先】四平台是否采纳意图元数据来源分级**（Apple `.appEntityIdentifier` 来源绑定/签名仍待补）。08-03 定的「改查安全白皮书 PDF」路径仍未跑完，下轮必须执行。
  - 核实 Agent Launchers 具体 Insider build 号 / 发布日期 / 是否受 08-02 记的 Experimental agentic features 同一 opt-in 开关管控。
  - 复核 LFM2.5-2.6B 的 BFCLv4 绝对值（厂商 + 镜像站 56.9%，需官方榜）。
  - 延续：Berkeley 官方 BFCL v4 博客原文、PrismML 技术报告、APOP 协议全文与对接、六方 Registry Checklist（仍仅 Android 填实）、Digital Omnibus 正式文本、HarmonyOS 银行 App 名、Per-Intent Privacy Manifest、荣耀 Robot Phone（8 月发布）、Måløy 类别级缓解。
