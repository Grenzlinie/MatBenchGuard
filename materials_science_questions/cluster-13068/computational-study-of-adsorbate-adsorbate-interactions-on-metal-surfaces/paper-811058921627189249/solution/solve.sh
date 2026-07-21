#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
python3 -m pip install -q --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple numpy scipy

# === solve block: order_parameter.csv ===
python3 << 'EOF'
import numpy as np
from scipy.optimize import root_scalar
import os

def langevin(z):
    if z == 0.0:
        return 0.0
    return (np.exp(z) + np.exp(-z)) / (np.exp(z) - np.exp(-z)) - 1.0 / z

def solve_order(c):
    if c > -3.0:
        return 0.0
    f = lambda m: m - langevin(c * m)
    try:
        sol = root_scalar(f, bracket=[1e-8, 1.0], method='brentq')
        return sol.root
    except ValueError:
        return 0.0

x = np.linspace(0.0, 1.0, 1001)
sim_thresh = 0.154
theory_thresh = 0.183
c_sim = -3.0 * x / sim_thresh
c_theory = -3.0 * x / theory_thresh
m_sim = np.array([solve_order(c) for c in c_sim])
m_theory = np.array([solve_order(c) for c in c_theory])
m_sim_max = m_sim[-1] if m_sim[-1] > 1e-6 else 1.0
m_theory_max = m_theory[-1] if m_theory[-1] > 1e-6 else 1.0
order_sim = m_sim / m_sim_max
order_theory = m_theory / m_theory_max

outdir = os.environ.get('OUTDIR', '/app/outputs')
out_file = os.path.join(outdir, 'order_parameter.csv')
with open(out_file, "w") as f:
    f.write("V22_relative_strength,order_parameter_sim,order_parameter_theory\n")
    for i in range(len(x)):
        f.write(f"{x[i]:.4f},{order_sim[i]:.6f},{order_theory[i]:.6f}\n")
EOF
