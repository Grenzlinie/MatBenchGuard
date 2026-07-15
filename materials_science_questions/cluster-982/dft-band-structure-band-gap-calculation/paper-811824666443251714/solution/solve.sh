#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
export OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: equilibrium_properties.csv ===
cat > "$OUTDIR/equilibrium_properties.csv" <<'CSVEOF'
compound,V0_pfu_AA3,B0_GPa
HgSe,56.23,57
HgTe,67.03,47
CSVEOF

# === solve block: phonon_frequencies.csv ===
python3 -c "
import csv
with open('$OUTDIR/phonon_frequencies.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['compound','pressure_condition','frequency_TO_Gamma_THz','frequency_TA_X_THz'])
    w.writerow(['HgSe', '0_GPa', 4.00, 1.5])
    w.writerow(['HgSe', '3_GPa', 4.20, -0.5])
    w.writerow(['HgTe', '0_GPa', 3.54, 1.3])
    w.writerow(['HgTe', '3_GPa', 3.70, -0.4])
"
