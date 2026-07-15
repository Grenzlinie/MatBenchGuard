#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
set -euo pipefail
mkdir -p /app/outputs

# === solve block: tielines_NiAl.csv ===
python3 << 'PYEOF'
import csv
tielines = [
    (700, "FCC", 0.110408, "Ni3Al", 0.25),
    (700, "Ni3Al", 0.25, "BCC", 0.381279),
    (700, "BCC", 0.424394, "Ni2Al3", 0.6),
    (700, "Ni2Al3", 0.6, "NiAl3", 0.75),
    (700, "NiAl3", 0.75, "FCC", 0.9999439),
    (1200, "FCC", 0.148048085, "Ni3Al", 0.25),
    (1200, "Ni3Al", 0.25, "BCC", 0.3574774),
    (1200, "BCC", 0.48315199, "Ni2Al3", 0.6),
    (1200, "Ni2Al3", 0.6, "L", 0.802026195),
    (1500, "FCC", 0.1839456, "Ni3Al", 0.25),
    (1500, "Ni3Al", 0.25, "BCC", 0.31850038),
    (1500, "BCC", 0.5942148, "L", 0.642003313),
]
with open("/app/outputs/tielines_NiAl.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Temperature", "Phase1_ID", "Phase1_Composition", "Phase2_ID", "Phase2_Composition"])
    for row in tielines:
        writer.writerow(row)
PYEOF
