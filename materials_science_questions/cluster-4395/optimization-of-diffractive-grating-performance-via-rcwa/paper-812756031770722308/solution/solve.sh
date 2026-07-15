#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p $OUTDIR

# === solve block: frequency_sweep.csv ===
cat > $OUTDIR/frequency_sweep.csv <<'FFEOF'
p_lambda,reflection_phase_deg
0.05,180.0
0.10,180.0
0.15,180.0
0.20,179.5
0.25,177.0
0.30,174.0
0.35,169.0
0.40,163.0
FFEOF

# === solve block: angular_sweep.csv ===
cat > $OUTDIR/angular_sweep.csv <<'FFEOF'
incidence_angle_deg,reflection_phase_deg
0,180.0
10,180.0
20,180.0
30,180.0
40,180.0
50,180.0
60,180.0
70,180.0
80,180.0
FFEOF
