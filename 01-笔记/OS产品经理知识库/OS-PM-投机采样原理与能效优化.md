---
tags: [product, pm, os, 端侧AI, speculative-decoding, 能效, 知识库]
aliases: ["投机采样", "Speculative Decoding", "草稿模型验证"]
source: "Gemini 对话导出 (gemini-code-1785420276458.txt)"
created: 2026-07-30
---

# 📑 OS 产品经理：投机采样（Speculative Decoding）原理与能效优化

> [!note] 笔记定位
> 端侧 LLM 最大瓶颈不是「NPU 算力不够」，而是「**内存带宽不够（Memory-Bound）**」。投机采样通过「小模型猜、大模型验证」提升计算访存比，从根本降低 DRAM 访存功耗。

## 一、核心痛点：为什么传统端侧推理特别费电/慢

### 1. Memory-Bound 与极低计算访存比
Decode 阶段每生成 1 Token 必须把整个权重从 LPDDR 读入 NPU 一次。
- 算例：3B INT4 权重 ~1.5GB，生成 1 Token 需 ~6 GFLOPs
- 计算访存比 = 6e9 / 1.5e9 = **4 FLOPs/Byte**
- 现代 NPU 算力达 50~100 FLOPs/Byte → **算力大幅过剩，NPU 在干等内存搬运**

### 2. 真凶：DRAM 访存功耗
- NPU 一次 8-bit MAC 仅 ~0.1 pJ
- 从 LPDDR 读 1 Byte 需 ~5~10 pJ（是计算的 **50~100 倍**）
- 生成 100 Token 要从 DRAM 搬 150GB 数据 → 总线持续高发热，发热降频、电池秒掉

## 二、工作机制（小模型猜、大模型验）
1. **Draft Model（小模型）**：100M~300M，极快，占用带宽极小
2. **Target Model（大模型）**：3B~7B，能力强，搬权重代价贵
```text
[Step1 Draft] 小模型串行 K 次 → [y1,y2,y3,y4]
   ▼
[Step2 Verify] 大模型单次 Forward Pass 并行算 4 个概率分布
   ▼
[Step3 Accept/Reject] 采纳前 M 个 + 大模型矫正第 M+1 个 → 大模型仅搬 1 次权重产出 M+1 个
```

### 关键性质
- Verify 阶段把 K 个 Token 组矩阵并行，大模型**只搬 1 次 1.5GB 权重**即可算 4 个 Token
- 拒绝采样数学保证：输出分布与单独用大模型**完全一致（无损 Lossless）**

## 三、量化算账（K=4, 接受率 α=75% → 4 有效 Token）
| 模式 | 大模型读取 | 小模型读取 | 总搬运 | 均摊/Tok |
| --- | --- | --- | --- | --- |
| 标准 Decode | 4 次 | 0 | 6.0 GB | 1.5 GB |
| SpecDec | **1 次** | 4 次 | **1.9 GB** | **0.475 GB** |

> 💡 **内存带宽需求降低约 68%**

功耗下降本质：
1. DRAM 访存功耗断崖下跌（搬运量↓60%~70%）
2. 计算访存比 4 → 4×K（如 16 FLOPs/Byte），从 Memory-Bound 移向 Compute-Bound，能量效率更高
3. 生成更快 → CPU/NPU/内存更快进入 Deep Sleep

## 四、PM 工程权衡（Trade-offs）
1. **接受率 α 与场景**：代码/固定格式 α=80%~90%（收益极高）；开放创作 α 可能跌 30%~40%（反而更慢更费电）。OS 应按任务类型动态开关/调 K。
2. **RAM 空间换带宽**：需同时载小+大模型，内存极紧时（后台游戏）多占 100~300MB 可能触发 LMK。
3. **无小模型变体**：Medusa / EAGLE（多头预测/树状解码）在大模型顶挂轻量预测头（几 MB），零额外权重开销，是端侧 PM 看好的方向。

> [!tip] 总结卡片
> 1. 瓶颈根因：端侧 Decode 是 Memory-Bound，DRAM 搬权重极耗电
> 2. 思路：小模型(100M)串行猜 K 个，大模型(3B)搬 1 次权重并行验
> 3. 收益：带宽↓60%+，延迟↓1.5x~2.5x，DRAM 功耗大降
> 4. 权衡：监控 α，在 RAM 占用与带宽/功耗节省间找平衡

> [!tip] 关联
> SpecDec 在 OS 中如何动态降级 → [[OS-PM-AI Runtime动态调度与降级策略]]
> 权重搬运的带宽代价印证 → [[OS-PM-3B模型内存预算推演]]
