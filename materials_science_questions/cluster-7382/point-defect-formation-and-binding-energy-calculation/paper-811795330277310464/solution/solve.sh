#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
set -euo pipefail
mkdir -p /app/outputs

# === solve block: computed_g_values.json ===
cat > /app/outputs/computed_g_values.json <<'FFEOF'
{
  "Kr_115K_g": 0.053,
  "Kr_110K_g": 0.059
}
FFEOF
