#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: limits.json ===
python3 -c "
import json

# Material constants for 304 stainless steel (from the paper)
kappa2 = 0.012      # MPa⁻¹
a2_alpha = 0.012    # MPa⁻¹ (α-model)
c2 = 10001          # MPa²
rho2 = 1.3          # dimensionless (r-model)

# Saturation limits
k_l = 1.0 / kappa2
alpha_l_norm = 1.0 / a2_alpha
c_l = 1.0 / (a2_alpha * c2)
r_l_norm = 1.0 / rho2

# Thermodynamic inequality checks
c2_a2_sq_inequality = (c2 * a2_alpha**2) >= 1.0
rho2_greater_than_1 = rho2 > 1.0

data = {
    'k_l': k_l,
    'alpha_l_norm': alpha_l_norm,
    'c_l': c_l,
    'r_l_norm': r_l_norm,
    'c2_a2_sq_inequality': c2_a2_sq_inequality,
    'rho2_greater_than_1': rho2_greater_than_1
}

with open('$OUTDIR/limits.json', 'w') as f:
    json.dump(data, f, indent=2)
"
