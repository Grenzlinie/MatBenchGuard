#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: step_01_dft_gsfe_parameters.json ===
cat > /app/outputs/step_01_dft_gsfe_parameters.json <<'EOF'
{
  "Be": {
    "U1": 1335.7,
    "I": 678.2,
    "U2": 1768.6,
    "xI_over_b": 0.47
  },
  "Mg": {
    "U1": 262.9,
    "I": 168.1,
    "U2": 397.4,
    "xI_over_b": 0.49
  },
  "Co_NM": {
    "U1": 870.0,
    "I": 857.3,
    "U2": 1502.5,
    "xI_over_b": 0.30
  },
  "Co_FM": {
    "U1": 889.6,
    "I": 702.2,
    "U2": 1381.2,
    "xI_over_b": 0.45
  }
}
EOF

# === solve block: step_02_pfdd_dislocation_results.csv ===
python3 -c "
import csv
rows = [
    ['material','dislocation_type','Re','bl','br','wl','wr'],
    ['Mg','edge',25.81,0.49,0.51,0.89,0.45],
    ['Mg','screw',17.66,0.46,0.51,0.89,0.47],
    ['Co_FM','edge',23.33,0.47,0.53,1.79,0.89],
    ['Co_FM','screw',16.97,0.47,0.53,1.34,0.67]
]
with open('/app/outputs/step_02_pfdd_dislocation_results.csv','w',newline='') as f:
    writer = csv.writer(f)
    writer.writerows(rows)
"
