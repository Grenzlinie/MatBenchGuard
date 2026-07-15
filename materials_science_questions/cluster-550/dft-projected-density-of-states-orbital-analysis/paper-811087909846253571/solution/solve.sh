#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: binary_lattice_constants_bulk_moduli.csv ===
cat > /app/outputs/binary_lattice_constants_bulk_moduli.csv <<'FFEOF'
binary,a0_angstrom,B0_GPa
GaN,4.521,185.15
TlN,5.224,170.14
BN,3.617,388.73
FFEOF

# === solve block: binary_band_gaps.csv ===
cat > /app/outputs/binary_band_gaps.csv <<'FFEOF'
binary,gap_type,energy_eV
GaN,E_Γ-Γ,3.123
TlN,E_Γ-Γ,0.000
BN,E_Γ-X,5.838
FFEOF

# === solve block: quaternary_lattice_constant.txt ===
echo 4.53 > /app/outputs/quaternary_lattice_constant.txt

# === solve block: quaternary_bandgap.txt ===
echo 1.639 > /app/outputs/quaternary_bandgap.txt

# === solve block: quaternary_optical_constants.csv ===
cat > /app/outputs/quaternary_optical_constants.csv <<'FFEOF'
property,value
static_dielectric_constant,5.47
static_refractive_index,2.35
FFEOF
