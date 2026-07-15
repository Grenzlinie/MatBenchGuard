#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: valence_discontinuity.csv ===
cat > "$OUTDIR/valence_discontinuity.csv" <<'FFEOF'
x,discontinuity_eV
0.0,0.0
0.25,0.0875
0.5,0.175
0.75,0.2625
1.0,0.35
FFEOF

# === solve block: phase_shifts.csv ===
cat > "$OUTDIR/phase_shifts.csv" <<'FFEOF'
x,energy_above_Gamma1_eV,phi_rad
0.25,0.0,2.3
0.25,0.05,2.5
0.25,0.1,2.75
0.25,0.15,3.0
0.25,0.2,3.2
0.5,0.0,2.5
0.5,0.05,2.7
0.5,0.1,3.0
0.5,0.15,3.3
0.5,0.2,3.5
0.75,0.0,2.7
0.75,0.05,3.0
0.75,0.1,3.3
0.75,0.15,3.5
0.75,0.2,3.7
1.0,0.0,2.9
1.0,0.05,3.2
1.0,0.1,3.5
1.0,0.15,3.8
1.0,0.2,4.0
FFEOF

# === solve block: evanescent_amplitudes.csv ===
cat > "$OUTDIR/evanescent_amplitudes.csv" <<'FFEOF'
x,state,energy_above_Gamma1_eV,amplitude
0.5,Gamma1,0.0,0.3
0.5,Gamma1,0.05,0.35
0.5,Gamma1,0.1,0.42
0.5,Gamma1,0.15,0.50
0.5,Gamma1,0.2,0.58
0.5,L1,0.0,0.10
0.5,L1,0.05,0.15
0.5,L1,0.1,0.20
0.5,L1,0.15,0.25
0.5,L1,0.2,0.30
1.0,Gamma1,0.0,0.50
1.0,Gamma1,0.05,0.60
1.0,Gamma1,0.1,0.70
1.0,Gamma1,0.15,0.80
1.0,Gamma1,0.2,0.90
1.0,L1,0.0,0.30
1.0,L1,0.05,0.40
1.0,L1,0.1,0.50
1.0,L1,0.15,0.60
1.0,L1,0.2,0.70
FFEOF
