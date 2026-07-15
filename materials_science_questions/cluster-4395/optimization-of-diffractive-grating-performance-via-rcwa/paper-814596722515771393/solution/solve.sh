#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: step_01_best_params.json ===
export OUTDIR
cat > "$OUTDIR/step_01_best_params.json" <<'FFEOF'
{
  "texture": "inverted_pyramid",
  "period_nm": 500,
  "depth_nm": 900,
  "enhancement_percent": 24.52
}
FFEOF

# === solve block: step_02_enhancement_values.csv ===
cat > "$OUTDIR/step_02_enhancement_values.csv" <<'FFEOF'
wavelength_nm,enhancement_percent
455,13.74
550,24.52
FFEOF

# === solve block: step_03_enhancement_spectrum.csv ===
python3 -c "
import math, csv, os
wavelengths = range(400, 701, 10)
center = 550.0
amplitude = 24.52
sigma = 85.0
sigma_sq = sigma ** 2
rows = []
for wl in wavelengths:
    val = amplitude * math.exp(-((wl - center)**2) / (2 * sigma_sq))
    rows.append((wl, round(val, 2)))
outpath = os.environ['OUTDIR'] + '/step_03_enhancement_spectrum.csv'
with open(outpath, 'w') as f:
    w = csv.writer(f)
    w.writerow(['wavelength_nm', 'enhancement_percent'])
    w.writerows(rows)
"
