---
title: 端侧小语言模型 SLM 生态 学习笔记
tags: [端侧AI, SLM, 模型选型, OS-PM]
created: 2026-08-10
source: 网络检索整理（见文末来源清单）
---

> **一句话心智模型**：端侧 SLM 不是「缩小版 LLM」，而是一张**受内存预算、许可证和 OS 分发方式三重约束的选型地图**——你真正在选的是「哪一档参数 × 哪一种许可 × 谁来负责分发权重」，能力只是这三者交叉后剩下的那个可行域。

---

## 学习定位

| 维度 | 说明 |
|---|---|
| **这篇解决什么** | 市面上端侧能用的模型家族有哪些、各自参数/上下文/许可证/落地形态如何、一个 OS PM 做选型时看哪些字段 |
| **这篇不解决什么** | 量化算法细节（见 [[端侧模型量化 学习笔记]]）、推理引擎与编译栈（见 [[移动端 NPU 与推理编译栈 学习笔记]]）、NPU 硬件与调度（见 [[端侧大模型推理 学习笔记]]）、模型架构分类学（见 [[AI模型类型与架构]]） |
| **深度约定** | **广度优先**。所有跑分数字一律不列（多方口径矛盾，列了会误导）；只列「硬信息」：参数量、上下文、许可证、发布时间、官方宣称形态 |
| **诚实约定** | 厂商口径标注「厂商宣称」，第三方实测标注「第三方」，核实不到的一律进文末 ⚠️ 清单 |

---

## 一、SLM 的定义与边界

### 1.1 「多少 B 算 small」没有统一答案

| 口径来源 | 定义 | 备注 |
|---|---|---|
| NVIDIA《Small Language Models are the Future of Agentic AI》(arXiv:2506.02153, 2025-06) | 能在**消费级设备上低延迟运行**的模型；论文给出 2025 年的经验阈值 **< 10B** | 定义锚在「能不能跑」而非参数数字本身，这是最适合 PM 借用的口径 |
| 厂商产品线口径 | 各家「端侧档」实际落在 **0.5B ~ 4B**（Apple ~3B、Gemini Nano 1.8B/3.25B、Qwen 0.6B~4B、Gemma E2B/E4B） | 手机侧真实可商用区间比论文阈值窄很多 |
| 「有效参数」口径 | Gemma 3n / Gemma 4 的 E 系列用 Per-Layer Embeddings，**总参数 ≠ 内存占用**（E2B 总参 5.1B、有效 2.3B） | 参数量作为选型指标正在失效，必须看实际内存 |

> 结论：**别用参数量当唯一尺子**。PM 该问的是「Q4 量化后常驻内存多少 MB、TTFT 多少 ms」，参数量只是代理指标。

### 1.2 为什么端侧非要 SLM 不可

| 端侧约束 | 直接后果 | 对模型的硬要求 |
|---|---|---|
| 手机可用 RAM 有限（旗舰 12–16GB，但 OS 只能给 AI 分配其中一小块） | 权重必须常驻或秒级加载 | 量化后 < 2–3GB |
| 统一内存 / 带宽是瓶颈 | decode 速度受内存带宽而非算力限制 | 参数越小 tok/s 越高 |
| 电池与发热 | 不能长时间满载 NPU | 短 prompt、短输出、低激活参数 |
| 分发成本 | 权重不能塞进每个 APK | 走 OS 级服务分发（AICore / Foundation Models） |
| 隐私与离线 | 数据不能出设备 | 能力必须自包含，不能依赖云补齐 |

延伸：内存预算怎么算见 [[OS-PM-3B模型内存预算推演]] 与 [[端侧 AI 基建与算力预算]]。

---

## 二、主流端侧模型家族横向盘点

### 2.1 两大阵营先分清

| 阵营 | 代表 | 权重归谁 | 谁负责分发 | PM 的控制力 |
|---|---|---|---|---|
| **开放权重（Open-weight）** | Phi、Gemma、Qwen、Llama、MiniCPM、SmolLM | 你可以下载/微调/自己打包 | 你自己（或你的 OS） | 高：可换、可调、可裁 |
| **OS 内置（平台托管）** | Gemini Nano（Android AICore）、Apple 端侧基础模型（Foundation Models framework） | 厂商 | 操作系统按需下发 | 低：只能调 API，模型黑盒 |

