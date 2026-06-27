---
文件代号: DIC-BBM
文件类型: Baseline Blueprint Map｜基线蓝图地图
版本: V0.1
状态: Working Draft
维护入口: 智核中枢·iS-Core
上一步: Step1｜关系与术语锚定
下一步: Step3｜DIC·BBL 章节展开逻辑
生产链条: DIC·BBM → DIC·BBL → DICB
创建日期: 2026-06-27
---

BBM｜超智科技·数智协同基线蓝图地图 V0.1

BBM｜Synexa DIC Baseline Blueprint Map V0.1

文件类型：Baseline Blueprint Map｜基线蓝图地图
目标文件：超智科技·数智协同基线 V0.1
英文名：Synexa Digital-Intelligence Collaboration Baseline V0.1
对外轻主名称：DIC Baseline V0.1
当前阶段：Step2｜DIC·BBM
文件状态：Working Draft / Blueprint
维护入口：智核中枢·iS-Core
后续生产链条：DIC·BBM → DIC·BBL → DICB
主源建议文件名：Synexa_DIC_Baseline_BBM_V0.1.md

⸻

0. BBM 任务定义

本文件不是《超智科技·数智协同基线》的正式正文，而是用于指导其生产的蓝图地图。

BBM 的任务，是在正式进入 BBLx、Markdown 主源、Python 渲染脚本与 HTML 阅读版之前，先把以下事项锚定清楚：

1. 《超智科技·数智协同基线》为什么需要建立；
2. 它与《超智科技认知基线 V3.10》的关系；
3. 它的核心定义与术语边界；
4. 它应解决哪些实际协同问题；
5. 它应继承 V3.10 的哪些上位结构；
6. 它应新增和展开哪些运行机制；
7. 它的章节结构应如何设计；
8. 它如何服务 Nex₂U、Synexa iS、Nex·EC、Nex·PVC 与 Project-to-Skill；
9. 它如何支持小步快跑、快速试错、经验沉淀和持续优化；
10. 它最终如何进入 md → py → html 的正式交付流程。

一句话：

DIC·BBM 是为了确保《超智科技·数智协同基线》不是 AI 工具说明书，也不是另起一套体系，而是与《超智科技认知基线 V3.10》严密咬合的数智协同运行基线。

⸻

1. 当前任务链条确认

本次 DIC 基线生产采用六步链条：

Step1 先锚定关系与术语
  ↓
Step2 生产专用 BBM｜数智协同基线蓝图地图
  ↓
Step3 基于「数智协同专项 BBM」生产 BBLx｜数智协同章节展开逻辑
  ↓
Step4 生成 md｜数智协同基线 Markdown 主源
  ↓
Step5 用 py｜渲染脚本生成 HTML
  ↓
Step6 输出 html｜阅读版 / 检查版 / 后续 PDF 预览基础

1.1 快速触发简称

简称	全称	触发动作	输出物
DIC·BBM	DIC Baseline Blueprint Map	生产数智协同基线蓝图地图	Synexa_DIC_Baseline_BBM_V0.1.md
DIC·BBL	DIC Baseline Build Logic	生产数智协同章节展开逻辑	Synexa_DIC_Baseline_BBLx_V0.1.md
DICB	DIC Baseline	生产正式数智协同基线主源与交付包	Synexa_DIC_Baseline_V0.1.md / .py / .html

1.2 各阶段性质

阶段	文件性质	是否为正式基线正文	核心作用
Step1 关系与术语锚定	前置共识	否	定义关系、名称、边界、术语
Step2 DIC·BBM	蓝图地图	否	定义基线文件怎么生产
Step3 DIC·BBL	章节展开逻辑	否	展开每章写作目标、内容、表格、锚点
Step4 md	Markdown 主源	是	正式事实主源
Step5 py	渲染脚本	否	将 md 渲染为 html，不承载事实修改
Step6 html	阅读输出	否	阅读版、检查版、PDF 预览基础

⸻

2. 文件命名与身份锚定

2.1 中文正式名

超智科技·数智协同基线

2.2 英文正式名

Synexa Digital-Intelligence Collaboration Baseline

2.3 对外轻主名称

DIC Baseline

2.4 文件名建议

