#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: computed_values.json ===
cat > "/app/outputs/computed_values.json" <<'FFEOF'
{
  "freon12_rc_cm": 2.79e-06,
  "freon12_W_keV": 0.184,
  "freon22_rc_cm": 1.53e-06,
  "freon22_W_keV": 0.049
}
FFEOF
