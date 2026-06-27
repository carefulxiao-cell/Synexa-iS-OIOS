---
文件代号: DIC-BBLx
文件类型: Baseline Layer Structure｜章节展开逻辑
版本: V0.1
状态: Working Draft
维护入口: 智核中枢·iS-Core
上一步: Step2｜DIC·BBM 基线蓝图地图
下一步: Step4｜DICB Markdown 主源
生产链条: DIC·BBM → DIC·BBL → DICB
创建日期: 2026-06-27
---

BBLx｜超智科技·数智协同基线章节展开逻辑 V0.1

BBLx｜Synexa DIC Baseline Build Logic Extended V0.1

文件类型：Baseline Build Logic Extended｜章节展开逻辑
目标文件：超智科技·数智协同基线 V0.1
英文名：Synexa Digital-Intelligence Collaboration Baseline V0.1
对外轻主名称：DIC Baseline V0.1
上一步文件：Synexa_DIC_Baseline_BBM_V0.1.md
当前阶段：Step3｜DIC·BBL
文件状态：Working Draft / Build Logic
维护入口：智核中枢·iS-Core
后续生产链条：DIC·BBM → DIC·BBL → DICB
主源建议文件名：Synexa_DIC_Baseline_BBLx_V0.1.md

⸻

0. BBLx 任务定义

本文件不是《超智科技·数智协同基线》的正式正文，而是基于 Synexa_DIC_Baseline_BBM_V0.1.md 进一步展开正式基线各章节的生产逻辑。

BBM 解决的是：

这份基线为什么要建、和 V3.10 什么关系、边界在哪里、整体结构是什么。

BBLx 解决的是：

每一章具体写什么、为什么写、引用哪里、需要什么表格、保留哪些判断、如何验收。

因此，BBLx 是 DICB 正式 Markdown 主源的直接施工逻辑。

⸻

1. 当前生产链条确认

DIC Baseline 生产链条如下：

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

快速触发简称：

DIC·BBM  →  生产《数智协同基线蓝图地图》
DIC·BBL  →  生产《数智协同章节展开逻辑》
DICB     →  生产《超智科技·数智协同基线》正式主源与交付包

当前状态：

Step1 已完成。
Step2 已完成主源草案。
Step3 本文件为 DIC·BBL 主源草案。
Step4 后续基于本文件生成 DICB Markdown 主源。

⸻

2. DICB 正式基线的章节总结构

正式《超智科技·数智协同基线｜DIC Baseline V0.1》建议采用以下章节结构：

CH(-1)｜Human-Machine-Digital Baseline Protocol｜人机数智共识协议
Executive Summary｜执行摘要
CH 00｜文件定位与使用边界
CH 01｜数智协同总定义
CH 02｜人、机器与系统的角色关系
CH 03｜任务归位机制
CH 04｜标准协同路径
CH 05｜任务节点设计机制
CH 06｜不同任务类型的节点模板
CH 07｜AI / Agent / 工具能力归位
CH 08｜执行包机制
CH 09｜小步快跑与快速试错机制
CH 10｜问题、异常与经验沉淀机制
CH 11｜Project-to-Skill 数智蒸馏机制
CH 12｜人智决策与风险权限
CH 13｜面向 Nex₂U 的应用示范
CH 14｜阶段路线图
CH 15｜DIC 版本治理与后续升级
Appendix A｜AI / Agent / Tool Capability Matrix
Appendix B｜Task Routing Table
Appendix C｜Task Node Template
Appendix D｜Execution Package Template
Appendix E｜Trial Loop Record Template
Appendix F｜Experience Asset Capture Template
Appendix G｜Machine-Readable Index
Appendix H｜Version Register & Change Log

章节主轴应始终围绕：

共识 → 方向 → 任务 → 路径 → 节点 → 分工 → 工具 → 执行 → 质检 → 回流 → 迭代

⸻

3. 全文写作总原则

3.1 不写成 AI 工具说明书

DIC Baseline 不是 ChatGPT、Claude、Codex、Manus、Kimi、Python 的工具百科。
工具章节只是其中一部分，且必须服务于数智协同运行机制。

3.2 不重复 V3.10

V3.10 定义公司总图、系统架构、能力体系、项目组合和全域治理规则。
DIC 不应重复 V3.10，而应继承并展开其运行层逻辑。

3.3 不替代 PCS / SOP / Skill

DIC 定义协同运行规则。
具体项目状态仍归 PCS；具体操作流程归 SOP；可复用能力归 Skill。

3.4 不追求一次写满

V0.1 应先形成稳定主干，包括：

1. 数智协同定义；
2. 人机角色关系；
3. 任务归位；
4. 路径链条；
5. 节点模板；
6. 工具 / Agent 分工；
7. 试错机制；
8. 经验沉淀；
9. Nex₂U 示例；
10. 版本治理。

后续可在 V0.2 / V0.3 中补充更多 Registry、字段字典、样例和项目应用。

3.5 保持人机双读

正式 DIC 文件必须同时满足：

读者	要求
人类协作者	能快速理解为什么、怎么做、谁负责、如何判断
AI / Agent	能解析章节、任务、字段、路径、触发条件
项目负责人	能拆任务、设节点、定责任、追状态
iS-Matrix	能据此生产 SOP / Skill / 模板
Manus / Codex	能据此生成文件、脚本、页面、模板
GitHub / Registry	能据此建立索引与版本管理

⸻

4. CH(-1)｜Human-Machine-Digital Baseline Protocol｜人机数智共识协议

4.1 章节目标

本章用于说明 DIC Baseline 是一份面向人类、机器、智能体、项目和组织共同读取的数智协同运行基线。

