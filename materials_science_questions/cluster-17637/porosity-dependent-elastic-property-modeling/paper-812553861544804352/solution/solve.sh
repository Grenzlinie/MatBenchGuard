#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p "/app/outputs"

# === solve block: degraded_properties.csv ===
cat > "/app/outputs/degraded_properties.csv" <<'EOF'
age,E_m,f_t
1,32686.42,3.8
25,31550.23,3.66
50,27824.35,3.23
75,23122.96,2.68
100,19086.7,2.21
EOF

# === solve block: response_summary.csv ===
cat > "/app/outputs/response_summary.csv" <<'EOF'
earthquake,motion_type,age,max_crest_displacement,max_major_principal_stress_heel,max_minor_principal_stress_neck,max_hydrodynamic_pressure
Northridge,NF,1,0.041,7.66,-8.11,0.29
Northridge,NF,75,0.045,6.38,-6.95,0.25
Northridge,FF,1,0.029,5.20,-6.49,0.20
Northridge,FF,75,0.036,4.61,-6.50,0.19
Imperial Valley,NF,1,0.035,6.80,-6.61,0.24
Imperial Valley,NF,75,0.044,6.20,-6.09,0.21
Imperial Valley,FF,1,0.028,5.45,-6.42,0.20
Imperial Valley,FF,75,0.025,3.97,-4.72,0.17
EOF
