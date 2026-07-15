#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: elastic_constants.json ===
cat > /app/outputs/elastic_constants.json <<'EOF'
{
  "a0": 5.626,
  "C11": 117,
  "C12": 57,
  "C44": 58,
  "C111": -691,
  "C112": -407,
  "C123": -67,
  "C144": 3,
  "C155": -280,
  "C456": -24
}
EOF

# === solve block: gsfe_fit_params.json ===
cat > /app/outputs/gsfe_fit_params.json <<'EOF'
{
  "relaxed": {
    "gamma": 0.14,
    "Delta1": -0.71,
    "Delta2": 0.27
  },
  "nonrelaxed": {
    "gamma": 0.14,
    "Delta1": -0.34,
    "Delta2": 0.15
  }
}
EOF

# === solve block: dislocation_properties.json ===
cat > /app/outputs/dislocation_properties.json <<'EOF'
{
  "relaxed_xi0": 0.16,
  "relaxed_xi": 0.22,
  "relaxed_sigmaP0": 8.11,
  "relaxed_sigmaP": 4.29,
  "nonrelaxed_xi": 0.17,
  "nonrelaxed_sigmaP": 9.79
}
EOF
