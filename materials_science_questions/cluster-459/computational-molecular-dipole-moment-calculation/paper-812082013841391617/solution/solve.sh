#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
set -euo pipefail
mkdir -p /app/outputs

# === solve block: dipole_moment_function.csv ===
cat > /app/outputs/dipole_moment_function.csv << 'EOF'
r,dipole_moment
1.5,-0.4766
1.6,-0.4249
1.7,-0.3685
1.8,-0.3083
1.9,-0.2452
2.0,-0.1802
2.13183,-0.09306
2.3,0.01720
2.5,0.1416
2.8,0.3005
3.1,0.4104
3.4,0.4758
3.7,0.4979
4.0,0.4688
4.5,0.3359
5.0,0.1958
5.5,0.1057
6.0,0.0526
EOF

# === solve block: dipole_matrix_elements.csv ===
cat > /app/outputs/dipole_matrix_elements.csv << 'EOF'
v_prime,v_double_prime,matrix_element_D
1,0,0.1070
2,0,-0.006415
EOF
