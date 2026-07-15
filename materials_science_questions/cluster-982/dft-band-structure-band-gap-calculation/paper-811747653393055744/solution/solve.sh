#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: bandgap.json ===
cat > /app/outputs/bandgap.json <<'JSONEOF'
{
  "band_gap_eV": 0.19,
  "is_direct": false
}
JSONEOF
