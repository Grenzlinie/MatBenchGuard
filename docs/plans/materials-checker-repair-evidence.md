# Materials checker-repair evidence

This note is the documentation and fixture evidence for the D1–D6 repair
slice. It narrows `AUTO_FIX` to deterministic restoration of an existing
contract or scoring wire. It does not change the v11 plan or any Harbor
package.

## Narrow `AUTO_FIX` boundary

For D1–D6, `AUTO_FIX` may restore only a uniquely determined relationship
already present in the frozen contract:

- synchronize an existing output path, filename, or declaration token across
  `instruction.md`, `tests/grading_spec.json`, and the grading steps;
- normalize an equivalent structural spelling or prose punctuation without
  changing a literal filename, field, unit, or format;
- restore an existing scorer's registration, binding, return path, or final
  reward connection when static evidence proves it is unique;
- restore a standard Harbor entrypoint around one unique existing producer; or
- normalize already-declared finite positive weights only when the operation
  preserves their proven ratios and does not choose a new scoring importance.

Every such operation needs source-bound proof, `core_science_change=false`, a
causal fail-before/pass-after regression, and the single equal-depth dual-lane
re-audit. A passing regression alone is not scientific evidence.

`AUTO_FIX` must not introduce or choose any of the following:

- Gold values, targets, tolerances, thresholds, formulas, or scorer
  algorithms;
- new outputs, fields, units, ordering rules, or scientific parameters;
- a new interpretation of the material system, endpoint, method, or
  reproduction semantics;
- a superficial read, weight, or breakdown entry that makes an ignored core
  output appear scored; or
- a fabricated solution producer, private checker protocol, or fixture.

An operation that needs semantic selection is not `AUTO_FIX`: it is
`ASSISTED_FIX` only when the evidence precision is sufficient, otherwise it is
`ABANDON`/`BLOCKED_EVIDENCE`. Oracle/solution content and metadata cannot
authorize a public contract, schema, scoring, or science change.

## D1–D6 boundary by check

| Check | `AUTO_FIX` may restore | It must not decide |
| --- | --- | --- |
| D1 | A stale output token whose unique target already exists in the contract | A new output or a different output identity |
| D2 | An existing declaration omitted or structurally drifted between instruction sections | New fields, units, formats, or scientific requirements |
| D3 | A uniquely proven existing scorer registration/return wire | A formula, scorer algorithm, constant-score policy, or direction |
| D4 | Ratio-preserving normalization of already-declared finite positive weights | New weights, component importance, thresholds, or tolerances |
| D5 | A standard entrypoint wrapper for one existing producer | A producer, Gold generator, or scientific implementation |
| D6 | A uniquely proven existing core scorer binding or final-reward wire | A superficial read, new scorer, or redefinition of the core task |

## Compact casebook

These cases are the real examples and ticket seams described by the plan. The
casebook records the decision boundary, not solution output.

### D1/D2 — issue #30

- A prose period after an output path is normalized as punctuation, while a
  quoted literal filename ending in a period remains distinct.
- An extra grading output is reported as `OUTPUT_NOT_CONTRACTED`.
- Cross-section field or unit drift is semantic, not structural; it cannot be
  silently repaired as `AUTO_FIX`.
- The safe automatic action is source-bound output-token synchronization only.

### D3/D4 — issue #28

- Non-finite, negative, zero, or ineffective weights remain findings rather
  than invitations to invent scoring intent.
- A proven incomplete return path or uniquely missing scorer registration can
  be restored when the existing source makes the target unambiguous.
- Literal divide-by-zero, always-pass/always-zero behavior, and any formula
  change require semantic evidence; they are not automatic formula repairs.

### D5 — issue #29

- A missing `solution/solve.sh` may receive a standard wrapper only when one
  existing implementation is uniquely identifiable.
- Metadata roles are not quality evidence.
- When no unique producer exists, Repair must not fabricate a scientific
  producer or claim completeness.

### D6 — issue #31

- A filename or existence check is not proof that the core content was read.
- A uniquely identified scorer registry connection is a valid wiring repair.
- An overwritten output alias, an unbound scorer, or a breakdown that is not
  included in final reward cannot be fixed by adding a superficial read or
  invented score path.

### Evidence and publication — issues #21 and #32

- A threshold change, Gold change, private checker/solution protocol, or
  arbitrary fixture is blocked even when a plan supplies plausible text.
- A deterministic plan must bind the complete source queue and current
  contract digest; stale or omitted bindings fail closed.
- A residual D1–D6 blocker prevents publication. The candidate needs one
  equal-depth dual-lane re-audit and a clean deterministic contract.

## Assisted semantic repairs

`ASSISTED_FIX` is the Agent-quality path for a scientific or scoring correction;
it is not a wider `AUTO_FIX` lane. Every operation links evidence carrying:

```json
{
  "source_kind": "PACKAGE_PAPER",
  "source": "paper/paper.md",
  "exact_quote": "the exact source text",
  "source_hash": "sha256:<retrieved bytes>",
  "applicability": "why the source governs this package",
  "derivation": "how the exact typed replacement follows",
  "core_science_change": false
}
```

`source_kind` may instead be `PACKAGE_DIRECT_SOURCE` for an
source-audit-hashed direct package source, or
`AUTHORITATIVE_PRIMARY_WEB`. The web form must also include an identical
`url`/`source`, `retrieved_at`, non-empty `retrieval_metadata`, and an explicit
approval object (`approved=true`, `primary=true`, an authoritative source
class, and a reference). Repair does not fetch web pages. Missing fields,
stale hashes, unsupported source roles, type mismatches, or conflicting
claims produce `BLOCKED_EVIDENCE`; the operation is not guessed or applied.

Agent-quality findings have no D1–D6 owner and cannot be converted to
`AUTO_FIX`. The source Review total must be at least 60 to enter Repair. A
re-audit total below 60 abandons the candidate; 60–79 may remain
`PARTIALLY_REPAIRED`. Publication still requires the authoritative total to be
at least 80, deterministic CLEAN, no Hard Gate, no unresolved HIGH/FATAL
finding, preserved identity, allowed scope, and closure of every target.

## Oracle-safe evidence rule

The positive Oracle mock is used only to exercise the positive checker path.
This note intentionally contains no Oracle values, raw rewards, breakdowns,
stdout/stderr, generated files, or solution contents. Discrimination and
equivalence evidence must use an independently justified, non-Oracle fixture
with a source-bound manifest.
