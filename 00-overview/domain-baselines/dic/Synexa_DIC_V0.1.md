<!-- COVER
topline: SYNEXA · DIC BASELINE · INTERNAL SSOT · DOMAIN BASELINE
title: 超智科技·数智协同基线
en: Synexa Digital-Intelligence Collaboration Baseline V0.1
sub: Defining the operating logic of human-AI collaboration within the Synexa ecosystem.
quote: 先让规则成文，再让 GitHub 和项目台按规则运行。V3.10 定义超智的总图，DICB 定义超智的走法。
stat_override:
  - 13 | 质量门 | Quality Gates
  - 6 | 触发条件 | Trigger Conditions
  - 10 | 路径节点 | Path Nodes
  - 4 | 协同主体 | Agent Types
  - 3 | 核心机制层 | Core Mechanisms
-->

# 超智科技·数智协同基线｜DICB V0.1


---

Synexa Digital-Intelligence Collaboration Baseline V0.1

DICB V0.1

文件类型：Domain / Operational Baseline｜专题运行基线
中文正式名：超智科技·数智协同基线
英文正式名：Synexa Digital-Intelligence Collaboration Baseline
对外轻主名称：DICB
当前版本：V0.1
当前状态：Working Draft / Markdown Master Source
上位文件：超智科技认知基线 V3.10
维护入口：智核中枢·iS-Core
首个应用样板：Nex₂U / 番医项目功能台预备
文件主源建议名：Synexa_DIC_Baseline_V0.1.md
后续输出：Synexa_DIC_Baseline_Render_V0.1.py / Synexa_DIC_Baseline_V0.1.html
生产链条：DIC·BBMap → DIC·BBL → DICB
当前阶段：Step4|DICB md|Markdown 主源

⸻

## CH(-1)｜Human-Machine-Digital Baseline Protocol

人机数智共识协议

### CH(-1).1 文件共识

《超智科技·数智协同基线｜DICB》是一份面向人类协作者、AI 智能体、数字工具、代码执行体、业务系统、项目执行体与组织经验资产共同读取的运行基线文件。

它不是普通说明书，也不是 AI 工具清单，而是用于统一以下事项的共识协议：

1. 人如何设定方向；
2. 机器如何执行任务；
3. Agent 如何接收边界；
4. 工具如何被调用；
5. 系统如何承载流程；
6. 项目如何形成闭环；
7. 问题如何被复盘；
8. 经验如何沉淀为资产；
9. 资产如何回流到 SOP、Skill、Agent Matrix、PCS 与 Master SSOT。

DICB 的目标不是把所有 AI 工具写得最多，而是在最小冗余下统一人类判断、机器执行、系统调度与经验沉淀的协同秩序。

⸻

### CH(-1).2 文件主源规则

本文件采用 Markdown 作为事实主源。

Markdown 是事实主源；
Python 是渲染工具；
HTML 是阅读输出；
PDF 是归档形态；
JSON / YAML 是机器索引；
ZIP 是完整交付包。

所有事实性修改必须回到 Markdown 主源，不应在 HTML、PDF 或临时聊天记录中直接修改事实内容。

| 文件形态 | 作用 | 是否事实主源 |
|---|---|---|
| Markdown | 正式内容主源 | 是 |
| Python | 渲染脚本 | 否 |
| HTML | 阅读版 / 检查版 | 否 |
| PDF | 后续归档版 | 否 |
| JSON / YAML | 机器索引 / 字段映射 | 否，除非专门声明 |
| ZIP | 完整交付包 | 否 |

⸻

### CH(-1).3 人机共读原则

本文件需要同时服务四类读者。

| 读者类型 | 读取目标 | 使用入口 |
|---|---|---|
| Human | 理解协同规则、任务路径、责任边界 | Executive Summary / CH01-CH05 |
| Machine | 解析字段、节点、路径、状态 | Appendix G / 表格 / 机器锚点 |
| Agent | 按任务归位、执行包、质量门推进 | CH03 / CH08 / Appendix D |
| Organization | 用于项目治理、经验沉淀、版本升级 | CH10 / CH11 / CH15 |

因此，本文件的写法必须同时满足：

1. 人类可以读懂；
2. 机器可以解析；
3. Agent 可以调用；
4. 项目可以执行；
5. 经验可以沉淀；
6. GitHub 可以回写；
7. 后续可以渲染为 HTML / PDF；
8. 可拆分为 SOP、Skill、Registry、PCS Patch 与 Experience Asset。

⸻

Executive Summary｜执行摘要

ES.1 为什么需要 DICB

超智科技正在从单点项目推进，进入多项目、多工具、多 Agent、多文件、多业务引擎协同的阶段。

在这个阶段，如果没有统一的数智协同基线，容易出现：

1. 人和机器理解不一致；
2. 不同工具各自执行，无法回流；
3. 项目任务缺少路径和节点；
4. 文件版本散落在聊天记录、HTML、PDF、临时表格中；
5. Agent 快速执行但偏离上位基线；
6. 经验没有沉淀为 SOP、Skill、Agent 或项目资产；
7. GitHub、PCS、Context OS 与 Master SSOT 之间缺少清晰同步关系。

因此，DICB 的核心作用，是将人的方向、机器的执行、系统的反馈、项目的推进和经验的沉淀，组织成可执行、可追踪、可复盘、可升级的协同秩序。

⸻

ES.2 DIC 与《超智科技认知基线》的关系

《超智科技认知基线》定方向、结构与边界；《超智科技·数智协同基线｜DICB》定路径、节点与协同动作。

前者是总图，后者是走法；前者让体系不漂，后者让行动不散。

| 维度 | 超智科技认知基线 V3.10 | DICB |
|---|---|---|
| 核心问题 | 超智是什么 | 人和机器如何协同把事做成 |
| 文件性质 | Master SSOT | 数智协同运行基线 |
| 关注重点 | 定位、架构、能力、项目组合 | 任务、路径、节点、试错、经验 |
| 作用 | 统一认知 | 统一行动 |
| 更新逻辑 | 审慎升级 | 小步迭代 |
| 输出方向 | 总图与边界 | 走法与机制 |

DICB 不替代《超智科技认知基线 V3.10》，而是在其上位框架下，进一步展开人、AI、Agent、工具、代码、业务系统与真实项目之间的协同运行机制。

⸻

ES.3 DIC 的核心功能

DICB 至少承担十项核心功能：

1. 统一数智协同定义；
2. 明确人、AI、Agent、工具、代码、系统、项目之间的角色关系；
3. 建立任务从目标到交付的标准路径链条；
4. 建立任务归位机制；
5. 建立不同任务类型的节点模板；
6. 建立工具与 Agent 的调用原则；
7. 建立外部执行包机制；
8. 建立小步快跑与快速试错机制；
9. 建立问题 / 异常 / 经验沉淀机制；
10. 建立从任务到 SOP、Skill、Digital Employee、Experience Asset 的转化机制。