它不是普通说明书，而是所有后续 DICB、GitHub 治理、项目台、执行包、试错复盘和经验沉淀的共同协议入口。

4.2 核心问题

本章必须回答：

1. 这份文件为什么需要人机共读；
2. 人、机器、Agent、系统分别如何读取；
3. 什么是 DIC 的主源；
4. 哪些输出只是阅读版或渲染版；
5. 如何避免聊天记录漂移、文件漂移、执行漂移。

4.3 必须保留的判断句

DIC Baseline 的目标不是把所有 AI 工具写得最多，而是在最小冗余下统一人类判断、机器执行、系统调度与经验沉淀的协同秩序。
Markdown 是事实主源，HTML 是阅读输出，PDF 是归档形态，JSON / YAML 是机器索引；所有事实修改必须回到 Markdown 主源。
DIC Baseline 面向人类理解，也面向机器解析；面向项目推进，也面向经验资产沉淀。

4.4 建议表格

表 1｜DIC 四类读者

读者类型	读取目标	使用入口
Human	理解协同规则、任务路径、责任边界	Executive Summary / CH01-CH05
Machine	解析字段、节点、路径、状态	Appendix G / 表格 / 机器锚点
Agent	按任务归位、执行包、质量门推进	CH03 / CH08 / Appendix D
Organization	用于项目治理、经验沉淀、版本升级	CH10 / CH11 / CH15

表 2｜DIC 文件源规则

文件形态	作用	是否事实主源
Markdown	正式内容主源	是
Python	渲染脚本	否
HTML	阅读版 / 检查版	否
PDF	后续归档版	否
JSON / YAML	机器索引 / 字段映射	否，除非专门声明
ZIP	完整交付包	否

4.5 上位引用关系

本章继承 V3.10 的 Human-Machine Baseline Protocol、人机共读结构、Markdown 主源规则与文件交付治理逻辑。

4.6 质量门

本章通过条件：

* 明确 DIC 是人机数智共识协议；
* 明确 Markdown 主源优先；
* 明确 HTML / PDF 不可作为事实修改源；
* 明确 DIC 不是 AI 工具说明书。

⸻

5. Executive Summary｜执行摘要

5.1 章节目标

用最短篇幅让读者理解：

1. DIC 是什么；
2. 为什么需要 DIC；
3. DIC 和 V3.10 的关系；
4. DIC 解决什么问题；
5. DIC 如何服务真实项目；
6. DIC 的核心运行链条是什么。

5.2 核心问题

本章必须回答：

如果只读 3 分钟，读者应该获得哪些不可丢失的共识？

5.3 必须保留的判断句

《超智科技认知基线》定方向、结构与边界；《超智科技·数智协同基线｜DIC Baseline》定路径、节点与协同动作。
前者是总图，后者是走法；前者让体系不漂，后者让行动不散。
DIC Baseline 不是为了追逐 AI 工具，而是为了让人、AI、Agent、工具、代码、系统与真实项目形成可执行、可反馈、可沉淀、可优化的协同机制。

5.4 建议表格

表 1｜DIC 核心摘要

项目	内容
中文正式名	超智科技·数智协同基线
英文正式名	Synexa Digital-Intelligence Collaboration Baseline
轻主名称	DIC Baseline
上位文件	超智科技认知基线 V3.10
文件性质	数智协同运行基线
核心功能	定路径、节点、任务、分工、工具、试错、沉淀
首个应用样板	Nex₂U
后续应用	GitHub 治理、项目台、番医功能台、SOP / Skill / Agent

表 2｜V3.10 与 DIC 的分工

维度	V3.10	DIC
核心问题	超智是什么	人和机器如何协同把事做成
文件性质	Master SSOT	数智协同运行基线
关注重点	定位、架构、能力、项目组合	任务、路径、节点、试错、经验
作用	统一认知	统一行动
更新逻辑	审慎升级	小步迭代

5.5 上位引用关系

继承 V3.10 的公司定位、Synexa iS、Human Judgment、Digital Intelligence、Decision Bridge、Nex·EC、Nex·PVC、Project-to-Skill 与 Experience Asset。

5.6 质量门

本章通过条件：

* 读者能快速理解 DIC 与 V3.10 的关系；
* 不把 DIC 误解为工具手册；
* 不把 DIC 误解为替代 Master SSOT；
* 明确 DIC 的首个应用样板是 Nex₂U。

⸻

6. CH 00｜文件定位与使用边界

6.1 章节目标

定义 DIC Baseline 的文件身份、适用对象、不适用对象、上下位关系、更新边界和使用方式。

6.2 核心问题

本章必须回答：

1. DIC 是哪类文件；
2. DIC 不是哪类文件；
3. 谁应该使用 DIC；
4. DIC 与 Master SSOT、Context OS、PCS、SOP、Skill 的关系；
5. DIC 未来如何升级。

6.3 必须保留的判断句

DIC Baseline 是《超智科技认知基线 V3.10》之下的数智协同运行基线，不替代 Master SSOT，不替代 PCS，不替代 SOP，不替代 Skill。
DIC 定义协同运行规则；具体项目状态仍由 PCS 管理，具体操作流程由 SOP 固化，可复用能力由 Skill 承载。

6.4 建议表格

表 1｜DIC 文件身份

项目	定义
Document Type	Domain / Operational Baseline
Chinese Name	超智科技·数智协同基线
English Name	Synexa Digital-Intelligence Collaboration Baseline
Short Name	DIC Baseline
Version	V0.1
Upper Source	Synexa Company Intro V3.10
Maintainer	iS-Core
Implementation Roles	iS-Matrix / Manus / Codex / Project PCS
First Application	Nex₂U

