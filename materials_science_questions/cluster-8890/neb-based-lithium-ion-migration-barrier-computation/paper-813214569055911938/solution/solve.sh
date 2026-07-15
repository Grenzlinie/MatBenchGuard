#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: results.json ===
cat > /app/outputs/results.json << 'EOF'
{
  "frenkel_formation_energies": {
    "type1_to_type2": 0.53,
    "type1_to_type3": 1.07,
    "type1_to_type4": 1.29,
    "tetrahedral_minimum": 0.60
  },
  "interstitial_migration_barriers": {
    "minimum_path_type3_intermediate": 0.75,
    "direct_type2_to_type2": 0.89
  },
  "vacancy_migration_barriers": {
    "octahedral_type1_along_a": 0.58,
    "octahedral_type1_along_c": 1.01,
    "tetrahedral_minimum": 0.17,
    "octahedral_to_tetrahedral_minimum": 0.21,
    "continuous_1d_barrier": 0.30,
    "inter_channel_barrier": 0.33
  },
  "activation_energies": {
    "vacancy_EA": 0.60,
    "interstitial_EA": 1.02
  },
  "dominant_mechanism": "vacancy"
}
EOF
