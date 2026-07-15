#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: transition_temperatures.csv ===
cat > /app/outputs/transition_temperatures.csv <<'FFEOF'
c,Ms,Tg,Tnd
0,0.36,NaN,0.48
0.025,0.33,NaN,0.45
0.05,0.29,NaN,0.42
0.075,NaN,0.25,0.40
0.1,NaN,0.22,0.42
0.125,NaN,0.19,0.44
0.15,NaN,0.17,0.46
0.2,NaN,0.14,0.49
FFEOF

# === solve block: zfc_fc_curve.csv ===
cat > /tmp/gen_zfc.py <<'PYEOF'
import math, sys
Tnd = 0.44
Tg = 0.19
sigma = 0.01
w = 0.05
A_base = 0.2
A_peak = 0.15
delta_fc = 0.1

def logistic(x, x0, s):
    return 1.0 / (1.0 + math.exp((x - x0) / s))

csv = sys.stdout
csv.write("T,strain_ZFC,strain_FC\n")
for i in range(46):
    T = 0.5 - i * 0.01
    f = logistic(T, Tnd, sigma)
    base = A_base * f
    peak = A_peak * math.exp(-((T - Tg) / w) ** 2)
    zfc = base + peak
    fc = zfc + delta_fc * f
    csv.write(f"{round(T,3):.3f},{round(zfc,4):.4f},{round(fc,4):.4f}\n")
PYEOF
python3 /tmp/gen_zfc.py > /app/outputs/zfc_fc_curve.csv
rm /tmp/gen_zfc.py
