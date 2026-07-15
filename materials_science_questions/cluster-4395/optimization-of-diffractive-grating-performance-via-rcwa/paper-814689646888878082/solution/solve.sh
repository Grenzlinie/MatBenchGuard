#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: tuning_ranges.json ===
cat > /app/outputs/tuning_ranges.json <<'FFEOF'
{
  "tuning_range_94GHz": 3.0,
  "tuning_range_220GHz": 7.0
}
FFEOF
