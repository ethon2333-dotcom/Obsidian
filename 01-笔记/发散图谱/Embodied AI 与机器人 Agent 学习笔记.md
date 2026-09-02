---
title: Embodied AI 与机器人 Agent 学习笔记
tags:
  - embodied-ai
  - robot-agent
  - vla
  - 具身智能
  - 世界模型
  - 广度种子
  - 发散图谱
created: 2026-08-19
updated: 2026-09-01
source: WebSearch/WebFetch 联网核实（首轮 2026-08-19；第二轮广度扩写 2026-09-01）· 多数数字为媒体/聚合站二手口径，见文末「附：来源清单」与「⚠️ 待核实清单」
---

# Embodied AI 与机器人 Agent 学习笔记

> **心智模型**：**具身智能 = 给大模型一个身体，让它在真实世界里跑「感知 → 决策 → 执行」的闭环**，而不只是在屏幕上生成文字。
> 而**机器人 Agent 范式的本质变化，是把这个闭环从「人手写的模块流水线」压成「一个端到端模型」**——VLA 把「看见什么、听懂什么、做什么动作」塞进同一个模型的同一次前向传播里。
>
> **对 Android OS PM 的意义**：这和手机端侧意图框架是**同一个问题的两种身体**。手机 Agent 的闭环是「屏幕像素/无障碍树 → 意图路由 → 调 App Intent」，机器人 Agent 的闭环是「摄像头 → VLA → 关节角度」。**换掉执行端（Action Space），中间那层意图/规划架构几乎可以照抄。** 机器人这边因为动作不可撤销、延迟约束更硬，很多问题被逼着先给答案——是手机侧的**先行实验场**。

关联锚点：[[发散图谱 MOC]] · [[AI 眼镜与可穿戴意图入口 学习笔记]] · [[智能座舱与车机 HMI 意图入口 学习笔记]] · [[端侧 AI 基建与算力预算]] · [[跨端与多设备意图流转]] · [[无障碍 Accessibility 与 GUI Agent 同源技术栈 学习笔记]]

---

## 一、定义与边界

| 维度 | 说明 |
|---|---|
| **Embodied AI 是什么** | 具备物理/虚拟身体、能感知环境、自主决策并施加动作以改变世界的智能体；核心是「具身闭环」而非纯推理。 |
| **vs 纯软件 Agent** | 纯软件 Agent 在信息空间行动（调 API、改文件）；具身 Agent 在物理空间行动（抓取、移动），受动力学与因果约束。 |
| **vs GUI Agent** | GUI Agent 操作屏幕像素与控件（见 [[工业级 GUI Agent 架构（VLM+无障碍树）]]）；具身 Agent 操作真实物体，模态从像素扩展到力/触觉/深度。 |
| **vs 自动驾驶** | 自动驾驶是「具身智能的单任务特例」——只有轮式移动+感知，无通用操作；具身 AI 强调跨任务、跨本体的通用策略。 |
| **形态谱系** | 人形（Figure/Optimus/Unitree G1）· 轮式（Agility Digit/配送）· 机械臂（Franka/协作臂）· 移动操作复合本体 · 四足/特种。 |

---

## 二、范式对比表：机器人怎么「决定下一步动作」

| 范式 | 核心思路 | 动作从哪来 | 代表工作 | 泛化能力 | 短板 |
|---|---|---|---|---|---|
| **传统运动规划（经典机器人学）** | 分模块流水线：感知 → 建图 → 规划 → 控制，每段人工设计 | 搜索/优化算轨迹（RRT、MPC、逆运动学） | 工业机械臂、AGV、波士顿动力早期液压控制 | 极低：换任务=重写代码 | 每任务工程量巨大，开放环境失效 |
| **模仿学习 / 视觉运动策略** | 端到端学「看到这个画面 → 做这个动作」 | 神经网络回归动作，常用 Diffusion Policy | Diffusion Policy、ALOHA 系列 | 中：同任务同场景强，换场景弱 | 无语言接口，不理解「为什么」 |
| **VLA（Vision-Language-Action）** | 拿预训练 VLM 当底座，**把「动作」当成一种新的输出模态** | 直接吐动作 token / 连续轨迹 | RT-2、OpenVLA、π0、Gemini Robotics 1.5、GR00T | 高：继承互联网级语义常识，可听自然语言 | 数据饥渴；控制频率与模型大小打架 |
| **机器人基础模型（Generalist Policy）** | VLA 的**工程化形态**：一个 checkpoint 跨多机身/多任务复用，下游少量样本微调 | 同上，重点在「预训练 + 跨机身」 | Open X-Embodiment / RT-2-X、Octo、π0.5/0.6、GR00T N 系列 | 高，且**跨机身（cross-embodiment）** | 「机器人的 ImageNet」尚未真正建成 |
| **世界模型驱动（World Model / sim-to-real）** | 先学一个「会预测未来」的世界模型，在里面想象/训练，再迁到真机 | 模型内部 rollout 后择优；或与动作联合预测 | NVIDIA Cosmos、DreamZero/DreamDojo、Genie 3、V-JEPA 2、GigaBrain-0 | 潜在最高（数据可无限生成） | sim-to-real gap；物理准确性难验证 |
| **World Action Model（2026 新苗头）** | **VLA 与世界模型合流**：一次前向同时预测「下一帧世界」和「下一步动作」 | 联合预测 | NVIDIA DreamZero / GR00T N2（预览）、RynnVLA-002 | 宣称显著优于纯 VLA（**待核实**） | 刚出现，无独立复现 |

