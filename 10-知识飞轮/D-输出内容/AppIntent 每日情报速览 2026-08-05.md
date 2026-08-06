---
type: output
status: draft
created: 2026-08-05
method_used: "系统级 Intent 路由评估 SOP + WebSearch/WebFetch 直取官方源（Horizon MCP 连续 7 日 disconnected）"
tags: [AppIntent, 速览, 2026-08-05]
window: "7 日滚动窗口 2026-07-30 → 2026-08-05"
---

# AppIntent 每日情报速览 2026-08-05（自动化 21:00 版）

## 目标读者与目标

- **读者**：OS 产品经理（尤其 Ethon 自身）、做端侧 Agent / 系统级意图框架的工程师。
- **目标**：30 秒掌握本期四大 OS 在系统级意图框架 / 端侧路由 / 执行安全上的窗口增量，并知道哪些已落库、哪些待补。

## 正文或成品链接

**本期 30 秒速览**

| 维度            | 本期结论                                                                                                                                                                                              | 重要性    |
| ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------ |
| 系统级执行总线       | **Windows Agent Launchers**：基于 App Actions + ODR 的系统级 Agent 注册表（`com.microsoft.windows.ai.agentInfo`、odr.exe agent-info add/remove/list），补齐 Windows「应用向系统声明能力」的注册层，与 Apple/Android/HarmonyOS 首次对齐 | 7–8/10 |
| 端侧 Planner 路由 | **LFM2.5-2.6B**（08-04）入表：2.6B on-device agentic，<2.5GB、手机约 30 tok/s；LFM2.5 家族 230M/450M/2.6B/8B-A1B 规模阶梯完整                                                                                        | 7/10   |
| 评测口径          | **BFCL v4 权重经 EvalScope 官方文档确认**（Agentic 40% / Multi-Turn 30% / Live+NonLive+Hallucination 各 10%），08-04 待办关闭                                                                                      | 6/10   |
| 四平台官方渠道       | Apple / Android / HarmonyOS / Windows 经逐条复核**无新增可执行 API**（HarmonyOS ArkAF 文章为 06-17，窗口外）                                                                                                          | —      |

**两条最可执行的判断**

1. **Windows 的「系统级意图框架」比本库此前记录的更完整**：有 ODR（MCP 连接器注册）+ Agent Launchers（agent 实体注册）两层。做跨平台对标时，Windows 不再是「只有工具注册」，而是具备「应用声明能力 → 系统受控发现」的完整骨架，只是颗粒度目前是 agent 而非细粒度 intent/function。
2. **端侧选型表若只有 BFCL 总分仍会选错**：v4 把 70% 权重压在 Agentic+Multi-Turn（小模型最弱处），而 Hallucination 那 10% 才是跨应用意图路由最该盯的一栏——「该说不会时硬编一个函数调用」恰是 Registry 变大后最高频的失败模式。

**详细原始资料**：[[AppIntent 每日情报 2026-08-05]]

## 使用的方法

- 7 日滚动窗口检索 + 先读既有 B/C 笔记做去重（双链不新建重复节点）。
- 新事实 vs 口径变化分类（BFCL v4 权重属口径，已升级为已核实）。
- 诚实标注：未复现数字标「待补」，镜像站≠官方榜。

## 发布反馈

（自动化产出，暂无人工反馈）

## 复盘

### 有效的部分

- 延续「同日不重跑全窗口、只补净新增 + 显式列无净新增清单」的运行模式，避免重复检索，也避免让用户误以为漏检。
- 用 EvalScope 官方文档交叉确认 BFCL v4 权重，把一条挂了 1 天的待办从「二手快照」升为「已核实」。

### 需要改进的部分

- Agent Launchers 的具体 Insider build 号 / 发布日期 / opt-in 开关归属仍未闭合，是下一轮应优先补的硬信息（目前只有官方文档页的行为口径，无时间锚点）。

### 回流到 A 的新问题或素材

- 四平台「意图元数据来源分级」连续第 5 日未解（最高优先），下轮仍按既定路径查安全白皮书 PDF。
- LFM2.5-2.6B 的 BFCLv4 绝对值（厂商 + 镜像站 56.9%）需以 Berkeley 官方榜复核。
