---
type: raw
status: inbox
date: 2026-08-01
captured: 2026-08-01
importance_score: ★★★★★
intent_category: 系统级意图框架 / 端侧 Planner 意图路由 / 跨应用 Intent 工作流 / 执行安全（XPIA）
source:
  - "https://enklypesalt.com/posts/context-collapse-part3-ai-worming-through-word/ （Håkon Måløy《Context Collapse, Part 3》原始披露 2026-07-28）"
  - "https://explainx.ai/blog/copilot-word-document-ai-worm-xpia-july-2026 （Copilot for Word AI 蠕虫 XPIA 拆解 2026-07-29）"
  - "https://news.ycombinator.com/item?id=49096188 （HN 讨论：指令/数据边界之争）"
  - "https://arxiv.org/abs/2403.02817 （Morris II：邮件助手蠕虫，先例）"
  - "https://cactuscompute.com/blog/needle （Cactus Compute：Needle 26M 函数调用模型官方公告）"
  - "https://github.com/cactus-compute/needle （Needle 源码与 Simple Attention Networks 架构文档）"
  - "https://huggingface.co/Cactus-Compute/needle （Needle 权重，MIT）"
  - "http://rits.shanghai.nyu.edu/ai/cactus-releases-needle-a-26m-distilled-model-for-on-device-tool-calling （Needle 架构第三方拆解）"
  - "https://developer.apple.com/cn/videos/play/wwdc2026/345 （WWDC26 Session 345：探索 App Intents 框架的新功能）"
  - "https://www.honor.com/cn/news/honor-waic-2026 （荣耀官方：WAIC 2026 发布 Agentic OS 与 Robot Phone）"
  - "https://mobile.it168.com/a2026/0718/6941/000006941659.shtml （荣耀 Agentic OS 全栈技术揭秘，黄非演讲实录）"
  - "https://www.ceweekly.cn/economic/industry/2026/0714/497277.html （阶跃星辰 Step AOS 发布 2026-07-13）"
  - "https://chinaainews.org/news/stepfun-launches-step-aos-the-first-agent-native-operating-system （Step AOS 英文技术要点）"
  - "https://www.techtimes.com/articles/321574/20260725/how-droiclaw-building-ai-native-operating-system-agentic-era.htm （DroiClaw 诸葛：AI 原生 OS）"
  - "https://cloud.tencent.com/developer/news/4355852 （DroiClaw 获路透社/TechCrunch 报道，2026-07-31 11:26）"
  - "https://m.gelonghui.com/p/5248344 （鸿蒙负一屏元服务与 Today-Task Skill，HDC 2026）"
  - "https://developer.android.google.cn/ai/appfunctions （AppFunctions 官方文档，本次无 24h 增量）"
  - "https://learn.microsoft.com/windows/security/book/operating-system-agentic-security （Windows 智能体安全，本次无官方文档增量）"
tags: [AppIntent, OS-Agent, 端侧Planner, 执行安全, XPIA, AgenticOS, 每日情报, 跨平台2026]
---

# AppIntent 每日情报（2026-08-01）

> [!abstract] 30 秒速览
> **核心突破**：三条主线同时出现质变——① **执行安全**：Copilot for Word 被证实存在**可自我传播的文档型 XPIA 蠕虫**，MSRC 协调披露 **144 天后漏洞类别仍未关闭**，模型从 GPT-5.5 升到 GPT-5.6 依然可复现，这是 OS Agent 安全叙事从「单次注入」升级为「**注入会自我复制**」的分水岭；② **端侧 Planner**：Cactus Compute 开源 **Needle——26M 参数、INT4 仅 14MB、完全没有 FFN 层**的函数调用模型，单次工具调用击败 FunctionGemma-270M / Qwen-0.6B / Granite-350M / LFM2.5-350M，论证「**工具调用是检索-组装任务，不是推理任务**」；③ **意图调度内核**：荣耀 AgenticOS、阶跃 Step AOS、卓易 DroiClaw 三家在一个月内先后宣布把 OS **调度对象从「进程/线程」改为「意图/任务」**，四大平台之外冒出第五类玩家。
> **关键指标**：Needle 6000 tok/s prefill、1200 tok/s decode，预训练 200B token / 16×TPU v6e / 27 小时，后训练 2B token / 45 分钟，MIT 开源；Word 蠕虫披露周期 144 天、两轮缓解均失败；Step Edge 端侧模型简单任务 <100ms、成功率 >99%（厂商口径）；鸿蒙负一屏 MAU 1.9 亿。
> **OS Agent 场景**：一句话跨 App 全流程（Step AOS × 携程/滴滴/美团/支付宝/WPS/剪映）；自然语言直驱**物理执行器**（荣耀 OpenClaw 把 4DoF 云台定义为智能体标准执行器）；千元档普惠 AI OS（DroiClaw 首发 999 元）；而所有这些「写回能力」正是 Word 蠕虫所揭示的攻击放大器。

