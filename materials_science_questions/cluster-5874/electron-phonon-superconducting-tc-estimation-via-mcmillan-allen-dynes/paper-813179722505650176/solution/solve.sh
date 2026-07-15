#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: tc_results.json ===
cat <<'EOF' > /app/outputs/tc_results.json
[
  {
    "structure": "A15",
    "lambda": 1.82,
    "omega_log": 989.0,
    "Tc_at_mu_0.13": 140.0
  },
  {
    "structure": "P4_2/mmc",
    "lambda": 1.56,
    "omega_log": 737.0,
    "Tc_at_mu_0.13": 90.0
  },
  {
    "structure": "Cccm",
    "lambda": 1.60,
    "omega_log": 793.0,
    "Tc_at_mu_0.13": 100.0
  }
]
EOF
