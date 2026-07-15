#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: results.json ===
cat > /app/outputs/results.json <<'EOF'
{
  "grain_boundary_thickness": 1.0,
  "grain_boundary": {
    "f_liq_bond": 0.332,
    "f_liq_mol": 0.305,
    "f_NHBneq4": 0.013,
    "D": 5.0e-13
  },
  "triple_junction": {
    "f_liq_bond": 0.638,
    "f_liq_mol": 0.527,
    "f_NHBneq4": 0.032,
    "D": 1.7e-12
  },
  "ice_vapor_interface": {
    "f_liq_bond": 0.406,
    "f_liq_mol": 0.393,
    "f_NHBneq4": 0.111,
    "D": 3.4e-11
  }
}
EOF
