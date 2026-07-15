#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs
# No additional setup; python3 is available.

# === solve block: ic_traces.csv ===
python3 << 'PYEOF'
import csv, math, random

def ic_curve(t, start=200, end=400, baseline=20, peak=120):
    midpoint = (start + end) / 2
    scale = 10.0 / (end - start)
    return baseline + (peak - baseline) / (1 + math.exp(-scale * (t - midpoint)))

time_steps = list(range(0, 600, 2))
N_neighbors = 6
random.seed(42)
target_IC = []
neighbors_IC = [[] for _ in range(N_neighbors)]
for t in time_steps:
    val = ic_curve(t, 200, 400)
    noise = random.gauss(0, 5)
    target = max(0, val + noise)
    target_IC.append(round(target, 2))
    for n in range(N_neighbors):
        n_noise = random.gauss(0, 5) * 0.8
        n_val = max(0, val + n_noise)
        neighbors_IC[n].append(round(n_val, 2))

with open('/app/outputs/ic_traces.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    header = ['time', 'target_IC'] + [f'neighbor_{i+1}_IC' for i in range(N_neighbors)]
    writer.writerow(header)
    for i, t in enumerate(time_steps):
        row = [t, target_IC[i]] + [neighbors_IC[j][i] for j in range(N_neighbors)]
        writer.writerow(row)
PYEOF

# === solve block: coherence_lengths.csv ===
python3 /solution/generate.py coherence /app/outputs/coherence_lengths.csv
