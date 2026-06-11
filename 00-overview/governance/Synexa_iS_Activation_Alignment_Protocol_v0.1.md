# Synexa iS Activation & Alignment Protocol｜SIA 全局级激活与对齐协议索引

> Version: v0.1.0
> Maintainer: iS-Core
> Status: Active — Foundation Skill / Global Governance Mechanism
> Skill Path: 04-skills/synexa-is-activation-alignment/
> Date: 2026-06-12

---

## 一、协议定位

SIA（Synexa iS Activation & Alignment）是 Synexa iS 的**全局级激活与对齐协议**，属于 Foundation Skill 层级，不归属于任何单一项目。

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
| `Cross_Workspace_Collaboration_Protocol` | SIA 是任务启动层，跨工作空间协同协议是任务执行层，两者互补 |
| `synexa-collaboration-router` Skill | SIA 负责激活与对齐，Router 负责路由与交接，先 SIA 后 Router |
| `IS_CODE_PACKAGE_GOVERNANCE` | SIA 的发布检查流程引用代码包治理原则 |
| `CONTEXT_OS.md` | SIA 运行结果应回写至 CONTEXT_OS 的当前状态字段 |

---

## 六、Patch Proposal（待后续工作空间处理）

以下文件建议在下一版本迭代中纳入 SIA 引用，但当前版本尚未存在，不强行创建：

1. `Synexa_iS_Operating_Architecture_v2.0.md` — 建议将 SIA 纳入 Task Room Runtime Layer 启动协议
2. `Synexa_iS_Capability_Asset_Taxonomy_v0.1.md` — 建议标注 SIA 属于 Foundation / Global Governance Skill
3. `Synexa_iS_Data_Source_Audit_Protocol_v0.1.md` — 建议标注 SIA-Audit 与 synexa-baseline-auditor 的关系

上述文件由 iS-Matrix 负责在下一迭代中创建或更新，并提交 iS-Core 裁决后入库。
