#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p "/app/outputs"

# === solve block: strengthening_contributions.json ===
python3 <<'PYEOF'
import math, json

# Constants
d = 74e-9        # m
k_HP = 0.09      # MPa·m^(1/2)
sigma_GB = k_HP / math.sqrt(d)   # MPa

Dp = 38e-9       # m
f = 0.03
L = math.sqrt(2.0/3.0) * Dp * (math.sqrt(math.pi/(4.0*f)) - 1.0)  # m
M = 3.06
G = 25.6e9       # Pa
b = 0.286e-9     # m
nu = 0.33
# Orowan strength from Redsten formula (Eq.2)
sigma_or_Pa = (0.4 * M) / (math.pi * math.sqrt(1.0 - nu)) * (G * b / L) * math.log(math.sqrt(2.0/3.0) * Dp / b)
sigma_or = sigma_or_Pa / 1e6  # MPa

# GND strengthening
Delta_alpha = 15e-6
Delta_T = 420
eps_CTE = Delta_alpha * Delta_T
rho_CTE = 12.0 * f * eps_CTE / (b * Dp)
rho_EM = 6.0 * f * eps_CTE / (b * Dp)
eta = 0.5
beta = 0.7
sigma_GND_Pa = (math.sqrt(3.0) * eta * G * b * math.sqrt(rho_EM) +
                math.sqrt(3.0) * beta * G * b * math.sqrt(rho_CTE))
sigma_GND = sigma_GND_Pa / 1e6  # MPa

total = sigma_GB + sigma_or + sigma_GND

result = {
    "grain_boundary_strengthening": round(sigma_GB, 1),
    "orowan_strengthening": round(sigma_or, 1),
    "gnd_strengthening": round(sigma_GND, 1),
    "total_calculated": round(total, 1)
}

with open("/app/outputs/strengthening_contributions.json", "w") as f:
    json.dump(result, f, indent=2)
print("Wrote strengthening_contributions.json")
PYEOF