文件	建议文件名
BBM 蓝图地图	Synexa_DIC_Baseline_BBM_V0.1.md
BBLx 章节展开逻辑	Synexa_DIC_Baseline_BBLx_V0.1.md
Markdown 主源	Synexa_DIC_Baseline_V0.1.md
Python 渲染脚本	Synexa_DIC_Baseline_Render_V0.1.py
HTML 阅读版	Synexa_DIC_Baseline_V0.1.html
后续机器索引	Synexa_DIC_Baseline_MachineIndex_V0.1.json
后续完整包	Synexa_DIC_Baseline_V0.1.zip

2.5 首屏标题建议

正式 DIC Baseline 首屏标题建议采用三层命名：

超智科技·数智协同基线
Synexa Digital-Intelligence Collaboration Baseline
DIC Baseline V0.1

2.6 命名原则

1. 中文正式名用于内部正式文件、中文材料、项目基线与 GitHub 中文标题；
2. 英文正式名用于英文标题、机器索引、跨语言表达和文件识别；
3. DIC Baseline 可作为对外轻主名称，用于图示、PPT、目录、轻量沟通和系统字段；
4. DIC 不仅是机器短名，也可以作为对外轻量识别名；
5. 正式语境中应优先保留中文名与英文名，DIC 作为辅助强化识别。

⸻

3. DIC Baseline 的一句话定义

建议正式定义为：

《超智科技·数智协同基线｜DIC Baseline》，是在《超智科技认知基线》之下建立的数智协同运行基线，用于统一人类协作者、AI 智能体、数字工具、代码执行体、业务系统与真实项目之间的协同共识，明确任务如何归位、方向如何确认、路径如何拆解、节点如何设计、工具如何调用、结果如何质检、问题如何复盘、经验如何沉淀，并支持超智以小步快跑、快速试错、持续优化的方式推进真实项目。

该定义必须保留以下关键词：

* 《超智科技认知基线》之下；
* 数智协同运行基线；
* 人类协作者；
* AI 智能体；
* 数字工具；
* 代码执行体；
* 业务系统；
* 真实项目；
* 任务归位；
* 方向确认；
* 路径拆解；
* 节点设计；
* 工具调用；
* 结果质检；
* 问题复盘；
* 经验沉淀；
* 小步快跑；
* 快速试错；
* 持续优化。

⸻

4. 与《超智科技认知基线 V3.10》的关系

4.1 关系总判断

《超智科技认知基线 V3.10》与《超智科技·数智协同基线｜DIC Baseline》不是并列竞争关系，而是上下位互补关系。

《超智科技认知基线 V3.10》
= 定义超智是谁、系统是什么、能力如何分层、项目如何归位。
= Company / System / Strategy Master SSOT。
《超智科技·数智协同基线｜DIC Baseline》
= 定义人、AI、Agent、工具、代码、系统与项目如何协同把事情做成。
= Collaboration / Execution / Iteration Baseline。

4.2 关系句

建议在正式 DIC 文件中保留以下关系句：

《超智科技认知基线》定方向、结构与边界；《超智科技·数智协同基线｜DIC Baseline》定路径、节点与协同动作。前者是总图，后者是走法；前者让体系不漂，后者让行动不散。

4.3 不替代原则

DIC Baseline 不替代以下文件：

1. 不替代 Master SSOT；
2. 不替代 Context OS；
3. 不替代 PCS；
4. 不替代 SOP；
5. 不替代 Skill；
6. 不替代项目任务表；
7. 不替代具体系统开发文档；
8. 不替代最终人类裁决。

4.4 继承展开原则

DIC 对 V3.10 的处理方式不是“搬走”，而是“继承、引用、展开”。

V3.10 保留上位定义
  ↓
DIC 继承这些定义
  ↓
DIC 将其展开为路径、节点、动作、模板、质量门和回流机制

4.5 两份文件的功能分工

维度	超智科技认知基线 V3.10	DIC Baseline
核心问题	超智是什么	人和机器如何协同把事做成
文件性质	公司级 Master SSOT	数智协同运行基线
关注重点	定位、能力、架构、项目组合、治理	方向、任务、路径、节点、工具、试错、沉淀
服务对象	决策者、合作方、投资人、内部团队、Agent	内部团队、项目负责人、Agent、数字员工、工具执行体
内容重心	系统成立	系统运行
输出方向	统一认知	统一行动
上下位关系	上位源	下位运行展开
更新逻辑	审慎升级	小步迭代、持续验证
核心风险	定位漂移	行动分散、工具滥用、经验流失

⸻

5. DIC Baseline 的文件层级

5.1 推荐层级

DIC Baseline 建议定位为：

L1 / L2 / L3 混合型专题运行基线

