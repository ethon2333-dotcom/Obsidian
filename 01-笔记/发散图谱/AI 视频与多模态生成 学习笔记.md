---
title: "AI 视频与多模态生成 学习笔记"
tags: [广度种子, AIGC, 视频生成, 多模态生成, 热点]
created: 2026-09-02
source: "WebSearch/WebFetch 核实（见文末来源清单）"
---

# 一句话心智模型

**2025–2026 多模态生成已从「能生成」跨入「声画一体 + 世界模拟」阶段；核心矛盾是 质量 / 时长 / 一致性 / 成本 四维仍未同时达标，且算力与版权约束把「生成」牢牢锁在云端。**

> 与 [[端侧多模态 VLM 学习笔记]]（端侧*视觉理解*，非生成）区分；与 [[世界模型与仿真合成环境 学习笔记]]（世界模型上游技术）同源但本篇聚焦 AIGC 产品格局与技术范式。

---

## 1. 广度覆盖：产品 / 模型格局

| 产品 / 模型 | 出品方 | 模态 | 关键能力 / 版本 | 进展状态 |
|---|---|---|---|---|
| Sora 2 | OpenAI | 视频 + 音频 | DiT + 时空块；原生音视频同步、Cameo 自插入、物理一致性；2025-09-30 发布 + Sora iOS 社交 App | 已上线（美加以邀请制）；ChatGPT Pro 可用 Sora 2 Pro |
| Veo 3 / 3.1 | Google DeepMind | 视频 + 音频 | 原生音频（对白/音效/环境）、4K、长时长叙事；3.1 于 2025-10-15 发布（多帧/编辑增强） | 已上线 Gemini / Flow / Vertex AI；SynthID 水印 |
| 可灵 Kling 2.0 / 3.0 | 快手 | 视频 + 图像 | DiT、MVL 多模态视觉语言、多模态编辑；3.0 系列主打音画同步与跨任务融合 | 已上线，全球用户 2200 万+；API 开放（3.0 细节待核实） |
| Runway Gen-4 / 4.5 | Runway | 视频 | 「世界一致性」跨镜头角色/物体一致、GVFX；4.5 于 2025-12 发布（约 10s / 4K 导出） | 已上线；2026-02 E 轮 3.15 亿美元（英伟达/AMD/Adobe 参投） |
| Pika 2.2 | Pika Labs | 视频 | 最长 10s / 1080p，Pikaframes 关键帧过渡、Pikaswaps/Pikadditions 局部编辑 | 已上线，社交 App 内测 |
| Midjourney V7 | Midjourney | 图像（及早期视频） | 2025-04 发布、6 月默认；Omni Reference、Draft Mode | 已上线；艺术/风格化领先 |
| FLUX / FLUX 2 | Black Forest Labs | 图像 | 1.1 Pro 基于 Flow Matching，约 4.5s/图、文本渲染强；2 代 32B 参数、开源权重可本地跑 | 已上线；2 代 2025-11 发布 |
| Suno v4.5 / 4.5+ | Suno | 音频（音乐） | 音质/人声提升，歌曲延至 8 分钟，风格混搭；4.5+ 加「添加人声/乐器」混合创作 | 已上线（付费） |
| Stable Diffusion 系 / WAN | Stability AI / 阿里 | 视频 / 图像 | 开源可本地部署；WAN 为阿里开源视频模型 | 开源生态 |
| Luma Ray / Dream Machine | Luma AI | 视频 | 世界模型方向、Ray2 逻辑事件序列 | 已上线 |
| Seaweed | 字节跳动 | 视频 | 低调上线视频生成模型 | 待核实（参数/开放范围） |

> 表中时长/分辨率上限多为**厂商口径或媒体估算**，标「待核实」者见文末清单。

---

## 2. 技术范式分类

- **扩散模型 + 时空一致性（主流）**：DiT 替代 U-Net，时空块（spacetime patches）联合建模空间(x-y)+时间(t)。Sora 系列、可灵、Veo、Runway、FLUX 均属此系。核心难点 = 运动连贯 / 光影一致 / 物体恒存（object permanence）。
- **自回归 / 因果生成**：逐帧或逐 token 因果预测，配扩散蒸馏（few-step）。代表 MAGI-1、CausVid、Self-Forcing（去曝光偏差、半实时）。利于长视频、流式、可控生成。
- **世界模型驱动**：把视频生成当「世界模拟器」，注入几何 / 3D / 物理先验（深度、姿态、轨迹、ControlNet 式条件），从「逐帧拟合」转向「物理一致的空间智能」。Sora 2 明确定位为世界模拟器；NVIDIA Cosmos 做数字孪生。与 [[世界模型与仿真合成环境 学习笔记]] 同源上游。

---

## 3. 2025–2026 重大进展（要点）

- **声画一体成标配**：Veo 3（2025-05）、Sora 2（2025-09）实现原生音频同步，终结「无声短片」时代。
- **世界一致性 / 物理一致性跃升**：Runway Gen-4（2025-04）「世界一致性」、Sora 2 物理反弹模拟、可灵 MVL 多模态编辑。
- **时长与分辨率推进**：由 5–10s/1080p 向 4K、分钟级演进（厂商口径，待核实上限）。
- **社交化 / 产品化**：Sora App（Cameo 自插入 + remix）、Pika 社交 App，AIGC 向「生成式社交平台」演化。
- **玩家融资与联盟**：Runway E 轮 3.15 亿美元（英伟达/AMD/Adobe）；Google 与 Netflix 自然语言搜索合作；可灵定位「视频创作新基础设施」。

