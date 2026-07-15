#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: mulliken_charges.json ===
  cat > /app/outputs/mulliken_charges.json <<'FFEOF'
{
  "charge_C": -0.93,
  "charge_Si": -0.83,
  "unit": "e"
}
FFEOF
