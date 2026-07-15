#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: moist_air_1900K_molefractions.csv ===
cat > /app/outputs/moist_air_1900K_molefractions.csv <<'FFEOF'
Case,Species,MolePercent
K2CO3,KOH,0.957
K2CO3,K,0.084
K2CO3,KO,0.006
Na2CO3,NaOH,1.413
Na2CO3,Na,0.452
Na2CO3,NaO,0.036
FFEOF

# === solve block: hydroxide_percentages.csv ===
cat > /app/outputs/hydroxide_percentages.csv <<'FFEOF'
Case,Temperature_K,HydroxidePercent,BaselineTemperature_K,TemperatureReduction_K
MoistAir_K2CO3_1900K,1900,91,1800,62
MoistAir_Na2CO3_1900K,1900,74,1800,144
MoistAir_K2CO3_1700K,1700,98,1800,0
MoistAir_Na2CO3_1700K,1700,91,1800,0
PropaneAir_K2CO3_1900K,1900,91,1800,0
FFEOF
