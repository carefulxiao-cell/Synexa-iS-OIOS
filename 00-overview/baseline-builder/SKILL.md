---
name: baseline-builder
description: Build structured baseline documents (md + HTML) from conversation content or existing materials. Use when user asks to "整理成基线文件", "生产基线文件", "整理出一个基线", or wants to convert conversation insights, project decisions, or operational knowledge into a persistent, visually consistent baseline document. Supports L2 (project-level) and L3 (workstation-level) baseline types aligned to Synexa iS governance standards.
---

# Baseline Builder

将对话内容、项目共识或运营知识，转化为符合 Synexa iS 标准的结构化基线文件（md + HTML）。

## 文件层级定义

| 层级 | 类型 | 适用场景 | 参考规范 |
|---|---|---|---|
| L2 | 项目级基线 | 一个完整项目的全量基线（定位、架构、规则、字典、SOP） | `references/L2_structure.md` |
| L3 | 专项台基线 | 某一专项主题的运营台（任务跟踪、人力管理、餐食运营等） | `references/L3_structure.md` |

## 执行流程

### Step 1：识别类型

判断当前任务是 L2 还是 L3：
- **L2**：覆盖整个项目，有完整的业务定义、字典、规则体系
- **L3**：聚焦某一专项主题，有任务状态、操作规程、当前进展

### Step 2：提炼内容

从对话内容或上传文件中提炼，按对应结构模板组织：
- 读取 `references/L2_structure.md`（L2 任务）
- 读取 `references/L3_structure.md`（L3 任务）

**提炼原则：**
- 保留所有业务定义、规则、关系、字典、决策结论
- 删除所有排版说明、视觉描述、HTML 标签
- 保留数字、比例、时间节点等具体数据
- 模糊表述转化为结构化字段，不猜测补全

### Step 3：生成机读 md

按结构模板输出纯净 md 文件：
- 文件头加上位引用声明（如适用）
- 章节标题使用 `#` / `##` / `###`，不使用 HTML 标签
- 表格使用标准 Markdown pipe 格式
- 版本号格式：`V0.x`（子业务初版）

### Step 4：生成人读 HTML

读取 `references/html_production.md` 执行 HTML 生产，CSS 从已有标准 HTML 提取（用户提供）或按规范手写。

**交付物命名规范：**
```
{项目名}_{文件类型}_V{版本号}.md
{项目名}_{文件类型}_V{版本号}.html
```

### Step 5：输出机读精简版（可选）

如用户需要上传到 Codex Project，额外生成 `_machine.md`：
- 剥离所有 HTML 标签（保留规则说明文字中的标签描述）
- 保留全部业务内容
- 目标体积比原版压缩 15-25%

## 排版依赖说明

HTML 生产需要 `fonts/` 字体文件夹与 HTML 文件同级存放。详见 `references/html_production.md` Section 0。

## 快速触发词

| 用户说 | 执行动作 |
|---|---|
| 整理成基线文件 | 识别类型 → 提炼 → 生成 md + HTML |
| 生产基线文件 | 同上 |
| 只要 md | 跳过 Step 4，只输出 md |
| 加机读版 | 额外执行 Step 5 |
| 更新基线 | 读取已有 md → 合并新内容 → 更新版本号 → 重新生成 HTML |
