#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: band_gaps.json ===
cat > /app/outputs/band_gaps.json <<'FFEOF'
{
  "ideal_wurtzite": 3.22,
  "wurtzite_vacancy": 2.91,
  "ideal_rocksalt": 3.25,
  "rocksalt_vacancy": 1.73
}
FFEOF
