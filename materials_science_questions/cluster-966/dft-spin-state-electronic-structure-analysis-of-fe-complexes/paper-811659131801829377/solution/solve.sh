#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: free_ligand_spin_densities.csv ===
cat > /app/outputs/free_ligand_spin_densities.csv <<'FFEOF'
ligand,geometry,bridgehead_spin_density_e,sulfur_spin_density_e
pdt,relaxed,0.03,0.92
pdt,fixed,0.02,0.96
dtma,relaxed,0.00,0.93
dtma,fixed,0.02,0.97
dtme,relaxed,0.00,0.93
dtme,fixed,0.01,0.97
FFEOF

# === solve block: casdtma_mixing.json ===
cat > /app/outputs/casdtma_mixing.json <<'FFEOF'
{
  "relaxed_max_mixing": 0.07,
  "fixed_max_mixing": 0.08
}
FFEOF
