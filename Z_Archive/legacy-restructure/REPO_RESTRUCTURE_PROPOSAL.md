# 仓库目录重构与清理草案 (v1.0)

基于 `REPO_GOVERNANCE_v1.0.md` 的治理规则，以及当前仓库的实际文件分布，我梳理了以下重构与清理方案。

## 一、 根目录冗余文件清理
**现状**：根目录下存在一些历史遗留文件。
**动作**：
1. `GPT_Sync_Package_20260409.md` → 移动至 `99-archive/`（历史同步包）
2. `REPO_INDEX.md` → 移动至 `99-archive/`（已被 `REPO_GOVERNANCE_v1.0.md` 替代）
3. `README.md` → 保留，但需更新内容以指向 `00-master/REPO_GOVERNANCE_v1.0.md` 和 `02-context-os/CONTEXT_OS.md`。

## 二、 00-master（全局治理层）重构
**现状**：文件极多（40+），包含大量旧版架构图、旧版指令包、旧版矩阵文件。
**动作**：
1. **架构图归档**：将 `SYNEXA_GLOBAL_ARCHITECTURE_v1.0` 到 `v1.6` 移动至 `00-master/archive/`，仅保留最新的 `v1.7`。
2. **旧版文件归档**：
   - `F02_INSTRUCTION_PACKAGE_v1.0.md` (保留 v1.1)
   - `IS_MATRIX_CAPABILITY_ATOMS_v1.0.md` (保留 v2.0)
   - `MATRIX_ATOMS_METHOD_SOURCES_v1.0.csv` (保留 v1.1)
3. **不合规文件移出**：
   - `W01_INSTRUCTION_PACKAGE_v1.5.md`、`F06_SUPPLEMENT_INSTRUCTION_v1.0.md` 等具体指令包，应移动至 `06-isync/` 或对应项目的 `03-projects/` 目录下。
   - `IS_SKILL_BOOTSTRAP_v1.0.md`、`PROMPT_ENGINEERING_SKILL_v1.0.md` 等 Skill 相关文件，应移动至 `06-skills/` 或 `05-sop/`。

## 三、 00-overview（认知基线层）重构
**现状**：包含大量旧版 SCI（V3.7, V3.8, V3.9）和一些旧的推演报告。
**动作**：
1. **SCI 旧版归档**：将 `Synexa_Company_Intro_V3.7.md`、`V3.8.md`、`V3.9.md` 移动至 `00-overview/archive/`，仅保留最新的 `V3.11.md` 及其 HTML。
2. **推演报告移出**：
   - `Synexa_Business_Model_Deduction.md`
   - `Synexa_Ecosystem_Architecture_Deduction.md`
   - `Synexa_Strategic_Thought_Comparison_Report.md`
   - 这些属于早期的战略推演，应移动至 `99-archive/00-overview/` 或建立一个专门的 `00-overview/deductions/` 目录存放。
3. **工作空间指令移出**：
   - `GPT_Project_Instructions_SynexaiS_v26.1.5.md`
   - `GPT_Project_Instructions_iSCore_v26.1.6.md`
   - `Manus_Project_Instructions_v26.1.6.md`
   - `iS_Instructions_All_Workspaces_v2.0.md`
   - 这些属于应用管理范畴，应移动至 `00-master/` 或建立专门的 `07-app-configs/` 目录。

## 四、 06-isync 与 06-tracker 合并
**现状**：存在 `06-isync/` 和 `06-tracker/` 两个目录，且都包含 `GLOBAL_INSTRUCTION_TRACKER.md`。
**动作**：
1. 删除 `06-tracker/` 目录。
2. 将 `06-tracker/GLOBAL_INSTRUCTION_TRACKER.md` 的内容（如有更新）合并到 `06-isync/GLOBAL_INSTRUCTION_TRACKER.md` 中。
3. 统一使用 `06-isync/` 作为指令同步与追踪的唯一目录。

## 五、 04-skills 与 06-skills 合并
**现状**：存在 `04-skills/`（包含 synexa-is-activation-alignment）和 `06-skills/`（包含 S3-N-Grid）。
**动作**：
1. 将 `04-skills/synexa-is-activation-alignment` 移动至 `06-skills/`。
2. 删除空的 `04-skills/` 目录。

## 六、 03-projects（项目层）清理
**现状**：存在散落的文件。
**动作**：
1. `NTogether_Architecture_Draft.md` → 移动至 `03-projects/NTogether/`（需新建目录）。

## 七、 05-sop（SOP层）清理
**现状**：存在非 SOP 文件。
**动作**：
1. `iS-Publish_PCS_v0.1.md` → 移动至 `03-projects/iS-Publish/` 或 `00-master/`（作为工作空间定义）。

---

**请确认：**
以上草案是否符合你的预期？如果同意，我将编写脚本一键执行上述移动和归档操作。如果有需要调整的地方，请指出。
