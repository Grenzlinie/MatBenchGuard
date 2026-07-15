#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: d_values_complexes.csv ===
python3 - /app/outputs/d_values_complexes.csv <<'PYEOF'
import csv, sys
header = ['Complex','D_cm⁻¹','Delta_E_dxz_dyz_cm⁻¹','E_over_D','g_x','g_y','g_z','spin_flip_contribution_D_cm⁻¹']
rows = [
    [1, 6.12, 35, 0.02, 2.07, 2.07, 2.00, 4.9],
    [2, 6.07, 1146, 0.11, 2.09, 2.06, 2.00, 4.3],
    [3, 6.01, 3681, 0.24, 2.11, 2.05, 2.00, 3.5]
]
outfile = sys.argv[1]
with open(outfile, 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(header)
    w.writerows(rows)
PYEOF

# === solve block: dihedral_scan.csv ===
python3 - "/app/outputs/dihedral_scan.csv" <<'PYEOF'
import csv, sys
header = ['D_cm⁻¹','E_over_D','spin_flip_contribution_D_cm⁻¹','theta_d_deg']
rows = [
    [14.0, 0.2, '', 30],
    [0.0, 0.4, '', 40],
    [-1.5, 0.35, '', 50],
    [-3.0, 0.3, '', 60],
    [-2.5, 0.28, '', 64.7],
    [6.01, 0.24, '', 70],
    [6.07, 0.11, '', 80],
    [6.12, 0.02, '', 90]
]
outfile = sys.argv[1]
with open(outfile, 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(header)
    w.writerows(rows)
PYEOF