> 对 Android OS PM 而言：**这两条路不是二选一，而是同时存在**——系统能力走平台托管，差异化能力往往需要自带开放权重模型。

### 2.2 开放权重阵营：规格横向对比

| 家族 | 端侧代表型号 | 参数量 | 原生上下文 | 许可证 | 模态 | 公开发布时间 |
|---|---|---|---|---|---|---|
| **Microsoft Phi** | Phi-4-mini-instruct | 3.8B | 128K | **MIT** | 纯文本 | 2025-02-26 |
| Microsoft Phi | Phi-4-multimodal-instruct | 5.6B | 128K | **MIT** | 文本 + 视觉 + 语音 | 2025-02-26 |
| **Google Gemma 3** | Gemma 3 1B | 1B | **32K** | Gemma Terms of Use | 纯文本 | 2025-03-12 |
| Google Gemma 3 | Gemma 3 4B | 4B | 128K | Gemma Terms of Use | 文本 + 图像 | 2025-03-12 |
| Google Gemma 3 | Gemma 3 270M | 270M | 32K | Gemma Terms of Use | 纯文本 | 2025 年（月份待核实） |
| **Google Gemma 3n** | Gemma 3n E2B | 总参 ~5B / 有效 ~2B | **32K** | Gemma Terms of Use | 文本+图像+音频+视频 | 2025-06-26（5 月预览） |
| Google Gemma 3n | Gemma 3n E4B | 总参 ~8B / 有效 ~4B | **32K** | Gemma Terms of Use | 同上 | 2025-06-26 |
| **Google Gemma 4** | Gemma 4 E2B | 总参 5.1B / 有效 2.3B | 128K | **Apache 2.0** | 文本+图像+视频+音频 | 2026 年（约 4 月初，日期待核实） |
| Google Gemma 4 | Gemma 4 E4B | 总参 8B / 有效 4.5B | 128K | **Apache 2.0** | 同上 | 同上 |
| Google Gemma 4 | Gemma 4 26B A4B (MoE) | 总参 25.2B / 激活 3.8B | 256K | **Apache 2.0** | 文本 + 图像（无音频） | 同上 |
| **Alibaba Qwen3** | Qwen3-0.6B | 0.6B | 32K | **Apache 2.0** | 纯文本 | 2025-04/05 |
| Alibaba Qwen3 | Qwen3-1.7B | 1.7B | 32K | **Apache 2.0** | 纯文本 | 2025-04/05 |
| Alibaba Qwen3 | Qwen3-4B | 4B | 32K（官方表；社区称可 YaRN 扩至 128K） | **Apache 2.0** | 纯文本 | 2025-04/05 |
| **Alibaba Qwen3.5 Small** | Qwen3.5-0.8B / 2B / 4B / 9B | 0.8B / 2B / 4B / 9B | 262,144 tokens | **Apache 2.0** | 文本 + 图像（早融合） | 2026 年 2–3 月（具体日期各方矛盾） |
| **Meta Llama 3.2** | Llama-3.2-1B-Instruct | 1.23B | 128K | Llama 3.2 Community License | 纯文本 | 2024-09-25 |
| Meta Llama 3.2 | Llama-3.2-3B-Instruct | 3.21B | 128K | Llama 3.2 Community License | 纯文本 | 2024-09-25 |
| **面壁 MiniCPM** | MiniCPM4-0.5B | 0.5B | 待核实 | **Apache 2.0** | 纯文本 | 2025-06-06 |
| 面壁 MiniCPM | MiniCPM4-8B | 8B | 128K（InfLLM v2 稀疏注意力） | **Apache 2.0** | 纯文本 | 2025-06-06 |
| 面壁 MiniCPM | MiniCPM4.1 | 待核实 | 原生 64K，YaRN 扩至 128K+ | **Apache 2.0** | 待核实 | 待核实 |
| **HuggingFace SmolLM** | SmolLM3-3B | 3B | 待核实（LiteRT 端侧包按 4096 KV 打包） | **Apache 2.0** | 纯文本 | 2025 年（待核实） |

