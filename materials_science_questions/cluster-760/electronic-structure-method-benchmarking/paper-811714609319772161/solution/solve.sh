#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: energies.json ===
cat > /app/outputs/energies.json <<'FFEOF'
{
  "201": {
    "electronic_energy": -175.000000000,
    "zpe": 0.020000000
  },
  "202": {
    "electronic_energy": -174.996701000,
    "zpe": 0.020000000
  },
  "Ts02_03": {
    "electronic_energy": -174.965910000,
    "zpe": 0.020000000
  }
}
FFEOF
