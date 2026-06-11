# Collaboration Cases

> Version: v0.1.2  
> Effective Date: 2026-06-10  
> Maintainer: iS-Matrix  
> Use: Case log for Synexa Collaboration Router

## Case 001A: Synexa Website Visual System

### Original Task

Generate a world-class visual system prompt for the Synexa official website.

The task was not only a prompt-writing task. It involved turning a real collaboration experience into a reusable cross-workspace protocol and eventually a Skill.

### Why Collaboration Was Triggered

Collaboration was triggered because the task crossed multiple responsibility boundaries:

1. iS-SCO was needed for strategy reasoning:
   - brand altitude
   - visual direction
   - global benchmark logic
   - strategic fit with Synexa positioning

2. iS-Matrix was needed for structured production:
   - prompt template
   - SOP
   - Skill source files
   - reusable workflow asset

3. iS-Synexa PCS was needed for project execution:
   - website delivery
   - visual implementation
   - content and design coordination

4. Manus / Claude Code / Kimi Claw were needed for execution:
   - file creation
   - repository updates
   - package validation
   - possible GitHub commit

5. iS-Core was needed only if baseline governance was triggered:
   - whether "out of scope" should be upgraded into a global collaboration protocol
   - whether the protocol should become reusable across Synexa iS

### Collaboration Route

Recommended route:

1. iS-SCO:
   - complete strategic reasoning
   - identify that the issue is not just visual output but cross-workspace coordination

2. iS-Core:
   - intervene only if this becomes a baseline collaboration rule
   - authorize Skill / SOP production if baseline upgrade is required

3. iS-Matrix:
   - create the collaboration router Skill
   - create templates, prompt pack, validation script, and case log

4. Manus / Claude Code:
   - create files
   - validate structure
   - package the Skill
   - update GitHub

5. iS-Synexa PCS:
   - use the resulting visual system prompt and workflow in the website project

6. Return feedback:
   - report execution results
   - identify missing fields
   - propose patches

### Expected Outputs

The collaboration should produce:

- `synexa-collaboration-router/SKILL.md`
- `agents/openai.yaml`
- `references/collaboration_protocol.md`
- `references/handoff_template.md`
- `references/return_feedback_template.md`
- `references/execution_principles.md`
- `references/agent_prompt_pack.md`
- `references/patch_log_template.md`
- `references/cases.md`
- `scripts/validate_handoff.py`
- packaged Skill archive
- GitHub update
- return feedback package

### Test Focus

This case tests whether the router can:

1. Identify a cross-workspace task.
2. Assign one main owner.
3. Separate strategy reasoning from template production.
4. Separate project execution from baseline governance.
5. Generate a usable handoff package.
6. Require return feedback.
7. Avoid sending all collaboration tasks to iS-Core.

### Lessons

1. 越界提示不应只用于停止任务。
2. 当任务天然跨越多个空间时，越界就是协同信号。
3. 当前空间应先完成自己能完成的高价值部分。
4. 协同任务必须有一个主责空间。
5. 下游执行体需要完整上下文，而不是一句“请处理”。
6. 回流反馈是系统进化的关键。
7. 实战案例应成为 patch note 的来源。
8. iS-Core 介入的关键不是“任务复杂”，而是“是否涉及基线、全局协议、职责重构或冲突裁决”。

### Patch Opportunities

Potential patches discovered from this case:

1. Add a standard handoff validation script.
2. Add a reusable downstream agent prompt pack.
3. Add a collaboration level system.
4. Add a rule: every Level 2 or Level 3 collaboration must include return feedback.
5. Add a rule: every system-level collaboration should create or update a case log.
6. Clarify when iS-Core must be involved.
7. Clarify difference between iS-Matrix production and PCS execution.
8. Prevent standard collaboration tasks from being unnecessarily escalated to iS-Core.

---

## Case 001B: Collaboration Router Self-Test

### Original Task

Test whether `synexa-collaboration-router` has been installed, whether it automatically triggers, and whether it can still be used when the current conversation cannot confirm installation or loading status.

### Why Collaboration Was Triggered

This case was created after a manual Case 001 test revealed a reporting ambiguity:

- The collaboration protocol was manually applied successfully.
- However, the current conversation environment could not confirm whether the Skill had been installed, discovered, or automatically loaded.
- Therefore, saying "test success" without qualification could be misleading.
- The correct result should distinguish between:
  - automatic skill invocation success
  - manual protocol success
  - runtime limitation
  - workflow failure

### Runtime Visibility Problem

The current environment may not expose:

- whether the Skill exists in the user's Skills Library
- whether the Skill has been installed
- whether the Skill is discoverable by the current assistant instance
- whether it was automatically loaded
- whether the output came from Skill invocation or from manually following the protocol text

### Required Expression Rule

When installation or loading status cannot be confirmed, the assistant must say:

> 当前无法确认 Skill 是否已安装或加载；可先按协议手动运行一次，并建议用户在 Skills Library 中确认。

The assistant must not say:

- "Skill 已安装成功"
- "Skill 已自动触发成功"
- "测试证明 Skill 自动调用成功"

unless the environment provides direct confirmation.

### Manual Fallback Route

If the Skill is not discoverable, not installed, or not loaded in the current conversation:

1. State the runtime limitation.
2. Apply the collaboration routing workflow manually.
3. Output the requested collaboration route, handoff package, feedback package, prompt, case log, or patch note.
4. Record execution mode as:

`manual protocol run`

5. Mark the limitation as:

`runtime limitation, not workflow failure`

6. Recommend that the user confirm the Skill in the Skills Library.

### Expected Outputs

For a self-test, the output should include:

- Skill name
- Test task
- Visibility status
- Automatic trigger status
- Manual fallback status
- Execution mode
- Result classification
- Recommended next validation step

### Result Classification

Use one of the following:

#### Automatic Trigger Success

Use only when the environment confirms the Skill was discovered and loaded automatically.

#### Manual Protocol Success

Use when the protocol was applied correctly, but Skill installation or automatic loading cannot be confirmed.

#### Runtime Limitation

Use when the environment cannot see installation, loading, or Skills Library status.

#### Workflow Failure

Use only when the collaboration routing workflow itself cannot be completed.

Do not classify runtime limitation as workflow failure.

### Test Prompt Example

```text
请测试 synexa-collaboration-router 是否会在跨工作空间任务中自动触发。
任务：为 Synexa 官网视觉系统生成跨工作空间协同 route、handoff package、return feedback requirement，并说明是否需要 iS-Core 介入。
```

### Expected Correct Response Pattern

```text
当前无法确认 Skill 是否已安装或加载；可先按协议手动运行一次，并建议用户在 Skills Library 中确认。

Execution mode: manual protocol run
Result classification: manual protocol success + runtime limitation

以下按 synexa-collaboration-router 协议手动执行：
...
```

### Lessons

1. 手动运行协议成功，不等于 Skill 自动触发成功。
2. 当前对话环境不可见的安装状态，必须如实说明。
3. Skill 自测案例应独立于业务协同案例。
4. 安装不可见是 runtime limitation，不是 workflow failure。
5. 测试结果必须分层表达，避免“看似成功，实际未验证自动加载”的误判。

### Patch Opportunities

1. Add runtime visibility rule to `SKILL.md`.
2. Add manual fallback path to `SKILL.md`.
3. Add installation visibility rule to `collaboration_protocol.md`.
4. Add manual fallback path to `collaboration_protocol.md`.
5. Split Case 001 into 001A business test and 001B self-test.
6. Add patch entries for installation visibility and fallback behavior.
