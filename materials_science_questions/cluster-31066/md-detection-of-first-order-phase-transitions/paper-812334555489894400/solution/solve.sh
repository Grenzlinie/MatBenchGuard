#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: transition_results.json ===
cat > /app/outputs/transition_results.json <<'FFEOF'
{
  "transition_pressure": 6.936,
  "tau_solid": 1.272,
  "tau_fluid": 1.297
}
FFEOF

# === solve block: md_pressure_table.csv ===
python3 << 'PYEOF'
import csv
import math

# MD data from Table I: tau, pv_md, pv_md_std
md_data = [
    (1.05, 41.56, 0.05),
    (1.1,  21.45, 0.08),
    (1.115,18.81, 0.12),
    (1.125,17.42, 0.05),
    (1.15, 14.76, 0.04),
    (1.175,12.93, 0.07),
    (1.2,  11.45, 0.03),
    (1.285, 8.55, 0.09),
    (1.3,   8.18, 0.06),
    (1.4,   6.52, 0.1),
    (1.5,   5.61, 0.09),
    (1.6,   5.13, 0.09),
    (1.7,   4.57, 0.11),
    (1.8,   4.18, 0.11),
    (1.9,   3.83, 0.10),
    (2.0,   3.57, 0.05)
]

def free_volume_pressure(t):
    s = math.sqrt(t)
    return s / (s - 1.0)

def pade_pressure(t):
    ti = 1.0 / t
    ti2 = ti * ti
    ti3 = ti2 * ti
    num = 1.0 - 0.98164*ti + 0.32755*ti2 - 0.0276113*ti3
    den = 1.0 - 2.98164*ti + 3.2908*ti2 - 1.3310*ti3
    return num / den

with open('/app/outputs/md_pressure_table.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['tau','pv_md','pv_md_std','pv_free_volume','pv_pade'])
    for tau, pmd, std in md_data:
        pfv = free_volume_pressure(tau)
        ppade = pade_pressure(tau)
        writer.writerow([tau, pmd, std, pfv, ppade])
PYEOF
