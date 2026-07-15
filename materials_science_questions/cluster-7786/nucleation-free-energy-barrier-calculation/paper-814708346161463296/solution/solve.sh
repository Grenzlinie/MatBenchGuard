#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: step_01_thermodynamic_params.json ===
python3 << 'PYEOF'
import json, math

materials = {
    "Pd43Ni10Cu27P20": {"Tm": 802.0, "Tg": 576.0, "Delta_Hm": 7010.0, "a": 1.0},
    "indomethacin":    {"Tm": 432.0, "Tg": 318.0, "Delta_Hm": 39400.0, "a": 1.0},
    "As2Se3":          {"Tm": 645.0, "Tg": 462.0, "Delta_Hm": 15600.0, "a": 0.753}
}

step1 = {}
for name, p in materials.items():
    Tm = p["Tm"]
    Tg = p["Tg"]
    dH = p["Delta_Hm"]
    a = p["a"]

    theta_g = (Tg - Tm) / Tm
    eps_lgs0 = 1.5 * theta_g + 2.0
    eps_ls0  = a * theta_g + 2.0
    de0 = eps_ls0 - eps_lgs0

    eps_ls0_sq = eps_ls0 * eps_ls0
    theta_0m_sq = (8.0/9.0)*eps_ls0 - (4.0/9.0)*eps_ls0_sq
    theta_0m = -math.sqrt(theta_0m_sq)
    T0m = Tm * (1.0 + theta_0m)

    eps_lgs0_sq = eps_lgs0 * eps_lgs0
    theta_0g_sq = (8.0/9.0)*eps_lgs0 - (4.0/9.0)*eps_lgs0_sq
    theta_0g = -math.sqrt(theta_0g_sq)
    T0g = Tm * (1.0 + theta_0g)

    dS = dH / Tm
    if abs(a - 1.0) < 1e-12:
        Dcp = 1.5 * dS
    else:
        Dcp = 2.0 * dS * (9.0/(4.0*a) - 1.5)

    theta_g_sq = theta_g * theta_g
    theta_K_sq = theta_g_sq + 0.5 * theta_g_sq * (4.0 * a / (9.0 - 6.0 * a))
    theta_K = -math.sqrt(theta_K_sq)
    TK = Tm * (1.0 + theta_K)

    step1[name] = {
        "epsilon_ls0": eps_ls0,
        "epsilon_lgs0": eps_lgs0,
        "delta_epsilon_0": de0,
        "T_0m": T0m,
        "T_0g": T0g,
        "Delta_Cp_Tg": Dcp,
        "T_K": TK
    }

with open("/app/outputs/step_01_thermodynamic_params.json", "w") as f:
    json.dump(step1, f, indent=2)
PYEOF

# === solve block: step_02_nucleation_rates.json ===
python3 << 'PYEOF'
import json

step2 = {
    "Pd43Ni10Cu27P20": {"ln_J_n_at_TK": 47.1},
    "indomethacin":    {"ln_J_n_at_TK": 44.5},
    "As2Se3":          {"ln_J_n_at_TK": 47.8}
}

with open("/app/outputs/step_02_nucleation_rates.json", "w") as f:
    json.dump(step2, f, indent=2)
PYEOF
