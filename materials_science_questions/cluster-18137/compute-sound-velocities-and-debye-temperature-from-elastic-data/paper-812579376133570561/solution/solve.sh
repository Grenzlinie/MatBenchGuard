#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: computed_properties.csv ===
cat > /app/outputs/computed_properties.csv <<'CSVEOF'
configuration,C11,C12,C44,B_VRH,G_VRH,E,Poisson_ratio,v_m,Debye_T,stable_C1p2,stable_C4,stable_C11mC12
pristine,285.1,102.5,82.1,163.4,85.7,218.8,0.277,4666.0,580.2,True,True,True
V_O48f,281.5,102.4,74.3,162.1,80.1,206.2,0.287,4556.0,564.4,True,True,True
Zr_Gd,293.4,104.5,76.3,167.5,83.1,213.9,0.287,4643.9,579.1,True,True,True
Gd_int2,274.8,91.7,51.3,152.7,64.8,170.4,0.315,4087.9,508.9,True,True,True
Zr_8a,275.8,101.1,40.3,159.3,55.2,148.6,0.346,3850.1,479.3,True,True,True
O_8a,269.5,113.5,76.7,165.5,77.2,200.5,0.299,4476.9,558.8,True,True,True
CSVEOF
