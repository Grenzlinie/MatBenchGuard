#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: relative_energies.csv ===
cat > "$OUTDIR/relative_energies.csv" <<'FFEOF'
substrate,pattern,unit_cell,relative_energy_eV_per_Al2O3
Ru(0001),pure_o,1x1,1.2
Ru(0001),zigzag_2x1,2x1,0.0
Ru(0001),stripe_3x1,3x1,0.5
Ru(0001),pure_t,1x1,1.0
Al(111),pure_o,1x1,1.8
Al(111),zigzag_2x1,2x1,0.0
Al(111),pure_t,1x1,1.6
FFEOF
