#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: thermo_optic_results.json ===
python3 -c '
import json
n0 = 1.82
alpha_T = 6.39e-6
p11 = -0.029
p12 = 0.0091
beta_sigma = 8.48e-6
corr = (alpha_T * n0**3) / 2 * (p11 + 2*p12)
beta_epsilon = beta_sigma + corr
rel_diff = corr / beta_sigma
with open("/app/outputs/thermo_optic_results.json", "w") as f:
    json.dump({"beta_epsilon": beta_epsilon, "relative_difference": rel_diff}, f)
'

# === solve block: bulging_coefficient.json ===
python3 -c "
import json
n0=1.82
alpha_T=6.39e-6
nu=0.26
chi_bg_2 = (n0 - 1) * (1 + nu) * alpha_T
with open('/app/outputs/bulging_coefficient.json','w') as f:
    json.dump({'chi_bg_2': chi_bg_2}, f)
"
