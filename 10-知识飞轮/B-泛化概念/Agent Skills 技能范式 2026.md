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