5.2 层级解释

层级	在 DIC 中的体现
L1 Domain Baseline	承接全域数智协同原则，统一人机数智协作方式
L2 Global Standard	定义任务路径、工具调用、Agent 执行、试错反馈、经验沉淀标准
L3 Project Baseline Support	服务 Nex₂U、NexChef、NexSply、Synexa Website 等具体项目

5.3 它不是哪一类文件

DIC Baseline 不是：

1. 不是 L0 Master SSOT；
2. 不是公司介绍文件；
3. 不是单一项目 PCS；
4. 不是 AI 工具说明书；
5. 不是 Agent 平台排行榜；
6. 不是代码开发文档；
7. 不是 SOP 合集；
8. 不是投标方案；
9. 不是客户版材料；
10. 不是对外宣传册。

⸻

6. DIC Baseline 的核心目标

6.1 总目标

统一人和机器在数智协同这件事上的共识，把超智的任务、方向、节点和路径推演清晰、细致、周全和科学；在明确方向和路线后，边走边优化，小步快跑，快速试错，并将问题、经验、规则和判断持续沉淀为可复用资产。

6.2 具体目标

DIC Baseline 至少要完成十项任务：

1. 统一数智协同的基本定义；
2. 明确人、AI、Agent、工具、代码、系统、项目之间的角色关系；
3. 建立任务从目标到交付的标准路径链条；
4. 建立任务归位机制；
5. 建立不同任务类型的节点模板；
6. 建立工具与 Agent 的调用原则；
7. 建立外部执行包机制；
8. 建立小步快跑与快速试错机制；
9. 建立问题 / 异常 / 经验沉淀机制；
10. 建立从任务到 SOP、Skill、Digital Employee、Experience Asset 的转化机制。

6.3 成功标准

本文件完成后，应满足以下标准：

1. 人类协作者能快速理解数智协同的共同规则；
2. AI 智能体能基于本文件识别任务归位和执行路径；
3. 项目负责人能用它拆解任务、节点、责任和质量门；
4. iS-Matrix 能基于它生产 SOP、Skill、模板和执行包；
5. iS-Hub 能基于它维护工具与 Agent Registry；
6. PCS 项目组能基于它推进真实任务；
7. Nex₂U 能以它作为 Step 4 协同架构映射的上位依据；
8. 所有试错结果能进入经验资产沉淀，而不是停留在聊天记录或临时文件中。

⸻

7. DIC Baseline 的核心术语锚定

7.1 数智协同

数智协同，是指在人的方向设定与责任承担之下，将 AI、Agent、数据、代码、工具、业务系统、供应网络、现场执行与经验资产组织成可执行、可反馈、可优化的协同运行机制。

关键边界：

1. 人设方向；
2. 机器出方案；
3. 系统组织任务；
4. Agent 执行动作；
5. 工具提供能力；
6. 项目验证结果；
7. 经验沉淀资产；
8. 下一轮持续优化。

7.2 人智判断 Human Judgment

人智判断，是人在方向、价值、责任、裁决、例外处理和高风险取舍中的不可替代作用。

DIC 中应明确：

* 人智不是补丁，而是方向锚；
* 人智不是低效阻碍，而是责任锚；
* 人不必处理所有细节，但必须保留关键裁决；
* 高风险任务必须保留拒绝、退回、修正和升级路径。

7.3 数智系统 Digital Intelligence

数智系统，是由 AI、Agent、数据、代码、工具、业务引擎、规则和模型共同构成的结构化执行与推演能力。

DIC 中应明确：

* 数智系统负责结构拆解、多引擎协同、任务调度、数据洞察、规则调用与模型进化；
* 数智系统不能自行定义最终价值；
* 数智系统必须接受人智方向与质量门约束。

7.4 协同转化桥 Decision Bridge

协同转化桥，是将人的判断转译为系统任务，再由能力体履约，并将执行结果回流为经验资产的机制。

DIC 的主流程应围绕 Decision Bridge 展开。

7.5 能力体 Capability Entity

能力体，是可以被主体调用的能力资源，包括 AI 模型、Agent、Python、Codex、Claude Code、Manus、Kimi、业务系统、供应网络、设备、知识库、SOP、Skill 等。

边界：

* 能力体响应目标；
* 能力体不自行创造最终目标；
* 能力体必须被任务、权限和质量门约束。

7.6 Agent｜智能体

Agent 是带有目标、工具、边界、上下文和输出要求的任务执行单元。

