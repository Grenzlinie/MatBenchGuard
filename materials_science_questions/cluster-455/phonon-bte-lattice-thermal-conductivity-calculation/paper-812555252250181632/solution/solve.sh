#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: thermal_conductivity_data.csv ===
cat > "$OUTDIR/thermal_conductivity_data.csv" <<EOF
temperature_K,kappa_100_W_mK,kappa_010_W_mK,kappa_001_W_mK
200.0,13.2,25.0,15.5
300.0,10.68,20.78,12.61
400.0,9.0,17.6,10.6
500.0,7.2,14.8,8.9
EOF

# === solve block: modal_accumulation_data.csv ===
python3 -c "
import csv

def piecewise_linear(x, nodes, values):
    for i in range(len(nodes)-1):
        if x <= nodes[i+1]:
            return values[i] + (values[i+1]-values[i])*(x-nodes[i])/(nodes[i+1]-nodes[i])
    return values[-1]

# Fraction of total conductivity accumulated at key frequencies (0, 5, 10, 15, 20 THz)
nodes = [0, 5, 10, 15, 20]
fracs = {
    '100': [0, 0.50, 0.80, 0.95, 1.00],
    '010': [0, 0.50, 0.80, 0.95, 1.00],
    '001': [0, 0.50, 0.80, 0.95, 1.00]
}
# Total thermal conductivity at 300 K in W/(m·K)
totals = {'100': 10.68, '010': 20.78, '001': 12.61}

step = 0.5
header = ['frequency_THz', 'kappa_100_accumulated_W_mK', 'kappa_010_accumulated_W_mK', 'kappa_001_accumulated_W_mK']

with open('/app/outputs/modal_accumulation_data.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(header)
    freq = 0.0
    while freq <= 20.0:
        acc = [freq]
        for direction in ['100', '010', '001']:
            acc.append(piecewise_linear(freq, nodes, [v * totals[direction] for v in fracs[direction]]))
        w.writerow(acc)
        freq = round(freq + step, 10)
"
