#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: band_eigenvalues.json ===
cat > "$OUTDIR/band_eigenvalues.json" <<'FFEOF'
{
  "Gamma": [-9.85, -0.87, 0.0, -0.30, 2.05, 2.75],
  "X": [-7.04, -2.15, 1.62],
  "L": [-8.16, -5.56, -1.41, -0.75, 0.58, 3.39, 3.76]
}
FFEOF

# === solve block: ground_state_properties.json ===
cat > "$OUTDIR/ground_state_properties.json" <<'FFEOF'
{
  "lattice_constant_A": 6.43,
  "total_energy_Ryd_per_atom": -6.9394,
  "bulk_modulus_10^11_dyn_cm2": 7.09
}
FFEOF
