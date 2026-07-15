#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
export OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: ratios.csv ===
# Write the reference ratios.csv directly from Table V values
python3 << 'PYEOF' > "$OUTDIR/ratios.csv"
import csv, sys

rows = [
    # 3 atm, 1750 K
    (1750, 3, 140.0, 10.0,   0.000364, 0.000832, 8.75, 7.77),
    (1750, 3, 100.0, 50.0,  0.00134,  0.00259,  14.45, 2.11),
    # 3 atm, 2000 K
    (2000, 3, 140.0, 10.0,   0.00487,  0.00545,  5.92, 10.76),
    (2000, 3, 100.0, 50.0,  0.0135,   0.0128,   13.02, 3.94),
    # 3 atm, 2250 K
    (2250, 3, 140.0, 10.0,   0.0396,   0.0254,   4.22, 13.41),
    (2250, 3, 100.0, 50.0,  0.0861,   0.0468,   12.23, 6.55),
    # 70 atm, 1750 K
    (1750, 70, 800.0, 200.0,  0.000938, 0.00960, 15.82, 0.87),
    (1750, 70, 500.0, 500.0,  0.00286,  0.0232,  16.66, 0.29),
    # 70 atm, 2000 K
    (2000, 70, 800.0, 200.0,  0.00875,  0.0438,  15.65, 1.77),
    (2000, 70, 500.0, 500.0,  0.0257,   0.10,    18.08, 0.65),
    # 70 atm, 2250 K
    (2250, 70, 800.0, 200.0,  0.0511,   0.15,    16.64, 3.32),
    (2250, 70, 500.0, 500.0,  0.14,     0.32,    23.18, 1.46),
]

writer = csv.writer(sys.stdout)
writer.writerow(['temperature_K','pressure_atm','H2_mol','H2O_mol','I_CsI','HI_CsI','CsOH_CsI','Cs_CsI'])
for r in rows:
    writer.writerow(r)
PYEOF
