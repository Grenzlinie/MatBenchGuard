#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: thermal_properties.json ===
cat > /app/outputs/thermal_properties.json <<'EOF'
{
  "kappa_armchair": 218.0,
  "kappa_zigzag": 285.0,
  "Lambda_armchair": 74.9,
  "Lambda_zigzag": 94.3
}
EOF

# === solve block: mechanical_properties.json ===
cat > /app/outputs/mechanical_properties.json <<'EOF'
{
  "modulus_armchair": 870.0,
  "modulus_zigzag": 800.0,
  "strength_armchair": 85.0,
  "strength_zigzag": 85.0
}
EOF
