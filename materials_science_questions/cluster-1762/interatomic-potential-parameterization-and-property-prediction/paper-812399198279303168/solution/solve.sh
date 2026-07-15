#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p "/app/outputs"

# === solve block: tensile_properties.csv ===
cat > "/app/outputs/tensile_properties.csv" <<'EOF'
Young_modulus_GPa,elongation_at_failure_percent,orientation,total_elongation_percent,ultimate_strength_GPa,work_of_deformation_GJm3,yield_strength_GPa
78,48,<100>,48,22.2,0.95,5.2
123,32,<110>,32,9.6,0.39,9.0
83,17,<111>,17,7.9,0.17,5.7
EOF
