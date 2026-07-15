#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: dos_contributions.csv ===
python3 <<'PYEOF'
import csv
import os

outdir = os.environ.get('OUTDIR', '/app/outputs')
output_path = os.path.join(outdir, 'dos_contributions.csv')

columns = ['compound', 'M_s', 'M_p', 'M_d', 'M_f', 'A_s', 'A_p', 'A_d', 'Si_s', 'Si_p', 'Si_d', 'total']

rows = [
    {'compound': 'Ca(Al0.5Si0.5)2', 'M_s': 0.028, 'M_p': 0.096, 'M_d': 0.663, 'M_f': 0.0, 'A_s': 0.023, 'A_p': 0.101, 'A_d': 0.033, 'Si_s': 0.023, 'Si_p': 0.116, 'Si_d': 0.044, 'total': 1.127},
    {'compound': 'Sr(Al0.5Si0.5)2', 'M_s': 0.061, 'M_p': 0.138, 'M_d': 1.344, 'M_f': 0.0, 'A_s': 0.022, 'A_p': 0.345, 'A_d': 0.043, 'Si_s': 0.013, 'Si_p': 0.241, 'Si_d': 0.067, 'total': 2.273},
    {'compound': 'Ba(Al0.5Si0.5)2', 'M_s': 0.083, 'M_p': 0.199, 'M_d': 1.460, 'M_f': 1.034, 'A_s': 0.018, 'A_p': 0.404, 'A_d': 0.038, 'Si_s': 0.009, 'Si_p': 0.237, 'Si_d': 0.066, 'total': 2.611},
    {'compound': 'Ca(Ga0.5Si0.5)2', 'M_s': 0.017, 'M_p': 0.073, 'M_d': 0.594, 'M_f': 0.0, 'A_s': 0.022, 'A_p': 0.104, 'A_d': 0.015, 'Si_s': 0.019, 'Si_p': 0.105, 'Si_d': 0.042, 'total': 0.992},
    {'compound': 'Sr(Ga0.5Si0.5)2', 'M_s': 0.034, 'M_p': 0.036, 'M_d': 0.936, 'M_f': 2.0, 'A_s': 2.0, 'A_p': 2.0, 'A_d': 2.0, 'Si_s': 2.0, 'Si_p': 2.0, 'Si_d': 2.0, 'total': 1.431},
    {'compound': 'Ba(Ga0.5Si0.5)2', 'M_s': 0.044, 'M_p': 0.076, 'M_d': 1.079, 'M_f': 0.108, 'A_s': 0.017, 'A_p': 0.219, 'A_d': 0.016, 'Si_s': 0.013, 'Si_p': 0.164, 'Si_d': 0.051, 'total': 1.757}
]

with open(output_path, 'w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=columns)
    writer.writeheader()
    writer.writerows(rows)
PYEOF
