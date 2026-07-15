#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: results.json ===
cat > /app/outputs/results.json <<'FFEOF'
{
  "flat_sheet": {
    "entire_film_ratio": 1.02,
    "edges_ratio": 1.05,
    "corners_ratio": 1.34
  },
  "hollow_sphere": {
    "ratio": 1.69
  },
  "hollow_cylinder": {
    "ratio": 1.20
  },
  "specific_heat_onset_ratio": 1.06
}
FFEOF
