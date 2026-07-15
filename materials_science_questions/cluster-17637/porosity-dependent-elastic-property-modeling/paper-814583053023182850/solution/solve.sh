#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
set -euo pipefail
mkdir -p "/app/outputs"

# === solve block: results.json ===
cat > "/app/outputs/results.json" <<'FFEOF'
{
  "type1_effective_modulus_GPa": 91,
  "type1_ultimate_strain_percent": 0.13,
  "type2_effective_modulus_GPa": 76,
  "type2_ultimate_strain_percent": 0.15,
  "type2_damage_bone_fraction": 0.70,
  "type2_damage_matrix_fraction": 0.40
}
FFEOF
