#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: optimized_liquid_parameters.json ===
cat > /app/outputs/optimized_liquid_parameters.json <<'FFEOF'
{
  "FeO-Nd2O3": {
    "delta_g0": -1966
  },
  "Fe2O3-Nd2O3": {
    "delta_g0": -38723
  },
  "B2O3-Nd2O3": {
    "delta_g0": -101002,
    "delta_g0_T": 27.614,
    "g_Nd3+Nd3+_1": -31380,
    "g_B3+B3+_1": 18200,
    "g_B3+B3+_3": 20920,
    "g_B3+B3+_5": 3766
  },
  "FeO-B2O3": {
    "delta_g0": -29288,
    "delta_g0_T": 8.368,
    "g_Fe2+Fe2+_1": 35564,
    "g_Fe2+Fe2+_3": 62764,
    "g_B3+B3+_1": 9205,
    "g_B3+B3+_1_T": 8.368,
    "g_B3+B3+_6": 58576,
    "g_B3+B3+_6_T": 33.472
  }
}
FFEOF

# === solve block: feo_nd2o3_phase_diagram.csv ===
python3 /solution/generate_phase_diagram.py
