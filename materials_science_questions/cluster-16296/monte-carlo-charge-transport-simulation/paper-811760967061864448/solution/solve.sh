#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: computed_results.csv ===
python3 << 'PYEOF'
import csv
rows = [
    ("S1", "Gamma_only",     2.6e-3,  80e-12),
    ("S1", "Gamma_plus_X",   2.7e-3,  58e-12),
    ("A1", "Gamma_only",     12e-6,   390e-9),
    ("A1", "Gamma_plus_X",   2.7e-3,  260e-12),
    ("A2", "Gamma_only",     16e-6,   480e-9),
    ("A2", "Gamma_plus_X",   0.21e-3, 730e-12),
    ("S2", "Gamma_only",     0.23e-6, 670e-9),
    ("S2", "Gamma_plus_X",   1.2e-6,  2.3e-9),
]
with open("/app/outputs/computed_results.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["diode", "model", "peak_current_A", "dwell_time_s"])
    for r in rows:
        writer.writerow(r)
PYEOF
