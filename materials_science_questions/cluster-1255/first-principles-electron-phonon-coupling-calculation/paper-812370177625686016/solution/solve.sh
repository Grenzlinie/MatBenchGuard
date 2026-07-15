#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs
OUTDIR=/app/outputs

# === solve block: results.json ===
python3 << 'PYEOF' > "$OUTDIR/results.json"
import json, math, sys

euler_gamma = 0.5772156649015328606
factor = 2 * math.exp(euler_gamma) / math.pi

cases = [
    {"case_id": "n2_generic", "n": 2,
     "lam": [0.30, 0.15], "omega": [50.0, 200.0], "alpha0": [0.5, 0.5]},
    {"case_id": "n2_coulomb", "n": 2,
     "lam": [0.45, -0.12], "omega": [60.0, 5000.0], "alpha0": [0.5, 0.0]},
    {"case_id": "n3_coulomb", "n": 3,
     "lam": [0.20, 0.10, -0.08], "omega": [30.0, 100.0, 1000.0],
     "alpha0": [0.5, 0.0, 0.0]},
    {"case_id": "case_a", "n": 3,
     "lam": [0.25, 0.35, -0.10], "omega": [40.0, 120.0, 600.0],
     "alpha0": [0.5, 0.5, 0.0]},
    {"case_id": "case_b", "n": 3,
     "lam": [0.35, 0.20, -0.10], "omega": [100.0, 250.0, 800.0],
     "alpha0": [0.5, 0.0, 0.0]},
]

results = []
for case in cases:
    n = case["n"]
    lam = case["lam"]
    omega = case["omega"]
    alpha0 = case["alpha0"]

    # Compute lam_star (1-indexed, lam_star[k] = λ_k*)
    lam_star = [0.0] * (n + 1)   # index 1..n
    for k in range(n, 1, -1):
        l_k = math.log(omega[k-1] / omega[k-2])
        if k == n:
            lam_k1_star = 0.0
        else:
            lam_k1_star = lam_star[k+1]
        denom = 1.0 - (lam[k-1] + lam_k1_star) * l_k
        lam_star[k] = (lam[k-1] + lam_k1_star) / denom

    lam_tilde = lam[0] + lam_star[2]
    Tc = factor * omega[0] * math.exp(-1.0 / lam_tilde)

    # Compute Lambda_k (1-indexed)
    Lambdas = [0.0] * (n + 2)   # index 1..n+1, with Lambda_{n+1}=0
    Lambdas[1] = 1.0
    for k in range(2, n+1):
        prod = 1.0
        for l in range(1, k):   # l = 1 .. k-1
            ratio = lam_star[l+1] / (lam[l-1] + lam_star[l+1])
            prod *= ratio * ratio
        Lambdas[k] = prod
    Lambdas[n+1] = 0.0

    alpha = 0.0
    for k in range(1, n+1):
        C_k = Lambdas[k] - Lambdas[k+1]
        alpha += C_k * alpha0[k-1]

    results.append({"case_id": case["case_id"], "Tc": Tc, "alpha": alpha})

json.dump(results, sys.stdout, indent=2)
PYEOF
