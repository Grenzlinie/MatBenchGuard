#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
set -euo pipefail
mkdir -p /app/outputs

# === solve block: step_01_dft_results.json ===
cat > /app/outputs/step_01_dft_results.json <<'EOF'
{
  "formation_energy_J_per_mol": -29600.0,
  "lattice_parameter_a_angstrom": 4.3079,
  "lattice_parameter_c_angstrom": 37.1029
}
EOF
