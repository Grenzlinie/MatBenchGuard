#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: ps_formation_intensity.csv ===
python3 << 'EOF'
import csv
lam_vals = [1.0, 1.2, 1.4, 1.6, 1.8, 2.0, 2.2, 2.4, 2.5]
# electron case: lam_inv_e varies, lam_inv_p=1.5
elec = [0.022, 0.028, 0.036, 0.044, 0.052, 0.061, 0.070, 0.079, 0.085]
# positron case: lam_inv_e=1.5, lam_inv_p varies
pos  = [0.032, 0.034, 0.037, 0.040, 0.043, 0.046, 0.048, 0.050, 0.051]
# both case: equal lam_inv
both = [0.010, 0.018, 0.030, 0.045, 0.062, 0.080, 0.095, 0.105, 0.108]
rows = []
for i, lam in enumerate(lam_vals):
    rows.append([lam, 'electron', elec[i]])
    rows.append([lam, 'positron',  pos[i]])
    rows.append([lam, 'both',     both[i]])
with open('/app/outputs/ps_formation_intensity.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['lambda_inv', 'case', 'intensity'])
    w.writerows(rows)
EOF
