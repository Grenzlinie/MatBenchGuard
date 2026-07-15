#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: sellmeier_coefficients.csv ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# Compute and write sellmeier_coefficients.csv
python3 <<'PYEOF'
import csv

# Matsuoka coefficients from the public instruction (Table 1)
coeffs = {
    'a': [
        (228.7018,  4.93e-5,  1.10e-7),
        (46.40806, -3.27e-5, -3.78e-8),
        (0.014173, -1.704e-6, -2.14e-9),
    ],
    'b': [
        (18.111630,  9.15e-5,  7.478e-5),
        (10.671082, -2.9913e-4, -4.8074e-8),
        (0.125,       1e-5,     1e-8),
    ]
}

temperatures = [20, 40]
rows = []
for T in temperatures:
    for i in range(3):
        a_i = coeffs['a'][i][0] + coeffs['a'][i][1]*T + coeffs['a'][i][2]*T*T
        b_i = coeffs['b'][i][0] + coeffs['b'][i][1]*T + coeffs['b'][i][2]*T*T
        rows.append((T, i+1, round(a_i, 8), round(b_i, 8)))

with open('/app/outputs/sellmeier_coefficients.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['temperature', 'i', 'a_i', 'b_i'])
    writer.writerows(rows)
print("sellmeier_coefficients.csv written.")
PYEOF
