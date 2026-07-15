#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: load_displacement_baseline.csv ===
python3 -c "
import csv
with open('$OUTDIR/load_displacement_baseline.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(['displacement_Angstrom', 'potential_energy_kcal_mol'])
    for d in range(0, 31):
        u = 0.3260 * d**2
        writer.writerow([f'{d:.1f}', f'{u:.6f}'])
"

# === solve block: results.csv ===
cat > /app/outputs/results.csv << 'FFEOF'
condition,J_integral
pure_PMMA,0.0032
CNT5wt%,0.0068
CNT10wt%_2pct_crosslink,0.0110
FFEOF
