# Domain Docs

How engineering skills consume this repository's domain documentation.

## Before exploring

Read:

- `CONTEXT.md` at the repository root;
- relevant ADRs under `docs/adr/`.

If either location does not exist, proceed silently. `/domain-modeling` creates files lazily when terminology or a hard-to-reverse decision is resolved.

## File structure

This is a single-context repository:

```text
/
├── CONTEXT.md
├── docs/
│   └── adr/
└── references/
```

## Use the glossary vocabulary

Use terms exactly as defined in `CONTEXT.md` in issues, specs, tests, reports, and skill instructions. If a required concept is absent or overloaded, resolve it through `/domain-modeling` before adding synonyms.

## Flag ADR conflicts

Surface any conflict with an existing ADR explicitly rather than silently overriding it.
