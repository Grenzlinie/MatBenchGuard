#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: damage_sensitivity_constants.json ===
mkdir -p /app/outputs
python3 -c '
import json, math

# undamaged concrete parameters (GPa, GPa·s)
kM = 24.42
muM = 13.27
kK = 39.27
muK = 14.07
etaMs = 22.0e8
etaMd = 7.75e8
etaKs = 1.52e8
etaKd = 0.254e8

# ---- bulk-side damage kernel coefficients ----
Qo_o = (16./9.) * etaMs * (etaMs + 2*etaMd) / (etaMd * (2*etaMs + etaMd))
Q1_o = (16./27.) * etaMs * (etaMs**2 + etaMd*etaMs + etaMd**2) / ((2*etaMs + etaMd)**2) * (
    3*(1./muM + 1./muK) - 2*(etaMs/etaMd)*(1./kM + 1./kK)
)
Qo_inf = (4./3.) * kM * (3*kM + 4*muM) / (muM * (3*kM + muM))
Qm1_inf = - (4./3.) * kM * (9*kM**2 + 6*muM*kM + 4*muM**2) / ((3*kM + muM)**2) * (
    3*(kM/muM)*(1./etaMs + 1./etaKs) - 2*(1./etaMd + 1./etaKd)
)

# ---- shear-side damage kernel coefficients ----
M_o_o = (32./45.) * (etaMs + 2*etaMd) * (3*etaMs + 2*etaMd) / ((etaMs + etaMd)*(2*etaMs + etaMd))
M_1_o = (32./45.) * etaMs * etaMd * (7*etaMs**2 + 10*etaMs*etaMd + 4*etaMd**2) / ((etaMs + etaMd)**2 * (2*etaMs + etaMd)**2) * (
    etaMs/(3*kK) + etaMs/(3*kM) - etaMd/(2*muK) - etaMd/(2*muM)
)
M_o_inf = (16./45.) * (9*kM + 4*muM) * (3*kM + 4*muM) / ((3*kM + 2*muM)*(3*kM + muM))
M_m1_inf = (16./15.) * kM * muM * (63*kM**2 + 60*kM*muM + 16*muM**2) / ((3*kM + muM)**2 * (3*kM + 2*muM)**2) * (
    3*kM/etaMs + 3*kM/etaKs - 2*muM/etaMd - 2*muM/etaKd
)

# ---- solve linear systems ----
kappa_M = Qo_inf
v_M_s = Qo_o
kappa_K = Qo_o + kK * ( 3*Q1_o/etaMs - (kappa_M - Qo_o)/kM )
v_K_s = Qo_inf + etaKs * ( Qm1_inf/(3*kM) - (v_M_s - Qo_inf)/etaMs )

m_M = M_o_inf
v_M_d = M_o_o
m_K = M_o_o + muK * ( 2*M_1_o/etaMd - (m_M - M_o_o)/muM )
v_K_d = M_o_inf + etaKd * ( M_m1_inf/(2*muM) - (v_M_d - M_o_inf)/etaMd )

result = {
    "bulk": {
        "kappa_M": kappa_M,
        "kappa_K": kappa_K,
        "v_M_s": v_M_s,
        "v_K_s": v_K_s
    },
    "shear": {
        "m_M": m_M,
        "m_K": m_K,
        "v_M_d": v_M_d,
        "v_K_d": v_K_d
    }
}
with open("/app/outputs/damage_sensitivity_constants.json", "w") as f:
    json.dump(result, f, indent=2)
'
