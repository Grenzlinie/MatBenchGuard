#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: optimized_lattice_constants.json ===
cat > /app/outputs/optimized_lattice_constants.json <<'FFEOF'
{
  "pure_TCNE": 9.98,
  "K_TCNE3": 9.96,
  "Na_TCNE3": 9.93
}
FFEOF

# === solve block: metallicity.json ===
cat > /app/outputs/metallicity.json <<'FFEOF'
{
  "pure_TCNE": false,
  "K_TCNE3": true,
  "Na_TCNE3": true
}
FFEOF
