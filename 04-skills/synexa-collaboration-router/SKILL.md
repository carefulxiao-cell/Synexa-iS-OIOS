---
name: synexa-collaboration-router
description: coordinate synexa is cross-workspace collaboration when a user request spans multiple responsibilities, including strategy reasoning, sop/template/prompt production, skill creation, project execution, github or file handoff, baseline governance, and routing between is-core, is-sco, is-matrix, pcs, manus, kimi, claude code, kimi claw, or other execution agents. use to generate collaboration routes, handoff packages, return feedback packages, downstream agent prompts, case logs, and patch notes.
---

# Synexa Collaboration Router

> Version: v0.1.2  
> Effective Date: 2026-06-10  
> Maintainer: iS-Matrix  
> Scope: Synexa iS cross-workspace collaboration routing

## Purpose

Use this skill when a user task crosses more than one Synexa iS workspace boundary.

This skill converts a simple "out of scope" signal into a collaboration route, handoff package, return feedback package, downstream agent prompt, and patchable workflow record.

The core purpose is:

> When a task crosses multiple agent responsibilities, turn boundary overflow into coordinated execution.

## Core Rule

Do not stop only because a task is out of scope.

Instead:

1. Identify the current workspace.
2. Identify whether the task is single-owner or cross-workspace.
3. Assign one main owner.
4. List collaborators.
5. Complete the most valuable part the current workspace can legitimately perform.
6. Generate a handoff package for downstream spaces or agents.
7. Require return feedback.
8. Capture patch opportunities.

Never pretend one workspace can do everything.

## Runtime Visibility Rule

The current conversation may not be able to confirm whether this skill has been installed, discovered, or automatically loaded.

When the environment cannot confirm installation or loading status:

- Do not claim that the skill is installed.
- Do not claim that the skill was automatically invoked.
- Do not describe a manual protocol run as an automatic skill-trigger success.
- State clearly: "当前无法确认 Skill 是否已安装或加载；可先按协议手动运行一次，并建议用户在 Skills Library 中确认。"

If the skill is not discoverable, not installed, or not loaded in the current conversation, manually apply the collaboration routing workflow and record this as a runtime limitation, not a workflow failure.

中文说明：

如果 Skill 当前不可发现、未安装或未加载，不应视为任务失败；应手动应用协同路由流程，并将其记录为运行环境限制。

## Manual Fallback Path

Use this fallback path when automatic skill availability is unclear:

1. Declare runtime limitation.
2. Apply the workflow manually.
3. Produce the required route, handoff package, feedback package, prompt, case log, or patch note.
4. Mark the execution mode as: `manual protocol run`.
5. Recommend that the user confirm installation in the Skills Library.
6. If testing the skill itself, distinguish between:
   - automatic trigger success
   - manual protocol success
   - runtime limitation
   - workflow failure

Do not confuse these states.

## Workflow

### Step 1: Parse the user task

Identify:

- original user intent
- requested deliverable
- strategic reasoning component
- SOP / template / prompt production component
- project execution component
- file / GitHub / repository operation component
- baseline governance component
- external execution agent component

### Step 2: Detect collaboration trigger

A collaboration trigger exists when the task requires two or more of:

- iS-Core baseline judgment or system governance
- iS-SCO strategy reasoning or risk evaluation
- iS-Matrix SOP, template, prompt, or reusable document production
- PCS project execution
- Manus / Kimi / Claude Code file creation, code editing, repository operations, or automation
- downstream agent prompt generation
- return feedback, patch logging, or case logging

### Step 3: Decide main owner

Select the main owner by the dominant value center:

- baseline decision, priority, project creation -> iS-Core
- strategic reasoning, evaluation, tradeoff, risk, model -> iS-SCO
- SOP, template, prompt, skill, instruction, reusable asset -> iS-Matrix
- concrete project delivery -> relevant PCS
- file creation, repo update, code execution -> Manus / Claude Code / Kimi Claw
- tool research or external agent evaluation -> iS-Hub
- immature idea validation -> iS-Lab

There must be exactly one main owner.

### Step 4: Decide collaborators

List all spaces or agents that must contribute.

Collaborators may include:

- iS-Core
- iS-SCO
- iS-Matrix
- iS-Hub
- iS-Lab
- iS-Synexa PCS
- iS-Nex2U PCS
- iS-Nexsply PCS
- iS-NexChef PCS
- Manus
- Kimi
- Claude Code
- Kimi Claw
- other execution agents

