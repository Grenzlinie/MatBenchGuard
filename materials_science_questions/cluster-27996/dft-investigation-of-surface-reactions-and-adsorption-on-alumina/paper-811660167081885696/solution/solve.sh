#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: dft_adsorption_energies.json ===
cat > "$OUTDIR/dft_adsorption_energies.json" << 'EOF'
{
  "CH3OH": 13.4,
  "CH3O": 52.8,
  "CH2OH": 49.8,
  "CH2O": 23.0,
  "CHOH": 78.1,
  "CHO": 60.8,
  "COH": 106.8,
  "CO": 46.5,
  "H": 61.5,
  "H2": 7.7
}
EOF

# === solve block: microkinetic_results.json ===
python3 /solution/generate_microkinetic.py > /app/outputs/microkinetic_results.json
