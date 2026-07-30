---
type: output
status: draft
created: 2026-07-30
method_used: "[[系统级 Intent 路由评估 SOP]]"
tags: [AppIntent, OS-Agent, 跨平台2026, 格局总览]
---

# AppIntent 跨平台格局总览（2026）

## 目标读者与目标

- **读者**：OS 系统 / 系统 Agent 方向的产品与技术同学（含 [[手机AI智能体知识库]] 读者群）。
- **目标**：一页看明白 Apple / Android / HarmonyOS / Windows 四大 OS 在「App Intent + 端侧 Agent 执行」上的共识与差异，并知道去哪篇笔记深挖。

## 正文

### 一句话格局

四平台同步把 App Intent 从「命令映射」升级为 **Schema Protocol + 端侧 Agent 执行总线**：开发者声明 Schema/Tool，System Broker 统一做意图解析、路由与跨应用编排。这是「意图即服务」分发入口之争。

### 四平台对照（速查）

| 维度 | Apple | Android | HarmonyOS | Windows |
|------|-------|---------|-----------|---------|
| 机制 | AppIntents Schema Protocol | AppFunctions（设备端 MCP） | Intents Kit + `Want` + 元服务 | Copilot Actions + ODR |
| 注册 | 系统 Schema 声明 | OS Registry（需 `EXECUTE_APP_FUNCTIONS`） | 元服务 `installationFree` | ODR 注册 MCP 连接器 |
| 路由 | IndexedEntity 语义索引 | 设备端 MCP 路由 | ArkAF + A2UI | Agent Workspace |
| 安全 | OwnershipProvidingEntity + 确认 | UI Automation 执行前预警 | 可信设备协商 | 隔离会话 + 签名 + ACL |
| 头号风险 | 注入/误执行 | 生态碎片化 | 跨设备安全 | XPIA |

### 三条主线（点链接深挖）

- **模式规范**：[[Intent Schema Protocol 意图模式规范]]（四平台 Schema 对照表）
- **端侧路由**：[[Intent Router 语义路由]] + [[Function Calling 端侧工具调用]]（含端侧 Planner 评测表）
- **安全执行**：[[Confirmation UI 安全机制]] + [[Agent Workspace 隔离执行]] + [[XPIA 跨提示注入]]

### 平台卡（2026 技术细节）

- [[Apple AppIntents Schema Protocol 2026]]
- [[Android AppFunctions 设备侧意图 2026]]
- [[HarmonyOS Intents Kit 与 ArkAF 2026]]
- [[Windows Copilot Actions 与 Agent Workspace 2026]]

### 与已有知识库的关系

本文是 [[手机AI智能体知识库]] 的「2026 技术框架」补强：已有笔记偏概念与国内生态（[[App Intent 的核心作用]]、[[Apple Intelligence 与 App Intents]]、[[国内安卓厂商做 App Intent 的阻力]]、[[工业级 GUI Agent 架构（VLM+无障碍树）]]），本文补「各平台官方框架 API 细节 + 端侧 Planner 实测 + 跨平台安全」，不重复已有内容。

## 使用的方法

- 原始情报：[[AppIntent 跨平台情报简报 2026-07-30]]（A 层）
- 评估方法：[[系统级 Intent 路由评估 SOP]]（C 层）

## 发布反馈

- 待发布后回填。

## 复盘

### 有效的部分

- 按 A→B→C→D 飞轮分层，原始情报→概念→方法→输出闭环完整。
- 严格双链到已有笔记，未重复已有知识。

### 需要改进的部分

- 端侧 Planner 评测表仍有 Gemma 4 / Qwen3-Coder-Next 待补（回流 A）。
- 缺四平台 Registry / 权限模型横向 Checklist（待补方法）。

### 回流到 A 的新问题或素材

- iOS 27 / Android 17 / HarmonyOS 7 / Windows Agentic 正式版落地差异？
- 四平台 Registry / 权限模型横向对比，能否提炼 OS Agent 设计 Checklist？

#标签/AppIntent #标签/格局总览 #标签/跨平台2026
