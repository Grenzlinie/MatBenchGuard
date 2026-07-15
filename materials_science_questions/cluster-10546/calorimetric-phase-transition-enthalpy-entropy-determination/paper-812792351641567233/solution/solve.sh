#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: temperature_ratio_results.json ===
python3 << 'EOF'
import json, math

gamma = -1.2
B_S = 525.0   # GPa
deltaP = 95.0  # GPa
Tc_Tb = 0.83
DeltaV_IM = -0.015  # cm^3/g
DeltaH_IM = 2.62     # kJ/g

Tb_Ta = math.exp(gamma * deltaP / B_S)
T2_T1_path = Tb_Ta * Tc_Tb

# Unit compatibility: GPa * cm^3/g = kJ/g
product = DeltaV_IM * deltaP   # kJ/g
exponent = product / DeltaH_IM
T2_T1_CC = math.exp(exponent)

result = {
    "T2_T1_path_decomposition": T2_T1_path,
    "Tb_Ta": Tb_Ta,
    "T2_T1_Clausius_Clapeyron": T2_T1_CC
}

with open("/app/outputs/temperature_ratio_results.json", "w") as f:
    json.dump(result, f, indent=2)
EOF
