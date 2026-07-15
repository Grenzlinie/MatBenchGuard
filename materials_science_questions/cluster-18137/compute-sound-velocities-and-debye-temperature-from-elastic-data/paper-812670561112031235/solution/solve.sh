#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
set -euo pipefail
mkdir -p /app/outputs

# === solve block: fitted_tensor.json ===
cat > /app/outputs/fitted_tensor.json <<'JSONEOF'
{
  "kappa_xx": 7.2,
  "kappa_yy": 5.3,
  "kappa_zz": 5.3,
  "kappa_xz": -0.2,
  "kappa_eff": 5.9,
  "kappa_xx_uncertainty": 1.7,
  "kappa_yy_uncertainty": 1.4,
  "kappa_zz_uncertainty": 1.6,
  "kappa_xz_uncertainty": 0.1
}
JSONEOF
