#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: transition_data.csv ===
cat > /app/outputs/transition_data.csv << 'EOF'
composition_x,transition_pressure_GPa,volume_collapse_percent
0.0,10,8.1
0.2,11,8.5
0.55,12.2,7.8
0.81,12.8,8.4
0.93,13,8.3
1.0,13.8,7.6
EOF

# === solve block: elastic_constants_B3.csv ===
cat > /app/outputs/elastic_constants_B3.csv << 'EOF'
composition_x,B_T_GPa,C44_GPa,C_s_GPa
0.0,129.8,103.1,39.9
0.2,132,104,40.9
0.55,146.5,114.2,41.1
0.81,154.9,118.8,41.4
0.93,163.3,122.6,41.7
1.0,156.5,104.2,52.5
EOF

# === solve block: soec_vs_pressure.csv ===
python3 << 'PYEOF'
import csv

pressures = list(range(0, 21))
rows = []
for P in pressures:
    if P < 10:
        C11 = 100 + 5 * P
        C12 = 50 + 3 * P
        C44 = 60 + 2 * P
    elif P == 10:
        # discontinuity at the B3→B1 transition
        C11 = 100 + 5 * 10 + 15
        C12 = 50 + 3 * 10 + 10
        C44 = 60 + 2 * 10 + 10
    else:
        C11 = 100 + 5 * 10 + 15 + 5 * (P - 10)
        C12 = 50 + 3 * 10 + 10 + 3 * (P - 10)
        C44 = 60 + 2 * 10 + 10 + 2 * (P - 10)
    rows.append([P, C11, C12, C44])

with open('/app/outputs/soec_vs_pressure.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['pressure_GPa', 'C11_GPa', 'C12_GPa', 'C44_GPa'])
    w.writerows(rows)
PYEOF
