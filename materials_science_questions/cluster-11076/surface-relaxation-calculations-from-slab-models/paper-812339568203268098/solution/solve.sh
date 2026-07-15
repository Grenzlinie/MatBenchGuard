#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: step_01_diffraction_profile.csv ===
python3 << 'PYEOF'
import csv, math

k_min, k_max, n_points = 0.0, 3.0, 300
k_vals = [k_min + (k_max - k_min) * i / (n_points - 1) for i in range(n_points)]

peak_center = 1.0
sigma = 0.1
background = 0.01

intensity = [math.exp(-0.5 * ((k - peak_center) / sigma) ** 2) + background for k in k_vals]
max_int = max(intensity)
intensity = [v / max_int for v in intensity]

with open('/app/outputs/step_01_diffraction_profile.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['k_percent_BZ', 'intensity'])
    for k, i in zip(k_vals, intensity):
        writer.writerow([f'{k:.6f}', f'{i:.6f}'])
PYEOF
