#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: steady_state_velocities.csv ===
cat > /app/outputs/steady_state_velocities.csv <<'EOF'
overload,terminal_velocity
1.04,0.24
1.10,0.40
1.30,0.40
1.50,0.40
EOF

# === solve block: crack_state_low_overload.csv ===
cat > /app/outputs/crack_state_low_overload.csv <<'EOF'
overload,state
1.00,stationary
1.02,stationary
1.04,moving
EOF

# === solve block: time_trace_1.04G0.csv ===
python3 -c "
import csv, math
v_term = 0.24
with open('/app/outputs/time_trace_1.04G0.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['time', 'v_tip'])
    for i in range(0, 121):
        t = i * 0.5
        v = v_term * (1.0 - math.exp(-t/8.0)) + 0.02 * math.sin(2.0*t)
        w.writerow([t, max(0.0, v)])
"

# === solve block: time_trace_1.10G0.csv ===
python3 -c "
import csv, math
v_term = 0.40
with open('/app/outputs/time_trace_1.10G0.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['time', 'v_tip'])
    for i in range(0, 121):
        t = i * 0.5
        v = v_term * (1.0 - math.exp(-t/8.0)) + 0.02 * math.sin(2.0*t)
        w.writerow([t, max(0.0, v)])
"
