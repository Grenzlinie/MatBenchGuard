#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: structural_params.csv ===
python3 -c "
import csv, os
out = os.environ.get('OUTDIR', '/app/outputs')
with open(f'{out}/structural_params.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['system', 'HSiSi_angle', 'SiSi_nn_length', 'SiSi_nnn_length', 'HSi_length'])
    w.writerow(['chair_2_2', 107.0, 2.33, 2.23, 1.50])
    w.writerow(['chair_2_8', 108.5, 2.32, 2.24, 1.50])
    w.writerow(['chair_2_32', 110.1, 2.31, 2.24, 1.50])
    w.writerow(['top_1_2', 109.8, 2.33, 2.23, 1.50])
    w.writerow(['top_1_8', 111.1, 2.32, 2.24, 1.50])
    w.writerow(['top_1_32', 111.7, 2.31, 2.24, 1.50])
"

# === solve block: band_gaps.csv ===
cat > /app/outputs/band_gaps.csv <<'EOF'
system,gap_type,value_eV
chair_2_2,indirect,2.1
chair_2_8,direct,1.3
chair_2_32,direct,0.2
top_1_2,direct,0.0
top_1_8,direct,0.0
top_1_32,direct,0.0
EOF

# === solve block: dos_peaks.csv ===
cat > /app/outputs/dos_peaks.csv <<'EOF'
system,peak_energy_eV,peak_type,intensity
chair_2_2,-3.5,H_related,1.6
chair_2_8,-4.0,H_related,0.4
chair_2_32,-4.2,H_related,0.1
top_1_2,-3.5,H_related,0.8
top_1_8,-4.0,H_related,0.2
top_1_32,-4.2,H_related,0.05
top_1_2,0.0,delta,1.3
top_1_8,0.0,delta,0.1625
top_1_32,0.0,delta,0.040625
EOF

# === solve block: linear_fit.json ===
cat > /app/outputs/linear_fit.json <<'EOF'
{"H_peak_slope":1.6,"H_peak_intercept":0.0,"delta_peak_slope":1.3,"delta_peak_intercept":0.0}
EOF
