#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: exchange_couplings.json ===
# exchange_couplings.json: json (scored)
cat > /app/outputs/exchange_couplings.json <<'FFEOF'
{
  "J1": 16.35,
  "J2": 12.14,
  "J3": 0.60,
  "J4": 0.35,
  "J5": -1.15,
  "J6": -1.85,
  "J7_less": -2.58,
  "J7_greater": -4.19,
  "J8_less": -0.94,
  "J8_greater": -2.44
}
FFEOF
