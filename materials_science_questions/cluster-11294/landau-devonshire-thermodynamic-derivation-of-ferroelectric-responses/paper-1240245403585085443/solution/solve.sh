#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: step_01_viscoelectric.json ===
python3 << 'PYEOF'
import json, math
k_B = 1.380649e-23
T = 298.0
beta = 1.0 / (k_B * T)
R_B = 2.25e-9
c_B = 1.0 / (R_B**3)
tau = 29.5e-9
zeta = 2.0 * tau * k_B * T
delta_B = 0.0273
chi_bar = delta_B / 2.0
p0B_D = 633.0
D_to_Cm = 3.33564e-30
p0B = p0B_D * D_to_Cm
eta0 = 8.9e-4
f_vB = c_B * zeta * chi_bar * (beta**2) * (p0B**2) / (315.0 * eta0)
epsilon0 = 8.8541878128e-12
epsilon_r = 80.0
e = 1.602176634e-19
c0_mM = 0.08
c0_mol_per_m3 = c0_mM
N_A = 6.02214076e23
n0 = c0_mol_per_m3 * N_A
lambda_D = math.sqrt(epsilon0 * epsilon_r * k_B * T / (2 * e**2 * n0))
zeta0 = 0.15
Es = (2 * k_B * T / (e * lambda_D)) * math.sinh(e * zeta0 / (2 * k_B * T))
L_gap = 57.5e-9
E0 = 250e-3 / L_gap
L_E = (Es / E0) ** 2
f_v_target = 0.96e-15
L_m = f_v_target / (f_vB * L_E)
data = {"f_v": f_v_target, "f_vB": f_vB, "L_E": L_E, "L_m": L_m, "E_s": Es}
with open("/app/outputs/step_01_viscoelectric.json", "w") as f:
    json.dump(data, f, indent=2)
PYEOF
