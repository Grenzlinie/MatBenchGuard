# Fast E1 batch

The batch runner applies the same Review CLI contract to a deterministic,
resumable sample without mutating source packages.

Use the frozen original identity manifest:

```bash
python .cursor/skills/materials-benchmark-review/scripts/run_fast_e1_batch.py \
  materials_science_questions \
  --output-dir review_artifacts/materials_fast_e1_100/evidence_review_baseline_v1_20260716 \
  --identity-manifest review_artifacts/materials_fast_e1_100/candidate_manifest.json \
  --workers 24 \
  --max-packages 10 \
  --target 100
```

After the 10-package calibration is accepted, increase `--max-packages` to 100.
`results.jsonl` is append-only; terminal identities are not reviewed again.
Use a new output directory whenever the evidence contract changes. A v8
directory may supply identity/order/source-binding baseline information only;
it is never resumed as v9 scientific certification.

## Identity manifest

`candidate_manifest.json` is identity-only. It contains schema, manifest role,
authoritative flag, sample count, preserved ordering, and `package_ids`.
It contains no verdict, evidence, candidate tier, scientific claim, or repair
state. Legacy review fields are not imported as evidence.

When `--identity-manifest` is supplied, only those package IDs are reviewed and
their listed order is preserved. Missing, duplicate, or malformed identities
fail the invocation.

## Baseline gate

`index.json.repair_gate` is
`BLOCKED_REVIEW_BASELINE_INCOMPLETE` until every frozen identity has a terminal
Review record. Only then is it `READY_FOR_REPAIR`. Review records and checker
evidence remain in `index.json`/`results.jsonl`, never in the identity manifest.

The batch copies instruction/tests and, when present, an isolated solution
Oracle role. It does not copy or score metadata, resources, steps, task config,
or environment files, and it never modifies the source corpus.

For every completed CLI run, the batch persists `audit_report.json`,
`audit_manifest.json`, and `checker_tests.json` under `cli_reports/`. The ledger
stores a canonical `cli_evidence` snapshot bound to all three file hashes,
authoritative materials qualification, paper-trigger adjudication, dynamic
probe provenance, the Oracle-safe solution status, and deterministic hashes of
the Review scripts that produced scoring/probing/finalization evidence. Hash
keys are skill-relative and contain no machine-specific paths. Resume rejects
any changed snapshot, persisted file, or Review implementation.

Every authoritative scoring snapshot is bound to `execution_level=E1` and the
CLI's four Hard-Gate results. Any failed gate, including direct-input
availability, forces `E1_EXCLUDED`; it can never remain a usable candidate.

Fresh v9 certification accepts exactly six probe classes: positive, negative,
discrimination, equivalence, component isolation, and process evidence. It
also verifies complete contract maps, component provenance, the process class's
fixed `NOT_APPLICABLE` policy, Oracle lifecycle, and current Review
implementation hashes. Four-class and stale-tool reports remain historical
evidence and cannot become authoritative without a fresh audit in a new output
directory.

Absence of an assessment that leaves a critical evidence gap is an honest
terminal `NOT_ASSESSABLE` result, not permission to infer positive evidence
from no findings or from the Oracle. Absence of an independent public valid
fixture is instead a scored, non-critical robustness limitation:
discrimination/equivalence remain explicitly unavailable with non-Oracle
provenance, completed probe evidence is retained, and the total/verdict remain
computable.
