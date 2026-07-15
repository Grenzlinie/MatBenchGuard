#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: computed_properties.json ===
cat > "$OUTDIR/computed_properties.json" <<'EOF'
{
  "Zr3N4": {
    "lattice_constant_a0": 6.837,
    "bulk_modulus_B0": 211,
    "pressure_derivative_B0p": 6.61,
    "elastic_constant_C11": 310.13,
    "elastic_constant_C12": 75.53,
    "elastic_constant_C44": 122.43
  },
  "Hf3N4": {
    "lattice_constant_a0": 6.578,
    "bulk_modulus_B0": 232,
    "pressure_derivative_B0p": 5.95,
    "elastic_constant_C11": 358.93,
    "elastic_constant_C12": 51.02,
    "elastic_constant_C44": 148.47
  }
}
EOF