**读表要点**：
- 上下文长度差异极大（32K ↔ 262K），且**同一家族内不同尺寸不一样**（Gemma 3 的 1B 是 32K 而 4B 是 128K）——这是最容易踩坑的字段。
- 「128K 上下文」是模型能力上限，不等于端侧可用值：KV cache 会吃掉内存预算，实际端侧往往只开 4K–32K。
- Gemma 4 换成 Apache 2.0 是 2026 年最重要的许可证事件（此前三代都是 Google 自有条款）。

### 2.3 OS 内置阵营：规格与形态

| 项目 | Google Gemini Nano | Apple 端侧基础模型 |
|---|---|---|
| 参数量 | Nano-1 1.8B / Nano-2 3.25B（Gemini 1.0 技术报告口径，广泛引用）；Pixel 9a 上另有裁剪版 Nano XXS | **约 3B**（Apple 2025 技术报告口径） |
| 上下文 | 4,096 tokens（第三方资料，⚠️ 待核实）；Nano 3 称扩至 8K（⚠️ 待核实） | **4,096 tokens / session**（Apple 官方文档，明确写死）；云端 PCC 模型 32K |
| 量化 | 4-bit（第三方） | **2-bit 权重 QAT**，embedding 4-bit，KV cache 8-bit（Apple 技术报告） |
| 架构优化 | 待核实 | KV-cache 共享：模型切两块，Block2 复用 Block1 的 KV，**KV 内存 −37.5%、TTFT −约 37.5%**（Apple 技术报告） |
| 分发方式 | **AICore** 系统服务统一下发/更新，权重不进 APK | 随 OS 内置，`FoundationModels` 框架暴露 |
| 开发者入口 | Google AI Edge SDK（低层）+ **ML Kit GenAI API**（Summarization / Proofreading / Rewriting / Image Description / Prompt / Speech） | Swift API：Guided Generation（`@Generable`/`@Guide`）、Tool Calling、Stateful Session |
| 定制方式 | **LoRA adapter 按需加载**，每个能力一个 adapter | **LoRA adapter 训练工具包**开放给开发者 |
| 硬件门槛 | Pixel 8+/Samsung S24+ 等，依赖 Tensor / Snapdragon / Dimensity NPU | A17 Pro 以上 iPhone、M1 以上 iPad/Mac |
| 云端兜底 | 切换到 Gemini 云端 API | Private Cloud Compute（32K 上下文） |

> Apple 侧的完整架构见 [[Apple Intelligence 端侧架构 学习笔记]]；这里只取「选型可比字段」。

### 2.4 许可证：PM 最该先看的一列

| 许可证 | 代表模型 | 商用 | 关键限制 | OS 厂商风险评级 |
|---|---|---|---|---|
| **MIT** | Phi-4-mini / Phi-4-multimodal | ✅ 自由 | 几乎无（保留版权声明） | 最低 |
| **Apache 2.0** | Qwen3 / Qwen3.5 / MiniCPM4 / SmolLM3 / **Gemma 4** | ✅ 自由 | 需保留声明；含专利授权条款 | 低 |
| **Gemma Terms of Use** | Gemma 3 / Gemma 3n | ✅ 允许商用 | 非 OSI 开源；含使用限制条款（Prohibited Use Policy），且**下游分发需传递条款** | 中：法务需逐条审 |
| **Llama 3.2 Community License** | Llama 3.2 1B / 3B | ✅ 但有门槛 | **月活 > 7 亿需单独向 Meta 申请授权**；须显著标注 "Built with Llama"；衍生模型名须以 "Llama" 开头 | **高**：手机 OS 天然逼近 7 亿 MAU 红线 |
| 平台闭源 | Gemini Nano / Apple AFM | N/A | 不给权重，只给 API；能力边界由平台定义 | 不适用「选型」，属于「依赖」 |

