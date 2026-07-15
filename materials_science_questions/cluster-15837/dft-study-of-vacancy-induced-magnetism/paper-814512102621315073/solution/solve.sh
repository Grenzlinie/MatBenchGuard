#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: step_01_pure_BN_properties.json ===
cat > /app/outputs/step_01_pure_BN_properties.json <<'FFEOF'
{
  "a": 3.621,
  "B0": 390,
  "E0": -5725.625
}
FFEOF

# === solve block: step_02_B09375V00625N_properties.json ===
cat > /app/outputs/step_02_B09375V00625N_properties.json <<'FFEOF'
{
  "a": 3.684,
  "B0": 374,
  "E0": -6012.056,
  "mag_moment": 2.0,
  "energy_FM": -6012.056,
  "energy_NM": -6012.0106,
  "minority_gap": 3.71,
  "local_moments": {
    "V": 1.61,
    "B": 0.028,
    "N": -0.011
  }
}
FFEOF

# === solve block: step_03_B0875V0125N_properties.json ===
cat > /app/outputs/step_03_B0875V0125N_properties.json <<'FFEOF'
{
  "a": 3.754,
  "B0": 378,
  "E0": -6298.807,
  "mag_moment": 4.0,
  "energy_FM": -6298.807,
  "energy_AFM": -6298.7288,
  "minority_gap": 3.2,
  "local_moments": {
    "V": 1.61,
    "B": 0.028,
    "N": -0.011
  }
}
FFEOF