**关键判断（广度层）**：2023–2024 的主线是「**把 VLM 改造成 VLA**」；2025–2026 的主线是「**给 VLA 配一个世界模型当数据引擎和想象力**」。两条线在 2026 年开始并成一条（World Action Model）。这与手机侧「大模型做意图理解」→「大模型 + 环境模拟器做多步任务预演」的演进方向同构。

---

## 三、技术栈（感知 → 动作）

| 层级 | 关键点 | 代表 |
|---|---|---|
| **Perception 多模态感知** | 视觉+深度+触觉+力觉+IMU，融合成世界状态表征 | 立体视觉、3D LiDAR、指尖力/触觉传感器、RGB-D |
| **具身推理层（新分层）** | 不出动作，只出空间理解与成功判定：读仪表、定位可抓取部位、判断上一步成没成 | Gemini Robotics-ER 1.5/1.6 |
| **VLA 模型** | 把视觉/语言指令直接映射为连续动作，2025 起成主流范式 | Gemini Robotics、GR00T、Helix、π 系列、OpenVLA |
| **World Model / 仿真** | 用视频/物理引擎预测未来状态，生成训练数据、降低真机依赖 | Isaac Sim、Cosmos、Genie 3、V-JEPA 2、RynnVLA-002、UniVLA |
| **Sim-to-Real** | 仿真数据 → 真机策略迁移，缓解真机采集昂贵瓶颈 | GR00T 训练栈、域随机化、GR00T-Dreams 合成数据蓝图 |
| **端侧部署** | 量化 VLA + 边缘算力，本体本地低延迟推理、断网可用 | Gemini Robotics On-Device、Jetson Thor / Orin |

> **关键趋势**：竞争重心从「本体硬件参数」转向「模型/大脑能力」——多份资料称机器人「大脑」层是更持久的护城河（类比 Physical AI 时代的 Android/iOS）。

---

## 四、代表技术 / 模型速查表

> 参数与数据量多为厂商或二手媒体口径，横向不完全可比。

