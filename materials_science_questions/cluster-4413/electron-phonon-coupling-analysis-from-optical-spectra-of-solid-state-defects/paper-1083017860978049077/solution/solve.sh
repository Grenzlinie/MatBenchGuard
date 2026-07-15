#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs
# Make the helper script executable (it is bundled under /solution)
chmod +x /solution/generate_outputs.py

# === solve block: step_06_relaxation_times.csv ===
OUTDIR=/app/outputs python3 -c "
import csv, math
with open('$OUTDIR/step_06_relaxation_times.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['temperature', 'exciton_index', 'relaxation_time'])
    A = [200.0, 150.0, 100.0, 80.0, 50.0]
    B = 0.5
    T0 = [80.0, 90.0, 100.0, 110.0, 120.0]
    for T in range(0, 301, 10):
        for ex in range(1, 6):
            tau = A[ex-1] * math.exp(-T / T0[ex-1]) + B
            w.writerow([T, ex, round(tau, 3)])
"

# === solve block: step_07_linewidth_params.json ===
cat > /app/outputs/step_07_linewidth_params.json <<'FFEOF'
{
  "exciton1": {"SA": 2.27, "SO": 0.10, "EA": 25.0, "EO": 48.1},
  "exciton5": {"gamma0": 29.3, "a": 2.0, "b": 10.0}
}
FFEOF

# === solve block: step_08_pl_spectrum.csv ===
python3 /solution/generate_outputs.py --pl > /app/outputs/step_08_pl_spectrum.csv
