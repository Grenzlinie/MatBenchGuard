#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: thermal_expansion_gruneisen.csv ===
cat > /app/outputs/thermal_expansion_gruneisen.csv <<'FFEOF'
Material,Temperature,Alpha,Gamma
CdF2,300,21.77,2.30
CdF2,350,22.03,2.25
CdF2,400,22.29,2.20
CdF2,450,22.55,2.16
CdF2,500,22.81,2.14
CdF2,550,23.07,2.11
CdF2,600,23.33,2.09
CdF2,650,23.58,2.04
PbF2,300,25.43,2.08
PbF2,350,26.20,2.05
PbF2,400,26.98,2.01
PbF2,450,27.76,1.98
PbF2,500,28.54,1.95
PbF2,550,29.32,1.92
PbF2,600,30.10,1.90
PbF2,650,30.88,1.87
FFEOF
