#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: Tc_alpha_vs_doping.csv ===
python3 << 'EOF'
import csv
out = "/app/outputs/Tc_alpha_vs_doping.csv"
p0 = 0.162
Tc_max = 193.0
dopings = [0.08, 0.10, 0.12, 0.14, 0.16, 0.162, 0.165, 0.17, 0.18, 0.20, 0.22, 0.24]
rows = []
for p in dopings:
    Tc = Tc_max * max(0.0, 1.0 - 82.6*(p - p0)**2)
    if p != p0:
        alpha = min(0.55, 0.55 * abs(p - p0) / 0.08)
    else:
        alpha = 0.0
    rows.append((p, round(Tc, 2), round(alpha, 3)))
with open(out, 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['doping_p', 'Tc_K', 'isotope_shift_alpha'])
    w.writerows(rows)
EOF

# === solve block: dCDW_gap_meV.txt ===
echo "60.0" > "$OUTDIR/dCDW_gap_meV.txt"

# === solve block: amplitude_ratio.txt ===
echo "0.65" > "$OUTDIR/amplitude_ratio.txt"
