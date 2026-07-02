# Synexa iS · Context OS (全局状态总账本)

> **版本**：v2.9
> **更新时间**：2026-06-27
> **定位**：Synexa iS 体系的动态运行层，记录当前活跃项目全景、全局状态与关键决策。
> **使用原则**：所有智能体在执行任务前，必须优先读取本文件以获取最新全局上下文。

---

## 1. 体系运行基线

* **当前体系版本**：SSADS V1.4
* **核心架构**：五层协同架构 (System -> SOP -> Skills -> Agent Matrix -> PCS)
* **方法总线**：18步全局工作流标准（2026-04-18 正式确立，详见 `SYNEXA_IS_BASE_FRAMEWORK_v1.0.md`）
* **最高裁决原则**：总纲 > Context OS > PCS > 决策日志 > 临时讨论
* **对话组总数**：L1×5 + L2×7 + L3/L4 若干（详见 `00-master/WORKSPACE_REGISTRY_v2.0.md`）
* **域名与基础设施注册**：详见 `00-master/DOMAIN_REGISTRY_v1.0.md`
* **主控入口**：【智核中枢·iS-Core】（对外品牌名：超智系统·Synexa iS）
* **全局文件命名规范**：`[中文摘要]_[英文代号]_v[版本].md`，所有工作空间生成文件时强制执行。详见 `00-master/PROMPT_SYSTEM_TASK_v1.0.md` 第五节。`IS_SOP_FILE_GOVERNANCE_v1.0.md` 中的命名规则已废止，以本规范为唯一标准。

---

## 1B. 品牌架构总览（iS-Synexa 战略推演 · 2026-04-29 更新）

> 本节已由 iS-Synexa 品牌建设组于 2026-04-29 完成战略推演升级，覆盖 2026-04-26 iS-Core 裁决版（七大引擎扩展），所有智能体与文件应以此为准。

### 超智（Synexa）的本质定位

**超智是一个「自带超级大脑的现代服务网络」，而非纯粹的软件公司。**

超智提供新一代健康餐食交付、供应链服务与整合营销服务。其核心护城河在于将多年在复杂现实场景（医院饭堂、供应链、大型传播项目）中积累的非结构化经验，提炼为可计算、可复制的七大数字引擎。**对外卖结果（代运营/交付结果），对内用系统（七大引擎）。**

**核心价值主张**：泥土里的数字孪生——既懂凌晨3点的菜市场，又懂 AI 智能体的调度。

### 七大引擎完整定位与收入路径（2026-04-29 确立）

七大引擎分为三类，遵循「先内部捶打，后对外开放」的演进逻辑：

**一、内部提效型（底盘引擎）**

| 引擎 | 定位 | 当前阶段 | 中期路径 | 长期路径 |
|---|---|---|---|---|
| **NexFlow** | 项目架构与任务管理平台，沉淀复杂项目管理经验的引擎平台 | 内部使用，持续捶打 | 合作项目提点分成 | SaaS / 服务市场 |
| **NexMPC** | 人力组织效能引擎，解决「谁来做、怎么考核」 | 内部使用，持续捶打 | 合作项目提点分成 | SaaS / 服务市场 |
| **NexFA** | 财务核算与成本控制引擎，解决「花多少、赚多少」 | 内部使用，持续捶打 | 合作项目提点分成 | SaaS / 服务市场 |

**二、核心生产型（直接创收引擎）**

| 引擎 | 定位 | 当前阶段 | 中期路径 | 长期路径 |
|---|---|---|---|---|
| **Nex2U** | 健康稳态计算中枢，「可以活十年的营养决策基础设施」，把营养学变成可计算的代码 | 健康餐食场景验证，直接创收 | 机构合作方案费 | 全行业营养决策基础设施 |
| **NexChef** | 餐食生产与物理履约引擎，把烹饪变成 SOP 和具身智能指令 | 医院饭堂等项目直接创收 | 连锁复制 / 加盟 | 全域餐食履约网络 |
| **Nexsply** | 供应链协同管理系统，更好管理供应链服务的工具，不只是采购渠道 | 供应链服务直接创收 | 行业供应链枢纽 | 全域原材料平台 |

**三、增收杠杆型（直接创收引擎）**

| 引擎 | 定位 | 当前阶段 | 中期路径 | 长期路径 |
|---|---|---|---|---|
| **NexIMC** | 新一代整合营销传播服务，面向餐饮、生活小家电等消费品牌，是创始人品牌传播积累的系统化载体 | 直接对外营销服务创收 | 扩大品类与客户规模 | 消费品牌营销基础设施 |

### 三阶段发展路径

