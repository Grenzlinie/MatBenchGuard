#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: results.json ===
cat > "$OUTDIR/results.json" <<'EOF'
{
  "adsorption_energies": {
    "CO": 0.78,
    "O2": 0.59,
    "O": 3.88,
    "CO2": 0.24
  },
  "bond_lengths": {
    "CO_C-O": 1.15,
    "O2_O-O": 1.39,
    "CO2_C-O": 1.17
  },
  "barrier_CO_O": 0.48
}
EOF
