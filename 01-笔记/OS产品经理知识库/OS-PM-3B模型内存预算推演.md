---
tags: [product, pm, os, 端侧AI, 内存预算, pss, 知识库]
aliases: ["3B 内存预算", "Memory Budget", "PSS 推演"]
source: "Gemini 对话导出 (gemini-code-1785420276458.txt)"
created: 2026-07-30
---

# 📑 OS 产品经理：端侧 3B 模型内存预算（Memory Budget）推演

> [!note] 笔记定位
> 规划端侧 AI 功能（长文档总结、全局搜索）时，PM 不能只说「支持 32k 上下文」，必须精确推算不同上下文下的 **PSS 峰值**。以 3B 级 SLM（Llama-3.2-3B / Qwen2.5-3B 架构）为基准。

## 一、推演基准参数（固定假设）
| 参数 | 符号 | 数值 | 备注 |
| --- | --- | --- | --- |
| 总参数量 | N | 3.21 B | INT4 部署 |
| 网络层数 | L | 28 | Transformer Layers |
| Query 头数 | H_Q | 24 | |
| KV 头数 | H_KV | 8 | GQA 3:1 |
| 单头维度 | d_head | 128 | 3072/24 |

## 二、四大组件公式
`Total RAM = Model Weights + KV Cache + Activations + System Overhead`

### 1. 模型静态权重
- FP16 原始：3.21B × 2B ≈ **6.42 GB**（移动端无法常驻）
- INT4（含 Scales/Zeros）≈ 0.56 Bytes/param → **≈ 1.80 GB**（固定，不随上下文变）

### 2. 动态 KV Cache（关键变量）
`KV per Token = 2 × L × H_KV × d_head × Bytes = 2×28×8×128 = 57,344 元素/Token`
- FP16 (2B)：**0.112 MB/Token**
- INT8 (1B)：**0.056 MB/Token**
- INT4 (0.5B)：**0.028 MB/Token**

### 3. 运行激活值 Activations
- 未优化 Full Prefill：随序列长度暴涨
- Chunked Prefill + FlashAttention（Chunk=512）：峰值锁死 **200~300 MB**，不随 8k/32k 膨胀

### 4. 系统 Overhead（固定 ≈ 400 MB）
- NPU/GPU 驱动 Workspace & DMA Scratchpad：~250 MB
- AI Runtime + Context Engine：~100 MB
- PagedAttention 页表：~30~50 MB

## 三、完整推演表（PSS 峰值）

### 1. 传统未优化（FP16 KV + 无 Chunked Prefill）
| 组成 | 2k | 8k | 32k |
| --- | --- | --- | --- |
| 权重 INT4 | 1.80 | 1.80 | 1.80 |
| KV FP16 | 0.23 | 0.92 | **3.67** |
| 激活 Full Prefill | 0.35 | 1.20 | **4.80** |
| Overhead | 0.40 | 0.40 | 0.40 |
| **PSS 总峰值** | **2.78 GB** | **4.32 GB** | **10.67 GB** (OOM) |

### 2. OS AI Runtime 优化（INT8 KV + Chunked Prefill + PagedAttention）
| 组成 | 2k | 8k | 32k |
| --- | --- | --- | --- |
| 权重 INT4 | 1.80 | 1.80 | 1.80 |
| KV INT8 | 0.11 | 0.46 | **1.84** |
| 激活 Chunk=512 | 0.25* | 0.25* | **0.25*** |
| Overhead | 0.40 | 0.40 | 0.40 |
| **PSS 总峰值** | **2.56 GB** | **2.91 GB** | **4.29 GB** (12GB手机可承受) |

### 3. 极致省电（INT4 KV + Token Eviction 50%）
- 2k → **2.50 GB** ｜ 8k → **2.68 GB** ｜ 32k(等效16k) → **3.35 GB**

## 四、PM 决策与规格结论
1. **32k 必须 Chunked Prefill**：否则激活 4.8GB 超模型本身，致命 OOM。强制拆 512/1024 Token Chunk。
2. **8GB RAM 手机极限 = 8k 上下文**：系统基底占 3.5~4.0GB，AI 安全配额 **3.0 GB**。优化后 8k 占 2.91GB 踩线；硬跑 32k 须开 Token Eviction 压 KV < 1GB。
3. **12GB/16GB 才具长文本全局 Agent 体验**：允许多 32k 3B 模型与相机/游戏后台保活。

> [!tip] 关联
> KV 为何能剪/量化 → [[OS-PM-PagedAttention与KV Cache剪枝]]
> 权重反复搬运的功耗代价 → [[OS-PM-投机采样原理与能效优化]]