## 检索与口径说明（诚实标注）

- **窗口**：严格 24h（2026-07-31 09:00 → 08-01 09:00）**硬命中仅 1 条**（DroiClaw 获海外主流媒体集中报道，腾讯云开发者社区 07-31 11:26 转载）。**这是连续第二天 24h 窗口过薄**，建议把自动化改为 **7 日滚动窗口**（详见「后续动作」）。
- **补漏**：另有 **6 条**为库内完全空白、但对本主题至关重要的进展，**逐条标注真实日期**，绝不冒充当日新闻。
- **信息源**：Horizon MCP 未出现在连接器列表中（不可用），改用 WebSearch/WebFetch 直取官方源（Apple 开发者站、Cactus 官方博客与 GitHub、荣耀官网、MSRC 协调披露原文链路）。合成由本 Agent 完成，未消耗外部分析额度。
- **厂商自述数据一律标注口径**，未经独立核验的名次与分数标「待补」。

---

## 原始内容

### 一、24h 真增量（2026-07-31 → 08-01）

#### 1. DroiClaw 诸葛：第三方 AI 原生 OS 供应商登上国际视野 ★★★☆☆
- **24h 事实**：路透社发表《Shanghai Droi Technology Launches DroiClaw AI Operating System with Hybrid Edge-Cloud Architecture》，TechCrunch 发表《How DroiClaw Is Building an AI-Native Operating System for the Agentic Era》，New Atlas / Dataconomy / Analytics Insight / TechTimes / Digital Trends / TechRadar 同期跟进（国内转载 07-31 11:26）。
- **产品事实（2026-06 发布，非 24h）**：上海卓易科技出品，中文名「诸葛」；首发机型 **酷派小方块 / 飞利浦小方块，售价 999 元**；采用「本地小模型 + 云端大模型」端云协同；**model-agnostic**，兼容通义千问、智谱 GLM、Kimi，支持私有模型部署；**APEX 模块化热更新**让 AI 能力静默升级、无需整机刷机。
- **为什么值得记（OS PM 视角）**：这是四大 OS 之外的**第三类角色——「给中小品牌做 AI OS 的中间层供应商」**。卓易累计装机超 2 亿台，靠的不是自有终端而是**方案输出**。它把「意图驱动 OS」从旗舰特权打到千元档，也把合规（EU AI Act 2026-08 落地）做成了可复用的底层能力：分层数据保护 + 灵活模型切换 + 全流程权限审计。
- ⚠️ 口径：装机量、隐私本地留存率均为厂商/媒体口径，**未独立核验（待补）**。

---

### 二、库内空白补漏（非 24h，已标真实日期）

#### 2. Copilot for Word 文档型 XPIA 蠕虫：披露 144 天，漏洞「类别」仍未关闭（2026-07-28/29）★★★★★

**这是本期最高价值条目，也是 OS Agent 执行安全的范式转折点。**

- **披露**：安全研究者 **Håkon Måløy** 发布 *Context Collapse, Part 3: AI Worming through Word*，与 Microsoft MSRC **协调披露**；HN 热议（id=49096188）。
- **攻击本质**：**XPIA + 传播阶段**。不是「Copilot 说错一次话」，而是恶意指令会**把自己复制进被生成的新文档**，形成载体链。
- **攻击链**：
  1. 攻击者分享一份**普通 .docx**（邮件 / SharePoint / Teams / 合作方交接），**不需要受害者的 M365 租户权限**；
  2. 载荷用**白底白字 / 极小字号**隐藏 —— 关键点：**Copilot for Word 在送入 LLM 前会剥离颜色与字号**，于是「人眼不可见、模型完全可见」；
  3. **Stage 1 立足**：Copilot 把文档里的指令当成权威指令执行（PoC 演示中把财务数字腰斩），且**不提示用户数字被改**；
  4. **Stage 2 蠕虫**：受污染的内部文档成为新载体。同事基于这份「可信的 Q1 报告」起草 Q2，**即使原始攻击文件已不在场**，Copilot 会再次改数并重新植入白字指令 —— **溯源彻底崩塌，每个载体看起来都是合法的内部创作事件**。
- **披露时间线（说明「为什么至今仍开放」）**：

  | 日期 | 事件 |
  |---|---|
  | 2026-03-06 | 首次 MSRC 报告 + PoC |
  | 2026-03-31 | 微软确认行为，启动缓解 |
  | 2026-04-03~09 | 第一轮缓解（Edit with Copilot）；原措辞被拦，**新的财务操纵变体成立** |
  | 2026-06-08 | 应微软要求推迟披露 |
  | 2026-07-14 | 第二轮缓解：**模型升级到 GPT-5.5** |
  | 2026-07-15 | **在 GPT-5.6 上复现利用与蠕虫行为**，披露推迟至 7-28 |
  | 2026-07-28 | 类别级公开披露，攻击**仍可复现** |

