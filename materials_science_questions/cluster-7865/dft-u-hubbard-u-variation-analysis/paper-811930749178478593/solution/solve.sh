#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: lattice_parameters.csv ===
cat > "$OUTDIR/lattice_parameters.csv" <<'FFEOF'
compound,a_calc,B0_calc
Pu,4.714,16
Ga,4.588,50
In,3.302,35
Sn,6.642,37
Ge,5.766,60
Pu3Ga,4.515,52
Pu3In,4.699,53
Pu3Sn,4.717,66
PuIn3,4.645,57
PuSn3,4.661,60
PuGe3,4.245,82
FFEOF

# === solve block: gap_widths.csv ===
cat > "$OUTDIR/gap_widths.csv" <<'FFEOF'
compound,gap_width
Pu3In,1.0
Pu3Ga,1.5
Pu3Sn,2.3
FFEOF

# === solve block: formation_heats.csv ===
cat > "$OUTDIR/formation_heats.csv" <<'FFEOF'
compound,formation_heat
Pu3In,-0.33
Pu3Ga,-0.42
Pu3Sn,-0.56
PuIn3,-0.39
PuSn3,-0.54
PuGe3,-0.70
FFEOF

# === solve finalize ===
# finalize: no further steps needed
