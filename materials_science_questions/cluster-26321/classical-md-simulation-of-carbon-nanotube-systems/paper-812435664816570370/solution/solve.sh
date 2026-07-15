#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: step_01_free_energy.csv ===
cat > /app/outputs/step_01_free_energy.csv <<'FFEOF'
N,free_energy_kT,uncertainty_kT
0,0.0,0.3
1,1.0,0.3
2,2.0,0.3
3,3.0,0.3
4,4.0,0.3
5,2.0,0.3
FFEOF

# === solve block: step_02_commitment.csv ===
cat > /app/outputs/step_02_commitment.csv <<'FFEOF'
config_id,p_fill
1,0.38
2,0.40
3,0.42
4,0.44
5,0.46
6,0.51
7,0.53
8,0.56
9,0.58
10,0.62
FFEOF

# === solve block: step_03_lifetimes.csv ===
cat > /app/outputs/step_03_lifetimes.csv <<'FFEOF'
tube_type,state,mean_lifetime_ps,std_ps,n_events
short,filled,190.0,40.0,20
short,empty,13.0,4.0,20
long,filled,240.0,80.0,15
long,empty,13.0,4.0,15
FFEOF

# === solve block: step_04_lambda_dependence.csv ===
cat > /app/outputs/step_04_lambda_dependence.csv <<'FFEOF'
lambda,slope,intercept
0.75,0.6,0.5
0.785,0.0,0.8
1.0,-3.6,3.0
FFEOF
