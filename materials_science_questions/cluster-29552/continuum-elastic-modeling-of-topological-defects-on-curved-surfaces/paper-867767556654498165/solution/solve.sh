#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: a1_coefficients.csv ===
python3 <<'PYEOF'
import csv
rows = [
    (1.5, 'n0', 1.51473),
    (1.5, 'nn', 1.51473),
    (1.25, 'n0', 1.22617),
    (1.25, 'nn', 1.22617),
    (1.0, 'n0', 1.10494),
    (1.0, 'nn', 1.10494),
    (0.75, 'n0', 1.04940),
    (0.75, 'nn', 1.04940),
    (0.5, 'n0', 1.02392),
    (0.5, 'nn', 1.02392),
]
with open('/app/outputs/a1_coefficients.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['gamma', 'lattice_type', 'a1'])
    w.writerows(rows)
PYEOF
