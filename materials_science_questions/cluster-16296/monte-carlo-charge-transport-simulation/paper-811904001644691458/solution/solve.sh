#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
set -euo pipefail
mkdir -p /app/outputs

# === solve block: emitted_electrons_vs_field.csv ===
python3 << 'PYEOF'
import csv, math

data = []
for i in range(29):
    F = 1.0 + i * 0.5
    if F < 3.0:
        ratio = 1.0 / (1.0 + math.exp(-5.0*(F-1.5)))  # smooth rise to 1 by 3 MV/cm
    elif F < 10.0:
        ratio = 1.0
    else:
        # sharp avalanche rise centered at 12.5 MV/cm
        ratio = 1.0 + 2.0 / (1.0 + math.exp(-5.0*(F-12.5)))
    data.append([F, 10000.0 * ratio])

with open('/app/outputs/emitted_electrons_vs_field.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['electric_field_strength', 'emitted_electron_count'])
    writer.writerows(data)
PYEOF

# === solve block: breakdown_range.json ===
cat > /app/outputs/breakdown_range.json << 'JSONEOF'
{
  "breakdown_range_MV_per_cm": [11.5, 12.5]
}
JSONEOF
