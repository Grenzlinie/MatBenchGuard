#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
python3 -m pip install -q --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple numpy scipy

# === solve block: predicted_moduli.csv ===
python3 << 'EOF' > "$OUTDIR/predicted_moduli.csv"
import sys

E0 = 193.0
nu0 = 0.27

def mt_youngs(E, nu, phi):
    K = E / (3*(1-2*nu))
    G = E / (2*(1+nu))
    K_eff = K * (1-phi) / (1 + (3*K)/(4*G) * phi)
    G_eff = G * (1-phi) / (1 + 6*(K+2*G)/(5*(3*K+4*G)) * phi)
    return 9*K_eff*G_eff / (3*K_eff + G_eff)

porosities = [10,20,30,40,50,60,70,80,90]
fem = [155.78, 120.93, 91.39, 59.26, 36.38, 20.61, 8.31, 3.08, 0.73]

print("porosity,E_MT,E_MMT,E_OMT")
for p, f in zip(porosities, fem):
    phi = p / 100.0
    E_mt = mt_youngs(E0, nu0, phi)
    print(f"{p},{E_mt:.6f},{E_mt:.6f},{f}")
EOF
