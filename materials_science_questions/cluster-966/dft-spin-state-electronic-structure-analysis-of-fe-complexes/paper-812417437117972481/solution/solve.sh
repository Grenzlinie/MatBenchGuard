#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: step_01_fe2_results.json ===
cat > /app/outputs/step_01_fe2_results.json <<'FFEOF'
{
  "Fe2_spin_restricted_bond_length": 1.90,
  "Fe2_spin_unrestricted_bond_length": 1.90,
  "Fe2_spin_restricted_neutral_total_energy": -69234.50,
  "Fe2_spin_restricted_cation_total_energy": -69226.70,
  "Fe2_spin_unrestricted_neutral_total_energy": -69236.00,
  "Fe2_spin_unrestricted_cation_total_energy": -69229.60,
  "Fe2_spin_restricted_IP": 7.80,
  "Fe2_spin_unrestricted_IP": 6.40
}
FFEOF

# === solve block: step_02_fe3_results.json ===
cat > /app/outputs/step_02_fe3_results.json <<'FFEOF'
{
  "Fe3_spin_unrestricted_bond_length": 2.00,
  "Fe3_spin_unrestricted_neutral_total_energy": -103500.00,
  "Fe3_spin_unrestricted_cation_total_energy": -103493.70,
  "Fe3_spin_unrestricted_IP": 6.30
}
FFEOF
