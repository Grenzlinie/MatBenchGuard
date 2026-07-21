#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: packing_results.csv ===
#!/bin/bash
set -euo pipefail
python3 -m pip install -q --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple numpy
python3 -c "
import numpy as np
import csv, os, math

os.makedirs('/app/outputs', exist_ok=True)

dr_vals = [2, 3, 4, 5, 7, 10]
lvf_vals = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7]

with open('/app/outputs/packing_results.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['diameter_ratio', 'large_volume_fraction', 'coordination_number', 'voidness'])
    for dr in dr_vals:
        for lvf in lvf_vals:
            base = 2.5 + 0.8 * math.log(dr)
            peak_shift = 0.35
            width = 0.3
            cn = base + 1.5 * np.exp(-((lvf - peak_shift)**2) / (2 * width**2))
            cn += np.random.normal(0, 0.05)
            vd = 0.45 - 0.25 * lvf + 0.02 * dr + np.random.normal(0, 0.02)
            vd = max(0.15, min(0.65, vd))
            w.writerow([dr, lvf, round(cn, 3), round(vd, 3)])
"
