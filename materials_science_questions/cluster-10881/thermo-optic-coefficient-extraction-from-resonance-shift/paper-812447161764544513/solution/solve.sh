#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: fitted_angles.json ===
python3 -c "import json; d={'T_C':[22.5,50.6,69.2,101.0,133.3],'D_rad':[-0.00051,0.000237,0.00069,0.00144,0.00241]}; json.dump(d,open('$OUTDIR/fitted_angles.json','w'))"

# === solve block: linear_regression_slope.json ===
python3 -c "import json, math; T=[22.5,50.6,69.2,101.0,133.3]; D=[-0.00051,0.000237,0.00069,0.00144,0.00241]; n=len(T); sumT=sum(T); sumD=sum(D); sumTD=sum(t*d for t,d in zip(T,D)); sumT2=sum(t*t for t in T); slope=(n*sumTD-sumT*sumD)/(n*sumT2-sumT**2); intercept=(sumD-slope*sumT)/n; res=[D[i]-(slope*T[i]+intercept) for i in range(n)]; rms=math.sqrt(sum(r*r for r in res)/n); json.dump({'slope_rad_per_C':slope,'intercept_rad':intercept,'rms_residual_rad':rms},open('$OUTDIR/linear_regression_slope.json','w'))"

# === solve block: acceptance_ratio.json ===
python3 -c "import json; json.dump({'Delta_theta_L_mrad_cm':0.64,'Delta_T_L_C_cm':26.0,'ratio_rad_per_C':2.46e-5},open('$OUTDIR/acceptance_ratio.json','w'))"
