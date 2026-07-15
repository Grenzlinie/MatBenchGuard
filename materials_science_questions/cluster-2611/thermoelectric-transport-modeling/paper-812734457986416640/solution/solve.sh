#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: ZT_vs_Ef.csv ===
python3 << 'PYEOF'
import csv, math

def zt(ef):
    a1, mu1, sigma1 = 20.0, -0.60, 0.080
    a2, mu2, sigma2 = 17.0,  0.60, 0.080
    bg = 0.5
    return bg + a1*math.exp(-((ef - mu1)/sigma1)**2 / 2.0) + a2*math.exp(-((ef - mu2)/sigma2)**2 / 2.0)

with open('/app/outputs/ZT_vs_Ef.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['Ef', 'ZT'])
    ef = -2.0
    while ef <= 2.0:
        w.writerow([round(ef, 6), round(zt(ef), 8)])
        ef += 0.005
PYEOF

# === solve block: summary.json ===
python3 << 'PYEOF'
import csv, json

max_zt = -1.0
best_ef = 0.0
with open('/app/outputs/ZT_vs_Ef.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader)  # skip header
    for row in reader:
        ef = float(row[0])
        z  = float(row[1])
        if z > max_zt:
            max_zt = z
            best_ef = ef

with open('/app/outputs/summary.json', 'w') as f:
    json.dump({"max_ZT": max_zt, "Ef_at_max_ZT": best_ef}, f)
PYEOF
