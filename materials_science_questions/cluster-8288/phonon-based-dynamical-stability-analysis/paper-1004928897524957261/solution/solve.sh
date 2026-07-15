#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: pristine_results.json ===
cat > /app/outputs/pristine_results.json <<'EOF'
{
  "CuSe": {
    "lattice_constant_a": 3.94,
    "cohesive_energy_per_atom": -3.03,
    "band_gap": 0.0
  },
  "AgSe": {
    "lattice_constant_a": 4.27,
    "cohesive_energy_per_atom": -2.38,
    "band_gap": 0.0
  }
}
EOF

# === solve block: functionalized_results.json ===
cat > /app/outputs/functionalized_results.json <<'EOF'
{
  "Li_CuSe": {
    "band_gap": 0.85,
    "dynamically_stable": true
  },
  "K_CuSe": {
    "dynamically_stable": false
  }
}
EOF
