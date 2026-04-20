# iS-Core 指令追踪表（Instruction Tracker）

> **维护主体**：iS-Core（智核中枢）
> **版本**：v1.5
> **最后更新**：2026-04-20
> **作用**：追踪 Core 工作空间下发的所有指令包的完整生命周期，确保指令不遗漏、不冲突、可追溯。

---

## 当前指令汇总表（截至 2026-04-20）

| 编号 | 描述 | 优先级 | 批次 | 状态 | 核心设计共识 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| SOP-001 | 建立全局18步工作流标准 | P1 | B1 | ✅ 已完成 | 写入 `SYNEXA_IS_BASE_FRAMEWORK_v1.0.md` 第六维度；分三大阶段共18步：分析层1-5 / 执行层6-11 / 沉化层12-18 | commit `4fdde5a` |
| PROJ-001 | NexFlow·Synexa Step 0A 最小定义 | P1 | B1 | ✅ 已完成 | 原 iS-GlobalPM，已重命名为 NexFlow·Synexa；G·集团级，P1；写入 `03-projects/_INDEX.md` | commit `4fdde5a` |
| ARCH-001 | 架构图 v1.4 → v1.5 迭代 | P2 | B2 | ✅ 已完成 | 左侧18步椭圆框竖排，虚线映射至右侧五节点；右侧主架构结构不变；以用户审定 v1.4.2 为终版 | commit `efd1ad3` |
| ARCH-002 | 架构图终版确认（v1.4.2 入仓） | P1 | B2 | ✅ 已完成 | 用户审定终版入仓为 `Synexa_iS_Base_Architecture_v1.4.2.webp`，同时存为 `v1.5_FINAL.webp` | commit `a8b947a` |
| SOP-002 | SOP_007 v1.0 发布（指令汇总体系级基线） | P1 | B2 | ✅ 已完成 | 响应 NexFlow PCS ISYNC 通报，裁决通过；定义标准字段、状态枚举、批次规则、废弃协议、协作约定 | commit `2b75d52` |
| SOP-003 | GLOBAL_INSTRUCTION_TRACKER.md 建立 | P1 | B2 | ✅ 已完成 | 初始化 `06-isync/GLOBAL_INSTRUCTION_TRACKER.md`，录入6个项目摘要行；各项目里程碑时推送摘要 | commit `2b75d52` |
| SOP-004 | SOP_007 升级至 v1.1 | P1 | B2 | ✅ 已完成 | 新增 FBR 触发协议（触发词 `汇总推送`）+ 经验反哺升级协议 + 执行主体定义（「中枢-xxxx」） | commit `3765476` |
| SOP-005 | ISYNC_PROTOCOL 升级至 v1.2 | P1 | B2 | ✅ 已完成 | 新增触发词三 `汇总推送 [项目代号]`；定义 FBR 主动读取 GitHub 文件的执行序列 | commit `3765476` |
| SOP-006 | INSTRUCTION_TRACKER 字段升级至 v1.4 | P1 | B2 | ✅ 已完成 | 编号语义化（DEC/ARCH/SOP/SYNC/PROJ）；状态枚举扩展至8种；新增备注字段 | commit `3463638` |
| DEC-001 | 下发 NexFlow 追踪表补建指令 | P1 | B2 | 📋 指令已下发·待项目执行 | NexFlow 补建专属 INSTRUCTION_TRACKER，按 SOP_007 规范清洗历史指令，编号语义化 | 写入 `DEC-001_NexFlow_Tracker_Init.md` |
| DEC-002 | NexFlow 产品族命名体系裁决 | P1 | B2 | ✅ 已完成 | NexFlow 为产品族主线；NexFlow·Synexa = 超智内部全局项管；NexFlow·iS = NexFlow 产品开发建构管理 | commit `964f4ed` |
| SYNC-001 | GPT Project 文件同步（本次批次） | P2 | B2 | 🔄 已推送·待用户确认 | 需上传：架构图终版 / SOP_007 / ISYNC_PROTOCOL / INSTRUCTION_TRACKER / CONTEXT_OS / _INDEX | 用户手动操作项 |
| PROJ-002 | NexFlow·Synexa Step 0B 启动检查 | P1 | B3 | 🔒 依赖锁定 | 在 iS-NexFlow V3.x 迭代稳定后立即启动，建立专属 PCS 工作空间 | 前置：NexFlow V3.x 稳定 |

---

## 已废弃指令

| 编号 | 描述 | 废弃时间 | 废弃原因 | 替代指令 |
| :--- | :--- | :--- | :--- | :--- |
| （暂无） | — | — | — | — |

---

## 执行批次策略

- **并行条件**：同一批次内指令须满足「文件不冲突 + 无前后依赖」方可并行
- **硬性规则**：Schema 变更必须单独成批，不得与业务逻辑指令混批
- **废弃协议**：删除文件 → 标记 🚫 → 记录原因，三步缺一不可

---

*注：每次生成新指令包后，必须同步更新此表。策略室每次回复末尾必须附上最新完整汇总表。*
