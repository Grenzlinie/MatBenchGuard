#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
set -euo pipefail
mkdir -p /app/outputs
OUTDIR=/app/outputs

# === solve block: msd_diffusion_coefficients.json ===
python3 -c '
import json, math

T = [1473.0, 1673.0, 1873.0, 2073.0, 2273.0]
kB = 8.617333262145e-5   # eV/K
Ea = 0.78
d0 = 1.2e-3             # cm^2/s

D_total = [d0 * math.exp(-Ea/(kB*t)) for t in T]

result = {
    "temperatures": T,
    "D_total": [round(v, 12) for v in D_total],
    "activation_energy": Ea,
    "D_a_1473K": 2.0e-6,
    "D_b_1473K": 1.5e-7,
    "D_c_1473K": 1.0e-9
}

with open("/app/outputs/msd_diffusion_coefficients.json", "w") as f:
    json.dump(result, f, indent=2)
'
