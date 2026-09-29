---
title: AI 音乐与音频生成 学习笔记
tags:
  - 发散图谱
  - AIGC
  - 音乐生成
  - 音频生成
  - 多模态
  - 端侧AI
created: 2026-09-20
source:
  - WebSearch/WebFetch 核实 2025-2026（Suno/Udio 诉讼与和解、ElevenLabs Music、TinyMusician arXiv:2509.00914、AudioCraft/Demucs 等）
  - 见文末「附：来源清单」
---

# 一句话心智模型
继文本 / 图像 / 视频被生成式 AI 攻破后，"声音与音乐"成为新 frontier——从文生音乐到音频修复 / 分离 / 配音，正在重塑内容生产与端侧交互的「声音层」。

> 与 [[AI 视频与多模态生成 学习笔记]]（视觉 / 视频生成）同源不同域；与 [[数字人与虚拟人 学习笔记]]（TTS / 语音克隆 / 口型驱动，偏说话人语音）互补——本篇聚焦**音乐与通用音频**而非说话人语音。

---

## 一、任务分类（广度覆盖，点到为止）

| 任务 | 定义 | 代表技术 / 产品 |
| --- | --- | --- |
| 文生音乐（Text-to-Music） | 自然语言 → 器乐 / 带人声的完整曲 | Suno、Udio、Stable Audio、MusicGen、Eleven Music |
| 文生歌 / 人声（Song+Vocal） | 含歌词、演唱、结构的整歌生成 | Suno v5.5/v6、Udio、Eleven Music、Riffusion |
| 音频扩散 / 修复 | 扩散模型补缺损、降噪、补帧 | AudioGen、Stable Audio（latent diffusion）、AudioSR |
| 音源分离（Separation） | 混音 → 人声 / 鼓 / 贝斯 / 伴奏 | Demucs（Meta）、UVR、Spleeter、Eleven Stems |
| AI 配音 / 拟声（TTS/Voice） | 文本 / 参考音 → 拟真语音 | ElevenLabs、Resemble、见 [[数字人与虚拟人 学习笔记]] |
| 环境音 / SFX 生成 | 氛围床、拟音、游戏音效 | AudioGen、Eleven SFX、Stable Audio Open |

---

## 二、主流模型与产品格局（定位 + 版权口径）

| 产品 / 模型 | 定位 | 是否可商用 / 版权争议 |
| --- | --- | --- |
| **Suno** | 消费级整歌生成龙头，移动优先（iOS/Android/CarPlay/Android Auto/iMessage） | 付费层可商用下载；2024 被 RIAA 诉训练侵权，2025 起转向授权模型 |
| **Udio** | 高保真整歌生成，音质口碑略优 | 与 UMG/WMG 和解转「walled garden」；Sony 仍在诉 |
| **ElevenLabs Music** | 与 TTS/配音同生态的「合规优先」音乐模型 | 与 Kobalt/Merlin 等授权，付费可商用（影视/播客/社媒/广告/游戏）；最防御性 |
| **Stable Audio Open** | Stability AI 开源权重的 latent diffusion | 训练于 CC 音频，开放权重；非商业/自部署为主 |
| **MusicGen / AudioCraft（Meta）** | 开源研究框架（MusicGen+AudioGen+EnCodec） | MIT 代码 + CC-BY-NC 权重（非商业）；MusicGen Mini ~300M 可端侧 |
| **Riffusion** | 频谱扩散做短循环 / 吉他向音乐 | 早期玩家，当前归属与商用口径 **待核实** |
| **Google MusicLM / Chirp / Lyria** | 谷歌音乐生成研究线 | 多停留研究/实验（MusicFX）；是否规模化商用 **待核实** |
| **Demucs（Meta）** | 音源分离 SOTA（Hybrid Transformer，~9.0 SDR） | MIT，开源可商用 |
| **Adobe Project Music GenAI** | Firefly 系音频生成（文本→音乐 + stem 控制） | 研究/内测为主，是否正式 GA **待核实** |
| **Boomy** | 一键生成可发布 royalty-free 曲库 | 平台化分发，授权模式较清晰 |
| **Resemble / 语音拟声** | 语音克隆 + 情感控制 | 偏说话人语音，见 [[数字人与虚拟人 学习笔记]] |

---

## 三、2025-2026 关键进展

