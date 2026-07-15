#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: step_02_results.csv ===
python3 << 'EOF'
import csv

def cp(T, a, b, c):
    return a * (1 - 1/(1 + b * T * T)) + c * T

rows = []
# LiBO2 coefficients from Table 2 (a in J/(mol·K), b in 1/K^2, c in J/(mol·K^2))
libo2 = [
    (298.15, 700, 62.082, 3.384e-5, 0.04636, 0.27738, 0.99995),
    (298.15, 1000, 58.259, 3.888e-5, 0.05135, 0.57288, 0.99993),
    (298.15, 1117, 57.364, 4.057e-5, 0.05240, 0.6843, 0.99994),
    (298.15, 1500, 56.095, 4.369e-5, 0.05371, 0.92854, 0.99995),
    (298.15, 2000, 55.191, 4.663e-5, 0.05452, 1.1699, 0.99996),
]
for start, end, a, b, c, delta, r in libo2:
    rows.append(['LiBO2', start, end, a, b, c, cp(100, a, b, c), cp(200, a, b, c), cp(298.15, a, b, c), delta, r])

# BaS coefficients from Table 2
bas = [
    (298.15, 700, 47.994, 28.381e-5, 0.01070, 0.18121, 0.99942),
    (298.15, 1000, 49.612, 18.820e-5, 0.00838, 0.33651, 0.99926),
    (298.15, 1500, 50.236, 16.309e-5, 0.00765, 0.41666, 0.99960),
    (298.15, 2000, 50.362, 15.813e-5, 0.00753, 0.43245, 0.99979),
    (298.15, 3000, 50.328, 15.971e-5, 0.00755, 0.43765, 0.99993),
]
for start, end, a, b, c, delta, r in bas:
    rows.append(['BaS', start, end, a, b, c, cp(100, a, b, c), cp(200, a, b, c), cp(298.15, a, b, c), delta, r])

with open('/app/outputs/step_02_results.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['compound', 'interval_start', 'interval_end', 'a', 'b', 'c', 'Cp_100', 'Cp_200', 'Cp_298', 'Delta', 'R'])
    w.writerows(rows)
EOF
