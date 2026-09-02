# 自动化执行记忆 · automation-1785426993325
# AppIntent 每日情报 → 知识飞轮（每日 09:00，hy3）

> 本文件记录高层执行摘要，供后续运行读取。不存放完整交付物正文。

## 角色与范围
系统级 Agent 与 OS 意图框架前沿情报官。每日检索过去 24h 内 Apple / Android / HarmonyOS / Windows 在「系统级意图框架 / 端侧 Agent 执行总线 / 设备侧 Planner 意图路由 / 跨应用 Intent 工作流 / 执行安全（XPIA、ODR、Confirmation UI）」的新进展，落库 Obsidian 知识飞轮。

## 落库分层约定（2026-08-06 起执行「日报索引化」）
- **A 原始资料 = 索引，不是容器**：`10-知识飞轮/A-原始资料/AppIntent 每日情报 YYYY-MM-DD.md` 只做**索引**——每条有价值信息 1 行（重要性 + 原子笔记链接 + 主题枢纽链接 + 一手来源），**禁止内联完整分析**。完整内容落 B 泛化概念。
- **每条信息 = 独立原子笔记（B 层）**：同一概念只在 B 有一处权威笔记（已存在则追加不新建）；正文必须外链到主题枢纽（如 [[Intent Router 语义路由]] / [[Agent Skills 技能范式 2026]] / [[意图框架·跨体系索引 MOC]]）。
- **防信息孤岛铁律**：A / D 层节点必须外链 ≥1 个 B 原子笔记或 MOC；B 笔记必须外链 ≥1 个主题枢纽 / MOC。原始资料不加工不链接 = 数字垃圾。
- B 泛化概念：`10-知识飞轮/B-泛化概念/`（用 `_模板/概念蒸馏.md`；已存在则**追加**不新建）
- C 可复用方法：`10-知识飞轮/C-可复用方法/`（用 `_模板/方法SOP.md`）
- D 输出内容：`10-知识飞轮/D-输出内容/`（用 `_模板/输出复盘.md`；速览须外链到对应 B 笔记，禁止 1 链接孤岛）
- 收尾：在 `10-知识飞轮/知识飞轮看板.md` 末尾「本次新增（日期）」区登记链接。
- 重构历史：2026-08-06 用户反馈日报过大+孤岛，确立索引化；08-05 日报已作为范本压成索引（内容零损失，全在 B 笔记）。

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

## 结构设计改进（2026-08-06 · 用户反馈，非情报跑）
- **反馈**：用户指出 AppIntent 每日情报日报节点过大且重复（正文 inline 重复 B 笔记内容）；A/D 层节点连线少=信息孤岛，时间久成数字垃圾。
- **新约定（已写入上方「落库分层约定」）**：日报=索引（每信息 1 行 + 原子笔记链接 + 主题枢纽链接 + 一手来源，禁内联分析）；每条信息=独立 B 原子笔记并外链主题枢纽（[[Intent Router 语义路由]]/[[Agent Skills 技能范式 2026]]/[[意图框架·跨体系索引 MOC]]）；A/D 必须外链 B/MOC 防孤岛。
- **范本**：08-05 日报已压成纯索引（内容全在 B 笔记，零损失）；D 速览 08-05 出链由 1 → 10+。
- **审计结论**：B 层健康（出链 13–16）；孤岛主因是 A 日报（内容黑洞）+ D 速览（少数 1 链接）。
- **待办（需用户确认）**：批量重构 07-31→08-04 共 7 期日报为索引；重构前须先核实每期内容是否已落 B 笔记（避免丢内容）。
- **已固化**：项目 `.workbuddy/memory/MEMORY.md` + 本文件落库分层约定。

## 全量深耕循环（vault-deepen · 2026-08-03 起，用户要求「一直循环直到手动停止」）

- **性质**：独立于每日情报采集的另一条循环线。对全库 137 篇做「拓展深度并延伸」（vault-deepen skill）。每轮读进度台账 `.workbuddy/memory/vault_deepen_progress.md` 下一批 pending → 逐篇深化+延伸 → 改 done；全部 done 后本轮 no-op 并报「✅ 全量深耕完成」。
- **优先级**：P1 B-泛化概念(30) → P2 01-笔记/手机AI智能体(12) → P3 知识飞轮 A/C/D → P4 01-笔记其余 → P5 02-项目。
- **方法论**：每篇补 反例与边界 / 开放问题 / 最新 2026 一手来源 / 与相邻概念关系，且**强制链 `[[意图框架·跨体系索引 MOC]]`**；修命名不一致（见 vault-deepen skill 映射 C）；不用子代理（曾 502）。
- **台账状态**：本文件只记每轮批次数与累计 done，不存全文。