- **作者核心论断（架构层面）**：要使用附件，模型必须把**攻击者 token 与用户请求放进同一个上下文**；等模型「判断这是不是攻击」时，那些 token **已经参与了这个判断**。这更像「运行程序才能知道它安不安全」，而非经典沙箱策略。「**用比目标 LLM 更弱的检测器，必然留下表征缺口；把 LLM 层层堆成盾牌，就变成 LLMs all the way down**」。
- **与既有认知的关系**：先例是 **Morris II**（邮件助手蠕虫，arXiv:2403.02817）；HN 引用 Simon Willison 的 **lethal trifecta**（私有数据 + 不可信内容 + 外发/执行能力）。本例的「行动」是**改写可信工作产物并为下一次会话重新埋雷** —— 属**完整性损害**，没有经典的数据外发 webhook，因此更难被 DLP 发现。
- **系列上下文**：Part 1（污染 Copilot 记忆）已缓解；Part 2（邮件正文 XPIA / CVE-2026-55145 范畴）有较强缓解；**Part 3 的「传播」类别未关闭**。
- **企业侧结论（原文明确）**：**没有任何客户侧开关能完整解决该类别**，只能靠卫生措施降低频率。给 CISO 的诚实答案是：「**载荷修了，类别没修**」。
- ⚠️ 与本库的直接互文：这正好击中 [[Agent Workspace 隔离执行]] 的边界 —— **隔离解决「执行域泄漏」，但解决不了「被污染的产物在人际间正常流转」**。

#### 3. Needle：26M 参数、无 FFN 的端侧函数调用模型（Cactus Compute，GitHub 提交 2026-05-12~16；7 月底经聚合媒体二次扩散）★★★★★

- **是什么**：Cactus Compute 从 **Gemini 3.1 Flash Lite 蒸馏**出的 **26M 参数**单次函数调用模型，**MIT 全开源**（权重 + 数据生成脚本）。INT4 量化后 **仅 14MB**，小到可放进桌面 CPU 的 L3 缓存。
- **架构创新 —— Simple Attention Network（SAN）**：**整个模型没有任何 MLP/FFN 层**，只有注意力与门控。
  - 编码器 **12 层（无 FFN）** + 解码器 **8 层**（masked self-attention + cross-attention）；
  - `d=512`，**8 注意力头 / 4 KV 头（GQA）**，BPE 词表 **8192**，RoPE 位置编码，编码器与输出投影**共享嵌入权重**；
  - 门控残差 `x + sigmoid(gate)·Attn(Norm(x))`，gate 初始化为 0；QK 头上用 **ZCRMSNorm** 稳定训练；
  - 一个 **CLIP 式对比学习的工具选择头**，用于从大工具集中先筛出相关工具；
  - **Muon 优化器** + 线性投影正交约束（防表征坍缩）；每 100 步注入 **INT4 量化感知训练**作为正则噪声。
- **设计论断（对 OS PM 最重要的一句）**：**「工具调用本质是检索与组装（把 query 匹配到工具名、抽取参数值、输出 JSON），不是推理。」** 既然事实已在输入里（工具 schema 就在 prompt 中），模型就不需要用 FFN 权重去记忆世界知识。去掉 MLP 砍掉了约 **2/3 参数量**。
  - 团队进一步称：**「无 FFN」结论可推广到任何模型能访问外部结构化知识的任务**（RAG、工具调用、检索增强生成）。实验结果**将随后发表（待补）**。
- **训练成本**：预训练 **200B token / 16 × TPU v6e / 27 小时**；后训练 **2B token 合成函数调用数据 / 45 分钟**；数据由 **Gemini 跨 15 个工具类别**（计时器、消息、导航、智能家居等）合成 —— 典型的「**把前沿模型当数据引擎，而不是当运行时依赖**」。
- **性能**：**6000 tok/s prefill、1200 tok/s decode**（在 Cactus 自家运行时上）。单次函数调用**优于 FunctionGemma-270M、Qwen-0.6B、Granite-350M、LFM2.5-350M** —— 这些模型比它大一个数量级。
- ⚠️ **口径纪律（延续本库规矩）**：
  - 上述对比为 **Cactus 自述、单次（single-shot）函数调用场景**，**不是官方 BFCL 榜单行**，不可与 BFCL 分数并列（**具体测试集与数值待补**）。
  - 团队自己明确说明：**那些更大的模型在对话场景下 scope/capacity 更强**，Needle 是窄域专才，「小模型会挑食（finicky）」，建议在自己的工具集上实测并微调。
  - 时间口径：GitHub 提交显示 **2026-05-12~16**，Cactus 官网首页仍挂 [NEW]；**7 月底由聚合媒体二次扩散**，故此前未进入本库。**不是 24h 新闻**。
