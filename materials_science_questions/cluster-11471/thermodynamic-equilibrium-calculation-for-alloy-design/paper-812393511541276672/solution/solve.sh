#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: table1_depressions.csv ===
python3 - <<'PYEOF'
import csv
rows = [
    ('Ni_wtPct','T_50kbar_C'),
    (0,652),
    (10,510),
    (20,415),
    (30,385),
    (40,380),
    (50,365),
    (55,350),
    (60,335),
]
with open('/app/outputs/table1_depressions.csv','w',newline='') as f:
    w = csv.writer(f)
    w.writerows(rows)
PYEOF

# === solve block: eutectoid_check.txt ===
echo 'Eutectoid present at 50 kbars: NO' > /app/outputs/eutectoid_check.txt
