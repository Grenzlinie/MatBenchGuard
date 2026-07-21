#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs
cat > /app/outputs/predictions.csv <<EOF
true_value,predicted_mean,predicted_std
1.0,1.0,0.1
2.0,2.0,0.1
EOF
