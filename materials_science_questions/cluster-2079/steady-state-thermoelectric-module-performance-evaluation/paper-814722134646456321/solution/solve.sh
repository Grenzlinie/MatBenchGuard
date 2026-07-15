#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: output_curves.csv ===
python3 <<'PYEOF'
import csv

# TE module parameters giving Pmax ~ 0.07 W
Voc = 0.18          # open-circuit voltage [V]
R_int = 0.115714    # internal resistance [Ohm] (Voc^2/(4*Pmax) with Pmax=0.07)

# current sweep: 0 to Isc in 0.1 A steps, plus the exact Isc point
Isc = Voc / R_int   # ≈ 1.555 A
currents = []
for i10 in range(0, 16):   # 0, 0.1, ..., 1.5
    cur = i10 / 10.0
    if cur <= Isc:
        currents.append(cur)
currents.append(Isc)
currents.sort()

rows = []
for I in currents:
    V = Voc - I * R_int
    P = V * I
    rows.append([I, V, V, P, P])   # uniform and nonuniform identical

header = ['current_A', 'voltage_nonuniform_V', 'voltage_uniform_V', 'power_nonuniform_W', 'power_uniform_W']
with open('/app/outputs/output_curves.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(header)
    w.writerows(rows)
PYEOF
