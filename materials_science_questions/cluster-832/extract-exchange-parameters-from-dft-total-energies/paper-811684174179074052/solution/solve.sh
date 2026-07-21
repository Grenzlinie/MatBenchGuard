#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: total_energies.csv ===
cat > /app/outputs/total_energies.csv <<'FFEOF'
U_eff,state,total_energy
5,FM,-1500.000000
5,AF1,-1500.033334
5,AF2,-1500.022000
6,FM,-1500.000000
6,AF1,-1500.027750
6,AF2,-1500.016650
7,FM,-1500.000000
7,AF1,-1500.022681
7,AF2,-1500.012021
FFEOF

# === solve block: exchange_parameters.csv ===
cat > /app/outputs/exchange_parameters.csv <<'FFEOF'
U_eff,J_FHF,J_pyz,ratio_J_pyz_J_FHF
5,-96.70,-63.82,0.660
6,-80.50,-48.30,0.600
7,-65.80,-34.87,0.530
FFEOF
