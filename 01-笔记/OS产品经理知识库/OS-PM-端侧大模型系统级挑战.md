---
tags: [product, pm, os, 端侧AI, llm, 挑战, 知识库]
aliases: ["SLM 系统挑战", "端侧大模型挑战", "AI-Native OS 挑战"]
source: "Gemini 对话导出 (gemini-code-1785420276458.txt)"
created: 2026-07-30
---

# 📑 OS 产品经理：端侧大模型（SLM）带来的系统级挑战

> [!note] 笔记定位
> 端侧 SLM（1B~7B）正从「偶发调用的 App」演变为「常驻后台的 OS 系统级服务（AI-Native OS Core）」，打破了传统 OS「前台优先、后台冻结/回收」的静态资源平衡模型。

## 一、PSS 内存极速膨胀与机制挑战

### 1. 静态权重 + 动态 KV Cache 双重挤压
- **静态权重常驻**：3B INT4 需 ~1.8~2.0GB RAM，作 OS 核心引擎不能像后台 App 被 OOM 杀，直接占 Base RAM 预算。
- **动态 KV Cache 暴涨**：随 Context 拉长（2k→8k→32k）线性甚至二次方增长，长文档/多轮对话额外吃 500MB~1.5GB+。
- **Prefill 内存尖峰**：首 Token 并行处理时激活张量瞬时冲高，易引发前台 App Crash。
```text
[系统总 PSS]
 ├─ 静态权重 (固定 ~1.8GB)
 ├─ 运行时激活张量 (首Token尖峰 ~300MB)
 └─ 动态 KV Cache (随对话递增 ~200MB → 1.5GB+)
```

### 2. 对传统回收机制的破坏
- **ZRAM 失效**：权重与 KV 是高维向量，ZRAM 压缩比 < 1.1:1，白耗 CPU 换不回内存。
- **LMK 失效 / 冷启动两难**：
  - 高优先级保活 → 前台游戏/相机因内存不足卡顿或杀后台
  - 低优先级可杀 → 重新读 2GB 权重需 **3~10s 初始化时延**，体验断层

### 3. PM 求解方案
- Unified Memory 零拷贝张量传递
- PagedAttention 模型按需分页（非活跃层丢入 mmap）
- KV Cache 动态剪枝 + 量化（INT8/INT4 + Token Evict）

## 二、NPU 调度与异构算力管理

### 1. 范式变革：短阵发 → 长流式
- 传统 NPU 任务（人脸解锁、美颜）：短时、阵发、批处理，毫秒级释放
- SLM 推理：长持续、流式（Autoregressive），可能占 NPU 数秒~数十秒

### 2. 抢占粒度粗 → 优先级反转
- NPU 硬件级抢占弱（矩阵内核无法中途中断）
- 冲突：后台 SLM 总结邮件时用户开相机（需 NPU 实时分割），相机掉帧/黑屏

### 3. PM 求解方案
- **Token 级 / 层级低时延抢占**：在 Token 间隙或 Layer 边界插入中断，抢占延迟 < 5ms
- **AI Workload QoS 分级**：
  - P0 Real-time：相机 ISP / 人脸 / AR（绝对优先）
  - P1 Interactive：用户主动 AI 对话 / 语音助手
  - P2 Background：静默语义抽取 / 本地向量 DB Embedding（空闲才跑）

## 三、功耗、热管理与续航极速劣化

### 1. 内存墙功耗（Memory Wall Power）
Decode 阶段算力开销不高但**带宽开销极大**——每生成一个 Token 要把整个 2GB 权重从 LPDDR 搬入 NPU 一次。DRAM 访存功耗占系统总功耗 **50%+**，发热极大。

### 2. 热降频恶性循环
SLM 长推理 → SoC 升温至阈值（如 45°C）→ Thermal Governor 强制降频 → Token 速度跌 **50%~70%** → 推理时间拉长 → 长期高发热 → 续航骤减。
```text
SLM 持续推理 → 内存带宽挂满 → SoC 发热 → Thermal Throttling 降频 → (生成变慢→更久→更热)
```

### 3. PM 求解方案
- **Speculative Decoding 投机采样**：小 Draft 模型猜、大模型验，减少权重反复调入
- **Context-aware Execution Routing**：电量足+WiFi→云端；离线/高隐私/弱网→端侧；高发热/低电→降级规则引擎或 SLM-lite

## 四、传统 OS vs AI-Native OS 指标对比
| 维度 | 传统移动 OS | AI-Native OS 新挑战 | PM 新指标 |
| --- | --- | --- | --- |
| 内存 RAM | Base ~2.5GB；单App PSS | 静态权重常驻 + KV Cache 膨胀 | **KV Cache Peak Footprint**、**TTFL** |
| 调度 | CPU/GPU 抢占，FPS/触控时延 | NPU 长任务流式，硬件抢占难 | **Token Preemption Latency**、**TTFT** |
| 功耗 | 屏幕/基带为主 | LPDDR 带宽搬运功耗、长发热 | **Energy per Token**、**Thermal Throttling Token Penalty** |

> [!tip] 关联
> 内存膨胀的底层机制 → [[OS-PM-PagedAttention与KV Cache剪枝]] 与 [[OS-PM-3B模型内存预算推演]]
> 带宽/功耗解法 → [[OS-PM-投机采样原理与能效优化]] 与 [[OS-PM-AI Runtime动态调度与降级策略]]
