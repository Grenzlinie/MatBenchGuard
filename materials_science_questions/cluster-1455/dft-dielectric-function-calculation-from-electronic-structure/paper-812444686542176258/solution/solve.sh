#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: dielectric_parameters.json ===
cat > /app/outputs/dielectric_parameters.json <<'EOF'
{
  "ε0": 4.9,
  "ε∞": 2.2,
  "Vdε0_dV": 14.1,
  "Vdε∞_dV": -0.96,
  "γ_TO": 2.41,
  "γ_LO": 1.05
}
EOF
