#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: raman_active_frequencies.json ===
cat > /app/outputs/raman_active_frequencies.json <<'FFEOF'
{
  "T2g_frequency": 417.63,
  "A1g_frequency": 1394.02,
  "Eg_frequency": 1504.15,
  "unit": "cm^-1"
}
FFEOF

# === solve block: thermal_conductivity_300K.json ===
cat > /app/outputs/thermal_conductivity_300K.json <<'FFEOF'
{
  "thermal_conductivity_300K": {
    "value": 266.17,
    "unit": "W/mK"
  }
}
FFEOF
