---
title: "端侧语音唤醒与 always-listening 隐私边界 学习笔记"
tags: [手机AI智能体, 端侧, 语音唤醒, 隐私, 广度种子]
created: 2026-10-30
source: [asqvox wake-word glossary, hashlytics how-androids-always-on-microphone-works, dataintelo ultra-low-power-voice-dsp-market, allaboutcircuits AON1120 CES2025, google support speaker lights, ifeng 2025 AI手机跑马灯隐私指示灯, clario/bbpmag/androidguias 麦克风隐私指示灯, freedomtech/franklinetech 语音助手隐私和解报道]
---

## 心智模型（一句话）

端侧语音唤醒 = 让一颗**超低功耗协处理器**在手机"睡着"时持续只监听一个唤醒词、其余音频本地丢弃不传出；它解决的是「既要随时待命、又不想把麦克风 24h 流式上云」的隐私/功耗矛盾——而真正的隐私风险不在"常录"，而在**误唤醒（false accept）把本不想录的对话送了出去**。

---

## 1. 定义：什么是 wake word / hotword detection

- **Wake word（唤醒词）**：触发设备"开始认真听"的那句短语（"Hey Siri" / "小爱同学" / "OK Google" / "Hi Bixby"）。
- **Hotword detection（热词检测）**：设备上**常驻、低功耗、本地运行**的一个极小模型，只认这一句话、拒绝其它一切；命中后才打开后续链路。
- 核心约束：必须在**极小功耗 + 极小算力预算**下无限期运行；命中前音频一般本地丢弃，仅保留一小段滚动缓冲（rolling buffer）防止漏掉句首。
- 设计目标不是"录一切"，恰恰相反——**靠本地检测避免把全量音频流式上云**（成本、带宽、隐私三重原因）。

## 2. 分类

### 2.1 唤醒技术路线

| 路线 | 运行位置 | 功耗 | 隐私姿态 | 备注 |
|---|---|---|---|---|
| 端侧唤醒（on-device） | 设备内低功耗 DSP/协处理器 | 极低（µW~mW 级） | 最优：麦克风音频不离开设备，直到唤醒词命中 | 主流手机/音箱默认，也是延迟更低的选择 |
| 服务端唤醒（server-side） | 原始音频持续流式到本地/远端主机 | 取决于传输 | 较弱：音频**持续在流**，即使不离开 LAN | 常见于硬件太弱跑不动本地模型的 DIY 方案，非主流消费设备 |

### 2.2 隐私级别（从强到弱）

| 级别 | 特征 | 代表 |
|---|---|---|
| L0 完全本地、不留存 | 唤醒后语音也在端侧处理/不留存 | Apple（尽量端侧 + 明确 opt-in 才留存） |
| L1 端侧唤醒、命中后上云 | 唤醒前不传，命中后音频/转写外发做 NLP | 多数 Android 语音助手默认 |
| L2 云端处理、处理后删除 | 音频仍上云，仅处理后删除而非留存 | Amazon Alexa（2025 移除本地处理选项后默认）【待核实】 |
| L3 持续流式上传 | 音频持续外发（含误唤醒片段） | 事故/泄露场景，非设计目标 |

## 3. 主流方案（端侧唤醒引擎 + 协处理器）

| 厂商/方案 | 低功耗载体 | 要点 |
|---|---|---|
| Apple | Neural Engine + 嵌入式微控制器 | "Hey Siri" 端侧检测；更重请求走 Private Cloud Compute（PCC） |
| Qualcomm | Hexagon DSP 内的 Sensing Hub（双 micro-NPU） | 安卓阵营主流 always-on 语音/传感器监听底座 |
| MediaTek | APU | 端侧 AI 协处理，含唤醒/情境感知 |
| NXP / Broadcom / Synaptics | 专用低功耗音频引擎 / 独立 DSP 核 | 独立供电域，主 AP 断电仍可监听 |
| AONDevices AON1120（CES 2025） | 双 NPU + RISC-V + DSP，<50KB 模型 | 监听模式 ~80µW、全处理 <260µW，噪杂环境（SNR<0dB）命中率>90%【厂商口径，待核实】 |
| 通用范式 | TensorFlow Micro / Cortex-M 级推理 | 单次推理几毫秒、内存可控，嵌入式"AI 迷你引擎" |

**功耗量级参考**：主流协处理器常驻监听约 5–10 mW，约占每日电量 1%【单一来源，待核实】；超低功耗语音 DSP 在检测模式可低于 10 mW，通用 AP 则 500mW+。

## 4. 2025–2026 进展（点到为止）

- **指示灯成为隐私信任核心 UI**：iOS 14 / Android 12 起系统级麦克风指示（iOS 橙点、Android 绿/橙点）——"AI 手机又爱上跑马灯"，Apple 借 Privacy Indicator / Visual Intelligence 把"AI 何时介入"可视化，强化过程正义与信任。
- **Gemini for Home 接替 Google Assistant**（智能音箱/显示器，2025-10-28 早期接入）：保留 "Hey Google" 唤醒词，新增多色 LED 反馈；唤醒后链路向 Gemini 云端能力迁移。
- **法律判例收紧隐私预期**：Apple Siri 集体诉讼和解（约 $95M，2025 年 9 月法院批准）、Google Assistant 类似和解（约 $68M，2026 年 1 月达成）【媒体口径金额，待核实】——核心是"误唤醒片段被人审/外泄"。
- **Amazon Alexa+ 转向云端 LLM**：报道称 2025-03-28 起移除部分 Echo 的"Do Not Send Voice Recordings"本地处理选项，命令默认上云【媒体口径，待核实】。
- **超低功耗语音 DSP 市场扩张**：报告称 2025 年约 $1.92B → 2034 年 $4.95B（CAGR 11.2%），受 GDPR / EU AI Act 推动"端侧处理"合规需求【市场报告口径，待核实】。

