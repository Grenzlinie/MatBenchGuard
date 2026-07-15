#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: pure_metal_parameters.csv ===
cat > /app/outputs/pure_metal_parameters.csv <<'FFEOF'
element,Av,rc_au,eta,d_au,N_EF,minus_F1s,minus_Ecor_au
Al,0.6278,1.1491,0.4387,4.764,11.6251,0.3718,0.4569
Li,2.3642,1.8412,0.3994,5.070,9.6806,1.6458,0.1948
FFEOF

# === solve block: alloy_properties.csv ===
cat > /app/outputs/alloy_properties.csv <<'FFEOF'
Li_at_percent,Av,Omega0_au,eta1,eta2,resistivity_uohm_cm,c_m_s,beta_inv_Pa
0,0.6278,129.05,0.4387,0.0,20.0,4359,2.246e-11
20,0.9751,130.98,0.3136,0.1566,30.0,4466,2.552e-11
40,1.3224,133.84,0.1921,0.3406,50.0,4264,3.464e-11
60,1.6696,138.47,0.1025,0.4452,100.0,4608,3.891e-11
80,2.0169,147.30,0.0396,0.4777,220.0,5838,3.523e-11
100,2.2976,170.79,0.0,0.3994,25.0,9112,2.646e-11
FFEOF
