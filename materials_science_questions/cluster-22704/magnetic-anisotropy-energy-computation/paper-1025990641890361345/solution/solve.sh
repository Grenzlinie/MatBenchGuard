#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: cluster_results.json ===
cat > /app/outputs/cluster_results.json <<'FFEOF'
{
  "neutral_ground_state_spin_multiplicity": 5,
  "anion_ground_state_spin_multiplicity": 4,
  "neutral_total_magnetic_moment_muB": 4.0,
  "anion_total_magnetic_moment_muB": 3.0
}
FFEOF

# === solve block: monolayer_pristine_results.json ===
cat > /app/outputs/monolayer_pristine_results.json <<'FFEOF'
{
  "lattice_constant_a_A": 4.70,
  "bond_length_UAu_A": 3.11,
  "magnetic_moment_muB": 2.08,
  "MAE_meV_per_atom": 5.49,
  "delta_E_ex_meV": -109.68,
  "J_meV_per_unit_cell": -6.85
}
FFEOF

# === solve block: monolayer_hydrogenated_results.json ===
cat > /app/outputs/monolayer_hydrogenated_results.json <<'FFEOF'
{
  "delta_E_ex_meV": 20.0,
  "J_meV_per_unit_cell": 5.0
}
FFEOF

# === solve block: curie_temperature.json ===
cat > /app/outputs/curie_temperature.json <<'FFEOF'
{
  "Curie_temperature_K": 210.0
}
FFEOF
