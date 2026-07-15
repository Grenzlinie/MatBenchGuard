#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: net_charges.json ===
cat > /app/outputs/net_charges.json <<'FFEOF'
{
  "tetrahedral_Li_charge": 0.76,
  "octahedral_Li_charge": 0.65
}
FFEOF