---

## 4. 玩家格局

- **美国前沿实验室**：OpenAI（Sora）、Google（Veo）、Runway、Luma、Black Forest Labs（FLUX）、Suno（音乐）。
- **中国厂商**：快手（可灵）、字节（Seaweed，待核实）、阿里（WAN 开源）。
- **开源阵营**：Stable Diffusion 系、FLUX dev/open、WAN、NVIDIA Cosmos。
- **平台入口**：Gemini / Flow / Vertex AI、ChatGPT / sora.com、可灵 Web/API、Runway Web/API、Midjourney Discord/Web。

---

## 5. 与端侧生成的差距（留白）

- 当前 SOTA 视频/图像生成均需云端大算力（GPU 集群、高显存）；端侧仅能跑小图 / 低分辨率或量化蒸馏版。
- 与 [[端侧多模态 VLM 学习笔记]] 区分：端侧 VLM 是「视觉**理解**」（感知/识别/推理），本主题是「**生成**」（从噪声到像素/声）；生成对算力 / 显存 / 能耗要求更高，端侧落地更难。
- **端侧扩散模型（小模型 + 量化 + 蒸馏）仍处早期** —— 可行性 / 画质 / 时长待补，见文末待解问题。
- 对安卓 OS PM 的含义：端侧生成若成熟，将把「内容创作入口」下沉到设备本地，与 [[AI 眼镜与可穿戴意图入口 学习笔记]] 的本地超低延迟创作可能耦合。

---

## 6. 版权与合规争议

- **深度伪造 / 虚假信息**：Veo 3 上线即出现伪造新闻片段病毒传播，引发 misinformation 担忧；各厂加水印（Google SynthID、OpenAI C2PA + 可见动态水印）。
- **肖像 / 声音权**：Sora 2 Cameo 引入「本人同意 + 可随时撤销」机制；likeness 滥用风险待监管。
- **训练数据版权**：Suno 等音乐生成面临唱片公司诉讼（进展待核实）；训练集来源不透明（Runway 拒透露）。
- **监管推进**：C2PA 溯源、平台分级（青少年限制）、SynthID 行业标准落地中。与 [[端侧模型安全与越狱 学习笔记]] 的「本地生成治理」议题呼应。

---

## 7. 待解问题（留给 Ethon 补充）

- [ ] 端侧视频生成当前可行性？（小模型 / 量化 / 蒸馏能否跑 1–3s / 720p？能耗与 NPU 约束？）
- [ ] 多模态生成对 OS 厂商「内容入口 / 创作入口」的重分配影响？安卓如何接住本地生成？
- [ ] 世界模型范式与 [[世界模型与仿真合成环境 学习笔记]] 的边界：视频生成是「弱世界模型」还是通往通用世界模型的必经路径？
- [ ] 生成式社交平台（Sora App / Pika）会否侵蚀短视频平台（TikTok / 抖音）用户时长？
- [ ] 端侧生成成熟后，版权 / 水印 / 深度伪造在设备本地如何治理？

---

## 附：来源清单

1. OpenAI Sora 2 发布（2025-09-30）：https://openai.com/index/sora-2/
2. Google Veo 3 / 3 Fast on Vertex AI：https://blog.google/intl/zh-tw/products/cloud/veo-3-and--veo-3-fast-on-vertex-ai/
3. 快手 IR 可灵 2.0 发布（2025-04-15）：https://ir.kuaishou.com/zh-hans/news-releases/news-release-details/kling-ai-advances-20-era-empowering-everyone-tell-great-stories
4. Runway 更新日志（Gen-4 / Aleph / GWM）：https://runwayml.com/ja/changelog
5. Runway Gen-4 百科（含 Gen-4.5 / GWM-1 / 融资）：https://baike.baidu.com/item/Runway%20Gen-4/65550597
6. Pika 2.2 功能概览：https://pika-art.net/ ；https://pikalabs.net/?p=206
7. Midjourney V7 vs FLUX 2 对比（2025）：https://aiphotolabs.com/compare/midjourney-v7-vs-flux-2-ai-image-generator-comparison-2025
8. Suno v4.5 发布：https://aibinger.com/ai-news/ai-tools-news/suno-ai-launches-version-4-5-with-smarter-prompts-and-better-music-creation ；https://sunnoai.com/v4.5
9. 视频生成技术范式综述（arXiv 2511.08585）：https://arxiv.org/html/2511.08585v1
10. 大模型视频生成核心技术（腾讯云）：https://cloud.tencent.com.cn/developer/techpedia/2528/19861
11. 2025 影视工业与「世界模拟器」转向：https://www.zgwypl.com/content/details78_447241.html
12. 视频生成格局（含 2026 版本前瞻，部分待核实）：https://www.swisscom.ch/de/about/nachhaltigkeit/swisscom-campus/generative-video-ki.html

---

## ⚠️ 待核实清单

- 可灵 3.0 音频同步 / 时长细节：官网确认 3.0 系列存在，但具体指标待核实。
- 各模型「最长时长 / 最高分辨率」上限多为厂商口径或媒体估算（如 Veo 3「最长约 10 分钟」、Runway 4K 导出），统一标待核实。
- 字节 Seaweed 具体参数与开放范围（待核实）。
- Suno 音乐版权诉讼具体进展（待核实）。
- Luma Ray3 / Pika 2.5 / Midjourney Video V1 / WAN 2.6 等 2026 迭代版本细节（部分来源为 2026 前瞻，待核实）。

---

#标签/广度种子/AIGC #标签/发散图谱/多模态生成
