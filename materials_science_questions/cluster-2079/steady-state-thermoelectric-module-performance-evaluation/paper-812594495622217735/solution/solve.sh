#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: temperature_profile.csv ===
cat > /app/outputs/temperature_profile.csv <<'EOF'
length_m,temperature_K
0.000,300.0
0.007,236.0
0.587,125.0
0.987,78.0
EOF
python3 -c "
import csv, sys
points = []
with open('/app/outputs/temperature_profile.csv', 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        points.append((float(row['length_m']), float(row['temperature_K'])))
xs, ts = zip(*points)
N = 1000
total_len = xs[-1]
with open('/app/outputs/temperature_profile.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(['length_m', 'temperature_K'])
    for i in range(N):
        x = i * total_len / (N-1)
        # piecewise linear interpolation
        if x <= xs[1]:
            seg = 0
        elif x <= xs[2]:
            seg = 1
        else:
            seg = 2
        x0, x1 = xs[seg], xs[seg+1]
        t0, t1 = ts[seg], ts[seg+1]
        t = t0 + (t1 - t0) * (x - x0) / (x1 - x0) if x1 != x0 else t0
        writer.writerow([round(x, 6), round(t, 2)])
"

# === solve block: heat_load_summary.json ===
cat > /app/outputs/heat_load_summary.json <<'EOF'
{
  "current_kA": 10,
  "warm_end_heat_load_W": 557,
  "peltier_cooling_power_W": 390,
  "pe_cui_interface_heat_W": 27,
  "joule_cui_W": 286,
  "intercepted_by_lp_W": 167,
  "joule_cuii_W": 59,
  "cold_end_heat_load_W": 205
}
EOF

# === solve block: zero_current_cold_end_heat_load.json ===
cat > /app/outputs/zero_current_cold_end_heat_load.json <<'EOF'
{
  "cold_end_heat_load_W": 140
}
EOF
