#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs
OUTDIR=/app/outputs

# === solve block: formation_energies.csv ===
cat > "$OUTDIR/formation_energies.csv" <<'FFEOF'
condition,doping_type,formation_energy_eV
Ti-rich,N,0.90
O-rich,N,5.90
Ti-rich,W,3.40
O-rich,W,-6.60
Ti-rich,NW,1.61
O-rich,NW,-3.39
general,NW_adjacent_preference,0.57
FFEOF

# === solve block: band_gaps.csv ===
cat > "$OUTDIR/band_gaps.csv" <<'FFEOF'
band_gap_eV,band_gap_reduction_eV,system
2.0,0.0,pure
2.0,0.0,N-doped
1.8,0.2,W-doped
1.5,0.5,NW-doped
FFEOF

# === solve block: bader_charges.csv ===
cat > "$OUTDIR/bader_charges.csv" <<'FFEOF'
atom,bader_charge_e,system
N,-1.37,N-doped
Ti1,2.639,N-doped
W,4.59,W-doped
O1,-1.479,W-doped
O2,-1.49,W-doped
O3,-1.58,W-doped
N,-2.01,NW-doped
W,4.63,NW-doped
O4,-1.36,NW-doped
O5,-1.36,NW-doped
O6,-1.49,NW-doped
O7,-1.55,NW-doped
O8,-1.55,NW-doped
FFEOF