- **阶段一（现在）**：卖「结果」，不卖「系统」。用系统武装自己，对外只谈「更健康、更稳定、成本更优的餐食方案」和「更有效的整合营销服务」。
- **阶段二（中期）**：卖「标准」，带「资源」。当饭堂项目跑通，供应链和管理系统有了说服力，开始向同行输出能力，底盘引擎通过合作项目提点分成创收。
- **阶段三（长期）**：卖「网络」，做「平台」。七大引擎成为行业基础设施，超智成为「产业路由器」，赚取整个网络的协同红利。

### 对外沟通三段论话术（代运营/交付结果导向）

**立足现实**：「我们提供各种形态的健康餐食产品或定制服务，以及专业的供应链和整合营销服务，让客户买到更对、更优质、价格更科学的产品，或者拿到更好的营销结果。」

**展现壁垒**：「我们之所以能做到这一点，是因为我们把多年经验提炼成了七大数字引擎。我们自己就是这些工具的重度使用者，用系统卡住每一个容易出错的门禁。」

**描绘未来**：「现在，我们不仅用这些引擎服务自己，也开始将它们作为生产协同工具开放出来，为需要供应链协同、项目管理、整合营销的企业，提供最前沿、体验最优的解决方案。」

> **历史价值保留**：Nex2U 的核心定位话术为「可以活十年的营养决策基础设施」，适合在深度沟通场景（投资人、战略合作方）中使用，比「新一代健康餐食交付」更有穿透力。

### 行业组合示例（超智协同输出）

- 医院饭堂：NexChef（餐食履约）+ Nex2U（营养决策）+ Nexsply（供应链）+ NexFlow（项目管理）
- 餐饮品牌：NexChef + Nexsply + NexIMC（整合营销）
- 消费品牌营销：NexIMC（独立服务）

> 超智负责把这些模块协同起来，对外输出完整的行业解决方案，而不是让客户自己拼装。

---

## 2. 待同步事项 (GPT 侧)

> **注意**：每次接入必须检查此列表。若有未完成项，必须在对话开头置顶提示用户上传，直至用户确认完成。

