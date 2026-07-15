#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: theoretical_data.json ===
cat > /app/outputs/theoretical_data.json <<'FFEOF'
{
  "CH4": {
    "u_prime": -1.68,
    "v": 3.39e12,
    "f_plus": 2.21,
    "f_rot": 27.6,
    "f_trans_prime": 1.3e26
  },
  "CF4": {
    "u_prime": 3.30,
    "v": 2.29e12,
    "f_plus": 13.0,
    "f_rot": 5720,
    "f_trans_prime": 34.0e26
  }
}
FFEOF
