#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: elastic_constants.json ===
cat > /app/outputs/elastic_constants.json <<'FFEOF'
{
  "SrLiH3": {
    "C11": 108.775,
    "C12": 10.520,
    "C44": 44.542
  },
  "SrPdH3": {
    "C11": 122.497,
    "C12": 64.361,
    "C44": 41.629
  }
}
FFEOF
