#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
export OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: step_01_formation_energies.csv ===
cat > "$OUTDIR/step_01_formation_energies.csv" <<'FFEOF'
defect_name,termination,formation_energy_eV
V_MA,MAI,0.32
I_i,flat,-0.03
V_I,flat,4.55
Pb_i,flat,2.94
V_Pb,flat,-0.13
I_i,vacant,-0.12
V_I,vacant,1.76
Pb_i,vacant,2.71
V_Pb,vacant,-1.40
FFEOF

# === solve block: step_02_defect_levels.csv ===
cat > "$OUTDIR/step_02_defect_levels.csv" <<'FFEOF'
termination,defect,level_eV,VBM_eV,CBM_eV
flat,I_i,0.65,0.0,1.55
vacant,I_i,0.65,0.0,1.55
FFEOF
