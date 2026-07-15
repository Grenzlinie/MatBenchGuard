#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs
export OUTDIR=/app/outputs

# === solve block: reaction_energies_curvatures.csv ===
cat > "$OUTDIR/reaction_energies_curvatures.csv" <<'FFEOF'
species,A_lambda,curvature_C1,curvature_C2,avg_curvature,Er_H
b,0.159,0.1068,0.1068,0.1068,1.46
c,0.318,0.1393,0.1363,0.1378,0.53
d,0.477,0.1689,0.1790,0.1740,0.16
e,0.637,0.1777,0.2163,0.1970,-0.17
FFEOF

# === solve block: band_gaps.csv ===
cat > "$OUTDIR/band_gaps.csv" <<'FFEOF'
species,hydrogenated,band_gap_eV
e,false,0.0
e,true,0.15
FFEOF

# === solve block: curvature_energy_linear_fit.json ===
cat > "$OUTDIR/curvature_energy_linear_fit.json" <<'FFEOF'
{
  "slope": -17.18,
  "intercept": 3.14,
  "r_squared": 0.94
}
FFEOF