## 5. 代表产品与 OS 实现

| 产品 | 唤醒词 | 端侧/云端切分 | 隐私指示灯/开关设计 |
|---|---|---|---|
| Siri（Apple） | "Hey Siri" | 端侧检测；复杂请求走 PCC | iOS 橙点（麦克风调用）；相对最隐私优先 |
| Google Assistant / Gemini | "Hey Google" / "OK Google" | 端侧 Voice Match 检测；命中后上云 NLP | Android 绿/橙点；音箱有麦克风物理开关 + 四橙点=mic off |
| 小爱同学（Xiaomi） | "小爱同学" | 端侧唤醒 + 云端语义【具体芯片/本地处理边界待核实】 | HyperOS 麦克风指示与物理/系统静音【具体设计待核实】 |
| Bixby（Samsung） | "Hi Bixby" | 端侧唤醒 + 三星云/端侧混合【具体低功耗载体待核实】 | One UI 麦克风指示与权限管控【具体设计待核实】 |
| Amazon Alexa / Alexa+ | "Alexa" | 端侧唤醒；Alexa+ 默认云端 LLM | 音箱物理静音键 + 橙灯=mic off |

**隐私边界设计的四件套（行业共识方向）**：① 系统级指示灯（mic/cam dot）让用户看见何时在听；② 本地处理优先、命中前不出端；③ 数据最小化（不存/短时存/可删）；④ 可完全关闭（物理键或系统开关）。

---

## 深度盲区（留给 Ethon 补充）

- [ ] **误唤醒率（FAR）与拒唤醒率（FRR）的真实产品级权衡曲线**：各厂商训练阈值设在哪？中文多音字/口音下的 FAR 实测是多少？
- [ ] **小爱 / Bixby 的端侧唤醒具体硬件载体与本地处理边界**：小米用哪家 DSP/NPU？唤醒后多久上云、哪些语义留端？
- [ ] **双阶段检测（粗筛+精确认证）、上下文过滤（连续两次命中）在主流 OS 的工程落地细节**。
- [ ] **"可关闭"的产品可用性代价**：关掉 always-listening 后，哪些依赖常驻感知的功能会退化？PM 视角的取舍。
- [ ] **EU AI Act / 国内个人信息保护法对"默认麦克风常驻"的合规要求边界**，与厂商 disclosure 义务的差异。
- [ ] **端侧唤醒模型本身的隐私攻击面**：对抗样本触发误唤醒、模型提取（model extraction）风险。

## 相关笔记

- [[AI 手机 Always-on 低功耗常驻感知 学习笔记]]（always-on 常驻感知总范式，本篇是其"语音唤醒"垂直切片）
- [[语音交互与端侧 ASR TTS 学习笔记]]（唤醒→ASR→意图→TTS 全链路，本篇聚焦"唤醒"这一最前段）
- [[端侧模型的个性化隐私联邦边界 学习笔记]]（隐私边界的横向方法论，本篇是语音场景的具体化）

## 附：来源清单

- asqvox — Wake word and hotword detection glossary（唤醒词定义、FAR/FRR 权衡、隐私维度）
- hashlytics — How Android's Always-On Microphone Works（协处理器、5–10mW、~1% 日耗电、关闭路径）
- dataintelo — Ultra-Low-Power Voice DSP Market（市场规模与合规驱动）
- All About Circuits — AONDevices AON1120 @ CES 2025（超低功耗传感器融合 IC）
- Google Support — Lights on your speaker（Gemini for Home / Assistant LED 语义、mic off 橙灯）
- 凤凰网 ifeng —《都2025年了，为什么 AI 手机又爱上二十年前的「跑马灯」》（Apple Privacy Indicator 设计哲学）
- clario / bbpmag / androidguias — 麦克风隐私指示灯（iOS 橙点 / Android 绿点机制）
- freedomtech / franklinetech — 语音助手隐私诉讼与误唤醒报道（Siri/Google 和解、Alexa 本地处理移除）

## ⚠️ 待核实清单

- 各项**法律和解金额**（$95M Siri / $68M Google）为媒体口径，需以法院文件/官方公告核实。
- Amazon Alexa "Do Not Send Voice Recordings" 选项**移除日期（2025-03-28）及适用范围**为媒体报道，待核实。
- 小米/小爱、三星/Bixby 的**具体低功耗载体、本地处理边界、隐私指示灯设计**暂无一手来源，全部待核实。
- "5–10 mW / 约 1% 日耗电"为单一来源（hashlytics），待交叉核实。
- 超低功耗语音 DSP "2025 $1.92B → 2034 $4.95B / CAGR 11.2%"为市场研究报告口径，待核实。
- AON1120 "80µW 监听 / 260µW 全处理 / >90% 噪杂命中率"为厂商自报，待实测核实。

#标签/手机AI智能体/端侧语音唤醒隐私
