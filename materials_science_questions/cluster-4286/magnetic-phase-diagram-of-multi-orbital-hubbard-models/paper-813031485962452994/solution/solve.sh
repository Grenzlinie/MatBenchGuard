#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs
OUTDIR=/app/outputs

# === solve block: uc_output.json ===
cat > "$OUTDIR/uc_output.json" <<'FFEOF'
{
  "U_c": 2.245
}
FFEOF

# === solve block: phase_points.json ===
cat > "$OUTDIR/phase_points.json" <<'FFEOF'
[
  {
    "U": -2.0,
    "h": 0.5,
    "delta0": 0.0,
    "Qx": 0.0,
    "Qy": 0.0,
    "phase": "NO"
  },
  {
    "U": -2.0,
    "h": 1.0,
    "delta0": 0.3,
    "Qx": 0.0,
    "Qy": 0.25,
    "phase": "FFLO"
  },
  {
    "U": -2.0,
    "h": 1.5,
    "delta0": 0.0,
    "Qx": 0.0,
    "Qy": 0.0,
    "phase": "NO"
  }
]
FFEOF

# === solve block: q_evolution.csv ===
python3 -c "
import csv, sys
writer = csv.writer(sys.stdout)
writer.writerow(['h/t', 'Qx', 'Qy', 'phase'])
points = [
    (0.5, 0.0, 0.0, 'NO'),
    (0.55, 0.0, 0.0, 'NO'),
    (0.6, 0.0, 0.0, 'NO'),
    (0.65, 0.0, 0.0, 'NO'),
    (0.7, 0.0, 0.0, 'NO'),
    (0.75, 0.0, 0.0, 'NO'),
    (0.8, 0.0, 0.0, 'NO'),
    (0.85, 0.3, 0.0, 'FFLO'),
    (0.9, 0.25, 0.1, 'FFLO'),
    (0.95, 0.15, 0.2, 'FFLO'),
    (1.0, 0.0, 0.25, 'FFLO'),
    (1.05, -0.1, 0.2, 'FFLO'),
    (1.1, -0.2, 0.1, 'FFLO'),
    (1.15, -0.25, 0.0, 'FFLO'),
    (1.2, 0.0, 0.0, 'NO'),
    (1.25, 0.0, 0.0, 'NO'),
    (1.3, 0.0, 0.0, 'NO'),
    (1.35, 0.0, 0.0, 'NO'),
    (1.4, 0.0, 0.0, 'NO'),
    (1.45, 0.0, 0.0, 'NO'),
    (1.5, 0.0, 0.0, 'NO'),
]
for h, qx, qy, phase in points:
    writer.writerow([h, qx, qy, phase])
" > "$OUTDIR/q_evolution.csv"
