# Synexa iS Capability Asset Taxonomy v0.1

## 1. Foundation Skills

General reusable skills used across projects and domains.

Examples:
- ekb-decision
- n-grid-strategy
- synexa-is-activation-alignment
- synexa-baseline-auditor

Rules:
- One foundation skill has one SKILL.md and one install package.
- It can be invoked by many project/theme skills.
- It usually does not depend on a project/theme skill.
- Archive and release filenames should use `[skill-name]_v[version]_skill.zip`.

## 2. Project / Theme Skills

Scenario-specific skills for a project, brand, business line, or content system.

Examples:
- synexa-website-visual-system
- nex2u-hospital-nutrition-system
- finesense-content-system
- verdatar-plant-archive

Rules:
- Can call or reference one or more foundation skills.
- Should not be required by foundation skills.
- Outputs belong to corresponding PCS or project asset libraries.
- Mature project skills may later be generalized into foundation skills or global SOP.

## 3. Foundation Capability Pack

A shared instruction and index pack for GPT/agent environments. It is not an installable multi-skill package.

Recommended filename:
`Synexa_Foundation_Capability_Pack_v0.1.zip`

Recommended contents:
- README.md
- foundation_skill_index.md
- ekb-decision_summary.md
- n-grid-strategy_summary.md
- task_room_orchestrator_summary.md
- baseline_auditor_summary.md
- invocation_rules.md

## 4. Instructions

Identity and task protocol for a domain, project, or agent environment.

Examples:
- iS-SCO_StrategyCenter_Instructions_v2.0.md
- iS-Matrix_StructuredProduction_Instructions_v2.0.md
- iS-Core_Governance_Instructions_v2.0.md

## 5. Data Source Manifest

The active data source list and removal rules for each environment.

Examples:
- iS-SCO_Data_Source_Manifest_v0.1.md

## Key relationship

Project/theme skills can flexibly call foundation skills. Foundation skills normally do not call project/theme skills.
