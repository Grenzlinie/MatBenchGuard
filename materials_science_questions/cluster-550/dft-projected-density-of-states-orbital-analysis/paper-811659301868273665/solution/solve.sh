#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: step_01_magnetic_ground_state.json ===
cat > /app/outputs/step_01_magnetic_ground_state.json <<'FFEOF'
{
  "NM": {"delta_E": 0.34, "MM": null},
  "FM": {"delta_E": 0.21, "MM": 1.03},
  "AFM1": {"delta_E": 0.25, "MM": [1.77, 1.82]},
  "AFM2": {"delta_E": 0.24, "MM": 0.97},
  "AFM3": {"delta_E": 0.0, "MM": 2.05}
}
FFEOF

# === solve block: step_02_elastic_constants.json ===
cat > /app/outputs/step_02_elastic_constants.json <<'FFEOF'
{
  "C11": 168,
  "C12": 21,
  "C13": 49,
  "C33": 176,
  "C44": 122,
  "C66": 86
}
FFEOF

# === solve block: step_03_bader_charges.json ===
cat > /app/outputs/step_03_bader_charges.json <<'FFEOF'
{
  "Th": 1.557,
  "Cr": 0.399,
  "Si": -1.178
}
FFEOF
