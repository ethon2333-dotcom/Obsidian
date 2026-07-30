---
tags: [product, pm, os, 端侧AI, pagedattention, kv-cache, 知识库]
aliases: ["PagedAttention", "KV Cache 剪枝", "分页注意力"]
source: "Gemini 对话导出 (gemini-code-1785420276458.txt)"
created: 2026-07-30
---

# 📑 OS 产品经理：PagedAttention 机制与 KV Cache 内存剪枝

> [!note] 笔记定位
> 端侧 LLM 最吃内存的除了**静态权重**，就是**动态 KV Cache**。**PagedAttention 解决碎片化浪费（How to store）**，**KV Cache 剪枝解决总量爆炸（How to shrink）**。

## 一、痛点：KV Cache 如何吃光端侧内存

自回归生成时缓存历史 Token 的 K/V 矩阵即为 KV Cache。
- **单 Token 公式**：`2 × 层数 × KV头数 × 头维度 × 精度字节`
- 以 3B（32层, 8 KV头, 128维, FP16）：`2×32×8×128×2 ≈ 131 KB/Token`
  - 2k 上下文 ≈ **262 MB** ｜ 8k ≈ **1.05 GB** ｜ 32k ≈ **4.2 GB**（超权重本身！）
- **传统预分配噩梦**：HuggingFace 类框架要求物理连续内存，按最大序列（如 8192）预申请。用户只说「你好」（10 Token）也虚占 8182 个 Token 空间，利用率 **< 20%~40%**。

## 二、PagedAttention：虚拟内存哲学的胜利（vLLM 提出）
灵感来自 OS 内核的**虚拟内存 + 分页**。
```text
[逻辑 KV Cache]  Block0|Block1|Block2|Block3   (16 Tokens/Block)
       │  Block Table 页表映射
       ▼
[物理 LPDDR]  Block2 | ... | Block0 | ... | Block1   (散落、无须连续)
```

### 运行逻辑
1. **逻辑切块**：连续 Token 按固定大小切（如 16 Token/Block）
2. **动态物理分配**：满 16 Token 才向内核动态申请新物理 Block
3. **页表映射**：Block Table 记录逻辑↔物理映射，NPU 借页表实时寻址

### 三大红利
- **零外部碎片**：利用率提升至 **96%+**（仅最后一个 Block 微量内部碎片）
- **Copy-on-Write & Parallel Sampling**：一问多答时 Prompt KV Block 被 3 分支共享，仅分叉时复制，**省 60%+ Prompt 内存**
- **跨应用共享 System Prompt 缓存**：系统 Agent 默认 System Prompt 的 KV 常驻共享页表，所有 App 直接映射，不重复占内存

## 三、KV Cache 剪枝与压缩（降低总量）
```text
原始 8k KV ─> [空间: INT4 量化] ─> 体积↓75%
           ─> [时间: Token 驱逐] ─> 仅保留 Sink+Heavy+Recent
```

### 1. 动态 Token 驱逐（Token Eviction）
注意力分布「两头重要、中间平庸」：
- **StreamingLLM (Attention Sink)**：最前 4 个 Token 始终吸大量注意力权重，必须永久保留，否则模型瞬间崩溃
- **H2O / SnapKV**：
  1. Sink Tokens：前 4 个（永久）
  2. Recent Tokens：最近滑动窗口（如最后 64 个，保局部连贯）
  3. Heavy Hitters：累加历史 Attention Score 挑最关键 M 个，其余（废话/过渡词）彻底擦除

### 2. 极低比特量化
- FP16→INT8/INT4：权重易量化（静态），KV 动态生成易有离群值
- Group-wise 动态量化实时压成 INT4/INT8；FP16→INT4 精度损失 < 1%，**KV 占用↓75%**（1GB→250MB）

## 四、OS 三层组合拳整合
**页表管理 + 剪枝策略 + 内核 Swap**：
1. **Unified Paging Pool**：内核划统一物理页池，所有 App 按需领用 Paged Block（非独占）
2. **Cold/Hot Page Swapping**：App 后台 >30s 标记 Cold Page，KV Block 压缩存 ZRAM 或 mmap 写 Flash，切回毫秒级恢复
3. **DMA Zero-Copy**：统一内存架构（Apple Silicon / 骁龙）下页表直映射 NPU MMU，NPU 经 DMA 直读物理页，免 CPU 往返拷贝

## 五、PM 指标评估矩阵
| 治理手段 | 解决瓶颈 | RAM 节省 | Trade-off |
| --- | --- | --- | --- |
| PagedAttention | 碎片化、无法并发 | **40%~60%** | 需 NPU 支持页表寻址；增 Block Table 维护开销 |
| KV Cache INT4 | 单 Token 体积大 | **75%** | 微 PPL 损耗；需 NPU 支持 INT4 混合精度 |
| Token Eviction | 长上下文总量膨胀 | **50%~80%** | 丧失被驱逐 Token 精准回忆（长文档精确检索） |
| ZRAM KV Swapping | 后台保活差 | **60%** (CPU换RAM) | 恢复时 TTFT 增 100~300ms |

> [!tip] 关联
> 量化/KV 占用的具体数字 → [[OS-PM-3B模型内存预算推演]]
> 为什么带宽才是真瓶颈 → [[OS-PM-投机采样原理与能效优化]]
