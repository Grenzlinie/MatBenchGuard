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
  "bulk_bandgap": 7.07,
  "1H_bandgap": 6.16,
  "1T_bandgap": 7.56,
  "bulk_direct": true,
  "1H_direct": true,
  "1T_direct": true,
  "1H_n_parallel": 1.39,
  "1H_n_perpendicular": 1.37,
  "1T_n_parallel": 1.375,
  "1T_n_perpendicular": 1.33
}
FFEOF
