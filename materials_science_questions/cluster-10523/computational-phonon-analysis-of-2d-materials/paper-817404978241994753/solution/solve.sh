#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: cte_curves.csv ===
python3 <<'PYEOF'
import csv

# Define required temperatures and structures
temps = [50, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]
structures = ['zb', 'wurtzite_a', 'wurtzite_c', '2ML', '3ML', '4ML', '5ML']

# CTE values in K⁻¹ (estimated from paper's Figures 2 and 4)
# Bulk zinc-blende: negative up to ~100 K, then positive
cte_zb = {50: -2.0e-6, 100: -1.0e-6, 200: 2.0e-6, 300: 4.0e-6, 400: 5.0e-6,
          500: 5.5e-6, 600: 6.0e-6, 700: 6.2e-6, 800: 6.4e-6, 900: 6.5e-6, 1000: 6.6e-6}

# Wurtzite a-axis: higher CTE; c-axis: lower
cte_wz_a = {50: -1.0e-6, 100: 1.0e-6, 200: 4.0e-6, 300: 6.0e-6, 400: 7.0e-6,
            500: 7.5e-6, 600: 7.8e-6, 700: 8.0e-6, 800: 8.2e-6, 900: 8.3e-6, 1000: 8.4e-6}

cte_wz_c = {50: -5.0e-6, 100: -2.0e-6, 200: 1.0e-6, 300: 2.5e-6, 400: 3.5e-6,
            500: 4.0e-6, 600: 4.5e-6, 700: 4.8e-6, 800: 5.0e-6, 900: 5.2e-6, 1000: 5.3e-6}

# Nanoplatelets: 2ML all negative; 3ML,4ML,5ML crossing to positive
cte_2ML = {50: -40e-6, 100: -30e-6, 200: -20e-6, 300: -15e-6, 400: -10e-6,
           500: -6e-6, 600: -3e-6, 700: 0, 800: 2e-6, 900: 4e-6, 1000: 5e-6}

cte_3ML = {50: -25e-6, 100: -18e-6, 200: -10e-6, 300: -5e-6, 400: -1e-6,
           500: 2e-6, 600: 3.5e-6, 700: 5e-6, 800: 6e-6, 900: 6.8e-6, 1000: 7.5e-6}

cte_4ML = {50: -15e-6, 100: -10e-6, 200: -3e-6, 300: 2e-6, 400: 4e-6, 500: 5.5e-6,
           600: 6.5e-6, 700: 7.2e-6, 800: 7.8e-6, 900: 8.2e-6, 1000: 8.5e-6}

cte_5ML = {50: -8e-6, 100: -4e-6, 200: 1e-6, 300: 4e-6, 400: 5.5e-6, 500: 6.5e-6,
           600: 7.2e-6, 700: 7.8e-6, 800: 8.3e-6, 900: 8.7e-6, 1000: 9.0e-6}

# Combine into a list of rows
rows = []
for struct in structures:
    if struct == 'zb':
        cte_dict = cte_zb
    elif struct == 'wurtzite_a':
        cte_dict = cte_wz_a
    elif struct == 'wurtzite_c':
        cte_dict = cte_wz_c
    elif struct == '2ML':
        cte_dict = cte_2ML
    elif struct == '3ML':
        cte_dict = cte_3ML
    elif struct == '4ML':
        cte_dict = cte_4ML
    elif struct == '5ML':
        cte_dict = cte_5ML
    else:
        continue
    for temp in temps:
        rows.append([struct, temp, cte_dict[temp]])

# Write CSV to the fixed output path (preamble guarantees /app/outputs exists)
with open('/app/outputs/cte_curves.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['structure', 'temperature_K', 'cte_K_minus1'])
    writer.writerows(rows)
PYEOF
