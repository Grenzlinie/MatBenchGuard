#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: free_energy_coefficients.json ===
python3 << 'PYEOF'
import json, os, math

# Heat capacity equations (cal/(K·mol)):
# CH4: 3.47 + 0.019 T
# H2:  6.52 + 0.00044 T
# C (amorph): 1.1 + 0.0024 T + 4.0e-7 T^2

# ΔCp = Cp(CH4) - [2*Cp(H2) + Cp(C)]
delta_C0 = 3.47 - (2*6.52 + 1.1)        # = -10.67
alpha    = 0.019 - (2*0.00044 + 0.0024)  # = 0.01572
beta     = 0.0 - 4.0e-7                   # = -4.0e-7   (paper erroneously used +4e-7)

I = 42.2
T0 = 293.0
delta_H_293 = -21730.0   # -ΔH₍ìì= 21730 cal ⇒ ΔH(293) = -21730

# ΔH(T) = ΔH₀ + ΔC₀ T + (α/2) T² + (β/3) T³
# ⇒ ΔH₀ = ΔH(293) - [ΔC₀·293 + (α/2)·293² + (β/3)·293³]
term_C0   = delta_C0 * T0
term_alfa = (alpha / 2.0) * T0**2
term_beta = (beta / 3.0) * T0**3

delta_H0 = delta_H_293 - term_C0 - term_alfa - term_beta
neg_delta_H0 = -delta_H0   # the constant term in -ΔF(T)

# Evaluate -ΔF(298) = -ΔH₀ + ΔC₀·T·ln(T) + (α/2)·T² + (β/6)·T³ + I·T
T = 298.0
term1 = neg_delta_H0
term2 = delta_C0 * T * math.log(T)
term3 = (alpha / 2.0) * T**2
term4 = (beta / 6.0) * T**3
term5 = I * T
delta_F_298 = term1 + term2 + term3 + term4 + term5

result = {
    "delta_H0": round(neg_delta_H0, 6),
    "delta_C0": delta_C0,
    "alpha": alpha,
    "beta": beta,
    "I": I,
    "delta_F_298": round(delta_F_298, 2)
}

outfile = "/app/outputs/free_energy_coefficients.json"
os.makedirs(os.path.dirname(outfile), exist_ok=True)
with open(outfile, "w") as f:
    json.dump(result, f, indent=2)
PYEOF
