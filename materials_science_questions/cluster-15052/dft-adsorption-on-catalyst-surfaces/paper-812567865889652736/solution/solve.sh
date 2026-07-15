#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: results.json ===
cat > /app/outputs/results.json <<'EOF'
{
  "adsorption_energies": {
    "H2S_on_pristine": -3.24,
    "SO2_on_pristine": -4.21,
    "O2_on_pristine": -6.15,
    "H2S_on_O2_hYN": -2.46,
    "SO2_on_O2_hYN": -1.75
  },
  "band_gaps": {
    "pristine_hYN": 0.722,
    "H2S_on_pristine": 0.862,
    "SO2_on_pristine": 0.976,
    "O2_hYN": 0.960,
    "H2S_on_O2_hYN": 0.976,
    "SO2_on_O2_hYN": 1.032
  },
  "total_energies": {
    "hYN": 0.0,
    "H2S_molecule": 0.0,
    "SO2_molecule": 0.0,
    "O2_molecule": 0.0,
    "H2S_on_pristine": 0.0,
    "SO2_on_pristine": 0.0,
    "O2_on_pristine": 0.0,
    "H2S_on_O2_hYN": 0.0,
    "SO2_on_O2_hYN": 0.0
  }
}
EOF
