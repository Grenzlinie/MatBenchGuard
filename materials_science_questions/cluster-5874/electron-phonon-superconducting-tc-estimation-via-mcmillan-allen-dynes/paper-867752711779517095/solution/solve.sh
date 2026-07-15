#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: derived_quantities.json ===
cat > /app/outputs/derived_quantities.json <<'FFEOF'
{
  "m_star": 0.312,
  "lambda_L_0": 11.8,
  "l_tr": 13.9,
  "xi_0": 1760.0,
  "xi_GL_0": 133.7,
  "lambda_GL_0": 81.7,
  "kappa_GL": 0.611
}
FFEOF