表 2｜DIC 不替代清单

不替代对象	原因
Master SSOT	V3.10 仍是公司级最高认知源
Context OS	Context OS 记录动态状态与待同步事项
PCS	PCS 管具体项目执行状态
SOP	SOP 管稳定流程
Skill	Skill 管可复用能力封装
GitHub Registry	Registry 管索引与文件状态
Human Judgment	高风险决策仍需人智裁决

6.5 上位引用关系

本章继承 V3.10 的文件说明与使用边界、Master SSOT 定位、文件主源规则、全域基线对齐协议。

6.6 质量门

本章通过条件：

* 文件身份清楚；
* 上下位关系清楚；
* 不替代原则清楚；
* 使用对象清楚。

⸻

7. CH 01｜数智协同总定义

7.1 章节目标

正式定义 Synexa 语境下的“数智协同”。

7.2 核心问题

本章必须回答：

1. 什么是数智协同；
2. 为什么不是单纯 AI 协同；
3. 为什么不是单纯数字化；
4. 为什么不是自动化；
5. 数智协同如何形成组织能力。

7.3 必须保留的定义

数智协同，是指在人的方向设定与责任承担之下，将 AI、Agent、数据、代码、工具、业务系统、供应网络、现场执行与经验资产组织成可执行、可反馈、可优化的协同运行机制。

7.4 必须保留的判断句

数智协同不是让机器替代人，而是让人的方向、机器的执行、系统的反馈和经验的沉淀形成持续进化的协同秩序。
工具可以借力，判断必须自有；代码可以生成，规则必须沉淀；Agent 可以执行，责任必须归人。

7.5 建议表格

表 1｜数智协同构成要素

要素	作用
人智判断	方向、价值、责任、裁决
AI / LLM	理解、推演、生成、结构化
Agent	任务执行与角色化推进
Python / Code	计算、清洗、自动化、文件生成
业务系统	承接流程、状态、履约
供应网络	真实资源与履约能力
现场执行	将方案变成真实服务
经验资产	将一次执行变成长期能力

表 2｜数智协同不是

误解	正确理解
AI 工具使用	数智协同运行机制
自动化替代人	人智定向 + 数智执行 + 人智裁决
做一个系统	形成可迭代的协同秩序
项目管理表	任务、节点、工具、反馈、经验闭环
模型能力展示	真实场景中的可交付能力

7.6 上位引用关系

继承 V3.10 的协同智能公司定位、主体 / 能力体 / 能力网络 / 协同网络、人智双锚、Decision Bridge。

7.7 质量门

本章通过条件：

* 数智协同定义准确；
* 不等同于 AI 工具；
* 不等同于自动化；
* 与 Synexa iS 关系清晰。

⸻

8. CH 02｜人、机器与系统的角色关系

8.1 章节目标

定义人类协作者、AI、Agent、工具、代码执行体、业务系统、Skill、Digital Employee、经验资产之间的角色关系。

8.2 核心问题

本章必须回答：

1. 谁是主体；
2. 谁是能力体；
3. Agent 与工具的区别；
4. Skill 与 SOP 的区别；
5. Digital Employee 何时成立；
6. 系统如何组织这些角色。

8.3 必须保留的判断句

主体拥有目标、判断与责任；能力体响应目标、执行任务并返回结果。
Agent 不是万能助手，而是带目标、工具、边界和输出要求的任务执行单元。
Skill 不是文档说明，而是可触发、可复用、可组合、可审计的能力资产。

8.4 建议表格

表 1｜角色关系总表

角色	定义	可做	不可做
Human Judgment	方向、价值、责任与裁决主体	定方向、审方案、承担责任	被机器替代
AI / LLM	认知发动机	理解、生成、推演、结构化	独立承担高风险决策
Agent	任务执行单元	按边界执行任务	自行定义目标
Tool	能力工具	提供特定功能	替代系统治理
Python / Code	计算与自动化手臂	数据处理、脚本、渲染	价值判断
Business System	业务承载系统	状态、流程、记录、履约	自行决定战略
SOP	稳定流程	规范做法	替代判断
Skill	可复用能力	执行高频能力	替代责任主体
Digital Employee	长期履职角色	持续承担标准化职责	超出授权范围行动
Experience Asset	经验沉淀	复用判断、规则、异常	停留在散乱记录

表 2｜SOP / Skill / Agent / DE 区分

类型	核心问题	成熟条件
SOP	标准流程怎么做	流程稳定、可培训
Skill	高频能力怎么复用	可触发、可封装、可验证
Agent	谁来执行一个任务	有目标、工具、边界
Digital Employee	谁长期承担一类职责	稳定职责 + 持续运行 + 质量门

8.5 上位引用关系

继承 V3.10 的主体、能力体、能力网络、协同网络、人智双锚和 Synexa iS 系统分层。

8.6 质量门

本章通过条件：

* 主体与能力体边界清楚；
* Agent / Tool / Skill / DE 不混淆；
* 人智责任不可替代。

⸻

9. CH 03｜任务归位机制

9.1 章节目标

定义一个任务出现后，应如何判断它归属于哪个工作空间、哪个项目、哪个执行体或是否需要新建项目。

9.2 核心问题

本章必须回答：

1. 一个任务来了先归哪里；
2. 什么任务归 Core；
3. 什么任务归 SCO；
4. 什么任务归 Matrix；
5. 什么任务归 Hub；
6. 什么任务归 Lab；
7. 什么任务归 PCS；
8. 什么任务交给 Manus / Codex / Kimi；
9. 什么任务需要建立新项目。

