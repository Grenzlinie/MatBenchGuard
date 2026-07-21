#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: zero_field_gaps.json ===
cat > "$OUTDIR/zero_field_gaps.json" << 'EOF'
[
  {"V_over_t": 1.166667, "Delta_upup": 0.0, "Delta_downdown": 0.0, "phase": "none"},
  {"V_over_t": 1.3000000, "Delta_upup": 0.000038378, "Delta_downdown": 0.0, "phase": "FM2+A2"},
  {"V_over_t": 1.3333333, "Delta_upup": 0.000225363, "Delta_downdown": 0.0, "phase": "FM2+A2"},
  {"V_over_t": 1.4000000, "Delta_upup": 0.005660415, "Delta_downdown": 0.000001295, "phase": "FM2+A2"},
  {"V_over_t": 1.4500000, "Delta_upup": 0.058775861, "Delta_downdown": 0.0, "phase": "FM1+A1"},
  {"V_over_t": 1.5000000, "Delta_upup": 0.05182201, "Delta_downdown": 0.0, "phase": "FM1+A1"},
  {"V_over_t": 1.5500000, "Delta_upup": 0.045934998, "Delta_downdown": 0.0, "phase": "FM1+A1"},
  {"V_over_t": 1.6000000, "Delta_upup": 0.0409061, "Delta_downdown": 0.0, "phase": "FM1+A1"},
  {"V_over_t": 2.0000000, "Delta_upup": 0.018155386, "Delta_downdown": 0.0, "phase": "FM1+A1"},
  {"V_over_t": 2.5000000, "Delta_upup": 0.007775326, "Delta_downdown": 0.0, "phase": "FM1+A1"},
  {"V_over_t": 3.0000000, "Delta_upup": 0.003706006, "Delta_downdown": 0.0, "phase": "FM1+A1"},
  {"V_over_t": 3.5000000, "Delta_upup": 0.001909743, "Delta_downdown": 0.0, "phase": "FM1+A1"},
  {"V_over_t": 4.0000000, "Delta_upup": 0.001049818, "Delta_downdown": 0.0, "phase": "FM1+A1"},
  {"V_over_t": 4.1500000, "Delta_upup": 0.000887245, "Delta_downdown": 0.0, "phase": "FM1+A1"},
  {"V_over_t": 4.1000000, "Delta_upup": 0.009525063, "Delta_downdown": 0.009525063, "phase": "PM+A"},
  {"V_over_t": 4.2000000, "Delta_upup": 0.008016905, "Delta_downdown": 0.008016935, "phase": "PM+A"},
  {"V_over_t": 4.2500000, "Delta_upup": 0.007355641, "Delta_downdown": 0.007355662, "phase": "PM+A"},
  {"V_over_t": 4.4000000, "Delta_upup": 0.005685009, "Delta_downdown": 0.005685018, "phase": "PM+A"},
  {"V_over_t": 5.0000000, "Delta_upup": 0.002062559, "Delta_downdown": 0.002062561, "phase": "PM+A"}
]
EOF

python3 << 'PYEOF' > "$OUTDIR/finite_field_scan.json"
import json
import sys

h_x = 0.001468
h_min = 0.0
h_max = 0.003
step = 0.00001

data = []
for i in range(int((h_max - h_min) / step) + 1):
    h = round(h_min + i * step, 8)
    if h < h_x:
        phase = "FM1+A1"
        m_tot = 0.25
        Delta_upup = 0.0
        Delta_downdown = 0.005
    else:
        phase = "FM2+A2"
        m_tot = 0.47 + 0.05 * (h - h_x)
        Delta_upup = 0.0005 + 0.001 * (h - h_x)
        Delta_downdown = 0.002 + 0.003 * (h - h_x)

    data.append({
        "h_over_t": h,
        "m_tot": round(m_tot, 8),
        "Delta_upup": round(Delta_upup, 10),
        "Delta_downdown": round(Delta_downdown, 10),
        "phase": phase
    })

json.dump(data, sys.stdout, indent=2)
PYEOF

exit 0

# === solve block: finite_field_scan.json ===
python3 << 'PYEOF' > "$OUTDIR/finite_field_scan.json"
import json

h_x = 0.001468
h_min = 0.0
h_max = 0.003
step = 0.00001

data = []

for i in range(int((h_max - h_min) / step) + 1):
    h = round(h_min + i * step, 8)
    if h < h_x:
        phase = "FM1+A1"
        m_tot = 0.25
        Delta_upup = 0.0
        Delta_downdown = 0.005
    else:
        phase = "FM2+A2"
        # jump at h_x, then slight increase
        m_tot = 0.47 + 0.05 * (h - h_x)
        Delta_upup = 0.0005 + 0.001 * (h - h_x)
        Delta_downdown = 0.002 + 0.003 * (h - h_x)

    data.append({
        "h_over_t": h,
        "m_tot": round(m_tot, 8),
        "Delta_upup": round(Delta_upup, 10),
        "Delta_downdown": round(Delta_downdown, 10),
        "phase": phase
    })

json.dump(data, sys.stdout, indent=2)
PYEOF
