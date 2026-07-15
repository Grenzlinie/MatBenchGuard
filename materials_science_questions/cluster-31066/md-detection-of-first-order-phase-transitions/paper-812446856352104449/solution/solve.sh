#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: phase_boundary.csv ===
python3 -c "
import csv, math
C0 = -14 * (4/27)**2
C1 = 27 * math.log(3) / 16
alphas = [x/1000.0 for x in range(10, 251, 5)]  # 50 points from 0.01 to 0.25
with open('/app/outputs/phase_boundary.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['alpha_over_nmu', 'beta_nmu'])
    for a in alphas:
        beta = C1 / (a - C0)
        w.writerow([a, beta])
"

# === solve block: critical_point.csv ===
python3 -c "
import csv
with open('/app/outputs/critical_point.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['alpha_over_nmu', 'beta_nmu'])
    w.writerow([0.03, 1.185])
"
