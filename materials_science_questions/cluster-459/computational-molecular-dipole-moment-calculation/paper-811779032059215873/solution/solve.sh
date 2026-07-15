#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: dipole_moments.json ===
cat > /app/outputs/dipole_moments.json <<'EOF'
{
  "mu_g": 2.56,
  "mu_e": 6.09,
  "delta_mu": 3.53,
  "mu_e_tddft": 4.78
}
EOF
