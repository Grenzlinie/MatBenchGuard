#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: step_02_electronic_properties.json ===
cat > /app/outputs/step_02_electronic_properties.json <<'FFEOF'
{
  "N_EF": 1.35,
  "gamma": 3.18
}
FFEOF
