#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: lattice_energies.csv ===
python3 - << 'PYEOF'
import csv

outdir = '/app/outputs'
with open(outdir + '/lattice_energies.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['crystal', 'lattice_energy_kcal'])
    writer.writerows([
        ['α-D-glucose', -36.4],
        ['β-D-glucose', -33.1],
        ['α-L-xylose', -24.6],
        ['β-L-arabinose', -28.2],
        ['methyl-α-D-glucopyranoside', -35.0],
        ['methyl-α-D-mannopyranoside', -27.8],
    ])
PYEOF
