#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: step_01_goodness_of_fit.json ===
# Write the paper-reported goodness-of-fit values
cat > /app/outputs/step_01_goodness_of_fit.json <<'EOF'
{
  "Ca2Mn3O8": [1.16, 1.13, 0.81],
  "CaMn2O4": [2.77, 2.65, 2.61]
}
EOF
