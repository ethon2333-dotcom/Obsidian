---
tags: [AI-Agent, Skill, 知识管理, 月报]
created: 2026-07-31
source_brief: 综合 claudeskills.info / claudewave / aibestskill / lobehub / skillsmp / openagentskill / theagenticleaderboard / 今日头条 / CSDN 等 2026-07 公开盘点
---

# 最近一个月热门 AI Agent Skill 整理（2026-07）

> 口径：检索窗口约 2026-06-30 ~ 2026-07-31。热度以「安装量 / 周增长 / GitHub Trending」综合近似，实时排名会变动。

## 一、先说清楚：什么是 Agent Skill？

Agent Skills 是 2025 年 Anthropic 提出的开放标准（2025-10 发布，2025-12-18 宣布为跨平台开放标准；Linux 基金会 AIDF 已将其列为候选标准之一）。一句话：**Skill 是「把某类工作的专业流程 / 规范打包成一个文件夹」，让通用 Agent 在需要时自动加载、变成该领域专家**。类比成「给新员工写的 onboarding 手册」最贴切。

核心文件结构：
- `SKILL.md`（必须）：YAML frontmatter（name + description）+ Markdown 指令正文
- `scripts/`（可选）：可执行代码（Python/Bash/JS），相当于轻量版 MCP
- `references/`（可选）：按需查阅的参考文档（规范、Spec 等）
- `assets/`（可选）：模板、图片、字体等静态资源

### 渐进式披露（Progressive Disclosure）—— Skill 的灵魂
三级加载机制，让「技能库」可以无限大而不撑爆上下文：
1. **第一级（YAML 元数据）**：启动时全部加载进 system prompt，只放 name + description（约 100 词），让 Agent 知道「什么时候该用这个 skill」。
2. **第二级（SKILL.md 正文）**：当 Agent 判断相关时，才把完整指令读进上下文（建议 ≤500 行）。
3. **第三级（关联文件）**：references/、assets/ 里的文件，仅在真正需要时才被 Agent 主动读取。

### Skill ≠ Prompt ≠ MCP
- **Prompt**：每次从零写的长指令，重复劳动。
- **MCP**：连接层，把 Agent 接到外部系统 / 工具（「厨房」——灶台、食材）。
- **Skill**：知识层，教 Agent 怎么用好这些工具（「菜谱」——步骤、规范、最佳实践）。
- 三者关系：MCP 解决「能不能用」，Skill 解决「用得好不好、稳不稳」。

### 格式之争（值得 OS PM 关注）
不同 Agent 宿主用不同约定，导致「写一次、处处能用」还没完全实现：
- Claude Code：`SKILL.md` / `CLAUDE.md`（最成熟）
- Codex：`CODEX.md` / `AGENT.md`
- Cursor：`.cursor/rules/`
- Gemini CLI：`.gemini/`
- OpenCode：自定义 YAML

社区正在呼吁一个「skill 版的 MCP」——统一描述 / 分发格式，让同一份技能跨 Claude / Codex / Cursor / Gemini 无缝运行（目前 `SKILL.md` 是事实上的最广泛兼容格式）。

## 二、生态规模（最近一个月的数据）
- **Claude Skills**：60,000+ 已发布，同比增长 **12 倍**，90%+ 开源；开发工作流 22% / 代码生成 18% / 测试 QA 14%。
- **MCP Servers**：18,000+，增长 9 倍。
- **Agent Frameworks**：3,200，增长 4 倍（Claude Code / NanoClaw / OpenClaw / CrewAI / LangGraph / AutoGPT）。
- **Custom Commands & Hooks**：900（新类别）。
- 第三方市场：LobeHub 收录 **332,954** 个 Skills；skillsmp.com 索引 **1,728,327** 份 `SKILL.md`。
- 预测：2027-03 Skills 破 200,000；MCP 成事实标准；企业采纳率 80%；质量危机倒逼标准化测试。

## 三、最近一个月热门 Skill 清单

### 综合热度 Top 20（2026-07 前后，基于 skills.sh 安装榜 + GitHub Trending + 社区盘点；安装量为近似值）
| 排名 | Skill | 来源 | 近期热度 | 用途 |
|---|---|---|---|---|
| 1 | find-skills | vercel-labs/skills | ~1.9M | 对话中搜索 / 发现 / 安装社区 Skills（Skill 搜索引擎） |
| 2 | frontend-design | anthropics/skills | ~515K | 提升 AI 生成 UI 审美，去「AI 味」 |
| 3 | vercel-react-best-practices | vercel-labs/agent-skills | ~459K | 约束 React / Next.js 代码质量 |
| 4 | agent-browser | vercel-labs/agent-browser | ~428K | Agent 自动控制浏览器（操作 / 测试 / 抓取） |
| 5 | microsoft-foundry | microsoft/azure-skills | ~377K | Azure AI 基础设施编排 |
| 6 | web-design-guidelines | vercel-labs/agent-skills | ~373K | 网页设计规则库 |
| 7 | azure-validate | microsoft/azure-skills | ~373K | Azure 资源配置校验 |
| 8 | remotion-best-practices | remotion-dev/skills | ~356K | 用代码生成视频 |