9.3 必须保留的判断句

任务不先归位，就不应直接执行；未归位的执行，往往会造成重复劳动、责任模糊和经验流失。
DIC 的任务归位不是行政分工，而是为了确保每个任务都有正确的认知层级、执行角色、质量门和回流位置。

9.4 建议表格

表 1｜任务归位判断表

归位类型	触发条件	典型输出
iS-Core	全局基线、项目归位、战略裁决、优先级冲突	裁决、Step 0A、全局同步
iS-SCO	战略推演、路径判断、复杂取舍	策略推演、选项评估
iS-Matrix	SOP、模板、Skill、基线文件生产	文档资产、规程、模板
iS-Hub	工具、Agent、平台、外部案例评估	Tool Registry、情报清单
iS-Lab	未成熟想法、轻量验证	可行性判断、立项建议
PCS	已归属具体项目的执行推进	项目任务、里程碑、复盘
External Agent	需要文件操作、代码、页面、资料整理	执行包、文件产出
New Project	出现新业务对象、长期机制或独立项目域	项目最小定义、PCS

表 2｜任务归位输出字段

字段	说明
Task ID	任务编号
Task Name	任务名称
Trigger	触发原因
Routing Decision	归位结论
Owner	主责角色
Support Role	协作角色
Required Input	输入材料
Expected Output	输出
QA Gate	质量门
Feedback Destination	回流位置

9.5 上位引用关系

继承 AI Workspace Architecture 中的 Core / Hub / SCO / Matrix / PCS / Lab 分工，以及 iS 指令中的工作空间职责边界。

9.6 质量门

本章通过条件：

* 各类任务归位清楚；
* 不把所有任务都交给 iS-Core；
* 不把执行任务误当战略任务；
* 每个任务都有回流位置。

⸻

10. CH 04｜标准协同路径

10.1 章节目标

建立 DIC 的全局主流程。

10.2 核心问题

本章必须回答：

一个目标如何从人的想法，变成机器可执行的任务，再变成可回流的经验资产？

10.3 必须保留的主流程

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

10.4 必须保留的判断句

DIC 的标准协同路径，不是为了增加流程，而是为了让每一次执行都能被理解、被分派、被检查、被复盘、被沉淀。

10.5 建议表格

表 1｜标准协同路径展开表

阶段	核心动作	主责	输出
目标提出	提出任务意图	人 / 项目负责人	初始目标
人智定向	明确方向、边界、成功标准	Judgment Holder	定向说明
任务归位	判断归属与路径	iS-Core / DIC	Routing Decision
路径推演	形成行动路线	SCO / Matrix	路径草案
节点拆解	拆成任务节点	Matrix / PCS	Node List
角色分工	分配人、Agent、工具	PCS / Task Room	Role Map
工具调用	生成执行包	Matrix / Manus / Codex	Handoff Package
执行交付	完成任务	人 / Agent / 工具	Deliverable
质量检查	检查内容、格式、风险	QA Role	QA Result
人智裁决	通过、退回、升级	Judgment Holder	Decision Record
SSOT / PCS 回写	回写主源或项目账本	Manus / PCS	Updated File
经验沉淀	形成资产	iS-Cortex / Matrix	Experience Asset
下一轮优化	修正路径与规则	Core / PCS	Patch / Version

10.6 上位引用关系

继承 V3.10 的 Human-Machine Decision Loop、Decision Bridge、OODA-PER、Project-to-Skill。

10.7 质量门

本章通过条件：

* 主流程完整；
* 每一步有主责和输出；
* 能连接 SSOT / PCS / Experience Asset；
* 不只是流程图，而能指导执行。

⸻

11. CH 05｜任务节点设计机制

11.1 章节目标

定义什么是任务节点，以及每个任务节点必须包含哪些字段。

11.2 核心问题

本章必须回答：

1. 什么是任务节点；
2. 一个节点如何被识别；
3. 一个节点如何被分派；
4. 一个节点如何检查；
5. 一个节点如何回流。

11.3 必须保留的定义

任务节点，是从目标到交付过程中可识别、可分派、可执行、可检查、可回流的工作单元。

11.4 建议表格

表 1｜Task Node 标准字段

字段	说明
Node ID	节点编号
Node Name	节点名称
Path Stage	所属路径阶段
Project / Domain	所属项目或领域
Input	输入
Action	执行动作
Owner Role	主责角色
Support Role	协作角色
Tool / Agent	可用工具或 Agent
Output	输出
QA Gate	质量门
Risk Level	风险等级
Status	状态
Feedback Destination	回流位置
Asset Candidate	是否可沉淀资产

表 2｜节点状态枚举

状态	含义
Draft	待确认
Ready	可执行
In Progress	执行中
Blocked	阻塞
Review	待审核
Returned	退回修正
Accepted	已通过
Archived	已归档
Assetized	已资产化

11.5 上位引用关系

继承 V3.10 的项目组合定位规则、NexTask、NexFlow、Output System、Experience Asset 机制。

11.6 质量门

本章通过条件：

* 节点字段可直接转表；
* 节点状态可追踪；
* 节点能回流 PCS / SOP / Skill / Experience Asset；
* 节点不是普通待办事项。

⸻

12. CH 06｜不同任务类型的节点模板

12.1 章节目标

为不同任务类型建立节点模板，避免所有任务都用同一张表。

12.2 必须覆盖的任务类型

1. 战略推演任务；
2. 项目推进任务；
3. 文档生产任务；
4. 工具选型任务；
5. 代码执行任务；
6. Nex₂U 业务任务；
7. 异常处理任务；
8. 外部 Agent 执行任务。

