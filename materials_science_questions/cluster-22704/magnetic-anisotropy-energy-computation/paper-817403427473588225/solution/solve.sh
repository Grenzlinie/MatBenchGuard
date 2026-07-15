#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: bulk_results.json ===
# Write bulk_results.json
cat > /app/outputs/bulk_results.json <<'FFEOF'
{
  "a_type_II": 8.250,
  "c_over_a_type_II": 1.077,
  "delta_E_type_I": 0.03,
  "delta_E_type_III": 0.05,
  "delta_E_type_IV": 0.14,
  "delta_E_normal": 0.61
}
FFEOF

# === solve block: mae_results.json ===
# Write mae_results.json
cat > /app/outputs/mae_results.json <<'FFEOF'
{
  "bulk_CuFe2O4_MAE": 0.12,
  "FeO_int_one_unit_CuFe2O4_MgO_MAE": 0.32,
  "FeO_int_two_unit_CuFe2O4_MgO_MAE": 0.24,
  "CuO_int_one_unit_CuFe2O4_MgO_MAE": 0.05,
  "FeO_int_one_unit_Fe3O4_MgO_MAE": 0.23,
  "FeO_int_two_unit_Fe3O4_MgO_MAE": -0.14
}
FFEOF