| 模型 | 出品方 | 参数量 | 动作生成方式 | 开放程度 | 一句话记忆点 |
|---|---|---|---|---|---|
| **RT-1** | Google（2022） | ~35M | 离散动作 token | 论文 | VLA 的史前时代，证明 Transformer 能开机器人 |
| **RT-2** | Google DeepMind（2023） | 55B（PaLI-X 底座） | 离散动作 token | 闭源 | **开创 VLA 范式**：动作被当成语言 token 输出 |
| **RT-2-X / Open X-Embodiment** | 21 家机构联合 | 55B | 同上 | 数据集开放 | 跨 22 种机身、约 100 万条轨迹的「机器人 ImageNet」尝试 |
| **Octo** | UC Berkeley | 93M | Transformer + 扩散头 | 开源 | **小而快**：Jetson 上可跑 15–20 Hz，单 GPU 半小时微调 |
| **OpenVLA** | Stanford / UC Berkeley | 7B（Llama 2 + SigLIP） | 256 档离散动作 token | 开源（Apache 2.0 与 MIT 两说，**待核实**） | **学术默认起点**：7B 打赢 55B 的 RT-2（宣称 +16.5% 绝对成功率） |
| **π0 (pi-zero)** | Physical Intelligence | ~3B（est.） | **Flow matching**（连续流） | 权重公开（openpi） | 用流匹配换平滑轨迹与亚秒推理，会叠衣服 |
| **π0.5 / π0.6 / π0.7** | Physical Intelligence | ~3B | 同上 + RECAP 自我改进 | 部分闭源 | **π0.6 号称能从自己的部署经验自我提升**（RECAP，**待核实**） |
| **Gemini Robotics 1.5** | Google DeepMind | 未公开 | Gemini 2.0/3.0 底座 + 动作模态 | 合作伙伴限定 | **Motion Transfer**（跨机身数据统一表示）+ Thinking Mode（先想后做） |
| **Gemini Robotics-ER 1.6** | Google DeepMind | 未公开 | 不出动作，出**空间推理** | Gemini API / AI Studio | 把「具身推理」拆成独立层，含成功检测与仪表读取 |
| **Gemini Robotics On-Device** | Google DeepMind | 未公开 | 端侧 VLA | 有限开放（2025-06） | **首个明确端侧跑的 VLA**，宣称 50–100 条示范即可微调 |
| **Isaac GR00T N1 → N1.7** | NVIDIA | 3B（N1.7） | 双系统：慢推理 + 快控制（Action Cascade） | 开放 + 商用许可 | 用 2 万+ 小时**第一人称人类视频**（EgoScale）替代稀缺机器人数据 |
| **Helix** | Figure AI | 未公开 | 双系统（VLM + 视觉运动策略） | 闭源 | 人形上半身高频灵巧控制的代表 |
| **SmolVLA** | Hugging Face | ~450–500M | Flow matching + 异步推理 | 开源（LeRobot） | 消费级 GPU / Jetson 上可跑的「够用版 VLA」 |
| **Cosmos / DreamZero / DreamDojo** | NVIDIA | 14B（DreamZero） | 世界模型 / 世界-动作联合 | 部分开放 | 合成数据引擎，宣称把「造数据」从数月压到数十小时（**待核实**） |
| **Genie 3** | Google DeepMind | 未公开 | 生成可交互 3D 环境 | 有限开放 | 实时生成可交互世界，宣称 720p/24fps |
| **V-JEPA 2** | Meta | 未公开 | JEPA 式世界模型 | 开源 | 不预测像素、预测**表示**；宣称零样本机器人规划 |

**效率化趋势值得单独记一笔**：OpenVLA（7B 打赢 55B）→ SmolVLA（~450M 接近 7B）→ NanoVLA（约 100M，宣称 Jetson 上快 52 倍，**研究阶段·待核实**）。**这条曲线和手机端侧小模型（量化/蒸馏/MoE）是同一条曲线**，见 [[端侧 AI 基建与算力预算]]。

---

## 五、主流玩家布局（2025–2026）

> ⚠️ 财务与出货数字均为公开报道口径，多为二手引述，见文末待核实清单。

### 5.1 模型/平台层（卖「脑子」）

| 玩家 | 定位 | 代表模型/产品 | 2025–2026 进展 |
|---|---|---|---|
| **Google DeepMind** | 全栈模型层，做「物理 AI 的 CUDA」 | Gemini Robotics 1.5 / ER 1.6 / On-Device、Genie 3 | 2025-03 首发 → 2025-09 出 1.5 → 2026-04 出 ER 1.6（**日期待核实**）；合作方含 Boston Dynamics、Apptronik、Agility、Agile Robots、Enchanted Tools；**不自造机器人** |
| **NVIDIA** | 三层通吃：模型（GR00T）+ 仿真/世界模型（Isaac Sim、Cosmos）+ 芯片（Jetson Thor） | GR00T N1→N1.7、N2/DreamZero 预览、Cosmos 3 | 事实上的**行业训练与推理底座**；GTC 2026 口号「Physical AI has arrived」；宣称发现「机器人灵巧性 scaling law」（**待核实**） |
| **Physical Intelligence** | 只做 AI 层、不做硬件（「机器人的 OpenAI」） | π0 → π0.7 + openpi | 13 个月连发三代（**待核实**）；估值 56 亿美元级（Bloomberg 口径，**待核实**）；openpi 成开源事实标准；押注「真机数据 > 互联网视频」 |
| **Meta / World Labs / 蚂蚁等** | 世界模型与研究侧 | V-JEPA 2、Marble、LingBot-VLA | 世界模型作为「数据与物理常识来源」被押注 |
| **Skild AI** | 「全机身通用」机器人大脑 | Skild Brain | 与 ABB、Universal Robots 合作，做工业跨硬件共享智能层 |
| **开源社区/高校** | 基线与生态 | OpenVLA、Octo、LeRobot、SmolVLA | 开源基线持续压缩闭源领先窗口 |

### 5.2 本体层（卖「身体」）

