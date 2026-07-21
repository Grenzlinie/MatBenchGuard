#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: step_01_ff_transport.csv ===
cat > "$OUTDIR/step_01_ff_transport.csv" <<'FFEOF'
D_GK,eta_GK,temperature
2.56e-04,7.72e-09,360.0
4.43e-04,4.44e-09,330.0
8.60e-04,2.30e-09,300.0
1.89e-03,1.04e-09,270.0
2.60e-03,7.56e-10,260.0
FFEOF

# === solve block: step_02_aimd_transport.csv ===
cat > "$OUTDIR/step_02_aimd_transport.csv" <<'FFEOF'
D_GK,eta_GK,functional,temperature
5.0e-04,3.5e-09,PBE-D3,360.0
NaN,NaN,PBE-D3,330.0
NaN,NaN,PBE-D3,300.0
NaN,NaN,PBE-D3,270.0
NaN,NaN,PBE-D3,260.0
2.6e-04,7.7e-09,optB88-vdW,360.0
7.0e-04,4.0e-09,optB88-vdW,330.0
1.5e-03,2.0e-09,optB88-vdW,300.0
3.5e-03,1.0e-09,optB88-vdW,270.0
NaN,NaN,optB88-vdW,260.0
2.7e-04,7.5e-09,SCAN,360.0
4.5e-04,4.3e-09,SCAN,330.0
1.46e-03,1.8e-09,SCAN,300.0
3.8e-03,5.0e-10,SCAN,270.0
5.2e-03,2.0e-10,SCAN,260.0
FFEOF

# === solve block: step_03_s2.csv ===
cat > "$OUTDIR/step_03_s2.csv" <<'FFEOF'
functional,s2_kB,temperature
FF,-2.5,360.0
FF,-2.7,330.0
FF,-3.0,300.0
FF,-3.4,270.0
FF,-3.6,260.0
PBE-D3,-5.0,360.0
PBE-D3,-5.2,330.0
PBE-D3,-5.5,300.0
PBE-D3,-5.9,270.0
PBE-D3,-6.0,260.0
optB88-vdW,-2.5,360.0
optB88-vdW,-3.2,330.0
optB88-vdW,-3.8,300.0
optB88-vdW,-4.5,270.0
optB88-vdW,-5.0,260.0
SCAN,-2.5,360.0
SCAN,-2.8,330.0
SCAN,-3.1,300.0
SCAN,-3.5,270.0
SCAN,-3.8,260.0
FFEOF

# === solve block: step_04_fit_params.csv ===
cat > "$OUTDIR/step_04_fit_params.csv" <<'FFEOF'
A_D,A_eta,B_D,B_eta,functional
0.352,0.429,-0.397,0.411,optB88-vdW
0.817,0.179,-0.524,0.531,SCAN
0.773,0.192,-0.458,0.452,FF
FFEOF

# === solve finalize ===
# No finalize steps needed
