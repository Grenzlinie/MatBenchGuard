#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: phonon_frequencies.csv ===
python3 <<'PYEOF'
import csv

rows = [
    ("Ag", 63.7),
    ("Ag", 82.1),
    ("Ag", 114.1),
    ("Ag", 125.5),
    ("B1g", 31.3),
    ("B1g", 63.8),
    ("B1g", 124.9),
    ("B1g", 158.5),
    ("B3g", 31.4),
    ("B3g", 64.2),
    ("B3g", 124.7),
    ("B3g", 157.3),
]

with open("/app/outputs/phonon_frequencies.csv", "w", newline='') as f:
    writer = csv.writer(f)
    writer.writerow(["symmetry", "frequency"])
    writer.writerows(rows)
PYEOF
