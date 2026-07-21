#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: equilibrium_constants.json ===
cat > /app/outputs/equilibrium_constants.json <<'FFEOF'
{
  "energy_difference_subsurface_surface_ev": 2.5,
  "keq_table": [
    {"doping": "none", "Keq": 0.15, "delta_G_kJmol": 14.2},
    {"doping": "Ni", "Keq": 0.56, "delta_G_kJmol": 4.3},
    {"doping": "Zn", "Keq": 2.79, "delta_G_kJmol": -7.7},
    {"doping": "Co", "Keq": 21.80, "delta_G_kJmol": -23.1}
  ]
}
FFEOF