> **对 Android OS PM 的直接结论**：Llama 3.2 的 7 亿 MAU 条款对绝大多数创业公司是「理论限制」，但对一个手机 OS 厂商是**真实的商务动作**。Gemma 4 转 Apache 2.0 之后，Google 系模型在合规上第一次和 Qwen/Phi 拉平。

### 2.5 内存占用：怎么估，别抄数字

先记公式，再看样本：

```
常驻内存 ≈ 权重字节数 + KV cache + 运行时开销
权重字节数 ≈ 参数量 × (量化位宽 / 8)
KV cache   ≈ 2 × 层数 × KV头数 × head_dim × 上下文长度 × KV位宽/8
```

| 样本 | 配置 | 观测/宣称占用 | 来源性质 |
|---|---|---|---|
| Phi-4-mini | Q4_K_M GGUF | 权重文件 2.49 GB；运行约 3.2 GB（+128K 上下文再加 1–2 GB） | 第三方实测博客 |
| SmolLM3-3B | int4 blockwise, KV 4096 | 文件 ~1.9 GB；iPhone 17 Pro 上 footprint ~1.24 GB | 模型卡（LiteRT 社区） |
| Gemma 3n E2B / E4B | 官方优化 | ~2 GB / ~3 GB RAM | **厂商宣称** |
| Gemma 4 E2B | 4-bit | 「部分设备可压到 1.5 GB 以下」 | **厂商宣称（媒体转述）** |
| Qwen3.5-2B | Q4 | ~1.5 GB 权重 + 2–3 GB 上下文余量 | 第三方 |

> ⚠️ 上表**不能直接抄进需求文档**。量化方案、KV 位宽、上下文开多长会让结论翻倍。真正的推演方法见 [[OS-PM-3B模型内存预算推演]]，量化位宽与精度损失的取舍见 [[端侧模型量化 学习笔记]]。

---

## 三、训练侧路线：这个模型是怎么变小的

| 路线 | 做法 | 代表 | 优点 | 代价 |
|---|---|---|---|---|
| **从头训小模型 + 数据工程** | 不压缩大模型，直接用高质量/合成数据训练小模型 | Phi 系列（合成「教科书式」数据，Phi-4-mini 训练 ~5T tokens）；SmolLM3 | 架构自由，可为端侧定制；数据配方是壁垒 | 需要完整预训练算力；数据配方难复现 |
| **知识蒸馏（Distillation）** | 小学生模型学大教师模型的输出分布（logits）或合成数据 | Gemma 系列（从 Gemini 蒸馏，按 token 采样 teacher logits）；Gemini Nano（从 Gemini 教师蒸馏） | 同参数量下质量更高；能继承教师的行为风格 | 依赖有一个强教师；容易继承教师的偏差 |
| **结构化剪枝 + 蒸馏再训练** | 先剪层/神经元/注意力头，再用原模型当教师做轻量再训练 | NVIDIA Minitron（15B→8B→4B；Llama-3.1 8B→4B） | NVIDIA 报告：相比从头训 MMLU **+16%**，每个衍生模型只需 **~100B tokens（最多省 40×）**，训练一整个家族省 **~1.8× 算力** | 只能从已有大模型派生；受原架构约束 |
| **极限量化 / 三值化** | 训练时就把权重压到 2 bit 甚至三值 | Apple 端侧模型（2-bit QAT）；BitCPM4（三值，宣称位宽降 90%） | 内存收益最大 | 需 QAT，训练成本高；常需 LoRA 补偿精度损失 |

**一句话取舍**：想要**可控与差异化**→从头训 + 数据工程；想要**性价比最高的家族矩阵**→剪枝 + 蒸馏；想要**端侧内存极限**→QAT + adapter 补偿。

---

## 四、SLM 与 LoRA adapter 热插拔

这是端侧 SLM 生态里最「产品化」的一环：**一个基座模型 + N 个小 adapter**，而不是 N 个模型。

