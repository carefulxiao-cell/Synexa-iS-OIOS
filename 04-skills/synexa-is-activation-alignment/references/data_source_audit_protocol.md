# Synexa iS Data Source & Baseline Audit Protocol v0.1

## Goal

Prevent historical files, outdated instructions, misplaced SKILL.md files, old logic, or mixed versions from contaminating current GPT/agent environments.

## Data source types

- core_instruction
- global_context
- workspace_methodology
- capability_domain_reference
- project_reference
- skill_source
- capability_pack
- archive

## File status

- active
- draft
- deprecated
- superseded
- archive

## Recommended metadata

Every governance or instruction file should include:

- Status
- Scope
- Owner
- Applies To
- Do Not Upload To
- Supersedes
- Superseded By
- Version
- Last Updated

## Audit cadence

- Weekly light audit
- Monthly full audit
- Special audit after major mechanism updates
- Release audit before publishing skills, SOPs, protocols, or packs

## Audit output

- Active Files
- Outdated Files
- Misplaced Files
- Conflict Risks
- Required Updates
- GPT/Agent Upload Suggestions
- GPT/Agent Remove Suggestions
- GitHub Patch Suggestions
- Manus/Kimi execution package if needed

## Current known rule

A SKILL.md that belongs to a specific installable skill should not be uploaded as a generic data source for an unrelated GPT/project environment. Use summaries or capability packs instead.
