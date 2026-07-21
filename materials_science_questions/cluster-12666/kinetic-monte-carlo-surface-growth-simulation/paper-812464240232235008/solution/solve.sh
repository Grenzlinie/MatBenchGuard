#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs
OUTDIR=/app/outputs

# === solve block: surface_width_without_incorporation.csv ===
python3 -c "
import math, csv
outfile = '$OUTDIR/surface_width_without_incorporation.csv'
with open(outfile, 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['time', 'surface_width'])
    for t in range(10, 1001, 10):
        s = 2.5 * math.sqrt(t)
        w.writerow([t, s])
"

# === solve block: surface_width_with_incorporation.csv ===
python3 /solution/generate_surface_width.py --out "$OUTDIR/surface_width_with_incorporation.csv" --exponent 0.333333 --scale 0.7 --time-step 10 --max-time 1000
