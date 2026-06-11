---
name: synexa-is-activation-alignment
description: activate synexa is global task room alignment for complex work that needs cross-domain collaboration, foundation skills, project/theme skills, execution agents, data source alignment, release checks, or governance routing. use when the user says 启动 sia, 按 sia 执行, 启动 sia 巡检, 启动 sia 发布检查, 全域协同, task room, 专项任务作战室, 基线巡检, 数据源治理, skill 生产, manus/kimi/claude code 执行包, or when a task spans strategy, production, audit, assets, github, skills, sop, or project execution.
---

# Synexa iS Activation & Alignment

Use this skill to activate Synexa iS global coordination logic. The skill converts complex work into a Task Room, calls relevant capability domains and skills in the current conversation, and prepares execution packages for external agents only when engineering execution is required.

## Core rule

Do not route users between fixed workspaces by default. Treat the current conversation as the Task Room when the task can be handled here. Call Core, SCO, Matrix, Hub, Lab, PCS, expert roles, professional roles, foundation skills, and project/theme skills as perspectives or capability domains inside the current Task Room.

Transfer to Manus, Kimi, Claude Code, Kimi Claw, Codex, Aily, Feishu, or other external agents only when the task requires file creation, code execution, repository work, packaging, large-file checking, external document review, Feishu field execution, or formal governance follow-up.

## Trigger modes

When the user says one of the following, use the matching mode:

- `启动 SIA`: activate a new Task Room and produce a Mission Brief.
- `按 SIA 执行`: run same-conversation all-domain collaboration and produce deliverables.
- `启动 SIA 巡检`: audit data sources, versions, skills, repositories, and baseline conflicts.
- `启动 SIA 发布检查`: check readiness before publishing a skill, SOP, protocol, pack, or repository update.

If the user does not explicitly say SIA but the task is complex, cross-domain, asset-producing, or execution-agent-dependent, apply SIA silently and briefly state that Task Room mode is active.

## Default output structure

Use G/B/D/E/F unless the user asks for another format:

- G｜Goal / General Judgment: goal, main judgment, SIA mode, whether Task Room is active.
- B｜Background / Boundary: context, constraints, scope, trigger condition, required roles.
- D｜Deduction / Design: reasoning, role design, capability-domain composition, risk and alternatives.
- E｜Execution Package: deliverables, source files, task packages, validation criteria, routing package.
- F｜Feedback / Follow-up: return feedback, tests, patch notes, versioning, whether Core is needed.

## Capability domains

Treat the six historical workspaces as capability domains, not mandatory separate conversations:

- Core: governance, baseline, project classification, priority, major commitments.
- SCO: strategy, N-Grid, RVM, EKB, risk exposure, decision support.
- Matrix: structured production, SOP, templates, prompt assets, skill source files.
- Hub: external intelligence, tools, agents, market examples, best practice scans.
- Lab: early experiments, concept pretests, minimum validation.
- PCS: project execution, milestones, delivery path, project asset ownership.

Core is not used for daily detail approval. Escalate to Core only for global baseline, project classification, major resource/priority conflicts, organizational rules, or external commitments.

## Skill and asset hierarchy

Classify capabilities into:

- Foundation Skills: general reusable skills such as EKB, N-Grid, Task Room Orchestrator, Baseline Auditor.
- Project / Theme Skills: scenario-specific skills such as Synexa Website, Nex2U, FineSense, Verdatar.
- Foundation Capability Pack: shared capability instructions and skill index, not an installable multi-skill package.
- Instructions: identity and task protocol for a domain/project/agent environment.
- Data Source Manifest: active, outdated, misplaced, and forbidden files for each environment.

A formal installable skill should contain one SKILL.md entrypoint and one install package. Do not merge multiple independent installable skills into one skill package.

## File naming and release rules

For installable skill zips, prefer unified readable names:

`[skill-name]_v[version]_skill.zip`

Use `skill.zip` only when a platform or packaging tool explicitly requires it. If both are produced, keep checksums or notes showing they contain the same package.

## References

Consult these files as needed:

- `references/sia_protocol.md` for SIA trigger modes and Task Room activation.
- `references/operating_architecture.md` for the three-layer operating model.
- `references/capability_asset_taxonomy.md` for skill and capability asset classification.
- `references/data_source_audit_protocol.md` for manifest, data source, and baseline audit rules.
- `references/execution_agent_packages.md` for Manus, Kimi, Claude Code, and Aily handoff formats.
- `references/release_checklist.md` for publishing checks.
- `references/test_cases.md` for IFT cases 001A, 001B, and 002.

## Quality bar

Always prefer current-task completion over unnecessary handoff. Produce usable artifacts or clear execution packages. Do not make the user carry context between agents. Record conflicts as patch opportunities. If installation, tool access, repository state, or data source state cannot be verified, say so and provide a manual fallback.
