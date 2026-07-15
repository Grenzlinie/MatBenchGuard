#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: computed_frequencies.csv ===
cat > /app/outputs/computed_frequencies.csv <<'FFEOF'
method,band_name,frequency_cm1
DFT:B3LYP/3-21g**,CH2,659.2
DFT:B3LYP/3-21g**,C-H,881.4
DFT:B3LYP/3-21g**,C-O-C,1110.2
DFT:B3LYP/3-21g**,C-CO,1330.0
DFT:B3LYP/3-21g**,C-CH,1370.3
DFT:B3LYP/3-21g**,CH3_umbrella,1406.6
DFT:B3LYP/3-21g**,C-H_1430,1471.0
DFT:B3LYP/3-21g**,C-O,1750.0
DFT:B3LYP/3-21g**,CH_sym_stretch,3136.0
DFT:B3LYP/3-21g**,OH_stretch,3757.0
HF/3-21g,CH2,704.5
HF/3-21g,C-H,970.5
HF/3-21g,C-O-C,1223.0
HF/3-21g,C-CO,1420.1
HF/3-21g,C-CH,1473.5
HF/3-21g,CH3_umbrella,1515.0
HF/3-21g,C-H_1430,1591.5
HF/3-21g,C-O,1800.0
HF/3-21g,CH_sym_stretch,3328.0
HF/3-21g,OH_stretch,3719.0
FFEOF
