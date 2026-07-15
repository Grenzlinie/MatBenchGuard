#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: results.json ===
cat > "$OUTDIR/results.json" <<'FFEOF'
{
  "lattice_constant_A": 8.674,
  "planar_density_atoms_per_A2": 0.364,
  "energy_relative_to_graphene_meV_per_atom": 313,
  "dft_band_gap_eV": 0.2,
  "gw_band_gap_eV": 1.2,
  "max_z_deviation_A": 0.0,
  "ribbon_dft_band_gap_eV": 0.2
}
FFEOF

# === solve finalize ===
echo 'Reference results written.'
