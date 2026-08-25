---
title: OS PM 端侧 AI Runtime 实测实验方案
type: experiment-plan
status: planned
tags: [OS产品经理, 端侧AI, AI Runtime, NPU, 性能评测]
created: 2026-08-06
updated: 2026-08-06
related: [OS-PM-学习方向与能力地图, OS-PM-AI Runtime动态调度与降级策略, OS-PM-3B模型内存预算推演]
---

# OS PM 端侧 AI Runtime 实测实验方案

> 目标：把“端侧模型原理”推进为“真实设备上的 Runtime、硬件、性能和产品门槛判断”。

## 一、当前缺口

已有笔记覆盖 PagedAttention、KV Cache、量化、Speculative Decoding、内存预算和动态降级，但还缺少：

- 模型如何转换、编译和部署到具体 Runtime；
- 哪些算子真正运行在 NPU，哪些发生 CPU / GPU fallback；
- driver buffer、workspace、allocator fragmentation 等隐藏内存；
- batch=1 手机交互与服务器高吞吐之间的差异；
- 温度、功耗、前台负载对持续性能的影响；
- App 内置 Runtime 与系统托管 Runtime 的生命周期、隐私和兼容性差异。

## 二、实验总框架

```text
模型 / 量化
→ Runtime / Delegate / 编译
→ CPU / GPU / NPU 执行
→ 内存 / 延迟 / 功耗 / 温度
→ 稳定性与降级
→ 设备分层和产品承诺
```

## 三、实验一：NPU 真执行率

不要只记录“启用了 NPU”。应确认算子是否真的在 NPU 执行。

### 控制变量

- model
- runtime
- SoC
- OS version
- driver version
- quantization
- input shape / dynamic shape
- cold start / warm start

### 输出字段

```text
supported_ops
fallback_ops
fallback_ratio
compile_time
load_time
prefill_tok_s
decode_tok_s
peak_PSS
thermal_status
energy_per_token
```

### PM 判断

- “支持 NPU”不等于“整条模型图都在 NPU”。
- weight-only INT4 可能因为反量化或算子不支持而 fallback 到 CPU。
- Runtime、driver、模型格式和 SoC 必须进入同一兼容矩阵。

## 四、实验二：手机端 LLM 性能基线

手机通常是 batch=1 的交互场景，优先看交互延迟，而不是服务器吞吐。

### 测试维度

```text
上下文：512 / 2K / 4K / 8K / 32K
输出长度：固定 64 / 256 / 1024 tokens
状态：冷启动 / 热启动 / 前台视频 / 低电量 / 高温
```

### 核心指标

- TTFT：Time to First Token
- TPOT / ITL：每 Token 延迟
- P50 / P95 尾延迟
- prefill tok/s
- decode tok/s
- 端到端任务时延
- 工具调用格式正确率
- 模型加载时间

## 五、实验三：完整内存预算

KV Cache 不能作为唯一的内存预算。对 GQA / MQA 模型，基础估算为：

```text
KV memory =
layers
× sequence_length
× batch
× 2(K,V)
× KV_heads
× head_dim
× bytes_per_element
```

还必须加入：

- activation buffer
- attention workspace
- Runtime / driver buffer
- allocator fragmentation
- tokenizer 与 UI 内存
- mmap / Flash staging buffer
- 多请求并发预留

### 输出

- 峰值 PSS / RSS
- native heap
- KV bytes per token
- workspace 峰值
- 可用 headroom
- OOM 临界点
- 回收和恢复时间

## 六、实验四：量化与算子覆盖

比较 FP16、INT8 W8A8、INT4 weight-only 和混合精度，同时测量模型体积、峰值内存、质量损失、NPU 覆盖率、反量化开销、tok/s 和 J/token。

量化方案不能只按模型精度选择，还必须按目标 SoC 的算子支持和 fallback 结果选择。

## 七、实验五：Speculative Decoding 净收益

高 acceptance rate 不一定代表更快。draft 模型、verify 模型、处理器切换和同步开销可能抵消收益。

必须同时报告：

```text
baseline_decode_tok_s
draft_latency
verify_latency
acceptance_rate
accepted_tokens_per_verification
scheduler_overhead
net_tok_s
TTFT
J_per_token
```

## 八、实验六：持续热性能

峰值性能不等于可持续性能。建议连续运行 10 / 20 / 30 分钟，并记录时间、温度、thermal status、CPU / NPU 频率、decode tok/s、TPOT P50 / P95、功耗和内存。

产品上更有意义的是：20 分钟后的持续 tok/s、热降频后的 P95 TPOT、每 1K token 的能耗、前台是否掉帧、是否影响系统其他 AI 功能。

## 九、App Runtime 与系统 Runtime

| 项目 | App 内置 Runtime | 系统托管 Runtime |
|---|---|---|
| 模型分发 | App 自己下载和更新 | 系统 / AICore 管理 |
| 硬件适配 | App 集成多个 vendor backend | OS 统一抽象 |
| 内存 | 计入 App 预算 | 系统服务统一调度的可能性更高 |
| 隐私 | App 自己负责 | 可由系统隔离和管控 |
| 兼容性 | 包体膨胀、版本碎片化 | 依赖系统版本和设备能力 |
| 产品风险 | 迭代快但不一致 | 稳定但受平台能力限制 |

这是 OS PM 区别于纯推理工程师的关键判断：系统是否值得托管 AI Runtime，不只取决于速度，还取决于内存、更新、隐私、调度和跨 App 复用。

## 十、产品输出模板

```markdown
## 设备 / 版本
## 模型 / Runtime / Delegate
## 测试条件
## 性能结果
## 功耗与热结果
## 内存结果
## Fallback 与兼容性问题
## 用户可见影响
## 产品建议
## 发布阻断条件
```

## 十一、官方资料

- [Google AI Edge](https://ai.google.dev/edge)
- [LiteRT 总览](https://developers.google.com/edge/litert/overview)
- [LiteRT-LM](https://developers.google.com/edge/litert-lm)
- [Android AICore](https://developer.android.com/ai/aicore)
- [Android 系统跟踪与 Perfetto](https://developer.android.com/topic/performance/tracing)
- [Macrobenchmark](https://developer.android.com/topic/performance/benchmarking/macrobenchmark-overview)
- [Android Vitals](https://developer.android.com/topic/performance/vitals)
- [Qualcomm AI Engine Direct SDK](https://www.qualcomm.com/developer/software/qualcomm-ai-engine-direct-sdk)
- [Qualcomm AI Hub](https://app.aihub.qualcomm.com/docs/hub/)
- [MediaTek NeuroPilot](https://neuropilot.mediatek.com/)
- [Arm Machine Learning on Arm](https://developer.arm.com/solutions/machine-learning-on-arm)

## 十二、论文入口

- [PagedAttention / vLLM](https://arxiv.org/abs/2309.06180)：重点看 KV Cache 管理，但不要直接当作手机 batch=1 指标。
- [LLM in a Flash](https://arxiv.org/abs/2312.11514)：重点看 DRAM 不足时的 Flash 按需加载。
- [MobileLLM](https://arxiv.org/abs/2402.14905)：重点看端侧架构、GQA 和权重共享。
- [Speculative Decoding](https://arxiv.org/abs/2211.17192)：重点看 draft / verifier 机制和端侧调度开销。
- [AWQ](https://arxiv.org/abs/2306.00978)
- [SmoothQuant](https://arxiv.org/abs/2211.10438)

