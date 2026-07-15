#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: superconducting_properties.json ===
cat > /app/outputs/superconducting_properties.json <<'FFEOF'
{
  "suspended": {
    "lambda": 0.62,
    "omega_log_cm-1": 316.8,
    "Tc_K": 10.33,
    "gap_meV": 1.56
  },
  "supported": {
    "lambda": 0.67,
    "omega_log_cm-1": 330.5,
    "Tc_K": 12.98,
    "gap_meV": 1.98
  }
}
FFEOF
