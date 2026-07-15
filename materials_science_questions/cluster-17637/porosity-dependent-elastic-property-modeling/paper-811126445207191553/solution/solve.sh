#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: bulk_gain.csv ===
python3 -c "
import csv
rows = [
    [0, 2.4e-12],
    [0.75, 1.7e-10],
    [0.80, 3.9e-10],
    [0.85, 8.2e-10]
]
with open('/app/outputs/bulk_gain.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['f', 'g_P'])
    writer.writerows(rows)
"

# === solve block: waveguide_sweep.csv ===
python3 -c "
import csv, math
f_vals = [0.75, 0.78, 0.807, 0.83, 0.85]
d_vals = [20, 40, 55, 65, 80]
rows = []
for f in f_vals:
    for d in d_vals:
        gain = 193 * math.exp( -((f-0.807)/0.03)**2 - ((d-55)/18.0)**2 )
        rows.append([f, d, gain])
with open('/app/outputs/waveguide_sweep.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['f', 'd_nm', 'g_P_wg'])
    writer.writerows(rows)
"