| 文件名 | 更新日期 | 状态 | 说明 |
| :--- | :--- | :--- | :--- |
| `Manus_Project_Instructions_v26.1.6.md` | 2026-04-09 | ⏳ 待上传 | 融合版 Manus 指令（iS-Core 主控） |
| `GPT_Project_Instructions_iSCore_v26.1.6.md` | 2026-04-09 | ⏳ 待复制录入 | 融合版 GPT 指令，需复制至 GPT Project Instructions 字段 |
| `iS_Instructions_All_Workspaces_v1.3.md` | 2026-04-16 | ⏳ 待上传 | 全工作空间指令模板（注入 FBR 机制触发词规则） |
| `AI_Workspace_Architecture_v1.3.md` | 2026-04-09 | ⏳ 待上传 | 工作空间架构说明（v1.2 已作废） |
| `iS_Workspace_Architecture_v1.3.png` | 2026-04-09 | ⏳ 待上传 | 工作空间架构图（新版） |
| `Synexa_Architecture_Definition_v1.1.md` | 2026-04-09 | ⏳ 待上传 | 四层架构完整定义 |
| `Synexa_iS_SSADS_Master_Blueprint_v1.4.md` | 2026-04-08 | ⏳ 待上传 | 总纲·制度母法 |
| `CONTEXT_OS.md` | 2026-04-18 | ⏳ 待上传 | 本文件（**v2.3**，含18步工作流、INSTRUCTION_TRACKER、iS-GlobalPM 三项裁决） |
| `FBL_Template_v1.1.md` | 2026-04-16 | ⏳ 待上传 | FBL 功能基线列表模板（v1.1，含三步闭环字段，旧版 v1.0 作废） |
| `SOP_001_FBR_Mechanism_v1.1.md` | 2026-04-16 | ⏳ 待上传 | FBR 机制标准操作程序（v1.1，核心逻辑修订为「指令积累→代码比对→验证闭环」，旧版 v1.0 作废） |
| `_INDEX.md` | 2026-04-18 | ⏳ 待上传 | 项目索引（已更新，新增 iS-GlobalPM Step 0A 最小定义） |
| `iS-Synexa_PCS_v0.1.md` | 2026-04-09 | ⏳ 待上传 | 超智建设 PCS |
| `Nex2U_PCS_Template_v0.2.md` | 2026-04-08 | ⏳ 待上传 | 智食引擎 PCS |
| `Synexa_iS_Overview.md` | 2026-04-09 | ⏳ 待上传 | 0号文件 |
| `Synexa_Codex_v1.0_Public_View.md` | 2026-04-11 | ⏳ 待上传 | Synexa Codex 首发版（L1+L2 Public View） |
| `iS-Publish_PCS_v0.1.md` | 2026-04-11 | ⏳ 待上传 | 信息生产与发布系统 PCS |
| `iS-NexFlow_PCS_Briefing_v0.6.md` | 2026-04-16 | ⏳ 待上传 | NexFlow 完整定位文件（V0.6，iS-Core 正式裁决通过） |
| `SYNEXA_OVERVIEW.md` | 2026-04-16 | ⏳ 待上传 | 超智总览（已更新母品牌 + 超级系列 + 四大引擎·中台描述） |
| `iS-NexFlow_Workspace_Startup_Guide_v1.0.md` | 2026-04-16 | ⏳ 待上传 | iS-NexFlow 工作空间启动指引（含系统提示词 + 启动路径 + 基线说明） |
| `NexFlow_TBF_V3.0.md` | 2026-04-16 | ⏳ 待上传 | NexFlow V3.0 任务目标基线文件（TBF 机制首个实例，含 SCO 核查结论） |
| `ISYNC_PROTOCOL.md` | 2026-04-16 | ⏳ 待上传 | 全局指令同步协议（ISYNC v1.0，含触发词 SOP 与接入指南） |
| `06-isync/_ISYNC_INDEX.md` + 各项目 ISYNC 文件 | 2026-04-16 | ⏳ 待上传 | ISYNC 目录初始化（5个对话组已建立初始文件） |
| `ISYNC_PROTOCOL.md` | 2026-04-17 | ⏳ 待上传 | **v1.2**（新增 TBF 三态核查门禁机制，旧版 v1.1 作废） |
| `TBF_Template_v2.1.md` | 2026-04-17 | ⏳ 待上传 | TBF 模板 v2.1（新增三态核查裁决区与强制提交规范联动，旧版 v2.0 作废） |
| `SOP_003_Execution_Submission_v1.0.md` | 2026-04-17 | ⏳ 待上传 | 执行框强制提交规范（新文件，含数据库迁移唯一路径原则） |
| `INSTRUCTION_TRACKER.md` | 2026-04-18 | ⏳ 待上传 | Core 指令追踪表（新文件，含 CORE-CMD-001 和 CORE-CMD-002） |
| `SYNEXA_IS_BASE_FRAMEWORK_v1.0.md` | 2026-04-18 | ⏳ 待上传 | 超智系统基座框架文档（已更新，新增全局18步工作流标准完整定义） |
| `Synexa_iS_Base_Architecture_v1.4.mmd` | 2026-04-18 | ⏳ 待上传 | 架构图 v1.4 Mermaid 源文件（新增 INSTRUCTION_TRACKER、iS-GlobalPM、18步工作流标注） |
| `Synexa_iS_Base_Architecture_v1.4.png` | 2026-04-18 | ⏳ 待上传 | 架构图 v1.4 渲染图（线框风格，适合 A3 打印） |
| `Synexa_iS_Base_Architecture_v1.4.2.webp` | 2026-04-20 | ⏳ 待上传 | **架构图 v1.5 终版（用户审定）**，含左侧18步竖排+虚线映射，已入仓为 v1.4.2 与 v1.5_FINAL 双文件 |
| `SOP_007_Instruction_Tracker_Standard_v1.0.md` | 2026-04-20 | ⏳ 待上传 | 指令汇总追踪表机制体系级标准规范（新文件，响应 NexFlow PCS ISYNC 通报裁决通过） |
| `GLOBAL_INSTRUCTION_TRACKER.md` | 2026-04-20 | ⏳ 待上传 | 全局指令追踪总表（新文件，6个项目摘要行，含 iS-NexFlow V3.0 阻塞项标注） |
| `INSTRUCTION_TRACKER.md` | 2026-04-20 | ⏳ 待上传 | iS-Core 指令追踪表（v1.2，新增 CORE-CMD-007/008，批次总览更新） |
| `WORKSPACE_REGISTRY_v2.0.md` | 2026-04-26 | ⏳ 待上传 | 对话组全局注册表 v2.0（L1×5 + L2×7，含 NexMPC/NexFA，Nex2U/NexChef 架构关系明确，旧版 v1.0 作废） |
| `DOMAIN_REGISTRY_v1.1.md` | 2026-04-26 | ⏳ 待上传 | 域名与基础设施注册表 v1.1（补充引擎归属字段；品牌域=产品介绍/系统域=实战工具；番医项目归属修正；全局枢纽看板归属 NexFlow；v1.0 作废） |
| `CONTEXT_OS.md` | 2026-04-26 | ⏳ 待上传 | 本文件（**v2.7**，Nex2U/NexChef 主题定位改为对外产品价值描述，内部架构关系移至备注；超智协同描述更新为七大引擎） |
| `TASK_SUMMARY_SKILL_v1.0.md` | 2026-05-03 | ⏳ 待上传 | 任务情况汇总 Skill v1.0（新文件，iS-Core 裁决通过，全局通用，含标准字段+双形态+6个触发词+工作空间接入指南） |

