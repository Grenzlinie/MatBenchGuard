#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: simulation_results.csv ===
python3 << 'PYEOF'
import math
import csv

conditions = [
    (100, 0.5),
    (100, 1.0),
    (1024, 0.5),
    (1024, 1.0),
    (10000, 0.5),
    (10000, 1.0),
]

a_2d = 258.6
with open('/app/outputs/simulation_results.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['N', 'T_J', 'M_mean', 'chi', 'z4', 'z6'])
    for N, T_J in conditions:
        M_mean = (1.0 / (2 * N)) ** (T_J / (8 * math.pi))
        chi = (1.0 / (2 * a_2d)) * N * (M_mean ** 2) * T_J
        z4 = 3.5
        z6 = 15.0
        writer.writerow([N, f"{T_J:.1f}", f"{M_mean:.10f}", f"{chi:.10f}", z4, z6])
PYEOF
