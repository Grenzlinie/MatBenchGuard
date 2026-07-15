#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: lattice_sums.json ===
cat > /app/outputs/lattice_sums.json <<'FFEOF'
{
  "alpha11": -1.428,
  "alpha33": -1.518,
  "EI_coefficient": 0.104,
  "madelung_constant": 4.374
}
FFEOF
