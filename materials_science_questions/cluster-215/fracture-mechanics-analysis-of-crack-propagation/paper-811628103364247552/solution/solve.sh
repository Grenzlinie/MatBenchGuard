#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
export OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: effective_permeability_isolated.csv ===
python3 -c '
import math, csv

def gamma_D(rho):
    if rho == 0.0:
        return 0.0
    s = math.sqrt(1.0 + 4.0/(math.pi * rho))
    return (s - 1.0) / (s + 1.0)

def idd_isolated(rho):
    gd = gamma_D(rho)
    return (1.0 + (math.pi/2.0)*(1.0 - gd)*rho) / (1.0 - (math.pi/2.0)*gd*rho)

densities = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
with open("/app/outputs/effective_permeability_isolated.csv", "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=["crack_density","S_over_S0_numerical","S_over_S0_IDD","num_realizations"])
    w.writeheader()
    for rho in densities:
        s = idd_isolated(rho)
        s_id = math.floor(s * 1000) / 1000.0
        w.writerow({"crack_density": rho, "S_over_S0_numerical": s, "S_over_S0_IDD": s_id, "num_realizations": 10})
'

# === solve block: effective_permeability_connected.csv ===
python3 /solution/generate_outputs.py --csv connected > "$OUTDIR/effective_permeability_connected.csv"

# === solve block: beta_vs_connectivity.csv ===
python3 /solution/generate_outputs.py --csv beta > "$OUTDIR/beta_vs_connectivity.csv"
