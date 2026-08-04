# Single-file Harbor Oracle full-score fixture

Use `solution/solve.sh` only to answer this packaging question:

> If a submission contains the frozen standard correct outputs, does the packaged verifier award reward `1.0` and full credit for every component?

It is not a reference scientific execution. Oracle success does not prove Gold correctness, task solvability, or that DFT, MD, training, fitting, or search was run.

## Required contract

- Keep exactly one entry under `solution/`: executable `solve.sh`.
- Start with `#!/usr/bin/env bash` and `set -euo pipefail`.
- Include the literal marker `CHECKER_FULL_SCORE_FIXTURE`.
- Use one or more inline `python3 ... <<'PYEOF'` heredocs; do not add helper files.
- Write every declared output under `/app/outputs`, with exact filenames, schemas, units, primary keys, cardinalities, condition groups, and mutually consistent enhanced results.
- Use standard-library Python when practical. Do not install packages, access the network, or run the primary scientific computation.
- Do not read `/tests`, import checker code, or extract checker constants. Implement the fixture and checker independently from the already frozen Gold/output contract.
- Fail nonzero if any declared output is missing, empty, malformed, duplicated, or non-finite.

## Template

```bash
#!/usr/bin/env bash
set -euo pipefail

readonly OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# CHECKER_FULL_SCORE_FIXTURE
python3 - "$OUTDIR" <<'PYEOF'
from __future__ import annotations

import csv
import json
import math
import sys
from pathlib import Path

outdir = Path(sys.argv[1])
outdir.mkdir(parents=True, exist_ok=True)

summary = {
    "condition_id": "<frozen-condition-id>",
    "target_value": 0.0,  # replace from the frozen Gold contract
}
(outdir / "summary.json").write_text(
    json.dumps(summary, indent=2, ensure_ascii=False) + "\n",
    encoding="utf-8",
)

rows = [
    {"x": 0.0, "y": 0.0},  # replace with the standard correct result
]
with (outdir / "curve.csv").open("w", encoding="utf-8", newline="") as handle:
    writer = csv.DictWriter(handle, fieldnames=["x", "y"])
    writer.writeheader()
    writer.writerows(rows)

required = [outdir / "summary.json", outdir / "curve.csv"]
for path in required:
    if not path.is_file() or path.stat().st_size == 0:
        raise RuntimeError(f"missing or empty Oracle output: {path}")
for key, value in summary.items():
    if isinstance(value, float) and not math.isfinite(value):
        raise RuntimeError(f"non-finite value in summary.json: {key}")
PYEOF
```

Replace the example filenames and values. Do not retain placeholder outputs that are absent from `instruction.md`.

## Validation

Run:

```bash
harbor run -p <candidate> -a oracle
```

Accept only when the run evidence shows:

- total reward exactly `1.0`;
- every scoring component at its maximum;
- `scientific_execution_performed = false` in the external authoring record.

Then run the required negative and tolerance probes separately. Oracle full reward proves positive-path compatibility; negative probes prove the verifier does not award full credit unconditionally.
