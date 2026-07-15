#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: core_shell_frequencies.txt ===
cat > "$OUTDIR/core_shell_frequencies.txt" << 'EOF'
O: ν = 109.8 THz ( 3663.76 cm⁻¹ )
U: ν = 133.6 THz ( 4457.39 cm⁻¹ )
EOF

# === solve block: oxygen_fp_recombination_times.csv ===
python3 /solution/recombination_times.py > "$OUTDIR/oxygen_fp_recombination_times.csv"

# === solve block: oxygen_fp_arrhenius_params.csv ===
python3 -c "
with open('$OUTDIR/oxygen_fp_arrhenius_params.csv','w') as f:
    f.write('rank,tau0_ps,Ea_eV\n')
    f.write('3,0.06,0.32\n')
    f.write('4I,0.16,0.11\n')
    f.write('4II,0.03,0.51\n')
    f.write('5,0.01,0.57\n')
"
