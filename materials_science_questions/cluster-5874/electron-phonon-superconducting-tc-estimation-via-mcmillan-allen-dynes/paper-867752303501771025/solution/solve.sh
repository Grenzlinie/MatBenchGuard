#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: sc_results.json ===
cat > /app/outputs/sc_results.json <<'FFEOF'
{
  "lambda": 0.68,
  "w_log": 78.9,
  "tc": 2.0
}
FFEOF
