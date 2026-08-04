---
type: output
status: draft
created: 2026-08-01
method_used: "[[Agent 写回路径 XPIA 风险评估 SOP]]"
tags: [AppIntent, 每日情报, 速览]
---

# AppIntent 每日情报速览（2026-08-01）

## 目标读者与目标

OS / Android 系统 PM、做端侧 Agent 与意图框架的工程师。目标：用 3 分钟掌握过去 24h + 库内空白补漏中，系统级意图框架与端侧 Agent 执行总线的最关键进展。完整原始资料见 [[AppIntent 每日情报 2026-08-01]]。

## 正文或成品链接

**三条主线同时质变：**

1. **执行安全（最高价值）**：Copilot for Word 被证实存在**可自我传播的文档型 XPIA 蠕虫**，MSRC 协调披露 **144 天后漏洞「类别」仍未关闭**，模型 GPT-5.5→5.6 仍复现。这是威胁模型从「一次注入」升级为「**注入会自我复制**」的分水岭。详见 [[文档型 XPIA 自传播蠕虫]]。

2. **端侧 Planner**：Cactus Compute 开源 **Needle——26M 参数、INT4 仅 14MB、完全没有 FFN 层**的函数调用模型，single-shot 击败 FunctionGemma-270M / Qwen-0.6B / Granite-350M / LFM2.5-350M，论证「**工具调用是检索-组装，不是推理**」。详见 [[Simple Attention Network 无FFN端侧路由]]。

3. **意图调度内核**：荣耀 AgenticOS、阶跃 Step AOS、卓易 DroiClaw 一个月内先后把 OS **调度对象从「进程/线程」改为「意图/任务」**，四大平台之外冒出第五类玩家。详见 [[Agentic OS 意图调度内核]]。

**其他要点：** Apple WWDC26 Session 345 补齐 AppIntents 代码级细节（`EntityCollection` / `SyncableEntity` / `RelevantEntities` 等）；鸿蒙负一屏 MAU 1.9 亿、Today-Task Skill 让智能体产出物有系统级承载位；Step AOS 四维安全补「可逆」维度。

**诚实标注：** 严格 24h 仅硬命中 1 条（DroiClaw），连续两天窗口过薄，**建议自动化改 7 日滚动窗口**；厂商自述名次/分数均标待补；鸿蒙设备数两组口径冲突待官方澄清。

## 使用的方法

- 情报采集：WebSearch/WebFetch 直取官方源（Horizon MCP 不可用）。
- 分层落库：A 原始资料 → B 泛化概念（3 净新增 + 5 增补）→ C 方法 SOP → D 速览。
- 去重：核查库内既有笔记，用 [[双链]] 指向，不重写用户原文件。

## 发布反馈

（待发布后填写）

## 复盘

### 有效的部分

- 24h 窗口过薄时，用「库内空白补漏 + 真实日期标注」保住信息价值，而非降阈值凑数。
- 「写回路径三问判据」把 Word 蠕虫提炼为可复用方法（[[Agent 写回路径 XPIA 风险评估 SOP]]），跨平台适用。

### 需要改进的部分

- 24h 硬命中连续两天 ≤4 条，信息密度不足以支撑「每日」节奏；下一步应评估改 7 日滚动窗口（保留首次入库存量判定做去重）。
- 单一来源（如聚合媒体二次扩散）的进展需标注一手来源与日期，避免被误当作当日新闻。

### 回流到 A 的新问题或素材

- Needle 对比测试集与 eval 脚本待核验；无 FFN 能否承担多轮编排待答。
- Word 蠕虫机制能否平移到 Android AppFunctions / HarmonyOS Skill 执行非预期调用并写回，四平台均无类别级评估。
- 三家新 OS 把调度单元改为「意图」后，Registry 权限模型与审核机制未公开（待扩为六方 Checklist）。

#标签/AppIntent #标签/每日情报
