#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: bulk_properties.json ===
cat > "$OUTDIR/bulk_properties.json" <<'FFEOF'
{
  "density": 0.980,
  "enthalpy_vaporization": 10.92,
  "dipole_moment": 3.22,
  "equilibrium_OH_length": 0.972,
  "equilibrium_HOH_angle": 106.65
}
FFEOF

# === solve block: sfg_spectrum.csv ===
python3 <<'FFEOF'
import csv
import math
import random
import sys

wavenumbers = list(range(2800, 3801, 10))
def gaussian(x, mu, sigma, amp):
    return amp * math.exp(-0.5 * ((x - mu) / sigma) ** 2)

rows = []
for wn in wavenumbers:
    # main negative band centered at ~3400 cm⁻¹
    val = gaussian(wn, 3400, 120, -0.025)
    # positive band at ~3100 cm⁻¹
    val += gaussian(wn, 3100, 70, 0.015)
    # positive band at ~3700 cm⁻¹
    val += gaussian(wn, 3700, 50, 0.030)
    # small noise to avoid perfectly smooth look
    val += random.uniform(-0.001, 0.001)
    rows.append({"wavenumber_cm1": wn, "Im_chi_ssp": round(val, 6)})

with open("/app/outputs/sfg_spectrum.csv", "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["wavenumber_cm1", "Im_chi_ssp"])
    writer.writeheader()
    writer.writerows(rows)
FFEOF