### 2026-08-03 第 1 轮（本次，批量 8）
- 处理 P1 B 层前 8 篇：`A2A 端侧智能体协议` / `Agent Data Injection 数据注入攻击` / `Agent Skills 技能范式 2026` / `Agent Workspace 隔离执行` / `Agent 身份与硬件级审批` / `Agentic OS 意图调度内核` / `Android AppFunctions 设备侧意图 2026` / `Apple AppIntents Schema Protocol 2026`。
- 后两篇（Android AppFunctions / Apple AppIntents）此前已自带 `最新进展 / 反例与边界 / 开放问题 / MOC 链接`，本轮仅标记 done，未重复改动；其余 6 篇补齐 `[[意图框架·跨体系索引 MOC]]` 链接 + `反例与边界` 小节。
- 同步强化 MOC：新增 `Context Engineering 学习笔记`、`端侧大模型推理 学习笔记` 两行前向索引（库内已存在但未入索引的手写笔记）。
- 累计 done：**8 / 142**（台账含少量额外文件）。下一轮从 `Atomic Service 元服务` 续。
- 已知：EBUSY 偶发（Obsidian 索引锁文件），重试即成功，非阻塞。

## 2026-08-09（21:00 版，本次）

- **状态**：完成（A/B/D 三层落库 + 看板登记）。7 日滚动窗口 2026-08-03→08-09。Horizon MCP 仍全部 disconnected（**连续 9 日**），继续 WebSearch/WebFetch 直取官方源 + 本 Agent 自行综合，未调外部 gemini，无 429。
- **本期主线 = 库内空白补漏 + 2 条窗口真增量**：① **Windows Agent Framework / Microsoft Agent Framework 端侧 Agent 执行框架**（Build 2026-06-02 OS 级栈 Runtime/Store/Mesh/Copilot Workspace/Polaris + 2026-04-02 合并 SK+AutoGen 的 MAF SDK 1.0，本库此前无完整框架节点，新建 B）② **NowSecure iOS 27 App Intents 攻击面**（2026-08-05，AppSec 视角补 XPIA 可测清单）③ **AgentAntibody**（arXiv 2608.04053，2026-08-04，XPIA 学习型防御第④支）。
- **重新核验**：本 turn 上下文未带前次 fetch 原文，落库前用 WebSearch/WebFetch 重验三关键事实——确认官方名为「Microsoft Agent Framework」（非「Windows Agent Framework」俗称）、Windows Agent Runtime 2026-06 Insider 预览 / Store 85:15 / Mesh Q4 GA / Copilot Workspace GA / Polaris 8 月替换 GPT-4、NowSecure 2026-08-05 博客与 Session 347 映射、AgentAntibody 提交 2026-08-04 且带 bench 数字（AgentDojo ASR 3.8% / LBB 2.5%）。
- **四大 OS 官方渠道经复核无新增可执行 API**，已在 A 层显式列「已复核·无净新增」清单避免重复检索。
- **落库**：A 1（AppIntent 每日情报 2026-08-09）｜ B 净新增 2（Windows Agent Framework 端侧 Agent 执行框架 2026 / AgentAntibody 自适应免疫防御 2026）｜ B 既有增补 3（Apple AppIntents Schema Protocol 2026 / XPIA 跨提示注入 / Windows Copilot Actions 与 Agent Workspace 2026）｜ D 1（AppIntent 每日情报速览 2026-08-09）｜ 看板已登记「本次新增（2026-08-09）」。
- **运行纪律延续**：同日不重跑全窗口只补净新增 + 显式列无净新增；库内补漏标真实日期不冒充当日新闻；诚实标注 NowSecure 厂商视角 / AgentAntibody 预印本数字 / Windows 部分生态组件（MXC/Entra Agent Identity）第三方解读均「待官方确认」。
- **⚠️ 待办**：**【连续第 6 日未解·最高优先】四平台意图元数据来源分级**（Apple `.appEntityIdentifier` 仍待补，下轮必须执行「查各平台安全白皮书 PDF」路径）；Windows Agent Framework 官方 MIT 许可页 / Runtime Insider build 号 / Mesh GA 日期；NowSecure 厂商视角独立核验；AgentAntibody 预印本数字独立榜复现；Berkeley 官方 BFCL v4 博客原文。

