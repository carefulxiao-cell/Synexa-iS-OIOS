# Synexa iS Activation & Alignment Protocol｜SIA 全局级激活与对齐协议索引

> Version: v0.2.0
> Maintainer: iS-Core
> Status: Active — Foundation Skill / Global Governance Mechanism
> Skill Path: 04-skills/synexa-is-activation-alignment/
> Date: 2026-06-30

---

## 一、协议定位

SIA（Synexa iS Activation & Alignment）是 Synexa iS 的**全局级激活与对齐协议**，属于 Foundation Skill 层级，不归属于任何单一项目。

**宪法级定位**：SIA 是落实体系第一性原理（认知负荷最小化）的强制启动仪式。通过标准化的 Task Room 激活流程，确保执行体在介入复杂现实前，拥有唯一且清晰的真相来源（SSOT），避免判断力被碎片化信息稀释。

其核心职能是：在执行任何复杂任务前，将任务快速组织成 Task Room，调用对应的能力域（Capability Domain）、基础 Skill、专项 Skill 与执行体，并在执行前后完成数据源、版本、资产归属与发布状态的对齐检查。

---

## 二、适用范围

本协议适用于 Synexa iS 全域，包括但不限于：

- 所有 Task Room（任务室）
- 所有 Capability Domain（能力域）
- Foundation Skill 层与 Project / Theme Skill 层
- 各项目对话组（PCS）
- 外部执行体（Manus、GPT、Kimi、Claude Code、Kimi Claw 等）协作前的启动与对齐

---

## 三、触发词

以下触发词可激活 SIA 协议：

- 启动 SIA
- 按 SIA 执行
- 启动 SIA 巡检
- 启动 SIA 发布检查

---

## 四、Skill 主体位置

```
04-skills/synexa-is-activation-alignment/
├── SKILL.md                          ← Skill 入口文件
├── VERSION                           ← 当前版本 0.1.0
├── CHANGELOG.md                      ← 版本变更记录
├── agents/openai.yaml                ← GPT Skills 接口定义
├── references/
│   ├── sia_protocol.md               ← SIA 协议正文
│   ├── capability_asset_taxonomy.md  ← 能力资产分类
│   ├── data_source_audit_protocol.md ← 数据源审计协议
│   ├── execution_agent_packages.md   ← 执行体包定义
│   ├── operating_architecture.md     ← 运营架构参考
│   ├── release_checklist.md          ← 发布检查清单
│   └── test_cases.md                 ← 测试用例
├── scripts/
│   └── validate_sia_manifest.py      ← Manifest 校验脚本
└── dist/releases/
    └── synexa-is-activation-alignment_v0.1.0_skill.zip  ← GPT 安装包
```

---

## 五、与其他全局机制的关系

| 机制 | 关系说明 |
|------|----------|
| `ISYNC_PROTOCOL.md` | **任务生命周期闭环**：SIA 负责「开局对齐」，ISYNC 负责「收尾沉淀」。无 SIA 不开局，无 ISYNC 不收尾。 |
| `WORKSPACE_REGISTRY_v2.2.md` | SIA 激活的 Task Room 必须映射到注册表中已定义的工作空间。 |
| `Cross_Workspace_Collaboration_Protocol` | SIA 是任务启动层，跨工作空间协同协议是任务执行层，两者互补 |
| `synexa-collaboration-router` Skill | SIA 负责激活与对齐，Router 负责路由与交接，先 SIA 后 Router |
| `IS_CODE_PACKAGE_GOVERNANCE` | SIA 的发布检查流程引用代码包治理原则 |
| `CONTEXT_OS.md` | SIA 运行结果应回写至 CONTEXT_OS 的当前状态字段 |

---

## 六、强制检查点（人智关键不绕过）

在 SIA 的启动检查清单（Release Checklist）中，必须包含以下强制检查项：

- **高风险裁决确认**：本次任务是否涉及方向设定或高风险裁决？若是，必须确认已获得 iS-Core 或人类指挥官的明确授权，不可由系统自行替代。

---

## 七、应用说明

SIA 解决的核心问题是：每次开始一个新任务，执行体（AI / 人）对「当前状态」的认知是混乱的。没有 SIA 的情况下，每次开局都需要重新回答「我们现在在哪、上次说到哪、任务边界是什么、谁负责、用哪个版本的文件」——这些问题消耗大量认知资源，且每次答案可能不一致。SIA 将这些问题变成一个**标准化的启动仪式**，强制在任务开始前一次性对齐。

### 7.1 层面一：单次任务启动（最常用）

**触发时机：** 开始一个新的、有一定复杂度的任务前。

| 步骤 | 内容 | 目的 |
|---|---|---|
| 1. 读取基线 | 确认当前体系版本（超智基线 V3.11 / DIC V0.3）和 CONTEXT_OS 状态 | 确保执行体使用最新的真相来源 |
| 2. 明确任务边界 | 本次任务做什么、不做什么、交付物是什么 | 防止任务蔓延，减少认知负荷 |
| 3. 确认角色 | 谁是指挥官（人），谁是执行体（AI），谁做裁决 | 落实「人智关键不绕过」 |
| 4. 高风险检查 | 本次任务是否涉及方向设定或高风险裁决？ | 若是，必须先获得 iS-Core 授权 |
| 5. 确认资产 | 本次任务依赖哪些文件、数据、工具？版本是否最新？ | 防止使用错误版本 |

**示例：** 「启动②超智基线 V3.10 审核完善」即为一个 SIA 触发点。正确做法是先完成上述5步对齐，再开始审核。

### 7.2 层面二：跨工作空间任务交接

**触发时机：** 一个任务需要从一个工作空间（如 iS-Core）移交到另一个（如 iS-SCO 或某个 PCS）时。

SIA 确保接收方拿到的是一个结构化的任务包，包含：当前状态、已完成的部分、待完成的部分、关键决策和约束——而不是一堆聊天记录。

**示例：** iS-Core 完成项目最小定义（Step 0A）后，移交给项目专属 PCS 工作空间。SIA 确保 PCS 接手时，无需重新理解背景。

### 7.3 层面三：定期体系巡检

**触发词：** `启动 SIA 巡检`

**触发时机：** 定期（如每月一次）或在体系发生重大变更后。

SIA 检查所有活跃工作空间的状态是否与 CONTEXT_OS 一致，发现「已执行但未沉淀」的决策，触发 ISYNC 补录。

### 7.4 完整任务生命周期闭环

```
SIA（开局对齐）→ 任务执行 → ISYNC（收尾沉淀）→ PER（经验归库）→ 基线升级（闭环）
```

SIA 是入口，ISYNC 是出口，两者共同保障「每次任务都有始有终，经验不丢失」。

---

## 八、Patch Proposal（待后续工作空间处理）

以下文件建议在下一版本迭代中纳入 SIA 引用，但当前版本尚未存在，不强行创建：

1. `Synexa_Company_Intro_V3.11.md` — 建议将 SIA 纳入 Task Room Runtime Layer 启动协议
2. `Synexa_DIC_V0.3.md` — 建议标注 SIA 属于 Foundation / Global Governance Skill
3. `Synexa_iS_Data_Source_Audit_Protocol_v0.1.md` — 建议标注 SIA-Audit 与 synexa-baseline-auditor 的关系

上述文件由 iS-Matrix 负责在下一迭代中创建或更新，并提交 iS-Core 裁决后入库。
