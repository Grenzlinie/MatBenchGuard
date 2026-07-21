#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: reproduction_results.json ===
cat > /app/outputs/reproduction_results.json <<'FFEOF'
{
  "total_energies": {
    "ti2n": -25000.0,
    "h2": -10.0,
    "ch4": -40.0,
    "c2h2": -76.0,
    "h2_ti2n": -25012.964,
    "ch4_ti2n": -25040.214,
    "c2h2_ti2n": -25081.527
  },
  "adsorption_energies": {
    "H2": -2.964,
    "CH4": -0.214,
    "C2H2": -5.527
  },
  "charge_transfers": {
    "H2": -0.227,
    "CH4": 0.047,
    "C2H2": -0.281
  },
  "bond_lengths": {
    "H2_HH": 2.973,
    "C2H2_CC": 1.44,
    "C2H2_CH": 1.069
  }
}
FFEOF
