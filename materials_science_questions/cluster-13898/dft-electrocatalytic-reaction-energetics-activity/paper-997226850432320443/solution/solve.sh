#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: dft_results.json ===
cat > "$OUTDIR/dft_results.json" <<'EOF'
{
  "Ni(OH)2": {
    "U0": {
      "G1": 0.90,
      "G2": 1.70,
      "G3": 3.05,
      "G4": -0.73
    },
    "U123": {
      "G1": -0.33,
      "G2": 0.47,
      "G3": 1.82,
      "G4": -1.96
    }
  },
  "doped": {
    "U0": {
      "G1": 0.60,
      "G2": 1.20,
      "G3": 2.55,
      "G4": 0.57
    },
    "U123": {
      "G1": -0.63,
      "G2": -0.03,
      "G3": 1.32,
      "G4": -0.66
    }
  },
  "Cl_adsorption_difference": 0.30
}
EOF
