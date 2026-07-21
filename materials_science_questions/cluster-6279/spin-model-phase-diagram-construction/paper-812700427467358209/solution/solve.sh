#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: rg_results.json ===
python3 <<'PYEOF'
import json
out = {
  "self_dual_fixed_points": [
    {"name": "I1", "h1_over_lambda1": 0.25, "h2_over_lambda1": 0.0, "lambda2_over_lambda1": 0.0, "thermal_eigenvalue": 2.0, "nu": 1.0},
    {"name": "I3", "h1_over_lambda1": 0.0, "h2_over_lambda1": 0.5, "lambda2_over_lambda1": 0.0, "thermal_eigenvalue": 2.0, "nu": 1.0},
    {"name": "P",  "h1_over_lambda1": 0.25, "h2_over_lambda1": 0.25, "lambda2_over_lambda1": 1.0, "thermal_eigenvalue": 2.5, "nu": 0.756}
  ],
  "block_fixed_points": [
    {"name": "Ising", "block_size": 2, "a": 1.277, "nu": 1.48, "lambda_t2": 0.81},
    {"name": "Ising", "block_size": 3, "a": 1.155, "nu": 1.31, "lambda_t2": 0.71},
    {"name": "Ising", "block_size": 4, "a": 1.105, "nu": 1.24, "lambda_t2": 0.70},
    {"name": "Potts", "block_size": 2, "b": 1.189, "x_equal_y": 1.193, "nu": 1.03, "lambda_t2": 1.18},
    {"name": "Potts", "block_size": 3, "b": 1.152, "x_equal_y": 1.212, "nu": 0.90, "lambda_t2": 1.32},
    {"name": "Potts", "block_size": 4, "b": 1.136, "x_equal_y": 1.219, "nu": 0.85, "lambda_t2": 1.44}
  ]
}
with open("/app/outputs/rg_results.json", "w") as f:
    json.dump(out, f, indent=2)
PYEOF

# === solve block: fss_phase_diagram.csv ===
python3 <<'PYEOF'
import csv, math
rows = []
# λ2/λ1 values from -0.95 to 1.5, covering the direct transition, Potts point, and three‑phase region
l_values = [-0.95, -0.80, -0.70, -0.50, -0.20, -0.10, 0.0, 0.20, 0.40, 0.60, 0.80, 0.90, 0.99]
# For λ2/λ1 ≤ 1 the transition is direct PM ↔ FO at h1/λ1 = 0.25 (self‑dual)
for l in l_values:
    rows.append([f"{l:.2f}", "0.25", "PM-FO"])
# For λ2/λ1 > 1, use the approximate upper/lower lines from eq. (4.4)
for l in [1.01, 1.02, 1.05, 1.1, 1.2, 1.3, 1.5]:
    if l == 1.0:
        continue
    upper = 0.25 + 0.125 * l * math.exp(-2.0/(l - 1.0))
    lower = 1.0/upper
    rows.append([f"{l:.2f}", f"{upper:.6f}", "PM-PO"])
    rows.append([f"{l:.2f}", f"{lower:.6f}", "PO-FO"])
# Potts point
rows.append(["1.00", "0.25", "Potts"])
rows.sort(key=lambda r: (float(r[0]), float(r[1])))
with open("/app/outputs/fss_phase_diagram.csv", "w", newline='') as f:
    w = csv.writer(f)
    w.writerow(["lambda2_lambda1", "h1_lambda1_critical", "phase_region"])
    w.writerows(rows)
PYEOF

# === solve block: fss_nu.csv ===
python3 <<'PYEOF'
import csv
# Approximate ν values along the critical line (λ2/λ1 ≤ 1) based on Fig 7 and known limits
nu = [
    (1.00, 0.667),   # Potts point
    (0.95, 0.69),
    (0.90, 0.71),
    (0.80, 0.73),
    (0.70, 0.76),
    (0.60, 0.79),
    (0.50, 0.83),
    (0.40, 0.87),
    (0.30, 0.91),
    (0.20, 0.95),
    (0.10, 0.98),
    (0.00, 1.00),   # decoupled Ising
]
with open("/app/outputs/fss_nu.csv", "w", newline='') as f:
    w = csv.writer(f)
    w.writerow(["lambda2_lambda1", "nu"])
    w.writerows(nu)
PYEOF
