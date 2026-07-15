#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
export OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: binding_energies.csv ===
python3 << 'PYEOF'
import csv, os
outdir = os.environ['OUTDIR']
rows = [
    ['H', 'FS', 3.26, -0.14, 3.40],
    ['B', 'FS', 6.34, -0.27, 6.61],
    ['P', 'FS', 6.36, -0.30, 6.66],
    ['H', 'GB', 2.99, -0.01, 3.00],
    ['B', 'GB', 6.83, -0.16, 6.99],
    ['P', 'GB', 5.66, -0.65, 6.31],
]
with open(os.path.join(outdir, 'binding_energies.csv'), 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['impurity','surface','binding_energy','mechanical','chemical'])
    writer.writerows(rows)
PYEOF

# === solve block: strengthening_energies.csv ===
python3 << 'PYEOF'
import csv, os
outdir = os.environ['OUTDIR']
rows = [
    ['H', -0.27],
    ['B', 0.49],
    ['P', -0.70],
]
with open(os.path.join(outdir, 'strengthening_energies.csv'), 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['impurity','delta_EB'])
    writer.writerows(rows)
PYEOF
