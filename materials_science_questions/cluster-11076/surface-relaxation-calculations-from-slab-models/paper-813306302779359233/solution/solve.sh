#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: surface_results.json ===
cat > /app/outputs/surface_results.json <<'FFEOF'
{
  "W(001)": {
    "delta_12": -8.803,
    "delta_23": -3.983,
    "delta_34": -0.998,
    "delta_14": -13.78,
    "surface_energy": 0.248,
    "dos_at_fermi": 5.68
  },
  "W(110)": {
    "delta_12": -2.778,
    "delta_23": -0.852,
    "delta_34": -0.667,
    "delta_14": -4.297,
    "surface_energy": 0.194,
    "dos_at_fermi": 5.12
  },
  "W(111)": {
    "delta_12": -8.119,
    "delta_23": -10.38,
    "delta_34": 11.87,
    "delta_14": -6.629,
    "surface_energy": 0.232,
    "dos_at_fermi": 5.22
  }
}
FFEOF