| 厂商 | 基座 | Adapter 机制 | 分发方式 | 官方给出的收益 |
|---|---|---|---|---|
| Google（Android） | Gemini Nano | 每个 ML Kit GenAI 能力配一个任务专属 LoRA，基座在设备上后按需加载 | AICore 系统服务 | **厂商宣称**：摘要质量内部评分 77.2 → 92.1；图像描述 86.9 → 92.3 |
| Apple | ~3B 端侧模型 | Foundation Models 框架开放 adapter 训练工具包；另有官方 Content Tagging Adapter | Background Assets 框架下发 | 第三方资料称 LoRA rank 32、单 adapter ~160MB（⚠️ 待核实） |
| Microsoft | Phi-4-mini | Phi-4-multimodal 直接把视觉/语音编码器通过 **LoRA adapter 挂到冻结的 Phi-4-mini 权重上** | 随模型发布 | 用一套语言骨干支撑多模态，避免重复常驻 |

**对 OS PM 的三个含义**：
1. **内存预算是按「基座 + 当前激活 adapter」算的**，不是按能力数量线性增长——这直接改变功能规划的成本模型。
2. **Adapter 是安全与合规的注入点**：Google 明确把 app 级安全数据训进 LoRA，让同一基座在不同场景满足不同安全标准。
3. **Adapter 可独立于 OS 版本更新**，能力迭代节奏和 OS 大版本解耦，这对产品排期意义很大。

架构维度上「外挂 adapter vs 原生多模态」的区别见 [[外挂适配式 vs 原生多模态架构]]。

---

## 五、能力天花板：哪些任务够用，哪些必须上云

| 任务类型 | 端侧 SLM（~1–4B） | 判断依据 |
|---|---|---|
| 文本摘要（短–中长） | ✅ 够用 | Apple/Google 官方文档都把摘要列为首推场景 |
| 改写 / 润色 / 校对 / 语气调整 | ✅ 够用 | ML Kit 直接提供 Proofreading / Rewriting API |
| 实体抽取、意图分类、打标签 | ✅ 够用（最佳场景） | Apple 官方能力表明确列出「抽取实体」「分类判断」「生成标签」 |
| 结构化输出 / JSON 生成 | ✅ 够用（需 guided generation 约束） | Apple `@Generable`、Gemma 4 原生结构化输出 |
| 函数调用 / 工具编排（步数少） | ⚠️ 边界地带 | Phi-4-mini、Gemma 4、MiniCPM4-MCP 都宣称支持；复杂多步仍不稳 |
| 短对话 / 游戏 NPC 对白 | ✅ 够用 | Apple 官方示例场景 |
| 数学计算 / 精确算术 | ❌ 应避免 | Apple 官方**明确列为「应避免的能力」** |
| 代码生成 | ❌ 端侧小尺寸应避免 | Apple 官方明确列为「应避免」；Gemma 4 的离线代码能力宣称在 26B/31B 档，非手机档 |
| 复杂逻辑/空间推理 | ❌ 应避免 | Apple 官方明确列为「应避免」 |
| 依赖世界知识的事实问答 | ❌ 必须上云或接 RAG | 小模型参数容量放不下长尾知识 |
| 超长文档（>32K 有效上下文） | ❌ 端侧受 KV cache 内存限制 | Apple 端侧 4096 tokens；需切块多 session 或走云端 |
| 多轮长记忆对话 | ❌ 受上下文窗口硬限 | Apple 官方给出的解法就是「拆成多个 session」 |

**能力边界的产品化表述**：端侧 SLM 擅长「**对已给定的文本做变换**」，不擅长「**凭空提供知识或做长链推理**」。这条线基本可以直接当作端云分流的第一版规则。分流与降级的工程做法见 [[OS-PM-AI Runtime动态调度与降级策略]] 与 [[端侧意图路由选型 PM Checklist]]。

---

## 六、2025–2026 的进展趋势