## 2026-08-09（晚间增补跑）

- **性质**：同日 21:00 已跑完整 7 日窗口，本轮为**增补跑**。只记 21:00 版之后的净新增，并显式列「已复核·无净新增」清单。Horizon MCP 仍全部 disconnected（连续 9+ 日）。
- **四大 OS 官方渠道无新增**：Apple（support.apple.com fetch 仅返回目录页、无 App Intents 来源校验内容，已记未决）、Android（AppFunctions 实验态无变化）、HarmonyOS（ArkAF 06-17 窗口外）、Windows（agentic security 四支柱一致）。
- **真增量来自客户端/浏览器层（非 OS 层）**：**Chrome Agent Origin Sets**（Google 官方 security.googleblog.com，2025-12-08，Nathan Parker）——按任务会话的只读/读写源白名单集 + 隔离的 User Alignment Critic 双 LLM 确定性门控；经 WebSearch 精确定日 + mirror 全文 + TechCrunch 一手引用，官方 URL 逐字待补。
- **6 天最高优先待办第二次实质进展**：结论从「两层（研究层 ADI/DualView + 治理层 MS AGT）」精化为**三层（研究 + 治理 + 客户端/浏览器 Chrome 产品化）**，但四大 OS intent 层仍全空白。同时把「最低成本判据」收口为 OS PM 在意图 Registry 加 `readOrWrite` 声明位。
- **落库**：A 1（AppIntent 每日情报 2026-08-09-晚）｜ B 净新增 1（Chrome Agent Origin Sets 与用户对齐评判器 2026）｜ B 既有增补 4（Agent Data Injection / 带外防御与确定性门控 / XPIA 跨提示注入 / Confirmation UI 安全机制）｜ D 1（AppIntent 每日情报速览 2026-08-09-晚）｜ 看板已登记。
- **层级纪律（关键收获）**：Chrome 是浏览器、Origin Sets 未下沉到 Android AppFunctions——同属 Google 两家产品线成熟度不可混淆，这是最容易「误填」该 6 天待办的坑，本轮已显式规避并写入笔记。
- **⚠️ 待办**：**【连续第 7 日未解·最高优先】四平台意图元数据来源分级**（Apple `.appEntityIdentifier` 仍待补，下轮改查 Apple Platform Security 白皮书 PDF 全文 + WWDC26 Session 347 逐字稿，不走 support.apple.com 在线指南）；Chrome Origin Sets 官方 URL 逐字复核；Windows Agent Framework MIT 许可页/build 号；NowSecure/AgentAntibody 独立核验；Berkeley 官方 BFCL v4 博客原文。

## 2026-08-15（21:00 版，本次）

