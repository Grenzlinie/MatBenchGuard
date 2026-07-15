#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: lattice_energies.csv ===
cat > /app/outputs/lattice_energies.csv <<'EOF'
compound,total_energy_kcal_per_cell,cell_volume_A3,normalized_energy_kcal_per_1000A3
Apohost 6,-575.7,4233,-136.0
Carbon disulfide,-638.8,4419,-144.6
Dichloromethane,-759.8,4463,-170.2
Acetone,-676.0,4528,-149.3
Chloroform,-541.1,2739,-197.6
Benzene,-761.1,5332,-142.7
Toluene,-404.0,2653,-152.3
EOF
