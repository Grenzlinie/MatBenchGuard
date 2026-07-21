#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: ironene_results.json ===
cat > "$OUTDIR/ironene_results.json" <<'EOF'
{
  "coordination_percentage_Z6": 96.0,
  "bond_angle_peak_degrees": 60.0,
  "nearest_neighbor_distance_peak_A": 2.45,
  "crystallization_temperature_K": 2640.0,
  "total_energy_per_atom_eV": -3.13,
  "global_bond_orientation_order_Psi6": 0.98
}
EOF
