#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: derived_volume_derivatives.json ===
cat > "$OUTDIR/derived_volume_derivatives.json" <<'EOF'
{
  "dln_lambda_dlnV": -5.4,
  "gamma_e_plus": -0.15,
  "dln_muplus_dlnV": -0.3,
  "dln_eta_dlnV": -9.4,
  "dln_I2_dlnV": -9.25
}
EOF
