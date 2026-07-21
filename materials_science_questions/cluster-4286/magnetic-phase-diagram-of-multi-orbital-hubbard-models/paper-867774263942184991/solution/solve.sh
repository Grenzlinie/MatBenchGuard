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
  "critical_rho_d_ferromagnetic": 0.131,
  "diagonal_sequence": [
    {"rho_d": 0.0, "configuration": "F"},
    {"rho_d": 0.5, "configuration": "D1"},
    {"rho_d": 0.6667, "configuration": "D2"},
    {"rho_d": 1.0, "configuration": "D3"},
    {"rho_d": 1.3333, "configuration": "D4"},
    {"rho_d": 1.5, "configuration": "D5"},
    {"rho_d": 2.0, "configuration": "E"}
  ]
}
FFEOF