| 玩家 | 阵营 | 代表产品 | 2025–2026 关键数字（**均待核实**） |
|---|---|---|---|
| **宇树科技 Unitree** | 中国·硬件+运控起家 | G1 / H1 / H2 / R1、四足、「Superman」 | **首家 A 股上市人形企业**（科创板），募资约 61 亿元 / 9.05 亿美元，超额认购逾 8000 倍，首日涨逾 600%；2025 营收 16.99 亿元、净利 2.78 亿元、交付 5,500+ 台；2026 H1 营收 11.52 亿（+48.5%）但扣非净利 −19.3%（**增收不增利**）；2026 H1 出货 5,900 台/份额 31%（退居第二）；募资近半（20.22 亿）投向**机器人大模型**——硬件公司买软件门票 |
| **智元机器人 AgiBot** | 中国·工业场景切入 | 远征/Genie 系列、ACoT-VLA、BFM/GCFM、AgiBot World 数据集 | **2026 H1 出货 8,400 台、全球份额 44%，首次登顶**；营收轨迹 30 万 → 6000 万 → 2025 破 10 亿；启动港股 IPO；上海临港量产基地 |
| **优必选 UBTECH** | 中国·港股已上市 | Walker 系列 | 市值 450 亿港元级 |
| **Figure AI** | 美国·高端企业交付 | Figure 02 / 03 + Helix | 宝马 Spartanburg 部署 11 个月、参与生产 3 万+ 辆 X3；Figure 03 产量破 1,000 台，BotQ 号称每小时 1 台 |
| **Tesla** | 美国·垂直自用优先 | Optimus Gen-3 | **口径严重冲突**：一说已小批量试产、设计年产能 100 万台；另一说 Fremont 至 2026 年中仍未开始生产、商用不早于 2027 |
| **Boston Dynamics（现代）** | 美韩·技术标杆 | 电动 Atlas、Spot、Stretch | 技术领先但成本高、未盈利；接 Gemini Robotics；现代工厂部署 |
| **Agility Robotics** | 美国·仓储人形标杆 | Digit | 亚马逊/GXO 物流商用，续航约 8h |
| **1X** | 挪威/美国·明确打家庭 | NEO | 家用预购，2026 交付 |
| **Apptronik** | 美国·企业级试点 | Apollo | 奔驰/NASA/Jabil 试点，Google 背书 |

**格局速记**：**「中国出身体、美国出脑子」是 2026 年最省事的粗略切法**（SAG 口径称 2026 H1 中国企业占全球人形出货 97%，**待核实**），但两边都在往对方阵地打——宇树把募资砸向大模型，Physical Intelligence 坚持不造硬件。**这与手机行业「芯片/OS 在外、整机与场景在内」的历史结构高度相似**，对 [[意图框架的商业与生态博弈]] 有直接类比价值。

---

## 六、2025–2026 进展要点（点到为止）

1. **VLA 从论文变成默认架构。** 2026 年主流说法是「每个大厂都有一个机器人基础模型在飞」；有聚合站称新部署中约 40% 以 VLA 为主策略骨干、2026 Q1 至少 11 个商业部署（**同一聚合站单一来源，待核实**）。
2. **动作生成方式分化出三条路**：离散 token（RT-2/OpenVLA，简单但对连续运动有损）、扩散/流匹配（π0/Octo，轨迹更平滑）、**动作链式思考（Action CoT）**（先想粗轨迹再精细执行，ACoT-VLA/dVLA 等 2026 会议工作）。
3. **双系统架构成为共识**：慢的「想」（2–5 Hz 语义推理）+ 快的「做」（200 Hz 级运动控制）。GR00T、Helix、Gemini Robotics（ER 云端 + On-Device 本地）都是这个形状。**这就是手机侧「云端大模型规划 + 端侧小模型执行」的同一个答案**。
4. **数据成为唯一真瓶颈，于是有了三条数据路线**：真机遥操作（贵，有报道称成本从 2024 年约 340 美元/小时降到约 118 美元/小时，**待核实**）、**第一人称人类视频**（GR00T EgoScale 用 2 万+ 小时；Gemini Motion Transfer 让手机拍的人类视频可用）、**世界模型合成数据**（Cosmos/DreamDojo/GR00T-Dreams）。
5. **端侧化真实发生。** Gemini Robotics On-Device、Jetson Thor、INT8/INT4 量化让量化后 VLA 在消费级 GPU 上跑到 10–25 Hz（**聚合站口径，待核实**）。机器人**没有「上云兜底」的余地**——断连即失控，端侧是硬需求不是省钱手段。这条逻辑与 [[智能座舱与车机 HMI 意图入口 学习笔记]] 里「隧道里必须能用」完全一致。
6. **资本切换叙事：从「技术故事」到「出货量」。** 有统计称 2026 上半年国内具身智能融资超 900 亿元（同比 5 倍）、2025 年全球机器人/物理 AI 初创融资约 276 亿美元（**均待核实**）。宇树 IPO 被普遍视为行业「成人礼」。
7. **落地仍然很浅（本篇最该记住的冷水）。** 宇树招股书口径：2025 年前三季度**工业部署占比不足 10%**，主力客户是科研教育。**无监督家庭通用助手「仍未到来」**（多来源一致结论）。「舞台表演 → 生产力验证」的下半场刚开始。

