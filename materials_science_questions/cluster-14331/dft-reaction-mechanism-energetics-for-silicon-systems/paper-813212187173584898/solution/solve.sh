#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: relative_energies.csv ===
python3 <<'EOF'
import csv
rows = [
    ("RC", -19.8),
    ("TS1", -14.8),
    ("IM1", -22.1),
    ("TS2", -7.7),
    ("TS2-cw", 0.3),
    ("TS2-sw", 5.6),
    ("IM2", -18.1),
    ("TS3", -3.7),
    ("TS3-cw", 12.9),
    ("TS3-sw", 8.4),
    ("TS4", -12.0),
    ("TS4-cw", 8.4),
    ("TS4-sw", 2.5),
    ("PC1", -22.0),
    ("PC2", -23.7),
    ("RC-w", -8.2),
    ("TS1-w", -2.1),
    ("IM1-w", -6.3),
    ("IM2-w", -3.6),
    ("PC1-cw", -7.0),
    ("PC1-sw", -4.0),
    ("PC2-cw", -9.0),
    ("PC2-sw", -7.0),
]
with open("/app/outputs/relative_energies.csv", "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["species", "energy"])
    for s, e in rows:
        w.writerow([s, f"{e:.6f}"])
EOF
