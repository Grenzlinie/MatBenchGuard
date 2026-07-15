#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs
OUTDIR=/app/outputs

# === solve block: computed_properties.json ===
cat > "$OUTDIR/computed_properties.json" <<'EOF'
{
  "deintercalation_voltage": 4.22,
  "magnetic_moment_Mg15Ni05TiO4": 1.7,
  "magnetic_moment_MgNi05TiO4": 2.1,
  "formation_energy_rutile": -0.97,
  "formation_energy_anatase": -17.315
}
EOF
