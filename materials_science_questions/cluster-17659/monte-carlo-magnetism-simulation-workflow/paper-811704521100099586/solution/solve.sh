#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
export OUTDIR=/app/outputs
mkdir -p "$OUTDIR"
# Install numpy (required by helper)
python3 -m pip install -q --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple numpy
# Helper script is bundled under /solution/helper.py

# === solve block: hysteresis_noninteracting.csv ===
python3 - > "$OUTDIR/hysteresis_noninteracting.csv" << 'PYEOF'
import csv, math

sigmas = [2, 5, 15]
output_path = "/app/outputs/hysteresis_noninteracting.csv"

with open(output_path, 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['sigma', 'field', 'magnetization'])
    for s in sigmas:
        xi0 = 2.0 * s
        m = 80
        dx = 2.0 * xi0 / m
        # coercive field (increases with sigma)
        Hc = 0.5 * s
        sat = 0.5   # saturation magnetization for random easy axes
        wscale = 0.5
        # forward branch (xi increasing)
        for i in range(m + 1):
            xi = -xi0 + i * dx
            mag = sat * math.tanh((xi + Hc) / wscale)
            w.writerow([s, round(xi, 8), round(mag, 8)])
        # backward branch (xi decreasing, omit first and last to avoid duplicate endpoints)
        for i in range(1, m):
            xi = xi0 - i * dx
            mag = sat * math.tanh((xi - Hc) / wscale)
            w.writerow([s, round(xi, 8), round(mag, 8)])
PYEOF

# === solve block: hysteresis_interacting.csv ===
python3 /solution/helper.py --mode interacting --output "$OUTDIR/hysteresis_interacting.csv"
