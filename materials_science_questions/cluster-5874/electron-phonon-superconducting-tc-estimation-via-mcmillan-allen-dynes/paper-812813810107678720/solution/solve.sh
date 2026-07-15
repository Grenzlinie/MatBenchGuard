#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: epc_results.json ===
cat > '/app/outputs/epc_results.json' <<'JSONEOF'
{
  "0.2e_strain_0pct": {
    "lambda": 0.05,
    "omega_log_cm1": 1956.573,
    "Tc_K": 0
  },
  "0.2e_strain_5pct": {
    "lambda": 0.09,
    "omega_log_cm1": 1598.48,
    "Tc_K": 0
  },
  "Li_deposited": {
    "lambda": 0.86,
    "omega_log_cm1": 258.268,
    "Tc_K": 13.03
  }
}
JSONEOF