DIC 中应区分：

* 研究 Agent；
* 结构 Agent；
* 代码 Agent；
* 执行 Agent；
* 审校 Agent；
* 回流 Agent；
* 长期数字员工。

7.7 Skill｜技能资产

Skill 是从高频任务和真实项目中沉淀出的可复用能力模块，包含触发条件、输入要求、执行步骤、工具调用、质量门和输出格式。

DIC 中应强调：

* Skill 不能凭空幻想；
* Skill 应从真实任务中提炼；
* Skill 是 Project-to-Skill 的结果之一；
* Skill 成熟后可进一步转化为 Digital Employee 或 Nex·EC 引擎模块。

7.8 Task Node｜任务节点

任务节点，是从目标到交付过程中可识别、可分派、可执行、可检查、可回流的工作单元。

每个任务节点至少应包含：

* 节点名称；
* 所属路径；
* 输入；
* 输出；
* 责任角色；
* 可用工具；
* 质量门；
* 风险等级；
* 回流位置。

7.9 Trial Loop｜试错闭环

试错闭环，是在明确方向与边界后，以最小可验证动作进行快速验证、记录结果、复盘判断、沉淀经验并决定继续、修正、暂停或升级的机制。

试错不是随意试，也不是盲目快。
试错必须有边界、有记录、有复盘、有资产回流。

7.10 Experience Asset｜经验资产

经验资产，是从真实任务、现场执行、异常处理、推演路径、人类判断和项目复盘中沉淀出的结构化资产。

DIC 中应至少使用以下资产类型：

* Pattern Asset；
* Exception Asset；
* Rule Asset；
* Field Asset；
* Judgment Asset；
* SOP；
* Skill；
* Digital Employee Candidate；
* Engine Module Candidate。

⸻

8. DIC 与 V3.10 的继承展开清单

DIC 应重点继承并展开以下 V3.10 内容：

V3.10 上位内容	DIC 中展开方向
Human-Machine Baseline Protocol	人机数智共识协议
Synexa 是协同智能公司	数智协同是公司定位的运行化表达
四层能力体系	场景智能、供应网络智能、系统智能、协同智能如何进入任务分工
主体 / 能力体 / 能力网络 / 协同网络	人、AI、Agent、工具、系统、项目的角色关系
Human-at-the-Beginning	任务前置定向机制
Human-at-the-Decision	人智裁决与退回机制
Synexa iS	DIC 的系统承载
Human Judgment Layer	人智方向、判断、责任、裁决
Digital Intelligence Layer	结构拆解、任务调度、工具调用、数据洞察
Decision Bridge	DIC 主流程
Nex·EC	任务进入业务引擎的节点化路径
Nex·PVC	数据、反馈、经验资产沉淀机制
Agent-Swarm Production Flow	Agent 分工与外部执行包机制
OODA-PER	任务推进与经验沉淀主方法
Tool / Code / SaaS 选型	工具与 Agent Registry
Project-to-Skill	任务到 SOP / Skill / 引擎模块的蒸馏机制
Experience Asset	问题、异常、字段、规则、判断资产沉淀
Human-Machine Decision Governance	风险分级与权限机制
Baseline Delivery Standard	md → py → html → PDF 的交付规则

⸻

9. DIC Baseline 必须解决的核心问题

9.1 方向问题

DIC 必须回答：

当前任务为什么要做？方向由谁定？成功标准是什么？哪些边界不能碰？

机制要求：

* 任务启动前必须有人智定向；
* 必须明确目标、边界、成功标准；
* 不清楚方向的任务不能直接交给 Agent 或外部工具；
* 高风险任务必须先进入推演或裁决。

9.2 归位问题

DIC 必须回答：

这个任务属于 Core、SCO、Matrix、Hub、Lab、PCS、外部执行体，还是需要新项目？

任务归位建议类型：

归位类型	说明
Core	涉及全局基线、项目归位、战略裁决
SCO	涉及战略推演、路径判断、风险权衡
Matrix	需要生产 SOP、模板、Skill、基线文件
Hub	涉及工具、Agent、平台情报与评估
Lab	未成熟想法，需最小验证
PCS	已归属具体项目的执行任务
External Agent	需 Manus、Codex、Claude Code、Kimi 等执行
New Project	出现新业务对象、新项目域或长期任务体系

9.3 路径问题

DIC 必须回答：

一个目标如何变成可执行路径？

标准路径：

目标提出
  ↓
人智定向
  ↓
