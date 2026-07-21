#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: connection_ratios.csv ===
python3 << 'PYEOF' > "$OUTDIR/connection_ratios.csv"
import csv
rows = [
    {"thickness_um": 2.0, "rc_percent": 100.0, "disconnection": False},
    {"thickness_um": 2.5, "rc_percent": 80.0, "disconnection": True},
    {"thickness_um": 3.0, "rc_percent": 60.0, "disconnection": True},
]
with open("/dev/stdout", "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["thickness_um", "rc_percent", "disconnection"])
    writer.writeheader()
    writer.writerows(rows)
PYEOF
