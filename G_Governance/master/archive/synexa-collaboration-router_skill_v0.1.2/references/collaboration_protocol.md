# Synexa Collaboration Protocol

> Version: v0.1.2  
> Effective Date: 2026-06-10  
> Maintainer: iS-Matrix  
> Scope: Synexa iS cross-workspace routing and collaboration handoff

## 1. 协议目的

本协议用于将“越界提示”升级为“协同任务编排”。

当任务同时涉及战略推演、结构化生产、项目执行、文件操作、基线裁决或多智能体协作时，不应简单停止，而应识别主责空间、协作空间，并生成可执行的交接任务包与回流反馈包。

一句话：

> 越界不是错误终点，而是协同启动信号。

## 2. 适用范围

适用于 Synexa iS 下列工作空间与执行体之间的协同：

- iS-Core：基线治理、项目孵化、裁决
- iS-SCO：战略推演、风险评估、决策支持
- iS-Matrix：SOP、模板、提示词、Skill、规程固化
- PCS：具体项目执行
- iS-Hub：外部工具、Agent 情报与评估
- iS-Lab：灵感与未成熟想法前测
- Manus：文件、仓库、流程执行
- Kimi：长文本理解、资料整理、辅助推理
- Claude Code / Kimi Claw：代码、仓库、脚本、自动化执行

## 3. 触发条件

出现以下任一情况时，触发协同路由：

1. 用户任务跨越两个或以上工作空间职责。
2. 当前工作空间可完成部分任务，但无法完成全部任务。
3. 任务需要先推演、再固化、再执行。
4. 任务需要文件创建、GitHub 操作、代码校验或仓库提交。
5. 任务需要 iS-Core 做基线裁决。
6. 任务产生了可复用流程，应形成 SOP、模板或 Skill。
7. 执行过程中发现旧模板、旧流程、旧职责边界需要修补。
8. 当前环境无法确认 Skill 是否已安装、可发现或已自动加载，需要手动降级运行协同路由流程。

## 4. 安装状态与运行可见性规则

在 ChatGPT 对话环境中，当前智能体不一定能确认某个 Skill 是否已经：

- 安装
- 出现在 Skills Library
- 被当前对话发现
- 被自动触发
- 被完整加载

因此，任何执行者都必须遵守以下表达规则：

1. 当当前环境无法确认 Skill 是否已安装或加载时，不得声称 Skill 已安装成功。
2. 当只是手动按协议执行时，不得声称 Skill 已自动调用成功。
3. 应明确说明：

> 当前无法确认 Skill 是否已安装或加载；可先按协议手动运行一次，并建议用户在 Skills Library 中确认。

4. 测试报告中必须区分：
   - automatic trigger success
   - manual protocol success
   - runtime limitation
   - workflow failure

## 5. 手动降级路径

If the skill is not discoverable, not installed, or not loaded in the current conversation, manually apply the collaboration routing workflow and record this as a runtime limitation, not a workflow failure.

中文说明：

如果 Skill 当前不可发现、未安装或未加载，不应视为任务失败；应手动应用协同路由流程，并将其记录为运行环境限制。

手动降级步骤：

1. 声明当前运行限制。
2. 说明无法确认 Skill 是否已安装或加载。
3. 手动执行协同路由 workflow。
4. 输出正常的 collaboration route、handoff package、return feedback package、agent prompt、case log 或 patch note。
5. 在结果中标注：`execution mode: manual protocol run`。
6. 建议用户在 Skills Library 中确认安装状态。
7. 如由 Manus 测试，应进一步检查文件是否已落盘、Skill 是否已打包、是否已上传或安装。

## 6. 协同分级

### Level 0: 单空间任务

一个空间即可完成。

处理方式：

- 直接执行
- 不生成协同任务包

### Level 1: 轻协同任务

主责清晰，只需另一个空间补充。

处理方式：

- 当前空间完成主体输出
- 附加简短交接说明

### Level 2: 标准协同任务

至少两个空间有明确职责。

处理方式：

- 明确主责空间
- 明确协作空间
- 生成完整 handoff package
- 要求 return feedback

iS-Core 介入边界：

- Level 2 标准协同任务默认不必提交 iS-Core。
- 只要主责清晰、无基线冲突、无优先级冲突、无职责重构，就由主责空间协调推进。
- 避免把所有标准协同任务都上升到治理层。

### Level 3: 系统级协同任务

涉及基线、项目、仓库、Skill、SOP 或多个智能体。

处理方式：

- 判断是否需要 iS-Core 裁决
- 必须生成 handoff package
- 必须生成 return feedback package
- 必须记录 case log
- 必须提出 patch opportunities

iS-Core 介入边界：

Level 3 不等于自动提交 iS-Core。只有涉及以下事项时，才提交 iS-Core：

- 基线变更
- 全局协议变更
- 项目立项
- 职责重构
- 优先级冲突
- 跨空间冲突裁决
- 需要授权进入 GitHub 全局基线或制度文件

治理层不应被执行细节淹没。能由主责空间解决的协同执行问题，不上升到 Core。