> **旧文件需删除**：`GPT_Project_Instructions_SynexaiS_v26.1.5.md`、`iS_Instructions_All_Workspaces_v1.1.md`、`iS_Instructions_All_Workspaces_v1.2.md`、`AI_Workspace_Architecture_v1.2.md`（如已上传）

---

## 3. 活跃项目全景 (Project Portfolio)

| 项目代号 | 项目名称 | 层级 | 当前所处 Step | 状态 | 负责人/主导 Agent | 核心目标 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **iS-Nex2U** | 智食引擎 | G·集团级 | Step 3 (业务结构建模) | 🟢 推进中 | 治理智能体 | 将非结构化健康餐饮逻辑转化为可计算的规则引擎 |
| **iS-NexFlow** | 【超级项管·iS-NexFlow】- PCS（一站式项目协同智能平台） | **G·集团级**（正式裁决） | 迭代推演中（V2.6-brand 当前基线，V3.0 TBF 已建立，补丁指令待执行） | 🟢 推进中 | iS-SCO | 将项目执行过程中所有信息流统一纳管，「信息不出系统」 |
| **NexFlow·Synexa** | 超智内部全局项管 | G·集团级 | Step 0A（最小定义完成） | 🟡 已立项 | iS-Core | NexFlow 产品族在超智 iS 体系内的内部部署版本，管理超智全局所有业务板块的项目推进；P1，待启动 |
| **NexFlow·iS** | NexFlow 产品开发建构管理 | G·集团级 | 概念方向 | 🟡 已立项 | iS-Core | iS 体系负责推进 NexFlow 产品开发建构的项管线 |
| **iS-Synexa** | 超智建设 | G·集团级 | Step 0B（待推进） | 🟡 已立项 | iS-Core | 超智品牌建设与对外表达，P2·次优先；需同步超智官网建设 |
| **iS-Nexsply** | 意臻供应链 | G·集团级 | 待启动 | ⚪ 待立项 | 待定 | 全球优质原材料采购与供应链整合 |
| **iS-NexChef** | NexChef（待定） | G·集团级 | 持续运营 | 🔵 运行中 | 待定 | 餐饮与生活方式品牌，项目名称待确认 |
| **iS-SOP** | 规程资产库 | F·功能模块级 | 待启动 | ⚪ 待立项 | iS-Matrix | 生产并维护全体系的 SOP 与操作规程 |
| **iS-Publish** | 信息生产与发布系统 | F·功能模块级 | Step 0A（已完成） | 🟡 已立项 | iS-Matrix | 基于"一源多发"机制，将 SSOT 渲染为面向不同受众的多深度文档切片（Synexa Codex 体系） |

---

## 4. 全局阻塞项与待决策事项 (Blockers & Pending Decisions)

### 4.1 待决策事项

* **GPT 侧全量同步**：2026-04-09、2026-04-16、2026-04-17、2026-04-18 多次大规模更新，GPT 侧尚未同步，需用户完成全量上传（见第2节清单）。
* **Nex₂U 业务系统设计推演**：基于现有雏形系统（NuBō/Nufō³），明确系统边界、多场景可配置架构逻辑，并识别直接升级与重构模块。（当前最高优先级）
* **各待立项项目启动**：iS-Nexsply、iS-NexChef（待定）、iS-SOP 需要在 iS-Core 完成最小定义后正式立项。
* **iS-Synexa Step 0B**：超智建设项目需推进至 Step 0B（启动检查），确认品牌叙事方向、官网目标受众、视觉规范起点；**同步通知超智官网建设负责方**，确保官网内容框架与体系架构定义保持一致。
* **【超级项管·iS-NexFlow】- PCS 工作空间建立**：iS-Core 已授权，启动指引（`iS-NexFlow_Workspace_Startup_Guide_v1.0.md`）已生成并归档至 GitHub。待用户在 Manus / GPT 建立专属 Project，命名「超级项管·iS-NexFlow」，粘贴指引中的系统提示词。V3.0 指令包（`nexflow_v3_0_final.md`）尚在本地沙盒，待推送至 `carefulxiao-cell/nexflow/docs/`。
* **NexFlow V3.0 文件中心补丁**：TBF 核查已确认文件中心（/files）6项均未完成，补丁指令待在【超级项管·iS-NexFlow】工作空间执行。
* **NexFlow·Synexa Step 0B**：超智内部全局项管已完成 Step 0A 最小定义，待后续推进至 Step 0B（启动检查）。

### 4.2 阻塞项

* *(暂无全局阻塞项)*

### 4.3 领域基线状态

| 代号 | 名称 | 当前进展 | 下一步 | 路径 |
| :--- | :--- | :--- | :--- | :--- |
| **DIC** | 数智协同基线 | Step1–Step6 全部✅ 全链条完成 | 翻医三台建设待启动，DIC V0.2 等 Nex₂U 验证后触发 | `00-overview/domain-baselines/dic/` |

