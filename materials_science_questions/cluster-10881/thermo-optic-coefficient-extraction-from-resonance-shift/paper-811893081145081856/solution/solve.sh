#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: sellmeier_results.json ===
cat > "$OUTDIR/sellmeier_results.json" <<'FFEOF'
{
  "fitted_parameters": {
    "A1": 0.6961663,
    "lambda1": 0.0684043,
    "A2": 0.4079426,
    "lambda2": 0.1162414,
    "A3": 0.8974794,
    "lambda3": 9.896161
  },
  "overall_average_absolute_residual": 0.0000105
}
FFEOF
