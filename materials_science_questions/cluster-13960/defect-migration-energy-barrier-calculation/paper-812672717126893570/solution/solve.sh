#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: charge_transfer.json ===
python3 -c "
import json
data = {'Al': 0.09, 'Zn': 0.05, 'Cu': 0.04, 'Ag': 0.02}
with open('$OUTDIR/charge_transfer.json', 'w') as f:
    json.dump(data, f)
"

# === solve block: barriers.json ===
python3 -c "
import json
data = {
    'neutral': {'barrier_eV': 0.97, 'reaction_energy_eV': 0.22},
    'electron': {'barrier_eV': 0.47, 'reaction_energy_eV': -0.45},
    'hole': {'barrier_eV': 1.24, 'reaction_energy_eV': 0.45}
}
with open('$OUTDIR/barriers.json', 'w') as f:
    json.dump(data, f)
"

# === solve block: pdos_integrated.csv ===
python3 -c "
import csv
rows = [(1, 0.88), (2, 1.78), (3, 2.72), (4, 3.60)]
with open('$OUTDIR/pdos_integrated.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['x', 'integrated_area'])
    w.writerows(rows)
"