---

## 5. 全局机制注册 (Global Mechanisms)

| 机制代号 | 机制名称 | 触发词 | 协议文件 | 状态 |
| :--- | :--- | :--- | :--- | :--- |
| **TBF** | 任务目标基线文件（三态核查） | 版本交付时强制执行 | `05-sop/TBF_Template_v2.1.md` | 🟢 已升级（v2.1，三态门禁生效） |
| **SOP-003** | 执行框强制提交规范 | 每次代码交付时强制执行 | `05-sop/SOP_003_Execution_Submission_v1.0.md` | 🟢 已启用（2026-04-17） |
| **ISYNC** | 全局指令同步协议 | `汇总指令` / `全面审查 [项目代号]` | `00-master/ISYNC_PROTOCOL.md` | 🟢 已启用（2026-04-16 初始化） |
| **INSTRUCTION_TRACKER** | 指令追踪表机制 | 每次新增指令时强制归档 | `06-isync/INSTRUCTION_TRACKER.md` | 🟢 已启用（2026-04-18，Core 首发，向全 PCS 推广中） |
| **SOP_007** | 指令汇总追踪表机制体系级标准规范 | 所有 PCS 工作空间建立指令追踪表时强制遵循 | `05-sop/SOP_007_Instruction_Tracker_Standard_v1.0.md` | 🟢 已启用（2026-04-20，响应 NexFlow PCS ISYNC 通报，为 SOP_004/005/006 上位体系级文件） |
| **GLOBAL_INSTRUCTION_TRACKER** | 全局指令追踪总表 | 各项目在里程碑节点或重大状态变更时向 iS-Core 提交 ISYNC 通报 | `06-isync/GLOBAL_INSTRUCTION_TRACKER.md` | 🟢 已启用（2026-04-20，初始化，6个项目摘要行） |
| **DIALOGUE_FRAMEWORK_L2** | Layer 2 标准四框架构定义 | 建立新对话组时强制对照 | `00-master/SYNEXA_DIALOGUE_ARCHITECTURE_v1.0.md`（待重建） | 🟡 架构已裁决，文件待重建 |
| **SOP-008** | 编撰线标准生产规范 | 启动任何文件/知识类生产任务时强制遵循 | `05-sop/SOP_008_Documentation_Workflow_v1.0.md` | 🟢 已启用（2026-04-25，确立七步工作流） |
| **TASK_SUMMARY_SKILL** | 任务情况汇总 Skill | `输出任务快照` / `更新任务台账` / `读取任务台账` / `新增任务 [任务名]` / `标记完成 [任务名]` / `全局任务审查` | `00-master/TASK_SUMMARY_SKILL_v1.0.md` | 🟢 已启用（2026-05-03，iS-Core 裁决通过，标准字段+双形态+触发词+接入指南） |
| **FILE_NAMING_CONVENTION** | 全局文件命名规范 | 生成任何文件时强制执行 | `00-master/PROMPT_SYSTEM_TASK_v1.0.md`（第五节） | 🟢 已启用（2026-05-17，iS-Core 裁决通过，格式：[中文摘要]_[英文代号]_v[版本].md，IS_SOP_FILE_GOVERNANCE 命名规则已废止） |

---

## 6. 关键决策日志 (Decision Log)

### 2026-04-20

**裁决事项**：「指令汇总追踪表机制」提升为体系级基线标准

**来源**：NexFlow PCS ISYNC 通报（机制建立申请）

**裁决结果**：通过。发布 SOP_007 v1.0，建立 GLOBAL_INSTRUCTION_TRACKER.md，要求所有活跃项目在下一次迭代时完成追踪表的标准化改造。SOP_007 定位为 SOP_004/005/006 的上位体系级文件，不引起冲突。

