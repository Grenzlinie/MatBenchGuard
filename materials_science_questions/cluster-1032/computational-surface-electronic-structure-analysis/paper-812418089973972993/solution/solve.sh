#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: adsorption_energies.csv ===
# Write adsorption energies at most favorable sites
cat > "$OUTDIR/adsorption_energies.csv" <<'FFEOF'
surface,adsorption_energy_kcal_per_mol
Ni(111),77
Ni(100),80.5
Ni(110),80
FFEOF

# === solve block: energy_variation_n111.csv ===
# Write maximum energy variation on Ni(111)
cat > "$OUTDIR/energy_variation_n111.csv" <<'FFEOF'
max_variation_kcal_per_mol
2.5
FFEOF
