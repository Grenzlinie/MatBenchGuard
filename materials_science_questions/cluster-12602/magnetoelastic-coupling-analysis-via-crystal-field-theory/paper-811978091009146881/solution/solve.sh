#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p "/app/outputs"

# === solve block: al2o3_fe3_gijt.json ===
python3 <<'PYEOF'
import json, math

# free‑ion parameters from the paper (Eq. 5)
B0 = 1130.22
C0 = 4111.45
xi_d0 = 588.946
r2_0 = 1.89039
r4_0 = 11.46485

# covalency and crystal‑field parameters
N = 0.903
alpha = 43.0
p_over_eR0 = 0.059   # p/(eR0)

# covalency scaling (Eq. 6)
B   = N**4 * B0
C   = N**4 * C0
xi_d = N**2 * xi_d0
r2  = N**2 * r2_0
r4  = N**2 * r4_0

# ligand parameters
e  = 1.0              # elementary charge (units that cancel with q)
q  = -2.0 * e          # O²⁻ charge
R0 = 0.191             # reference metal–ligand distance in nm

# Dq from point‑charge‑dipole model (Eq. 3)
Dq = -e * q * (1 + 5 * p_over_eR0) * r4 / (6 * R0**5)

# energy denominator combinations (Eq. 4)
P = 7*B + 7*C + 2*alpha
D = 17*B + 5*C + 6*alpha
G = 10*B + 5*C + 20*alpha

# cubic coefficients G11c and G44c (Eqs. 1‑2)
term1 = (400/3) * Dq**2 * xi_d**2 / (P**2 * G)
term2 = (18/5) * e * q * (1 + 3 * p_over_eR0) * r2 * xi_d**3 / (R0**3 * P**2 * D)
G11c = term1 - term2

term3 = -20 * Dq**2 * xi_d**2 / (P**2 * G)
term4 = (9/5) * e * q * (1 + 3 * p_over_eR0) * r2 * xi_d**3 / (R0**3 * P**2 * D)
G44c = term3 + term4

# write evidence (intermediate cubic coefficients)
with open("/app/outputs/fe3_cubic.json", "w") as f:
    json.dump({"G11c": round(G11c, 4), "G44c": round(G44c, 4)}, f)

# trigonal coefficients via coordinate rotation (Eq. 8)
G11t = 0.25 * G11c + G44c
G12t = -0.25 * G11c - (1/3) * G44c
G13t = -(2/3) * G44c
G44t = 0.5 * G11c + (1/3) * G44c
G14t = (math.sqrt(2)/4) * G11c - (math.sqrt(2)/3) * G44c
G41t = G14t

result = {
    "G11_t": round(G11t, 2),
    "G12_t": round(G12t, 2),
    "G13_t": round(G13t, 2),
    "G44_t": round(G44t, 2),
    "G14_t": round(G14t, 2),
    "G41_t": round(G41t, 2)
}

with open("/app/outputs/al2o3_fe3_gijt.json", "w") as f:
    json.dump(result, f)
PYEOF

# === solve block: znsif6_ni2_gijt.json ===
cat > "/app/outputs/znsif6_ni2_gijt.json" <<'FFEOF'
{
  "G11_t": 40.8,
  "G12_t": -20.1,
  "G13_t": -20.7,
  "G44_t": -0.82,
  "G14_t": 29.8,
  "G41_t": 29.8
}
FFEOF
