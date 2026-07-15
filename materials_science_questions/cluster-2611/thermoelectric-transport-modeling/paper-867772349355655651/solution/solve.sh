#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: step_03_N(E_F).txt ===
echo "3.19" > "$OUTDIR/step_03_N(E_F).txt"

# === solve block: step_04_plasma_frequencies.csv ===
cat > "$OUTDIR/step_04_plasma_frequencies.csv" <<'FFEOF'
direction,hbar_omega_p
xx,4.40
yy,2.11
zz,4.71
FFEOF

# === solve block: step_05_thermopower_300K.csv ===
cat > "$OUTDIR/step_05_thermopower_300K.csv" <<'FFEOF'
direction,S_300K
xx,-8.3
yy,-9.6
zz,-0.3
FFEOF

# === solve block: step_06_lambda.txt ===
echo "0.55" > "$OUTDIR/step_06_lambda.txt"
