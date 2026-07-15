#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: free_energy_curve.csv ===
python3 <<'PYEOF'
import csv
import math

steps = 200
initial = 1000.0
final = 100.0
tau = 50.0

with open('/app/outputs/free_energy_curve.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['time_step', 'free_energy'])
    for t in range(steps):
        free = final + (initial - final) * math.exp(-t / tau)
        writer.writerow([t, free])
PYEOF
