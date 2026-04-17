# GPT 双轨同步日志 (GPT Sync Log)

> **定位**：记录向 GPT 侧工作空间同步体系基线文件的历史记录，作为「定期轨」与「机动轨」的基准参照。
> **维护主体**：iS-Core

---

## 1. 同步机制定义

| 轨道 | 触发条件 | 频率 | 内容范围 |
| :--- | :--- | :--- | :--- |
| **定期轨** | 固定日期触发 | 建议每两周一次 | 距离上次同步后的**全量**变更文件清单 |
| **机动轨** | Core 重大裁决后 | 不定期，按需 | 仅本次裁决产生的**增量**文件清单 |

---

## 2. 同步记录区

### [2026-04-17] 定期轨：近10天全量基线同步

**背景**：GPT 侧近 10 天未进行系统性更新，本次执行全量基线文件同步，对齐至 2026-04-17 的最新状态。

**需上传至 GPT【智核中枢·iS-Core】Project 的文件清单（共 18 个）**：

**【00-master 核心制度】**
1. `Synexa_iS_SSADS_Master_Blueprint_v1.4.md` (总纲)
2. `Synexa_Architecture_Definition_v1.1.md` (四层架构定义)
3. `ENGINEERING_GOVERNANCE_WHITEPAPER_v1.0.md` (工程治理白皮书)
4. `ISYNC_PROTOCOL.md` (v1.1，全局指令同步协议)

**【01-core 核心指令】**
5. `Manus_Project_Instructions_v26.1.6.md` (Manus 融合版指令)
6. `GPT_Project_Instructions_iSCore_v26.1.6.md` (GPT 融合版指令，需复制文本)
7. `iS_Instructions_All_Workspaces_v1.3.md` (全工作空间指令模板)
8. `AI_Workspace_Architecture_v1.3.md` (工作空间架构说明)

**【02-context-os 全局状态】**
9. `CONTEXT_OS.md` (v2.2，全局状态总账本)
10. `SYNEXA_OVERVIEW.md` (超智总览)

**【03-projects 项目定义】**
11. `_INDEX.md` (项目索引)
12. `iS-NexFlow_PCS_Briefing_v0.6.md` (NexFlow 定位文件)
13. `iS-NexFlow_Workspace_Startup_Guide_v1.0.md` (NexFlow 启动指引)

**【05-sop 标准规程】**
14. `FBL_Template_v1.1.md` (功能基线列表模板)
15. `SOP_001_FBR_Mechanism_v1.1.md` (FBR 机制 SOP)
16. `SOP_002_Manus_Workspace_Naming_v1.2.md` (命名规范 SOP)
17. `SOP_003_Execution_Submission_v1.0.md` (执行框提交规范)
18. `TBF_Template_v2.1.md` (TBF 模板)

**需在 GPT 侧删除的过期文件**：
- `GPT_Project_Instructions_SynexaiS_v26.1.5.md`
- `iS_Instructions_All_Workspaces_v1.1.md` / `v1.2.md`
- `AI_Workspace_Architecture_v1.2.md`
- `FBL_Template_v1.0.md`
- `SOP_001_FBR_Mechanism_v1.0.md`
- `SOP_002_Manus_Workspace_Naming_v1.0.md` / `v1.1.md`
- `TBF_Template_v2.0.md`

**状态**：⏳ 待用户确认上传完成。
