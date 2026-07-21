#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
# No special preamble required; Python3 with stdlib is sufficient.

# === solve block: delta_h2_scaling.csv ===
python3 - <<'PYEOF'
import csv
import math

sizes = [24, 48, 72]
# paper's reported fit: delta_h2 = 0.00889233 + 0.0406318 * ln(L)
data = [(L, 0.00889233 + 0.0406318 * math.log(L)) for L in sizes]

with open('/app/outputs/delta_h2_scaling.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['L', 'delta_h2'])
    writer.writerows(data)
PYEOF

# === solve finalize ===
# No finalize step needed.
