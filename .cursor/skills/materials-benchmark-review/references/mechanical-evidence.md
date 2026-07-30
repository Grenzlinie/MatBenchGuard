# Mechanical evidence layer

Mechanical tools collect reproducible facts for the Agent. They never emit
findings, criterion statuses, scores, Hard Gates, repair decisions, or verdicts.

## Static collection

Run:

```bash
python .cursor/skills/materials-benchmark-review/scripts/collect_package_evidence.py \
  <package> --output <evidence-dir>/mechanical_evidence.json
```

Add `--probe-urls` whenever `instruction.md` or `resources.json` contains an
explicit HTTP(S) URL. This performs only a lightweight status check; it does not
call Playground to pull a resource, download its body, or verify deployment.

The collector records:

- package inventory, roles, sizes, hashes, and required-core structure status,
  including the mandatory `tests/test.sh`;
- lexical instruction output/resource candidates with exact lines;
- repeated final/last analysis-window candidates across instruction, steps, and
  grading files;
- lexical Cartesian/crystallographic directions, solver-choice language,
  derived-parameter language, and fixed-target language. These only index
  possible simulation dependencies; zero hits never prove parameter closure;
- the raw-compatible grading output contract, steps, weights, threshold, and
  unsupported-shape limitations;
- checker AST functions, literal file access calls, scorer registries, constant
  returns, reward writes, risky-call candidates, and per-output scoring-chain
  candidates;
- lexical Gold-provenance risk candidates in `tests/` for random,
  interpolated/fitted, smoke, synthetic, dummy, or placeholder reference
  generation;
- instruction- and `resources.json`-declared data/model/URL candidates, plus
  optional lightweight URL status observations.

Lexical mismatch, missing expected keys, or unsupported shapes are limitations
or candidates—not schema findings. The Agent must adjudicate output roles,
aliases, scientific coverage, resource indispensability, and equivalent forms.
Missing required core files are structural facts; scientific-risk lexical hits
remain candidates and must not be promoted automatically. In particular, a
`smoke`, `random`, `fit`, or `interpolate` hit in `tests/` may belong to a
negative fixture, robustness test, declared analysis, or reduced runner rather
than Gold generation; retain the exact line and adjudicate its data flow into
the acceptance rule. The collector must skip `solution/**` entirely: no content
read, hash, lexical candidate, or evidence record.

For every simulation task, the Agent must still read the complete paper and
package and create `simulation_parameter_matrix.json`. Mechanical evidence
cannot decide whether a parameter is necessary, source-required, uniquely
derived, representation-equivalent, solver-selectable, or missing.

## Dynamic observations

Run built-in negative cases:

```bash
python .cursor/skills/materials-benchmark-review/scripts/run_checker_probes.py \
  <package> --output <evidence-dir>/checker_observations.json
```

Supply evidence-backed cases when available:

```bash
... --case valid_positive=<outputs-dir> \
    --case quality_gradient=<outputs-dir> \
    --case semantic_equivalence=<outputs-dir> \
    --case component_isolation=<outputs-dir> \
    --case minimal_exploit:wrong-time-axis=<outputs-dir> \
    --case duplicate_records:conflicting-key=<outputs-dir>
```

Agent-supplied cases are allowed for all eleven probe classes. Use
`PROBE_CLASS:VARIANT` for task-specific attacks; builtin generic observations
are retained rather than overwritten. Multiple variants may be supplied for one
class.

The runner copies `tests/**` to a disposable workspace, rewrites Harbor absolute
paths only in that copy, creates generic missing/empty/malformed/random/
duplicate/non-finite/minimal cases, executes `tests/test.sh`, and records exit
code, finite reward, breakdown, errors, stdout/stderr, rewritten files, and
limitations.

Checker execution is mandatory by default for this controlled corpus. The
runner uses disposable copies, path redirection, and per-case timeouts, but this
is not a security sandbox. Run the static collector/security review first and,
when available, prefer an isolated container/VM with no secrets, restricted
filesystem/network, and resource limits. `--no-execute` exists only for an
explicit diagnostic dry run; its `NOT_ASSESSED` output cannot satisfy Review.

The runner does not know expected scientific rewards. `OBSERVED` means the
result was mechanically usable, not that checker behavior passed audit.
`UNUSABLE` and `NOT_ASSESSED` require Agent follow-up. Path rewriting is only a
local approximation: host-path absence, rewrite failure, or unsupported
container layout is an automation limitation unless the problem is reproduced
under the package's declared container paths and mounts or those declarations
are independently proven invalid.

Quality-gradient, equivalence, component-isolation, and scientifically valid
positive outputs cannot be fabricated generically. The Agent constructs or
selects them from public task evidence without opening `solution/`.

Pass every builtin and task-specific observation file to the decision validator.
The validator checks that applicable decision claims cite an actually executed
`case_id`; it does not decide whether the observed reward is scientifically
acceptable.
