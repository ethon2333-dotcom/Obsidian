---
title: 合成媒体检测与 deepfake 防御 学习笔记
tags:
  - deepfake
  - media-forensics
  - synthetic-media
  - AI安全
  - 被动检测
  - 内容取证
created: 2026-10-06
source: "WebSearch/WebFetch 核实 + 公开资料（2025-2026）"
---

> **心智模型**：合成媒体检测的本质是"识别假"——在生成模型不断进化的攻防对抗中，用**被动取证信号**（生物信号 / 频域痕迹 / 跨模态不一致）给内容打"可疑度"，而不是像 [[模型水印与内容溯源 学习笔记]] 那样主动打标溯源。检测的"绝对真相"不存在，只有"当前样本在当前检测器下的可疑分"。

> 本篇刻意区别于库内 [[模型水印与内容溯源 学习笔记]]（主动水印 / C2PA provenance 技术）与 [[AI 视频与多模态生成 学习笔记]]（生成侧广度）：本文侧重**被动检测、取证与防御侧**。

## 一、广度覆盖（BREADTH > DEPTH）

| 维度 | 定义 / 分类 | 主流方案（被动检测） | 2025-2026 进展 | 代表产品（厂商 / 工具） |
|---|---|---|---|---|
| **总体定义** | 合成媒体 = AI 生成/篡改的图/视频/音频；deepfake 特指把真人"换脸/换声/换言行"。检测 = 不依赖生成端配合、从内容本身找伪造痕迹 | 被动取证（passive forensics） vs 主动溯源（C2PA/水印，见 [[模型水印与内容溯源 学习笔记]]） | Europol 预测 2026 年高达 90% 在线内容含 AI 生成成分（待核实，来源为行业预测口径） | — |
| **视觉/空域痕迹** | 皮肤蜡质化、发际/颈部边缘模糊闪烁、光照/阴影几何不一致、眼部反射异常 | CNN / ViT 分类器、频域（spectral）分析抓 GAN 频谱尖峰、patch-based 局部特征 | 扩散模型（Diffusion）留下的频谱指纹比 GAN 更弱，检测更难；压缩/重编码会抹掉痕迹 | DeepFake-O-Meter（UB 开源聚合，集成 18+ 模型）、DeepSafe、微软 Video Authenticator |
| **生物信号取证** | 活体才有的生理信号：血流动引起的面部像素色变（rPPG/PPG）、呼吸节奏、微表情、瞳孔/眨眼节律 | 远程光体积描记（rPPG）检测"血液流动信号"是否存在；屏幕回放/面具/合成视频该信号缺失 | Intel FakeCatcher 用 PPG，厂商自报 ~96% 准确率、可并发 72 路实时流；被认为比纯 NN 分类更难被对抗训练绕过（厂商口径，待核实） | Intel FakeCatcher、微软 Video Authenticator |
| **音频与跨模态** | 音频伪造痕迹：金属感、呼吸/停顿不自然、频带能量异常、神经编解码器压缩伪影；跨模态：口型-语音不同步、音画情绪错位 | 说话人嵌入比对、呼吸/停顿模式、环境声学校验、唇形-音素（phoneme-viseme）一致性、多分支网络投票 | 人耳辨别克隆声仅略高于随机；Pindrop 在呼叫路径实时打分，厂商自报语音深伪检出率高（具体数字待核实，多来自厂商案例） | Pindrop（Pulse/Liveness，银行场景）、Resemble AI |
| **行为生物特征** | 不只"你是谁"，而是"你如何交互"：打字节奏、鼠标轨迹、导航习惯 | 连续认证（continuous authentication），session 内抓异常 | 英国政府 2026 年市场分析将行为信号列为对抗生物 spoof 的关键补充；多用于金融/企业 | 各 IAM / 反欺诈厂商（行为分析模块） |
| **攻防对抗 / 鲁棒性** | 检测器自身是攻击面：生成端可专门训练以**绕过检测**（adversarial evasion）；新生成方法让旧检测器失效（泛化鸿沟） | 对抗训练、持续周级重训练（crowdsourced 威胁情报）、多模态集成（降假阴性 ~63% 厂商口径待核实） | **泛化鸿沟是核心痛点**：Deepfake-Eval-2024（88 网站/52 语言真实深伪）上开源 SOTA 检测器 AUC 跌 ~50%（视频）/48%（音频）/45%（图像）；IEEE 2025 口径：已知方法 85-95% → 未见方法 60-75% | Reality Defender（周级更新模型，2026 接入 Zoom 实时告警）、NVIDIA Synthetic Video Detector（SIGGRAPH 2026，NIM 微服务，厂商自报 92% 未压缩/82% 50% 压缩，定位为"编辑部分流信号"而非定论） |
| **监管 / 法规** | 披露/标注义务是"治理假"的另一条腿（区别于技术检测） | 显式+隐式标识、机器可读标记、平台核验 | **中国**：《人工智能生成合成内容标识办法》+ GB 45438-2025，2025-09-01 生效（显式+隐式标识、传播平台核验）；**EU**：AI Act 第 50 条透明度义务，2026-06 发布《AI 生成内容透明度行为准则》；**美国**：>20 州专项立法（选举广告/亲密影像）；**印度**：2025 IT 修订草案（标签覆盖≥10% 画面/音频前 10%）；**英国**：Online Safety Act 2023（NCII）；**NIST SP 800-63-4**（2025-07）纳入注入攻击与伪造媒体控制 | 详见 [[AI 监管与合规落地 学习笔记]] |
| **平台治理实践** | 平台侧：要求创作者声明 + 自动检测 + 显著标签 + 不合规失免责保护 | "Made with AI" 标签、政治广告披露、社区注记（Community Notes）、可信度降权 | Meta/YouTube/TikTok 已对 AI 生成内容加标签；X 用 Community Notes；Reality Defender 2026 接入 Zoom 会议实时告警；印度草案要求 SSMI（>500 万用户）前端核验 | Meta、Google/YouTube、TikTok、X、Reality Defender |

