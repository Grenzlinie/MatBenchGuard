#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: lambda_values.json ===
cat > /app/outputs/lambda_values.json <<'FFEOF'
[
  {"material": "MgB2", "lambda": 0.59},
  {"material": "NbB2", "lambda": 0.43}
]
FFEOF

# === solve block: tc_values.json ===
cat > /app/outputs/tc_values.json <<'FFEOF'
[
  {"material": "MgB2", "mu_star": 0.10, "Tc": 23.0},
  {"material": "NbB2", "mu_star": 0.10, "Tc": 4.0}
]
FFEOF
