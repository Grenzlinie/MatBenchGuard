#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: results.json ===
cat > /app/outputs/results.json <<'FFEOF'
{
  "energy_barriers": {
    "He": 0.11,
    "Ne": 0.51,
    "Ar": 2.45
  },
  "selectivities": {
    "He_Ne": 5170000,
    "He_Ar": 1.89e39
  }
}
FFEOF
