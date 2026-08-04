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

## 深化补充

### 一句话心智模型

> **PagedAttention 是"合租"，Token Eviction 是"断舍离"。前者不扔东西、只是把柜子塞满；后者是真的把东西扔了。**

这个区分是整篇最该记住的一点，因为**两者的代价性质完全不同**：

| | 干了什么 | 有信息损失吗 | PM 该怎么看 |
|---|---|---|---|
| **PagedAttention** | 消除碎片，提高装填率 | **没有** | 纯工程收益，**无脑上** |
| **KV INT4 量化** | 每件东西压缩 | 极小（PPL < 1%） | 基本无脑上 |
| **Token Eviction** | **扔掉一部分历史** | **有，且不可逆** | **必须产品决策，不能工程自决** |

原文那张"PM 指标评估矩阵"把三者并列，容易让人以为它们是同一类手段。**但第三行是有产品后果的**——它会让用户问"我们刚才说的那个细节"时，Agent 答不上来。

**这条线（无损优化 vs 有损优化）应该是 PM 在这个话题上唯一必须守住的边界。** 无损的部分交给工程去做到极致，有损的部分必须回到产品桌上讨论。

### Attention Sink 这个现象值得单独记住

原文里最反直觉的一个事实：**最前面 4 个 token 必须永久保留，删了模型"瞬间崩溃"。**

我一开始觉得这很怪——开头几个 token 通常是 system prompt 的开头，语义上并不重要，为什么删不得？

我的理解（可能不准确，**待核实**）：这不是**语义**上的重要，是**机制**上的必需。Softmax 要求注意力权重和为 1，模型在"这一层其实不需要关注任何东西"的时候，需要一个地方把多余的注意力倾倒掉。最前面的 token 就充当了这个"垃圾桶"。删掉垃圾桶，注意力就被迫分配到真正的内容上，分布全乱。

**如果这个理解对，那它有一个很有意思的产品含义**：模型内部存在一些"看起来没用、实际是承重墙"的结构。这提醒我在做任何"看起来能砍的优化"时，都要先问一句"**它是不是承重墙**"。这个思维习惯比记住 Attention Sink 这个具体知识更有用。

### 跨 App KV 共享——被低估的一条

原文第二节提到"系统 Agent 默认 System Prompt 的 KV 常驻共享页表，所有 App 直接映射"。我觉得这条的战略意义远超它在原文里的篇幅。

**它意味着：System Prompt 成了一种系统级公共资源。** 推论：

1. 谁定义这个 System Prompt，谁就定义了所有 App 上 Agent 的**基础行为规范**（安全边界、拒绝策略、语气）。这是**平台权力**。
2. 它必须**极度稳定**——改一次，所有缓存失效，全系统重算。这和 [[OS-PM-系统架构与底层技术]] 里"越底层越要稳定"完全一致。
3. 它也是个**攻击面**：如果 System Prompt 能被污染，影响范围是全系统所有 Agent（对照 [[XPIA 跨提示注入]]）。

**所以"共享 System Prompt KV"表面是个内存优化，实际是在创造一个新的系统级契约。** 这种"工程优化悄悄变成产品决策"的情况，是我作为 PM 最该警觉的一类。

### 关联

- 内存总账 → [[OS-PM-3B模型内存预算推演]] ｜ [[OS-PM-端侧大模型系统级挑战]]
- 谁来做全局页池仲裁 → [[OS-PM-系统AI Runtime vs 应用引擎]] ｜ [[OS-PM-AI Runtime动态调度与降级策略]]
- System Prompt 的安全面 → [[XPIA 跨提示注入]] ｜ [[Agent Data Injection 数据注入攻击]]
- 长上下文的产品价值 → [[Agent 记忆与个性化意图理解]]（记忆能不能替代长上下文？）
- 分层稳定性原则 → [[OS-PM-系统架构与底层技术]]

### 待解问题

- [ ] Token Eviction 的"精准回忆丧失"，能不能用**端侧 RAG 兜底**？即：驱逐前先把内容存进本地向量库，需要时检索回来。这样长上下文变成"短上下文 + 检索"——**代价是延迟，收益是内存**。这个 trade-off 有人做过对比吗（待核实）？
- [ ] 如果 RAG 能兜底，那"支持 32k 上下文"这个产品指标本身是不是就没意义了？**用户要的是"记得住"，不是"上下文长"。** 这两个需求可能被混为一谈了。
- [ ] 共享 System Prompt KV 的**版本管理**怎么做？OTA 更新了 System Prompt，正在运行的 Agent 会话怎么办？强制重算还是新旧共存？