12.3 建议表格

表 1｜战略推演任务节点

节点	输入	输出	主责
背景识别	事件 / 问题 / 机会	背景说明	SCO
目标确认	用户意图	战略目标	Core / User
约束识别	资源 / 时间 / 风险	约束清单	SCO
路径推演	目标与约束	选项与判断	SCO
人智裁决	推演结果	决策记录	Core / Judgment Holder
回写	决策结果	Context / PCS / Log	Core / Manus

表 2｜文档生产任务节点

节点	输入	输出
BBM	目标与关系锚定	蓝图地图
BBLx	BBM	章节展开逻辑
md	BBLx	Markdown 主源
py	md + 渲染规范	渲染脚本
html	md + py	阅读版
QA	全部输出	质检记录
回写	通过文件	GitHub / Index

表 3｜Nex₂U 业务任务节点

节点	输入	输出
用户需求识别	用户 / 患者 / 场景	需求标签
营养规则转译	医学 / 营养建议	规则条目
菜品数据结构化	菜品 / 原料	营养字段
菜单生成	规则 + 菜品	菜单方案
订单履约	用户选择	厨房任务
供应备货	菜单需求	原料需求
现场执行	出品 / 服务	状态记录
反馈采集	用户 / 现场反馈	反馈记录
经验沉淀	反馈 / 异常	Asset / SOP / Skill

12.4 上位引用关系

继承 Nex₂U、NexChef、NexSply、NexTask、NexMPC、NexLens、OODA-PER、Project-to-Skill。

12.5 质量门

本章通过条件：

* 每类任务有节点模板；
* 模板可转 CSV / Base / 系统字段；
* Nex₂U 示例足够清晰；
* 不把所有任务粗暴统一。

⸻

13. CH 07｜AI / Agent / 工具能力归位

13.1 章节目标

定义不同 AI 工具、Agent、代码能力和外部执行体在 DIC 中的角色分工。

13.2 核心问题

本章必须回答：

1. ChatGPT 做什么；
2. Claude 做什么；
3. Codex / Claude Code 做什么；
4. Python 做什么；
5. Manus 做什么；
6. Kimi 做什么；
7. Skill、Agent、Digital Employee 如何区别；
8. 哪些工具不能承担最终裁决。

13.3 必须保留的判断句

工具可以借力，判断必须自有。
模型可以替换，协同秩序不能漂移。
外部 Agent 只能执行任务包，不应直接接收模糊战略任务。

13.4 建议表格

表 1｜工具能力归位表

工具 / 能力体	DIC 角色	适合任务	禁止事项
ChatGPT	中枢推演与结构化	战略整理、文件结构、执行包、审校	替代最终 SSOT
Claude	长文档复核	长文审校、结构对照	单独裁决业务
Codex	工程执行	代码、脚本、测试	决定业务规则
Claude Code	工程协作	代码库理解、开发任务	替代产品判断
Python	计算与自动化	数据处理、渲染、表格、模型	价值判断
Manus	文件工程与执行落地	页面、PPT、HTML、文件包、GitHub 整理	自行改写上位定义
Kimi	中文资料初筛	长资料、政策、投标、供应商材料	最终裁决
Skill	能力资产	高频可复用能力	临时内容堆放
Agent	任务角色	带边界执行任务	自行定义目标
Digital Employee	长期履职角色	稳定职责运行	超授权行动

13.5 上位引用关系

继承 V3.10 的工具、代码与 SaaS 选型机制、Agent-Swarm Production Flow、Project-to-Skill、Human-Machine Decision Governance。

13.6 质量门

本章通过条件：

* 工具分工清晰；
* 有禁用边界；
* 不写成工具百科；
* 支持后续 Tool / Agent Registry。

⸻

14. CH 08｜执行包机制

14.1 章节目标

定义如何把一个任务交给 Manus、Codex、Claude Code、Kimi、ChatGPT、Python 等执行体。

14.2 核心问题

本章必须回答：

1. 什么是执行包；
2. 什么时候需要执行包；
3. 执行包必须包含什么；
4. 返回结果如何检查；
5. 什么时候暂停；
6. 什么时候升级给 iS-Core。

14.3 必须保留的判断句

外部执行体不是项目负责人；外部执行体必须接收清晰任务包，并按输入、边界、输出、质量门和返回格式执行。

14.4 建议表格

表 1｜执行包标准字段

字段	说明
Mission Name	任务名称
Background	背景
Goal	目标
Input Materials	输入材料
Scope	执行范围
Non-Goals	不做事项
Output Requirements	输出要求
File Naming	文件命名
Version Strategy	版本策略
QA Criteria	质量标准
Pause Conditions	暂停条件
Return Format	返回格式
Review Items	待裁决项

表 2｜常见执行包类型

类型	适用对象
Manus Handoff Package	文件工程、页面、PPT、GitHub 整理
Codex Execution Package	代码实现、测试、脚本
Claude Code Package	工程审查、代码库理解
Kimi Research Package	中文长资料、行业 / 政策 / 投标材料
Python Automation Package	表格、清洗、渲染、计算
ChatGPT Structuring Package	结构推演、文档主稿、审校

14.5 上位引用关系

继承 Synexa Task Room Orchestrator、iS-Matrix、外部 Agent 执行包机制。

14.6 质量门

本章通过条件：

* 执行包字段完整；
* 明确外部 Agent 边界；
* 明确暂停和回流机制；
* 可直接转模板。

⸻

15. CH 09｜小步快跑与快速试错机制

