---
tags: [AI-Agent, Skill, 范式, 知识管理]
created: 2026-07-31
---

# Agent Skills 技能范式 2026

## 定义
Agent Skills 是 Anthropic 于 2025-10 提出的开放标准（2025-12-18 成为跨平台开放标准；Linux 基金会 AIDF 候选标准）。本质：**把某类工作的程序性知识（procedural knowledge）打包成一个文件夹，让通用 Agent 在需要时动态加载，变成该领域的专家**。类比「给新员工写的 onboarding 手册」。

## 核心结构
- `SKILL.md`（必须）：YAML 元数据（name + description）+ Markdown 指令
- `scripts/`（可选）：可执行代码，轻量版 MCP 能力
- `references/`（可选）：按需加载的参考文档
- `assets/`（可选）：模板、图片、字体等输出资源

## 渐进式披露（Progressive Disclosure）—— 灵魂设计
1. **第一级 YAML 元数据**：启动即加载进 system prompt，仅 name + description（~100 词），用于「触发判断」。
2. **第二级 SKILL.md 正文**：判定相关时才读入（建议 ≤500 行）。
3. **第三级 关联文件**：references / assets，仅按需被 Agent 主动发现读取。
→ 好处：技能库可极大扩展而不撑爆上下文；天然契合端侧 / 低带宽。

## Skill vs Prompt vs MCP
- Prompt：每次重写的长指令，重复劳动。
- MCP：连接层（「厨房」——工具 / 数据接入）。
- Skill：知识层（「菜谱」——流程 / 规范 / 最佳实践）。
- MCP 解决「能不能用」，Skill 解决「用得好不好、稳不稳」。

## 格式之争（平台机会）
- Claude Code：`SKILL.md` / `CLAUDE.md`（最成熟）
- Codex：`CODEX.md` / `AGENT.md`
- Cursor：`.cursor/rules/`
- Gemini CLI：`.gemini/`
- OpenCode：自定义 YAML
社区呼吁「skill 版 MCP」——统一描述 / 分发格式；目前 `SKILL.md` 是事实最广泛的兼容格式。

## 与既有笔记的关联
- 索引：[[意图框架·跨体系索引 MOC]]
- 端侧 / 低带宽友好 → [[Function Calling 端侧工具调用]]、[[Local Agent Bench 端侧智能体基准]]
- 自我进化 → [[知识飞轮看板]]、长期记忆方向（obsidian-second-brain、claude-reflect）
- 企业级治理 → [[企业级 Agent 平台与 Agent-as-Asset 2026]]
- 安全审批 → [[Agent 身份与硬件级审批]]
- OS 平台借鉴 → [[Apple AppIntents Schema Protocol 2026]]、[[Windows Copilot Actions 与 Agent Workspace 2026]]（设备端 MCP / Registry 思路）

## 对 OS PM 的启示
1. Skill 成为「能力分发单位」，分发市场是生态战场。
2. 渐进式披露 = 端侧算力范式，可参考用于系统级 Skill 商店。
3. 格式统一者掌握生态入口（类比 MCP 之于工具调用）。
4. self-improving（从纠错回写长期记忆）是 2026 主线之一。

## 反例与边界（Skill 范式的失效场景）

- **上下文污染 / 过度召回**：Skill 被加载即获得领域指令权；若 `description` 写得过宽，通用 Agent 会错误触发或在错误上下文执行——这是 Skill 版的「过度召回」，须靠精准 description + 触发护栏缓解。
- **恶意 Skill 注入**：非签名 Skill（尤其社区分发）可夹带指令注入，呼应 [[Agent Data Injection 数据注入攻击]]；企业场景必须有来源校验与签名（见 [[Agent 身份与硬件级审批]]）。
- **格式碎片化反噬**：若「skill 版 MCP」统一呼吁失败，Skill 市场会重演 MCP 早期多格式并存的碎片化，反而抬高跨平台分发成本。

## 最新进展（2026 一手来源）

