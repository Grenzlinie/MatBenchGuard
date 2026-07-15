#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: step_01_j_coupling_results.csv ===
cat > "$OUTDIR/step_01_j_coupling_results.csv" <<'FFEOF'
molecule,position,functional,J_calc
fluorocyclohexane,axial,B3LYP,149.3
fluorocyclohexane,axial,BLYP,148.9
fluorocyclohexane,axial,PBEPBE,135.7
fluorocyclohexane,equatorial,B3LYP,153.9
fluorocyclohexane,equatorial,BLYP,153.4
fluorocyclohexane,equatorial,PBEPBE,140.1
2-chloropyran,anomeric,B3LYP,180.8
2-chloropyran,anomeric,BLYP,181.0
2-chloropyran,anomeric,PBEPBE,165.9
FFEOF
