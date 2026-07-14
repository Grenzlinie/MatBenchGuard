# Issue tracker: GitHub

Issues and PRDs for this repo live in `Grenzlinie/qa-review` GitHub Issues. Use the `gh` CLI and pass `--repo Grenzlinie/qa-review` when repository inference is unavailable.

## Conventions

- Create: `gh issue create --repo Grenzlinie/qa-review --title "..." --body "..."`
- Read: `gh issue view <number> --repo Grenzlinie/qa-review --comments`
- List: `gh issue list --repo Grenzlinie/qa-review`
- Comment: `gh issue comment <number> --repo Grenzlinie/qa-review --body "..."`
- Label: `gh issue edit <number> --repo Grenzlinie/qa-review --add-label "..."`
- Close: `gh issue close <number> --repo Grenzlinie/qa-review --comment "..."`

Use heredocs for multiline bodies.

## Pull requests as a triage surface

**PRs as a request surface: no.**

## When a skill says "publish to the issue tracker"

Create a GitHub issue in `Grenzlinie/qa-review`.

## When a skill says "fetch the relevant ticket"

Read the issue and all comments with `gh issue view`.

## Blocking relationships

Prefer GitHub native issue dependencies. If unavailable, record `Blocked by: #<n>` in the issue body. A ticket is ready when all blockers are closed.
