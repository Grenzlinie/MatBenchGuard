#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: scc_results.json ===
python3 << 'PYEOF'
import json, math

N = 1000
mu = 2
nu = 1
G_MRT = -3.0
K = math.exp((mu + nu) * G_MRT)
cc = mu / (mu + nu)

def S_CC(c, n3):
    return c*(1-c) - (n3/N)*( mu*(1-c)**2 + nu*c**2 - (mu+nu)**2 * (cc-c)**2 )

def equilibrium_n3(c):
    n3_max = min(N*c/mu, N*(1-c)/nu)
    a = 0.0
    b = n3_max
    f_a = a - K * (N*c)**mu * (N*(1-c))**nu
    f_b = b - K * (N*c - mu*b)**mu * (N*(1-c) - nu*b)**nu if N*c - mu*b >= 0 else b
    if f_a * f_b >= 0:
        return float('nan')
    for _ in range(100):
        mid = (a + b) / 2
        n1 = N*c - mu*mid
        n2 = N*(1-c) - nu*mid
        if n1 < 0 or n2 < 0:
            b = mid
            continue
        f_mid = mid - K * (n1**mu) * (n2**nu)
        if f_mid == 0.0:
            return mid
        if f_a * f_mid < 0:
            b = mid
            f_b = f_mid
        else:
            a = mid
            f_a = f_mid
    return (a + b) / 2

results = {}
for c_val, key_suffix in [(0.1, "c0p1"), (2/3, "c2p3")]:
    frozen_n3 = N * c_val / mu
    eq_n3 = equilibrium_n3(c_val)
    results["frozen_in_" + key_suffix] = S_CC(c_val, frozen_n3)
    results["equilibrium_" + key_suffix] = S_CC(c_val, eq_n3)

with open("/app/outputs/scc_results.json", "w") as f:
    json.dump(results, f, indent=2)
PYEOF