任务归位
  ↓
路径推演
  ↓
节点拆解
  ↓
角色分工
  ↓
工具 / Agent 调用
  ↓
执行交付
  ↓
质量检查
  ↓
人智裁决
  ↓
SSOT / PCS 回写
  ↓
经验资产沉淀
  ↓
下一轮优化

9.4 节点问题

DIC 必须回答：

路径中有哪些节点，每个节点由谁负责，用什么工具，产出什么，如何检查？

每个任务节点至少包含：

字段	说明
Node ID	节点编号
Node Name	节点名称
Path Stage	所属路径阶段
Input	输入
Action	执行动作
Owner Role	责任角色
Tool / Agent	可用工具或 Agent
Output	输出
QA Gate	质量门
Risk Level	风险等级
Feedback Destination	回流位置

9.5 工具问题

DIC 必须回答：

ChatGPT、Claude、Codex、Python、Manus、Kimi 等工具分别适合什么，不适合什么？

DIC 中不应写成工具百科，而应写成任务分派规则。

9.6 试错问题

DIC 必须回答：

如何在不失控的情况下小步快跑、快速试错？

必须定义：

* 最小闭环；
* 可试错边界；
* 不可试错事项；
* 试错记录字段；
* 继续 / 修正 / 暂停 / 升级规则；
* 复盘进入资产库的路径。

9.7 沉淀问题

DIC 必须回答：

一次任务如何变成组织能力？

标准路径：

任务执行
  ↓
问题识别
  ↓
对象抽取
  ↓
规则抽取
  ↓
异常归档
  ↓
字段标准化
  ↓
SOP
  ↓
Skill
  ↓
Agent / Digital Employee 配置
  ↓
Nex·EC 引擎模块
  ↓
iS-Cortex 经验资产

9.8 治理问题

DIC 必须回答：

哪些事情可以交给机器？哪些必须人来确认？哪些必须上升到 Core？

风险权限应至少分为：

风险等级	机器权限	人智要求
Low	可建议并自动执行	事后抽查
Medium	可生成方案与执行建议	责任人审核
High	只可推演和建议	Judgment Holder 裁决
Critical / Red	不得自动执行	Core / 指定负责人确认

⸻

10. DIC Baseline 建议章节结构

CH(-1)｜Human-Machine-Digital Baseline Protocol

人机数智共识协议

说明本文件用于统一人类、AI、Agent、工具、系统与项目执行体之间的共同协同规则。

Executive Summary｜执行摘要

用高密度方式说明：

* 为什么建立 DIC；
* DIC 和 V3.10 的关系；
* DIC 解决什么问题；
* DIC 如何服务任务、路径、节点、试错和经验沉淀。

CH 00｜文件定位与使用边界

明确：

* 文件类型；
* 适用对象；
* 不适用对象；
* 上位来源；
* 与 Master SSOT、Context OS、PCS、SOP、Skill 的关系。

CH 01｜数智协同总定义

定义 Synexa 语境下的数智协同，明确其不是单纯 AI 使用，而是人智、数智系统、能力体、业务项目与经验资产之间的协同运行机制。

CH 02｜人、机器与系统的角色关系

展开：

* 主体；
* 能力体；
* Agent；
* Skill；
* Digital Employee；
* 工具；
* 系统；
* 经验资产；
* 人智双锚。

CH 03｜任务归位机制

定义任务如何判断归属：

* Core；
* SCO；
* Matrix；
* Hub；
* Lab；
* PCS；
* External Agent；
* New Project。

CH 04｜标准协同路径

建立从目标提出到经验沉淀的完整路径链条。

CH 05｜任务节点设计机制

定义节点字段、节点模板、节点质量门、节点回流规则。

CH 06｜不同任务类型的节点模板

至少包含：

* 战略推演任务；
* 项目推进任务；
* 文档生产任务；
* 工具选型任务；
* 代码执行任务；
* Nex₂U 业务任务；
* 异常处理任务；
* 外部 Agent 执行任务。

CH 07｜AI / Agent / 工具能力归位

定义 ChatGPT、Claude、Codex、Claude Code、Python、Manus、Kimi 等工具的任务分工、适用场景、禁用边界和回流要求。

CH 08｜执行包机制

定义外部执行包标准：

* Manus 执行包；
* Codex 执行包；
* Claude Code 执行包；
* Kimi 研究包；
* ChatGPT 结构推演包；
* Python 自动化执行包。

CH 09｜小步快跑与快速试错机制

