---
title: AI 模型供应链安全与开源投毒防护 学习笔记
tags: [安全, 模型供应链, 开源投毒, SBOM, 端侧模型]
created: 2026-10-10
source:
  - safeguard.sh（Securing LLM and Model Supply Chains with SBOMs；Hugging Face Model Hub Supply Chain Risks in 2025）
  - opswat.com（The Hidden Security Risks of Pre-Trained AI Models）
  - cisa.gov（2025 Minimum Elements for a Software Bill of Materials，2025-08 公众意见稿）
  - isc.sans.edu / protectai（ModelScan 模型序列化攻击防护）
---

> 心智模型：**加载一个开源模型权重 ≈ 执行一段来源不明的代码**——模型/依赖的"供应链可信"和软件依赖是同一个问题，只是载体从 `.whl` 换成了 `.pt/.safetensors`。

本篇是「广度种子」，点到为止；深度留白给 Ethon。区别于 [[模型水印与内容溯源 学习笔记]]（主动给生成内容打标溯源）与「合成数据/训练数据污染」主题（聚焦训练数据本身被投毒）——**本篇聚焦"从来源到部署的模型文件与依赖的可信与投毒防护"**，即 artifact 本身的完整性与来源验证。

## 一、定义（一句话卡位）

| 概念 | 含义 |
| --- | --- |
| 模型供应链攻击 | 在"获取权重 / 安装依赖 / 转换格式 / 加载部署"任一环节植入恶意代码或后门，使受害者机器在加载模型时执行攻击者指令 |
| 开源模型投毒 | 在公开 Hub（Hugging Face / PyTorch Hub）发布带恶意载荷或后门权重的模型，诱导下载 |
| ML-BOM / AI-BOM | ML 版软件物料清单：基座模型来源·哈希·许可证、训练/RAG 数据溯源、微调记录、扫描与签名证据 |
| 模型签名 | 用 Sigstore/Cosign 思路对权重做签名 + 可验证 provenance，消费者可验来源与完整性 |

## 二、攻击面分类（广度覆盖）

| 攻击面 | 机制 | 典型手法 | 检测难度 |
| --- | --- | --- | --- |
| 依赖投毒 | 恶意 PyPI/npm 包在加载时拉恶意模型或执行代码 | 仿冒名（如 aliyun-ai-labs-sdk）、typosquat | 中——SCA 工具部分覆盖 |
| 模型权重投毒 | pickle 反序列化即执行任意代码 | `reduce` 钩子起 reverse shell、偷 SSH key/环境变量 | 高——需专用扫描器 |
| 训练数据投毒 | 训练/微调数据被污染（见"合成数据/后训练"主题，非本篇重点） | 毒样本、后门触发 | 很高——行为测试才显形 |
| 转换工具链投毒 | 自动 pickle→safetensors 转换服务、量化(GPTQ/AWQ/GGUF)、LoRA 适配器被植入后门 | 量化后门、adapter trojan、转换流水线注入 | 高——需比对/行为测试 |
| 命名空间抢占 | Hub 组织名/模型名仿冒 | `mistraI-ai`（大写 I）、动态拼名解析到恶意库 | 低-中——需来源白名单 |
| Spaces 凭证窃取 | HF Space 借 OAuth 拿访客 token/私库权限 | 提权 OAuth scope | 中——结构性风险 |

## 三、防护层（四道防线）

| 防护层 | 做法 | 工具/标准 |
| --- | --- | --- |
| 来源验证 | 锁定可信仓库、Pin 哈希、组织名核验、来源白名单 | Hugging Face 组织校验、Sigstore Model Signing |
| 签名 | 权重签名 + 可验证 provenance attestation（类 Cosign 容器镜像） | Sigstore Model Transparency、Model Signing |
| 扫描 | 加载前静态/启发式扫恶意代码与反序列化风险 | ModelScan（开源）、PickleScan、Fickling、HF 内置恶意扫描、JFrog Xray |
| SBOM | 记录模型+依赖的来源/版本/哈希/许可证 | CISA 2025 SBOM 最小元素、CycloneDX ML-BOM |

## 四、主流方案与工具

- **SafeTensors**：HF 主推的 data-only 格式，无执行引擎，加载即不触发代码——关掉 pickle RCE 直接路径；但"仅换格式"不能覆盖转换/扫描基础设施本身的可信问题。
- **ModelScan**（Protect AI，Apache-2.0 开源）：逐字节扫 Pickle/Cloudpickle/Dill/Joblib、HDF5、TF SavedModel、Keras v3，输出 CRITICAL/HIGH/MED/LOW 分级，建议接 CI/CD。
- **PickleScan / Fickling**：pickle 专项分析与扫描。
- **Hugging Face 恶意模型扫描**：2024 起对上传模型强制扫描（研究者数周内即演示绕过）。
- **PyPI/npm 审计**：`pip-audit`、SCA 工具；但传统 SCA 多数不进 `.bin` 内部。
- **CISA / NIST 指南**：CISA 2025-08 SBOM 最小元素意见稿新增 Component Hash / License / Tool Name / Generation Context，并专门讨论"SBOM for AI Software Systems"；NIST AI RMF 提供治理框架。

