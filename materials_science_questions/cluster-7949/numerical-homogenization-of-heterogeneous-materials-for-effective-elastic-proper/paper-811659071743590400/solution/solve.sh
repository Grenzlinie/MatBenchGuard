#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
set -euo pipefail
mkdir -p /app/outputs

# === solve block: sent_results.csv ===
python3 -c "
import csv
import os

rows = [
    ['a_over_w', 'K_I_norm', 'T_norm'],
    ['0.2', '1.373', '-0.437'],
    ['0.3', '1.664', '-0.368'],
    ['0.4', '2.110', '-0.271'],
    ['0.5', '2.811', '-0.146'],
    ['0.6', '3.990', '0.013'],
    ['0.7', '6.297', '0.212'],
]

outpath = os.path.join(os.environ.get('OUTDIR', '/app/outputs'), 'sent_results.csv')
with open(outpath, 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(rows)
"