- **产品化上下文**：Cactus 同时提供 **Hybrid Router** —— 按复杂度在端侧/云端之间路由函数调用，宣称 **5× 成本节省、端侧 <120ms 延迟**；跨 iOS / Android / macOS / 可穿戴单一 SDK。这与本库既有的「本地优先 + 低置信升级」架构完全同构。

#### 4. 荣耀 AgenticOS：调度对象从「进程/线程」升级为「意图/任务」（WAIC 2026-07-18；Robot Phone 8 月发售）★★★★☆

- **定位**：MagicOS 升维为**行业首个「伙伴型多模态智能体操作系统」**；荣耀首席 AI 科学家**黄非**发布技术框架。核心一句：「**不是在系统里加一个 AI 助手，而是重构一个以『意图』和『任务』为中心的新型操作系统。**」
- **六层全栈重构**：硬件抽象层 → AI 内核层 → 大模型层 → **Agent 框架层** → 交互层 → 生态层。
  - **调度的对象从进程、线程变成意图与任务**；
  - **内核管理的资源从内存、算力扩展到模型与智能体**；
  - Agent 框架层含**感知 / 规划 / 行动 / 工具 / 记忆**完整 LOOP，外加全局多智能体协同、认知记忆自适应沉淀、场景自循环三大能力。
  - 黄非的判词：「这是 **AI 原生操作系统与装了 AI 的操作系统的分水岭**。」
- **范式图示（值得直接引用）**：「意图进来，系统理解、调度、拆解、闭环，而**应用、服务、数据、设备、Agent 从『用户要面对的入口』转换为『系统要调用的资源』**。」
- **四大特征**：意图驱动 / 自然交互（声音·手势·眼神·动作**多通道叠加消除歧义**）/ 主动智能 / 天生跨端。
- **跨端三机制**：**统一记忆**（上下文归属于人而非某台机器）、**能力分布**（屏幕/传感器/算力都可被 OS 调度）、**任务迁移**（活派给最合适的节点，**失败后可换端重试**）。
- **一主多专、三端协同**：一个随身主智能体 + 海量终端 + 垂域生态 + 云端超算大脑。
- **物理执行器**：Robot Phone 内置行业最小 **4DoF 钛合金机械云台**（比主流方案缩小 70%、0.8 秒弹出、360° 追踪、CIPA 5.5 级防抖、步行抖动补偿率 96%）。真正的架构决策是：**通过 OpenClaw 开放平台把云台定义为 AgenticOS 智能体的标准化物理执行器** —— 开发者不写电机控制代码，用自然语言描述动作意图，系统负责翻译成物理指令。闭环：多模态感知 → 意图推理 → 任务决策 → **硬件执行** → 结果反馈。
- **第三方评价**：中国工程院院士**郑纬民**概括为「不是在传统 OS 上重做，而是在上面**加了一层认知软件层**，专门管智能体的全流程调度、协作与安全」。
- **模型侧**：六大自研大模型矩阵；自动执行智能体 / 端侧多模态 / 智能体模型分别登 **MobileWorld、MMBench、ACEBench** 榜单；与阿里千问（达摩院）共创 **端侧 Omni、端侧 VLM、Agentic Pro、Agentic Fast、GUI Agent** 多版本。⚠️ **具体名次与分数官方未公布，待补。**
- **落地节奏**：AgenticOS 内核**首发于 8 月发售的荣耀 Robot Phone**；**Q4 Magic9 系列**上线尝鲜版。

#### 5. 阶跃星辰 Step AOS：为智能体「盖房子」而非「开门」（2026-07-13，MWC 上海）★★★★☆

- **发布物**：全球首个**智能体原生操作系统 Step AOS**（Step Agentic-native OS）+ 个人智能体 **Amoo** + AI 终端品牌 **STEPX** + 首款机型 **STEPX Neo**。构成「模型—系统—硬件」三位一体闭环。
- **金句（董事长印奇）**：「**在旧系统上给智能体开一扇门，它永远是访客；为智能体盖一座房子，它才是原住民。**」判断 AI 原生的标准：「**去掉 AI 还是一部完整传统手机，那就只是功能升级。**」
- **关键定位澄清**：Step AOS **并非替代 Android**，而是**架设在现有系统之上**，对内核调度、数据体系、安全架构做深度改造。
- **三层重构**：
  - **计算**：统一计算资源池调度 CPU/GPU/NPU 异构算力，端云弹性供给；
  - **数据**：**统一语义数据层**把感知、行为与个人数据加工为统一语义文件，打破 App 数据孤岛；
  - **应用与服务**：**原子能力引擎**把系统功能与服务拆解为**数千个原子化服务单元**，配统一协议开放平台。