15.1 章节目标

定义什么是可控试错，如何用最小闭环验证方向，而不是盲目做大系统。

15.2 核心问题

本章必须回答：

1. 什么叫最小闭环；
2. 什么可以试错；
3. 什么不能试错；
4. 试错如何记录；
5. 试错如何复盘；
6. 试错结果如何进入资产库。

15.3 必须保留的判断句

小步快跑不是无边界试错，而是在明确方向、风险和记录机制之后，用最小闭环验证真实世界反馈。
没有记录、没有复盘、没有回流的试错，只是消耗，不是学习。

15.4 建议表格

表 1｜Trial Loop 标准字段

字段	说明
Trial ID	试错编号
Goal	验证目标
Scope	范围
Boundary	边界
Risk Level	风险
Minimum Loop	最小闭环
Observation	观察指标
Result	结果
Decision	Continue / Revise / Pause / Escalate
Asset Destination	资产归位

表 2｜试错动作结论

动作	含义
Continue	继续扩大验证
Revise	修正路径后继续
Pause	暂停等待条件
Escalate	升级至 Core / SCO / Matrix / PCS

15.5 上位引用关系

继承 V3.10 的 OODA-PER、Experience Asset、Project-to-Skill 与人智风险权限机制。

15.6 质量门

本章通过条件：

* 区分可试错与不可试错；
* 试错有记录模板；
* 试错结果能回流资产；
* 不鼓励无序快跑。

⸻

16. CH 10｜问题、异常与经验沉淀机制

16.1 章节目标

建立问题从出现到归类、处理、复盘、资产沉淀的机制。

16.2 核心问题

本章必须回答：

1. 问题如何分类；
2. 异常如何归因；
3. 处理动作如何记录；
4. 经验如何沉淀；
5. 哪些进入 Pattern / Exception / Rule / Field / Judgment；
6. 哪些进入 SOP / Skill / DE。

16.3 必须保留的流程

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

16.4 建议表格

表 1｜问题分类表

问题类型	示例	资产方向
任务问题	责任不清、节点遗漏	Pattern / Field
工具问题	工具输出失真	Exception / Rule
数据问题	字段缺失、格式不一	Field / Rule
规则问题	判断标准不清	Rule / Judgment
代码问题	脚本失败、页面错误	Exception / SOP
现场问题	出品延误、服务异常	Exception / Pattern
供应问题	缺货、涨价、替代	Rule / Exception
人员问题	排班缺口、职责模糊	Pattern / Field
财务问题	成本异常、结算不清	Rule / Field
判断问题	取舍依据不足	Judgment

表 2｜经验资产类型

资产类型	核心字段
Pattern Asset	场景、对象、流程、角色、输入、输出、成功条件
Exception Asset	异常类型、发生环节、触发信号、处理动作、复盘
Rule Asset	规则名称、触发条件、执行动作、例外情况
Field Asset	字段名称、类型、来源、质量要求
Judgment Asset	判断场景、判断人、价值依据、风险权衡、裁决理由
SOP	操作流程、适用范围、责任角色
Skill	触发条件、输入、步骤、工具、质量门
DE Candidate	长期职责、授权边界、运行频率

16.5 上位引用关系

继承 V3.10 的 CH22 经验资产库与字段策略。

16.6 质量门

本章通过条件：

* 问题分类完整；
* 经验资产类型清晰；
* 能转化为模板；
* 能服务 GitHub / PCS / iS-Cortex。

⸻

17. CH 11｜Project-to-Skill 数智蒸馏机制

17.1 章节目标

定义真实项目如何转化为 SOP、Skill、Agent 配置、Digital Employee、Nex·EC 模块和经验资产。

17.2 核心问题

本章必须回答：

1. 什么样的项目经验值得蒸馏；
2. 如何识别对象；
3. 如何抽取规则；
4. 如何归档异常；
5. 如何模板化；
6. 如何 Skill 化；
7. 何时进入 Digital Employee 或 Engine Module。

17.3 必须保留的流程

真实项目运行
  ↓
对象识别
  ↓
规则抽取
  ↓
异常归档
  ↓
模板化
  ↓
Skill 化
  ↓
Agent / DE 配置
  ↓
Nex·EC 模块候选
  ↓
经验资产库

17.4 建议表格

表 1｜Project-to-Skill 蒸馏表

步骤	输入	输出
真实项目运行	项目任务 / 现场数据	真实样本
对象识别	用户、菜品、订单、岗位、供应商	对象清单
规则抽取	成功 / 失败案例	规则条目
异常归档	异常记录	Exception Asset
模板化	字段 / 流程 / 判断	SOP / Template
Skill 化	高频能力	Skill
Agent 配置	稳定任务角色	Agent / DE
引擎化	可模块化功能	Nex·EC Candidate

17.5 上位引用关系

继承 V3.10 的 CH21 Project-to-Skill、CH23 Skill 化候选清单、CH22 Experience Asset。

17.6 质量门

本章通过条件：

* 项目到 Skill 的路径清晰；
* 不把 Skill 当普通文档；
* 能服务 Nex₂U / 番医 / 后续项目台。

⸻

18. CH 12｜人智决策与风险权限

18.1 章节目标

定义哪些任务可以机器执行，哪些必须人审，哪些必须上升 Core。

18.2 核心问题

本章必须回答：

1. 不同风险等级如何定义；
2. 机器在不同风险等级中的权限；
3. 人类在何时必须介入；
4. 什么是退回修正；
5. 什么是 Core 升级；
6. 如何形成 Judgment Asset。

18.3 必须保留的判断句