定义：

* 最小闭环；
* 试错触发条件；
* 试错边界；
* 试错记录；
* 复盘机制；
* 继续 / 修正 / 暂停 / 升级判断。

CH 10｜问题、异常与经验沉淀机制

定义：

* 问题分类；
* 异常归因；
* 处理动作；
* 资产类型；
* 回流路径；
* 资产字段。

CH 11｜Project-to-Skill 数智蒸馏机制

展开真实任务如何转化为：

* SOP；
* Skill；
* Agent 配置；
* Digital Employee；
* Nex·EC 模块；
* Experience Asset。

CH 12｜人智决策与风险权限

定义：

* 风险等级；
* 机器权限；
* 人类审核；
* 退回修正；
* Core 升级；
* Decision Record；
* Judgment Asset。

CH 13｜面向 Nex₂U 的应用示范

以 Nex₂U 为首个应用样板，说明 DIC 如何指导：

* 营养规则；
* 菜品数据；
* 订单履约；
* 供应协同；
* 现场反馈；
* NexLens 看板；
* 经验沉淀。

CH 14｜阶段路线图

建议分为：

* 0-30 天：建立 DIC、工具注册、首批执行包与最小节点模板；
* 30-90 天：围绕 Nex₂U 跑最小闭环；
* 90-180 天：形成 SOP / Skill / Agent / Experience Asset 初步体系。

CH 15｜DIC 版本治理与后续升级

定义：

* V0.1 工作版；
* V0.2 试运行版；
* V1.0 稳定版；
* 更新触发条件；
* 与 V3.10 的反向补丁机制。

Appendix A｜AI / Agent / Tool Capability Matrix

工具能力矩阵。

Appendix B｜Task Routing Table

任务归位判断表。

Appendix C｜Task Node Template

任务节点模板。

Appendix D｜Execution Package Template

外部执行包模板。

Appendix E｜Trial Loop Record Template

试错记录模板。

Appendix F｜Experience Asset Capture Template

经验资产沉淀模板。

Appendix G｜Machine-Readable Index

机器可读索引。

Appendix H｜Version Register & Change Log

版本记录与变更日志。

⸻

11. DIC Baseline 必须详细展开的四大机制

11.1 路径链条机制

DIC 必须提供一条全局标准路径：

目标提出
  ↓
人智定向
  ↓
任务归位
  ↓
路径推演
  ↓
节点拆解
  ↓
角色分工
  ↓
工具 / Agent 调用
  ↓
执行交付
  ↓
质量检查
  ↓
人智裁决
  ↓
SSOT / PCS 回写
  ↓
经验资产沉淀
  ↓
下一轮优化

该链条是 DIC 的主轴。

11.2 任务节点机制

DIC 必须为不同任务类型建立节点模板。

至少包含：

1. 战略推演任务节点；
2. 项目推进任务节点；
3. 文档生产任务节点；
4. 工具选型任务节点；
5. 代码执行任务节点；
6. Nex₂U 业务任务节点；
7. 异常处理任务节点；
8. 外部 Agent 执行任务节点。

每个节点必须可以回答：

* 输入是什么；
* 谁负责；
* 用什么工具；
* 输出什么；
* 如何检查；
* 风险多高；
* 回流到哪里。

11.3 试错机制

DIC 必须明确小步快跑不是无序试错。

试错必须具备：

1. 明确目标；
2. 明确边界；
3. 明确最小闭环；
4. 明确风险等级；
5. 明确观察指标；
6. 明确记录模板；
7. 明确复盘方式；
8. 明确资产回流位置。

试错结论必须导向四类动作之一：

动作	含义
Continue	继续扩大验证
Revise	修正路径后继续
Pause	暂停，等待条件成熟
Escalate	升级至 Core / SCO / Matrix / PCS 处理

11.4 问题 / 经验沉淀机制

DIC 必须建立问题到资产的回流路径。

问题出现
  ↓
问题归类
  ↓
风险判断
  ↓
处理动作
  ↓
结果记录
  ↓
复盘结论
  ↓
资产归档
  ↓
SOP / Skill / Agent / Engine 更新

问题类型至少包括：

* 任务问题；
* 工具问题；
* 数据问题；
* 规则问题；
* 代码问题；
* 现场问题；
* 供应问题；
* 人员问题；
* 客户问题；
* 财务问题；
* 版本问题；
* 判断问题。

经验沉淀资产至少包括：

