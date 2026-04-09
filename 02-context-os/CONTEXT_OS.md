# Synexa iS · Context OS (全局状态总账本)

> **版本**：v1.3
> **更新时间**：2026-04-08
> **定位**：Synexa iS 体系的动态运行层，记录当前活跃项目全景、全局状态与关键决策。
> **使用原则**：所有智能体在执行任务前，必须优先读取本文件以获取最新全局上下文。

---

## 1. 体系运行基线

* **当前体系版本**：SSADS V1.4
* **核心架构**：五层协同架构 (System -> SOP -> Skills -> Agent Matrix -> PCS)
* **方法总线**：7步建构路径
* **最高裁决原则**：总纲 > Context OS > PCS > 决策日志 > 临时讨论

---

## 2. 待同步事项 (GPT 侧)

> **注意**：每次接入必须检查此列表。若有未完成项，必须在对话开头置顶提示用户上传，直至用户确认完成。

| 文件名 | 更新日期 | 状态 |
| :--- | :--- | :--- |
| `Synexa_Architecture_Definition_v1.0.md` | 2026-04-09 | ⏳ 待上传 |
| `AI_Workspace_Architecture_v1.2.md` (V.1.3) | 2026-04-09 | ⏳ 待上传 |
| `iS_Instructions_All_Workspaces_v1.1.md` | 2026-04-08 | ⏳ 待上传 |
| `Synexa_iS_SSADS_Master_Blueprint_v1.4.md` | 2026-04-08 | ⏳ 待上传 |
| `CONTEXT_OS.md` | 2026-04-09 | ⏳ 待上传 |
| `_INDEX.md` | 2026-04-09 | ⏳ 待上传 |
| `iS-Synexa_PCS_v0.1.md` | 2026-04-09 | ⏳ 待上传 |


---

## 3. 活跃项目全景 (Project Portfolio)

| 项目代号 | 项目名称 | 层级 | 当前所处 Step | 状态 | 负责人/主导 Agent | 核心目标 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **iS-Nex2U** | 智食引擎 | L2·知识推演 | Step 3 (业务结构建模) | 🟢 推进中 | 治理智能体 | 将非结构化健康餐饮逻辑转化为可计算的规则引擎 |
| **iS-Synexa** | 超智建设 | G·集团级 | Step 0B（待推进） | 🟡 已立项 | iS-Core | 超智品牌建设与对外表达，P2·次优先 |
| **iS-Nexsply** | 意臻供应链 | L2·知识推演 | 待启动 | ⚪ 待立项 | 待定 | 全球优质原材料采购与供应链整合 |
| **iS-NexChef** | NexChef（待定） | L2·知识推演 | 持续运营 | 🔵 运行中 | 待定 | 餐饮与生活方式品牌，项目名称待确认 |
| **iS-SOP** | 规程资产库 | L3·技能规程 | 待启动 | ⚪ 待立项 | iS-Matrix | 生产并维护全体系的 SOP 与操作规程 |

---

## 4. 全局阻塞项与待决策事项 (Blockers & Pending Decisions)

### 4.1 待决策事项
* **Synexa 命名体系深化**：Synexa（超智）/ Synexa iS（超智 iS）/ iS-Core（智核中枢）三层命名当前为暂定版，需找时间深化定义、对外表达口径与内部文件统一更新。
* **Nex₂U 业务系统设计推演**：基于现有雏形系统（NuBō/Nufō³），明确系统边界、多场景可配置架构逻辑，并识别直接升级与重构模块。 (当前最高优先级)
* **各待立项项目启动**：iS-Nexsply、iS-NexChef（待定）、iS-SOP 需要在 iS-Core 完成最小定义后正式立项。（iS-Synexa 已于 2026-04-09 完成 Step 0A 立项）

### 4.2 阻塞项
* *(暂无全局阻塞项)*

---

## 5. 关键决策日志 (Decision Log)

| 日期 | 决策事项 | 决策结果 | 影响范围 |
| :--- | :--- | :--- | :--- |
| 2026-04-08 | 工作空间架构重构 | 确立六类工作空间（Core/Hub/SCO/Matrix/PCS/Lab），明确 Matrix 为结构化产出引擎，取消 SOP 独立组，确立五节点知识生产闭环。 | 全局 |
| 2026-04-08 | iS-Hub 重新定义 | 将 iS-Hub 定义为"情报室·智能体资源库"，负责内外部 Agent 案例、工具与平台的汇聚与参照。 | 全局 |
| 2026-04-09 | iS-Synexa 立项（Step 0A） | 完成超智建设项目的最小定义：G·集团级，P2·次优先，创建 PCS v0.1，待推进至 Step 0B。 | iS-Synexa |
| 2026-04-09 | 修复体系身份混淆 Bug | 全面核查并修复了将 System Layer（Synexa iS）与 Module Layer（iS-Core）混同的系统性 Bug，更新了 Manus/GPT 指令母本、全工作空间指令模板、Overview 及 README。 | 全局 |
| 2026-04-08 | 强化跨平台同步机制 | 在 CONTEXT_OS 引入「待同步事项」追踪机制，强制 AI 每次接入主动盯紧 GPT 侧的文件同步状态。 | 全局 |
| 2026-04-07 | Manus Project 指令文件入库（智核中枢） | `Manus_Project_Instructions_v26.1.3.md` 推送至 `00-overview/` 目录，作为 Manus 智核中枢 Project 的正式治理指令 | 全局 |
| 2026-04-07 | Manus Project 指令文件入库（Nex₂U） | `Manus_Project_Instructions_Nex2U_v26.1.1.md` 推送至 `03-projects/Nex2U/` 目录，作为 Manus 智食引擎 Project 的正式治理指令 | Nex₂U 项目 |
| 2026-04-07 | 体系目录结构重构 | 引入 `02-context-os` 和 `05-sop` 目录，解耦项目层与体系层，确立 Context OS 为全局动态入口。 | 全局 |
| 2026-04-07 | SSADS 总纲升级 | 将 `01-master-blueprint` 目录下的总纲文件从 v1.2 升级至 V1.4 完整版。 | 全局 |

---

*注：本文件由 Manus 治理智能体维护，任何全局状态变更必须同步回写至此。*
