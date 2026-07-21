#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: elastic_limits.csv ===
python3 <<'PYEOF'
import os, csv
rows = [
    ["(010)90°", 0.6e-5],
    ["(010)0°", 6.9e-8],
    ["(111)0°half", 2.1e-4],
    ["(111)120°half", 5.7e-4],
    ["(111)90°", 2.6e-4],
    ["(111)30°", 3.0e-5],
]
with open('/app/outputs/elastic_limits.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(rows)
PYEOF