- **状态**：完成（A/B/D 三层落库 + 看板登记）。7 日滚动窗口 2026-08-09→08-15。Horizon MCP 仍全部 disconnected（连续 13+ 日），继续 WebSearch/WebFetch 直取官方源 + 本 Agent 自行综合，未调外部 gemini，无 429。
- **本期最重（8/10）：Trust Insights（WWDC26 Session 379，iOS 27）—— 执行安全第三元素**。Apple 首次给出「意图真实性 / 被胁迫意图」检测框架：`InsightEvaluator` / `IsLikelyBeingCoachedInsight` / 5 类 operationCategories / entitlement `com.apple.developer.trustinsights.base`。与 XPIA（注入指令）和 Confirmation UI（用户授权）**正交**，构成三元模型（注入 / 授权 / 意图真实性）。前 7 轮全漏，本轮补建净 B 节点。
- **关掉一个错误前提（最高优先待办连续第 7 日）**：逐条核验 Apple 官方文档，确认 `.appEntityIdentifier` 是「实体-视图链接（Session 343 View Annotations 的屏幕感知）」、**不是来源校验/签名**。四平台意图元数据来源分级仍全空白，待办不关闭，下轮改查 **Apple Platform Security 白皮书 PDF + Session 347 逐字稿**。
- **其余窗口真增量 / 补漏（均 5–6/10）**：iOS 27 Beta 5 App Intents 逐字变更（AttributedString name / calendar.deleteEvent 重命名 / AppEntity 10MB / 后台 Neural Engine entitlement `com.apple.developer.background-tasks.continued-processing.inference`，首条端侧 Planner 托管治理信号）；Android AppFunctions 真机有限预览（Galaxy S26 + Pixel 10，非 GA）；Windows Copilot Vision + 语义文件索引扩张 XPIA 读路径（应用层非 ODR 总线）；FunctionGemma 类端侧 router 部署路径（CoreML/LiteRT-LM ~283MB + 严格 `call:NAME{...}` 语法）。
- **四大 OS 官方渠道经复核无新增可执行 API**，已在 A 层显式列「已复核·无净新增」清单避免重复检索。
- **落库**：A 1（AppIntent 每日情报 2026-08-15）｜ B 净新增 1（Trust Insights 意图 coercion 检测框架 2026）｜ B 既有增补 6（Apple AppIntents Schema Protocol 2026 / Android AppFunctions 设备侧意图 2026 / Agent Data Injection 数据注入攻击 / XPIA 跨提示注入 / Confirmation UI 安全机制 / Function Calling 端侧工具调用）｜ D 1（AppIntent 每日情报速览 2026-08-15）｜ 看板已登记「本次新增（2026-08-15）」。
- **运行纪律延续**：同日不重跑全窗口只补净新增 + 显式列无净新增；库内补漏标真实日期；诚实标注预印本/媒体数字「待补」；双链指向既有 B 节点不新建重复；净新增 B 仅 Trust Insights 一个。
- **⚠️ 待办**：**【连续第 8 日未解·最高优先】四平台意图元数据来源分级**（Apple `.appEntityIdentifier` 已证伪为视图链接，下轮必跑 **Apple Platform Security 白皮书 PDF + Session 347 逐字稿**）；Watch OS 26 / 其他平台是否也有 Trust Insights 类意图真实性机制；Windows Agent Framework MIT 许可页/build 号；NowSecure / AgentAntibody 独立核验；Berkeley 官方 BFCL v4 博客原文；Chrome Origin Sets 官方 URL 逐字复核。

### 2026-08-16（21:00 版，本次）

