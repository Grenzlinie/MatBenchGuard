# Mechanical evidence layer

Mechanical tools collect reproducible facts for the Agent. They never emit
findings, criterion statuses, scores, Hard Gates, repair decisions, or verdicts.

## Static collection

Run:

```bash
python .cursor/skills/materials-benchmark-review/scripts/collect_package_evidence.py \
  <package> --output <evidence-dir>/mechanical_evidence.json
```

Add `--probe-urls` only when external access checks are appropriate.

The collector records:

- package inventory, roles, sizes, and hashes;
- lexical instruction output/resource candidates with exact lines;
- the raw-compatible grading output contract, steps, weights, threshold, and
  unsupported-shape limitations;
- checker AST functions, literal file access calls, scorer registries, constant
  returns, reward writes, risky-call candidates, and per-output scoring-chain
  candidates;
- instruction-declared data/model/URL candidates and optional URL observations.

Lexical mismatch, missing expected keys, or unsupported shapes are limitations
or candidates—not schema findings. The Agent must adjudicate output roles,
aliases, scientific coverage, resource indispensability, and equivalent forms.

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
    --case component_isolation=<outputs-dir>
```

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
selects them from public task evidence without reading solution values.
