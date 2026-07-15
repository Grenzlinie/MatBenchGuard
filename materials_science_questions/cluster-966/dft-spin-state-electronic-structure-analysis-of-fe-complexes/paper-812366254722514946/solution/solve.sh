#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: oscillator_strengths_odd_vibrations.csv ===
cat > "$OUTDIR/oscillator_strengths_odd_vibrations.csv" <<'FFEOF'
initial_state,final_state,vibration_mode,oscillator_strength
^6A1g,^4T2g(1),T1u(nu3),5.56e-07
^6A1g,^4T2g(1),T1u(nu4),3.44e-07
^6A1g,^4T2g(1),T2u(nu6),4.7e-08
^6A1g,^4Eg(1),T1u(nu3),3.94e-07
^6A1g,^4Eg(1),T1u(nu4),1.22e-07
^6A1g,^4Eg(1),T2u(nu6),4.59e-07
^6A1g,^4A1g,T1u(nu3),2.69e-07
^6A1g,^4A1g,T1u(nu4),8.9e-08
^6A1g,^4A1g,T2u(nu6),2.95e-07
^6A1g,^4T1g(1),T1u(nu3),1.52e-07
^6A1g,^4T1g(1),T1u(nu4),2.61e-07
^6A1g,^4T1g(1),T2u(nu6),1.1e-08
FFEOF

# === solve block: faraday_parameters_odd_vibrations.csv ===
cat > "$OUTDIR/faraday_parameters_odd_vibrations.csv" <<'FFEOF'
transition,vibration_mode,A,B,C,B_plus_C_over_kT
^6A1g -> ^4T2g(1),T1u(nu3),-251.5,0.180,649.4,3.427
^6A1g -> ^4T2g(1),T1u(nu4),-42.1,0.039,148.1,0.780
^6A1g -> ^4T2g(1),T2u(nu6),6.8,0.040,-20.5,-0.063
^6A1g -> ^4Eg(1),T1u(nu3),-170.6,-0.411,331.6,1.247
^6A1g -> ^4Eg(1),T1u(nu4),-15.7,0.231,30.6,0.384
^6A1g -> ^4Eg(1),T2u(nu6),180.2,0.033,-350.3,-1.719
^6A1g -> ^4A1g,T1u(nu3),107.8,0.342,-209.6,-0.706
^6A1g -> ^4A1g,T1u(nu4),35.2,-0.214,-68.4,-0.556
^6A1g -> ^4A1g,T2u(nu6),-118.8,0.057,231.0,1.212
FFEOF
