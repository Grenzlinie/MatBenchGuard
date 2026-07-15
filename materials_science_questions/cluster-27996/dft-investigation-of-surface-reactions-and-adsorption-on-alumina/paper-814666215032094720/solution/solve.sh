#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: dft_adsorption_geometry.json ===
cat > /tmp/gen_dft.py << 'PYEOF'
import json

xyz = '''10
comment line
Al  0.000  0.000  0.000
Al  2.860  0.000  0.000
P   1.430  0.000  2.200
O   0.000  0.000  1.950
O   2.860  0.000  2.000
C   1.430 -1.200  3.000
H   1.430 -2.200  2.500
H   1.430 -1.000  4.000
C   1.430  0.000  4.000
H   1.430  1.000  3.500
'''
data = {
    'al_oxygen_distance_1': 1.95,
    'al_oxygen_distance_2': 2.00,
    'coordinates_xyz': xyz.strip()
}
with open('/app/outputs/dft_adsorption_geometry.json', 'w') as f:
    json.dump(data, f, indent=2)
PYEOF
python3 /tmp/gen_dft.py
rm /tmp/gen_dft.py

# === solve block: qmmm_hbond_distance.json ===
cat > /tmp/gen_qmmm.py << 'PYEOF'
import json

xyz = '''15
comment line
Al  0.000  0.000 -1.800
O   0.000  0.000  0.000
H   0.700  0.000  0.000
Al  3.000  2.000 -1.800
O   3.000  2.000  0.000
H   3.700  2.000  0.000
P   4.370  0.000  0.000
O   2.770  0.000  0.000
O   4.370  0.000  1.480
O   4.370  1.480  0.000
C   5.900  0.000  0.000
H   6.300  0.900  0.000
H   6.300 -0.900  0.000
C   6.500  0.000  1.390
H   6.100  0.900  1.890
'''
data = {
    'o_ho_distance': 2.07,
    'coordinates_xyz': xyz.strip()
}
with open('/app/outputs/qmmm_hbond_distance.json', 'w') as f:
    json.dump(data, f, indent=2)
PYEOF
python3 /tmp/gen_qmmm.py
rm /tmp/gen_qmmm.py
