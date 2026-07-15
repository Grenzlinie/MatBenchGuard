#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs
OUTDIR=/app/outputs

# === solve block: step_02_invariant_equilibria.csv ===
cat > "$OUTDIR/step_02_invariant_equilibria.csv" <<'FFEOF'
reaction,T_C,composition_phase1,composition_phase2,composition_phase3
Ni(s)/ liquid,1455.1,0.0,0.0,
fcc-(Ni)/ liquid/ζ,909.7,7.9,25.0,31.4
fcc-(Ni)/ Ni₃In/ζ,845.0,6.9,25.0,31.6
Ni₃In/ Ni₂In/ζ,665.0,25.0,33.3,33.4
Ni₂In/ ζ/ζ',472.6,33.3,35.3,40.9
ζ/liquid/ δ,923.8,41.7,48.7,51.2
ζ/ζ'/δ,868.7,41.0,42.4,51.6
ζ'/NiIn/ δ,862.8,42.4,50.0,51.8
ζ/liquid,946.6,35.6,35.6,
δ/liquid,926.2,55.0,55.0,
NiIn/δ/ Ni₂In₃,776.4,50.0,55.8,60.0
δ/Ni₂In₃/ liquid,868.9,59.4,60.0,76.1
Ni₂In₃/ Ni₃In₇/ liquid,404.2,60.0,70.0,96.3
Ni₃In₇/ liquid/ In(s),156.3,70.0,99.9,100.0
In(s)/ liquid,156.6,100.0,100.0,
FFEOF

# === solve block: step_03_in_partial_pressures.csv ===
cat > "$OUTDIR/step_03_in_partial_pressures.csv" <<'FFEOF'
two_phase_region,log_p_In
ζ/ζ',-7.941
ζ'/NiIn,-7.801
NiIn/Ni₂In₃,-7.415
Ni₂In₃/liquid,-7.053
FFEOF

# === solve block: step_04_enthalpies_melting.csv ===
cat > "$OUTDIR/step_04_enthalpies_melting.csv" <<'FFEOF'
phase,melting_T_C,composition,enthalpy_melting
ζ-Ni₂In,946.6,0.356,15914
δ-NiIn,926.2,0.549,19628
FFEOF
