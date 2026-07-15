#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: step_01_dft_energies.csv ===
cat > /tmp/write_energies.py <<'PYEOF'
import csv

rows = [
    ['material', 'vacancy_site', 'formation_energy_eV'],
    ['SrFeO3', 'V_O1', 2.04],
    ['SrFeO3', 'V_O2', 2.01],
    ['SrFe0.75Cu0.25O3', 'V_O1', 1.85],
    ['SrFe0.75Cu0.25O3', 'V_O2', 1.90],
    ['SrFe0.75Cu0.25O3', 'V_O3', 0.88],
    ['SrFe0.75Cu0.25O3', 'V_O4', 0.92],
]

with open('/app/outputs/step_01_dft_energies.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(rows)
PYEOF
python3 /tmp/write_energies.py
