#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
# Paper2ARM reference oracle — write scored artifacts directly.
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: step_01_lattice_params.csv ===
cat > "$OUTDIR/step_01_lattice_params.csv" <<'FFEOF'
Compound,a,c,u
CuAlO2,2.816,16.978,0.1091
CuGaO2,2.963,17.172,0.1073
CuInO2,3.285,17.270,0.1056
FFEOF

# === solve block: step_02_band_gaps.csv ===
cat > "$OUTDIR/step_02_band_gaps.csv" <<'FFEOF'
Compound,fundamental_direct_gap_F,fundamental_direct_gap_L,fundamental_direct_gap_Γ,indirect_gap
CuAlO2,2.95,2.68,2.93,1.97
CuGaO2,3.05,2.54,1.63,0.95
CuInO2,3.34,3.08,0.73,0.41
FFEOF

# === solve block: step_03_apparent_gaps.csv ===
cat > "$OUTDIR/step_03_apparent_gaps.csv" <<'FFEOF'
Compound,apparent_direct_gap
CuAlO2,2.75
CuGaO2,2.70
CuInO2,3.12
FFEOF

# === solve block: step_05_band_offsets.csv ===
cat > "$OUTDIR/step_05_band_offsets.csv" <<'FFEOF'
Compound,VBM_offset,CBM_offset
CuAlO2,0.0,0.0
CuGaO2,0.02,-1.00
CuInO2,0.08,-1.48
FFEOF

# === solve finalize ===
# All artifacts written.
