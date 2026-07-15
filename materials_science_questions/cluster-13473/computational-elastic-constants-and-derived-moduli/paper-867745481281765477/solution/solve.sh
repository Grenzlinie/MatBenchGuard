#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
export OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: mueff_table.csv ===
python3 -c "
import csv
with open('$OUTDIR/mueff_table.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['Gamma','b11','c44','mueff','uncertainty_mueff'])
    w.writerow(['inf',0.0220,0.1699,0.1107,0.0])
    w.writerow([834,0.0209,0.1617,0.1054,0.002])
    w.writerow([200,0.0154,0.1253,0.0813,0.006])
"
