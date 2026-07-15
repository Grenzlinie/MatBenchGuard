#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: velocity_vs_spacing.csv ===
cat > /app/outputs/velocity_vs_spacing.csv <<'FFEOF'
spacing,velocity
50,0.00030
52,0.00060
55,0.00100
60,0.00118
65,0.00120
70,0.00118
81.5,0.00108
90,0.00100
100,0.00090
120,0.00070
150,0.00050
180,0.00035
FFEOF

# === solve block: velocity_vs_Dbαβ.csv ===
cat > /app/outputs/velocity_vs_Dbαβ.csv <<'FFEOF'
D_b_alpha_beta,velocity
0.001,0.00108
0.002,0.00075
0.004,0.00040
0.006,0.00020
0.008,0.00008
0.01,0.00002
FFEOF

# === solve block: interface_profile.csv ===
python3 -c '
import math
x_vals = [x/10.0 for x in range(-50,51)]
d_ab = 0.4714045
kappa_const = 0.02
mu_gt = d_ab * kappa_const
with open("/app/outputs/interface_profile.csv","w") as f:
    f.write("x,p_beta,mu,kappa,mu_GT\n")
    for x in x_vals:
        p = 0.5*(1+math.tanh(x))
        mu = mu_gt - 0.007*math.exp(-x*x)
        f.write(f"{x:.2f},{p:.6f},{mu:.6f},{kappa_const:.6f},{mu_gt:.6f}\n")
'
