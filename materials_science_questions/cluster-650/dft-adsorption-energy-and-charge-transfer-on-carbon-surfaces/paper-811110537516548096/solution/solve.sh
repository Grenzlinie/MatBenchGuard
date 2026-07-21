#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
set -euo pipefail
mkdir -p /app/outputs

# === solve block: band_gaps.csv ===
cat > "$OUTDIR/band_gaps.csv" <<'CSVEOF'
system,Eg
pristine,1.23
Cu-I,1.56
Cu-E,1.68
Cu-O,1.45
Ag-I,1.78
Ag-E,1.92
Ag-O,2.05
Au-I,2.23
Au-E,2.41
Au-O,2.62
CSVEOF

# === solve block: adsorption_energies.csv ===
python3 << 'PYEOF'
import csv

hartree = 27.2114
# Table 2 adsorption energies (a.u.)
# (system, Eads_a.u)
au_vals = [
    ('Cu-I', -0.100),
    ('Cu-E', -0.119),
    ('Cu-O', -0.133),
    ('Ag-I', -0.122),
    ('Ag-E', -0.199),
    ('Ag-O', -0.215),
    ('Au-I', -3.288),
    ('Au-E', -3.422),
    ('Au-O', -3.440),
]
rows = [(sys, round(val * hartree, 3)) for sys, val in au_vals]
outfile = '/app/outputs/adsorption_energies.csv'
with open(outfile, 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['system', 'Eads'])
    w.writerows(rows)
PYEOF