## 二、深度盲区（待 Ethon 补充）

- [ ] **防御组合拳的"最佳实践栈"是什么？** 检测 / 溯源 / 带外流程核验（callback、预设口令、多人审批）三者如何按渠道（KYC、呼叫中心、高管通讯）分层？[[AI 监管与合规落地 学习笔记]] 里有无对应落地模板？
- [ ] **对抗鲁棒性的量化基线**——除了 Deepfake-Eval-2024，还有哪些权威、可复现的"in-the-wild"基准？各检测器在"未见生成方法"下的真实 AUC 是多少（非厂商自报）？
- [ ] **端侧/实时检测的可靠边界**：FakeCatcher 的 PPG 在暗光、戴面具、超实时注入流下是否仍稳？on-device 检测的功耗与误报成本谁在埋单？
- [ ] **生成侧与检测侧的"军备竞赛"节奏**：Sora 2 / Veo 3.1 / Runway Gen-4.5 等新生成器出现后，检测器的"滞后窗口"通常多长？[[AI 视频与多模态生成 学习笔记]] 里生成侧演进能否对齐时间线？
- [ ] **法律可执行性缺口**：标注法规（如中国显式+隐式标识、EU 第 50 条）如何惩戒"剥离元数据/截图重发"的规避行为？平台失免责（safe harbour）的触发边界在哪？
- [ ] **误报的代价**：高敏感场景（司法证据、政治辟谣）下，检测器"假阳性"带来的声誉/法律风险，是否有标准化的"人工复核 + 可解释输出"流程？

## 三、连入库内笔记

- 互补（检测 vs 主动溯源）：[[模型水印与内容溯源 学习笔记]]
- 监管框架延伸：[[AI 监管与合规落地 学习笔记]]
- 生成侧威胁来源：[[AI 视频与多模态生成 学习笔记]]

## 四、附：来源清单

1. aiwiki.ai — Deepfake 词条（检测分类、NVIDIA Synthetic Video Detector、DaaS）
2. stingrai.io — Deepfake Statistics 2026（5 类在用检测法、Deepfake-Eval-2024 泛化鸿沟、NIST SP 800-63-4、C2PA v2.3）
3. detectdeepfakes.com — Detecting Video Deepfakes in 2026（空间/声学/跨模态痕迹、supervised 检测 shortcut learning 缺陷）
4. adaptivesecurity.com — AI Deepfake Fraud / Deepfakes（rPPG、行为生物特征、分类器 10-20pp 真实跌）
5. stateofsurveillance.org — Synthetic Media Detection 2026（商业工具、实时检测、C2PA 局限）
6. ddg.fr / ima.qq.com / 81.cn / aiunderstanding.org — 中欧 deepfake 标注法规（中国 2025-09-01 办法、EU AI Act 第 50 条、2026 行为准则）
7. 24aiglobal.com — 61 国 DPA 联合警示 deepfakes（GDPR 第 9 条生物特征、EU AI Act 罚款上限）
8. marketintelo.com — Deepfake Detection Market 2025-2034（Microsoft/FakeCatcher/Pindrop/Sensity/Reality Defender/Truepic 格局，含厂商口径数字）
9. aivideodetector.org / startbrain.io / uplatz.com — 检测工具对比、企业策略、开源生态（DeepFake-O-Meter、DeepSafe、DFDC）
10. dqindia.com / economictimes.indiatimes.com — 印度 2025 IT 修订草案（标签覆盖面积要求）
11. channelnewsasia.com / zaobao.com.sg — Meta/Google/TikTok/X 平台标注实践（GE2025 背景）
12. researchconnect.suny.edu / dartcollective.net / sourceforge.net — DeepFake-O-Meter（UB 开源，NIST 资助，集成 18+ 检测器）

## 五、⚠️ 待核实清单

- 各厂商自报准确率（FakeCatcher 96%、Sensity 95-98%、Pindrop 高检出率、NVIDIA 92%/82%）均为**厂商口径或自家基准**，真实 in-the-wild 表现需独立复现，勿当客观事实引用。
- "Europol 预测 2026 年 90% 在线内容含 AI 生成"为行业预测口径，待核实原始出处。
- "多模态集成降假阴性 63%"、"检测市场 2024 融资 4.2 亿美元 / Top5 占 54%"来自 marketintelo 行业报告，数字待交叉验证。
- 印度 2025 IT 修订规则为**草案（draft amendment）**，尚未最终立法，引用时注明"拟议"。
- 各法规生效时间（中国 2025-09-01、EU 行为准则 2026-06、NIST SP 800-63-4 2025-07）据公开报道，落地细则以官方文本为准。
- "开源 vs 商业工具性能差"结论多来自供应商对比评测，存在利益偏向，待独立研究佐证。

#标签/合成媒体检测 #标签/deepfake防御 #标签/AI安全
