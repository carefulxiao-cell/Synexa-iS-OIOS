# SOP_002_Manus_Workspace_Naming_v1.0

> **版本**：v1.0
> **生效日期**：2026-04-16
> **维护主体**：iS-Core（智核中枢）
> **定位**：定义超智体系在 Manus 平台上的工作空间（Workspace）与对话框（Session）的命名规范与管理机制。

---

## 1. 机制概述

为了确保 Synexa iS 体系在 Manus 平台上的多项目、多角色协同能够有序进行，必须建立一套标准化的工作空间与对话框命名规范。这套规范旨在：
1. **清晰识别角色与层级**：通过命名前缀，快速识别当前对话框所属的治理层级（如 Core, SCO, PCS）。
2. **精准定位项目与任务**：通过项目代号和任务描述，明确对话框的具体工作内容。
3. **保持全局状态一致性**：确保 Manus 平台上的对话框结构与 GitHub 中央仓的目录结构、GPT 侧的 Project 结构保持高度映射。

---

## 2. 命名规范 (Naming Convention)

Manus 对话框的命名应遵循以下标准结构：

**`[角色前缀] - [项目/系统代号] · [任务/模块描述]`**

### 2.1 角色前缀 (Role Prefix)

用于标识当前对话框所属的治理层级或角色定位：

- `Core`：智核中枢，负责全局基线治理、跨项目裁决、状态同步。
- `SCO`：策略中心，负责战略推演、需求定义、架构设计。
- `PCS`：项目控制系统，负责具体项目的执行、开发、交付。
- `Matrix`：智核矩阵，负责知识沉淀、SOP 制定、培训。

### 2.2 项目/系统代号 (Project/System Code)

用于标识当前对话框所属的具体项目或系统：

- `iS-Core`：智核中枢基线系统
- `NexFlow`：超级项管
- `Nex2U`：智食引擎
- `Nexsply`：意臻国际供应链
- `NTogether`：膳食同行

### 2.3 任务/模块描述 (Task/Module Description)

用于简要描述当前对话框的具体工作内容或聚焦的模块：

- `动态功能基线·FBR`
- `全面审查`
- `执行框`

---

## 3. 典型命名示例

根据上述规范，以下是一些典型的 Manus 对话框命名示例：

### 3.1 治理层级 (Governance Layer)

- `Core - 智核中枢·iS-Core`：用于全局状态同步、基线维护。
- `Core - 动态功能基线·FBR (Functional Baseline & Review)`：用于 FBR 机制的专项治理与推演。

### 3.2 项目执行层级 (Execution Layer)

- `PCS - 超级项管·NexFlow`：NexFlow 项目的主执行对话框。
- `PCS - 智食引擎·Nex2U`：Nex2U 项目的主执行对话框。
- `PCS - 膳食同行·NTogether`：NTogether 项目的主执行对话框。

### 3.3 专项任务层级 (Task Layer)

- `Core - 超级项管·NexFlow`：用于 NexFlow 项目的跨层级裁决与状态同步。
- `SCO - 超级项管·NexFlow`：用于 NexFlow 项目的战略推演与需求定义。
- `全面审查 - 超级项管·iS-NexFlow`：用于执行 NexFlow 项目的 FBR 全面审查任务。
- `执行框 - 超级项管·NexFlow`：用于 NexFlow 项目的具体开发与执行任务。

---

## 4. 管理机制与融合方案

### 4.1 目录映射与对齐

Manus 平台上的项目文件夹（Folder）应与 GitHub 中央仓的 `03-projects/` 目录结构保持一致。例如：
- Manus 文件夹：`【超级项管·iS-NexFlow】 - PCS`
- GitHub 目录：`03-projects/NexFlow/`

### 4.2 对话框生命周期管理

1. **创建**：由 iS-Core 或 SCO 触发新项目/新任务时，按规范命名创建新的对话框。
2. **执行**：在对话框内执行具体任务，所有关键决策和产出必须回写至 GitHub 中央仓。
3. **归档**：任务完成后，对话框可保留作为历史记录，但不再作为活跃工作区。

### 4.3 跨平台状态同步

- **GPT 侧**：GPT 侧的 Project 命名与结构应与 Manus 侧保持一致。
- **GitHub 侧**：所有对话框的核心产出（如 TBF, FBL, SOP）必须统一归档至 GitHub 中央仓，确保 SSOT（Single Source of Truth）。

---

*注：本规范自发布之日起生效，所有新建的 Manus 对话框均应遵循此规范。现有对话框应逐步进行重命名调整。*
