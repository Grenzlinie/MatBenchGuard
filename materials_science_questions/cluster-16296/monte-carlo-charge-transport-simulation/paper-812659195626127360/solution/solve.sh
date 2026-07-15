#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: predicted_iv_parameters.csv ===
# Write predicted I-V parameters from paper Table II.
cat > /tmp/write_iv.py << 'PYEOF'
import csv

header = [
    "well_doping",
    "peak_pos_mV",
    "valley_pos_mV",
    "peak_current_Acm2",
    "valley_current_Acm2",
    "peak_to_valley_ratio"
]

rows = [
    {"well_doping": "n-type", "peak_pos_mV": 130, "valley_pos_mV": 220,
     "peak_current_Acm2": 7800, "valley_current_Acm2": 650,
     "peak_to_valley_ratio": 12.0},
    {"well_doping": "undoped", "peak_pos_mV": 160, "valley_pos_mV": 250,
     "peak_current_Acm2": 7500, "valley_current_Acm2": 850,
     "peak_to_valley_ratio": 8.8},
    {"well_doping": "p-type", "peak_pos_mV": 180, "valley_pos_mV": 280,
     "peak_current_Acm2": 7000, "valley_current_Acm2": 740,
     "peak_to_valley_ratio": 9.4}
]

with open("/app/outputs/predicted_iv_parameters.csv", "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=header)
    writer.writeheader()
    writer.writerows(rows)
PYEOF

python3 /tmp/write_iv.py
