#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: extracted_parameters.json ===
cat > /app/outputs/extracted_parameters.json <<'FFEOF'
{
  "bulk_soec": [183.3, 159.4, 44.3],
  "bulk_toec": [-998.8, -1487.3, 1505.1, -191.4, -5032.2, -200.0],
  "core_young_modulus_x": 140.80,
  "core_young_modulus_2nd_x": -827.7,
  "surface_young_modulus_x": 2.73,
  "surface_young_modulus_2nd_x": 4.11,
  "surface_eigenstress_x": 1.53,
  "Y_n_direct_3nm": 154.0,
  "Y_n_scaling_3nm": 154.0
}
FFEOF