## 7. 主责空间判断规则

主责空间由“任务主要价值产出”决定，而不是由用户当前所在空间决定。

### iS-Core 作为主责

当任务核心是：

- 基线裁决
- 优先级确认
- 项目立项
- 职责归位
- 全局状态变更
- 多空间冲突裁决

不应将以下任务默认交给 iS-Core：

- 普通文件创建
- 标准 handoff package 生成
- 常规 SOP / 模板生产
- 无冲突的 PCS 执行拆解
- 无基线变更的 Skill 小版本修正
- 普通下游 agent prompt 生成
- 单纯的 Skill 安装状态不可见问题

### iS-SCO 作为主责

当任务核心是：

- 战略推演
- 风险揭示
- 方案权衡
- 期望值判断
- 反向验证
- 决策模型构建

### iS-Matrix 作为主责

当任务核心是：

- SOP
- 模板
- 提示词
- Skill 源文件
- 操作手册
- 标准规程
- 数字员工指令
- Skill runtime fallback rule
- Skill test case refinement

### PCS 作为主责

当任务核心是：

- 项目推进
- 具体交付
- 执行拆解
- 时间节点
- 项目资产落地
- 业务场景实施

### Manus / Claude Code / Kimi Claw 作为主责

当任务核心是：

- 创建文件
- 修改仓库
- 编写代码
- 执行脚本
- 打包
- 校验
- 推送 GitHub
- 验证 Skill 文件结构
- 验证 Skill 是否可打包上传

### iS-Hub 作为主责

当任务核心是：

- 外部工具调研
- Agent 案例评估
- 平台能力比较
- 智能体能力地图

### iS-Lab 作为主责

当任务核心是：

- 未成熟想法
- 早期概念
- 新业务苗头
- 最小验证

## 8. 当前空间处理原则

当前空间不得因越界完全停摆。

应先判断：

1. 当前空间能合法完成什么？
2. 哪些部分必须转交？
3. 下游需要什么上下文？
4. 谁必须回流反馈？
5. 是否需要补丁记录？
6. 是否真的需要 iS-Core 裁决？
7. 当前环境是否能确认 Skill 已安装或自动加载？
8. 如不能确认，是否应启动 manual fallback？

当前空间必须完成“最有价值且不冒充全能”的部分。

## 9. 交接任务包标准

交接任务包必须包含：

- Task Name
- Original User Intent
- Current Workspace Judgment
- Collaboration Trigger
- Main Owner
- Collaborators
- Completed Inputs
- Downstream Tasks
- Output Requirements
- Return Feedback Requirement

标准模板见：

`handoff_template.md`

## 10. 回流反馈包标准

回流反馈包必须包含：

- Received Task
- Completed Work
- Issues Found
- Upstream Calibration
- Template or SOP Patch Suggestions
- Baseline Decision Needed
- GitHub Update Suggested

标准模板见：

`return_feedback_template.md`

## 11. 补丁机制

当实战任务暴露以下问题时，必须提出 patch suggestion：

- 工作空间职责边界不清
- handoff 字段不够用
- 下游 agent 执行困难
- GitHub 路径不清
- Skill 触发条件不准
- 模板太重或太轻
- 回流反馈缺失
- 旧 SOP 与新实践不一致
- Skill 安装、发现、加载状态不可见
- 手动运行与自动调用被混淆
- 测试案例未区分业务案例与 Skill 自测案例

补丁不等于立即修改。

补丁流程：

1. 记录 patch suggestion
2. 标注 affected files
3. 判断是否需要 iS-Core 裁决
4. 若无需裁决，由 iS-Matrix 更新模板
5. 若涉及基线，由 iS-Core 裁决后再更新
6. Manus 或代码执行体负责落盘与提交

## 12. 版本管理

建议采用语义化轻量版本：

- v0.1：初始草案
- v0.1.1：落盘、校验、Markdown 与治理边界小修
- v0.1.2：安装状态不可见、手动降级路径与测试案例拆分补丁
- v0.2：首次实战修订
- v1.0：稳定可复用版本
- v1.x：小修补
- v2.0：结构性升级

每次修改必须记录：

- date
- trigger problem
- changed files
- version impact

## 13. 示例案例

### Case 001A: Synexa Website Visual System

用于测试官网视觉系统任务的跨工作空间协同。

重点测试：

- 是否能识别 iS-SCO、iS-Matrix、PCS、Manus、iS-Core 的不同职责
- 是否能生成 handoff package
- 是否能避免 iS-Matrix 冒充战略推演或项目执行
- 是否能识别 iS-Core 仅在全局协议升级时介入

### Case 001B: Collaboration Router Self-Test

用于测试 synexa-collaboration-router 本身是否已安装、是否自动触发、如不能自动触发时是否可以手动降级运行。

重点测试：

- 是否诚实说明安装状态不可见
- 是否区分自动触发成功与手动协议成功
- 是否在不可确认时启动 manual fallback
- 是否将不可加载记录为 runtime limitation，而不是 workflow failure
