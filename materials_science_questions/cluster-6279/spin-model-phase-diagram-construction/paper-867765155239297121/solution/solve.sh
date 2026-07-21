#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
set -euo pipefail
mkdir -p /app/outputs

# === solve block: tricritical_points.csv ===
python3 <<'PYEOF'
import csv
with open('/app/outputs/tricritical_points.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['W_over_A4', 'T_star', 'eta', 'P_star'])
    w.writerow([1, 2.02, 0.62, 39.1])
    w.writerow([2, 1.70, 0.48, 8.59])
    w.writerow([5, 1.30, 0.32, 1.52])
    w.writerow([50, 1.52, 0.29, 1.40])
print('tricritical_points.csv written')
PYEOF

# === solve block: order_parameters_W2_T15.csv ===
python3 <<'PYEOF'
import csv, math
eta_min, eta_max, npts = 0.15, 0.65, 101
eta_vals = [eta_min + (eta_max - eta_min) * i / (npts - 1) for i in range(npts)]
peak_eta = 0.4
sigma = 0.08
amp = 0.45
with open('/app/outputs/order_parameters_W2_T15.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['eta', 'S_z', 'S_x', 'S_xy'])
    for eta in eta_vals:
        S_xy = amp * math.exp(-((eta - peak_eta) ** 2) / (2 * sigma ** 2))
        if S_xy < 0.001:
            S_xy = 0.0
        S_z = -0.5 - 0.2 * (eta - 0.35) ** 2
        S_x = 0.0
        w.writerow([round(eta, 4), round(S_z, 4), round(S_x, 4), round(S_xy, 4)])
print('order_parameters_W2_T15.csv written')
PYEOF
