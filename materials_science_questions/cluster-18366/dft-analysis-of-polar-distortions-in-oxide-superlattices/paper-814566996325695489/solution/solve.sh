#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: step_01_strain_analysis.json ===
cat > /app/outputs/step_01_strain_analysis.json <<'EOF'
{
  "cubic": {
    "a_1-10": 7.241,
    "a_11-2": 6.271,
    "alpha": 90.0,
    "Delta_a_avg": 1.520,
    "Delta_alpha_avg": 0.0
  },
  "tetragonal": {
    "a_1-10": 7.199,
    "a_11-2": 6.218,
    "alpha": 90.5,
    "Delta_a_avg": 1.425,
    "Delta_alpha_avg": 0.5
  },
  "monoclinic": {
    "a_1-10": 5.000,
    "a_11-2": 8.000,
    "alpha": 85.0,
    "Delta_a_avg": 2.704,
    "Delta_alpha_avg": 5.0
  },
  "orthorhombic": {
    "a_1-10": 7.000,
    "a_11-2": 7.200,
    "alpha": 89.0,
    "Delta_a_avg": 1.804,
    "Delta_alpha_avg": 1.0,
    "a_minus211": 6.019,
    "a_1-21": 6.117
  }
}
EOF
