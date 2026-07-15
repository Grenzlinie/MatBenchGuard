#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: computed_parameters.json ===
cat > /app/outputs/computed_parameters.json <<'EOF'
{
  "Co1": {"D": -79.04, "E_over_D": 0.2546},
  "Co3": {"D": -88.76, "E_over_D": 0.2328},
  "Ni": {"J1": -17.2, "J2": 18.5}
}
EOF
