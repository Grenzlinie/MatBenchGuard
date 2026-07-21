#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs
python3 /solution/write_outputs.py

# === solve block: adsorption_workfunction.csv ===
cat > "$OUTDIR/adsorption_workfunction.csv" << 'EOF'
site,orientation,adsorption_energy_eV,work_function_eV,work_function_change_eV
H',Cs-up,-5.2,3.49,-1.46
T3,Cs-up,-5.0,3.48,-1.47
T3',Cs-up,-5.1,4.09,-0.86
T4,Cs-up,-6.34,3.79,-1.16
T4',Cs-up,-5.3,4.09,-0.86
H',NF3-up,-3.5,4.10,-0.85
T3,NF3-up,-3.55,4.15,-0.80
T3',NF3-up,-3.5,4.25,-0.70
T4,NF3-up,-3.55,4.20,-0.75
T4',NF3-up,-3.5,4.25,-0.70
EOF

# === solve block: mulliken_charges.csv ===
# written by /solution/write_outputs.py

# === solve block: dipole_descriptors.csv ===
# written by /solution/write_outputs.py

# === solve block: geometric_structure.csv ===
# written by /solution/write_outputs.py