- **标准状态**：Anthropic 于 2025-12-18 将 Skill 定为跨平台开放标准并进入 Linux 基金会 AIDF；2026 年 OpenAI、Cursor、GitHub Copilot、Claude Code 等已采纳，`SKILL.md` 成为事实最广的兼容格式（详见上方「深化补充」）。
- **生态动向**：2026 年「Agent Skill 市场 / 分发」成为企业级 Agent 平台竞争焦点，与 [[企业级 Agent 平台与 Agent-as-Asset 2026]] 互为表里；一手进展持续跟踪 [[AppIntent 每日情报速览]] 系列与 [[知识飞轮看板]]。

## 深化补充

- **标准时间线修正**：Anthropic 于 **2025-12-18** 正式将 Skill 定为**跨平台开放标准**（非 2025-10 首次提出时），并进入 **Linux 基金会 AIDF** 候选；截至 2026 已被 OpenAI、Cursor、GitHub Copilot、Claude Code 等多家采纳，`SKILL.md` 成为事实最广的兼容格式。
- **与 OS Registry 的关系**：Skill 的「渐进式披露」三层级（YAML 元数据 → SKILL.md → 关联文件）与四平台意图框架的「能力声明 → 语义索引 → 执行」同构；OS 完全可把 `SKILL.md` 当作跨厂商 **能力描述** 的可迁移载体，直接对齐 [[智能体互联国家标准与 AIP]] 的「五段式」能力描述段。
- **与 MCP 分工**：Skill=知识层（菜谱），MCP=连接层（厨房），二者在 OS Agent 里对应「声明能力」与「注册工具」（见 [[Intent Schema Protocol 意图模式规范]]、[[端侧执行通道 GUI 与 MCP 路线之争]]）。

- [ ] 当 Skill 被 OS 系统 Agent 动态加载并执行写回操作时，其安全边界归属 App 还是系统？需明确责任链。
- [ ] 企业级 Skill 市场（见 [[企业级 Agent 平台与 Agent-as-Asset 2026]]）如何做来源校验与签名，避免恶意 Skill 注入（呼应 [[Agent Data Injection 数据注入攻击]]）？
- [ ] 端侧低带宽下，Skill 的渐进式披露与 [[Simple Attention Network 无FFN端侧路由]] 的轻量路由能否共用同一套「按需加载」运行时？

## 2026-09-20 增补：技能层供应链投毒 —— 从概念警告到实证攻击类（来源 [[AppIntent 每日情报 2026-09-20]]）

> 接续本笔记「反例与边界」里的「恶意 Skill 注入」概念警告（line 54）与「企业级 Skill 市场来源校验与签名」待办（line 69）。本期把该警告补上**实证攻击数据**，并显式映射到四平台 Skills / A2A 分发层。

- **三篇 2026-02 arXiv 实证（首次入库，库内空白补漏）**：
  - **Skill-Inject（arXiv 2602.20156，Schmotz et al.）**：基准测主流 LLM agent 在**恶意指令嵌入 skill 文件**时的遵从率，证明被污染 skill 可让 agent 执行有害动作——**agent 生态新供应链攻击面**。
  - **Malicious Agent Skills in the Wild（arXiv 2602.06547，Liu et al.）**：分析 **~100,000 个 agent skills**，识别恶意行为与漏洞，揭示被污染 skill 可触发**多阶段攻击链（数据外泄 + agent 劫持）**。
  - **SkillJect（arXiv 2602.14211，Jia et al.）**：用**闭环反馈**自动生成 stealthy 恶意 skill，主动提升注入有效性（攻击侧自我进化，与 [[XPIA 跨提示注入]] 09-17 SIR 同源）。
