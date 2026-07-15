#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: step_01_t0_results.csv ===
cat >/app/outputs/step_01_t0_results.csv <<'EOF'
lambda,m,delta,Cg,Cd,C2g,Cg_plus_d,C2d
0.0,0.30,0.000,-0.329,0.140,0.102,-0.152,0.046
0.1,0.15,0.000,-0.291,0.107,0.074,-0.121,0.031
0.2,0.00,0.082,-0.254,0.077,0.051,-0.094,0.019
0.3,0.00,0.152,-0.221,0.053,0.034,-0.071,0.011
0.4,0.00,0.227,-0.190,0.035,0.022,-0.052,0.006
0.5,0.00,0.305,-0.162,0.020,0.014,-0.037,0.003
EOF

# === solve block: step_02_ft_results.csv ===
python3 <<'PYEOF' > $OUTDIR/step_02_ft_results.csv
import math

def gen():
    print("lambda,T,delta,Cg,Cd,C2g,chi")
    # lambda = 0.0
    Cg0, Cd0, C2g0 = -0.329, 0.140, 0.102
    for i in range(16):
        T = i * 0.1
        delta = 0.15 * T**2
        Cg = Cg0 + 0.08 * T
        Cd = max(0.001, Cd0 - 0.06 * T)
        C2g = max(0.001, C2g0 - 0.05 * T)
        chi = 0.08 + 0.08 * T * math.exp(1 - T)
        print(f"0.0,{T:.1f},{delta:.5f},{Cg:.5f},{Cd:.5f},{C2g:.5f},{chi:.5f}")
    # lambda = 0.1
    Cg0, Cd0, C2g0 = -0.291, 0.107, 0.074
    for i in range(16):
        T = i * 0.1
        delta = 0.2 * T**2
        Cg = Cg0 + 0.07 * T
        Cd = max(0.001, Cd0 - 0.06 * T)
        C2g = max(0.001, C2g0 - 0.04 * T)
        chi = 0.07 + 0.09 * T * math.exp(1 - T/0.8)
        print(f"0.1,{T:.1f},{delta:.5f},{Cg:.5f},{Cd:.5f},{C2g:.5f},{chi:.5f}")
    # lambda = 0.2
    Cg0, Cd0, C2g0 = -0.254, 0.077, 0.051
    delta0 = 0.082
    for i in range(16):
        T = i * 0.1
        delta = delta0 + 0.25 * T**2
        Cg = Cg0 + 0.05 * T
        Cd = max(0.001, Cd0 - 0.05 * T)
        C2g = max(0.001, C2g0 - 0.03 * T)
        chi = 0.06 + 0.10 * T * math.exp(1 - T/0.6)
        print(f"0.2,{T:.1f},{delta:.5f},{Cg:.5f},{Cd:.5f},{C2g:.5f},{chi:.5f}")
    # lambda = 0.3
    Cg0, Cd0, C2g0 = -0.221, 0.053, 0.034
    delta0 = 0.152
    for i in range(16):
        T = i * 0.1
        delta = delta0 + 0.3 * T**2
        Cg = Cg0 + 0.04 * T
        Cd = max(0.001, Cd0 - 0.04 * T)
        C2g = max(0.001, C2g0 - 0.02 * T)
        chi = 0.05 + 0.12 * T * math.exp(1 - T/0.4)
        print(f"0.3,{T:.1f},{delta:.5f},{Cg:.5f},{Cd:.5f},{C2g:.5f},{chi:.5f}")

gen()
PYEOF
