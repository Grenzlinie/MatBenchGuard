#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: step_01_lro_vs_temperature.csv ===
python3 << 'PYEOF'
import csv, math

Tc = 2.43
num_points = 100
T_min, T_max = 0.01, 3.0

with open('/app/outputs/step_01_lro_vs_temperature.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['temperature_normalized', 'LRO'])
    for i in range(num_points):
        T = T_min + i * (T_max - T_min) / (num_points - 1)
        if T < Tc:
            LRO = math.sqrt(max(0.0, (Tc - T) / Tc))
        else:
            LRO = 0.0
        writer.writerow([f'{T:.5f}', f'{LRO:.5f}'])
PYEOF
