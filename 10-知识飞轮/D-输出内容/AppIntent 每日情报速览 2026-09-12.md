---
type: output
status: draft
created: 2026-09-12
method_used: "AppIntent 每日情报自动化（WebSearch/WebFetch 直采官方/媒体源，无 Horizon MCP）"
tags: [AppIntent, 速览, 每日]
---

# AppIntent 每日情报速览 2026-09-12

## 目标读者与目标
OS PM / 意图框架方向同学；一句话看清「过去窗口（2026-09-04→09-12，因自动化 9 天未跑而补跑）四大 OS 在系统级意图框架上的净变化」。

## 正文或成品链接
- 索引主笔记：[[AppIntent 每日情报 2026-09-12]]
- 本窗口净新增 / 增补落点：
  - [[HarmonyOS Intents Kit 与 ArkAF 2026]]（9-7 后信通院增强级认证 + 支付宝反诈实测 35.8%/42.3% + perf 22%/25%）
  - [[A2UI 生成式UI协议(Google)与鸿蒙落地 2026]]（新节点：高德 AGenUI 基于 Google A2UI）
  - [[Function Calling 端侧工具调用]]（Needle 2 跨模型 BFCL v4 单轮对照 + Seal-Tools 域外 28.7% 居首）
  - [[端侧 Router 置信度门控与工具可达性收缩 2026]]（attention-only 消融 0.47→0.006 nats + grammar 跳过 98% 词表 + well-formed 93.4%）
  - [[Windows Copilot Actions 与 Agent Workspace 2026]]（build 26200.8313/26220.7262 +「Agents」面板 +「@」调 Agent）

## 使用的方法
- 先读自动化 memory 与既有 B 笔记，避免重复；再 WebSearch/WebFetch 官方/媒体源（Apple/Android/HarmonyOS/Windows 官方文档 + aibacon 第三方拆解）；按「重要性≥6/10 + OS 级/端侧路由/执行安全」筛选；落到 A 索引 + B 增补 + 看板登记。

## 发布反馈
- （自动生成，暂无人工反馈）

## 复盘

### 有效的部分
- **框架层无净新增，但「发布后实测/认证」成主增量**：四平台框架 API 稳定，竞争焦点转向可信认证（鸿蒙信通院增强级）、量化反诈（支付宝 -35.8%）、跨平台 UI 协议（AGenUI/A2UI）。
- **端侧 Planner「小模型 + 严格语法约束 + 置信门控」路线被反复独立印证**：Needle 2 的 93.4% well-formed（靠 byte-level grammar 约束）、attention-only 消融（0.47→0.006 nats）、Seal-Tools 域外居首，共同坐实本库 08 月起的选型纪律。

### 需要改进的部分
- **诚实口径压力大**：本窗口关键数字（信通院认证、支付宝反诈、AGenUI 协议遵循度、Windows build 号）均来自媒体/厂商口径，缺官方逐字文档；已在各笔记标「待官方核验」。
- **BFCL v4 仍依赖第三方引述**：Apple FM 61.7% / Needle 2 42.6% 等仍无 Berkeley 官方榜复核。

### 回流到 A 的新问题或素材
- 待 Berkeley 官方 BFCL v4 榜复核；待高德 AGenUI 官方仓库核验 A2UI 协议字段；待 9-14 iOS 27 GA 后核查 per-intent 路由 API；延续 Watch OS 26 / NowSecure / Chrome Origin Sets 待办。
