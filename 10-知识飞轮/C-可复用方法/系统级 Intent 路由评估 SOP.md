---
type: method
status: active
derived_from: "[[Function Calling 端侧工具调用]] | [[Intent Router 语义路由]]"
tags: [AppIntent, 评估, SOP, 端侧Planner]
---

# 系统级 Intent 路由评估 SOP

> 用途：评估 / 选型「端侧 Intent Planner（OS Agent 路由方案）」。实测数据见 [[Function Calling 端侧工具调用]]。

## 使用场景

- OS / 系统 Agent 团队要选型或验收端侧意图路由方案。
- 判断某小模型能否在目标设备算力下承担「Tool Choice + 参数抽取」。
- 设计「本地优先 + 低置信升级云端」混合架构。

## 输入

- 单应用 / 窄域 Tool Schema 数据集（含参数定义）。
- 多轮对话样本（覆盖槽位缺失、歧义、跨步骤依赖）。
- 目标设备算力预算（NPU 型号、内存上限、可接受延迟）。

## 步骤

1. **明确评估目标**：单应用 vs 跨应用路由；延迟/成本预算（如 Pixel 7 ≥ 2000 tok/s）。
2. **准备 Schema 数据集**：单应用 Tool Schema + 多轮样本，刻意覆盖槽位缺失与歧义。
3. **选型基线**：小模型 Planner（FunctionGemma 270M 类）做本地路由，配「低置信升级云端」兜底。
4. **跑 benchmark（必须双基准，2026-08-03 更新）**：
   - **格式合规度**：BFCL（注明 v3/v4、官方榜单行 or 自测）→ 测「能不能按 Schema 把槽填对」。
   - **语义理解度**：NexusRaven 或等价复杂 API 语义集 → 测「懂不懂这个 API 是干嘛的」。
   - **两者必须同时记录**：实测存在同一模型 BFCL 73.3% / NexusRaven 43.8% 且与对手排名倒转的情况（Bonsai-8B vs Qwen3.5-9B）。**只看 BFCL 会在跨应用编排场景选错模型。**
   - 同时记录：Tool Choice 准确率、参数抽取 F1、延迟、tok/s、**云端逃逸率**。
5. **设检查标准**：本地优先达标线（如准确率 ≥ 85%、延迟达标）；定义低置信升级阈值。
6. **加语义缓存**：Qwen3-Embedding-0.6B 类语义缓存吸收高频意图，降低云端依赖（学习环）。
7. **失败处理**：低置信 → 升级云端；槽位缺失 → Parameter Slot-filling（`requestValue` 反向追问）。

## 完成标准

- 本地 Planner 准确率 / 延迟达标，且升级链路闭环。
- 语义缓存命中后高频意图零上云。
- 跨域 / 低置信样本有明确升级路径，无静默错误。

## 常见失败与处理

| 失败 | 处理 |
|------|------|
| 跨域泛化差、准确率低 | 缩小 Planner 域 + 强化云端升级；或对单应用 Schema 微调（官方口径 **base 58% → 微调 85%**） |
| 设备算力不足、tok/s 不达标 | 降模型规模（270M/0.6B）或量化 |
| **BFCL 高但线上跨应用频繁出错** | 补测 NexusRaven；语义分低说明模型只会填格式不懂 API，**限制其只做窄域固定 Schema 路由**，跨应用编排上移 |
| **FP16 模型填槽准确率反常低** | 试 1-bit/低比特 **QAT** 版本——结构化输出任务上 QAT 是增益而非损失（Bonsai-4B FP16 25.3% → 1-bit 73.3%） |
| 语义缓存污染 | 设 TTL / 置信门槛，定期失效 |
| 槽位缺失导致执行失败 | 强制 Slot-filling 反向追问，禁止静默默认 |

## 2026-08-03 增补：量化选型纪律

**端侧 Planner 的量化策略不按「保精度」选，按「保 Schema 合规」选。** 通用能力强 ≠ 填槽准；量化感知训练把模型表达力压向「只吐合法 JSON」这一窄目标，在意图路由场景反而有利。选型时**必须实测量化版本，不能用 FP16 分数外推**。

## 示例

- FunctionGemma 270M 经单应用 Tool Schema 微调 + LiteRT-LM，Mobile Actions **base 58% → 85%**（Google 官方口径）；S25 Ultra 实测 prefill 1718 tok/s / decode 125.9 tok/s（详见 [[Function Calling 端侧工具调用]]）。
- 混合栈：FunctionGemma 本地 + 低置信升级 Gemini Flash + Qwen3-Embedding-0.6B 语义缓存。
- 双基准反例：Bonsai-8B（1-bit, 1.15GB）BFCL **73.3%** 却 NexusRaven **43.8%**，Qwen3.5-9B 恰好相反（64.0% / 75–77.1%）→ 详见 [[AppIntent 每日情报 2026-08-03-晚]]。

#标签/评估 #标签/SOP #标签/端侧Planner