⸻

ES.4 DIC 的主流程

DICB 的标准协同路径如下：

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

这条路径不是为了增加流程，而是为了让每一次执行都能被理解、被分派、被检查、被复盘、被沉淀。

⸻

ES.5 首个应用样板

DICB 的首个应用样板是 Nex₂U。

Nex₂U 涉及营养规则、用户需求、菜品结构、点餐履约、供应协同、现场执行、数据反馈和经验沉淀，天然适合作为数智协同的真实验证场。

Nex₂U 当前不应先追求完整大系统，而应先跑通最小闭环：

点餐体验 → 生产保障 → 服务运维 → 采购支持 → 人力管理 → 财务管控 → 经验沉淀

详见 CH13.3 最小闭环节点表。

⸻

## CH 00｜文件定位与使用边界

### CH00.1 文件身份

《超智科技·数智协同基线｜DICB》是《超智科技认知基线 V3.10》之下的专题运行基线。

它的核心任务不是重新定义超智，而是回答：

在超智已经有公司定位、系统架构、项目组合和能力体系的前提下，人、机器、工具、Agent、代码、业务系统与真实项目如何协同把事情做成？

| 项目 | 定义 |
|---|---|
| Document Type | Domain / Operational Baseline |
| Chinese Name | 超智科技·数智协同基线 |
| English Name | Synexa Digital-Intelligence Collaboration Baseline |
| Short Name | DICB |
| Version | V0.1 |
| Upper Source | Synexa Company Intro V3.10 |
| Maintainer | iS-Core |
| Implementation Roles | iS-Matrix / Manus / Codex / Project PCS |
| First Application | Nex₂U |

⸻

### CH00.2 不替代原则

DICB 不替代以下文件或机制：

| 不替代对象 | 原因 |
|---|---|
| 超智认知基线（SCI V3.10） | `Synexa_Company_Intro_V3.10.md` 是公司级最高认知源，DICB 在其上位框架下展开协同运行机制 |
| Context OS | Context OS 记录动态状态与待同步事项 |
| PCS | PCS 管具体项目执行状态 |
| SOP | SOP 管稳定流程 |
| Skill | Skill 管可复用能力封装 |
| GitHub Registry | Registry 管索引与文件状态 |
| Human Judgment | 高风险决策仍需人智裁决 |

DIC 定义协同运行规则；具体项目状态仍由 PCS 管理，具体操作流程由 SOP 固化，可复用能力由 Skill 承载。

⸻

### CH00.3 适用对象

DICB 适用于：

1. iS-Core：用于裁决任务归位、基线关系与版本治理；
2. iS-SCO：用于战略推演、路径判断与复杂任务拆解；
3. iS-Matrix：用于生产 SOP、Skill、模板、执行包；
4. iS-Hub：用于维护 Tool / Agent Registry；
5. iS-Lab：用于未成熟想法的最小验证；
6. PCS 项目组：用于项目任务、节点、反馈和经验沉淀；
7. 外部执行体（对话型 AI / 代码执行平台 / 自动化集成）：用于接收结构化执行包，具体工具分工详见 CH07.2；
8. 人类项目负责人：用于判断方向、审核结果、裁决风险；
9. GitHub / Registry 管理者：用于文件归位、版本追踪、索引维护。

⸻

### CH00.4 不适用对象

DICB 不适用于：

1. 对外客户宣传；
2. 投资人版路演；
3. 单个产品介绍；
4. 单次项目报价；
5. 临时任务备忘；
6. 纯 AI 工具排行；
7. 纯代码开发说明；
8. 纯设计视觉规范；
9. 法律、医疗、财务责任文件。

如需面向外部表达，应由 iS-Synexa 或对应项目组基于 DIC 进行转译，不应直接以本文件作为对外文件。

⸻

## CH 01｜数智协同总定义

### CH01.1 正式定义

数智协同，是指在人的方向设定与责任承担之下，将 AI、Agent、数据、代码、工具、业务系统、供应网络、现场执行与经验资产组织成可执行、可反馈、可优化的协同运行机制。

它不是单纯 AI 使用，不是自动化替代人，也不是做一个软件系统。

它的核心是：

人设方向；
机器出方案；
系统组织任务；
Agent 执行动作；
工具提供能力；
项目验证结果；
经验沉淀资产；
下一轮持续优化。

⸻

### CH01.2 数智协同不是什么

| 误解 | 正确理解 |
|---|---|
| AI 工具使用 | 数智协同运行机制 |
| 自动化替代人 | 人智定向 + 数智执行 + 人智裁决 |
| 做一个系统 | 形成可迭代的协同秩序 |
| 项目管理表 | 任务、节点、工具、反馈、经验闭环 |
| 模型能力展示 | 真实场景中的可交付能力 |

数智协同不是让机器替代人，而是让人的方向、机器的执行、系统的反馈和经验的沉淀形成持续进化的协同秩序。

⸻

### CH01.3 数智协同的构成要素

| 要素 | 作用 |
|---|---|
| 人智判断 | 方向、价值、责任、裁决 |
| AI / LLM | 理解、推演、生成、结构化 |
| Agent | 任务执行与角色化推进 |
| Python / Code | 计算、清洗、自动化、文件生成 |
| 业务系统 | 承接流程、状态、履约 |
| 供应网络 | 真实资源与履约能力 |
| 现场执行 | 将方案变成真实服务 |
| 经验资产 | 将一次执行变成长期能力 |

工具可以借力，判断必须自有；代码可以生成，规则必须沉淀；Agent 可以执行，责任必须归人。

⸻

### CH01.4 DIC 与 Synexa iS 的关系

Synexa iS 是组织级智能操作系统，是超智体系中负责治理、认知、规则、能力、Agent、项目与经验资产协同的系统承载。

DICB 是 Synexa iS 在“数智协同运行层”的专题基线。

两者关系如下：

Synexa iS
  ↓
定义系统如何组织能力、任务、Agent、项目与经验资产
DICB
  ↓
定义人、AI、Agent、工具、代码、系统与真实项目如何协同推进任务

⸻

## CH 02｜人、机器与系统的角色关系

### CH02.1 主体与能力体

DICB 中，必须区分主体与能力体。

主体拥有目标、判断与责任；能力体响应目标、执行任务并返回结果。

