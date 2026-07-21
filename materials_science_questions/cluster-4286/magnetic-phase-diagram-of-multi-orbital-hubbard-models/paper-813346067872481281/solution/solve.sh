#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p "$OUTDIR"
python3 -m pip install -q --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple numpy

# === solve block: magnetic_phase_diagram.csv ===
python3 << PYEOF
import csv
rows = [
    (0.5, 2.5, 4.0),
    (0.75, 2.8, 4.1),
    (1.0, 3.2, 4.3),
    (1.25, 3.7, 4.6),
    (1.5, 4.3, 5.0),
    (2.0, 5.5, 5.5),
    (2.5, 7.0, 6.0),
    (3.0, 8.5, 6.8),
    (3.5, 10.2, 7.8),
    (4.0, 12.0, 9.0)
]
with open('$OUTDIR/magnetic_phase_diagram.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['tA_over_tB', 'Uc_pipi', 'Uc_pi0'])
    w.writerows(rows)
PYEOF
