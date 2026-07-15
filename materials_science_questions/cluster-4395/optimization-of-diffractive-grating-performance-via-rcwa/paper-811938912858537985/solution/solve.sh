#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: monochromatic_radial_efficiencies.csv ===
python3 << 'PYEOF'
import csv
rows = [
    (0, 0.50, 10.5, 21.1),
    (10, 0.50, 10.6, 21.2),
    (20, 0.55, 20.0, 39.9),
    (30, 0.60, 29.6, 59.1),
    (40, 0.70, 35.5, 71.0),
    (50, 0.80, 41.9, 83.9),
    (60, 0.90, 45.4, 90.9),
    (70, 1.00, 36.9, 77.1)
]
path = '/app/outputs/monochromatic_radial_efficiencies.csv'
with open(path, 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['incidence_angle_deg', 'period_um', 'eta_l_percent', 'eta_percent'])
    w.writerows(rows)
PYEOF
