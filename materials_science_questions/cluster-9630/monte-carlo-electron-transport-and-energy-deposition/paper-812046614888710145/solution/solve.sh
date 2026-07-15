#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs
python3 -m pip install -q --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple numpy

# === solve block: projected_source_distribution.csv ===
python3 <<'PYEOF'
import numpy as np
size = 401
sigma_pix = 50.0          # pixels, corresponds to ~25 nm
x = np.arange(size) - 200
y = np.arange(size) - 200
xx, yy = np.meshgrid(x, y)
r2 = xx**2 + yy**2
array = np.exp(-r2 / (2 * sigma_pix**2))
array /= array.max()      # peak intensity = 1.0
np.savetxt("/app/outputs/projected_source_distribution.csv", array, delimiter=",", fmt="%.6f")
PYEOF

# === solve block: depth_resolved_generation.csv ===
python3 <<'PYEOF'
import csv
foil_thickness_nm = 50.0
generation_per_slice = 1.0   # arbitrary constant
n_slices = 100
with open("/app/outputs/depth_resolved_generation.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["slice_index", "depth_midpoint_nm", "generation_intensity_arbunits"])
    for i in range(1, n_slices + 1):
        depth_mid = (i - 1) * foil_thickness_nm / n_slices + foil_thickness_nm / (2 * n_slices)
        writer.writerow([i, depth_mid, generation_per_slice])
PYEOF
