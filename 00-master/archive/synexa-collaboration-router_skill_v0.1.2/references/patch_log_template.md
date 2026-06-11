# Patch Log Template

> Version: v0.1.2  
> Effective Date: 2026-06-10  
> Maintainer: iS-Matrix  
> Use: Record reusable workflow improvements discovered during collaboration

## Patch ID

PATCH-[YYYYMMDD]-[###]

## Related Case

Case ID:

Case Name:

## Date

YYYY-MM-DD

## Trigger Problem

Describe the problem that triggered this patch.

Examples:

- Workspace boundary was unclear.
- Handoff package missed required file path.
- Downstream agent lacked enough context.
- Return feedback was not requested.
- Script validation failed.
- GitHub destination was ambiguous.
- Skill trigger description was too weak.
- Template became too heavy for a simple task.
- Skill installation status was not visible in the current runtime.
- Manual protocol execution was confused with automatic skill invocation.

## Proposed Change

Describe the proposed change.

Keep it practical and patch-sized.

## Affected Files

- `SKILL.md`
- `references/collaboration_protocol.md`
- `references/handoff_template.md`
- `references/return_feedback_template.md`
- `references/execution_principles.md`
- `references/agent_prompt_pack.md`
- `references/patch_log_template.md`
- `references/cases.md`
- `scripts/validate_handoff.py`
- Other: `[path]`

## Decision

- [ ] Accepted
- [ ] Rejected
- [ ] Deferred
- [ ] Needs iS-Core decision
- [ ] Needs iS-SCO calibration
- [ ] Needs execution test

Decision notes:

[Write notes here.]

## Version Impact

- [ ] No version change
- [ ] Patch version update
- [ ] Minor version update
- [ ] Major version update

Suggested new version:

v[major].[minor].[patch]

---

# Patch Entries

## PATCH-001: Installation Visibility Expression Rule

### Related Case

Case ID: Case 001B  
Case Name: Collaboration Router Self-Test

### Date

2026-06-10

### Trigger Problem

During manual testing, the current conversation environment could not confirm whether `synexa-collaboration-router` had been installed, discovered, or automatically loaded.

Previous wording risked implying that a manual protocol run proved automatic Skill invocation.

### Proposed Change

Add an explicit expression rule:

When the current environment cannot confirm whether the Skill has been installed or loaded, do not claim installation success or automatic invocation success.

Required wording:

> 当前无法确认 Skill 是否已安装或加载；可先按协议手动运行一次，并建议用户在 Skills Library 中确认。

### Affected Files

- `SKILL.md`
- `references/collaboration_protocol.md`
- `references/cases.md`
- `references/patch_log_template.md`

### Decision

- [x] Accepted
- [ ] Rejected
- [ ] Deferred
- [ ] Needs iS-Core decision
- [ ] Needs iS-SCO calibration
- [ ] Needs execution test

Decision notes:

Accepted as a runtime honesty and testing clarity patch. This does not change the core collaboration workflow.

### Version Impact

- [ ] No version change
- [x] Patch version update
- [ ] Minor version update
- [ ] Major version update

Suggested new version:

v0.1.2

---

## PATCH-002: Manual Fallback Path

### Related Case

Case ID: Case 001B  
Case Name: Collaboration Router Self-Test

### Date

2026-06-10

### Trigger Problem

If the Skill is not discoverable, not installed, or not loaded in the current conversation, the workflow should not stop or be treated as failed.

The prior version did not explicitly define a manual fallback path.

### Proposed Change

Add manual fallback rule:

If the skill is not discoverable, not installed, or not loaded in the current conversation, manually apply the collaboration routing workflow and record this as a runtime limitation, not a workflow failure.

中文说明：

如果 Skill 当前不可发现、未安装或未加载，不应视为任务失败；应手动应用协同路由流程，并将其记录为运行环境限制。

### Affected Files

- `SKILL.md`
- `references/collaboration_protocol.md`
- `references/cases.md`
- `references/patch_log_template.md`

### Decision

- [x] Accepted
- [ ] Rejected
- [ ] Deferred
- [ ] Needs iS-Core decision
- [ ] Needs iS-SCO calibration
- [ ] Needs execution test

Decision notes:

Accepted as a runtime resilience patch. It preserves workflow continuity without pretending automatic Skill invocation occurred.

### Version Impact

- [ ] No version change
- [x] Patch version update
- [ ] Minor version update
- [ ] Major version update

Suggested new version:

v0.1.2

---

## PATCH-003: Split Case 001

### Related Case

Case ID: Case 001  
Case Name: Synexa Website Visual System / Collaboration Router Self-Test

### Date

2026-06-10

### Trigger Problem

The original Case 001 mixed two different test purposes:

1. Testing cross-workspace collaboration for the Synexa Website Visual System.
2. Testing whether `synexa-collaboration-router` itself was installed, automatically triggered, or manually applied.

This created ambiguity in interpreting test results.

### Proposed Change

Split the case into:

1. Case 001A: Synexa Website Visual System
   - Tests website visual system cross-workspace collaboration.

2. Case 001B: Collaboration Router Self-Test
   - Tests installation visibility, automatic trigger status, and manual fallback behavior.

### Affected Files

- `references/cases.md`
- `references/collaboration_protocol.md`
- `references/patch_log_template.md`

### Decision

- [x] Accepted
- [ ] Rejected
- [ ] Deferred
- [ ] Needs iS-Core decision
- [ ] Needs iS-SCO calibration
- [ ] Needs execution test

Decision notes:

Accepted as a test clarity patch. This makes future validation cleaner and prevents false success reporting.

### Version Impact

- [ ] No version change
- [x] Patch version update
- [ ] Minor version update
- [ ] Major version update

Suggested new version:

v0.1.2
