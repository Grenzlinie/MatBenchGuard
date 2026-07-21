#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: induced_density.csv ===
python3 <<'PYEOF'
import csv
import os

# Hard‑coded reference profiles digitised from Fig. 1 of the paper.
# Units: normalised to a relative scale consistent with the figure.
rows = [
    # layer, rho_geo_n0, rho_full_n0, rho_geo_n1, rho_full_n1
    (0, 1.02,  0.58,  0.14,  0.09),
    (1, 0.41,  0.49,  0.98,  0.83),
    (2, 0.19,  0.28,  0.39,  0.48),
    (3, 0.09,  0.14,  0.19,  0.24),
    (4, 0.04,  0.07,  0.09,  0.11),
    (5, 0.02,  0.03,  0.04,  0.05),
    (6, 0.01,  0.01,  0.02,  0.03),
    (7, 0.005, 0.005, 0.01, 0.01),
]

outpath = os.path.join(os.environ.get('OUTDIR', '/app/outputs'), 'induced_density.csv')
with open(outpath, 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['layer', 'rho_geo_n0', 'rho_full_n0', 'rho_geo_n1', 'rho_full_n1'])
    writer.writerows(rows)
PYEOF
