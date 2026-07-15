#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: dft_energies.json ===
cat > /app/outputs/dft_energies.json <<'EOF'
{
  "NiAl": {
    "cohesive_energy": -6.16,
    "formation_enthalpy": -0.66
  },
  "NiAlTi1": {
    "cohesive_energy": -6.15,
    "formation_enthalpy": -0.65
  },
  "NiAlTi2": {
    "cohesive_energy": -6.13,
    "formation_enthalpy": -0.63
  },
  "NiAlTi3": {
    "cohesive_energy": -6.11,
    "formation_enthalpy": -0.62
  }
}
EOF