- **智能体工具调度框架**：**兼容 MCP 与 A2A 协议**，Amoo 直接调用与编排原子单元，**而非模拟点击** —— 与 [[端侧执行通道 GUI 与 MCP 路线之争]] 中的「结构化通道」阵营一致。
- **记忆**：**双域三步记忆结构**（用户域 + 智能体域；记录—整理—召回），短/中/长期上下文。厂商口径：**PersonalMem / LongMemEval 达 SOTA**，简单查询召回 **10.3ms**，复杂 **800ms**。
- **端云路由**：**Step Edge** 端侧基座模型，简单任务（设闹钟、找照片、开 App）**<100ms 响应、成功率 >99%**；复杂任务升级云端 Pro / Flash 模型；宣称在 **29 项权威基准中位列同类端侧模型第一**。⚠️ 全为厂商口径，**基准清单与对比对象待补**。
- **四维安全框架（对 [[Confirmation UI 安全机制]] 是重要补充）**：
  - **可信** —— 数据本地加密不出设备；
  - **可见** —— 每一步操作全程可审计追溯；
  - **可控** —— **权限按需授予，任务结束自动回收**；
  - **可逆** —— 操作出错**支持一键撤回**与任务中止。
  - 「可逆」是本库此前完全没有的维度：Confirmation UI 解决「执行前」，**Undo 解决「执行后」**。
- **合规与标准**：STEPX Neo 称是**唯一通过《人工智能终端智能化分级》L3 最高等级认证**的智能体手机；联合上海人工智能实验室发布《新一代智能体系统安全技术白皮书》《端侧大模型网络安全指南》，并牵头制定行业安全国家标准。⚠️ 标准编号与认证机构**待补**。
- **生态**：首批伙伴 **美团、支付宝、滴滴、携程、WPS、剪映**。8 月中旬联合 B 站发起「STEPX 狂想计划」，开放 **Agent / Skill 开发共创**。

#### 6. Apple WWDC26 Session 345 代码级细节补齐（2026-06，面向「2027 年新版本」）★★★★☆

> 库内此前**只记录了 API 名称**（见 [[Apple AppIntents Schema Protocol 2026]]），本次补齐**用法、机制与性能语义**。⚠️ Apple 原视频只说「2027 年的新版本」，**未给出具体系统版本号（待补）**。

| API | 解决什么问题 | 用法要点 |
|---|---|---|
| `ValueRepresentation` | Transferable 只能传「有文件格式的数据」，无法把**无格式的结构化类型**跨 App 传递（如地标坐标传给 Maps） | 与既有 Transferable 表示并列添加；可用闭包导出 `PlaceDescriptor`（GeoToolbox），若实体已有该 `@Property` 则**直接用 key path** |
| `RelevantEntities` | 全新内容既没被 Spotlight 搜过、也没有交互可捐献，系统无从推荐 | 确定实体 → 建上下文（如 `AppEntityContext.audio(.workout(activityType: .running))`）→ `updateEntities` 注册；`removeAllEntities(for:)` 移除 |
| `EntityCollection` | Intent 执行前系统会**解析每一个实体**（调查询、填全属性），批量场景灾难 | 参数类型从 `[PhotoEntity]` 改为 `EntityCollection<PhotoEntity>`，**只传标识符**给 `perform`；官方演示「查找并标记 1000 张照片」，改后**近乎瞬时**（⚠️ 原视频**未给具体秒数**） |
| `SyncableEntity` | 各设备本地生成的 ID 不同，Siri 跨设备续接对话时找不到同一实体 | ID 已稳定（服务器 UUID / CloudKit record ID）则只需加协议；本地 ID（如 CoreData 行 ID）用 `SyncableEntityIdentifier<Local, Stable>` 配对 |
| `@UnionValue` | 一个参数需要代表「多选一」的不同类型 | 宏定义枚举，各 case 包装不同实体类型；提供 `typeDisplayRepresentation` 与 `caseDisplayRepresentations`；宏自动生成选择器支持 |
| `LongRunningIntent` + `CancellableIntent` | Intent **默认 30 秒**上限，大文件上传等做不完 | `performBackgroundTask { }` 包裹，循环内 `Task.checkCancellation()`；进度自动以 **Live Activity** 呈现；`onCancel: { reason in cleanup(for: reason) }`，取消原因含用户点停止 / 系统超时 / 资源回收；支持后台 GPU（需在授权中添加 GPU 访问权限） |
| `ExecutionTargets` | 多进程（主 App / AppIntents 扩展 / Widget 扩展）写同一存储会冲突 | `static var allowedExecutionTargets: ExecutionTargets`，取值 `.main` / `.appIntentsExtension` / `.widgetKitExtension` 或数组；**写操作指定 `.main`**，Widget 给只读 |
| 原生参数类型扩展 | 免自定义 | 新增 `Duration`（原生时间选择器）、`PersonNameComponents`（结构化姓名），自带 Siri 理解与本地化 |