| 趋势 | 具体表现 | 证据强度 |
|---|---|---|
| **许可证向 Apache 2.0 收敛** | Gemma 4 从 Google 自有条款切到 Apache 2.0；Qwen / MiniCPM / SmolLM 本就 Apache 2.0；Phi 是 MIT | 强（官方模型卡） |
| **「有效参数」取代「总参数」成为端侧口径** | Gemma 3n / Gemma 4 的 PLE 技术；MoE 的激活参数（26B A4B 只激活 3.8B） | 强 |
| **端侧模型默认多模态** | Gemma 3n/4 原生音频+视频；Qwen3.5 Small 全系带视觉编码器（早融合）；Phi-4-multimodal 视觉+语音 | 强 |
| **端侧上下文从 4K 向 128K–256K 拉** | Qwen3.5 Small 原生 262,144；Gemma 4 边缘档 128K | 中（模型能力≠端侧可用，受 KV cache 限） |
| **稀疏/线性注意力进端侧** | MiniCPM4 的 InfLLM v2 可训练稀疏注意力（128K 下每 token 只算 <5% token）；Qwen3.5 的 Gated DeltaNet 混合注意力 | 中强 |
| **「SLM 是 Agent 的未来」成为学术立场** | NVIDIA 2025-06 立场论文；对三个开源 Agent 的案例估计：MetaGPT ~60%、Open Operator ~40%、Cradle ~70% 的 LLM 调用可由 SLM 承担 | 中（属论文估计，非实测） |
| **异构模型编排成为默认架构** | Apple：端侧 + PCC（32K）+ 第三方 provider 三层可组合；Google：Nano 端侧 + Gemini 云端 | 强 |
| **开放权重模型成为 OS 内置模型的基座** | 媒体报道 Gemma 4 是下一代 Gemini Nano 4 的基座、AICore Developer Preview 向前兼容 | 弱（⚠️ 仅媒体转述，待核实） |

---

## 七、对 OS PM 的意义

### 7.1 选型时真正要填的表

| 字段 | 为什么 PM 必须问 | 常见坑 |
|---|---|---|
| 许可证类型 + MAU 门槛 | 决定能不能预装进出货机 | Llama 系的 7 亿 MAU 条款对 OS 厂商是硬约束 |
| Q4 量化后权重体积 | 决定 ROM 占用与 OTA 包大小 | 只看参数量会低估 30–50% |
| 端侧**实际开放**的上下文 | 决定产品形态（能不能读整封邮件） | 把「模型支持 128K」当成「端侧能用 128K」 |
| 是否支持 adapter 热插拔 | 决定能力扩展的边际成本 | 每个能力独立模型 = 内存与 ROM 线性爆炸 |
| 模态覆盖（音频/视觉） | 决定要不要额外挂编码器 | 挂外部编码器会额外吃内存与常驻 |
| 结构化输出/函数调用是否原生 | 决定要不要自己写解析兜底 | 靠正则解析自由文本的方案维护成本极高 |
| 权重由谁分发 | 决定 OTA 策略与包体归属 | 塞进 APK 会被应用市场包体限制卡死 |
| 模型迭代节奏 | 决定能否跟上 OS 大版本 | 一年一代 vs 季度一代，排期完全不同 |

### 7.2 三条可以直接拿去用的判断

1. **端侧模型选型的第一道过滤器是许可证，不是跑分。** 跑分差 3 个点可以靠 adapter 补，许可证不合规是一票否决。
2. **「一个基座 + N 个 adapter」应当作为端侧 AI 能力规划的默认架构范式。** Google、Apple、Microsoft 三家在这一点上已经收敛到同一答案。
3. **端云分流规则的第一版可以直接照抄「文本变换 vs 知识/推理」这条线。** 不需要等到有精确的路由模型，先用任务类型硬编码，再逐步演进到动态路由。

更上位的系统级挑战见 [[OS-PM-端侧大模型系统级挑战]]；本笔记归属 [[AI模型基础 MOC]]。

---

## 待解问题（留给 Ethon 深挖）

