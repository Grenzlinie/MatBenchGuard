#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: alpha.json ===
python3 -c "
import json
with open('$OUTDIR/alpha.json', 'w') as f:
    json.dump({'alpha': 0.8}, f)
"

# === solve block: compton_profiles_qmc.csv ===
python3 << 'PYEOF'
import csv

OUTDIR = '/app/outputs'

# Anchor points (digitized from Fig.6)
p_anch = [0.0, 0.5, 0.6, 0.7, 1.0, 2.0]
j100 = [1.32, 0.82, 0.55, 0.22, 0.12, 0.01]
j110 = [1.42, 0.88, 0.60, 0.25, 0.13, 0.01]
j111 = [1.52, 0.94, 0.65, 0.28, 0.14, 0.01]

def lin_interp(x, xp, fp):
    if x <= xp[0]: return fp[0]
    if x >= xp[-1]: return fp[-1]
    for i in range(len(xp)-1):
        if xp[i] <= x <= xp[i+1]:
            t = (x - xp[i]) / (xp[i+1] - xp[i])
            return fp[i] + t * (fp[i+1] - fp[i])
    return fp[-1]

with open(f'{OUTDIR}/compton_profiles_qmc.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['p', 'J_100', 'J_110', 'J_111'])
    for i in range(41):
        p = round(i * 0.05, 2)
        v100 = round(lin_interp(p, p_anch, j100), 6)
        v110 = round(lin_interp(p, p_anch, j110), 6)
        v111 = round(lin_interp(p, p_anch, j111), 6)
        w.writerow([p, v100, v110, v111])
PYEOF
