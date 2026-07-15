#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: derived_quantities.json ===
cat > /app/outputs/derived_quantities.json <<'FFEOF'
{
  "k2_at_723K": 2000000,
  "k8_at_723K": 500,
  "E2_inf": 25.0,
  "E8_inf": 35.6,
  "delta_Hf_EtSiH": 47.7,
  "group_additivity_C_H2_C_Si": -1.3
}
FFEOF
