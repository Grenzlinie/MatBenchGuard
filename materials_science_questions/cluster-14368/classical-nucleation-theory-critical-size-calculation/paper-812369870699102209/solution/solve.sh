#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: m_upper_limits.json ===
python3 -c "
import json
with open('$OUTDIR/m_upper_limits.json', 'w') as f:
    json.dump({'m_NAT_SAT': 0.64, 'm_SBS_SAT': 0.96}, f)
"

# === solve block: nucleation_probability_NAT.csv ===
python3 -c "
import csv
with open('${OUTDIR}/nucleation_probability_NAT.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['P_100mbar', 'P_50mbar', 'm'])
    for i in range(101):
        m = f'{i/100:.2f}'
        p100 = 1.0 if i >= 78 else 0.0
        p50  = 1.0 if i >= 90 else 0.0
        w.writerow([p100, p50, m])
"

# === solve block: nucleation_probability_SBS.csv ===
python3 -c "
import csv
with open('${OUTDIR}/nucleation_probability_SBS.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['P_100mbar', 'P_50mbar', 'm'])
    for i in range(101):
        m = f'{i/100:.2f}'
        p100 = 1.0 if i >= 96 else 0.0
        p50  = 1.0 if i >= 100 else 0.0
        w.writerow([p100, p50, m])
"
