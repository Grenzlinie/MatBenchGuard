#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: dopant_di_occupancy.csv ===
cat > "$OUTDIR/dopant_di_occupancy.csv" <<'FFEOF'
ion,d_i_Li,d_i_Nb,occupancy_predicted
Mg,0.215,0.750,Li
Zn,0.161,0.833,Li
Mn,0.320,1.575,Li
Sc,0.279,1.193,Li
In,0.140,1.839,Li
Pr,2.942,6.157,Li
Nd,2.435,5.375,Li
Eu,1.998,4.692,Li
Ho,1.378,3.747,Li
Er,0.962,3.105,Li
Yb,0.723,2.737,Li
Al,1.535,0.742,Nb
Cr,1.059,0.009,Nb
Fe,0.866,0.288,Nb
Ni,1.475,0.650,Nb
Ti,1.518,0.175,Nb
Hf,0.485,1.416,Li
Ta,1.703,0.080,Nb
W,2.730,0.961,Nb
FFEOF

# === solve block: threshold_table.csv ===
cat > "$OUTDIR/threshold_table.csv" <<'FFEOF'
ion,threshold_concentration_mol_percent
Mg,5.20
Zn,5.30
Sc,2.62
In,2.73
Mn,5.03
Al,1.27
Cr,2.60
Fe,2.02
Ni,1.74
Ti,1.03
Hf,1.69
Er,1.90
Yb,2.20
FFEOF
