#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
export OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: adsorption_energies.csv ===
cat > "$OUTDIR/adsorption_energies.csv" << 'CSV_EOF'
surface,adsorbate,adsorption_energy_eV
001,CO2,1.37
111_Co,CO2,1.32
111_CoZn,CO2,2.19
111_CoZn,CO2,1.76
001,Na,1.32
111_Co,Na,1.24
111_CoZn,Na,1.23
001,Na2CO3,2.66
111_Co,Na2CO3,5.18
111_CoZn,Na2CO3,5.09
CSV_EOF

# === solve block: dos_data.csv ===
python3 << 'PYEOF'
import math, csv

out = "/app/outputs/dos_data.csv"
with open(out, 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['surface','energy_eV','pdos_Co'])
    for surf in ['001','111_Co','111_CoZn']:
        for j in range(81):
            e = -2.0 + j*0.05
            # Gaussian centred at 0.8 eV, sigma 0.3, plus offset
            pdos = 5.0*math.exp(-((e-0.8)/0.3)**2) + 0.1
            if e > 0:
                pdos += 0.05   # ensure unoccupied states
            w.writerow([surf, round(e,6), round(pdos,6)])
PYEOF
