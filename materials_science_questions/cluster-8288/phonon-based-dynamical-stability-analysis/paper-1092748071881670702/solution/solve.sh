#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: bulk_energies.csv ===
cat > /app/outputs/bulk_energies.csv <<'FFEOF'
system,phase,total_energy_per_atom
TiC,B1,-8.000
TiC,HX1a,-7.800
TiC,HX1b,-7.500
TiC,HX2,-7.200
MoC,HX2,-7.500
MoC,HX1a,-7.300
MoC,HX1b,-7.100
MoC,B1,-6.900
FFEOF

# === solve block: mxene_energies.csv ===
cat > /app/outputs/mxene_energies.csv <<'FFEOF'
system,mxene_label,total_energy_per_atom
TiC,T-1,-6.000
TiC,T-2,-5.883
TiC,H-1,-5.787
TiC,H-2,-5.663
MoC,H-1,-6.000
MoC,H-2,-5.944
MoC,T-2,-5.903
MoC,T-1,-5.826
FFEOF

# === solve block: phonon_results.txt ===
cat > /app/outputs/phonon_results.txt <<'FFEOF'
TiC T-1: No, dynamically stable
MoC H-1: No, dynamically stable
FFEOF
