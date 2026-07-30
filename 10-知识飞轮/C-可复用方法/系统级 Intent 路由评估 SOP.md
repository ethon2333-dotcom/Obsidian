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
4. **跑 benchmark**：BFCL / 内部评测，记录 Tool Choice 准确率、参数抽取 F1、延迟、tok/s。
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
| 跨域泛化差、准确率低 | 缩小 Planner 域 + 强化云端升级；或对单应用 Schema 微调（见 FunctionGemma 46%→90%） |
| 设备算力不足、tok/s 不达标 | 降模型规模（270M/0.6B）或量化（INT4） |
| 语义缓存污染 | 设 TTL / 置信门槛，定期失效 |
| 槽位缺失导致执行失败 | 强制 Slot-filling 反向追问，禁止静默默认 |

## 示例

- FunctionGemma 270M 经单应用 Tool Schema 微调 + LiteRT-LM，Tool Choice/参数抽取 **46% → 90%**，Pixel 7 ~2000 tok/s（详见 [[Function Calling 端侧工具调用]]）。
- 混合栈：FunctionGemma 本地 + 低置信升级 Gemini Flash + Qwen3-Embedding-0.6B 语义缓存。

#标签/评估 #标签/SOP #标签/端侧Planner
