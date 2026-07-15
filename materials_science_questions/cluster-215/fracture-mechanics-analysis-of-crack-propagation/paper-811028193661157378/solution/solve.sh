#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: singularity_orders.json ===
cat > "$OUTDIR/singularity_orders.json" <<'FFEOF'
{
  "lambda_A": 0.4788,
  "lambda_B": 0.4113
}
FFEOF