---

## 七、与端侧智能 / 手机意图框架的同源关系（本篇差异化落点）

| 环节 | 机器人 Agent | 手机端侧 Agent | 同源度 | 谁走得更前 |
|---|---|---|---|---|
| **感知（Perception）** | 摄像头 + 深度 + 力觉 → 视觉编码器 | 屏幕像素 + 无障碍树 → VLM/UI 语义树 | ★★★★☆ | 手机更前（无障碍树是结构化捷径，见 [[无障碍 Accessibility 与 GUI Agent 同源技术栈 学习笔记]]） |
| **意图理解 / 规划** | 语言指令 → 任务分解（Thinking Mode / ER 层） | 用户一句话 → 意图路由 + 多步规划 | ★★★★★ | **几乎同一套东西**，可互相抄 |
| **执行（Action Space）** | 关节角度、末端位姿（连续、**不可撤销**） | App Intent 调用、GUI 点击（离散、多数可撤销） | ★★☆☆☆ | 分岔点：机器人错误代价是物理的 |
| **端云分工** | ER 云端推理 + On-Device 实时控制 | 云端大模型 + 端侧小模型路由 | ★★★★★ | 机器人更前（被延迟逼出来的） |
| **数据飞轮** | 遥操作 + 人类视频 + 仿真合成 | 用户行为日志 + 影子模式 | ★★★☆☆ | 手机数据量大但**动作标注稀缺**，机器人反之 |
| **跨机身 / 跨端泛化** | cross-embodiment（22 种机身共享一个策略） | 跨设备意图流转（手机/车/眼镜） | ★★★★☆ | 概念完全对应，见 [[跨端与多设备意图流转]] |
| **成功判定 / 失败恢复** | ER 显式做「刚才那步成了吗」（单视角约 86%、多视角约 93%，**待核实**） | 任务完成率、降级率、回滚 | ★★★★☆ | **机器人更前**：把「自我成功检测」做成独立模型能力，手机侧值得抄 |
| **形态外辐射** | 人形/轮式/机械臂 | 手机 → [[AI 眼镜与可穿戴意图入口 学习笔记\|眼镜]] → [[智能座舱与车机 HMI 意图入口 学习笔记\|车机]] → 机器人 | ★★★★★ | 机器人是形态谱系的**终点站**：算力最富、约束最硬、动作最不可逆 |

**一句话结论**：**机器人 Agent 是意图入口形态谱系上「执行端最重、纠错最贵」的那一端。** 眼镜解决「没有屏幕怎么表达意图」，车机解决「不能占用视线怎么表达意图」，机器人解决「**动作错了收不回来怎么办**」——后者逼出的「先想后做 + 显式成功检测 + 端侧实时兜底」三件套，是手机意图框架最值得直接搬的三个设计。

---

## 八、对 OS PM 的意义（安卓系统视角）

- **意图入口的物理化**：未来「系统入口」未必是 App 或语音助手，而可能是具身 Agent 接管现实任务（取物、递送、操作设备）——OS 需思考如何成为「物理意图」的调度层。
- **端侧算力需求上探**：VLA/World Model 的端侧推理对 NPU 带宽、内存、能效提出远超当前手机 LLM 的需求；应提前规划「机器人/穿戴/车机」统一的端侧推理底座。
- **跨端流转成刚需**：当意图可在手机→眼镜→车机→机器人间无缝接续，OS 层的「意图总线 / 设备能力发现」将成为新的平台级护城河。
- **权限模型必须重做**：物理执行（动别人的东西）比屏幕操作风险更高，需要更严格的「动作权限 / 二次确认 / 可撤销性分级」设计。**机器人把「不可撤销动作如何授权」这个问题提前逼出了答案，手机侧的支付/发送类 Intent 面临同一问题。**
- **「通用策略模型」是新的系统核心能力**：具身智能可能重演「App → Agent」的范式迁移——继内核、运行时之后，通用策略模型值得被当作一等系统能力对待。

