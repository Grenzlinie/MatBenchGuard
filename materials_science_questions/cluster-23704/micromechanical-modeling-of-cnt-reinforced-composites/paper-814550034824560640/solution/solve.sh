#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: fe_results.csv ===
python3 > "$OUTDIR/fe_results.csv" <<'PYEOF'
import csv, sys
w = csv.writer(sys.stdout)
w.writerow(["RVE_config", "E_L", "E_T", "G_T", "v_L", "v_T"])
rows = [
    ("1CNT+1Clay", 5.3245, 2.420, 0.7868, 0.3938, 0.5382),
    ("1CNT+2Clay", 7.0019, 2.626, 0.8468, 0.3938, 0.5508),
    ("1CNT+3Clay", 8.6448, 2.8338, 0.9092, 0.3928, 0.5582),
    ("1CNT+4Clay", 10.2846, 3.0908, 0.9929, 0.3917, 0.5564),
    ("1Clay+1CNT", 5.3236, 2.4137, 0.7838, 0.3948, 0.5397),
    ("1Clay+2CNT", 6.9921, 2.4899, 0.7963, 0.3944, 0.5634),
    ("1Clay+3CNT", 8.6552, 2.5700, 0.8164, 0.3940, 0.5753),
    ("1Clay+4CNT", 10.3201, 2.6521, 0.8381, 0.3935, 0.5820),
]
w.writerows(rows)
PYEOF

# === solve block: halpin_tsai_results.csv ===
python3 /solution/halpin_tsai.py > "$OUTDIR/halpin_tsai_results.csv"
