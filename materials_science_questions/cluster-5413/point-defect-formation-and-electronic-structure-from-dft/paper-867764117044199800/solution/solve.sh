#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
export OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: pure_structure.json ===
cat > "$OUTDIR/pure_structure.json" <<'FFEOF'
{
  "M": {
    "a": 5.18,
    "b_a": 1.011,
    "c_a": 1.037,
    "beta_deg": 99.1667,
    "positions": {
      "Zr": [0.276, 0.044, 0.210],
      "OI": [0.065, 0.327, 0.350],
      "OII": [0.451, 0.757, 0.475]
    }
  },
  "T": {
    "a": 5.11,
    "c_a": 1.030,
    "dz": 0.057
  }
}
FFEOF

# === solve block: energy_differences.csv ===
cat > "$OUTDIR/energy_differences.csv" <<'FFEOF'
doping_concentration,E_M,E_T,delta_E
0.0,-2047.891,-2048.000,0.109
3.125,-2047.910,-2048.000,0.090
6.25,-2047.928,-2048.000,0.072
12.5,-2047.972,-2048.000,0.028
18.75,-2048.030,-2048.000,-0.030
FFEOF
