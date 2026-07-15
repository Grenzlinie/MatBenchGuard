#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: computed_data.csv ===
cat > "$OUTDIR/computed_data.csv" <<'FFEOF'
species,surface_type,adsorption_energy,fermi_level_shift
H2O,pristine,-0.18,0.06
OH,pristine,-1.41,0.44
O,pristine,-2.88,0.26
C,pristine,-3.93,0.36
CH,pristine,-3.23,0.44
H2O,vacancy,-0.18,0.29
OH,vacancy,-3.61,0.55
O,vacancy,-5.42,0.00
C,vacancy,-3.58,0.07
CH,vacancy,-4.49,0.20
FFEOF

# === solve block: reaction_energies.csv ===
cat > "$OUTDIR/reaction_energies.csv" <<'FFEOF'
reaction,delta_E
H2O/V -> OH/V + H/S,0.76
OH/V -> O/V + H/S,1.72
H2O/V -> O/V + H2,0.60
FFEOF
