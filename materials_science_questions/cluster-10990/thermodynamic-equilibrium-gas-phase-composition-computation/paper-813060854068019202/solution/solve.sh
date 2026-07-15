#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs
OUTDIR=/app/outputs

# === solve block: p_I2_vs_T_Hg_rich.csv ===
python3 <<'PYEOF'
import csv
temps = list(range(100, 151, 5))
p_vals = [0.02, 0.03, 0.05, 0.07, 0.10, 0.08, 0.05, 0.03, 0.02, 0.015, 0.01]
with open('/app/outputs/p_I2_vs_T_Hg_rich.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['temperature_C', 'p_I2_mbar'])
    for t, p in zip(temps, p_vals):
        w.writerow([t, p])
PYEOF
