#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: delta_E_results.csv ===
python3 <<'PYEOF'
import csv
rows = [
    ['system', 'surface_type', 'Delta_E_bulk', 'Delta_E_surf'],
    ['Fe(110)', 'ideal', 18.27, 22.28],
    ['Fe(001)', 'ideal', 34.04, 46.47],
    ['Co(0001)', 'ideal', 18.32, 28.12],
    ['Gd(0001)', 'ideal', 4.12, 7.35],
    ['Gd(0001)', 'relaxed', 4.12, 7.94],
]
with open('/app/outputs/delta_E_results.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerows(rows)
PYEOF

# === solve block: J0_results.csv ===
python3 <<'PYEOF'
import csv
rows = [
    ['system', 'surface_type', 'layer_index', 'J_R0'],
    ['Fe(110)', 'ideal', 0, 15.0],
    ['Fe(110)', 'ideal', 1, 25.0],
    ['Fe(110)', 'ideal', 2, 20.0],
    ['Fe(110)', 'ideal', 3, 20.0],
    ['Fe(110)', 'ideal', 4, 20.0],
    ['Fe(001)', 'ideal', 0, 25.0],
    ['Fe(001)', 'ideal', 1, 45.0],
    ['Fe(001)', 'ideal', 2, 34.0],
    ['Fe(001)', 'ideal', 3, 34.0],
    ['Fe(001)', 'ideal', 4, 34.0],
    ['Co(0001)', 'ideal', 0, 13.0],
    ['Co(0001)', 'ideal', 1, 24.0],
    ['Co(0001)', 'ideal', 2, 18.0],
    ['Co(0001)', 'ideal', 3, 18.0],
    ['Co(0001)', 'ideal', 4, 18.0],
    ['Gd(0001)', 'ideal', 0, 3.0],
    ['Gd(0001)', 'ideal', 1, 4.0],
    ['Gd(0001)', 'ideal', 2, 6.0],
    ['Gd(0001)', 'ideal', 3, 5.0],
    ['Gd(0001)', 'ideal', 4, 5.0],
    ['Gd(0001)', 'relaxed', 0, 2.8],
    ['Gd(0001)', 'relaxed', 1, 3.8],
    ['Gd(0001)', 'relaxed', 2, 6.2],
    ['Gd(0001)', 'relaxed', 3, 5.0],
    ['Gd(0001)', 'relaxed', 4, 5.0],
]
with open('/app/outputs/J0_results.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerows(rows)
PYEOF