- **三条内容曝光路径的官方分工**（对做分发的 PM 直接有用）：**Spotlight** = 让内容可被搜索并被 Siri 检索；**IntentDonationManager 交互捐献** = 让系统学习用户使用规律、推荐可能重复的操作；**RelevantEntities** = 主动告诉系统「什么内容在什么情境下相关」。
- **安全侧**：Session 345 **没有新增用户确认 API**；仅涉及 GPU 后台授权与 Widget 只读数据设计。取消（Live Activity 停止按钮）是**运行中**的用户控制手段。

#### 7. 鸿蒙负一屏：元服务成为智能体可分发的能力单元（HDC 2026 + 2026-07-29 报道）★★★☆☆

- **负一屏 MAU 突破 1.9 亿**，是元服务最重要的系统级入口；服务四格升级为**橱窗卡**。
- **Today-Task Skill**：负一屏新上线，**关联 AI Claw 智能体**后，用户给智能体布置任务（如「每天 18 点汇总当天 HDC 最值得看的技术亮点」），**任务完成后自动同步到负一屏** —— 即「智能体的产出物有了系统级承载位」，而不只是聊天气泡。
- **「探索元服务」**：负一屏下滑进入，基于 **LBS + 消费/阅读习惯**推卡片；跨地理边界自动切换本地服务模式（如出境后聚合当地出行/消费/文旅）。遵循**最小权限原则**，每个服务只取必要数据。
- **范式**：从「人找服务」→「服务找人」，从「偶然发现」→「常驻使用」。对开发者是**绕开应用商店推荐位的新触达路径**。
- ⚠️ **数据口径冲突（必须标注）**：一处称「截至 7-2，鸿蒙 6 终端 **7000 万台**，开源鸿蒙全场景设备超 13 亿台，注册开发者超 1100 万，**应用与元服务超 40 万款**」；另一处称「搭载全新鸿蒙的终端 **6600 万台**，鸿蒙应用及元服务 **3.5 万款**」。两组数字**统计口径明显不同**（后者疑为「原生鸿蒙」窄口径），**待官方澄清**。

---

## 正文拆解

### ① Schema 定义与语义路由机制

**A. 「Schema 该多重」的答案正在收敛：越薄越好，越结构化越好。**

Needle 给出了一个近乎极端的证明：既然工具 schema 本来就写在 prompt 里，Planner **就不需要世界知识**，因此可以砍掉 FFN、只留注意力做「query ↔ schema」的匹配与参数抽取。这从模型架构侧反向验证了本库长期主张的 [[意图模式规范]] 路线 —— **Schema 描述得越规范、越自解释，Planner 就可以越小**。反过来说，如果 Schema 写得含糊（比如 Android AppFunctions 的 KDoc 写得像给人看的注释），再大的模型也救不回来。

**B. 四大平台 + 第五类玩家的路由分层，已经能画成同一张图。**

| 层 | Apple | Android | HarmonyOS | Windows | 新一类（AgenticOS / Step AOS / DroiClaw） |
|---|---|---|---|---|---|
| 能力声明 | App Intents + Schema | `@AppFunction` + KDoc | Skill（`describe`/`execute`）+ 意图框架 | MCP / 连接器 | 原子能力引擎（Step）/ 生态层（荣耀） |
| 发现与索引 | Spotlight / IndexedEntity | OS Registry | 意图框架注册工具能力 | ODR 受控发现 | 统一语义数据层（Step） |
| 相关性提示 | **`RelevantEntities`（新）** | 待补 | 负一屏近场感知 + LBS | 待补 | 认知记忆自适应沉淀（荣耀） |
| 路由决策 | 端侧模型 + 云端大模型 | Gemini（私测） | 图推理引擎（子任务 DAG 并行） | Copilot | **意图/任务成为内核调度单元** |
| 参数填充 | Slot-filling / `$label.requestValue` | 结构化参数 | Want 参数 | 连接器 schema | 语义文件 |
| 跨设备 | **`SyncableEntity`（新）** | 待补 | 分布式软总线 / 端 A2A | 待补 | 统一记忆 + 任务迁移（荣耀） |

