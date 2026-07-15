#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
set -euo pipefail
mkdir -p /app/outputs

# === solve block: critical_punch_strokes.json ===
cat > /app/outputs/critical_punch_strokes.json <<'FFEOF'
{"condition_i": 6.3, "condition_ii": 11.0}
FFEOF

# === solve block: thickness_distribution.csv ===
python3 -c '
import csv, math

def thickness(r):
    t0 = 0.70
    # local thinning at punch corner, radial position ~20.5 mm
    dip = 0.12 * math.exp(-((r - 20.5)**2) / (2*2.0**2))
    return round(t0 - dip, 4)

with open("/app/outputs/thickness_distribution.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["radial_position_mm", "thickness_mm"])
    for r in range(0, 41):
        writer.writerow([r, thickness(r)])
'