通过不是唯一出口，退回修正是人类保留真实控制权的关键路径。
越是高风险、强不确定、涉及外部承诺或责任承担的事项，越不能绕过人智裁决。

18.4 建议表格

表 1｜风险权限表

风险等级	机器权限	人智要求	记录要求
Low	可建议并自动执行	事后抽查	自动记录
Medium	可生成方案与建议	责任人审核	记录审核人
High	只可推演与建议	Judgment Holder 裁决	记录权衡理由
Critical / Red	不得自动执行	Core / 指定负责人确认	完整决策记录

表 2｜升级触发条件

触发条件	升级对象
改变全局基线	iS-Core
改变项目定位	iS-Core / PCS
涉及对外承诺	Judgment Holder
涉及医疗 / 财务 / 法律责任	Core / 指定负责人
工具输出冲突	Matrix / Hub
项目资源冲突	Core / PCS

18.5 上位引用关系

继承 V3.10 的 Human-Machine Decision Loop、人智退回修正环、Risk-Based Human-Machine Decision Rights。

18.6 质量门

本章通过条件：

* 风险等级明确；
* 机器权限边界明确；
* 人智裁决机制明确；
* 能沉淀 Judgment Asset。

⸻

19. CH 13｜面向 Nex₂U 的应用示范

19.1 章节目标

用 Nex₂U 作为 DIC 的首个应用样板，说明 DIC 如何进入真实业务。

19.2 核心问题

本章必须回答：

1. 为什么 Nex₂U 是首个样板；
2. DIC 如何服务 Nex₂U Step 4；
3. Nex₂U 最小闭环是什么；
4. 哪些任务可转 Skill；
5. 哪些字段可进入后续项目台。

19.3 必须保留的判断句

Nex₂U 当前关键不是先做漂亮前端，而是跑通规则、菜品、订单、履约、供应、反馈和经验沉淀的最小闭环。

19.4 必须保留的最小闭环

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

19.5 建议表格

表 1｜Nex₂U 最小闭环节点

节点	输出	对应引擎
用户需求	用户标签	Nex2U
营养规则	规则库	NuStā / Nex2U
菜品数据	菜品字段	NexChef
点餐原型	用户入口	NexChef
厨房履约	出品任务	NexChef / NexOps
供应备货	原料需求	NexSply
反馈记录	反馈表	NexLens / iS-Cortex
复盘	资产 / Skill	Project-to-Skill

表 2｜首批 Skill 候选

Skill	来源
营养规则转译 Skill	医学 / 营养建议
菜品营养结构化 Skill	菜品 / 原料数据
供应替代策略 Skill	缺货 / 成本 / 品质
现场异常处理 Skill	运营异常
反馈复盘 Skill	用户 / 现场 / 供应反馈

19.6 上位引用关系

继承 Nex₂U PCS、V3.10 的 Nex2U / NexChef / NexSply / NexLens / iS-Cortex / Project-to-Skill。

19.7 质量门

本章通过条件：

* Nex₂U 不被写成泛案例；
* 能直接服务 Step 4 协同架构映射；
* 最小闭环可执行；
* Skill 候选明确。

⸻

20. CH 14｜阶段路线图

20.1 章节目标

定义 DIC 从 V0.1 到运行化的阶段路线。

20.2 核心问题

本章必须回答：

1. 0-30 天做什么；
2. 30-90 天做什么；
3. 90-180 天做什么；
4. 什么时候进入 GitHub 治理；
5. 什么时候进入番医功能台；
6. 什么时候升 V1.0。

20.3 建议表格

表 1｜DIC 阶段路线

阶段	目标	输出
0-30 天	建立 DIC 主源与最小协同机制	DICB、模板、执行包
30-90 天	围绕 Nex₂U / 番医跑最小闭环	任务台、餐食台、人力台、反馈资产
90-180 天	扩展 SOP / Skill / Registry	Tool Registry、Skill Registry、Experience Asset
180 天后	形成稳定运行基线	DIC V1.0

表 2｜阶段优先级

优先级	事项
P0	DIC 主源完成、HTML 输出、基础模板
P1	GitHub 治理、项目台机制、番医三台
P2	Tool / Agent / Skill Registry
P3	系统化后台、小程序、自动化集成

20.4 上位引用关系

继承 V3.10 的发展路径、Project-to-Skill、Experience Asset、工具选型与全域治理。

20.5 质量门

本章通过条件：

* 路线有时间分层；
* 不承诺一步到位；
* GitHub 与番医被放在 DIC 主源之后；
* 可小步快跑。

⸻

21. CH 15｜DIC 版本治理与后续升级

21.1 章节目标

定义 DIC Baseline 的版本策略、升级条件、反向补丁机制和 GitHub 同步机制。

21.2 核心问题

本章必须回答：

1. V0.1 是什么状态；
2. 什么时候升 V0.2；
3. 什么时候升 V1.0；
4. 哪些变化需要回写 V3.10；
5. 哪些变化只在 DIC 内部更新；
6. 哪些变化进入 PCS / SOP / Skill。

21.3 建议表格

表 1｜DIC 版本路径

版本	状态	触发条件
V0.1	Working Draft	首版主源完成
V0.2	Pilot Version	Nex₂U / 番医试运行后
V0.3	Registry Version	Tool / Agent / Skill Registry 建立
V0.5	Operational Beta	多项目使用后
V1.0	Stable Baseline	经 2-3 个项目验证稳定

表 2｜更新归位规则

更新类型	归位
公司定位变化	V3.10
DIC 协同机制变化	DIC Baseline
项目状态变化	PCS
操作流程稳定	SOP
高频能力封装	Skill
工具评估变化	Tool Registry
经验沉淀	Experience Asset

