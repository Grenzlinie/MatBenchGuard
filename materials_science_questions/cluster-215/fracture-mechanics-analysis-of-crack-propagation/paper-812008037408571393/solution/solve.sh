#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: critical_location_criterion.json ===
cat > /app/outputs/critical_location_criterion.json <<'FFEOF'
{
  "a": 3.29,
  "b": -1.54,
  "c": 0.10
}
FFEOF

# === solve block: section_average_criterion.json ===
cat > /app/outputs/section_average_criterion.json <<'FFEOF'
{
  "a": 3.41,
  "b": -2.23,
  "c": 0.22
}
FFEOF

# === solve block: burst_pressure_predictions.csv ===
cat > /app/outputs/burst_pressure_predictions.csv <<'FFEOF'
pipe_no,predicted_burst_pressure_MPa
MNA,24.16
MNB,21.58
FFEOF