**新增的结构性观察**：Apple 用 `SyncableEntity` 解决「跨设备指同一个实体」，荣耀用「统一记忆 + 任务迁移 + 失败换端重试」解决同一问题，Step AOS 用「统一语义数据层」解决 —— **三家路径不同，但都承认『上下文必须归属于人，而不是归属于某台设备』**。这是 2026 年跨端意图路由的共识。

**C. 性能语义正在进入 Schema 设计。**

`EntityCollection` 是个被低估的信号：Apple 明确承认「**解析实体本身是有成本的**」，并给了开发者「只传 ID 不解析」的逃生门。这意味着 Intent 设计从此要区分「**需要完整实体的语义操作**」和「**只需要标识符的批量操作**」。做 OS 侧 Schema 规范的人应当把这个二分**写进规范**，而不是等开发者踩坑。

---

### ② 系统安全与用户体验（Confirmation / 隔离 / 防注入）

**A. XPIA 的威胁模型必须升级：从「一次注入」到「注入会繁殖」。**

Word 蠕虫是本库安全叙事的一次范式跃迁。此前四平台的防线（[[确认机制]]、[[隔离执行]]、ODR 受控发现、用户始终在环）全部假设：**攻击是一次性的，拦住这次就安全**。蠕虫打破了这个假设：

- **隔离失效路径**：Agent Workspace 能隔离「Agent 的执行域」，但**隔离不了被污染的产出物在同事之间正常流转**。载体是一份看起来完全合法的内部文档。
- **确认失效路径**：Confirmation UI 拦的是「敏感动作」（付款、发信、删除）。而「**改一份草稿里的财务数字**」不是敏感动作，它是 Copilot 的**本职工作**，不会触发任何确认。
- **审计失效路径**：每一次传播都是一次「合法的内部创作事件」，审计日志里看不出异常。
- **溯源失效路径**：第二代载体已经不需要原始攻击文件在场。

**B. 由此得出的新设计原则（本库首次提出，已写入 C 层 SOP）：**

> **凡是 Agent 具备「写回」能力的路径，都必须评估「注入能否自我复制」。**
> 判据三问：① Agent 能否修改会被他人复用的产物？② 这个产物会不会再次进入 Agent 上下文？③ 修改本身是否属于 Agent 的正常职责（因而不触发确认）？三问全「是」= 蠕虫风险。

**C. 用户体验侧出现了两个重要补丁：**

1. **「可逆」是被忽略的第四维。** Step AOS 的「可信 / 可见 / 可控 / 可逆」中，**可逆（一键撤回 + 任务中止）** 是本库此前完全没有的维度。Confirmation UI 管「执行前」，隔离管「执行中」，**Undo 管「执行后」** —— 而 Word 蠕虫恰恰证明了「执行后才发现」是常态。同理，Step AOS 的「**权限按需授予、任务结束自动回收**」与 Android 17 的「系统代持 + 单次 + 字段级」授权是同一思路的两种实现。

2. **「主动智能」的真正难点是克制，不是预测。** 荣耀黄非的表述值得整段收藏：

   > 「被动和主动的区别，听起来是产品体验，本质上是一个决策问题 —— **决策发生在指令之前还是指令之后？**」
   > 「难的不是预测，而是克制。**预测错了轻则打扰，重则事故。**所以每一次主动背后都是一次**置信度和代价的判断** —— **想清楚了才规划，时机对了才出现，拿到授权才执行。**」
   > 「主动智能的本质是替你推进目标，并且**永远把最后的决定权留在你手里**。」

   这三句「想清楚了才规划 / 时机对了才出现 / 拿到授权才执行」，是目前见过对 **Proactive Agent 的 Confirmation 设计**最凝练的表述，可直接作为 PRD 的验收口径。

**D. 一个尚未有人回答的问题**：当 OS 把调度单元升级为「意图」，**意图本身会不会成为被注入的对象？** 如果一份文档能让 Copilot 改写文档，那么一份文档能不能让 AgenticOS **注册一个恶意意图**、或污染「认知记忆自适应沉淀」？三家新 OS 的公开材料**均未回应**（待补 —— 已列入后续动作）。

---

## 值得保留的点