| 角色 | 定义 | 可做 | 不可做 |
|---|---|---|---|
| Human Judgment | 方向、价值、责任与裁决主体 | 定方向、审方案、承担责任 | 被机器替代 |
| AI / LLM | 认知发动机 | 理解、生成、推演、结构化 | 独立承担高风险决策 |
| Agent | 任务执行单元 | 按边界执行任务 | 自行定义目标 |
| Tool | 能力工具 | 提供特定功能 | 替代系统治理 |
| Python / Code | 计算与自动化手臂 | 数据处理、脚本、渲染 | 价值判断 |
| Business System | 业务承载系统 | 状态、流程、记录、履约 | 自行决定战略 |
| SOP | 稳定流程 | 规范做法 | 替代判断 |
| Skill | 可复用能力 | 执行高频能力 | 替代责任主体 |
| Digital Employee | 长期履职角色 | 持续承担标准化职责 | 超出授权范围行动 |
| Experience Asset | 经验沉淀 | 复用判断、规则、异常 | 停留在散乱记录 |

⸻

### CH02.2 人智判断 Human Judgment

人智判断，是人在方向、价值、责任、裁决、例外处理和高风险取舍中的不可替代作用。

人智不是系统补丁，而是方向锚与责任锚。

DIC 中的人智至少承担五类职责：

1. 定义目标；
2. 设定边界；
3. 判断优先级；
4. 裁决高风险事项；
5. 承担责任。

机器可以提供方案、选项、对比、风险提示与执行结果，但不能替代人类承担最终责任。

⸻

### CH02.3 AI / LLM

AI / LLM 是认知发动机，适合理解、生成、推演、总结、结构化与草案生成。

适合：

1. 文档理解；
2. 方案生成；
3. 结构化整理；
4. 任务拆解；
5. 会议纪要；
6. SOP 草案；
7. 规则抽取；
8. 执行包生成；
9. 复盘归纳。

不适合：

1. 最终战略裁决；
2. 医疗责任判断；
3. 财务付款动作；
4. 对外合同承诺；
5. 供应商最终选择；
6. 未经审核的正式发布。

⸻

### CH02.4 Agent

Agent 是带有目标、工具、边界、上下文和输出要求的任务执行单元。

Agent 不是万能助手，而是角色化执行体。

DIC 中应区分：

1. 研究 Agent；
2. 结构 Agent；
3. 代码 Agent；
4. 执行 Agent；
5. 审校 Agent；
6. 回流 Agent；
7. 长期数字员工。

Agent 必须接受任务边界、输入材料、输出要求、暂停条件和质量门约束。

⸻

### CH02.5 SOP / Skill / Agent / Digital Employee 区分

| 类型 | 核心问题 | 成熟条件 |
|---|---|---|
| SOP | 标准流程怎么做 | 流程稳定、可培训 |
| Skill | 高频能力怎么复用 | 可触发、可封装、可验证 |
| Agent | 谁来执行一个任务 | 有目标、工具、边界 |
| Digital Employee | 谁长期承担一类职责 | 稳定职责 + 持续运行 + 质量门 |

Skill 不是文档说明，而是可触发、可复用、可组合、可审计的能力资产。

⸻

## CH 03｜任务归位机制

### CH03.1 为什么需要任务归位

任务不先归位，就不应直接执行；未归位的执行，往往会造成重复劳动、责任模糊和经验流失。

DIC 的任务归位不是行政分工，而是为了确保每个任务都有正确的认知层级、执行角色、质量门和回流位置。

⸻

### CH03.2 任务归位类型

| 归位类型 | 触发条件 | 典型输出 |
|---|---|---|
| iS-Core | 全局基线、项目归位、战略裁决、优先级冲突 | 裁决、Step 0A、全局同步 |
| iS-SCO | 战略推演、路径判断、复杂取舍 | 策略推演、选项评估 |
| iS-Matrix | SOP、模板、Skill、基线文件生产 | 文档资产、规程、模板 |
| iS-Hub | 工具、Agent、平台、外部案例评估 | Tool Registry、情报清单 |
| iS-Lab | 未成熟想法、轻量验证 | 可行性判断、立项建议 |
| PCS | 已归属具体项目的执行推进 | 项目任务、里程碑、复盘 |
| External Agent | 需要文件操作、代码、页面、资料整理 | 执行包、文件产出 |
| New Project | 出现新业务对象、长期机制或独立项目域 | 项目最小定义、PCS |

⸻

### CH03.3 任务归位输出字段

| 字段 | 说明 |
|---|---|
| Task ID | 任务编号 |
| Task Name | 任务名称 |
| Trigger | 触发原因 |
| Routing Decision | 归位结论 |
| Owner | 主责角色 |
| Support Role | 协作角色 |
| Required Input | 输入材料 |
| Expected Output | 输出 |
| QA Gate | 质量门 |
| Feedback Destination | 回流位置 |

每一个任务必须知道：

1. 归哪里；
2. 谁负责；
3. 谁支持；
4. 用什么工具；
5. 输出什么；
6. 回到哪里；
7. 是否可能沉淀为资产。

⸻

### CH03.4 新项目触发条件

当一个任务具备以下任一特征，应考虑进入 Step 0A 项目最小定义：

1. 出现新的业务对象；
2. 出现长期执行场景；
3. 出现独立项目目标；
4. 出现跨项目资源调度；
5. 出现可持续收入或交付机会；
6. 出现需要单独 PCS 管理的任务簇；
7. 出现可沉淀为独立引擎或模块的能力。

⸻

## CH 04｜标准协同路径

### CH04.1 全局主流程

DIC 的标准协同路径如下：

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

DIC 的标准协同路径，不是为了增加流程，而是为了让每一次执行都能被理解、被分派、被检查、被复盘、被沉淀。

⸻

### CH04.2 路径展开

| 阶段 | 核心动作 | 主责 | 输出 |
|---|---|---|---|
| 目标提出 | 提出任务意图 | 人 / 项目负责人 | 初始目标 |
| 人智定向 | 明确方向、边界、成功标准 | Judgment Holder | 定向说明 |
| 任务归位 | 判断归属与路径 | iS-Core / DIC | Routing Decision |
| 路径推演 | 形成行动路线 | SCO / Matrix | 路径草案 |
| 节点拆解 | 拆成任务节点 | Matrix / PCS | Node List |
| 角色分工 | 分配人、Agent、工具 | PCS / Task Room | Role Map |
| 工具调用 | 生成执行包 | Matrix / Manus / Codex | Handoff Package |
| 执行交付 | 完成任务 | 人 / Agent / 工具 | Deliverable |
| 质量检查 | 检查内容、格式、风险 | QA Role | QA Result |
| 人智裁决 | 通过、退回、升级 | Judgment Holder | Decision Record |
| SSOT / PCS 回写 | 回写主源或项目账本 | Manus / PCS | Updated File |
| 经验沉淀 | 形成资产 | iS-Cortex / Matrix | Experience Asset |
| 下一轮优化 | 修正路径与规则 | Core / PCS | Patch / Version |

