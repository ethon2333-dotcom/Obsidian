---
type: output
status: draft
created: 2026-11-02
method_used: "WebSearch + WebFetch 直查官方/权威源（无 Horizon MCP，仅 agent-mail 在线）；逐平台核验 + 去重"
tags: [AppIntent, 每日情报, 速览, 零净新增, 复核型]
---

# AppIntent 每日情报速览 2026-11-02

## 目标读者与目标

面向 OS PM / 端侧 Agent 框架观察者，用 30 秒讲清本窗口（2026-10-31 21:53 → 2026-11-02 12:21，约 38h）四大 OS 系统级意图框架 + 跨平台端侧 Planner 评测 + XPIA 研究线的净新增结论：**再次零净新增**，并登记唯一一条低于阈值的 Windows Copilot Actions surface 收敛。

## 正文或成品链接

- 完整情报笔记（A 索引）：[[AppIntent 每日情报 2026-11-02]]

### 速览表

| 平台 / 维度 | 本窗口净新增 | 重要性 | 处置 |
|---|---|---|---|
| Apple App Intents | 无 2026-11 新 `@AppIntent(schema:)`；iOS 27.2 已 GA、无 iOS 27.3 新意图 Schema 信号 | ★★☆☆☆ | 已复核·无净新增 |
| Android AppFunctions | 仍 `1.0.0-beta01`（10-21）；A2UI/ML Kit Agentic API 仍 alpha | ★★☆☆☆ | 已复核·无净新增 |
| HarmonyOS Intents Kit / ArkAF | 指南与概述稳定，无 11-01/02 新 API | — | 已复核·无净新增 |
| Windows Copilot Actions / Agent Workspace | 无新 OS 执行总线 API；但 **File Explorer 8 项 OneDrive Copilot Actions 整合进「Ask Copilot」（MC1515940，11 中旬起分阶段）** | ★5/10（surface 收敛） | ★5 状态行追加到 [[Windows Copilot Actions 与 Agent Workspace 2026]] |
| 跨平台 BFCL v4 端侧 Planner | FunctionGemma 270M / qwen3-0.6b-tool-router 仍不在榜；无新 ≤数 B entry | ★★☆☆☆ | 已复核·无端侧净新增 |
| XPIA 研究线 | 原理/分类复述波（appsecmaster/nhimg/zone.ci），无新 OS 机制 | — | 丢弃 |

### 结论要点

1. **OS 框架不日更，连续多轮确认**：四平台官方框架层本 38h 窗口再次零净新增，与 10-30/10-31 完全连续。
2. **唯一窗口内信号（★5，低于 6 阈值）**：Windows 把 File Explorer 右键菜单 8 项 OneDrive Copilot Actions 收敛进「Ask Copilot」统一入口（MC1515940，2026-11 中旬起 ~ 12 初完成）。这是 Copilot Actions **surface 整理**，能力保留、非新 API、非新安全机制——只在 Windows B 笔记追加状态行，不升 B 节点。
3. **Ignite 2026（11-17~20）尚未开幕**：预热议程（Agentic security / Zero Trust runtime / Entra agent identity）属路线图预告，非已发布 API，不计入。
4. **最高优先待办延续**：四平台意图 Registry **来源/provenance 轴仍全空白（confirmed）**，最低成本补丁仍是加 `readOrWrite` 声明位。

## 使用的方法

- 逐平台 WebFetch 直查官方源（Apple App Intents Updates / Android Jetpack all-channel Release Notes / Huawei Intents Kit+ArkAF / Microsoft Learn+Security Blog）+ WebSearch 交叉核验权威媒体。
- 严格去重：对比库内既有 B 笔记与近 3 轮运行（10-26/10-29/10-30/10-31），对窗口外事件（LFM3 Oct27 / Bonsai2 Oct15 / Nemotron Bolt Oct19）与纯模型发布按口径丢弃。
- 重要性阈值 ≥6/10 才升 B 节点；★5 仅追加状态行。

## 发布反馈

（待用户反馈）

## 复盘

### 有效的部分

- 沿用「OS 框架不日更 → 纯复核型」判定，避免编造增量；对唯一 ★5 信号（Windows Copilot Actions 收敛）做了正确的层级纪律处理：登记但不升节点。
- 对窗口外模型发布（LFM3/Bonsai2/Nemotron Bolt）显式标注窗口外，避免重复计入。

### 需要改进的部分

- 无（本窗口为低信息密度复核型，结构已稳定）。

### 回流到 A 的新问题或素材

- 跟踪 MC1515940 实际分阶段落地进度（11 中旬起），以及这是否预示 Windows 对 Copilot Actions 做「入口收敛」的产品策略转向。
- Ignite 2026（11-17~20）开幕后重点核验：是否披露新 Windows OS 执行总线 Registry API / Agent Launchers 新能力 / Copilot Actions 从 experimental 转正式。

---

> 关联：[[Apple AppIntents Schema Protocol 2026]] ｜ [[Android AppFunctions 设备侧意图 2026]] ｜ [[HarmonyOS Intents Kit 与 ArkAF 2026]] ｜ [[Windows Copilot Actions 与 Agent Workspace 2026]] ｜ [[Function Calling 端侧工具调用]] ｜ [[四平台意图 Registry 来源轴与权限模型对比 2026]] ｜ [[XPIA 跨提示注入]] ｜ [[Intent Router 语义路由]] ｜ [[Confirmation UI 安全机制]] ｜ [[Agent Workspace 隔离执行]]
