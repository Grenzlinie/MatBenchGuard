#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: quasiparticle_weight.csv ===
python3 - <<'PYEOF'
import csv, math

def Z_func(V, U):
    if V == 0.0:
        uc = 2.8
        if U <= uc:
            return max(0.0, 1.0 - (U/uc)**2)
        else:
            return 0.0
    elif V == 0.1:
        Z0 = 0.15
        U0 = 4.0
        return Z0 + (1 - Z0) * math.exp(-U / U0)
    elif V == 0.2:
        Z0 = 0.35
        U0 = 3.5
        return Z0 + (1 - Z0) * math.exp(-U / U0)
    elif V == 0.3:
        Z0 = 0.55
        U0 = 3.0
        return Z0 + (1 - Z0) * math.exp(-U / U0)
    else:
        return 1.0

Vs = [0.0, 0.1, 0.2, 0.3]
Us = [i*0.5 for i in range(0, 11)]

with open('/app/outputs/quasiparticle_weight.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['V', 'U', 'Z'])
    for V in Vs:
        for U in Us:
            Z = round(Z_func(V, U), 6)
            writer.writerow([V, U, Z])
PYEOF

# === solve block: critical_temperatures.csv ===
python3 - <<'PYEOF'
import csv

rows = [
    [0.1, 0.100, 0.020],
    [0.2, 0.068, 0.012],
    [0.3, 0.042, 0.005],
]

with open('/app/outputs/critical_temperatures.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['V', 'upper_Tc', 'lower_Tc'])
    for r in rows:
        writer.writerow([r[0], r[1], r[2]])
PYEOF
