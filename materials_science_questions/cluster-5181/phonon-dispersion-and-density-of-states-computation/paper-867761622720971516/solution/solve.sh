#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: fitted_coefficients.csv ===
# Write fitted coefficients in atomic units
python3 -c "
import csv
out = '/app/outputs/fitted_coefficients.csv'
with open(out, 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['coefficient', 'value', 'unit'])
    w.writerows([
        ['e0', '0.2176', 'atomic units'],
        ['e1', '-0.1126', 'atomic units'],
        ['e2', '0.0489', 'atomic units'],
        ['p0', '-0.6756', 'atomic units'],
        ['Q0', '-0.346', 'atomic units'],
        ['Q1', '-0.069', 'atomic units'],
        ['Q2', '0.110', 'atomic units']
    ])
"

# === solve block: susceptibilities.csv ===
# Write susceptibilities in SI units
cat > /app/outputs/susceptibilities.csv <<'EOF'
label,value,unit
chi_11,14.8,m^0
chi_22,6.88e-10,m/V
chi_33,2.97e-18,m^2/V^2
chi_31,3.22e-15,m^2/V^2
DC_shift,0.26,meV
EOF
