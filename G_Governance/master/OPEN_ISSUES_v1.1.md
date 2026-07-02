# Synexa iS · Open Issues (待解决问题清单)

> **版本**：v1.1
> **更新时间**：2026-04-26（v1.1：修正 ISSUE-P01 NexChef 命名；新增 ISSUE-A04/A05/B04/B05/P04；由 iS-Core 审核入库）
> **定位**：Synexa iS 体系内所有跨组遗留问题、待确认事项的集中管理池。
> **维护者**：iS-Core 审核入库 / 编撰-智核中枢·iS-Core 生产

---

## 1. 状态定义

| 状态标签 | 说明 |
| :--- | :--- |
| 🔴 **Blocked** | 阻塞中，依赖前置条件或外部决策 |
| 🟡 **Pending** | 待处理，已记录但尚未分配优先级 |
| 🔵 **In Progress** | 处理中，已有明确负责人和推进计划 |
| 🟢 **Resolved** | 已解决，等待归档清理 |

---

## 2. 全局待解决问题清单

### 2.1 架构与机制类 (Architecture & Mechanisms)

| Issue ID | 标题 | 描述 | 状态 | 负责人 | 依赖项 / 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **ISSUE-A01** | **GPT 侧全量同步缺失** | 2026-04-09 至 04-18 期间多次大规模更新，GPT 侧尚未同步，需用户完成全量上传。 | 🔴 **Blocked** | 用户 | 依赖用户手动上传文件 |
| **ISSUE-A02** | **DIALOGUE_FRAMEWORK_L2 重建** | Layer 2 标准四框架构定义已裁决，但 `SYNEXA_DIALOGUE_ARCHITECTURE_v1.0.md` 文件待重建。 | 🟡 **Pending** | 编撰-iS-Core | 归属 F-10 任务排期 |
| **ISSUE-A03** | **Git 推送门禁（A+C 机制）落地** | SOP_008 Step 7 需拆分为 7a（输出待入库清单等确认）+ 7b（确认后推送）；Project Instructions 需增加强制规则。 | 🟡 **Pending** | iS-Core | 归属 G-01 任务排期 |
| **ISSUE-A04** | **WORKSPACE_REGISTRY L3/L4 三项待确认** | 云图计划归档状态、植言集·Verdata 定位、视觉类对话组命名三项尚未确认，F-06 正式版无法生产。 | 🔴 **Blocked** | 用户 | 用户确认后，F-06 可立即生产正式版 |
| **ISSUE-A05** | **NexMPC / NexFA PCS 文件待创建** | 两个引擎已完成 Step 0A 最小定义（人力管理引擎 / 财务管理引擎），但 PCS 文件尚未创建，专属对话组尚未建立。 | 🟡 **Pending** | iS-Core | 归属 G-04 任务排期 |

---

### 2.2 业务系统类 (Business Systems)

| Issue ID | 标题 | 描述 | 状态 | 负责人 | 依赖项 / 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **ISSUE-B01** | **Nex₂U 业务系统设计推演** | 基于现有雏形系统（NuBō/Nufō³），明确系统边界、多场景可配置架构逻辑，并识别直接升级与重构模块。 | 🔵 **In Progress** | iS-Nex2U | 当前最高优先级业务推演 |
| **ISSUE-B02** | **【超级项管·iS-NexFlow】- PCS 工作空间建立** | iS-Core 已授权，启动指引已生成。待用户在 Manus / GPT 建立专属 Project，粘贴系统提示词。 | 🔴 **Blocked** | 用户 | 依赖用户手动建组 |
| **ISSUE-B03** | **NexFlow V3.0 文件中心补丁执行** | TBF 核查已确认文件中心（/files）6项均未完成，补丁指令待在【超级项管·iS-NexFlow】工作空间执行。 | 🔴 **Blocked** | 执行-NexFlow | 依赖 ISSUE-B02 完成 |
| **ISSUE-B04** | **Nexsply PCS 文件定位待更新** | Nexsply 已裁决升级为「供应链智能中台（全链路协同覆盖）」，但 PCS 文件内容尚未同步更新，存在定位不一致风险。 | 🟡 **Pending** | 编撰-iS-Core | 待排期更新 PCS 文件 |
| **ISSUE-B05** | **DOMAIN_REGISTRY 服务器信息待补充** | DOMAIN_REGISTRY v1.1 中服务器/托管字段目前为空，需补充各系统对应的服务器、托管平台、IP 等核心信息。 | 🟡 **Pending** | 用户 + iS-Core | 依赖用户提供服务器信息后录入 |

---

### 2.3 项目立项与推进类 (Projects & Operations)

| Issue ID | 标题 | 描述 | 状态 | 负责人 | 依赖项 / 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **ISSUE-P01** | **各待立项项目启动 (Step 0A)** | iS-Nexsply、iS-NexChef（消费与应用交互引擎）、iS-SOP 需要在 iS-Core 完成最小定义后正式立项。 | 🟡 **Pending** | iS-Core | 待排期推进 |
| **ISSUE-P02** | **iS-Synexa Step 0B 推进** | 超智建设项目需推进至 Step 0B（启动检查），确认品牌叙事方向、官网目标受众、视觉规范起点。 | 🟡 **Pending** | iS-Core | 需同步通知超智官网建设负责方 |
| **ISSUE-P03** | **NexFlow·Synexa Step 0B 推进** | 超智内部全局项管已完成 Step 0A 最小定义，待后续推进至 Step 0B（启动检查）。 | 🟡 **Pending** | iS-Core | 待排期推进 |
| **ISSUE-P04** | **超智建设官网结构对齐（下周商务前）** | 下周需对接养老/金融/招商局，官网叙事框架和结构需在超智建设对话组完成 Step 0B 对齐，时间紧迫。 | 🔴 **Blocked** | 超智建设对话组 | 依赖超智建设对话组启动，G-05 任务 |

---

## 3. 解决与归档记录

*(暂无已解决记录)*

---
*注：本清单由编撰框生产，iS-Core 审核后入库。各工作空间在发现跨组遗留问题时，应通过 iS-Core 申请录入本表。v1.0 作废，以 v1.1 为准。*
