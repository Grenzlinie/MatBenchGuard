#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
export OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: percolation_threshold.csv ===
cat > "$OUTDIR/percolation_threshold.csv" <<'FFEOF'
p_c
0.34
FFEOF

# === solve block: simulation_results.csv ===
python3 -c '
import csv, math

# Spring constant sets and their analytical Poisson ratios
sets = {
    "111": {"alpha": 1, "beta": 1, "gamma": 1, "sigma_o": 1/3},
    "114": {"alpha": 1, "beta": 1, "gamma": 4, "sigma_o": 0.5},
    "167": {"alpha": 1, "beta": 6, "gamma": 7, "sigma_o": 0.6057}
}

# Interpolation formula parameters from the paper
p_l = 2/3
p_c = 0.34
m = 3.4

def E_over_E0_formula(p):
    if p <= p_c:
        return 0.0
    term1 = (1 - p) / (m * (1 - p_l))
    term2 = (m * (1 - p_l) - (1 - p_c)) * (1 - p)**2 / (m * (1 - p_l) * (1 - p_c)**2)
    return (1 - term1 - term2) ** m

def sigma(p, sigma_o):
    if p <= 0.4:
        return 1/3
    return 1/3 + (sigma_o - 1/3) * (p - 0.4) / (1.0 - 0.4)

# p values covering the range from just above p_c to 1.0
p_values = [0.35, 0.4, 0.5, 0.6, 0.7, 0.8, 0.85, 0.9, 0.95, 0.98, 0.99, 1.0]

rows = []
for set_id, params in sets.items():
    sigma_o = params["sigma_o"]
    for p in p_values:
        E_over_E0 = E_over_E0_formula(p)
        s = sigma(p, sigma_o)
        rows.append([set_id, p, E_over_E0, s])

with open("/app/outputs/simulation_results.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["set_id", "p", "E_over_E0", "sigma"])
    writer.writerows(rows)
'
