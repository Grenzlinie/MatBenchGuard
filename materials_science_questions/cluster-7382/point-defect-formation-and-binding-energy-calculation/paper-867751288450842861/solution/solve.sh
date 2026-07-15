#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: energy_differences.json ===
cat > "/app/outputs/energy_differences.json" <<'FFEOF'
{
  "K_12.5": 15.0,
  "K_25": 51.0,
  "La_12.5": 34.0,
  "La_25": 64.0
}
FFEOF

# === solve block: curie_temperatures.json ===
cat > "/app/outputs/curie_temperatures.json" <<'FFEOF'
{
  "K_25": 327,
  "La_25": 453
}
FFEOF

# === solve block: doped_band_gaps.json ===
cat > "/app/outputs/doped_band_gaps.json" <<'FFEOF'
{
  "K_12.5": {
    "band_gap": 1.0,
    "fermi_level_type": "valence_band"
  },
  "La_12.5": {
    "band_gap": 1.0,
    "fermi_level_type": "conduction_band"
  }
}
FFEOF
