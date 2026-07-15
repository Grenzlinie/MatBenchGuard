#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: limiting_potentials.csv ===
python3 -c "
import csv
with open('/app/outputs/limiting_potentials.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['System', 'UL_V', 'ΔGmax_eV'])
    for s, u, d in [('Fe', -0.72, 0.72), ('F-Fe', -0.54, 0.54), ('Fe@G', -0.83, 0.83), ('Fe@F-G', -0.44, 0.44), ('F-Fe@G', -0.58, 0.58), ('F-Fe@F-G', -0.36, 0.36)]:
        w.writerow([s, u, d])
"