经验类型	沉淀资产
重复出现的流程	Pattern Asset
异常、错误、延误、投诉	Exception Asset
可判断、可触发、可执行的规则	Rule Asset
可复用字段、表格、状态	Field Asset
人类关键判断、拒绝理由、取舍依据	Judgment Asset
可复用操作流程	SOP
可封装能力	Skill
可长期履职角色	Digital Employee
可模块化引擎能力	Nex·EC Engine Module Candidate

⸻

12. DIC 与 Nex₂U 的首个应用关系

12.1 Nex₂U 是 DIC 的首个重点验证场

DIC 应把 Nex₂U 作为首个实际应用样板。原因：

1. Nex₂U 是当前推进中的实战样板；
2. Nex₂U 涉及营养规则、用户需求、菜品结构、订单履约、供应协同、现场执行、数据反馈；
3. Nex₂U 天然需要人、AI、规则、系统、供应链和现场团队协同；
4. Nex₂U 适合验证从任务到 Skill、从项目到经验资产的闭环。

12.2 Nex₂U 最小闭环建议

DIC 中可将 Nex₂U 最小闭环定义为：

10 道菜品
  ↓
4 类营养规则
  ↓
3 类用户
  ↓
1 个点餐页面原型
  ↓
1 个厨房履约表
  ↓
1 个供应备货表
  ↓
1 个反馈记录表
  ↓
1 次复盘
  ↓
沉淀 3 个 Skill

12.3 Nex₂U 首批 Skill 候选

Skill 候选	说明
营养规则转译 Skill	将医学 / 营养建议转化为餐食规则
菜品营养结构化 Skill	将菜品转化为营养字段、标签和适配人群
供应替代策略 Skill	根据缺货、价格、品质和周期生成替代方案
现场异常处理 Skill	将现场异常转为处理动作和经验资产
反馈复盘 Skill	将用户、现场、供应、财务反馈转为复盘资产

⸻

13. DIC 与工作空间的协同关系

DIC Baseline 需要服务现有工作空间，不新增无必要工作空间。

工作空间	与 DIC 的关系
iS-Core	裁决 DIC 定位、版本、上位关系和重大变更
iS-SCO	提供战略推演、路径判断、风险权衡
iS-Matrix	基于 DIC 生产 SOP、Skill、模板、执行包
iS-Hub	基于 DIC 建立 Tool / Agent Registry
iS-Lab	使用 DIC 的试错机制验证未成熟想法
PCS 项目组	使用 DIC 的路径、节点、回流机制推进项目
iS-Nex2U	作为 DIC 首个重点验证样板
iS-Synexa	将 DIC 转译为官网、对外表达和授权展示材料
iS-Nexsply	使用 DIC 的供应协同与工具选型机制
iS-NexChef	使用 DIC 的履约、现场、异常与反馈机制

⸻

14. DIC 的工具与 Agent 归位原则

DIC 不是工具说明书，但必须建立工具归位规则。

14.1 工具角色原则

工具 / 能力体	在 DIC 中的角色
ChatGPT	中枢推演、结构化、执行包、审校
Claude	长文档复核、复杂结构审校、第二视角
Codex	代码实现、仓库任务、脚本、测试
Claude Code	工程协作、代码库理解、开发任务
Python	计算、清洗、自动化、文件生成
Manus	外部执行包落地、网页、PPT、原型
Kimi	中文长资料、政策、投标、供应资料初筛
Skill	可复用能力封装
Agent	任务执行角色
Digital Employee	长期稳定履职角色
PCS	项目状态留账
iS-Cortex	经验资产沉淀

14.2 工具边界原则

1. 工具可以借力，判断必须自有；
2. 代码可以生成，规则必须沉淀；
3. Agent 可以执行，责任必须归人；
4. 模型可以替换，协同秩序不能漂移；
5. 外部执行包必须有输入、边界、输出、质量门和返回格式；
6. 高风险任务不得直接交给外部 Agent 自动完成；
7. 工具输出必须经过回流，不得停留在临时文件或聊天记录中。

⸻

15. DIC 的版本策略

15.1 建议版本路径

版本	状态	说明
V0.1	Working Draft	首版基线主源，完成结构与核心机制
V0.2	Pilot Version	经 Nex₂U 最小闭环试运行后更新
V0.3	Registry Version	增补 Tool / Agent / Skill Registry
V0.5	Operational Beta	完成多个项目使用后的运行版
V1.0	Stable Baseline	经至少 2-3 个项目验证后形成稳定基线