---

## 九、待解问题（留给 Ethon）

- [ ] **机器人 Agent 的端侧部署可行性到底到哪一步了？** Gemini Robotics On-Device、量化 VLA 在 Jetson Thor 上的真实控制频率、首 token 延迟、功耗预算各是多少？「10–25 Hz」是什么量化精度、什么任务下的数字？——答案可直接回填 [[端侧 AI 基建与算力预算]]。
- [ ] **具身数据飞轮怎么构建才成立？** 三条路线（真机遥操作 / 第一人称人类视频 / 世界模型合成）的**边际成本与边际收益曲线**各是什么形状？World Model 生成的数据能真正替代真机采集，还是只能做补充？NVIDIA 的「灵巧性 scaling law」有无第三方复现？
- [ ] **动作 token 化 vs 流匹配 vs Action CoT，哪条会赢？** 还是像 NLP 一样最终分层共存（高层 CoT + 底层扩散）？这个架构选择对手机侧「意图 token 化」有无启示？
- [ ] **「一个模型跨所有机身」是真趋势还是暂时叙事？** cross-embodiment 的迁移损失有多大？若基础模型会锁死在训练时的硬件动力学上，那**软件层的「通用性」是否被硬件悄悄绑定了**——这对「谁掌握意图裁决权」的商业判断影响巨大。
- [ ] **VLA 在「无监督家庭长程操作」上的真实成功率是多少？** 当前公开多为受控演示/厂商视频，缺独立第三方评测。有无可信的第三方 benchmark 与失败模式分析？
- [ ] **具身智能的「技能生态」在哪？** 手机 Agent 的价值来自 App 生态；机器人 Agent 的技能由谁定义、谁分发、怎么收费？有无类似 App Intent 的标准接口层？——这是 [[意图框架的商业与生态博弈]] 的镜像问题。
- [ ] **中美「身体 vs 脑子」分工会固化还是收敛？** 宇树把 IPO 募资近半投向大模型、智元自研 ACoT-VLA，本体厂上攻模型层能成吗？（对照手机行业：整机厂自研 SoC/OS 的历史胜率）
- [ ] **安卓/移动 OS 应如何定义「物理意图」的权限与安全模型？** 不可撤销动作的确认机制、误执行的责任归属、多用户环境下的授权边界。

---

## 附：来源清单

> ⚠️ **本篇来源质量整体偏弱**：除少数 arXiv 论文与 CNN 报道外，多数为 2026 年的 SEO 聚合站与行业博客，非一手论文或官方发布。所有参数、出货、财务数字请按「二手口径」对待。深挖时应优先回到 arXiv 原文与厂商官方 blog/newsroom。

### 首轮检索（2026-08-19）

| 来源 | 主题 | 性质 |
|---|---|---|
| aiwiki.ai / Humanoid robot autonomy levels | 2025–2026 人形进展、GR00T/Helix/Gemini | 维基式综述 |
| ai2.work / VLA Models: The Hidden Brain | VLA 商业化、资本/部署数字 | 行业博客（数字待核实） |
| 新浪财经（2026-08-06） | 孙正义/贝佐斯/黄仁勋押注机器人「大脑」 | 中文财经 |
| compare-robots.com / Humanoids 2026 | 可购买机型与价格 | 消费市场视角 |
| incrypted.com / Humanoid Robot Race | Figure 03/Optimus/Unitree 规格 | 规格汇总 |
| presenc.ai / Humanoid Robot Market Tracker 2026 | 出货/部署/估值 | 汇总表（部分数字冲突） |
| arXiv 2510.19430（GigaBrain-0） | World Model + VLA | **论文（一手）** |
| arXiv 2511.17502（RynnVLA-002） | VLA + World Model 统一，含 LIBERO 97.4% | **论文（一手）** |
| Awesome-VLA 综述 | VLA 模型/基准一览 | 学术汇总 |

### 第二轮广度扩写（2026-09-01）

