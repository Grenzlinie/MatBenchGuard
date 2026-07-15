#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
set -euo pipefail
mkdir -p /app/outputs

# === solve block: thermo_epc.json ===
python3 <<'PYEOF' > "$OUTDIR/thermo_epc.json"
import json, math, sys

# =============================================
# Physical constants
# =============================================
R = 8.314                # J mol⁻¹ K⁻¹
N_A = 6.02214076e23      # Avogadro constant
kB = 1.380649e-23         # J/K
eV = 1.602176634e-19      # J/eV
mu_star = 0.1
N_atoms = 3               # atoms per formula unit

# =============================================
# Inputs for the two compounds
# (γ, β in mJ; convert to J; Tc in K)
# =============================================
inputs = {
    "MoTe2":       {"gamma": 3.06, "beta": 0.758, "Tc": 0.1},
    "MoTe1.8S0.2": {"gamma": 2.07, "beta": 0.635, "Tc": 1.3}
}

# =============================================
# Helper functions
# =============================================
def compute_Theta_D(beta_mJ):
    """Debye temperature from β (mJ mol⁻¹ K⁻⁴)"""
    beta_J = beta_mJ * 1e-3           # J mol⁻¹ K⁻⁴
    coeff = N_atoms * (12/5) * math.pi**4 * R
    return (coeff / beta_J) ** (1/3)

def compute_N_EF(gamma_mJ):
    """N(E_F) in states/eV per f.u. from γ (mJ mol⁻¹ K⁻²)"""
    gamma_J = gamma_mJ * 1e-3         # J mol⁻¹ K⁻²
    # γ = (π²/3)·k_B²·N_A·N(E_F)  → N(E_F) in 1/J per f.u.
    N_EF_per_J = gamma_J / ((math.pi**2/3) * kB**2 * N_A)
    return N_EF_per_J * eV            # convert to states/eV

def compute_lambda_ep(Tc, Theta_D):
    """McMillan-Allen-Dynes λ_ep (μ*=0.1)"""
    arg = 1.45 * Tc / Theta_D
    if arg <= 0:
        return 0.0
    ln_arg = math.log(arg)
    numerator = mu_star * ln_arg - 1.04
    denominator = 1.04 + ln_arg * (1.0 - 0.62 * mu_star)
    return numerator / denominator

# =============================================
# Compute and build result
# =============================================
result = {}
for key, vals in inputs.items():
    td = compute_Theta_D(vals["beta"])
    nef = compute_N_EF(vals["gamma"])
    lam = compute_lambda_ep(vals["Tc"], td)
    result[key] = {
        "Theta_D": round(td, 2),
        "N_EF":    round(nef, 3),
        "lambda_ep": round(lam, 3)
    }

json.dump(result, sys.stdout, indent=2)
PYEOF
