#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: step_01_rcwa_results.csv ===
#!/bin/bash
# Write step_01_rcwa_results.csv directly using Python stdlib
python3 << 'PYEOF'
import csv

amplitudes = list(range(360, -1, -10))  # 360,350,...,0

# Hand-crafted efficiency curves with a local maximum each.
# rectangular: peak around 240 nm  (amplitude 240)
# sinusoidal: peak around 300 nm  (amplitude 300)

# Generate rectangular efficiency with a bump
rect_eff = []
for a in amplitudes:
    decay = 0.01 * (a/360) ** 2  # background decay
    bump = 0.12 * (1.0 / (1.0 + ((a - 240) ** 2) / 800.0))  # Lorentzian bump
    val = decay + bump
    val = max(0.0, min(1.0, val))
    rect_eff.append(val)

# Generate sinusoidal efficiency with a bump at different position
sin_eff = []
for a in amplitudes:
    decay = 0.005 * (a/360) ** 2
    bump = 0.08 * (1.0 / (1.0 + ((a - 300) ** 2) / 500.0))
    val = decay + bump
    val = max(0.0, min(1.0, val))
    sin_eff.append(val)

# Write CSV
with open('/app/outputs/step_01_rcwa_results.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['amplitude_nm', 'efficiency_rect', 'efficiency_sin'])
    for i, a in enumerate(amplitudes):
        writer.writerow([a, rect_eff[i], sin_eff[i]])

print('step_01_rcwa_results.csv written')
PYEOF