1. **「工具调用是检索-组装，不是推理」** —— Needle 用无 FFN 架构给出了工程证明。这直接改写端侧 Planner 的选型逻辑：不要按「模型聪不聪明」选，要按「schema 匹配准不准」选。
2. **26M / 14MB 能跑赢 270M~600M** —— 端侧意图路由的算力门槛可能被高估了一个数量级。对 OS PM 意味着：**低端机也能上系统级 Agent 的结构化路由**（GUI 路线才是真吃算力的）。
3. **「载荷修了，类别没修」** —— 面对 AI 安全问题时最该学会的一句话。区分「某个 PoC 字符串失效」与「漏洞类别关闭」。
4. **调度对象从进程/线程 → 意图/任务** —— 三家厂商独立收敛到同一句话，说明这不是营销词，而是一个真实的架构分层变化。
5. **「应用、服务、数据、设备从『用户要面对的入口』变成『系统要调用的资源』」** —— 这句话应该贴在每个做 OS 级 Agent 的 PM 工位上。
6. **安全四维中的「可逆」** —— 补上了 Confirmation UI 的时间盲区。
7. **「想清楚了才规划，时机对了才出现，拿到授权才执行」** —— Proactive Agent 的三道闸。
8. **第三类玩家（AI OS 中间层供应商）出现** —— DroiClaw 证明「AI OS 能力」可以被打包成方案卖给中小品牌，这会加速长尾终端的意图化，也会让「意图框架碎片化」问题更严重。

## 我的问题

1. Needle 的对比是在**什么测试集**上做的？是否有可复现的 eval 脚本？其「工具选择头」在**工具数量增长到几百个**（真实 OS Registry 规模）时是否还成立？
2. 无 FFN 架构能否承担**多轮 / 多工具编排**（而非 single-shot）？Cactus 明说这是「实验性单次调用」，那么 OS 级 Planner 需要的**串行依赖推理**由谁承担？
3. Word 蠕虫的机制能否**平移到 OS Agent**：一份被污染的文档 / 一条被污染的日历事件，能否让 Android AppFunctions 或 HarmonyOS Skill **执行非预期调用并把载荷写回**？四平台都没有公开的类别级评估。
4. 荣耀 / 阶跃 / 卓易三家把调度单元改为「意图」后，**Registry 的权限模型**是什么？谁能注册意图？注册需要什么审核？（这正是本库挂了多日的「四平台 Registry/权限横向 Checklist」应当扩展到六方的原因）
5. Step AOS 架设在 Android 之上 —— 那它如何获得**跨 App 原子能力**的调用权？是靠无障碍、靠厂商 ROM 特权，还是靠与美团/支付宝等首批伙伴的**双边协议**？如果是双边协议，其可扩展性与 [[国内安卓厂商做 App Intent 的阻力]] 描述的困境完全一致。
6. Apple「2027 年的新版本」到底对应哪些系统版本号？（iOS 28？）官方未明说。

## 后续动作

- [x] 提炼为概念（本次净新增 3 个 B 节点，增补 5 个既有节点）
- [x] 关联已有方法（新增 1 个 C 层 SOP）
- [ ] **【流程改进·优先】** 24h 窗口连续两天硬命中 ≤4 条，建议把自动化改为 **7 日滚动窗口**（保留「首次进入本库」判定做去重），避免为凑数而降低阈值
- [ ] 核验 Needle 的评测集与 eval 脚本；若有官方 BFCL 行则回填
- [ ] 跟踪 Måløy Context Collapse 系列后续 / 微软是否发布类别级缓解
- [ ] 核验《人工智能终端智能化分级》标准编号与 L3 认证机构
- [ ] 回填荣耀在 MobileWorld / MMBench / ACEBench 的具体名次
- [ ] **把「四平台 Registry/权限横向 Checklist」扩展为六方**（+ AgenticOS / Step AOS），已挂 4 天
- [ ] 跟踪荣耀 Robot Phone 8 月正式发布会与 AgenticOS 开发者文档是否开放
- [ ] 澄清鸿蒙设备数/元服务数两组冲突口径

> [!note] 概念节点双链
> [[意图模式规范]] ｜ [[语义路由]] ｜ [[端侧工具调用]] ｜ [[确认机制]] ｜ [[元服务]] ｜ [[隔离执行]] ｜ [[A2A 端侧智能体协议]] ｜ [[XPIA 跨提示注入]]
>
> **本库对应节点**：[[Intent Schema Protocol 意图模式规范]] ｜ [[Intent Router 语义路由]] ｜ [[Function Calling 端侧工具调用]] ｜ [[Confirmation UI 安全机制]] ｜ [[Atomic Service 元服务]] ｜ [[Agent Workspace 隔离执行]] ｜ [[A2A 端侧智能体协议]] ｜ [[XPIA 跨提示注入]]
>
> **本次新建**：[[Simple Attention Network 无FFN端侧路由]] ｜ [[Agentic OS 意图调度内核]] ｜ [[文档型 XPIA 自传播蠕虫]]
>
> **既有笔记（不重写，仅指向）**：[[App Intent 的核心作用]] ｜ [[Apple Intelligence 与 App Intents]] ｜ [[国内安卓厂商做 App Intent 的阻力]] ｜ [[工业级 GUI Agent 架构（VLM+无障碍树）]] ｜ [[手机AI智能体知识库]]
