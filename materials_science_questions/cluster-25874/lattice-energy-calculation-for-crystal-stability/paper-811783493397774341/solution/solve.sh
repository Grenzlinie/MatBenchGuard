#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: densities.json ===
cat > "$OUTDIR/densities.json" <<'FEJSON'
{
  "alpha_SrNCN": {
    "density_g_per_cm3": 4.09,
    "unit_cell_volume_A3": 207.3,
    "formula_units_per_cell": 4
  },
  "beta_SrNCN": {
    "density_g_per_cm3": 3.98,
    "unit_cell_volume_A3": 159.8,
    "formula_units_per_cell": 3
  }
}
FEJSON

# === solve block: lattice_energies.json ===
cat > "$OUTDIR/lattice_energies.json" <<'FEJSON'
{
  "alpha_SrNCN": {
    "total_energy_per_fu_eV": -135.51,
    "total_energy_per_fu_Ry": -9.960
  },
  "beta_SrNCN": {
    "total_energy_per_fu_eV": -135.55,
    "total_energy_per_fu_Ry": -9.963
  },
  "energy_difference_beta_minus_alpha_eV_per_fu": -0.04,
  "more_stable_polymorph": "beta"
}
FEJSON
