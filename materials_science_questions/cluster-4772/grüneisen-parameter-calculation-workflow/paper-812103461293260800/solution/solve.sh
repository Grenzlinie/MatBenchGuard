#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: final_results.json ===
cat > /app/outputs/final_results.json <<'EOF'
{
  "Theta_a": 368,
  "Theta_c": 440,
  "chi_a": 7.42e-12,
  "chi_c": 4.53e-12,
  "S_A": 1.16e-11,
  "S_AC": -0.42e-11,
  "S_C": 1.29e-11,
  "gamma_a": 0.47,
  "gamma_c": 0.54
}
EOF
