#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
set -euo pipefail
mkdir -p /app/outputs

# === solve block: structural_properties.json ===
cat > /app/outputs/structural_properties.json <<'EOF'
[
  {"compound": "c-BN", "lattice_constant_A": 3.621, "bulk_modulus_GPa": 390, "total_energy_eV": -5725.625},
  {"compound": "B0.9375V0.0625N", "lattice_constant_A": 3.684, "bulk_modulus_GPa": 374, "total_energy_eV": -6012.056},
  {"compound": "B0.875V0.125N", "lattice_constant_A": 3.754, "bulk_modulus_GPa": 378, "total_energy_eV": -6298.807}
]
EOF

# === solve block: band_gaps.json ===
cat > /app/outputs/band_gaps.json <<'EOF'
{"B0.9375V0.0625N": 3.71, "B0.875V0.125N": 3.2}
EOF

# === solve block: magnetic_moments.json ===
cat > /app/outputs/magnetic_moments.json <<'EOF'
{"B0.9375V0.0625N": 2.0, "B0.875V0.125N": 4.0}
EOF
