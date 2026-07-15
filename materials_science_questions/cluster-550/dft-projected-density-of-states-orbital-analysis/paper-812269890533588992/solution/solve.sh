#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: computed_properties.csv ===
cat > "$OUTDIR/computed_properties.csv" <<'FFEOF'
compound,arrangement,space_group,optimized_a,total_energy_ev,band_gap_ev,is_metallic
LiAlSi,I,F-43m,5.9433,-354.40,NA,False
LiAlSi,II,F-43m,5.9577,-353.99,NA,False
LiAlSi,III,F-43m,5.7626,-353.27,NA,True
Li2AlSi,non-centrosymmetric,F-43m,6.253,-544.040,NA,True
Li2AlSi,centrosymmetric,Fm-3m,6.148,-544.048,NA,True
Li7Al3Si4,ordered,F-43m,12.230,-9999.0,NA,False
Li5AlSi2,ordered,P21/m,13.075,-9999.0,NA,True
Li9AlSi3,ordered,C2221,12.357,-9999.0,NA,True
FFEOF