- [ ] Gemma 4 E2B/E4B 的 PLE「有效参数」在**真实 Android 设备**上到底省了多少内存？和 Gemma 3n 的同名技术相比增量在哪？
- [ ] Qwen3.5 Small 宣称的 262K 原生上下文，在手机 4–6GB 可用内存下**实际能开到多少 K**？KV cache 是瓶颈还是权重是瓶颈？
- [ ] Apple 把端侧上下文硬限在 4096 tokens 是**架构限制还是产品决策**？如果是后者，Android 侧敢不敢开更大？
- [ ] Gemini Nano 3 / Nano 4 的真实规格（参数量、上下文、是否支持 function calling）——目前公开信息全是二手转述，需要找官方文档或 Android 开发者博客确认。
- [ ] LoRA adapter 在端侧的**切换延迟**是多少？能否做到跟随用户当前 App 实时热切？160MB/adapter 的说法是否成立？
- [ ] 「一个基座 + N adapter」在 OS 层需要什么样的生命周期管理（谁触发下载、谁做版本对齐、谁做内存驱逐）？
- [ ] 三值化 / 2-bit QAT（BitCPM4、Apple AFM）在中文任务上的质量损失，是否和英文一致？国内厂商能否直接照搬？
- [ ] 从 OS 厂商角度，自研端侧 SLM vs 基于 Apache 2.0 模型做深度定制，**分水岭在哪个业务量级**？
- [ ] 端侧 SLM 的 function calling 可靠性怎么量化？有没有可复现的评测集（而不是厂商自报）？
- [ ] Gemma 4 转 Apache 2.0 之后，Google 在端侧的商业模式如何闭环？这对 Android 生态的模型分发策略意味着什么？

---

## 附：来源清单

| 来源名 | 链接 | 查阅日期 |
|---|---|---|
| Microsoft Phi-4-mini-instruct 官方模型卡（HuggingFace） | https://huggingface.co/microsoft/Phi-4-mini-instruct | 2026-08-10 |
| Google Gemma 3 官方模型卡 | https://ai.google.dev/gemma/docs/core/model_card_3 | 2026-08-10 |
| Google Gemma 3n 官方模型卡 | https://ai.google.dev/gemma/docs/gemma-3n/model_card | 2026-08-10 |
| Google Gemma 4 官方模型卡 | https://ai.google.dev/gemma/docs/core/model_card_4 | 2026-08-10 |
| Qwen3 官方发布博客（含各尺寸上下文表） | https://qwen.ai/blog?id=qwen3 | 2026-08-10 |
| Meta Llama-3.2-1B 官方模型卡（含 Community License 全文） | https://huggingface.co/meta-llama/Llama-3.2-1B/blob/main/README.md | 2026-08-10 |
| Llama 3.2 Community License 摘要（7 亿 MAU 条款） | https://canirun.ai/license/llama-3-2-community/ | 2026-08-10 |
| MiniCPM4-3B-Base 模型卡（ModelScope） | https://modelscope.cn/models/OpenBMB/MiniCPM4-3B-Base | 2026-08-10 |
| MiniCPM4-0.5B-mlx 模型卡（ModelScope） | https://www.modelscope.cn/models/OpenBMB/MiniCPM4-0.5B-mlx | 2026-08-10 |
| SmolLM3-3B LiteRT-LM 端侧版模型卡 | https://modelscope.cn/models/litert-community/SmolLM3-3B | 2026-08-10 |
| Apple Intelligence Foundation Language Models Tech Report 2025 | https://machinelearning.apple.com/papers/apple_intelligence_foundation_language_models_tech_report_2025.pdf | 2026-08-10 |
| Apple 开发者文档：Managing the context window（4096 tokens） | https://developer.apple.com/documentation/FoundationModels/managing-the-context-window | 2026-08-10 |
| Apple 开发者文档：Generating content with Foundation Models（能力/避免能力表） | https://developer.apple.com/documentation/foundationmodels/generating-content-and-performing-tasks-with-foundation-models | 2026-08-10 |
| Apple TN3193 技术说明（上下文窗口管理） | https://developer.apple.com/documentation/Technotes/tn3193-managing-the-on-device-foundation-model-s-context-window | 2026-08-10 |
| NVIDIA 技术博客：Prune and Distill Llama-3.1 8B → Minitron 4B | https://developer.nvidia.com/blog/how-to-prune-and-distill-llama-3-1-8b-to-an-nvidia-llama-3-1-minitron-4b-model/ | 2026-08-10 |
| NVIDIA Research：Small Language Models are the Future of Agentic AI（arXiv:2506.02153） | https://research.nvidia.com/labs/lpr/slm-agents | 2026-08-10 |
| Gemini Nano / AICore / ML Kit GenAI 综述（含 LoRA 提升数据） | https://aiwiki.ai/wiki/gemini_nano | 2026-08-10 |
| Gemma 4 发布报道（钛媒体） | https://www.tmtpost.com/7940633.html | 2026-08-10 |
| Gemma 4 开源解读（53AI / 赛博禅心） | https://www.53ai.com/news/OpenSourceLLM/2026040397423.html | 2026-08-10 |
| Qwen3.5 Small Series 规格综述（第三方） | https://machineherald.io/article/2026-03/15-alibaba-qwen-35-small-models-pack-multimodal-intelligence-into-sub-10-billion-parameters-for-edge-devices | 2026-08-10 |
| Phi-4-mini 本地部署实测（GGUF 体积与内存） | https://tinyweights.dev/posts/run-phi-4-mini-locally | 2026-08-10 |

