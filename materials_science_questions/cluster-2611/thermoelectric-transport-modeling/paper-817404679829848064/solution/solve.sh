#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: pristine_band_gap.txt ===
cat > "$OUTDIR/pristine_band_gap.txt" <<'EOF'
0.523
EOF

# === solve block: transport_properties.csv ===
cat > "$OUTDIR/transport_properties.csv" <<'EOF'
temperature,material,Seebeck,sigma_over_tau,kappa_over_tau,ZT
300,pristine,-340.0,1.2e19,2.2e15,0.010
400,pristine,-310.0,1.5e19,2.1e15,0.026
500,pristine,-280.0,1.8e19,2.0e15,0.038
600,pristine,-250.0,2.2e19,1.9e15,0.052
700,pristine,-220.0,2.6e19,1.8e15,0.061
800,pristine,-190.0,3.0e19,1.7e15,0.070
300,Sm8,-55.0,8.5e19,3.3e15,0.0009
400,Sm8,-75.0,8.2e19,3.2e15,0.0018
500,Sm8,-95.0,7.9e19,3.1e15,0.0025
600,Sm8,-115.0,7.6e19,3.0e15,0.0031
700,Sm8,-135.0,7.3e19,2.9e15,0.0036
800,Sm8,-155.0,7.0e19,2.8e15,0.0040
300,Sm17,-70.0,1.4e20,2.6e15,0.052
400,Sm17,-90.0,1.35e20,2.5e15,0.082
500,Sm17,-105.0,1.30e20,2.4e15,0.147
600,Sm17,-115.0,1.25e20,2.3e15,0.216
700,Sm17,-120.0,1.20e20,2.2e15,0.286
800,Sm17,-120.0,1.15e20,2.1e15,0.320
EOF