## 五、2025-2026 进展（点到为止）

- 格式迁移：新发布模型默认 safetensors 渐成趋势；长尾社区模型仍多为 pickle-only。HF safetensors 占比（不同来源口径不一，**待核实**）。
- 扫描器自身成靶子：2025-12 JFrog 披露 PickleScan 三个零日（含 CVE-2025-10155，CVSS 9.3），恶意文件用 `.bin/.pt` 扩展名诱使扫描器用错解析逻辑而漏检。
- 攻击工业化："Stacked Pickle"分层+压缩嵌套载荷，PoC 在 VirusTotal 全引擎 0 检出；仿冒大厂 PyPI 包（2025-05 阿里系仿冒包 ~1600 次下载、<24h 下架）。
- 并购：Palo Alto Networks 于 2025-07 完成收购 Protect AI（约 $634.5M），Guardian 并入 Prisma AIRS——企业模型安全扫描走向平台化。

## 六、代表事件与产品

| 事件/产品 | 要点 |
| --- | --- |
| JFrog 2024-03 扫描 HF | 约 100 个含恶意 pickle 载荷的模型文件，reverse shell，约 95% 瞄准 PyTorch |
| star23/baller13（2024-01） | HF 上带 reverse shell 的 PyTorch 模型 |
| 阿里系仿冒 PyPI 包（2025-05） | aliyun-ai-labs-sdk 等，加载时拉恶意模型，~1600 下载 |
| Hugging Face 转换 bot 被攻（HiddenLayer 2024） | 自动 pickle→safetensors 转换流水线本身成为注入点 |
| 产品 | ModelScan（开源）、JFrog Xray/AI Catalog、Prisma AIRS(Guardian)、Sigstore Model Signing、CycloneDX ML-BOM |

## 深度盲区（留白给 Ethon）

- [ ] 端侧 OTA 分发模型时，权重签名 + TEE 解密如何与 [[端侧大模型安全芯片级防护 学习笔记]] 的硬件信任根衔接？飞轮里签名验证落在哪一层？
- [ ] 量化（GPTQ/AWQ/GGUF）后门在端侧小模型上是否更易被利用？有无轻量行为比对手段？
- [ ] LoRA/adapter 投毒在端侧"热插拔"场景下审计责任归谁（模型厂 / 应用 / 用户）？
- [ ] ML-BOM 在 Android 应用商店上架审核里能否成为合规证据（类比 SBOM）？国内有没有对应指南？
- [ ] 模型红队（[[AI 评测红队与对齐 学习笔记]]）是否该把"加载即执行"当成独立攻击面，而非仅评能力/对齐？
- [ ] 长尾社区 pickle-only 模型，PM 视角的"禁止加载"策略在开发者体验与安全的权衡点在哪里？

## 关联（库内已有笔记）

- 模型来源/权重完整性 ≠ 内容溯源：见 [[模型水印与内容溯源 学习笔记]]（主动打标溯源，是输出侧）
- 端侧权重落盘保护：见 [[端侧大模型安全芯片级防护 学习笔记]]（硬件信任根/TEE）
- 红队方法论衔接：见 [[AI 评测红队与对齐 学习笔记]]

## 附：来源清单

- safeguard.sh — Securing LLM and Model Supply Chains with SBOMs；Hugging Face Model Hub Supply Chain Risks in 2025
- opswat.com — The Hidden Security Risks of Pre-Trained AI Models
- cisa.gov — 2025 Minimum Elements for a Software Bill of Materials（2025-08 公众意见稿）
- isc.sans.edu / protectai GitHub — ModelScan 模型序列化攻击防护
- 交叉印证：JFrog 2024-03 ~100 恶意模型、CVE-2025-10155（safeguard.sh）；阿里系 PyPI 仿冒（opswat）

## ⚠️ 待核实清单

- Hugging Face 上 safetensors vs pickle 的精确占比（2026 口径各源不一）→ 媒体估算，需一手数据。
- "约 95% 瞄准 PyTorch""~100 个恶意模型"为 JFrog 2024-03 研究引用，具体样本量与时间以 JFrog 原始公告为准。
- CVE-2025-10155 的 CVSS 9.3 与 PickleScan 三零日细节，以 NVD/CISA 公告原文为准。
- Protect AI 收购金额 $634.5M 为媒体披露，以 Palo Alto Networks 官方 filing 为准。
- 「训练数据投毒」「合成数据污染」属相邻主题，本篇未展开，深度待补。

#标签/安全/模型供应链