---

## ⚠️ 待核实清单

1. **Gemma 3 270M 的具体发布月份** —— 第三方称 2025 年 8 月，未在官方模型卡中找到明确日期。
2. **Gemma 3n 的上下文长度** —— 官方模型卡写 32K，但多个第三方页面写 128K，存在矛盾；本文采信官方 32K。
3. **Gemma 4 的确切发布日期** —— 官方模型卡未标日期，媒体口径为 2026-04-02/03，需以 Google 官方博客为准。
4. **Gemma 4 的 12B Unified 型号** —— 官方模型卡列出 5 个变体（含 12B Unified），但发布期媒体普遍只报道 4 个，可能是后续追加，需核实。
5. **Qwen3.5 Small Series 的发布日期** —— 「2 月下旬 / 3 月 1 日 / 3 月 2 日」三种说法并存，需以 Qwen 官方博客为准。
6. **Qwen3.5 各尺寸的上下文** —— 有 256K 与 262,144 两种写法（后者更可能是官方值），且未找到官方模型卡一手确认。
7. **Qwen3-4B 的上下文** —— 官方发布博客表格写 32K，部分二手资料写「原生 32K / 可扩 128K」，扩展方式与官方支持度待确认。
8. **MiniCPM4-0.5B 的上下文长度** —— 未在模型卡中找到明确数值。
9. **MiniCPM4.1 / MiniCPM-SALA 的参数量与发布时间** —— 仅见第三方聚合站描述，无一手模型卡佐证。
10. **SmolLM3-3B 的原生上下文长度与发布日期** —— 仅确认 Apache 2.0 与 3B 参数，端侧包按 4096 KV 打包不等于模型上限。
11. **Gemini Nano 的上下文窗口（4,096 tokens / 单 prompt 1,024 tokens）** —— 仅见第三方博客，未找到 Google 官方文档明确数值。
12. **Gemini Nano 3 / Nano v3 的规格** —— 参数量（3.5B？）、上下文（8K？）、发布时间（2026-07-17？Android 15+？还是 I/O 2026 随 Android 17？）多方说法互相矛盾，**本文正文未采信任何一种**。
13. **Gemma 4 是否为 Gemini Nano 4 的基座** —— 仅见媒体转述，无官方确认。
14. **Apple LoRA adapter 的 rank 32 与单个 ~160MB 体积** —— 来自第三方开发者博客，Apple 官方文档未见此数据。
15. **Apple 端侧模型支持的语言数量** —— 技术报告称「16 种语言」，另有二手资料写 15 种。
16. **Apple「AFM core advanced ~20B」模型** —— 来自 WWDC26 Group Lab 问答转述，非正式文档，规格与定位均待核实。
17. **各家端侧内存占用数字** —— 表 2.5 中「厂商宣称」行未经独立复现；「第三方」行的测试硬件与量化配置各不相同，不可横向直接比较。
18. **NVIDIA 立场论文中 MetaGPT 60% / Open Operator 40% / Cradle 70% 的可替换比例** —— 属论文作者估计值，非实测结果。

---

#笔记/端侧AI #笔记/模型选型