- **版权诉讼与平台政策（最大变量）**：RIAA（UMG/Sony/Warner）2024-06 起诉 Suno、Udio 未经授权训练。2025-10 UMG 与 Udio 和解；2025-11 Warner 先后与 Udio、Suno 和解并转授权合作（Suno 退役未授权模型、2026 推授权模型，免费层仅播放/分享、下载需付费）。**Sony 截至 2026 仍两案在诉**。2026-06 NMPA 与 Udio 达成「行业首份全行业授权」（词曲/录音 50/50 分账）。2026-07 慕尼黑法院（GEMA v. Suno）判 AI 训练侵权 **待核实细节**。
- **授权化成为主流路径**：Suno v6（2026-09）宣称仅基于 Warner/BMG/Believe 授权曲库训练；ElevenLabs 自始走授权路线。结论趋势：**「先侵权后和解」→「先授权后生成」**。
- **实时 / 交互生成**：Suno 进 iMessage（2026-07 文本/语音即时成歌）、CarPlay/Android Auto（2026-05）；ElevenMusic iOS App（2026-04）；YouTube/社媒「把消息变歌」玩法扩散。生成延迟已压到秒级（云端）。
- **端侧轻量化（与 OS PM 强相关）**：**TinyMusician**（arXiv:2509.00914，2025-08）从 MusicGen 蒸馏 + 混合精度量化，体积 -55%、保留 93% 性能、~1.04GB，**首个可移动端离线部署的音乐生成模型**；但测试硬件上推理 ~26s，仍受端侧 kernel 优化制约 **待核实落地时延**。

---

## 四、与端侧 / 可穿戴 / 陪伴的潜在结合（发散钩子）

- 端侧 TinyMusician 让**离线氛围音乐 / 情绪 BGM** 成为可穿戴（眼镜、手表）的低功耗本地能力，呼应 [[AI 眼镜与可穿戴意图入口 学习笔记]] 的功耗约束。
- 陪伴 Agent（[[AI 陪伴与情感陪伴 Agent 学习笔记]]）可调用「动态配乐」：音乐随对话情绪/场景实时生成，而非播放固定歌单——声音层即情感反馈层。
- TTS + 音乐生成同栈（ElevenLabs 生态）预示「会说话 + 会唱 + 会配乐」的一体化声音引擎，与 [[端侧语音大模型 学习笔记]] 的端到端语音对话形成上下层互补（注：该笔记库内文件暂未建，仅 MOC 引用）。

---

## 深度留白（BREADTH > DEPTH，留给 Ethon）

- [ ] 端侧音乐生成的**功耗预算**到底多少 mW·s/曲？能否进 Always-on 可穿戴？
- [ ] 「授权曲库训练」模式下，小厂/开源社区的合规出路是什么？CC 数据是否够用？
- [ ] 实时生成（<1s）在端侧 NPU 上是否可行？INT4/1bit 对 FAD/CLAP 分数的掉点实测？
- [ ] AI 生成音乐若要标 AIGC 水印，音频水印（vs 图像 C2PA）标准与安卓系统级支持进度？
- [ ] 陪伴场景里「动态配乐」会不会加剧情感依赖？未成年人保护边界？
- [ ] 厂商口径里的「可商用」具体条款（地域/平台/收入上限）细读差异？

---

# 标签/发散图谱 #标签/AIGC #标签/音乐生成 #标签/音频生成 #标签/多模态

---

## 附：来源清单
1. RIAA v. Suno/Udio 诉讼与和解追踪 — legalclarity.org / musicbusinessworldwide.com（2024-06 起诉；2025-10~11 和解）
2. Suno 官方 App 页（sunnoai.com/app）— 2026 移动功能、v5.5、CarPlay/Android Auto、iMessage（2026-07-15）、100M+ 用户
3. ElevenLabs 官网与 Eleven Music 2026 指南 — v1(2025-08)、Music v2(2026-05/06)、iOS App(2026-04)、授权商用口径
4. TinyMusician: On-Device Music Generation — arXiv:2509.00914（2025-08-31），蒸馏自 MusicGen
5. Meta AudioCraft / MusicGen / Demucs — github facebookresearch/audiocraft、demucs（MIT，CC-BY-NC 权重）
6. Stable Audio Open — Stability AI（2024-07，latent diffusion，开放权重）
7. NMPA × Udio 行业授权（2026-06）、GEMA v. Suno 慕尼黑判决（2026-07，细节待核实）

## ⚠️ 待核实清单
- Suno「$5.4B 估值 / 2M 付费订阅」等经营数字（单一来源，未交叉验证）
- Google MusicLM / Chirp / Lyria 当前是否规模化商用（多停留研究/实验）
- Riffusion 当前归属、商用口径
- Adobe Project Music GenAI 是否正式 GA
- GEMA v. Suno 慕尼黑判决具体法条与适用范围
- TinyMusician 端侧真实时延（依赖硬件与量化 kernel 优化）
- 各产品「可商用」条款的地域/收入上限细差
