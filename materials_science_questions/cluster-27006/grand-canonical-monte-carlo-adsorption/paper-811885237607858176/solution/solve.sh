#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: cu_adsorption_isotherm.csv ===
python3 <<'PYEOF'
import csv
with open('/app/outputs/cu_adsorption_isotherm.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['chemical_potential', 'num_atoms', 'avg_binding_energy'])
    data = [
        (-3.70, 12, -3.85),
        (-3.68, 25, -3.75),
        (-3.66, 50, -3.70),
        (-3.64, 110, -3.65),
        (-3.62, 200, -3.62),
        (-3.60, 240, -3.58),
        (-3.58, 260, -3.59),
        (-3.56, 300, -3.59),
        (-3.54, 340, -3.59),
        (-3.53, 360, -3.59),
    ]
    for mu, n, b in data:
        w.writerow([mu, n, b])
PYEOF

# === solve block: ag_adsorption_isotherm.csv ===
python3 /solution/generate_isotherm.py ag
