#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: cce_alloying_elements.csv ===
cat > /app/outputs/cce_alloying_elements.csv <<'FFEOF'
Alloy_element,Temperature_C,Austenite_vol_fraction,C_austenite_wt
Al,400,0.10,1.45
Cr,400,0.10,1.30
Cu,400,0.10,1.56
Mn,400,0.10,1.57
Mo,400,0.10,1.30
Ni,400,0.10,1.56
Si,400,0.10,1.57
P,400,0.10,1.75
FFEOF

# === solve block: cce_trip_steels.csv ===
cat > /app/outputs/cce_trip_steels.csv <<'FFEOF'
Steel_label,Composition,Intercritical_T_C,Austempering_T_C,V_gamma_calc,C_austenite_CCE_wt
TRIP1,0.19C 1.57Mn 1.46Si 0.06Al,800,400,0.097,1.88
TRIP2,0.19C 1.57Mn 1.46Si 0.06Al,770,400,0.099,1.85
TRIP3,0.19C 1.57Mn 1.46Si 0.06Al,770,450,0.102,1.79
TRIP4,0.31C 1.57Mn 0.34Si 1.23Al,800,400,0.133,2.16
TRIP5,0.31C 1.57Mn 0.34Si 1.23Al,770,400,0.121,2.40
TRIP6,0.31C 1.57Mn 0.34Si 1.23Al,770,450,0.133,2.19
TRIP7,0.11C 1.53Mn 1.50Si,750,450,0.108,1.50
TRIP8,0.218C 1.539Mn 0.267Si 1.750Al,840,400,0.088,2.12
FFEOF
