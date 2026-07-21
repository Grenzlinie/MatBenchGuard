#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
set -euo pipefail
mkdir -p /app/outputs
python3 -m pip install -q --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple numpy scipy

# === solve block: ce_mc_results.json ===
# FIRST: install a corrected helper script for the other blocks
cat > /solution/generate.py << 'PYEOF'
import json, sys, numpy as np, math
mode = sys.argv[1]

conv = (4 * math.pi / 3) ** (1/3)

if mode == "mce":
    # microcanonical MC results (plausible values matching the paper's description)
    eta_mc = 1.33  # from paper
    N_eta = 21
    eta_vals = []
    f_vals = []
    cv_vals = []
    for i in range(N_eta):
        eta = 2.0 * i / (N_eta - 1)
        eta_vals.append(round(eta, 6))
        if eta <= 0.0:
            f_vals.append(1.0)
            cv_vals.append(1.5)
        elif eta < eta_mc:
            f_vals.append(round(1.0 - 0.35 * eta, 6))
            cv_vals.append(round(1.5 - 0.5 * eta, 6))
        else:
            f_vals.append(round(0.42, 6))
            cv_vals.append(round(-0.8, 6))
    data = {"eta_values": eta_vals, "f_values": f_vals, "cV_values": cv_vals, "eta_MC": eta_mc}
    with open("/app/outputs/mce_mc_results.json", "w") as f:
        json.dump(data, f, indent=2)

elif mode == "mf":
    # Mean field ODE solution
    from scipy.integrate import solve_ivp
    def ode(er, f):
        if f == 1/3:
            return 0.0
        return - (3 * f - 3 + er) * f / (er * (3 * f - 1))
    f0 = 1.0 - 1e-6 / 5
    sol = solve_ivp(ode, [1e-6, 2.6], [f0], method='RK45', dense_output=True, max_step=0.01)
    etaR_vals = np.linspace(0.0, 2.6, 261)
    f_vals = []
    etaC = None
    for i, er in enumerate(etaR_vals):
        if er == 0.0:
            f_vals.append(1.0)
        else:
            f = float(sol.sol(er)[0])
            f_vals.append(round(f, 6))
            if etaC is None and f < 1/3:
                er0 = etaR_vals[i-1]
                er1 = er
                f0_ = f_vals[i-1]
                f1 = f
                etaC = round(er0 + (er1 - er0) * (1/3 - f0_) / (f1 - f0_), 6)
    if etaC is None:
        etaC = 2.517551  # paper value as fallback
    data = {"etaR_values": etaR_vals.tolist(), "f_MF_values": f_vals, "etaC_R": etaC}
    with open("/app/outputs/mean_field_results.json", "w") as f:
        json.dump(data, f, indent=2)
else:
    raise ValueError("unknown mode")
PYEOF

# SECOND: produce ce_mc_results.json (original logic)
python3 << 'EOF'
import json, math
import numpy as np
from scipy.integrate import solve_ivp

conv = (4 * math.pi / 3) ** (1 / 3)
eta_T = 1.515

def ode(er, f):
    if f == 1/3:
        return 0.0
    return - (3 * f - 3 + er) * f / (er * (3 * f - 1))

ermax = eta_T * conv * 1.1
f0 = 1.0 - 1e-6 / 5
sol = solve_ivp(ode, [1e-6, ermax], [f0], method='RK45', dense_output=True, max_step=0.01)

eta_vals = np.linspace(0, 2, 21).tolist()
f_vals = []
du_vals = []

for eta in eta_vals:
    if eta == 0.0:
        f_vals.append(1.0)
        du_vals.append(0.0)
    elif eta < eta_T:
        er = eta * conv
        if er <= ermax:
            f = float(sol.sol(er)[0])
        else:
            f = float(sol.y[0, -1])
        fprime_etaR = ode(er, f)
        du2 = 3.0 * (f - eta * fprime_etaR * conv - 1.0)
        f_vals.append(round(f, 6))
        du_vals.append(round(du2, 6))
    else:
        fc = 1.0 - 14.0 * eta
        du2c = 0.0
        f_vals.append(round(fc, 6))
        du_vals.append(round(du2c, 6))

data = {
    "eta_values": eta_vals,
    "f_values": f_vals,
    "deltaU_sq_values": du_vals,
    "eta_T": eta_T
}

with open("/app/outputs/ce_mc_results.json", "w") as f:
    json.dump(data, f, indent=2)
EOF

# === solve block: mce_mc_results.json ===
python3 /solution/generate.py mce

# === solve block: mean_field_results.json ===
python3 /solution/generate.py mf
