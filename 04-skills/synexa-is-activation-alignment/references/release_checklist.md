# SIA Release Checklist

Use for `启动 SIA 发布检查`.

## Skill release

- One SKILL.md entrypoint only.
- Technical name is stable and lowercase.
- Display name is human-friendly.
- Description includes trigger conditions.
- References are one level from SKILL.md unless needed otherwise.
- Package filename: `[skill-name]_v[version]_skill.zip` unless platform requires `skill.zip`.
- Version is recorded in CHANGELOG or VERSION.
- Test cases are defined.
- Runtime fallback is documented.
- Core escalation need is checked.

## Protocol / governance release

- Status and scope are clear.
- Supersedes / superseded-by fields are set when applicable.
- Active vs archive state is clear.
- Data source manifest updates are included.
- GitHub target path is specified.
- GPT/agent upload/remove suggestions are included.

## Capability pack release

- It is not mislabeled as an installable skill.
- README and index exist.
- Each included capability has scope and invocation rule.
- It does not include unrelated full skill source unless intentionally documented.
