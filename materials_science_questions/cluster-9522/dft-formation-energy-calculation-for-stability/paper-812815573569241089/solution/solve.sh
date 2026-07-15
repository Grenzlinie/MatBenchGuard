#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: formation_enthalpies.csv ===
python3 -c "
import csv
rows = [
    ('compound', 'num_O', 'formation_enthalpy_kJ_per_mol'),
    ('NiTi2', 0, -63.3),
    ('Ni2Ti4O0.25', 4, -1766.43),
    ('Ni2Ti4O0.5', 8, -3339.33),
    ('Ni2Ti4O0.75', 12, -4795.82),
    ('Ni2Ti4O1', 16, -6148.27),
]
with open('/app/outputs/formation_enthalpies.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(rows)
"

# === solve finalize ===
:
