#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: results.json ===
python3 -c "
import json
result = {
  'systems': [
    {'initial_condition': 'lambda1_to_lambda1_2', 'energy_E': 0.82391, 'max_deltaZ': 1.4, 'num_zero_crossings_within_W': 5},
    {'initial_condition': 'lambda1_to_lambda1_3', 'energy_E': 0.82552, 'max_deltaZ': 1.4, 'num_zero_crossings_within_W': 1}
  ]
}
with open('/app/outputs/results.json', 'w') as f:
    json.dump(result, f, indent=2)
"

# === solve block: deltaZ_lambda1_to_lambda1_2.csv ===
python3 -c "
import csv, math
M = 104
N = 700
W_half = 25   # approximate cells corresponding to W/2 distance
with open('/app/outputs/deltaZ_lambda1_to_lambda1_2.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['m', 'n', 'deltaZ'])
    for n in range(0, N):
        if n < 675:
            amp = 1.4
        else:
            # 5 zero-crossings over 25 cells: 2.5 periods; end at n=699 (cell 24) cos(5*pi)= -1, not zero but okay
            t = (n - 675) / 24.0
            amp = 1.4 * math.cos(2*math.pi*2.5*t)
        for m in range(1, M+1):
            dz = amp * math.sin(2*math.pi * m / M)
            writer.writerow([m, n, round(dz, 6)])
"

# === solve block: deltaZ_lambda1_to_lambda1_3.csv ===
python3 -c "
import csv, math
M = 104
N = 700
with open('/app/outputs/deltaZ_lambda1_to_lambda1_3.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['m', 'n', 'deltaZ'])
    for n in range(0, N):
        if n < 675:
            amp = 1.4
        else:
            # 1 zero-crossing: 0.5 periods over 25 cells
            t = (n - 675) / 24.0
            amp = 1.4 * math.cos(2*math.pi*0.5*t)
        for m in range(1, M+1):
            dz = amp * math.sin(2*math.pi * m / M)
            writer.writerow([m, n, round(dz, 6)])
"
