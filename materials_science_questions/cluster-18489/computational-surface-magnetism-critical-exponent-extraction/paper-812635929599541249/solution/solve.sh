#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: computed_quantities.json ===
#!/bin/bash
# Hidden oracle: write computed_quantities.json with correct values
python3 <<'PYEOF'
import json, math

r0 = 6e-10
f = 0.01
t_list = [0.001, 0.002, 0.005, 0.01, 0.02, 0.05, 0.1]
delta = 7.38
delta2 = delta**2
delta3 = delta**3

def gamma(t):
    return 0.77 * r0 * math.sqrt(t) / f

gammas = [gamma(t) for t in t_list]
Lks = [delta3 * g for g in gammas]
Ds = [delta2 * g for g in gammas]

# Solve D = r0/(2*sqrt(3*t)) for t analytically
t_k_star = f / (delta2 * 0.77 * 2 * math.sqrt(3))
L_k_star = delta3 * 0.77 * r0 * math.sqrt(t_k_star) / f

result = {
    "gamma": gammas,
    "L_k": Lks,
    "D": Ds,
    "t_k_star": t_k_star,
    "L_k_star": L_k_star
}

with open("/app/outputs/computed_quantities.json", "w") as fh:
    json.dump(result, fh, indent=2)
PYEOF
