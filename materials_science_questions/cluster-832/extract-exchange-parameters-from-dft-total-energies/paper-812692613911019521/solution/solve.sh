#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: spin_wave_specific_heat.csv ===
cat > "$OUTDIR/spin_wave_specific_heat.csv" <<'FFEOF'
Material,Temperature_K,C_M_J_per_K_per_mole
NiF2,0.36,7.4e-10
MnF2,2.5,2.6e-12
FeF2,2.5,2.6e-12
CoF2,2.5,1.2e-7
NiF2,2.5,1.4e-4
MnF2,5.0,0.029
FeF2,5.0,7.4e-6
CoF2,5.0,0.0001
NiF2,5.0,0.0013
MnF2,7.5,0.158
FeF2,7.5,0.0014
CoF2,7.5,0.010
NiF2,7.5,0.0052
MnF2,10.0,0.509
FeF2,10.0,0.020
CoF2,10.0,0.097
NiF2,10.0,0.017
MnF2,12.5,1.088
FeF2,12.5,0.100
CoF2,12.5,0.350
NiF2,12.5,0.049
MnF2,15.0,1.785
FeF2,15.0,0.281
CoF2,15.0,0.785
NiF2,15.0,0.123
MnF2,20.0,3.158
FeF2,20.0,0.941
CoF2,20.0,1.96
NiF2,20.0,0.479
MnF2,25.0,4.248
FeF2,25.0,1.800
CoF2,25.0,3.15
NiF2,25.0,1.102
MnF2,30.0,5.043
FeF2,30.0,2.650
CoF2,30.0,4.15
NiF2,30.0,1.808
MnF2,35.0,5.614
FeF2,35.0,3.394
CoF2,35.0,4.94
NiF2,35.0,2.645
MnF2,40.0,6.029
FeF2,40.0,4.011
NiF2,40.0,3.320
MnF2,45.0,6.337
FeF2,45.0,4.513
NiF2,45.0,3.975
MnF2,50.0,6.569
FeF2,50.0,4.919
NiF2,50.0,4.527
FFEOF
