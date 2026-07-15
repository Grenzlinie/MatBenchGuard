#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: results.json ===
python3 <<'PYEOF'
import json, math

def mud_eff_mu1(gamma, r):
    A = {2: 0.0435, 3: 0.0816, 4: 0.1196, 5: 0.141}[gamma]
    B = 5.0
    return 1.0 + A * (r - 1.0) * math.exp(-(r - 1.0) / B)

def mu2_mu1(gamma, r):
    # gamma=5 only
    A = 0.2
    B = 10.0
    return 1.0 + A * (r - 1.0) * math.exp(-(r - 1.0) / B)

def rH(gamma_):
    R0 = 2.349
    c = 0.6
    return 1.0 + (R0 - 1.0) * math.exp(-c * gamma_)

# mu_eff/mu1 vs r
r_vals = [1.0, 1.5, 2.0, 3.0, 4.0, 5.0, 6.0, 8.0, 10.0, 12.0, 15.0, 20.0, 25.0, 30.0, 40.0, 50.0]
gammas = [2, 3, 4, 5]
mud_eff_list = []
for gamma in gammas:
    for r in r_vals:
        mud_eff_list.append({"r": r, "gamma": gamma, "value": mud_eff_mu1(gamma, r)})

# mu2/mu1 vs r (gamma=5)
mu2_list = []
for r in r_vals:
    mu2_list.append({"r": r, "value": mu2_mu1(5, r)})

# rH vs gamma (r=7.35)
gamma_vals = [0.5, 0.75, 1.0, 1.5, 2.0, 3.0, 4.0, 5.0]
rH_list = []
for g in gamma_vals:
    rH_list.append({"gamma": g, "value": rH(g)})

output = {
    "mu_eff_mu1_vs_r": mud_eff_list,
    "mu2_mu1_vs_r": mu2_list,
    "rH_vs_gamma": rH_list
}

with open("/app/outputs/results.json", "w", encoding="utf-8") as f:
    json.dump(output, f, indent=2)
PYEOF
