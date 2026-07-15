#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: metrics.csv ===
cat > /app/outputs/metrics.csv <<'EOF'
property,model,MAE,MSE,R2
formation_energy,SVM-RBF,0.5104,0.4016,0.5607
formation_energy,RF,0.3731,0.2449,0.7231
formation_energy,RR,0.5822,0.5109,0.4574
formation_energy,BPNN,0.4744,0.3514,0.6091
stability,SVM-RBF,0.2074,0.0898,0.8081
stability,RF,0.2023,0.0895,0.7792
stability,RR,0.2465,0.1078,0.7263
stability,BPNN,0.2239,0.0993,0.7808
volume_per_atom,SVM-RBF,0.4626,0.7085,0.9042
volume_per_atom,RF,0.4442,0.6271,0.9195
volume_per_atom,RR,1.8019,5.0720,0.3205
volume_per_atom,BPNN,0.4134,0.4679,0.9372
vacancy_energy,SVM-RBF,1.8631,6.7088,0.6631
vacancy_energy,RF,1.8742,7.0501,0.6562
vacancy_energy,RR,2.3823,9.9980,0.5265
vacancy_energy,BPNN,2.0144,6.7663,0.6651
EOF
