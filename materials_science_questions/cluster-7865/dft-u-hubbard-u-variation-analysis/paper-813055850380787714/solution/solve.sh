#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: results.json ===
cat > /app/outputs/results.json << 'FFEOF'
{
  "sheet": {
    "delta_E_meV": 526.8,
    "magnetic_moments": {
      "N1": 0.4,
      "N2": 0.15,
      "N3": 0.15
    }
  },
  "nanotube": {
    "delta_E_meV": 10.2,
    "magnetic_moments": {
      "N1": 0.4,
      "N2": 0.15,
      "N3": 0.15
    }
  }
}
FFEOF

# === solve finalize ===
echo "Reference results.json written."
