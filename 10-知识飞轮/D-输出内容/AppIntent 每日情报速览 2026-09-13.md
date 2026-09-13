---
type: output
status: draft
created: 2026-09-13
method_used: "WebSearch/WebFetch 官方源 + 库内去重（7 日滚动窗口 2026-09-06→09-13）"
tags: [AppIntent, 速览]
---

# AppIntent 每日情报速览 2026-09-13

## 目标读者与目标
OS PM（Ethon）；30 秒掌握四平台系统级意图框架过去一周真增量。

## 正文
本期窗口（2026-09-06→09-13）四大 OS 官方框架层**无净新增 API**，真增量集中在「评测权威化」与「执行安全加固」：

1. **BFCL v4 官方榜单上线（最高价值）**：Berkeley Gorilla 维护的 BFCL v4 现在公开可查（DataLearner 镜像 2026-09-07 更新）。SOTA = **MiniCPM5-2B（OpenBMB）66.60**，2.5B、免费商用。意义：① 端侧级小模型首次登官方 v4 榜首，端侧 Planner 评测有了权威锚点；② 校准历史第三方分数——Apple FM 61.7% / Needle 2 42.6% / FunctionGemma 27–46% 等此前均为第三方引述，现可逐步用官方榜复核（长期待办「Berkeley 官方榜」收口）。⚠️ 某中文综述称「BFCL V4 88.5%」疑为单轮子集/厂商自报，与官方 Overall 66.60 口径不同，**待补**。

2. **Windows Microsoft Execution Containers（IFA 2026）**：Windows 把 Agent 隔离从「独立低权限账号 + ACL」升级为**内建沙箱容器（Microsoft Execution Containers）**，强制企业安全策略 + 全量活动日志；同期整合 NVIDIA OpenShell / Hermes / OpenClaw。是四平台里**最明确的 OS 内建 Agent 容器隔离原语**（非仅 Defender 端点侧检查）。Project Zenith（64GB 统一内存门槛）/ RTX Spark 属硬件定位，不计入意图框架增量。

3. **HarmonyOS 7 确认 API 26 + provenance-at-source**：凤凰网版本说明明确 **HarmonyOS 7 = API 26**，关闭库内长期的「26 vs 23」冲突待办。新增**安全相机 2.0 数字内容溯源** + **数字身份 DID**（硬件 TEE 级 VC 签名）——虽非意图 Registry 层 provenance，但表明鸿蒙在**数据源层**补 provenance，与「四平台意图 Registry 来源轴全空白」待办形成对照信号。

4. **iOS 27 RC + GA 明日**：build 24A435（09-09）为 beta 收尾，**无新 App Intents API**；GA 2026-09-14 是核查「per-intent 路由/来源声明 API」的触发点（待办延续）。

## 使用的方法
WebSearch/WebFetch 直查官方/媒体源（无 Horizon MCP）；库内去重：对照 09-12 看板与既有 B 笔记，只追加增量、不新建重复节点。

## 发布反馈
（待发布后回填）

## 复盘
### 有效的部分
BFCL 官方榜上线一举收口连续多轮「Berkeley 官方榜」待办，端侧评测口径从「第三方引述」升「可复核」；HarmonyOS API 26 冲突待办关闭。

### 需要改进的部分
iOS 27 GA（09-14）未到，per-intent 路由 API 核查须下轮执行；鸿蒙 安全相机2.0/DID 字段细节与是否真接意图回路待官方文档。

### 回流到 A 的新问题或素材
Execution Containers 是否受 08-02 同一 `Experimental agentic features` opt-in 管控、与 Agent Workspace 容器关系、MiniCPM5-2B 在端侧 SoC 实测待补。
