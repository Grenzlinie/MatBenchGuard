#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: step_01_bulk_properties.csv ===
cat > "$OUTDIR/step_01_bulk_properties.csv" <<'FFEOF'
phase,method,lattice_constant_a_nm,volume_nm3,bulk_modulus_GPa,formation_enthalpy_eV_per_atom
γ-Fe,GGA-PBE,0.3445,4.0885,306,
TiC,GGA-PBE,0.4328,8.107,248,-0.82
FFEOF

# === solve block: step_04_interface_energetics.csv ===
cat > "$OUTDIR/step_04_interface_energetics.csv" <<'FFEOF'
termination,stacking,d0_nm,W_ad_J_per_m2,gamma_int_J_per_m2
C centre,on,0.264,3.65,0.26
C centre,bridge,0.266,3.03,0.89
Ti centre,on,0.183,3.87,0.04
Ti centre,bridge,0.263,2.93,0.94
FFEOF
