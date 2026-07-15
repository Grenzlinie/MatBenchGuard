#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: band_gaps.csv ===
python3 <<'PYEOF'
import csv

rows = [
    {"band_gap_eV": 2.60, "band_gap_type": "indirect", "compound_name": "(R)-MBAPbBr3"},
    {"band_gap_eV": 1.95, "band_gap_type": "indirect", "compound_name": "(R)-MBAPbI3"},
    {"band_gap_eV": 1.65, "band_gap_type": "direct",   "compound_name": "(R)-MBA2PbI4"}
]
with open("/app/outputs/band_gaps.csv", "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["band_gap_eV", "band_gap_type", "compound_name"])
    writer.writeheader()
    writer.writerows(rows)
PYEOF
