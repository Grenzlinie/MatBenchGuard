#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: spin_densities.csv ===
cat > /app/outputs/spin_densities.csv <<'CSVEOF'
ligand,rho_Al_t
H,0.63
F,0.65
Cl,0.66
Br,0.64
OH,0.65
NH2,0.64
CH3,0.62
C6H5,0.64
CSVEOF

# === solve block: bond_energies.csv ===
cat > /app/outputs/bond_energies.csv <<'CSVEOF'
ligand,D1_eV,D2_eV
H,2.14,3.12
F,4.88,5.71
Cl,3.37,4.23
Br,2.87,3.72
OH,3.21,4.07
NH2,1.73,2.61
CH3,0.75,1.72
C6H5,0.74,1.62
CSVEOF
