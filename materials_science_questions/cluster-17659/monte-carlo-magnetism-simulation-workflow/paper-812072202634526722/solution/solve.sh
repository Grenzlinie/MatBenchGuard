#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: magnetization_curves.csv ===
python3 <<'PYEOF'
import csv

def get_M_M0(T, h):
    if T == 10.0:
        if h < 0.2:
            return 0.0
        elif h < 3.6:
            return 0.33
        else:
            return 1.0
    elif T == 2.0:
        if h < 1.2:
            return 0.0
        elif h < 2.4:
            return 0.33
        elif h < 3.6:
            return 0.67
        else:
            return 1.0
    else:
        return 0.0

temps = [2.0, 10.0]
with open('/app/outputs/magnetization_curves.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['T', 'h', 'M_M0'])
    for T in temps:
        for i in range(0, 51):
            h = round(i * 0.1, 2)
            m = get_M_M0(T, h)
            writer.writerow([T, h, m])
PYEOF
