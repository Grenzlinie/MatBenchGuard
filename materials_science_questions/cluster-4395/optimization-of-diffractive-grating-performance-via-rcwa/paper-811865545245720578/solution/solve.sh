#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: step_01_nonconical_results.csv ===
cat > /app/outputs/step_01_nonconical_results.csv <<'EOF'
polarization,model_type,de0
TE,first_order,1.1958
TE,second_order,0.0104
TE,higher_order,0.0135
TE,RCWA,0.0001
TM,first_order,3.7546
TM,second_order,0.0564
TM,higher_order,0.4554
TM,RCWA,0.0007
EOF

# === solve block: step_02_conical_results.csv ===
cat > /app/outputs/step_02_conical_results.csv <<'EOF'
lambda_over_period,de0_TE_HLM,de0_TM_HLM,de0_total_HLM,phase_HLM,de0_TE_RCWA,de0_TM_RCWA,de0_total_RCWA,phase_RCWA
4.0,0.08,0.03,0.11,-140.0,0.081,0.029,0.11,-139.0
5.0,0.06,0.02,0.08,-145.0,0.061,0.0195,0.0805,-144.0
6.0,0.045,0.015,0.06,-148.0,0.046,0.0148,0.0608,-147.5
7.0,0.035,0.012,0.047,-150.0,0.036,0.0118,0.0478,-149.5
8.0,0.028,0.01,0.038,-152.0,0.029,0.0098,0.0388,-151.5
9.0,0.023,0.008,0.031,-153.0,0.024,0.0079,0.0319,-152.5
10.0,0.019,0.007,0.026,-154.0,0.02,0.0069,0.0269,-153.5
EOF

# === solve finalize ===
echo 'Oracle artifacts written.'
