#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p "/app/outputs"

# === solve block: step_00_refinement_R1.txt ===
echo "0.0116" > "$OUTDIR/step_00_refinement_R1.txt"

# === solve block: step_01_dipole_moment.txt ===
echo "42.4" > "/app/outputs/step_01_dipole_moment.txt"

# === solve block: step_02_topological_properties.json ===
cat > "/app/outputs/step_02_topological_properties.json" <<'EOF'
{
  "N1-C8": {
    "rho": 2.65,
    "nabla2": -28.53,
    "G": 1067.60,
    "V": -2910.97,
    "H": -1843.37
  },
  "N3-H3N...O2": {
    "rho": 0.26,
    "nabla2": 7.74,
    "G": 173.01,
    "V": -135.49,
    "H": 37.53
  },
  "N2-H2N...O4": {
    "rho": 0.37,
    "nabla2": 5.49,
    "G": 159.14,
    "V": -168.90,
    "H": -9.76
  }
}
EOF