⸻

### CH04.3 人智定向

人智定向必须至少回答：

1. 为什么做；
2. 做到什么程度；
3. 不做什么；
4. 成功标准是什么；
5. 风险边界在哪里；
6. 谁承担最终责任；
7. 是否需要回写 Master SSOT / Context OS / PCS。

没有定向的任务，不应直接进入外部 Agent 执行。

⸻

### CH04.4 人智裁决

人智裁决包括：

1. 接受；
2. 退回；
3. 修正；
4. 暂停；
5. 升级；
6. 作废；
7. 归档；
8. 资产化。

通过不是唯一出口，退回修正是人类保留真实控制权的关键路径。

⸻

## CH 05｜任务节点设计机制

### CH05.1 任务节点定义

任务节点，是从目标到交付过程中可识别、可分派、可执行、可检查、可回流的工作单元。

任务节点不是普通待办事项。
它必须具备输入、动作、主责、工具、输出、质量门、风险等级与回流位置。

⸻

### CH05.2 Task Node 标准字段

| 字段 | 说明 |
|---|---|
| Node ID | 节点编号 |
| Node Name | 节点名称 |
| Path Stage | 所属路径阶段 |
| Project / Domain | 所属项目或领域 |
| Input | 输入 |
| Action | 执行动作 |
| Owner Role | 主责角色 |
| Support Role | 协作角色 |
| Tool / Agent | 可用工具或 Agent |
| Output | 输出 |
| QA Gate | 质量门 |
| Risk Level | 风险等级 |
| Status | 状态 |
| Feedback Destination | 回流位置 |
| Asset Candidate | 是否可沉淀资产 |

⸻

### CH05.3 节点状态枚举

| 状态 | 含义 |
|---|---|
| Draft | 待确认 |
| Ready | 可执行 |
| In Progress | 执行中 |
| Blocked | 阻塞 |
| Review | 待审核 |
| Returned | 退回修正 |
| Accepted | 已通过 |
| Archived | 已归档 |
| Assetized | 已资产化 |

⸻

### CH05.4 节点质量门

每个节点必须至少具备一个质量门。

常见质量门包括：

1. 输入是否完整；
2. 输出是否符合格式；
3. 是否与上位基线冲突；
4. 是否需要人智裁决；
5. 是否触发风险升级；
6. 是否可回写 PCS；
7. 是否可沉淀资产；
8. 是否需要版本记录。

⸻

## CH 06｜不同任务类型的节点模板

### CH06.1 战略推演任务节点

| 节点 | 输入 | 输出 | 主责 |
|---|---|---|---|
| 背景识别 | 事件 / 问题 / 机会 | 背景说明 | SCO |
| 目标确认 | 用户意图 | 战略目标 | Core / User |
| 约束识别 | 资源 / 时间 / 风险 | 约束清单 | SCO |
| 路径推演 | 目标与约束 | 选项与判断 | SCO |
| 人智裁决 | 推演结果 | 决策记录 | Core / Judgment Holder |
| 回写 | 决策结果 | Context / PCS / Log | Core / Manus |

⸻

### CH06.2 项目推进任务节点

| 节点 | 输入 | 输出 |
|---|---|---|
| 项目归位 | 任务目标 / 业务对象 | PCS / 项目定义 |
| 阶段确认 | 当前 Step / 阻塞项 | 阶段状态 |
| 任务拆解 | 阶段目标 | 任务列表 |
| 责任分配 | 任务列表 | Owner / Support |
| 执行追踪 | 任务状态 | 进度记录 |
| 阻塞处理 | Blocker | 处理路径 |
| 阶段复盘 | 执行结果 | 经验资产 |
| PCS 回写 | 复盘结果 | 更新 PCS |

⸻

### CH06.3 文档生产任务节点

| 节点 | 输入 | 输出 |
|---|---|---|
| BBMap | 目标与关系锚定 | 蓝图地图 |
| BBLx | BBMap | 章节展开逻辑 |
| md | BBLx | Markdown 主源 |
| py | md + 渲染规范 | 渲染脚本 |
| html | md + py | 阅读版 |
| QA | 全部输出 | 质检记录 |
| 回写 | 通过文件 | GitHub / Index |

⸻

### CH06.4 工具选型任务节点

| 节点 | 输入 | 输出 |
|---|---|---|
| 需求定义 | 业务目标 | 工具需求说明 |
| 候选搜集 | 需求说明 | 候选清单 |
| 初筛评分 | 候选清单 | 2-3 个候选 |
| PoC 验证 | 候选工具 | 最小验证结果 |
| 风险检查 | 验证结果 | 风险清单 |
| 归位登记 | 通过工具 | Tool Registry |
| 回流复盘 | 使用反馈 | Tool Review Asset |

⸻

### CH06.5 代码执行任务节点

| 节点 | 输入 | 输出 |
|---|---|---|
| 需求包 | 业务需求 | Codex / Claude Code Package |
| 仓库定位 | 文件路径 | 实施范围 |
| 代码实现 | 执行包 | 代码变更 |
| 测试验证 | 变更文件 | 测试结果 |
| 审查 | 测试结果 | Review Item |
| 合并 / 回写 | 通过结果 | GitHub 更新 |
| 经验沉淀 | 代码问题 | SOP / Skill / Exception |

⸻

### CH06.6 Nex₂U 业务任务节点

| 节点 | 输入 | 输出 |
|---|---|---|
| 用户需求识别 | 用户 / 患者 / 场景 | 需求标签 |
| 营养规则转译 | 医学 / 营养建议 | 规则条目 |
| 菜品数据结构化 | 菜品 / 原料 | 营养字段 |
| 菜单生成 | 规则 + 菜品 | 菜单方案 |
| 订单履约 | 用户选择 | 厨房任务 |
| 供应备货 | 菜单需求 | 原料需求 |
| 现场执行 | 出品 / 服务 | 状态记录 |
| 反馈采集 | 用户 / 现场反馈 | 反馈记录 |
| 经验沉淀 | 反馈 / 异常 | Asset / SOP / Skill |

⸻

### CH06.7 异常处理任务节点

| 节点 | 输入 | 输出 |
|---|---|---|
| 异常发现 | 现场 / 数据 / 工具反馈 | 异常记录 |
| 风险判断 | 异常记录 | 风险等级 |
| 临时动作 | 风险等级 | 处理动作 |
| 责任确认 | 处理动作 | Owner |
| 复盘归因 | 执行结果 | 原因分析 |
| 规则更新 | 复盘结论 | Rule / SOP |
| 资产沉淀 | 异常资料 | Exception Asset |

