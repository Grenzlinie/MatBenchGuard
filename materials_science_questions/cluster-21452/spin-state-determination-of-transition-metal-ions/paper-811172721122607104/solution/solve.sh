#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
set -euo pipefail
mkdir -p /app/outputs

# === solve block: hyperfine_constants.json ===
cat > /app/outputs/hyperfine_constants.json <<'FFEOF'
{
  "A_s": 33.82,
  "A_p": 7.82
}
FFEOF