| 标题 | URL | 性质 |
|---|---|---|
| 从实验室到科创板，宇树科技能否跑出具身智能"加速度"?（宇树 IPO、2026H1 财务、SAG 份额） | https://new.qq.com/rain/a/20260819A06Y8F00 | 媒体（转载光明网） |
| World's top humanoid robot maker surges in blockbuster market debut in China（宇树 IPO、2025 营收/净利/交付、工业占比<10%） | https://cnn.it/4qrbAoL | 媒体（**本篇最可信来源**） |
| 宇树"第一股"，具身"成人礼"丨《2026 具身智能行业研究报告》（中美玩家路径对比） | https://m.21jingji.com/article/20260819/herald/4a4360d8e92708219357775289c53f42.html | 媒体（引研报） |
| 融资 900 亿，机器人大厂在资本时代互搏（IT桔子融资数据、智元营收轨迹、SAG 出货） | https://www.21jingji.com/article/20260819/herald/ec62e4f89a4503c2e92181d225b43f88.html | 媒体（引 IT桔子/SAG） |
| Unitree Raises $904M in China's First Humanoid Robot IPO（Figure/BMW、Tesla 产线、Omdia 份额、GR00T 绑 G1） | https://techfastforward.com/articles/unitree-raises-904m-chinas-first-humanoid-robot-ipo | 聚合站（**多处未标源**） |
| Best Foundation Models for the Physical World in 2026（世界模型全景、DreamZero/DreamDojo/Genie 3/V-JEPA 2/Alpamayo） | https://encord.com/blog/foundation-models-physical-ai-2026 | 厂商博客（行业观察） |
| Top 10 Physical AI Models Powering Real-World Robots in 2026（GR00T N 系列版本与日期、Gemini Robotics 时间线、EgoScale 20,854 小时） | https://cryptokeepercanada.com/top-10-physical-ai-models-powering-real-world-robots-in-2026/ | 聚合站（**站点可信度低**） |
| Physical AI in 2026: Foundation Models for Robot Learning（Pi0/GR00T/OpenVLA/Octo/SmolVLA 参数与推理频率对比） | https://www.roboticscenter.ai/blog/physical-ai-2026 | 行业机构博客 |
| Vision-language-action models: Why they matter（动作头三分法、2026 VLA 模型表、dVLA/ACoT-VLA/NanoVLA） | https://roboticsbiz.com/?p=13544/ | 行业媒体（引 ICLR/CVPR 2026 投稿，**未核对原文**） |
| Vision-Language-Action Models: The Hidden Brain in New Robots（40% 部署占比、遥操作成本、PitchBook 276 亿、π0.6 RECAP） | https://ai2.work/blog/vision-language-action-models-the-hidden-brain-in-new-robots | 聚合站（**数字多处无一手来源**） |
| How Vision-Language-Action Models are Giving Robots Brains（NVIDIA 三层栈、Skild AI、sim-to-real 流程） | https://nexthumanoid.com/?p=250/ | 聚合站（**待核实**） |
| Gemini Robotics 架构深度解析（三模型家族分工、Motion Transfer、Thinking Mode、ER 成功检测 86%/93%、Pointing 87.9%） | http://vibekk.com/archives/gemini-robotics-deep-dive-architecture | 个人博客（**需回 DeepMind 官方核对**） |
| Google DeepMind's Gemini Robotics: Building the CUDA of Physical AI（生态飞轮、Agile Robots 2 万套、加速器计划） | https://www.ainvest.com/de/news/google-deepmind-gemini-robotics-building-cuda-physical-ai-2604 | 财经自媒体（**投资视角，有夸大倾向**） |
| 具身智能/VR-AR 行业综述（π0/OpenVLA/Octo/Hume 双系统、Policy Contrastive Decoding +108%） | https://ima.qq.com/wiki/（分享页，无稳定 URL） | 二手汇编（**URL 不稳定，降权**） |

---

## ⚠️ 待核实清单

