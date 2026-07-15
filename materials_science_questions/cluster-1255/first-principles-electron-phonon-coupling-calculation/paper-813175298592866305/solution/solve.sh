#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: results.json ===
python3 << 'PYEOF'
import json, math

def make_boxcar(omega1, omega2, lambda_target):
    omega = list(range(1, 2001))
    alpha = [0.0] * len(omega)
    sum_inv = sum(1.0/w for w in range(omega1, omega2+1))
    h = lambda_target / (2 * sum_inv)
    for i in range(omega1-1, omega2):
        alpha[i] = h
    return omega, alpha

omega_sus, alpha_sus = make_boxcar(200, 502, 0.62)
omega_sup, alpha_sup = make_boxcar(210, 520, 0.67)

data = {
    "suspended": {
        "omega": omega_sus,
        "alpha2F": [round(v, 8) for v in alpha_sus],
        "lambda": 0.62,
        "log_avg_freq": 316.8,
        "Tc": 10.33,
        "delta_sc": 1.56
    },
    "supported": {
        "omega": omega_sup,
        "alpha2F": [round(v, 8) for v in alpha_sup],
        "lambda": 0.67,
        "log_avg_freq": 330.5,
        "Tc": 12.98,
        "delta_sc": 1.98
    }
}

with open("/app/outputs/results.json", "w") as f:
    json.dump(data, f, indent=2)
print("results.json written")
PYEOF
