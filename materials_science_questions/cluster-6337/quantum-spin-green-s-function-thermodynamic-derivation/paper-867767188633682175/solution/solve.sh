#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
python3 -m pip install -q --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple numpy scipy

# === solve block: bloch_vector_results.json ===
python3 << 'EOF'
import json, numpy as np
from scipy.integrate import quad
from scipy.special import erf, exp1

alpha=1.0; g=1.0; beta=5.0; mu=0.4
gb = g*beta
Z = 2.0/(2.0+gb)

t_vals = np.array([0.0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0])

def integrand_eta(t):
    def f(r):
        s = mu**2 + r**2
        return np.exp(-(gb+2)*r**2) * (r**2 / s) * np.sin(t * np.sqrt(s))**2
    return f

lambda3_0 = 0.5
lambda1_0 = 0.375
lambda2_0 = 0.375

lambda3_list = []
lambda1_list = []
for t in t_vals:
    # eta via quad
    f = integrand_eta(t)
    Ieta, _ = quad(f, 0, np.inf, limit=200)
    eta = (8.0 / Z) * Ieta
    l3 = lambda3_0 * (1.0 - eta)
    lambda3_list.append(float(l3))
    
    # zeta analytic
    a = mu*(gb+2)
    s = np.sqrt(gb+2)
    z1 = (a + 1j*t)/s
    z2 = (a - 1j*t)/s
    diff = erf(z1) - erf(z2)
    prefactor = (1j*t/2) * np.sqrt(np.pi/(2+gb)) * np.exp((2+gb)*mu**2 - t**2/(2+gb))
    zeta_complex = np.cos(2*mu*t) + prefactor * diff
    zeta = np.real_if_close(zeta_complex)
    # xi analytic
    diff_xi = erf(z2) - erf(z1)
    prefactor_xi = (1j*mu/2) * np.sqrt(np.pi*(2+gb)) * np.exp((2+gb)*mu**2 - t**2/(2+gb))
    xi_complex = prefactor_xi * diff_xi
    xi = np.real_if_close(xi_complex)
    
    l1 = lambda1_0 * (zeta + eta/2) + lambda2_0 * xi
    lambda1_list.append(float(l1))

eta_inf = mu**2 * (gb+2) * np.exp(mu**2*(gb+2)) * exp1(mu**2*(gb+2))
tau = np.sqrt(2+gb)

output = {
    "t": t_vals.tolist(),
    "lambda3": lambda3_list,
    "lambda1": lambda1_list,
    "eta_inf": float(eta_inf),
    "tau": float(tau)
}

with open("/app/outputs/bloch_vector_results.json", "w") as f:
    json.dump(output, f, indent=2)
EOF