- **状态**：完成（A/B/D 三层落库 + 看板登记）。7 日滚动窗口 2026-08-10→08-16。Horizon MCP 仍全部 disconnected（连续 14+ 日），继续 WebSearch/WebFetch 直取官方源 + 本 Agent 自行综合，未调外部 gemini，无 429。
- **本期最重（8/10）**：**Needle 2（Cactus Compute，2026-08 中旬发布）** —— 本窗口**唯一新增的端侧 router 模型**，45M 参数 / **CQ2-bit（从预训练起 2-bit）** / 14MB 二进制 / ~28MB RAM；带来两道安全闸：**置信度门控**（置信分 = min(校准头, 解码概率)，离线返回空调用 `[]`）+ **工具可达性收缩**（>5 工具时对比检索头只放行 top-5，未选中当轮不可达）。BFCL v4 42.6（Cactus 自述，归因于消费设备语料偏向，非官方榜）。已建净 B 节点 [[端侧 Router 置信度门控与工具可达性收缩 2026]]。
- **第②重（8/10）**：**Apple Session 347 风险元数据（副作用轴）+ 鉴权棘轮 + `createTimer` 持久化注入** —— `@AppIntent(schema:)` 自动继承 schema 副作用分类（destructive/exfiltration/shared-content update）；`authenticationPolicy` 只能更严不能更松（棘轮）；createTimer 可选 String label 经模型填参被注入、list timers 拉回污染新上下文 = ADI 具象实例。已建净 B 节点 [[意图风险元数据与鉴权策略棘轮 2026]]。
- **最高优先待办从「全空白」重构为两正交轴（核心收获）**：副作用轴（动作多危险）Apple 已解；来源/溯源轴（数据从哪来、可不可信）四平台 OS intent 层仍全空白。待办不关闭，但收窄为「来源轴」。最低成本补丁仍是意图 Registry 加 `readOrWrite` 声明位。
- **四大 OS 官方渠道经复核无新增可执行 API**，已在 A 层显式列「已复核·无净新增」清单避免重复检索。
- **排除 4 条（过滤纪律）**：LightAgent v0.10.0 / DeepSeek Harness / OmniBot / PalmClaw 均应用层 agent 框架，非 OS 意图框架/端侧路由/执行安全，低于阈值排除。
- **第三方 corroboration（非官方）**：agentinterface.app tracker（2026-08-13）确认 Windows Copilot Actions 铺开 Insiders（opt-in 默认关）+ Apple 弃用 SiriKit；仅综述，须以 Microsoft 官方源复核。
- **落库**：A 1（AppIntent 每日情报 2026-08-16）｜ B 净新增 2（意图风险元数据与鉴权策略棘轮 2026 / 端侧 Router 置信度门控与工具可达性收缩 2026）｜ B 既有增补 7（Apple AppIntents / Confirmation UI / ADI / SAN / Function Calling / Windows Copilot Actions / 数据溯源分级与单调棘轮）｜ D 1（AppIntent 每日情报速览 2026-08-16）｜ 看板已登记「本次新增（2026-08-16）」。
- **运行纪律延续**：同日不重跑全窗口只补净新增 + 显式列无净新增；库内补漏标真实日期（Needle 2 标 2026-08 中旬，厂商自述数字标非官方榜）；诚实标注媒体数字「待补」；双链指向既有 B 节点不新建重复；净新增 B 仅 2（均为窗口内/补漏高价值，无重复）。
- **⚠️ 待办（两轴化）**：**【来源轴仍空白·最高优先】四平台意图元数据来源分级**（副作用轴 Apple 已解；来源轴 Apple `.appEntityIdentifier` 证伪为视图链接、Android `app_metadata` / HarmonyOS A2A / Windows 工具响应均无来源类型字段）；Needle 2 BFCL v4 42.6 厂商自述非官方榜；Windows Copilot Actions Insider build 号；Watch OS 26 是否 Trust Insights 类；Windows Agent Framework MIT 许可页/build 号；NowSecure / AgentAntibody 独立核验；Berkeley 官方 BFCL v4 博客原文；Chrome Origin Sets 官方 URL 逐字复核。

### 2026-08-17（21:00 版，本次）

- **状态**：完成（A/B/D 三层落库 + 看板登记）。7 日滚动窗口 2026-08-11→08-17。Horizon MCP 仍全部 disconnected（连续 15+ 日），继续 WebSearch/WebFetch 直取官方源 + 本 Agent 自行综合，未调外部 gemini，无 429。
- **本期最重（8/10）：连续第 8 日最高优先待办「四平台意图元数据来源分级」收口为确认结论** —— 经逐平台核验（Apple Session 347 逐字稿 / Android AppFunctions 元数据 / HarmonyOS insight_intent.json / Windows ODR connector 元数据），**四平台 OS intent Registry 层均无「数据来源 / 可信度」元数据字段**，来源轴空白从「待查」升级为「**架构性空白（confirmed）**」。Apple 用「副作用轴风险元数据 + 零信任输入处理（spotlighting/脱敏）」回答「动作多危险 / 数据可不可信」，但 Registry 本身不记 provenance；最低成本补丁仍是意图 Registry 加 `readOrWrite` 声明位，仍非完整 provenance。已建净 B 节点 [[四平台意图 Registry 来源轴与权限模型对比 2026]]。
- **库内空白补漏 5 条（标真实日期·非 24h 新公告）**：① Apple **Core AI 框架（OS 级模型运行时，Apple Silicon / MSL Swift / AOT / 零服务器依赖）+ Dynamic Profiles（会话内切换模型/工具）+ 多模型 Foundation Models（Claude/Gemini 经 Language Model 协议）+ Evaluations 框架**（iOS 27 指南，2026-06）；② Session 347 逐字稿补 Foundation Models 侧确定性护栏 `.onToolCall`（执行前拦截）/ `.historyTransform`（spotlighting+脱敏）；③ **Apple Secure Enclave「Secure intent」硬件确认锚点**（物理按键→Secure Enclave，绕过 OS/AP，root 不可伪造）；④ **HarmonyOS A2UI 生成式 UI 精确定义 + insight_intent.json 三步（定义→注册→执行）+ 1200 底层能力 Skill 化**（HDC2026/2026-06，口径冲突 2100+ vs 1200+ 延续标注）；⑤ Needle 2 发布日锚定 2026-08-11 + Pebble Index 01 量产落地 + SAN arXiv 2607.18363。
- **四大 OS 官方渠道经复核无新增可执行 API**，已在 A 层显式列「已复核·无净新增」清单避免重复检索；Windows 8-14 Copilot 改名 / 8-11 Patch Tuesday 属常规/安全更新，低于阈值排除。
- **落库**：A 1（AppIntent 每日情报 2026-08-17）｜ B 净新增 1（四平台意图 Registry 来源轴与权限模型对比 2026）｜ B 既有增补 6（Apple AppIntents Schema Protocol 2026 / 意图风险元数据与鉴权策略棘轮 2026 / Confirmation UI 安全机制 / HarmonyOS Intents Kit 与 ArkAF 2026 / 端侧 Router 置信度门控与工具可达性收缩 2026 / Function Calling 端侧工具调用）｜ D 1（AppIntent 每日情报速览 2026-08-17）｜ 看板已登记「本次新增（2026-08-17）」。
- **运行纪律延续**：同日不重跑全窗口只补净新增 + 显式列无净新增；库内补漏标真实日期；诚实标注厂商/第三方数字「待补」（Needle 2 BFCL v4 42.6 / FunctionGemma v4 第三方聚合 27.03 均标非官方榜）；双链指向既有 B 节点不新建重复。
- **⚠️ 待办**：Berkeley 官方 BFCL v4 博客原文；Windows Agent Framework MIT 许可页/build 号；Watch OS 26 是否 Trust Insights 类；NowSecure / AgentAntibody 独立核验；Chrome Origin Sets 官方 URL 逐字复核；HarmonyOS `insight_intent.json` 字段全量 + API level 冲突（26 vs 23）澄清；各平台具体 entitlement/字段名以官方文档为准。

