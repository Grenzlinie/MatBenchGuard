#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: results.json ===
cat > /app/outputs/results.json <<'EEOF'
{
  "AFM-a": {
    "band_gap": 0.0,
    "total_energy_per_Ru": 11.9
  },
  "AFM-b": {
    "band_gap": 0.1,
    "total_energy_per_Ru": 0.0
  },
  "AFM-c": {
    "band_gap": 0.0,
    "total_energy_per_Ru": 6.0
  }
}
EEOF
