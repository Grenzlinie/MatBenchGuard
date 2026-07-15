#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: adsorption_energies.csv ===
cat > /app/outputs/adsorption_energies.csv <<'FFEOF'
site,adsorption_energy_eV
T,-6.75
B,-6.80
H1,-7.15
H2,-7.05
FFEOF

# === solve block: diffusion_barriers.csv ===
cat > /app/outputs/diffusion_barriers.csv <<'FFEOF'
path,barrier_eV
surface_path1,0.224
surface_path2,0.224
surface_to_bulk,12.44
FFEOF

# === solve block: theoretical_capacity.txt ===
cat > /app/outputs/theoretical_capacity.txt <<'FFEOF'
106,0.882
FFEOF
