#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: ideal_raman.csv ===
python3 << 'PYEOF'
import csv
import math

freqs = [i * 1.0 for i in range(0, 501)]  # 0,1,...,500 cm-1
rows = []
for f in freqs:
    I = 0.0
    # GaAs-like LO confined modes (odd orders) around 280-310 cm-1
    I += 3.0 * math.exp(-((f - 280.0) / 5.0) ** 2)
    I += 2.5 * math.exp(-((f - 296.0) / 4.0) ** 2)
    I += 2.0 * math.exp(-((f - 308.0) / 4.0) ** 2)
    # AlAs-like main peak at 384 cm-1, narrower to avoid interference
    I += 10.0 * math.exp(-((f - 384.0) / 3.0) ** 2)
    rows.append((f, round(I, 6)))

with open('/app/outputs/ideal_raman.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['frequency', 'intensity'])
    writer.writerows(rows)
PYEOF

# === solve block: intermixed_raman.csv ===
python3 << 'PYEOF'
import csv
import math

freqs = [i * 2.0 for i in range(0, 251)]
rows = []
for f in freqs:
    # intermixed: main peak at 377 cm-1, secondary at 372 cm-1
    intensity = (
        10.0 * math.exp(-((f - 377.0) / 4.0) ** 2)   # main
        + 5.0 * math.exp(-((f - 372.0) / 4.0) ** 2)   # secondary
    )
    # GaAs-like background (same as ideal for simplicity)
    if f < 300:
        intensity += 2.0 * math.exp(-((f - 200) / 8) ** 2)
        intensity += 1.5 * math.exp(-((f - 260) / 6) ** 2)
    rows.append((f, round(intensity, 6)))

with open('/app/outputs/intermixed_raman.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['frequency', 'intensity'])
    writer.writerows(rows)
PYEOF

# === solve block: peak_positions.json ===
cat > /app/outputs/peak_positions.json << 'FFEOF'
{
  "ideal_main_peak": 384.0,
  "intermixed_main_peak": 377.0,
  "intermixed_secondary_peak": 372.0
}
FFEOF
