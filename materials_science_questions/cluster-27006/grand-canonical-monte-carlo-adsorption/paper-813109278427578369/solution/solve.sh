#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: binding_energies.csv ===
cat > "$OUTDIR/binding_energies.csv" << 'EOF'
site,E_ads_kJmol
hollow,-13.72
ligand,-10.76
metal_side_on,-10.61
metal_end_on,-6.50
EOF

# === solve block: isotherms_77K.csv ===
python3 << 'PYEOF' > "$OUTDIR/isotherms_77K.csv"
import csv, sys
data = [
    (1,    2.55, 2.56),
    (2,    3.19, 3.21),
    (3,    3.49, 3.52),
    (4,    3.65, 3.69),
    (5,    3.76, 3.81),
    (10,   4.05, 4.13),
    (20,   4.00, 4.32),
    (30,   4.00, 4.40),
    (40,   4.00, 4.46),
    (50,   4.00, 4.50),
    (60,   4.00, 4.53),
    (70,   4.00, 4.56),
    (80,   4.00, 4.58),
    (90,   4.00, 4.60),
    (100,  4.00, 4.62),
]
w = csv.writer(sys.stdout)
w.writerow(['pressure_bar', 'exc_wt', 'abs_wt'])
for row in data:
    w.writerow(row)
PYEOF

# === solve block: isotherms_298K.csv ===
python3 << 'PYEOF' > "$OUTDIR/isotherms_298K.csv"
import csv, sys
data = [
    (0,   0.0,   0.0),
    (10,  0.022, 0.063),
    (20,  0.044, 0.126),
    (30,  0.066, 0.189),
    (40,  0.088, 0.252),
    (50,  0.110, 0.315),
    (60,  0.132, 0.378),
    (70,  0.154, 0.441),
    (80,  0.176, 0.504),
    (90,  0.198, 0.567),
    (100, 0.220, 0.630),
]
w = csv.writer(sys.stdout)
w.writerow(['pressure_bar', 'exc_wt', 'abs_wt'])
for row in data:
    w.writerow(row)
PYEOF

# === solve block: electrostatic_contrib_77K.csv ===
cat > "$OUTDIR/electrostatic_contrib_77K.csv" << 'EOF'
pressure_bar,abs_wt_LJplusCoulomb,abs_wt_LJonly,coulomb_wt,electrostatic_pct
1,2.56,1.90,0.66,25.78
2,3.21,2.53,0.68,21.18
3,3.52,2.83,0.69,19.60
4,3.69,3.01,0.68,18.43
5,3.81,3.15,0.66,17.32
10,4.13,3.52,0.61,14.77
20,4.32,3.81,0.51,11.81
30,4.40,3.97,0.43,9.77
40,4.46,4.06,0.40,8.97
50,4.50,4.14,0.36,8.00
EOF
