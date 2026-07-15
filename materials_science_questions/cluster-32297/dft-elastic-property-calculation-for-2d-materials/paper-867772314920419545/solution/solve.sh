#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: reproduced_properties.json ===
cat > /app/outputs/reproduced_properties.json <<'FFEOF'
{
  "lattice_constant_a_angstrom": 5.415,
  "lattice_constant_b_angstrom": 5.782,
  "cohesive_energy_eV_per_atom": -3.84,
  "bond_length_d1_angstrom": 2.436,
  "bond_length_d2_angstrom": 2.320,
  "bond_length_d3_angstrom": 2.379,
  "buckling_height_angstrom": 3.740,
  "spin_up_band_gap_eV": 0.62,
  "magnetic_moment_per_Co_muB": 1.04,
  "curie_temperature_K": 770,
  "critical_strain_x": 0.56,
  "critical_strain_y": 0.53,
  "ideal_strength_x_GPa": 16.19,
  "ideal_strength_y_GPa": 11.50,
  "negative_poisson_ratio_yz": -0.24,
  "bond_angle_alpha_change_stage1_percent": 22.0,
  "bond_length_d3_change_stage1_percent": 2.0,
  "bond_angle_alpha_change_stage2_percent": 26.0,
  "bond_length_d3_change_stage2_percent": 12.0,
  "stress_jump_strain_x": 0.24,
  "new_dimer_bond_length_d4_angstrom": 2.45
}
FFEOF