⸻

### CH06.8 外部 Agent 执行任务节点

| 节点 | 输入 | 输出 |
|---|---|---|
| 任务包生成 | 目标 / 材料 / 边界 | Handoff Package |
| Agent 执行 | 执行包 | 文件 / 代码 / 页面 |
| 返回反馈 | 执行结果 | Return Feedback |
| QA 检查 | 返回结果 | Review Item |
| 人智确认 | QA 结果 | 接受 / 退回 |
| 回写归档 | 确认结果 | GitHub / PCS |
| 资产化 | 执行经验 | SOP / Skill / Exception |

⸻

## CH 07｜AI / Agent / 工具能力归位

### CH07.1 工具归位原则

DIC 不是工具说明书，但必须定义工具的协同位置。

核心原则：

工具可以借力，判断必须自有。
模型可以替换，协同秩序不能漂移。
外部 Agent 只能执行任务包，不应直接接收模糊战略任务。

⸻

#### CH07.2 工具能力归位表

> 外部执行体按接入类型分组，具体产品为参考，不写死。产品迭代不影响分工逻辑。

| 接入类型 | 工具 / 平台 | DIC 角色 | 适合任务 | 禁止事项 |
|---|---|---|---|---|
| **对话型 AI · 中枢推演** | ChatGPT（GPT-4o/o1） | 中枢推演与结构化 | 战略整理、文件结构、执行包生成、审校、跨对话状态管理 | 替代最终 SSOT |
| **对话型 AI · 中枢推演** | Gemini（Google） | 多模态推演与搜索增强 | 需要实时信息、多模态输入、Google 生态集成的任务 | 单独裁决业务逻辑 |
| **对话型 AI · 长文处理** | Claude（Anthropic） | 长文档复核与结构对照 | 长文审校、结构对照、高密度内容分析 | 单独裁决业务 |
| **对话型 AI · 中文增强** | Kimi（Moonshot） | 中文资料初筛 | 长资料、政策、投标、供应商材料 | 最终裁决 |
| **对话型 AI · 中文增强** | 文心一言 / 通义千问 | 中文场景辅助 | 中文内容生成、本地化表达、国内合规场景 | 替代结构化推演 |
| **代码执行平台** | Manus | 文件工程与执行落地 | 页面、HTML、PPT、文件包、GitHub 整理、自动化脚本 | 自行改写上位定义 |
| **代码执行平台** | Codex（OpenAI） | 工程执行 | 代码、脚本、测试、API 集成 | 决定业务规则 |
| **代码执行平台** | Claude Code | 工程协作 | 代码库理解、大型开发任务、代码审查 | 替代产品判断 |
| **计算与自动化** | Python / 脚本 | 计算与数据处理 | 数据处理、渲染、表格、模型、批量操作 | 价值判断 |
| **自动化集成** | n8n / Zapier / Make | 流程自动化 | 触发器、跨系统数据同步、定时任务 | 自行定义业务目标 |
| **体系内能力** | Skill | 可复用能力资产 | 高频标准化任务 | 临时内容堆放 |
| **体系内能力** | Agent | 角色化任务执行体 | 带边界执行任务 | 自行定义目标 |
| **体系内能力** | Digital Employee | 长期履职角色 | 稳定职责持续运行 | 超授权行动 |

⸻

### CH07.3 工具调用基本规则

1. 模糊任务先回到 iS-Core / SCO / Matrix，不直接交给外部 Agent；
2. 工程任务必须有执行包；
3. 文档任务必须先有 BBMap / BBLx 或明确结构；
4. 高风险任务不能由工具直接完成；
5. 所有输出必须能回流；
6. 结果必须经过质量门；
7. 重要输出必须进入 GitHub / PCS / Registry；
8. 工具输出不得直接覆盖上位基线。

⸻

## CH 08｜执行包机制

### CH08.1 执行包定义

执行包，是将人智目标和系统任务转化为外部 Agent 或工具可执行指令的结构化任务包。

外部执行体不是项目负责人；外部执行体必须接收清晰任务包，并按输入、边界、输出、质量门和返回格式执行。

⸻

### CH08.2 执行包标准字段

| 字段 | 说明 |
|---|---|
| Mission Name | 任务名称 |
| Background | 背景 |
| Goal | 目标 |
| Input Materials | 输入材料 |
| Scope | 执行范围 |
| Non-Goals | 不做事项 |
| Output Requirements | 输出要求 |
| File Naming | 文件命名 |
| Version Strategy | 版本策略 |
| QA Criteria | 质量标准 |
| Pause Conditions | 暂停条件 |
| Return Format | 返回格式 |
| Review Items | 待裁决项 |

⸻

### CH08.3 常见执行包类型

| 类型 | 适用对象 |
|---|---|
| Manus Handoff Package | 文件工程、页面、PPT、GitHub 整理 |
| Codex Execution Package | 代码实现、测试、脚本 |
| Claude Code Package | 工程审查、代码库理解 |
| Kimi Research Package | 中文长资料、行业 / 政策 / 投标材料 |
| Python Automation Package | 表格、清洗、渲染、计算 |
| ChatGPT Structuring Package | 结构推演、文档主稿、审校 |

⸻

### CH08.4 暂停条件

执行体遇到以下情况必须暂停并返回 Review Item：

1. 上位定义冲突；
2. 文件路径不确定；
3. 任务范围超出执行包；
4. 需要删除或覆盖原文件；
5. 涉及公司定位、项目归位、对外承诺；
6. 涉及医疗、财务、法律风险；
7. 输出会影响 Master SSOT；
8. 缺少必要输入材料。

⸻

## CH 09｜小步快跑与快速试错机制

### CH09.1 试错定义

试错闭环，是在明确方向与边界后，以最小可验证动作进行快速验证、记录结果、复盘判断、沉淀经验并决定继续、修正、暂停或升级的机制。

小步快跑不是无边界试错，而是在明确方向、风险和记录机制之后，用最小闭环验证真实世界反馈。

没有记录、没有复盘、没有回流的试错，只是消耗，不是学习。

⸻

### CH09.2 Trial Loop 标准字段

| 字段 | 说明 |
|---|---|
| Trial ID | 试错编号 |
| Goal | 验证目标 |
| Scope | 范围 |
| Boundary | 边界 |
| Risk Level | 风险 |
| Minimum Loop | 最小闭环 |
| Observation | 观察指标 |
| Result | 结果 |
| Decision | Continue / Revise / Pause / Escalate |
| Asset Destination | 资产归位 |

⸻

### CH09.3 试错动作结论

