#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: decomposition_energies.json ===
cat > /app/outputs/decomposition_energies.json <<'FFEOF'
{
  "Li6SiO4Cl2_Pna2_1": -18,
  "Li6SiO4ClBr_Pna2_1": -16,
  "Li6SiO4Br2_Pna2_1": -6,
  "Li6SiO4ClI_P6_3mc": -2
}
FFEOF

# === solve block: elastic_constants.json ===
cat > /app/outputs/elastic_constants.json <<'FFEOF'
{
  "B_DFT": 53,
  "G_DFT": 31
}
FFEOF
