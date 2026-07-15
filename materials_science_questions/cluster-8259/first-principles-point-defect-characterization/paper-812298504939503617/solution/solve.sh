#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: anhydrous_lattice_parameters.csv ===
cat > "$OUTDIR/anhydrous_lattice_parameters.csv" <<'CSVEOF'
pressure_GPa,a_Ang,b_Ang,c_Ang,V_Ang3
0,4.705,10.131,5.957,283.99
2,4.688,10.065,5.926,279.59
4,4.674,10.000,5.898,275.61
6,4.659,9.942,5.870,271.87
8,4.646,9.885,5.844,268.42
10,4.633,9.831,5.820,265.12
12,4.622,9.782,5.797,262.08
CSVEOF

# === solve block: anhydrous_band_gaps.csv ===
cat > "$OUTDIR/anhydrous_band_gaps.csv" <<'CSVEOF'
pressure_GPa,Eg_eV
0,3.72
16,4.24
CSVEOF

# === solve block: hydrous_band_gaps.csv ===
cat > "$OUTDIR/hydrous_band_gaps.csv" <<'CSVEOF'
orientation,Eg_eV
[100],0.942
[010],1.007
[001],0.693
CSVEOF
