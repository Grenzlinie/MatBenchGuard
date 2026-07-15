#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: step_01_lowdin_populations.csv ===
cat > "$OUTDIR/step_01_lowdin_populations.csv" <<'FFEOF'
configuration,atom_type,population
SrFeO3,Fe,6.81
SrFeO3,Sr,9.85
SrFeO3,O,6.42
SrFeO2.875,Fe1,6.81
SrFeO2.875,Fe2,6.82
SrFeO2.875,Fe3,6.87
SrFeO2.875,Sr1,9.83
SrFeO2.875,Sr2,9.88
SrFeO2.875,O1,6.44
SrFeO2.875,O2,6.44
SrFeO2.875,O3,6.45
SrFeO2.875,O4,6.42
SrFeO2.875,O5,6.41
SrFeO2.875,O6,6.33
SrFeO2.875,O7,6.45
FFEOF

# === solve block: step_02_vacancy_formation_energy.txt ===
cat > "$OUTDIR/step_02_vacancy_formation_energy.txt" <<'FFEOF'
E_vf1 = 0.92 eV
E_vf2 = 1.32 eV
FFEOF
