#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"
python3 -m pip install -q --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple numpy scipy

# === solve block: step_01_zt_vs_filler.csv ===
python3 /solution/helper.py "$OUTDIR/step_01_zt_vs_filler.csv" 0.035 0.06

# === solve block: step_02_zt_noshift.csv ===
python3 /solution/helper.py "$OUTDIR/step_02_zt_noshift.csv" 0.06 0.06

# === solve block: step_03_summary.txt ===
python3 <<'PYEOF'
import csv

def find_peak(filename):
    with open(filename, newline='') as f:
        reader = csv.DictReader(f)
        max_zt = -1.0
        max_vol = None
        for row in reader:
            zt = float(row['ZT'])
            if zt > max_zt:
                max_zt = zt
                max_vol = row['filler_vol_percent']
    return max_zt, max_vol

zt1, vol1 = find_peak("/app/outputs/step_01_zt_vs_filler.csv")
zt2, vol2 = find_peak("/app/outputs/step_02_zt_noshift.csv")

with open("/app/outputs/step_03_summary.txt", 'w') as f:
    f.write(f"Peak ZT (shifted): {zt1} at {vol1}\n")
    f.write(f"Peak ZT (no shift): {zt2} at {vol2}\n")
PYEOF
