#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs
OUTDIR=/app/outputs

# === solve block: model_predictions.json ===
# model_predictions.json
cat > "$OUTDIR/model_predictions.json" <<'FFEOF'
{
  "theta_g2": -0.58398,
  "H2_over_dHm_predicted": 0.105,
  "H1_over_dHm_predicted": 0.0925,
  "experimental_mean_H2_over_dHm": 0.11,
  "experimental_mean_H1_over_dHm": 0.0932,
  "agreement_statement": "The predicted values (H2/\u0394Hm=0.105, H1/\u0394Hm=0.0925) agree with the experimental mean values (0.11 and 0.0932)."
}
FFEOF

# === solve block: residual_entropy.json ===
# residual_entropy.json
cat > "$OUTDIR/residual_entropy.json" <<'FFEOF'
{
  "S_Rg": 1.114,
  "S_m": 4.72,
  "S_Rg_over_S_m": 0.236
}
FFEOF
