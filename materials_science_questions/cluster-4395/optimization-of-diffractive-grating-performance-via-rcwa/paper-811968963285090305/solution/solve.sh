#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: step_01_diffraction_efficiencies.csv ===
cat > /app/outputs/step_01_diffraction_efficiencies.csv <<'EOF'
m,eta_r,theta_r,eta_t,theta_t
-5,0.4,8.4,1.2,12.7
-4,0.4,17.4,1.1,26.6
-3,1.1,26.8,5.9,42.5
-2,0.7,37.0,15.4,64.6
-1,12.3,50.0,,
0,55.8,65.0,,
EOF

# === solve block: step_02_outcoupled_power.csv ===
cat > /app/outputs/step_02_outcoupled_power.csv <<'EOF'
f,power_60,power_70,power_80
0.20,3.5,1.0,0.0
0.25,7.0,3.0,1.0
0.30,11.0,5.5,2.5
0.35,15.0,8.0,4.5
0.40,19.0,11.0,7.0
0.45,23.0,14.0,10.0
0.50,27.5,17.5,13.5
EOF
