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
  "C_values": {
    "1": 10.0,
    "2": -15.0,
    "3": -17.5,
    "4": -9.0,
    "6": 5.0,
    "24": 20.0
  }
}
FFEOF
