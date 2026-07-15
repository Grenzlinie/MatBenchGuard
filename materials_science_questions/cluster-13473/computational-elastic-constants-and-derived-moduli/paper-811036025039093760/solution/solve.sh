#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: step_stiffness_results.json ===
cat > "$OUTDIR/step_stiffness_results.json" <<'FFEOF'
[
  {
    "composition": "Al-87.4at.%Si",
    "temperature_K": 1570,
    "orientation": "[1̅10]",
    "stiffness_J_per_m": 1.78e-11,
    "stiffness_uncertainty_J_per_m": 0.12e-11
  },
  {
    "composition": "Al-87.4at.%Si",
    "temperature_K": 1570,
    "orientation": "[11̅2]",
    "stiffness_J_per_m": 1.67e-11,
    "stiffness_uncertainty_J_per_m": 0.11e-11
  },
  {
    "composition": "Al-59.4at.%Si",
    "temperature_K": 1230,
    "orientation": "[1̅10]",
    "stiffness_J_per_m": 2.61e-11,
    "stiffness_uncertainty_J_per_m": 0.13e-11
  },
  {
    "composition": "Al-59.4at.%Si",
    "temperature_K": 1230,
    "orientation": "[11̅2]",
    "stiffness_J_per_m": 2.60e-11,
    "stiffness_uncertainty_J_per_m": 0.16e-11
  }
]
FFEOF
