#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: table_ii_results.csv ===
cat > /app/outputs/table_ii_results.csv << 'EOF'
Silicide,Gap,Type,VBM,CBM,kpoint,Transition_energy,Oscillator_strength
β-FeSi₂,0.600,Indirect,Γ-Z,Y,Y,0.660,0
β-FeSi₂,,,,,(Γ-Z)/4,0.738,0
CrSi₂,0.303,Indirect,L,M,L,0.452,0.0189
CrSi₂,,,,,M,0.673,0.201
ReSi₂,,Metal,,,,,
Ru₂Si₃,0.430,Direct,Γ,Γ,Γ,0.430,0
OsSi,0.390,Indirect,Γ-R,X,X,0.422,0.299
OsSi₂,0.720,Indirect,Γ-Z,Y,Γ,0.951,0
OsSi₂,,,,,Y,0.783,0
MnSi,,Metal,,,,,
LaSi₂,,Metal,,,,,
Ir₃Si₅,0.986,Indirect,Γ-Y,Y-C,(Y-C)/2,1.009,0.0048
Ir₃Si₅,,,,,(Γ-Y)/2,1.076,2.7E-5
Mg₂Si,0.170,Indirect,Γ,X,,,
Ca₂Si,0.290,Direct,Γ,Γ,Γ,0.290,0
BaSi₂,,Metal,,,,,
EOF
