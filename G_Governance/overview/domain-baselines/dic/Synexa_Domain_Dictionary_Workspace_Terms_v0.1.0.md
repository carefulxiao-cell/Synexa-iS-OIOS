# Synexa 全域字典｜数据工作区共同术语

| 字段 | 内容 |
|---|---|
| Document Type | L1 Domain Dictionary |
| Chinese Name | Synexa 全域字典｜数据工作区共同术语 |
| English Name | Synexa Domain Dictionary — Data Workspace Terms |
| Short Name | DIC-WORKSPACE |
| Version | v0.1.0-pilot.1 |
| Status | candidate |
| Maintainer | iS-Core |
| Upper Source | `G_Governance/overview/Synexa_Company_Intro_V3.11.md` §26.9.11 |
| Scope | 页面、界面、业务工作区、看板、分区、视图、模块、组件、模板、数据资产；附“工作空间”消歧 |
| Updated At | 2026-11-15 |

## 1. 主源与使用规则

本文件是上述术语的共同定义主源。各 Skill、项目和文档引用本文件的路径与版本，只补充自身适用说明，不另建竞争定义。事实性修改回到本 Markdown 主源；HTML、表格、页面或对话摘要均为派生形态。

这些术语描述可按业务目标组合的对象，**不是固定的逐级包含链**。基本关系为：页面承载工作区；工作区按目标组织看板、表格、表单和操作功能；看板可以划分多个分区；视图决定怎样看；界面承载实际呈现与操作。不得按文件、图表或截图数量推定工作区数量。

候选状态表示定义已形成并完成本次跨文件核对，不表示所有平台已经加载或所有业务已经采用。跨项目复用后，按上位主源 §26.9.11 的垂直整合原则补证据、修订或晋升。

## 2. 术语表

| Term ID | 中文名 | 英文名 | Short Name | Definition | Layer | Project | Category | Related Terms | Allowed Usage | Forbidden Usage | Version | Status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| DIC-WS-001 | 页面 | Page | page | 具有明确地址、导航入口或内容边界的信息承载单元，可承载一个或多个工作区及其他内容。 | L1 | Global | 信息承载 | 界面、业务工作区、模板 | 描述网站、应用或文档式应用中的内容承载 | 不把每个页面自动认定为一个工作区 | v0.1.0-pilot.1 | candidate |
| DIC-WS-002 | 界面 | Interface | interface | 内容实际呈现并供人查看或操作的画面，包含当时可见的布局、控件、状态与反馈。 | L1 | Global | 人机交互 | 页面、视图、组件、分区 | 描述可见呈现、交互和状态验收 | 不与页面地址或设计稿文件数量混同 | v0.1.0-pilot.1 | candidate |
| DIC-WS-003 | 业务工作区 | Business Workspace | business_workspace | 围绕持续业务目标，组织数据组区、分析逻辑、指标主题、信息呈现、操作与交付及质量边界的能力环境。 | L1 | Global | 业务能力 | 看板、表格、表单、视图、数据资产 | 描述支持持续判断或行动的业务操作环境 | 不按文件、图表、截图或页面数量推定；不与协作对话组混称 | v0.1.0-pilot.1 | candidate |
| DIC-WS-004 | 看板 | Dashboard | dashboard | 集中呈现指标、构成、变化、异常及必要追溯入口的信息组织形态，可划分多个分区。 | L1 | Global | 信息组织 | 分区、视图、模块、业务工作区 | 描述综合监控、分析或管理信息集合 | 不把单张图表或任意页面都称为看板 | v0.1.0-pilot.1 | candidate |
| DIC-WS-005 | 分区 | Section | section | 界面或看板内围绕局部信息或操作目的划分的区域，可包含模块、组件、表格或表单。 | L1 | Global | 局部结构 | 看板、界面、模块、组件 | 描述局部内容布局与功能区域 | 不作为独立业务工作区的计数依据 | v0.1.0-pilot.1 | candidate |
| DIC-WS-006 | 视图 | View | view | 同一业务主题在特定筛选、分组、指标、排序和布局条件下形成的观察方式。 | L1 | Global | 观察方式 | 界面、看板、数据资产 | 描述怎样看同一主题及切换观察条件 | 不把视图切换冒充数据事实或业务状态变化 | v0.1.0-pilot.1 | candidate |
| DIC-WS-007 | 模块 | Module | module | 围绕可识别职责组织的一组规则、数据、功能或内容，可跨界面或交付物复用。 | L1 | Global | 职责单元 | 业务工作区、分区、组件、模板 | 描述分析、管理或业务功能职责 | 不与仅负责呈现的组件或固定页面区域混同 | v0.1.0-pilot.1 | candidate |
| DIC-WS-008 | 组件 | Component | component | 完成特定呈现或交互任务的可复用界面单元，如图表、筛选器、表格控件或按钮组。 | L1 | Global | 界面单元 | 界面、分区、模块、视图 | 描述可复用控件及其状态和行为 | 不以组件数量推定模块或工作区数量 | v0.1.0-pilot.1 | candidate |
| DIC-WS-009 | 模板 | Template | template | 为同类任务提供可复用初始结构、字段、规则或样式的起点，实例化后可按业务需要调整。 | L1 | Global | 复用起点 | 模块、组件、页面、业务工作区 | 描述可复用设计或生产起点 | 不把模板数量当作已完成成果或业务采用数量 | v0.1.0-pilot.1 | candidate |
| DIC-WS-010 | 数据资产 | Data Asset | data_asset | 具有明确业务含义、来源、粒度、口径、质量、权限、版本及维护责任，可供持续使用的数据对象或其可追溯派生物。 | L1 | Global | 数据治理 | 业务工作区、视图、模块 | 描述来源事实、分析结果、可编辑计划和执行记录等受治理对象 | 不把无来源文件、临时缓存或测试输入冒充正式数据资产 | v0.1.0-pilot.1 | candidate |
| DIC-WS-011 | 工作空间 | Collaboration Workspace | collaboration_workspace | 为协作者、智能体、会话或项目协作提供上下文与沟通边界的协作环境，其业务成果需连接到相应业务工作区或主源。 | L1 | Global | 协作环境 | 业务工作区、页面、数据资产 | 描述协作对话组、项目协作区或智能体工作环境 | 不与面向业务操作和持续分析的业务工作区混用 | v0.1.0-pilot.1 | candidate |

## 3. 引用方式

机器或文档引用至少记录：`repository`、`path`、`version`、`fixed_commit`、`status` 和 `read_mode`。分支入口用于发现，固定提交用于同版回读；候选、已发布、平台实际加载和业务采用分别核验。
