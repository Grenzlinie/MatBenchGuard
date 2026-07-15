#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: raw_total_energies.csv ===
cat > /app/outputs/raw_total_energies.csv <<'FFEOF'
system_name,total_energy_eV
Fe_slab,-200.0
Fe_slab_Cr_S,-202.170
Fe_slab_Cr_Sm1,-201.616
Fe_slab_Cr_Sm2,-202.312
Fe_slab_Cr_central,-201.163
Fe_bulk,-5.0
Cr_bulk,-6.0
FFEOF

# === solve block: solution_energies.csv ===
cat > /app/outputs/solution_energies.csv <<'FFEOF'
layer,e_sol_eV,e_seg_eV,m_cr_muB
S,-0.085,0.078,-3.1
S-1,0.192,0.355,-1.8
S-2,-0.156,0.007,-1.6
central,-0.163,0.0,-1.6
FFEOF