> 注：Azure 系列集中上榜，说明**企业云自动化**已成为重要落地场景。

### 近期高增速 / 新晋热门（来自 aibestskill.com 周增长榜，截至 2026-07）
- **andrej-karpathy-skills**（176k，+9,985/周）：规避 LLM 常见编码错误的行规指南。
- **Understand-Anything**（60k，+452/周）：从代码库 / 知识库生成交互式知识图谱。
- **claude-md-improver**（9k，2026-07-19 更新）：审计并优化 CLAUDE.md。
- **claude-automation-recommender**（8.9k，2026-07-12）：分析代码库并推荐自动化（hooks / subagents / skills / MCP）。
- **claude-reflect**（self-learning，2026-07-08）：会话中捕获纠正并同步到 CLAUDE.md——典型 **self-improving Agent**。
- **dev-browser**（6.3k）：带持久页面状态的浏览器自动化。
- **drawio-skill**（3.4k，+393/周）：画架构图 / 流程图。
- **Trail of Bits skills**（安全研究 / 漏洞检测，3 天前更新）。
- **obsidian-second-brain**（3.6k）：把 Obsidian 库变成 AI 优先的「第二大脑」（45 条命令，自改写笔记、语义搜索、定时维护）——与知识飞轮高度相关。

### 2026-07-13 当周开源 Agent 榜 Top 10（theagenticleaderboard）
ECC #1、cline #2、agentic-awesome-skills #3、ppt-master #4、AutoGPT #5、n8n #6、dify #7、cherry-studio #8、langchain #9、page-agent #10。

### 垂直场景热门（2026-07 特别火）
- **新媒体运营类**（CSDN 红狐 Hub 7 月 Top 10）：小红书低粉爆款笔记、小红书爆款查询（三维评分）、抖音热榜、小红书爆款创作、公众号账号诊断（四维评分）、爆款封面生成、热点文章生成器、多平台违禁词检测、账号诊断师、图文运营创作器。
- **PPT / 演示类**：ppt-generation（字节 deer-flow，70.8k）、ppt-master、mattpocock code-review / grill-with-docs / to-spec。
- **金融数据类**：himself65/finance-skills、westock 等（与金融 MCP 技能互补）。
- **医疗类**：OpenClaw-Medical-Skills、biomni（自主生物医学 Agent）。

## 四、热门 Skill 的分类地图
1. **开发 / 代码**：frontend-design、vercel-react、code-reviewer、auto-write-tests、PR review、root-cause-tracing。
2. **浏览器 / 网页自动化**：agent-browser、dev-browser、browser-use、page-agent。
3. **生产力 / 文档**：docx、ppt-generation、NotebookLM 集成、Document Skills Suite、obsidian-second-brain。
4. **AI / ML 工程**：prompt-master、rag-engineer、agent-evaluation、langfuse、ai-agents-architect。
5. **安全**：Trail of Bits、Computer Forensics、Codebase Auditor。
6. **设计 / 创意**：algorithmic-art、canvas-design、Slack GIF、封面生成。
7. **自我进化（self-improving）**：claude-reflect、claude-md-improver、self-reflection framework。
8. **垂直场景**：新媒体运营、金融、医疗、游戏（godogen 自主游戏开发）。

## 五、对 OS PM 的启发
1. **Skill 正在成为「能力分发单位」**：热度不再只看 Star，更看实际安装量。这意味着**分发渠道 / 市场**会成为 Agent 生态的关键战场——对 OS PM 而言，「系统级 Skill 商店 / Registry」是可借鉴的产品形态（可双链 [[Apple AppIntents Schema Protocol 2026]] / [[Windows Copilot Actions 与 Agent Workspace 2026]] 设备端 MCP 思路）。
2. **渐进式披露 = 端侧算力友好**：三级加载天然契合**端侧 / 低带宽**场景（参考 [[Function Calling 端侧工具调用]] / [[Local Agent Bench 端侧智能体基准]]）。
3. **self-improving 是趋势**：claude-reflect 这类「从纠错中学习并回写长期记忆」的范式，与知识飞轮、长期记忆方向一致。
4. **格式标准之争 = 平台机会**：谁能统一 Skill 格式，谁就掌握生态入口（类比 MCP 之于工具调用）。
5. **安全治理**：YubiKey / Entrust 硬件级审批 + skills 的可审计性，是 [[Agent 身份与硬件级审批]] 的延伸。

## 六、趋势总结（2026 十大方向收敛）
多模态 Agent / 自主决策与自我进化 / 端侧部署 / Agent OS / MCP + A2A 互操作 / 长期记忆 / 企业级平台（AaaS）/ 具身智能 / 多智能体协作（MAS）/ 安全治理。质量危机（6 万 skill 里良莠不齐）正倒逼标准化评测。

## 相关链接
- 原始资料：[[AI Agent Skill 生态半月情报 2026-07-31]]
- 泛化概念：[[Agent Skills 技能范式 2026]]
- 既有相关：[[企业级 Agent 平台与 Agent-as-Asset 2026]]、[[前沿 Agent 大模型 2026H2]]
