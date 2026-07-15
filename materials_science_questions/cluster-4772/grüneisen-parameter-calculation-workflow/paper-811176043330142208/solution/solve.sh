#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: lattice_parameter_vs_temperature.csv ===
cat > /app/outputs/lattice_parameter_vs_temperature.csv <<'CSVEOF'
temperature_K,lattice_parameter_A
0,4.04100
300,4.03500
600,4.02500
900,4.01800
1200,4.02000
1500,4.02400
CSVEOF

# === solve block: thermal_conductivity_vs_temperature.csv ===
cat > /app/outputs/thermal_conductivity_vs_temperature.csv <<'CSVEOF'
temperature_K,thermal_conductivity_W_mK
300,2.70
600,1.72
900,1.35
1200,1.12
1500,0.97
CSVEOF

# === solve block: weighted_gruneisen_parameter_vs_temperature.csv ===
cat > /app/outputs/weighted_gruneisen_parameter_vs_temperature.csv <<'CSVEOF'
temperature_K,weighted_gruneisen_parameter
0,-1.00
300,-0.80
600,-0.50
900,-0.20
1200,0.10
1500,0.20
CSVEOF
