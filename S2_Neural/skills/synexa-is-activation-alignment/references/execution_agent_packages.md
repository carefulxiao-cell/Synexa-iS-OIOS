# Execution Agent Packages

## General rule

External agents should not receive vague strategy discussions. They should receive clear execution packages with goals, inputs, paths, outputs, validation, pause conditions, and return feedback templates.

## Manus package

Use Manus for:
- file landing
- multi-file directory updates
- GitHub commits
- registry updates
- packaging skill zips
- running validation scripts

Required fields:
- Mission name
- Source package/path
- Target GitHub path
- Files to create/update
- Validation steps
- Version naming
- Pause conditions
- Return feedback package

## Kimi package

Use Kimi for:
- long-text comparison
- consistency checks
- document review
- cross-file logic review

Required fields:
- Documents to compare
- Questions to answer
- Conflict criteria
- Output format

## Claude Code / Codex package

Use for:
- code refactor
- scripts
- packaging automation
- tests

Required fields:
- repository path
- scripts/tests to run
- expected output
- failure handling

## Aily package

Use Aily for Feishu field execution:
- group chat summaries
- meeting minutes
- task extraction
- Feishu doc/table整理
- onsite status update

Aily should not decide global architecture, baseline, or official releases.
