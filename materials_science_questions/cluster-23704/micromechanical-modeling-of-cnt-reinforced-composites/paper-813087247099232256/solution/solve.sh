#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
set -euo pipefail
mkdir -p /app/outputs

# === solve block: contact_force_validation.csv ===
python3 << 'EOF'
import csv, math, os
outdir = os.environ.get('OUTDIR', '/app/outputs')
outfile = os.path.join(outdir, 'contact_force_validation.csv')
T = 0.00025
Fmax = 2800.0
dt = 1e-6
times = []
forces = []
t = 0.0
while t <= T:
    f = Fmax * math.sin(math.pi * t / T)
    times.append(t)
    forces.append(f)
    t += dt
with open(outfile, 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['time','contact_force'])
    for t, force in zip(times, forces):
        w.writerow([t, force])
EOF

# === solve block: contact_force_fg_cntrc.csv ===
python3 /solution/generate_all.py

# === solve block: summary_metrics.json ===
python3 /solution/generate_all.py
