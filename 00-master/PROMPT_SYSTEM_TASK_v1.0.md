# PROMPT_SYSTEM_TASK · 提示词体系建设任务

> **版本**：v1.0
> **创建日期**：2026-05-03
> **归档路径**：`carefulxiao-cell/Synexa-iS-OIOS/00-master/PROMPT_SYSTEM_TASK_v1.0.md`
> **负责方**：iS-Core（裁决）+ 各工作空间（执行）
> **触发词**：`继续推进提示词体系任务`

---

## 一、任务定义

建立 Synexa iS 体系的提示词（Prompt / Workspace Spec / Skill）三层架构，实现「一处定义，全局调用，集中升级」，消除当前各工作空间规范重叠、维护分散、行为漂移的问题。

---

## 二、核心原则（已裁决，2026-05-03）

以下为全局自定义指令与工作空间规范设计的最高准则，经 iS-Core 与用户对齐确认。

### 2.1 提示词分层原则

| 层级 | 存放位置 | 作用范围 | 内容定位 |
|---|---|---|---|
| **全局自定义指令** | Manus「个性化」设置 | 所有对话 | 底线规则：角色定位 + 执行约束 + 沟通风格 |
| **工作空间规范** | 各 Project「项目指令」字段 | 该 Project 内所有对话 | 身份定义 + 职责边界 + Skill 引用声明 |
| **Skill 文件** | GitHub 仓库 `00-master/` | 任何引用它的工作空间 | 可复用能力模块，通过触发词激活 |
| **操作指令追踪** | `INSTRUCTION_TRACKER.md` | 记录用，不影响 AI 行为 | 审计工具，独立运作 |

**覆盖关系**：工作空间规范 > 全局自定义指令 > 默认行为。层级高的覆盖层级低的，不叠加。

### 2.2 全局自定义指令设计原则

全局指令只锚定三件事，不做任何超出这三件事的内容：

1. **角色定位**：AI 的默认工作模式（战略顾问）
2. **执行约束**：先对齐再动手；禁止未授权的工程操作；默认交付形式为文字+文档
3. **沟通风格**：精炼、结构化、不废话

模式切换前缀（快速回答/发散讨论/仅限本题/启动项目）作为轻量扩展保留，但触发逻辑必须严密。

### 2.3 提示词质量标准

- **信息密度优先**：每个字符都在传递一条规则，不写修饰性语言
- **规则语言 > 描述语言**：用条件句和优先级声明，不用「应该」「尽量」「避免」等模糊表达
- **边界条件完备**：每条规则必须包含「触发条件 + 执行动作 + 禁止行为」三要素
- **压缩率指标**：字符数 / 覆盖规则数，作为版本迭代的质量评估维度

### 2.4 词汇统一（已裁决）

| 概念 | 体系内术语 | 对应文件 |
|---|---|---|
| 用户向 AI 发出的操作命令 | **指令**（Instruction） | `INSTRUCTION_TRACKER.md` |
| 写给 AI 的系统规则/提示词 | **工作空间规范** / **Skill** | `iS_Instructions_All_Workspaces` / `*_SKILL.md` |
| 优化提示词的方法论 | **提示词工程**（Prompt Engineering） | `PROMPT_ENGINEERING_SKILL_v1.0.md` |

---

## 三、当前进展

### 已完成

| 产出物 | 路径 | 状态 |
|---|---|---|
| 任务情况汇总 Skill v1.0 | `00-master/TASK_SUMMARY_SKILL_v1.0.md` | ✅ 已裁决，已推送 |
| CONTEXT_OS.md 注册 TASK_SUMMARY_SKILL | `02-context-os/CONTEXT_OS.md` | ✅ 已推送 |
| 全局自定义指令 v2.0（高密度版） | Manus 个性化设置 | ✅ 本次交付，待用户粘贴 |
| 提示词体系三层架构定义 | 本文件第二节 | ✅ 已裁决 |
| 建立 `PROMPT_ENGINEERING_SKILL_v1.0.md` | `00-master/PROMPT_ENGINEERING_SKILL_v1.0.md` | ✅ 已完成，待裁决 |
| 重写 `iS_Instructions_All_Workspaces` → v2.0 | `00-overview/iS_Instructions_All_Workspaces_v2.0.md` | ✅ 已完成，待裁决 |
| 各工作空间规范引用 `TASK_SUMMARY_SKILL` | `00-overview/iS_Instructions_All_Workspaces_v2.0.md` | ✅ 已完成，包含在 v2.0 中 |

### 待推进

| 任务 | 优先级 | 说明 |
|---|---|---|
| 建立提示词版本迭代记录机制 | P2 | 记录「AI 行为偏离 → 根因 → 修正方式」 |

---

## 四、下一次接续指引

触发词：`继续推进提示词体系任务`

接续时，AI 读取本文件后，输出：
1. 当前进展确认（已完成 / 待推进）
2. 建议下一步优先推进的任务
3. 等待用户裁决后再动手

---

## 五、文件命名规范（已裁决，2026-05-16）

### 5.1 标准格式

```
[中文摘要]_[英文代号]_v[版本].md
```

**原则**：中文摘要在前，方便快速识别；英文代号在后，保持机器可读性与版本控制兼容性。

### 5.2 规则说明

| 字段 | 说明 | 示例 |
|---|---|---|
| 中文摘要 | 2-8 字，直接说明文件内容 | `提示词体系建设任务` |
| 英文代号 | 全大写，下划线分隔，与内容强绑定 | `PROMPT_SYSTEM_TASK` |
| 版本号 | `v主版本.次版本`，无版本迭代的文件可省略 | `v1.0` |

### 5.3 示例对照

| 旧命名 | 新命名 |
|---|---|
| `PROMPT_SYSTEM_TASK_v1.0.md` | `提示词体系建设任务_PROMPT_SYSTEM_TASK_v1.0.md` |
| `TASK_SUMMARY_SKILL_v1.0.md` | `任务情况汇总_TASK_SUMMARY_SKILL_v1.0.md` |
| `CONTEXT_OS.md` | `全局状态总账本_CONTEXT_OS.md` |
| `CORE_PRINCIPLES.md` | `核心原则_CORE_PRINCIPLES.md` |
| `WORKSPACE_REGISTRY_v2.1.md` | `工作空间注册表_WORKSPACE_REGISTRY_v2.1.md` |

### 5.4 迁移策略

- **新文件**：即时执行新规范
- **旧文件**：逐步迁移，不做全面清洗；每次更新旧文件时顺带重命名
- **例外**：`CONTEXT_OS.md` 等被大量文件引用的核心文件，重命名前需评估影响范围

---

## 六、关联文件

| 文件 | 路径 | 关系 |
|---|---|---|
| TASK_SUMMARY_SKILL_v1.0.md | `00-master/` | 本任务产出的第一个 Skill |
| CORE_PRINCIPLES.md | `00-master/` | 体系最高行为准则，提示词设计的上位文件 |
| iS_Instructions_All_Workspaces_v2.0.md | `00-overview/` | 现有工作空间规范，已用新方法论重写 |
| INSTRUCTION_TRACKER.md | `06-isync/` | 操作指令追踪，与本任务独立运作 |
| CONTEXT_OS.md | `02-context-os/` | 全局状态总账本，本任务重大进展须同步 |