- **对 Skill 范式的安全含义（落回本笔记）**：
  - Skill 的「渐进式披露」三层级（YAML 元数据 → SKILL.md → 关联文件）本就是**把领域指令权交给通用 Agent**；若 `description` 过宽会过度召回（本笔记已记），而**非签名 / 社区分发 skill 夹带指令**现在有了实证——「恶意 Skill 注入」从待办升级为**已证实攻击类**。
  - **与四平台 Skills 层直接映射**：HarmonyOS ArkAF 2.0 **Skills 上架**（端侧/云端 Skill 同名冲突、A2UI Schema 版本兼容）、Android AppFunctions **agent skill**、A2A 协议——这些「Skill = 能力分发单位」机制正是 Skill-Inject 靶面；**OS 级 Skill Registry 若不做来源校验 + 签名，等于把供应链投毒面原样搬进系统层**。
  - **新增设计护栏**：Skill manifest 须**来源校验 + 签名 + 权限最小化**（与 [[Agent 身份与硬件级审批]] 同构）；企业级 Skill 市场（[[企业级 Agent 平台与 Agent-as-Asset 2026]]）须把恶意 Skill 注入纳入准入扫描；端侧低带宽下仍须保留签名校验（不能为了渐进式披露牺牲来源可信）。
- → 与 [[XPIA 跨提示注入]] 的协同：本库 XPIA 威胁模型新增「**能力描述（Skill）注入**」靶面，即意图框架的声明层本身成为注入面；OS Agent 执行安全须把 Skill 来源完整性纳入爆炸半径边界。
- ⚠️ 诚实标注：三篇均 2026-02 arXiv 预印本、由本轮检索首次入库（非 24h 新发布）；具体 benchmark 数字待一手论文复核，先不写精确百分数。

## 2026-11-05 增补：Apple 入局 `SKILL.md` + 跨平台技能格式收敛（来源 [[AppIntent 每日情报 2026-11-05]]）

> 接续本笔记「格式之争」与「深化补充」段（SKILL.md 为事实最广兼容格式）。本期把「跨平台 SKILL.md 收敛」从预判升级为 **已发生事实**——Apple 在 iOS 27.3 Siri AI 开发者预览中采用 `SKILL.md` 子集作为 App Skills 格式，且 Google 已声明 Gemini 可复制其他平台 skill。

- **Apple App Skills = Agent Skills (`SKILL.md`) 的子集**：每个 skill 是 `Skills.skillsbundle` 内独立文件夹的 `SKILL.md`，body ≤10,000 字符，仅 YAML 元数据（name + description）+ Markdown 指令体，**无 scripts / references / 其他字段**（比 Claude Code / Anthropic 标准更瘦）；依赖脚本的 skill 需为 Gemini 重写（格式兼容但能力受限）。
- **Google 已确认跨平台 skill 可移植**：wain.blog 引述——Google 声明「在其他平台写的 skill 可复制到 Gemini，同样用 `SKILL.md`」——与 Apple 子集同源。→ **Apple + Google 首次在技能描述文件格式上对齐到 `SKILL.md`**，是四平台之外**技能分发层的跨厂商收敛**，坐实本笔记「格式统一者掌握生态入口」的判断。
- **🔑 关键安全约束（跨平台通用）**：Apple 明确 app skills **不能保证确定性执行顺序**——「Siri AI does not necessarily run the intents listed in a skill in sequence」。→ 把本笔记「反例与边界」的「过度召回/恶意 Skill 注入」之外，补上**「编排非确定性」靶面**：OS 级 skill 若串多步含写回/确认流程，**不能靠 skill 文案顺序保证安全，必须在被调用意图内部做确定性护栏**（呼应 [[Confirmation UI 安全机制]] 与 [[Apple AppIntents Schema Protocol 2026]] 11-05 增补）。
- **对 OS PM 的启示**：① 技能格式战趋近终局，`SKILL.md` 成事实标准，OS 系统 Agent 直接以 `SKILL.md` 为跨厂商能力描述载体（本笔记「深化补充」的预判兑现）；② 但「skill 可移植」≠「skill 安全可移植」——跨平台 skill 携带的脚本/指令注入面（见本笔记 09-20 增补 Skill-Inject/Malicious Agent Skills）随可移植性放大，**OS Skill Registry 的来源校验 + 签名门槛须同步抬高**。