### 2026-08-26（21:00 版，本次）

- **状态**：完成（A/B/D 三层落库 + 看板登记）。7 日滚动窗口 2026-08-19→08-26。Horizon MCP 仍全部 disconnected（连续 20+ 日），继续 WebSearch/WebFetch 直取官方源 + 本 Agent 自行综合，未调外部 gemini，无 429。
- **本期主线（两条 ★7/10）**：① Apple **App Intents Testing 框架（iOS 27 Beta）** —— 进程外类型擦除 API（`AnyAppIntent/AnyAppEntity/AnyEntityQuery`/`AnyAppEnum`/`AnyTransientAppEntity`）+ `ViewAnnotation` 测试，把意图集成质量/安全验证左移到发布前；② **IFFC 解耦路由范式（arXiv 2608.22472，2026-08）** —— 工具选择从主 LLM 解耦为独立 SRM（0.5B–15B）+ 用「指令遵循上下文」替代「工具调用上下文」提升小模型路由准确率，为端侧 Planner 提供架构级解法。已建净 B 节点 [[端侧函数调用解耦路由与指令遵循范式 IFFC 2026]]。
- **四条 ★6/10 上下文（均补库）**：BFCL v4 公开榜 08-22 快照（LFM2.5-2.6B 56.9% / Needle 2 42.6% / Nexus-TinyFunction-1.2B 94.25% simple）+ LFM2.5-350M 微调 96–98%；CSA web 级 IPI（月 20–30 亿页 / 2025-11→2026-02 +32%）+ Black Hat USA 2026「每个 AI 浏览器都脆弱」；HarmonyOS 端侧 Skill 同名冲突静默优先端侧 / 3 秒超时 / A2UI 静默失败；Samsung Gallery + Gemini AppFunctions 真机闭环 + UI Automation 兜底框架。
- **四大 OS 官方渠道经复核无新增可执行 API**（iOS 27 Beta 7 仅修 Bug / AppFunctions alpha10 稳定 / HarmonyOS 7 SP8 消费版 / Windows 四支柱一致），已在 A 层显式列「已复核·无净新增」清单避免重复检索。
- **落库**：A 1（AppIntent 每日情报 2026-08-26）｜ B 净新增 1（端侧函数调用解耦路由与指令遵循范式 IFFC 2026）｜ B 既有增补 5（Apple AppIntents Schema Protocol 2026 / Android AppFunctions 设备侧意图 2026 / HarmonyOS Intents Kit 与 ArkAF 2026 / Function Calling 端侧工具调用 / XPIA 跨提示注入）｜ D 1（AppIntent 每日情报速览 2026-08-26）｜ 看板已登记「本次新增（2026-08-26）」。
- **运行纪律延续**：同日不重跑全窗口只补净新增 + 显式列无净新增；库内补漏标真实日期；诚实标注厂商/第三方数字（CDN 镜像域 `msc-/ma-kobol-public-prod.apple.com`、安全研究引用）；双链指向既有 B 节点不新建重复；净新增 B 仅 IFFC 一个。
- **⚠️ 待办**：核验 App Intents Testing canonical 路径与最小 iOS 27 Beta 版本（本轮命中 CDN 镜像域）；IFFC 是否给出 BFCL v4（当前仅 v3）；CSA 数据回流至 [[Agent 读入路径可信数据边界 SOP]]；Berkeley 官方 BFCL v4 博客原文；Watch OS 26 是否 Trust Insights 类；NowSecure / AgentAntibody 独立核验；Chrome Origin Sets 官方 URL 逐字复核；六方 Registry/权限 Checklist（仍仅 Android 填全）。