| 动作 | 含义 |
|---|---|
| Continue | 继续扩大验证 |
| Revise | 修正路径后继续 |
| Pause | 暂停等待条件 |
| Escalate | 升级至 Core / SCO / Matrix / PCS |

⸻

### CH09.4 可试错与不可试错

| 类型 | 可否试错 | 要求 |
|---|---|---|
| 页面原型 | 可 | 明确不作为正式系统 |
| 字段模板 | 可 | 可回滚、有版本 |
| 内部流程 | 可 | 不影响外部承诺 |
| 菜品组合测试 | 可 | 不涉及医疗承诺 |
| 工具评估 | 可 | 不接入敏感数据 |
| 对外报价 | 谨慎 | 必须人工确认 |
| 医疗营养承诺 | 不可自动试错 | 必须专业审核 |
| 法律 / 财务责任 | 不可自动试错 | 必须人智裁决 |

⸻

## CH 10｜问题、异常与经验沉淀机制

### CH10.1 问题到资产的路径

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

⸻

### CH10.2 问题分类表

| 问题类型 | 示例 | 资产方向 |
|---|---|---|
| 任务问题 | 责任不清、节点遗漏 | Pattern / Field |
| 工具问题 | 工具输出失真 | Exception / Rule |
| 数据问题 | 字段缺失、格式不一 | Field / Rule |
| 规则问题 | 判断标准不清 | Rule / Judgment |
| 代码问题 | 脚本失败、页面错误 | Exception / SOP |
| 现场问题 | 出品延误、服务异常 | Exception / Pattern |
| 供应问题 | 缺货、涨价、替代 | Rule / Exception |
| 人员问题 | 排班缺口、职责模糊 | Pattern / Field |
| 财务问题 | 成本异常、结算不清 | Rule / Field |
| 判断问题 | 取舍依据不足 | Judgment |

⸻

### CH10.3 经验资产类型

| 资产类型 | 核心字段 |
|---|---|
| Pattern Asset | 场景、对象、流程、角色、输入、输出、成功条件 |
| Exception Asset | 异常类型、发生环节、触发信号、处理动作、复盘 |
| Rule Asset | 规则名称、触发条件、执行动作、例外情况 |
| Field Asset | 字段名称、类型、来源、质量要求 |
| Judgment Asset | 判断场景、判断人、价值依据、风险权衡、裁决理由 |
| SOP | 操作流程、适用范围、责任角色 |
| Skill | 触发条件、输入、步骤、工具、质量门 |
| DE Candidate | 长期职责、授权边界、运行频率 |

⸻

### CH10.4 经验沉淀原则

1. 重复出现的流程进入 Pattern Asset；
2. 异常、错误、延误、投诉进入 Exception Asset；
3. 可判断、可触发、可执行的规则进入 Rule Asset；
4. 可复用字段、表格、状态进入 Field Asset；
5. 人类关键判断、拒绝理由、取舍依据进入 Judgment Asset；
6. 稳定流程进入 SOP；
7. 高频能力进入 Skill；
8. 稳定长期职责进入 Digital Employee Candidate；
9. 可模块化功能进入 Nex·EC Engine Module Candidate。

⸻

## CH 11｜Project-to-Skill 数智蒸馏机制

### CH11.1 定义

Project-to-Skill，是从真实项目中提取可复用能力的过程。

它不是把项目总结写成文章，而是把真实任务中的对象、规则、异常、字段、判断和流程沉淀为可复用资产。

⸻

### CH11.2 标准蒸馏路径

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

⸻

### CH11.3 Project-to-Skill 蒸馏表

| 步骤 | 输入 | 输出 |
|---|---|---|
| 真实项目运行 | 项目任务 / 现场数据 | 真实样本 |
| 对象识别 | 用户、菜品、订单、岗位、供应商 | 对象清单 |
| 规则抽取 | 成功 / 失败案例 | 规则条目 |
| 异常归档 | 异常记录 | Exception Asset |
| 模板化 | 字段 / 流程 / 判断 | SOP / Template |
| Skill 化 | 高频能力 | Skill |
| Agent 配置 | 稳定任务角色 | Agent / DE |
| 引擎化 | 可模块化功能 | Nex·EC Candidate |

⸻

### CH11.4 Skill 成熟条件

一个 Skill 至少应满足：

1. 有明确触发条件；
2. 有明确输入材料；
3. 有稳定执行步骤；
4. 有可调用工具；
5. 有质量门；
6. 有输出格式；
7. 有失败 / 暂停条件；
8. 有适用与不适用边界；
9. 有版本记录；
10. 有真实项目验证来源。

⸻

## CH 12｜人智决策与风险权限

### CH12.1 风险权限原则

越是高风险、强不确定、涉及外部承诺或责任承担的事项，越不能绕过人智裁决。

机器可以推演、建议、整理、模拟、执行低风险任务，但不能替代人承担高风险决策责任。

⸻

### CH12.2 风险权限表

| 风险等级 | 机器权限 | 人智要求 | 记录要求 |
|---|---|---|---|
| Low | 可建议并自动执行 | 事后抽查 | 自动记录 |
| Medium | 可生成方案与建议 | 责任人审核 | 记录审核人 |
| High | 只可推演与建议 | Judgment Holder 裁决 | 记录权衡理由 |
| Critical / Red | 不得自动执行 | Core / 指定负责人确认 | 完整决策记录 |

⸻

### CH12.3 升级触发条件

| 触发条件 | 升级对象 |
|---|---|
| 改变全局基线 | iS-Core |
| 改变项目定位 | iS-Core / PCS |
| 涉及对外承诺 | Judgment Holder |
| 涉及医疗 / 财务 / 法律责任 | Core / 指定负责人 |
| 工具输出冲突 | Matrix / Hub |
| 项目资源冲突 | Core / PCS |

⸻

### CH12.4 Judgment Asset

当一个决策涉及明显取舍、风险、拒绝、暂停、升级或高价值判断时，应形成 Judgment Asset。

Judgment Asset 至少包含：

1. 判断场景；
2. 判断人；
3. 背景；
4. 选项；
5. 风险；
6. 价值依据；
7. 裁决结果；
8. 后续动作；
9. 是否回写 Context OS / PCS / Master SSOT。

⸻

## CH 13｜面向 Nex₂U 的应用示范

### CH13.1 为什么以 Nex₂U 作为首个样板

Nex₂U 是超智体系当前推进中的重要实战样板，涉及用户需求、营养规则、菜品结构、订单履约、供应协同、现场反馈与经验沉淀。

因此，Nex₂U 适合作为 DICB 的首个真实验证场。

⸻

### CH13.2 Nex₂U 当前关键判断

