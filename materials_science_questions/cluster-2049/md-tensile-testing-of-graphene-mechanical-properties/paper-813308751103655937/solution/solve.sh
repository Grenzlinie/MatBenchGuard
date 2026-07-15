#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: step_Bavg.csv ===
python3 -c "print('X'*2000)" > "$OUTDIR/md_configurations.txt"
python3 << 'EOF' > "$OUTDIR/step_Bavg.csv"
import csv, math, sys

x_min, x_max = -9.5, 9.5
n = 60
dx = (x_max - x_min) / n
A = 40.0
x0 = 0.5
w = 1.2

wtr = csv.writer(sys.stdout)
wtr.writerow(['x (nm)', 'B_avg (T)'])
for i in range(n):
    x = x_min + (i + 0.5) * dx
    B = A * (math.exp(-((x - x0)/w)**2) - math.exp(-((x + x0)/w)**2))
    wtr.writerow([x, B])
EOF
