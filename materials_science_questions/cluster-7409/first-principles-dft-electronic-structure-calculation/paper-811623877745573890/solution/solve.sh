#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: band_gaps.json ===
cat > /app/outputs/band_gaps.json <<'FFEOF'
{
  "CsTaWO6_undoped": 3.8,
  "CsTaWO6_doped": 2.3,
  "CsCa2Ta3O10_undoped": 2.1,
  "CsCa2Ta3O10_doped": 1.6,
  "Ba4Ta4O15_undoped": 4.0,
  "Ba4Ta4O15_doped": 2.0
}
FFEOF
