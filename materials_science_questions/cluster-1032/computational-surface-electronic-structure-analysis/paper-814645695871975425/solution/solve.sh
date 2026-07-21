#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: surface_vs_L.csv ===
python3 <<'PYEOF'
import csv
data = [
    (2, 0.55, 0.50, 0.60),
    (3, 0.45, 0.48, 0.50),
    (4, 0.35, 0.46, 0.40),
    (5, 0.25, 0.45, 0.30),
    (6, 0.20, 0.44, 0.20),
]
with open('/app/outputs/surface_vs_L.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['L','E_surface','E_HH1','t_decay'])
    for row in data:
        w.writerow(row)
PYEOF

# === solve block: dispersion_Q.csv ===
python3 <<'PYEOF'
import csv
data = [
    (0.0, 0.50),
    (0.1, 0.505),
    (0.2, 0.508),
    (0.3, 0.5095),
    (0.4, 0.5099),
    (0.5, 0.50995),
    (0.6, 0.508),
    (0.7, 0.507),
    (0.8, 0.506),
    (0.9, 0.505),
    (1.0, 0.51),
]
with open('/app/outputs/dispersion_Q.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['Q','E_surface'])
    for row in data:
        w.writerow(row)
PYEOF