Nex₂U 当前关键不是先做漂亮前端，而是跑通规则、菜品、订单、履约、供应、反馈和经验沉淀的最小闭环。

⸻

### CH13.3 Nex₂U 最小闭环

点餐体验
  ↓
生产保障
  ↓
服务运维
  ↓
采购支持
  ↓
人力管理
  ↓
财务管控
  ↓
经验沉淀

⸻

### CH13.4 Nex₂U 最小闭环节点

| 业务闭环层 | 操作链条层 | 对应引擎 |
|---|---|---|
| 点餐体验 | 用户需求 / 营养规则 / 菜品结构 / 点餐原型 | Nex2U / NexChef |
| 生产保障 | 厨房履约 / 出品任务 / 质量核查 | NexChef / NexOps |
| 服务运维 | 现场执行 / 异常处理 / 设备状态 | NexOps |
| 采购支持 | 原料需求 / 供应备货 / 替代策略 | NexSply |
| 人力管理 | 岗位状态 / 排班 / 效能记录 | NexMPC |
| 财务管控 | 成本核控 / 结算对账 / 毛利追踪 | NexFA |
| 经验沉淀 | 反馈记录 / 复盘 / Skill 提炼 | iS-Cortex / Project-to-Skill |

⸻

### CH13.5 首批 Skill 候选

| # | Skill | 使用者 | 核心职责 | 当前状态 |
|---|---|---|---|---|
| 1 | 菜单设计 | 营养师/运营 | 每日/周菜单方案生成 | 规划 |
| 2 | 点单保障 | 前台/收银 | 点单异常处理、补单 | 部分就绪（打单已封装） |
| 3 | 履约协同 | 厨房/运营 | 出品任务、履约状态 | 规划 |
| 4 | 采购管理 | 采购/仓管 | 采购需求、备货、供应商 | 规划 |
| 5 | 财务管控 | 财务/管理层 | 成本、毛利、结算对账 | 规划 |
| 6 | 人力调度 | 店长/运营 | 岗责描述、排班、效能 | 规划 |
| 7 | 日常运维 | 店长/全员 | 食安检查、设备、环境、开关店、合规记录 | 规划 |
| 8 | 任务跟踪 | 项目人员 | 任务状态、阻塞项、进度 | 规划 |
| 9 | 报告台账 | 管理层/中台 | 经营日报/周报、复盘、资产入库 | 规划 |
| 10 | MetaSkill（Skill 治理） | 中台管理 | 检查 Skill 运行状态、输出质量、版本升级 | 储备规划 |

> **打单系统归位说明**：当前打单系统定位为 Skill（点单保障的一部分）。其演进路径为：Skill（打单格式生成）→ System（订单数据持久化与规则引擎）→ Agent（自动监听与触发）。

⸻

### CH13.6 与番医项目的关系

番医项目可作为 DIC 从 Nex₂U 规则走向真实项目功能台的启动场景。

但番医任务台、餐食台、人力台不应先于 DIC 主源完成而盲目搭建。
正确顺序应为：

DIC 主源完成
  ↓
GitHub / 文件归位规则明确
  ↓
项目台机制确认
  ↓
番医三台启动
  ↓
任务 / 餐食 / 人力最小闭环
  ↓
试运行与经验回流

⸻

## CH 14｜阶段路线图

### CH14.1 阶段总览

| 阶段 | 目标 | 输出 |
|---|---|---|
| 0-30 天 | 建立 DIC 主源与最小协同机制 | DICB、模板、执行包 |
| 30-90 天 | 围绕 Nex₂U / 番医跑最小闭环 | 任务台、餐食台、人力台、反馈资产 |
| 90-180 天 | 扩展 SOP / Skill / Registry | Tool Registry、Skill Registry、Experience Asset |
| 180 天后 | 形成稳定运行基线 | DIC V1.0 |

⸻

### CH14.2 阶段优先级

| 优先级 | 事项 |
|---|---|
| P0 | DIC 主源完成、HTML 输出、基础模板 |
| P1 | GitHub 治理、项目台机制、番医三台 |
| P2 | Tool / Agent / Skill Registry |
| P3 | 系统化后台、小程序、自动化集成 |

⸻

### CH14.3 当前建议推进顺序

当前阶段建议按以下顺序执行：

DIC·BBMap
  ↓
DIC·BBL
  ↓
DICB Markdown 主源
  ↓
py 渲染脚本
  ↓
html 阅读版
  ↓
GitHub 全仓整理
  ↓
项目台机制
  ↓
番医任务台 / 餐食台 / 人力台

先让规则成文，再让 GitHub 和项目台按规则运行。

⸻

## CH 15｜DIC 版本治理与后续升级

### CH15.1 版本路径

| 版本 | 状态 | 触发条件 |
|---|---|---|
| V0.1 | Working Draft | 首版主源完成 |
| V0.2 | Pilot Version | Nex₂U / 番医试运行后 |
| V0.3 | Registry Version | Tool / Agent / Skill Registry 建立 |
| V0.5 | Operational Beta | 多项目使用后 |
| V1.0 | Stable Baseline | 经 2-3 个项目验证稳定 |

⸻

### CH15.2 更新归位规则

| 更新类型 | 归位 |
|---|---|
| 公司定位变化 | V3.10 |
| DIC 协同机制变化 | DICB |
| 项目状态变化 | PCS |
| 操作流程稳定 | SOP |
| 高频能力封装 | Skill |
| 工具评估变化 | Tool Registry |
| 经验沉淀 | Experience Asset |

⸻

### CH15.3 V3.10 反向补丁原则

DIC V0.1 完成后，不建议立即升级 V3.10。

待 DIC 经 Nex₂U / 番医最小闭环验证后，再考虑给 V3.10 增加轻量引用补丁，例如：

1. 在项目组合或基线索引中加入 DICB；
2. 在全域基线对齐协议中说明 DIC 是下位运行基线；
3. 在 Machine Index 中补入 DIC 文件；
4. 在版本日志中记录 DIC 的形成。

⸻

## Appendix A｜AI / Agent / Tool Capability Matrix

