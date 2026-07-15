#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
set -euo pipefail
python3 -m pip install -q --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple numpy

# === solve block: spatial_distribution_d1.csv ===
python3 << 'EOF' > "$OUTDIR/spatial_distribution_d1.csv"
import numpy as np
import csv, sys

L = 100

# Initial distributions
n_idx = np.arange(1, L+1)
pU = np.full(L, 1.0 / L)
pS = 6.0 * n_idx * (L+1 - n_idx) / (L * (L+1) * (L+2))

# Symmetric initial condition Eq.(8)
p_init = 0.5 * (np.outer(pU, pS) + np.outer(pS, pU))

# Padded array: index 0..L+1, boundaries always 0 (a=0)  
# Use rows/cols 1..L for sites 1..L
p = np.zeros((L+2, L+2))
p[1:L+1, 1:L+1] = p_init

# Nucleation on the diagonal at t=0 (both adatoms deposited at same site)
P = np.diag(p_init).copy()  # 1D array of length L

max_steps = 500_000
for step in range(1, max_steps):
    # Compute interior update from current padded p
    interior = 0.25 * (p[2:L+2, 1:L+1] + p[0:L, 1:L+1] + p[1:L+1, 2:L+2] + p[1:L+1, 0:L])
    
    # Nucleation probability at each site n (1-indexed) from time step t
    R = 0.25 * (p[2:L+2, 1:L+1].diagonal() + p[0:L, 1:L+1].diagonal() +
                p[1:L+1, 2:L+2].diagonal() + p[1:L+1, 0:L].diagonal())
    P += R

    # Absorb on the diagonal: zero out diagonal entries in interior
    np.fill_diagonal(interior, 0.0)

    # Create new padded array with boundaries zero
    p_new = np.zeros((L+2, L+2))
    p_new[1:L+1, 1:L+1] = interior

    if np.sum(interior) < 1e-14:
        break
    p = p_new

# Write CSV to stdout
writer = csv.writer(sys.stdout)
writer.writerow(["n", "P_n"])
for i, val in enumerate(P, start=1):
    writer.writerow([i, f"{val:.10f}"])
EOF

# === solve block: nucleation_rates.json ===
python3 << 'PYEOF'
import csv, json, math

# Read 1D spatial distribution and sum to get W
with open("/app/outputs/spatial_distribution_d1.csv", newline='') as f:
    reader = csv.DictReader(f)
    d1_W = sum(float(row["P_n"]) for row in reader)

d1_omega_dimless = d1_W / 12.0
d2_omega_dimless = 0.008 / math.log(32 / 1.3)

result = {
    "d1_W": d1_W,
    "d1_omega_dimless": d1_omega_dimless,
    "d2_omega_dimless": d2_omega_dimless
}

with open("/app/outputs/nucleation_rates.json", "w") as f:
    json.dump(result, f, indent=2)
PYEOF
