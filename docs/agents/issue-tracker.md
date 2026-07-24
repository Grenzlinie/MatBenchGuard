# Issue tracker: GitHub

Issues and PRDs for this repo live in `Grenzlinie/MatBenchGuard` GitHub Issues. Use the `gh` CLI and pass `--repo Grenzlinie/MatBenchGuard` when repository inference is unavailable.

## Conventions

- Create: `gh issue create --repo Grenzlinie/MatBenchGuard --title "..." --body "..."`
- Read: `gh issue view <number> --repo Grenzlinie/MatBenchGuard --comments`
- List: `gh issue list --repo Grenzlinie/MatBenchGuard`
- Comment: `gh issue comment <number> --repo Grenzlinie/MatBenchGuard --body "..."`
- Label: `gh issue edit <number> --repo Grenzlinie/MatBenchGuard --add-label "..."`
- Close: `gh issue close <number> --repo Grenzlinie/MatBenchGuard --comment "..."`

Use heredocs for multiline bodies.

## Pull requests as a triage surface

**PRs as a request surface: no.**

## When a skill says "publish to the issue tracker"

Create a GitHub issue in `Grenzlinie/MatBenchGuard`.

## When a skill says "fetch the relevant ticket"

Read the issue and all comments with `gh issue view`.

## Blocking relationships

Prefer GitHub native issue dependencies. If unavailable, record `Blocked by: #<n>` in the issue body. A ticket is ready when all blockers are closed.