| Tool Name | Tool Type | Best Use | Forbidden Use | Required Input | Output Type | QA Gate | Owner | Status | Registry Destination |
|---|---|---|---|---|---|---|---|---|---|
| ChatGPT | LLM / Structuring | 战略整理、文件主稿、执行包 | 替代 SSOT 裁决 | 背景、目标、边界 | 文档 / 结构 | 人智审校 | iS-Core | Active | Tool Registry |
| Claude | LLM / Review | 长文档复核、第二视角 | 单独业务裁决 | 文档、审校目标 | Review Note | 结构一致性 | iS-Matrix | Candidate | Tool Registry |
| Codex | Code Agent | 代码、脚本、测试 | 业务规则裁决 | 执行包、仓库路径 | Code / PR | 测试通过 | Codex Owner | Candidate | Agent Registry |
| Claude Code | Code Agent | 工程理解、代码库协作 | 替代产品判断 | 仓库、任务说明 | Code / Review | 工程审查 | Dev Owner | Candidate | Agent Registry |
| Python | Automation | 表格、清洗、渲染、计算 | 价值判断 | 数据、脚本需求 | CSV / HTML / JSON | 输出校验 | iS-Matrix / Manus | Active | Tool Registry |
| Manus | Execution Agent | 文件工程、HTML、PPT、GitHub整理 | 自行改写上位定义 | Handoff Package | 文件包 | iS-Core QA | Manus | Active | Agent Registry |
| Kimi | Research Agent | 中文长资料、政策、供应商资料 | 最终裁决 | 资料与问题 | Research Note | 事实核查 | iS-Hub | Candidate | Tool Registry |

⸻

## Appendix B｜Task Routing Table

| Task Type | Trigger | Target Workspace | Required Output | Risk Level | Feedback Destination |
|---|---|---|---|---|---|
| 全局基线变更 | 影响 SSOT / Context OS | iS-Core | 裁决 / Patch | High | Master SSOT / Context OS |
| 战略路径推演 | 多方案取舍 | iS-SCO | Strategy Note | Medium | Decision Log |
| SOP / Skill 生产 | 高频流程沉淀 | iS-Matrix | SOP / Skill Draft | Medium | SOP / Skill Registry |
| 工具评估 | 新工具 / Agent | iS-Hub | Tool Review | Low-Medium | Tool Registry |
| 未成熟想法 | 灵感 / 方向未定 | iS-Lab | Validation Note | Low | Lab Log |
| 项目执行 | 已有 PCS | PCS | Task Update | Medium | PCS |
| 文件工程 | 渲染 / HTML / GitHub | Manus | File Package | Low-Medium | GitHub |
| 代码执行 | 脚本 / 系统 | Codex / Claude Code | Code / Test | Medium | Repo / Review Log |

⸻

## Appendix C｜Task Node Template

node_id:
node_name:
path_stage:
project_or_domain:
input:
action:
owner_role:
support_role:
tool_or_agent:
output:
qa_gate:
risk_level:
status:
feedback_destination:
asset_candidate:
review_items:

⸻

## Appendix D｜Execution Package Template
```markdown
# Execution Package
## 1. Mission Name
## 2. Background
## 3. Goal
## 4. Input Materials
## 5. Scope
## 6. Non-Goals
## 7. Output Requirements
## 8. File Naming
## 9. Version Strategy
## 10. QA Criteria
## 11. Pause Conditions
## 12. Return Format
## 13. Review Items

⸻
```
⸻
## Appendix E｜Trial Loop Record Template
```yaml
trial_id:
hypothesis:
goal:
minimum_action:
scope:
boundary:
risk_level:
metric:
observation:
result:
decision: Continue | Revise | Pause | Escalate
asset_destination:
owner:
date:
review_items:

⸻
```
⸻
## Appendix F｜Experience Asset Capture Template
```yaml
F.1 Pattern Asset

asset_type: Pattern
scenario:
object:
process:
roles:
input:
output:
success_condition:
reuse_condition:
source_project:

F.2 Exception Asset

asset_type: Exception
exception_type:
stage:
trigger_signal:
impact:
temporary_action:
root_cause:
review_result:
future_rule:
source_project:

F.3 Rule Asset

asset_type: Rule
rule_name:
trigger_condition:
action:
exception:
owner:
qa_gate:
source_project:

F.4 Field Asset

asset_type: Field
field_name:
field_type:
definition:
source:
quality_requirement:
related_table:
source_project:

F.5 Judgment Asset

asset_type: Judgment
scenario:
judgment_holder:
background:
options:
risk:
value_basis:
decision:
reason:
follow_up:
source_project:

F.6 Skill Candidate

asset_type: Skill Candidate
skill_name:
trigger:
input:
steps:
tools:
output:
qa_gate:
failure_condition:
source_project:

F.7 Digital Employee Candidate

asset_type: Digital Employee Candidate
role_name:
responsibility:
trigger_frequency:
input:
output:
authority_boundary:
qa_gate:
source_project:

F.8 Engine Module Candidate

asset_type: Engine Module Candidate
module_name:
engine:
business_function:
input:
output:
dependency:
validation:
source_project:

⸻
```

## Appendix G｜Machine-Readable Index

{
  "document_id": "Synexa_DIC_Baseline_V0.1",
  "zh_name": "超智科技·数智协同基线",
  "en_name": "Synexa Digital-Intelligence Collaboration Baseline",
  "short_name": "DICB",
  "version": "V0.1",
  "status": "Working Draft",
  "upper_source": "Synexa_Company_Intro_V3.10",
  "maintainer": "iS-Core",
  "first_application": "Nex2U",
  "core_concepts": [
    "Digital-Intelligence Collaboration",
    "Human Judgment",
    "Digital Intelligence",
    "Decision Bridge",
    "Task Routing",
    "Task Node",
    "Execution Package",
    "Trial Loop",
    "Experience Asset",
    "Project-to-Skill"
  ],
  "output_files": {
    "markdown": "Synexa_DIC_Baseline_V0.1.md",
    "render_script": "Synexa_DIC_Baseline_Render_V0.1.py",
    "html": "Synexa_DIC_Baseline_V0.1.html"
  },
  "next_steps": [
    "Generate render script",
    "Generate HTML reading version",
    "Review with Manus",
    "Prepare GitHub governance",
    "Prepare Fanyi project workbench"
  ]
}

⸻

## Appendix H｜Version Register & Change Log

| Version | Date | Change Summary | Impact Scope | Owner |
|---|---|---|---|---|
| V0.1 | 2026-06-27 | 首版 DICB Markdown 主源草案 | DICB / Nex₂U / GitHub 后续治理 | iS-Core |

⸻

Closing Statement｜结语

V3.10 定义超智的总图，DICB 定义超智的走法。

BBMap 定蓝图，BBLx 定章节逻辑，DICB 定正式主源。

先让规则成文，再让 GitHub 和项目台按规则运行。

DICB 的核心价值，不是把工具列全，而是让人和机器在真实项目中形成共同协同秩序，并把问题、规则、判断和经验持续沉淀为可复用资产。

⸻

本文件为《超智科技·数智协同基线 V0.1》Markdown 主源草案。后续所有事实性修改应回到本 Markdown 主源进行。HTML / PDF / JSON / ZIP 均为输出形态，不替代主源。