1. **所有版本号与发布日期均需回官方核对**：GR00T N1（2025-03 GTC）/ N1.5（2025-05 COMPUTEX）/ N1.6（2025-12-15）/ N1.7 EA（2026-04-17）、Gemini Robotics 1.5（2025-09）、ER 1.6（2026-04-14）、π0 开源（2025-02）——**多来自聚合站，未见官方 newsroom 原文**。首轮已记的「GR00T 版本号 N1.5/N1.6/N1.7 表述不一」问题，第二轮拿到了完整时间线但**来源可信度低**，仍未闭环。
2. **Tesla Optimus 状态口径严重冲突（跨两轮检索均未解决）**：说法包括 2026-03 弗里蒙特量产 / 2026-07~08 启动 / Gen-3 已小批量试产（设计年产能 100 万台）/ 至 2026 年 7 月中仍未开始生产且商用不早于 2027 年底。**四说互斥，暂不采信任一。**
3. **Figure 价格与产能口径冲突**：Figure 03 有称试点约 $130K、另有称起价 $20K；BotQ 产能有「目标 1.2 万台/年」与「每小时 1 台」两种表述。宝马部署数字（11 个月、3 万+ 辆 X3、9 万+ 钣金件、产量破 1,000 台）均为聚合站转述公司口径。
4. **出货与份额数据均为第三方机构二手引述**：SAG 称 2026 H1 全球人形出货 1.91 万台（+274.5%）、中国占 97%、智元 8,400 台/44%、宇树 5,900 台/31%；Omdia 称智元 2025 年 39% 份额。**未获原始报告，统计口径（是否含轮式/四足/教育机型）不明，SAG 与 Omdia 数字体系不一致。「中国占 97%」这类极端份额需特别警惕。**
5. **宇树财务有两套口径**：CNN 称 2025 营收「近 17 亿元 / 2.52 亿美元」、净利 2.78 亿元；21 经济网称 16.99 亿元。基本一致但应以招股书为准。**「发行市值 609 亿元 / 219 倍发行市盈率 / 超额认购 8000 倍 / 首日涨 600% / 募资 20.22 亿投向机器人大模型」需以交易所公告核对。**「Superman 跳高 2 米、速度 12.66 m/s」为公司发布 + 媒体转述，测试条件未知。
6. **智元营收轨迹（30 万 → 6000 万 → 破 10 亿 → 2027 目标 100 亿）为创始人在合作伙伴大会自述**；「2026 Q1 已超 10 亿」为「投资人和智元人士透露」，**属未署名信源，视为传闻**。港股估值区间（400–500 亿港元 / 51–64 亿美元）为外界报道。
7. **Physical Intelligence 估值 56 亿美元**：Bloomberg / Series B（2025-11）口径，经聚合站转述，**未见一手报道**；「13 个月发三代」「RECAP 使吞吐量翻倍」为公司口径。
8. **模型参数多为估算**：π0「~3B (est.)」、GR00T N1「~2B (est.)」、Gemini Robotics 系列全部未公开。**OpenVLA 许可证有 Apache 2.0 与 MIT 两说、归属有 Stanford 与 UC Berkeley 两种表述，需查仓库 LICENSE 与论文。**
9. **性能宣称全部未经独立复现**：OpenVLA 比 RT-2 高 16.5%、dVLA 在 LIBERO 达 96.4%、Policy Contrastive Decoding 使 π0 +108%、DreamZero「泛化翻倍」、GR00T「1000→20000 小时人类视频使任务完成率翻倍」、NanoVLA「快 52 倍」、ER 1.6 仪表读取 93%（vs ER 1.5 的 23%）、Pointing 87.9%——**benchmark 条件与基线均未核对；ICLR/CVPR 2026 部分为投稿状态，可能未录用。**
10. **论文基准数字勿误读为量产表现**：RynnVLA-002 在 LIBERO 达 97.4%、LeRobot 真机实验世界模型提升约 50%——**均为论文仿真/实验室结果，非产品级指标。**
11. **经济性数字最可疑（跨两轮均只有单一来源 ai2.work）**：「新部署 40% 以 VLA 为骨干」（Robotics Center of Silicon Valley）、「遥操作成本 340→118 美元/小时」、「2025 年物理 AI 初创融资 276 亿美元」（PitchBook）、「量化 VLA 在消费级 GPU 跑 10–25 Hz」、「2026 Q1 至少 11 个商业部署」——**无交叉验证，可信度最低。** 中国侧「2026 H1 融资超 900 亿元、同比 5 倍」为 IT桔子口径经媒体转述。
12. **「NVIDIA 选宇树 G1 作为 Isaac GR00T 研究平台」及 Stanford/UCSD/ETH 测试**：聚合站口径，**未见 NVIDIA 官方确认**。「日本航空在羽田机场三年试点 2 台宇树机器人」同源，待核实。
13. **「Helix 02 全身控制 / 4 分钟 61 个动作」**：出自中文财经文章，Figure 官方多称 Helix（Figure 03 搭载）——**传闻·未证实**。
14. **World Action Model / GR00T N2 / Cosmos 3 均处预览或研究阶段**，2026 年底前不宜作为已成立的技术路线引用。
15. **Hume（2025-05 双系统 VLA）、LingBot-VLA（蚂蚁）、ACoT-VLA（智元/CVPR 2026）** 仅见于二手汇编，**未核对论文原文**。

---

#标签/具身智能 #标签/机器人Agent #标签/VLA #标签/世界模型 #标签/广度种子 #标签/发散图谱
