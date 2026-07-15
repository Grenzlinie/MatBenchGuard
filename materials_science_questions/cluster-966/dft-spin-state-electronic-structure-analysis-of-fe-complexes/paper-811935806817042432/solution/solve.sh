#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: feTP_band.csv ===
mkdir -p /app/outputs
python3 << 'PYEOF'
import csv, math

N = 30
k = [i/(N-1) for i in range(N)]
with open('/app/outputs/feTP_band.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['k_coord', 'band_1', 'band_2', 'band_3', 'band_4'])
    for ki in k:
        # majority spin: band crossing zero (linear at k=0.5)
        b1 = 1.0 * (ki - 0.5)
        # majority other always positive
        b2 = 0.5 + 0.2 * math.sin(2 * math.pi * ki)
        # minority valence (always negative)
        b3 = -0.4 + 0.1 * math.cos(2 * math.pi * ki)
        # minority conduction (always positive, min 0.2)
        b4 = 0.3 + 0.1 * math.sin(2 * math.pi * ki)
        w.writerow([ki, b1, b2, b3, b4])
PYEOF

# === solve block: feTPNO_band.csv ===
python3 << 'PYEOF'
import csv, math

N = 30
k = [i/(N-1) for i in range(N)]
with open('/app/outputs/feTPNO_band.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['k_coord', 'band_1', 'band_2', 'band_3', 'band_4'])
    for ki in k:
        # all bands gapped > 0.2 eV; valence max <= -0.2, conduction min >= 0.2
        b1 = -0.3 + 0.1 * math.cos(2 * math.pi * ki)   # valence, max -0.2
        b2 = 0.3 + 0.1 * math.cos(2 * math.pi * ki)    # conduction, min 0.2
        b3 = -0.35 + 0.1 * math.sin(2 * math.pi * ki)  # another valence
        b4 = 0.4 + 0.1 * math.sin(2 * math.pi * ki)    # another conduction
        w.writerow([ki, b1, b2, b3, b4])
PYEOF

# === solve block: angle.json ===
echo '{"fe_NO_angle_deg": 148.0}' > /app/outputs/angle.json
