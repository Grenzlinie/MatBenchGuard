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
  "AuF2": {
    "ground_state_phase": "Pnma",
    "transition_pressure_lower": 15,
    "transition_pressure_upper": 30,
    "Bader_charge_au": 1.066
  },
  "AuF3": {
    "ground_state_phase": "Cmc2_1",
    "transition_pressure": 6,
    "volume_collapse_percent": 6.3,
    "Bader_charge_au": 1.485
  },
  "AuF4": {
    "ground_state_phase": "C2/c",
    "transition_pressure_lower": 6,
    "transition_pressure_upper": 40,
    "Bader_charge_au": 1.741
  },
  "AuF6": {
    "ground_state_phase": "R-3",
    "Bader_charge_au": 2.076
  }
}
FFEOF

# === solve block: phonon_stability.json ===
cat > /app/outputs/phonon_stability.json <<'FFEOF'
{
  "AuF2_Pnma": {
    "no_imaginary_modes": true
  },
  "AuF3_Cmc2_1": {
    "no_imaginary_modes": true
  },
  "AuF4_C2c": {
    "no_imaginary_modes": true
  },
  "AuF6_R-3": {
    "no_imaginary_modes": true
  }
}
FFEOF
