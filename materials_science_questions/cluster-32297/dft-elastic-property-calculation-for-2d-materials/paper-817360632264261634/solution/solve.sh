#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: step_01_energy_surface.csv ===
python3 << 'PYEOF'
import csv
q_vals = [-1.5, -1.0, -0.5, 0.0, 0.5, 1.0, 1.5]
b02 = -47.1
b04 = 245.7
b06 = -116.0
b08 = 17.3
c12 = -356.7
c14 = 100.1
a20 = 102.6

with open('/app/outputs/step_01_energy_surface.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Q1', 'Q2', 'energy_mev_per_fu'])
    for q1 in q_vals:
        for q2 in q_vals:
            E = (b02 * q2**2 + b04 * q2**4 + b06 * q2**6 + b08 * q2**8 +
                 c12 * q1 * q2**2 + c14 * q1 * q2**4 + a20 * q1**2)
            writer.writerow([q1, q2, E])
PYEOF