15.2 与 V3.10 的反向补丁策略

DIC V0.1 完成后，暂不立即升级 V3.10。
待 DIC 完成初步验证后，再考虑给 V3.10 做轻量引用补丁。

建议补丁位置：

1. CH04.1 项目组合总表；
2. CH26.9 全域基线对齐协议；
3. Appendix G Machine-Readable Index；
4. Version Register。

建议新增项目项：

Project ID	项目 / 模块名称	架构归属	生态定位	当前成熟度	基线归属
PRJ-026	Synexa Digital-Intelligence Collaboration Baseline｜超智科技·数智协同基线	Decision Bridge / Output Layer / Long-term Value Layer	数智协同运行基线，定义人、AI、Agent、工具、系统与项目如何协同推进任务	concept / active	L1 / L2 / L3 Baseline

⸻

16. DIC·BBL 的生产要求

下一步 DIC·BBL 应基于本 BBM，进一步展开每一章的生产逻辑。

DIC·BBL 必须为每章输出：

1. 章节目标；
2. 章节核心问题；
3. 章节必须保留的判断句；
4. 章节应包含的表格；
5. 章节应引用的上位来源；
6. 章节与 V3.10 的关系；
7. 章节与 Nex₂U / PCS / SOP / Skill 的关系；
8. 章节机器锚点；
9. 章节质量门；
10. 章节输出边界。

DIC·BBL 不是正文，但必须足够细，使后续 Markdown 主源可以稳定生成。

⸻

17. DICB 的生产要求

DICB 触发后，应完成正式基线生产。

17.1 最小交付物

交付物	文件名
Markdown 主源	Synexa_DIC_Baseline_V0.1.md
Python 渲染脚本	Synexa_DIC_Baseline_Render_V0.1.py
HTML 阅读版	Synexa_DIC_Baseline_V0.1.html

17.2 建议后续交付物

交付物	文件名
Machine Index	Synexa_DIC_Baseline_MachineIndex_V0.1.json
PDF 预览版	Synexa_DIC_Baseline_V0.1.pdf
完整包	Synexa_DIC_Baseline_V0.1.zip
Audit Note	Synexa_DIC_Baseline_AuditNote_V0.1.md

17.3 交付原则

1. Markdown 是主源；
2. Python 是渲染工具；
3. HTML 是阅读输出；
4. PDF 是后续正式归档形态；
5. JSON / YAML 是机器索引；
6. ZIP 是完整交付包；
7. 内容修改必须回到 Markdown 主源；
8. HTML / PDF 不作为事实修改源。

⸻

18. BBM 质量门

本 BBM 通过条件如下：

检查项	通过标准
文件关系	明确 DIC 与 V3.10 的上下位关系
命名体系	中文名、英文名、DIC 轻主名称均已锚定
文件性质	明确 DIC 是数智协同运行基线，不是工具说明书
继承关系	明确 V3.10 中哪些内容由 DIC 继承展开
核心机制	路径链条、任务节点、试错机制、经验沉淀机制已纳入
应用样板	明确 Nex₂U 是首个重点验证场
生产路径	明确 DIC·BBM → DIC·BBL → DICB
交付路径	明确 md → py → html
边界控制	明确不替代 Master SSOT、PCS、SOP、Skill
后续动作	明确下一步进入 DIC·BBL

⸻

19. BBM 结论

本 BBM 确认：

1. 《超智科技·数智协同基线｜DIC Baseline》应作为《超智科技认知基线 V3.10》之下的数智协同运行基线；
2. DIC 不另起体系，不替代 V3.10，而是继承并展开 V3.10 中与人机协同、任务推进、工具调用、试错反馈、经验沉淀有关的机制；
3. DIC 的核心功能，是统一人类协作者、AI 智能体、数字工具、代码执行体、业务系统与真实项目之间的协同共识；
4. DIC 必须详细展开路径链条、任务节点、试错机制、问题复盘、经验沉淀、工具调用、Agent 分工和人智裁决机制；
5. Nex₂U 应作为 DIC 首个重点验证场；
6. 后续生产应按 DIC·BBM → DIC·BBL → DICB 执行；
7. 正式主源应采用 Markdown，后续通过 Python 渲染为 HTML 阅读版。

最终锚定句：

V3.10 定义超智的总图，DIC Baseline 定义超智的走法。
前者让体系不漂，后者让行动不散。
前者回答“我们是什么”，后者回答“人和机器如何一起把事情做成”。