21.4 上位引用关系

继承 V3.10 的 SSOT 升级治理机制、版本记录、完整交付标准与 GitHub 回写原则。

21.5 质量门

本章通过条件：

* 版本策略清楚；
* 归位规则清楚；
* 不轻易升级 V3.10；
* 所有关键更新可追踪。

⸻

22. Appendix A｜AI / Agent / Tool Capability Matrix

22.1 目标

提供 AI / Agent / Tool 能力矩阵，作为后续 Tool Registry 的基础。

22.2 必须包含字段

字段	说明
Tool Name	工具名称
Tool Type	类型
Best Use	最佳用途
Forbidden Use	禁用场景
Required Input	所需输入
Output Type	输出类型
QA Gate	质量门
Owner	责任人
Status	状态
Registry Destination	登记位置

22.3 质量门

* 可直接转 CSV / JSON；
* 不写成主观推荐；
* 有禁用边界。

⸻

23. Appendix B｜Task Routing Table

23.1 目标

建立任务归位判断表，供人类和 Agent 快速判断任务入口。

23.2 必须包含字段

字段	说明
Task Type	任务类型
Trigger	触发条件
Target Workspace	目标工作空间
Required Output	输出
Risk Level	风险
Feedback Destination	回流位置

⸻

24. Appendix C｜Task Node Template

24.1 目标

提供可复用任务节点模板。

24.2 必须包含字段

同 CH05 Task Node 标准字段。

⸻

25. Appendix D｜Execution Package Template

25.1 目标

提供外部执行包模板。

25.2 必须包含版本

1. Manus 执行包；
2. Codex 执行包；
3. Claude Code 执行包；
4. Kimi 研究包；
5. Python 自动化包；
6. ChatGPT 结构推演包。

⸻

26. Appendix E｜Trial Loop Record Template

26.1 目标

提供试错记录模板。

26.2 必须包含字段

字段	说明
Trial ID	试错编号
Hypothesis	假设
Minimum Action	最小动作
Boundary	边界
Metric	指标
Result	结果
Decision	Continue / Revise / Pause / Escalate
Asset Destination	资产归位

⸻

27. Appendix F｜Experience Asset Capture Template

27.1 目标

提供经验资产捕捉模板。

27.2 必须覆盖

1. Pattern Asset；
2. Exception Asset；
3. Rule Asset；
4. Field Asset；
5. Judgment Asset；
6. SOP Candidate；
7. Skill Candidate；
8. Digital Employee Candidate；
9. Engine Module Candidate。

⸻

28. Appendix G｜Machine-Readable Index

28.1 目标

提供机器可读索引，方便后续 RAG、Agent 调用、GitHub 检索与自动化渲染。

28.2 建议字段

字段	说明
concept_id	概念 ID
zh_name	中文名
en_name	英文名
definition	定义
source_chapter	来源章节
related_concepts	关联概念
output_type	输出类型
update_rule	更新规则

⸻

29. Appendix H｜Version Register & Change Log

29.1 目标

记录 DIC Baseline 的版本变化。

29.2 建议表格

Version	Date	Change Summary	Impact Scope	Owner
V0.1	2026-06-27	首版 BBLx 章节展开逻辑	DIC Baseline	iS-Core

⸻

30. DICB 正式 Markdown 主源生产要求

基于本 BBLx，下一步 DICB Markdown 主源必须满足：

1. 不只给提纲；
2. 不只给增补包；
3. 每章有正式正文；
4. 每章有必要表格；
5. 每章有判断句；
6. 每章有边界说明；
7. 每章能支持机器解析；
8. 每章能服务后续 GitHub / PCS / SOP / Skill / Experience Asset；
9. 全文保持 V0.1 工作版状态；
10. 不直接改写 V3.10，只继承展开。

⸻

31. DIC·BBL 质量门

本文件通过条件如下：

检查项	通过标准
章节完整性	覆盖 CH(-1) 至 CH15 与 Appendix A-H
上下位关系	明确继承 V3.10，不替代 V3.10
机制完整性	路径、节点、工具、试错、经验沉淀均已展开
表格可转化	关键机制均可转 CSV / JSON / Base
应用导向	Nex₂U 作为首个样板已展开
后续生产	可直接指导 DICB Markdown 主源生产
边界控制	不提前进入 GitHub 全仓治理和番医三台
文件治理	明确 md 主源、py 渲染、html 阅读版

⸻

32. BBLx 结论

本 BBLx 确认：

1. Synexa_DIC_Baseline_BBM_V0.1.md 已作为 Step2 蓝图文件；
2. 本文件 Synexa_DIC_Baseline_BBLx_V0.1.md 是 Step3 章节展开逻辑；
3. 下一步应进入 Step4，生产 Synexa_DIC_Baseline_V0.1.md；
4. GitHub 全仓整理可后置，待 DIC 主源完成后再统一规划；
5. 番医任务台、餐食台、人力台应在 DIC 主源完成后启动，避免先执行后补规则；
6. DIC Baseline 的主轴是：共识、方向、任务、路径、节点、分工、工具、执行、质检、回流、迭代；
7. DIC Baseline 的核心价值是：让人和机器在真实项目中形成共同协同秩序，并把问题、规则、判断和经验沉淀为可复用资产。

最终锚定句：

V3.10 定义超智的总图，DIC Baseline 定义超智的走法。
BBM 定蓝图，BBLx 定章节逻辑，DICB 定正式主源。
先让规则成文，再让 GitHub 和项目台按规则运行。