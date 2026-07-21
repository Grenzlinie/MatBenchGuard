#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: homogenized_results.json ===
cat > /tmp/hom.py << 'HEREDOC'
import json

E0 = 3.3
nu0 = 0.34
E1 = 70.0
nu1 = 0.27
E2 = 101.0
nu2 = 0.06
f0 = 0.7254
f1 = 0.1433
f2 = 0.1313

def bulk_shear(E, nu):
    K = E / (3*(1-2*nu))
    G = E / (2*(1+nu))
    return K, G

def young_poisson(K, G):
    E = 9*K*G/(3*K+G)
    nu = (3*K - 2*G)/(2*(3*K+G))
    return E, nu

K0, G0 = bulk_shear(E0, nu0)
K1, G1 = bulk_shear(E1, nu1)
K2, G2 = bulk_shear(E2, nu2)

# Dilute
K_dil = K0
G_dil = G0
for f, K, G in [(f1,K1,G1),(f2,K2,G2)]:
    K_dil += f * (K - K0) * (3*K0 + 4*G0) / (3*K + 4*G0)
    denom = G0*(9*K0 + 8*G0) + 6*G*(K0 + 2*G0)
    G_dil += f * 5*G0*(G - G0)*(3*K0 + 4*G0) / denom

E_dil, nu_dil = young_poisson(K_dil, G_dil)

# Mori-Tanaka
sum_num_K = 0.0
sum_den_K = 0.0
sum_num_G = 0.0
sum_den_G = 0.0
for f,K,G in [(f0,K0,G0),(f1,K1,G1),(f2,K2,G2)]:
    sum_num_K += f * K / (3*K + 4*G0)
    sum_den_K += f / (3*K + 4*G0)
    denom_G = G0*(9*K0 + 8*G0) + 6*G*(K0 + 2*G0)
    sum_num_G += f * G / denom_G
    sum_den_G += f / denom_G

K_mt = sum_num_K / sum_den_K
G_mt = sum_num_G / sum_den_G

E_mt, nu_mt = young_poisson(K_mt, G_mt)

result = {
    "E_dil": E_dil,
    "v_dil": nu_dil,
    "E_mt": E_mt,
    "v_mt": nu_mt
}
print(json.dumps(result))
HEREDOC
python3 /tmp/hom.py > /app/outputs/homogenized_results.json