## 2026-08-31（21:00 版，本次）

- **状态**：完成（A/B/D 三层落库 + 看板登记）。7 日滚动窗口 2026-08-25→08-31。Horizon MCP 仍全部 disconnected（连续 21+ 日），继续 WebSearch/WebFetch 直取官方源 + 本 Agent 综合，未调外部 gemini，无 429。
- **窗口内四平台 OS 官方框架层经逐条复核无净新增 API**：Apple iOS 27 Beta 8 Release Notes 的 App Intents 段落（含 `notes.createNote`/`notes.updateNote` 的 `AttributedString` name 参数）与 08-15 已录 Beta 5 **逐字一致（同 bug 号 173431080）**，初检误判为净新增、比对后确认已覆盖，不重复计数；Android AppFunctions 守 alpha10；HarmonyOS 7 消费版无新 API；Windows agentic security 四支柱一致；BFCL v4 公开榜端侧分数均已在 08-26 入表。**关键纪律**：遇到「Beta N 新功能」必须先与库内既有 Beta 记录按 bug 号去重。
- **核心产出（★8/10 分析价值）= 收口悬挂 8+ 天的最高优先待办**：「Per-Intent Privacy Manifest 是否真实 App Intents API」经**官方文档直查 + 多源检索**判定为「**不存在**」——WebFetch 官方 App Intents 框架文档 + Privacy manifest files 文档均无 per-intent 隐私/路由声明接口（iOS 17 起仅有通用 `PrivacyInfo.xcprivacy`，与意图路由无关）；第三方博客（byteiota SiriKit 弃用文）说法系误读 iOS 17 通用隐私清单 / 未来推测。原 08-02「待官方确认」升级为「confirmed non-existent」。不新建 B 节点（负结果归并至既有来源轴对比笔记）。
- **落库**：A 1（AppIntent 每日情报 2026-08-31）｜ B 既有增补 1（四平台意图 Registry 来源轴与权限模型对比 2026，Per-Intent Privacy Manifest 证伪 + 来源轴待办收口）｜ D 1（AppIntent 每日情报速览 2026-08-31）｜ 看板已登记「本次新增（2026-08-31）」。本窗口**净新增 B 节点 = 0**（无通过阈值的全新概念，全部为待办收口 + 无净新增复核）。
- **运行纪律延续**：同日不重跑全窗口只补净新增 + 显式列无净新增；诚实标注 Beta 8 无净新增 / Per-Intent Privacy Manifest 已证伪 / BFCL v4 数字已在 08-26；双链指向既有 B 节点不新建重复。
- **⚠️ 待办**：若 iOS 27 正式版（约 2026-09-14）新增 per-intent 路由/来源声明 API，重评来源轴结论；把「来源轴空白 + Per-Intent Privacy Manifest 证伪」回流至 [[Agent 读入路径可信数据边界 SOP]]；延续 Berkeley 官方 BFCL v4 博客原文、Watch OS 26 Trust Insights 类、NowSecure/AgentAntibody 复核、Chrome Origin Sets 官方 URL 逐字复核。
