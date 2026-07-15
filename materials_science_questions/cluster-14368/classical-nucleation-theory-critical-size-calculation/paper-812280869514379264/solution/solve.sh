#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: results.json ===
python3 << 'PYEOF' > /app/outputs/results.json
import json, math

k_B = 1.380649e-23

# BaSO4
V_Ba = 8.6638e-29
gamma_Ba = 0.136
S_Ba = 25
T_Ba = 298
phi_Ba = 2 * k_B * T_Ba * math.log(S_Ba)
R_Ba = (4 * V_Ba * gamma_Ba**2) / phi_Ba
R_Ba_nm = R_Ba * 1e9

# KClO4
V_K = 9.1263e-29
gamma_K = 0.044
S_K = 1.2
T_K = 280
phi_K = 2 * k_B * T_K * math.log(S_K)
R_K = (4 * V_K * gamma_K**2) / phi_K
R_K_nm = R_K * 1e9

result = {
    "R_BaSO4_nm": round(R_Ba_nm, 6),
    "R_KClO4_nm": round(R_K_nm, 6)
}
print(json.dumps(result))
PYEOF
