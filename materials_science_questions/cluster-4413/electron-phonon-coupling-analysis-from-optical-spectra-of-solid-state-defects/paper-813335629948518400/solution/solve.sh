#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
export OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: polaron_spectral_weights.csv ===
cat > "$OUTDIR/polaron_spectral_weights.csv" << 'FFEOF'
tube_id,diameter_nm,chiral_angle_deg,phonon_mode,temperature_K,polaron_shift_meV,spectral_weight_transfer_percent
zigzag_9_0,0.7047,0.0,Gamma-LO,300,15.0,35.0
zigzag_9_0,0.7047,0.0,K,300,35.0,60.0
zigzag_12_0,0.939,0.0,Gamma-LO,300,10.0,25.0
zigzag_12_0,0.939,0.0,K,300,25.0,45.0
zigzag_15_0,1.174,0.0,Gamma-LO,300,7.0,18.0
zigzag_15_0,1.174,0.0,K,300,20.0,35.0
zigzag_18_0,1.409,0.0,Gamma-LO,300,5.0,12.0
zigzag_18_0,1.409,0.0,K,300,15.0,25.0
zigzag_21_0,1.644,0.0,Gamma-LO,300,3.0,8.0
zigzag_21_0,1.644,0.0,K,300,10.0,15.0
kataura_12_0,0.939,0.0,Gamma-LO,300,10.0,25.0
kataura_12_0,0.939,0.0,K,300,25.0,45.0
kataura_11_2,0.949,8.2,Gamma-LO,300,9.0,22.0
kataura_11_2,0.949,8.2,K,300,23.0,40.0
kataura_10_4,0.978,16.1,Gamma-LO,300,8.0,18.0
kataura_10_4,0.978,16.1,K,300,20.0,35.0
zigzag_18_0,1.409,0.0,Gamma-LO,1000,5.0,22.0
FFEOF
