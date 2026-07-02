# TASK_SUMMARY_SKILL · 任务情况汇总 Skill

> **版本**：v1.1
> **创建日期**：2026-05-03
> **归档路径**：`carefulxiao-cell/Synexa-iS-OIOS/00-master/TASK_SUMMARY_SKILL_v1.0.md`
> **定位**：Synexa iS 体系全局通用 Skill，任何工作空间均可轻量激活。
> **状态**：🟢 活跃（已与 TASK_TRACKING_PROTOCOL 融合）

---

## 一、Skill 定位与融合说明

本 Skill 已与 `TASK_TRACKING_PROTOCOL_v1.0.md`（全局任务追踪协议）完成融合。
- **字段规范与状态标签**：全部由 `TASK_TRACKING_PROTOCOL_v1.0.md` 统一定义。
- **本文件定位**：精简为纯触发词声明与接入指南，作为各工作空间快速激活任务追踪能力的入口。

---

## 二、触发词清单（对齐全局协议）

| 触发词 | 执行动作 |
|---|---|
| `读取任务协议` | 读取 TASK_TRACKING_PROTOCOL 全文，按协议规范建立或校验当前工作空间的任务追踪表 |
| `初始化任务表 [工作空间代号]` | 按协议字段规范，创建该工作空间的标准任务追踪表，文件命名为 `TASK_BOARD_[代号].md` |
| `更新任务表` | 追加/更新当前工作空间任务板的任务行，并在回复末尾附推进汇总表 |
| `输出推进汇总` | 按协议模板输出标准推进汇总表（Markdown 表格格式） |
| `输出任务快照` | 读取 IS_TRACKER_MASTER，输出全局 11 条推进台账 |
| `输出项目快照` | 读取 TASK_BOARD_[当前工作空间]，输出本项目内部任务清单 |
| `全局任务审查` | 读取所有活跃工作空间的 `TASK_BOARD_*.md`，输出全局任务健康度报告 |

---

## 三、工作空间接入指南

任何工作空间（Manus Project / GPT Project）需要激活本 Skill，只需在系统提示词中加入以下一段：

```markdown
【任务情况汇总 Skill】
本工作空间已接入 Synexa iS 全局任务情况汇总 Skill。
- 字段规范与状态标签：严格遵循 `00-master/TASK_TRACKING_PROTOCOL_v1.0.md`
- 触发词机制：
  - `初始化任务表 [代号]`：新建本项目任务板
  - `更新任务表`：更新本项目任务板
  - `输出项目快照`：输出本项目任务清单
  - `输出推进汇总`：每次回复末尾输出推进汇总表
执行时必须先读取 TASK_TRACKING_PROTOCOL，严格遵循其中的 11 字段规范，不得自行增减字段。
```
