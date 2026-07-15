#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: step_02_ground_states.csv ===
cat > "$OUTDIR/step_02_ground_states.csv" <<'FFEOF'
b_site_ordering,compound,formation_energy_meV_per_fu,magnetic_order,space_group
010,Sr2FeCoO5,-709.1,G-AFM,Pbcm
100,Sr2FeNiO5,-472.2,G-AFM,Pbcm
100,Sr2FeMnO5,594.8,G-AFM,Pbcm
100,Sr2CoNiO5,-287.1,G-AFM,Pbcm
100,Sr2CoMnO5,594.7,G-AFM,Pnma
100,Sr2NiMnO5,-476.4,A-AFM,Pbcm
FFEOF

# === solve block: step_03_phonon_stability.txt ===
cat > "$OUTDIR/step_03_phonon_stability.txt" <<'FFEOF'
Sr2FeCoO5:true
Sr2FeNiO5:false
Sr2CoNiO5:false
Sr2NiMnO5:true
FFEOF

# === solve block: step_04_electronic_summary.csv ===
cat > "$OUTDIR/step_04_electronic_summary.csv" <<'FFEOF'
bandgap_eV,compound,electronic_type,magnetic_ordering
1.3,Sr2FeCoO5,insulator,G-AFM
1.0,Sr2NiMnO5,half-metal,A-AFM
FFEOF

# === solve block: step_05_exchange_constants.csv ===
cat > "$OUTDIR/step_05_exchange_constants.csv" <<'FFEOF'
compound,interaction,value_meV
Sr2FeCoO5,J_CoCo,12.2
Sr2FeCoO5,J_FeCo,-98.1
Sr2FeCoO5,J_FeFe,-81.0
Sr2NiMnO5,J_NiNi,-56.6
Sr2NiMnO5,J_MnMn,18.7
Sr2NiMnO5,J_NiMn,31.4
FFEOF
