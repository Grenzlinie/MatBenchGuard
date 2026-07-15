#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: phonon_analysis_results.json ===
cat > "/app/outputs/phonon_analysis_results.json" <<'FFEOF'
{
  "gamma_modes": {
    "Zr": ["A2u","Eu","B1g","E_g"],
    "O": ["A1g","B1g","E_g","E_g","A2u","B2u","Eu","Eu"]
  },
  "M_modes": {
    "Zr": ["M1","M2","M3"],
    "O": ["M1","M2","M2","M3","M4","M4"]
  },
  "primary_order_parameter": "M1+M2",
  "secondary_parameter": "E_g",
  "coupling_terms": [
    "δ1 * (φ1^2 + φ2^2 + ψ1^2 + ψ2^2) * (e1 + e2)",
    "δ2 * (φ1^2 + φ2^2 + ψ1^2 + ψ2^2) * e3",
    "γ * (φ1^2 + φ2^2 + ψ1^2 + ψ2^2) * (e4^2 + e5^2)"
  ]
}
FFEOF
