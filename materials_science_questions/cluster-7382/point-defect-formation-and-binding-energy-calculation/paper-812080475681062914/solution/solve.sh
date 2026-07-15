#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: step_01_formation_enthalpies.csv ===
cat > /app/outputs/step_01_formation_enthalpies.csv <<'FFEOF'
compound,V_A_enthalpy,V_B_enthalpy
SiC,4.94,2.92
AlAs,2.76,2.75
AlSb,2.30,2.81
GaN,5.10,2.73
GaP,2.98,2.64
GaAs,2.59,2.59
GaSb,2.03,2.56
InP,3.04,2.17
InAs,2.61,2.07
InSb,2.12,2.12
ZnO,5.41,3.00
ZnS,3.47,3.13
ZnSe,3.09,3.09
ZnTe,2.54,3.06
CdS,3.56,2.69
CdSe,3.18,2.65
CdTe,2.75,2.75
FFEOF