| 日期 | 决策事项 | 决策结果 | 影响范围 |
| 2026-06-08 | **超智公司定位升级为「协同智能公司」（iS-Core 裁决）** | ①放弃「数智工业科技」公司名方向，公司注册名维持「超智（广州）数字科技有限公司」，未来适时改为「超智（广州）科技有限公司」；②超智品牌定位正式确立为「协同智能公司（Collaborative Intelligence Company）」；③能力体系确立为四层：场景智能/供应网络智能/系统智能/协同智能；④核心认知框架确立为四层结构：主体→能力体→能力网络→协同网络（自进化协同网络）；⑤场景布局：核心场景医疗养老健康生活，第一延展方向地产物业，持续关注能源管理；⑥建立历史文件归档机制（`99-archive/`），SOP 升级为 v1.1；⑦`Synexa_Company_Intro` 升级为 v2.0，旧版及四个历史推演文件归档入库。详见 `00-overview/Synexa_Company_Intro_v2.0.md`，SOP 见 `00-master/IS_SOP_FILE_GOVERNANCE_v1.1.md`。 | 全局品牌定位，文件治理体系 |
| 2026-06-09 | **超智公司介绍升级至 v2.1** | 新增「发展路径」三阶段与「分受众表达」七模块（含对客户/合作伙伴/地产物业/能源/投资人），详见 Synexa_Company_Intro_v2.0.md | iS-Core |
| :--- | :--- | :--- | :--- |
| 2026-04-29 | **超智（Synexa）战略定位与七大引擎体系全面升级（iS-Synexa 品牌建设组推演确立）** | 核心共识：①超智定位从「系统公司」升级为「自带超级大脑的现代服务网络」；②引擎体系在 2026-04-26 七大基础上新增 NexIMC（整合营销传播），形成完整七大引擎（NexFlow/NexMPC/NexFA/Nex2U/NexChef/Nexsply/NexIMC）；③确立三类引擎分类（内部提效型/核心生产型/增收杠杆型）及三阶段收入路径；④NexIMC 定位为整合营销传播服务，面向餐饮、生活小家电等消费品牌，直接创收；⑤对外话术确立为「代运营/交付结果」导向的三段论；⑥保留奇绩申请表历史价值：Nex2U「可以活十年的营养决策基础设施」定位话术。详见 `00-overview/Synexa_Seven_Engines_Positioning_and_Strategy.md`，PCS 升级为 `iS-Synexa_PCS_v0.2.md`。 | 全局品牌，iS-Synexa |
| 2026-04-26 | **引擎体系扩展：四大→七大（iS-Core 裁决）** | ①新增 NexMPC（人力管理引擎·超级人力管理）、NexFA（财务管理引擎·超级财务管理）；②Nexsply 定位升级为「供应链智能中台（全链路协同覆盖）」；③Nex2U / NexChef 架构关系明确：Nex2U 为规则 SSOT 面向 B 端决策层，NexChef 为消费与应用交互引擎面向 C 端及 B 端操作层，点餐系统归属 NexChef；④iS-Lab 正名为「智核实验·iS-Lab」，副名「灵感前测」；⑤建立 WORKSPACE_REGISTRY v2.0 与 DOMAIN_REGISTRY v1.0 两个新注册表文件。 | 全局品牌架构，L2 引擎体系 |
| 2026-04-24 | **Layer 2 标准框型扩展：新增「编撰-」框型（iS-Core 裁决）** | Layer 2 同组协作层标准框型从三框扩展为四框：①中枢框（`iS-[项目]`）：指令生产·目标确认·阶段裁决；②执行框（`执行-`）：系统/网站/代码类工程生产；③**编撰框（`编撰-`）**：文件/知识/治理文档类生产（新增）；④审查框（`审查-`）：里程碑独立审查。执行框与编撰框可并行运作，互不干扰。全局架构图同步更新至 v1.2（颜色+线条+编撰框）。 | 全局体系治理，Layer 2 架构定义 |
| 2026-04-18 | **全局18步工作流标准正式确立（iS-Core 裁决）** | 超智全局工作流程标准化为18个步骤，分三大阶段：分析层（步骤1-5：描述情况→推演可能→目标制定→交流互补→对齐理解）、执行层（步骤6-11：生成指令→审核指令→汇总推进→入仓留存→下发执行→反查完善）、沉化层（步骤12-18：阶段完成→整理汇总→状态审查→跟踪推进→整洁清理→更新通报→全局对齐）。已写入 `SYNEXA_IS_BASE_FRAMEWORK_v1.0.md`。 | 全局体系治理 |
| 2026-04-18 | **INSTRUCTION_TRACKER 机制全局启动（iS-Core 裁决）** | `INSTRUCTION_TRACKER.md` 在 Core 工作空间正式初始化，包含批次管理、废弃协议、跨仓库可见性三项优化字段。裁决：该机制将向所有 PCS 工作空间推广，每个 PCS 在下次重大迭代时同步建立本空间的 INSTRUCTION_TRACKER。 | 全局体系治理 |
| 2026-04-22 | **NexFlow 批次G V1.9 MEET-002 会议记录模块重构（iS-NexFlow PCS 执行完成）** | 完成会议记录模块从「逐项填表」到「非结构化纪要→AI标准化→任务卡片校正→汇入闭环→通报生成」的完整重构。数据层：meetings 表新增 standardizedMinutes 字段，status 枚举更新为5态（draft/standardized/tasks_reviewed/organized/archived），migration 0023 执行成功。接口层：重构 create/aiParse/processTodo 三接口，新增 updateStandardized 接口，实现 AI 标准化、结构化任务卡片提取、语义去重比对、批量汇入（sourceOrigin/sourceRefs 写入）、通报自动生成。前端层：Meetings.tsx 完全重写为四视图流程（Input→Standardized→TasksReview→Report），STATUS_LABEL 对齐 schema 枚举。TypeScript 0 errors，9文件 89用例全部PASS。Checkpoint: 62f9cdd1，GitHub commit: 42f4728。 | iS-NexFlow |
| 2026-04-20 | **NexFlow 产品族命名体系更新（iS-Core 裁决）** | 确立 NexFlow 为产品族主线。原 `iS-GlobalPM` 重命名为 `NexFlow·Synexa`（超智内部全局项管）；新增 `NexFlow·iS`（NexFlow 产品开发建构管理）。 | 全局体系治理 |
| 2026-04-18 | **iS-GlobalPM Step 0A 最小定义（iS-Core 裁决）** | 项目代号：`iS-GlobalPM`（后更名为 `NexFlow·Synexa`）；名称：超智全局超级项管系统；一句话定义：针对超智全局系统的高效高质执行落地管理，基于18步工作流标准搭建；层级：G·集团级；优先级：P1。已写入 `03-projects/_INDEX.md`。 | iS-GlobalPM |
| 2026-04-17 | **协作链路结构性修复三项裁决（iS-Core 正式裁决）** | ①ISYNC 协议升级为 v1.2，写入 TBF 三态核查门禁机制（✅通过/⚠️待验证/❌未通过），强制阻断未完成生产验证的下一阶段推进；②新增 `SOP_003_Execution_Submission_v1.0.md`，确立执行框强制提交报告规范，含架构规范自查（无原生 SQL、唯一迁移路径）与生产环境验证截图要求，格式不符 PCS 有权拒绝接收；③确立数据库迁移唯一路径原则：所有数据库结构变更必须通过 Drizzle ORM 标准迁移流程，禁止任何独立建表脚本，违反可要求回滚。TBF 模板同步升级为 v2.1。根因：体系有规范文档但无执行门禁，本次三条裁决将现有规范从「建议」升级为「门禁」。 | 全局体系治理，iS-NexFlow 首发 |
| 2026-04-17 | **工程治理白皮书 v1.0 + TBF 模板 v2.0 发布（iS-Core 正式裁决）** | ①发布《Synexa iS 工程治理白皮书 v1.0》，归档至 `00-master/ENGINEERING_GOVERNANCE_WHITEPAPER_v1.0.md`，确立 7步闭环工作流与 ISO/IEC 25010 八大质量维度为全体系最高工程原则；②发布 TBF 标准模板 v2.0，归档至 `05-sop/TBF_Template_v2.0.md`，强制增加 NFR（非功能性需求）和架构设计确认两大板块；③确立 NexFlow V3.0 为首个试运行样板项目。 | 全局体系治理，iS-NexFlow 首发 |
| 2026-04-16 | **ISYNC 机制建立（iS-Core 正式裁决）** | 建立全局指令同步协议（ISYNC v1.0）：①在 `00-master/ISYNC_PROTOCOL.md` 定义协议；②在 `06-isync/` 目录初始化5个对话组的指令文件；③确立 `汇总指令` 与 `全面审查 [项目代号]` 两条触发词；④ISYNC 成为所有独立立项对话组的标配机制。 | 全局体系治理 |
| 2026-04-16 | **FBR 机制正式裁决 v1.1（iS-Core 修订）** | 核心逻辑修订：FBR 机制的本质是「指令积累 → 代码比对 → 验证闭环」三步工作流。①所有开发指令共识形成文件留存积累于中央仓；②激活审查时以 FBL（指令汇总文件）为基准，一一扫描代码包比对；③正向验证（指令→代码是否实现）+ 反向验证（代码→指令是否记录），发现偏差及时完善增补去重。文件升级为 FBL_Template_v1.1 + SOP_001_FBR_Mechanism_v1.1。 | 全局体系治理 |
| 2026-04-16 | **TBF 机制基线原则裁决（iS-Core 正式裁决）** | ①每次版本迭代，指令包必须附带 TBF，与指令包同时归档至 `docs/` 目录 ✅通过；②执行框完成后必须逐项回写 TBF，不得只说「已完成」✅通过；③SCO 每次版本交付后执行 TBF 核查，核查结论回写 TBF ✅通过；④TBF 是版本交付的必要条件，未完成核查不得标记「已完成」✅通过；⑤TBF 机制适用所有有代码交付的 PCS 项目，从 NexFlow V3.0 开始试行 ✅通过。NexFlow V3.0 TBF 已同步建立并归档。 | 全局体系治理，iS-NexFlow 首发 |
| 2026-04-16 | **iS-NexFlow 七项裁决（iS-Core 正式裁决）** | ①定位升级：「执行操作系统」→「一站式项目协同智能平台 / 一站项管协同中台」✅通过；②层级升级：G·集团级（与 Nex2U / Nexsply / NexChef 同级）✅通过；③品牌架构确认：超智=母品牌+中央引擎·中台，超级系列=对外产品线品牌，四大引擎·中台对应关系 ✅通过；④GitHub 仓库更新授权 ✅已执行；⑤PCS 文件归档 ✅已归档（03-projects/NexFlow/）；⑥新专栏建立授权 ✅已授权，待用户操作；⑦超智官网建设同步 ✅已记录为待决策事项，归入 iS-Synexa Step 0B 推进范畴。 | iS-NexFlow, 全局品牌, iS-Synexa |
| 2026-04-16 | 超智品牌架构定义正式裁决 | 确认「超智 = 母品牌 + 中央引擎·中台」、「超级系列 = 对外产品线品牌」、四大引擎·中台与超级系列对应关系；更新至 CONTEXT_OS v1.6 及 SYNEXA_OVERVIEW.md；超智官网建设需同步对齐（归入 iS-Synexa Step 0B）。 | 全局品牌 |
| 2026-04-16 | iS-NexFlow 品牌架构与定位对齐 | iS-SCO 提交 PCS Briefing V0.6，明确 NexFlow 为「超级项目管理」主题引擎·中台，定位升级为「一站式项目协同智能平台」，层级申请 G·集团级；品牌标识 NexFlow · IntP·Lab；系统内品牌文字已同步更新（登录页、侧边栏、Guide页、index.html title）；PCS 文件已归档至 carefulxiao-cell/nexflow/docs/ 与 Synexa-iS-OIOS/03-projects/NexFlow/；iS-Core 正式裁决通过。 | iS-NexFlow, 全局品牌 |
| 2026-04-14 | NexFlow 平台定位与迭代推演 | 确认 NexFlow 定位为与 Nex₂U 同级别的引擎业务输出（Execution OS）；识别当前系统底层数据（依赖关系、优先级算法）缺失风险；输出三阶段迭代序列，提交 iS-Core 裁决。 | iS-NexFlow |
| 2026-04-11 | iS-Publish 立项（Step 0A）；Synexa Codex v1.0 Public View 首发 | 确立 iS-Publish 为 F·功能模块级项目；定义"动态知识协议（DKP）"与 L1/L2/L3 三层受众切片机制；完成《Synexa Codex v1.0 Public View》首个产物；创建 PCS v0.1。 | iS-Publish, iS-Synexa |
| 2026-04-09 | iS-Synexa 立项（Step 0A） | 完成超智建设项目的最小定义：G·集团级，P2·次优先，创建 PCS v0.1，待推进至 Step 0B。 | iS-Synexa |
| 2026-04-09 | 融合「超智系统·Synexa iS」与「智核中枢·iS-Core」 | 两者合并为单一对话组【智核中枢·iS-Core】；「Synexa iS」保留为对外品牌名；对话组总数从10个减为9个；更新全部相关文件。 | 全局 |
| 2026-04-09 | 修复体系身份混淆 Bug | 全面核查并修复了将 System Layer（Synexa iS）与 Module Layer（iS-Core）混同的系统性 Bug，更新了 Manus/GPT 指令母本、全工作空间指令模板、Overview 及 README。 | 全局 |
| 2026-04-08 | 工作空间架构重构 | 确立六类工作空间（Core/Hub/SCO/Matrix/PCS/Lab），明确 Matrix 为结构化产出引擎，取消 SOP 独立组，确立五节点知识生产闭环。 | 全局 |
| 2026-04-08 | iS-Hub 重新定义 | 将 iS-Hub 定义为"情报室·智能体资源库"，负责内外部 Agent 案例、工具与平台的汇聚与参照。 | 全局 |
| 2026-04-08 | 强化跨平台同步机制 | 在 CONTEXT_OS 引入「待同步事项」追踪机制，强制 AI 每次接入主动盯紧 GPT 侧的文件同步状态。 | 全局 |
| 2026-04-07 | SSADS 总纲升级 | 将总纲文件从 v1.2 升级至 V1.4 完整版。 | 全局 |

| 2026-06-27 | **DIC 领域基线体系建立（iS-Core 裁决）** | 新建 `00-overview/domain-baselines/dic/` 目录；落盘 DIC·BBM V0.1（Step2）和 DIC·BBLx V0.1（Step3）两个文件；同步更新 REPO_INDEX v1.1 / _INDEX / CONTEXT_OS v2.9。3个索引文件全部对齐。首个验证场：Nex₂U；Review Item：V3.10 CH04.1 补丁等 DIC V0.2 后执行。 | DIC 领域基线，全局文件索引 |

---

*注：本文件由 Manus 治理智能体（iS-Core）维护，任何全局状态变更必须同步回写至此。*