### Step 5: Produce current workspace output

The current workspace should complete the portion it is designed to complete.

Examples:

- iS-Matrix should produce the reusable document, SOP, prompt, template, or skill source draft.
- iS-SCO should produce reasoning, tradeoff, risk map, or decision memo.
- PCS should produce execution plan, project artifact, or delivery state update.
- iS-Core should produce baseline decision, owner assignment, or project definition.

### Step 6: Generate handoff package

Use `references/handoff_template.md`.

The package must include:

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

### Step 7: Generate return feedback requirement

Use `references/return_feedback_template.md`.

Every handoff must ask downstream agents to return:

- what was completed
- what failed
- what needs calibration
- what template or SOP should be patched
- whether iS-Core baseline decision is needed
- whether GitHub should be updated

### Step 8: Record case and patch opportunities

When the task reveals a reusable workflow, record it as a case.

Use:

- `references/cases.md`
- `references/patch_log_template.md`

Do not overbuild. Capture only practical changes that improve next execution.

## Workspace Routing Rules

### iS-Core

Route to iS-Core when the task requires:

- baseline governance
- final decision
- workspace responsibility correction
- priority setting
- new project creation
- project minimum definition
- conflict resolution between spaces

Do not route routine Level 2 collaboration tasks to iS-Core by default. Escalate only when governance judgment is actually required.

### iS-SCO

Route to iS-SCO when the task requires:

- strategy reasoning
- expected value analysis
- risk evaluation
- reverse validation
- decision framework
- tradeoff comparison
- new strategic hypothesis

### iS-Matrix

Route to iS-Matrix when the task requires:

- SOP
- procedure
- template
- digital employee instruction
- reusable prompt
- skill source file
- training manual
- standardized document asset

### PCS

Route to the relevant PCS when the task requires:

- concrete project execution
- project artifact delivery
- project state update
- implementation plan inside an existing project
- operating cadence
- execution coordination

### Manus / Kimi / Claude Code / Kimi Claw

Route to execution agents when the task requires:

- file creation
- repository operations
- code editing
- packaging
- validation
- batch processing
- automation script execution
- GitHub pull, commit, or push

### iS-Hub

Route to iS-Hub when the task requires:

- external AI tool research
- agent landscape comparison
- platform evaluation
- third-party workflow reference

### iS-Lab

Route to iS-Lab when the task is:

- immature
- not yet project-ready
- exploratory
- pre-validation
- a possible new business or concept seed

## Required Output

When invoked, produce at least one of the following:

1. Collaboration route
2. Cross-workspace handoff package
3. Return feedback package
4. Downstream agent prompt
5. Patch log entry
6. Case log entry
7. Workspace routing explanation

For production tasks, prefer this output order:

1. Current workspace deliverable
2. Handoff package
3. Return feedback requirement
4. Patch opportunities
5. Suggested GitHub path

For self-test tasks, include:

1. installation / loading visibility status
2. automatic trigger status, if confirmable
3. manual fallback status
4. runtime limitation note
5. next validation step for Manus or user

## References

Load these files only when needed:

- `references/collaboration_protocol.md` for full protocol rules
- `references/handoff_template.md` for handoff package format
- `references/return_feedback_template.md` for feedback format
- `references/execution_principles.md` for collaboration principles
- `references/agent_prompt_pack.md` for downstream agent prompts
- `references/patch_log_template.md` for patch logging
- `references/cases.md` for examples and case history

Use `scripts/validate_handoff.py` to check whether a markdown handoff package includes all required fields.

## Quality Bar

A good output must:

- identify one main owner
- preserve workspace boundaries
- avoid pretending one agent can do everything
- include enough context for downstream execution
- require return feedback
- leave a patch trail when the workflow is reusable
- remain lightweight and operational
- distinguish automatic skill invocation from manual protocol execution
- state runtime limitations honestly when installation or loading status is not visible

A bad output:

- only says "out of scope"
- assigns no owner
- mixes strategy, production, governance, and execution without boundaries
- gives downstream agents vague instructions
- omits return feedback
- creates heavy process for a simple task
- claims the skill is installed or automatically triggered without confirmation
- treats an installation visibility limitation as a workflow failure
