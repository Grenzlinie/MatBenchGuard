#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: dft_results.csv ===
# Write the reference DFT results (Table 2)
cat > "$OUTDIR/dft_results.csv" <<'FFEOF'
C_C_A,Cendo_H_A,Nb_Cexo_A,Nb_H_A,inter_ring_angle_deg,model,relative_energy_kcal_mol,state
1.434,2.320,2.338,1.757,43,6,0,a
1.427,2.332,2.344,1.765,54,7,0,a
1.431,2.313,2.333,1.762,61,8,0,a
1.466,1.430,2.299,1.814,38,6,12.45,b
1.448,1.573,2.317,1.809,53,7,9.22,b
1.478,1.385,2.281,1.881,58,8,12.68,b
1.504,1.205,2.278,1.976,47,6,10.61,c
1.503,1.200,2.268,1.988,53,7,6.46,c
1.509,1.193,2.263,2.005,59,8,10.61,c
1.543,1.105,2.265,2.856,48,6,18.91,d
1.540,1.107,2.248,2.766,54,7,14.30,d
1.534,1.110,2.249,2.681,60,8,17.30,d
FFEOF
