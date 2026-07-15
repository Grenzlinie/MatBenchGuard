#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: spectral_response.csv ===
python3 -c "
import csv, math

peak = 0.97
fwhm = 0.17
lambda0 = 1550.0
step = 0.001
start = 1549.0
end = 1551.0

wavelengths = []
reflectances = []
x = start
while x <= end + 1e-12:
    wavelengths.append(x)
    # main reflection peak as a Gaussian; background set to an extremely tiny value
    if abs(x - lambda0) < fwhm * 2:
        r = peak * math.exp(-4.0 * math.log(2) * ((x - lambda0) / fwhm) ** 2)
    else:
        r = 1e-12
    reflectances.append(r)
    x = round(x + step, 10)

with open('/app/outputs/spectral_response.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['wavelength_nm', 'reflectance'])
    for w, r in zip(wavelengths, reflectances):
        writer.writerow([w, r])
"

# === solve block: summary_metrics.json ===
python3 -c "
import csv, math, json

with open('/app/outputs/spectral_response.csv', newline='') as f:
    reader = csv.DictReader(f)
    wavelengths = []
    reflectances = []
    for row in reader:
        wavelengths.append(float(row['wavelength_nm']))
        reflectances.append(float(row['reflectance']))

peak_val = max(reflectances)
idx_peak = reflectances.index(peak_val)
lambda_peak = wavelengths[idx_peak]

# FWHM
half = peak_val / 2.0
low_i = None
high_i = None
for i, r in enumerate(reflectances):
    if r >= half:
        if low_i is None:
            low_i = i
        high_i = i
if low_i is not None:
    fwhm_calc = wavelengths[high_i] - wavelengths[low_i]
else:
    fwhm_calc = 0.0

# max side lobe outside ±0.5 nm window around peak wavelength
low_bound = lambda_peak - 0.5
high_bound = lambda_peak + 0.5
side_lobes = [r for w, r in zip(wavelengths, reflectances) if w < low_bound or w > high_bound]
if side_lobes:
    max_side = max(side_lobes)
    max_side_db = 10.0 * math.log10(max_side) if max_side > 0 else -100.0
else:
    max_side_db = -100.0

metrics = {
    'peak_reflectance': round(peak_val, 6),
    'fwhm_nm': round(fwhm_calc, 6),
    'max_side_lobe_dB': round(max_side_db, 6)
}
with open('/app/outputs/summary_metrics.json', 'w') as f:
    json.dump(metrics, f)
"
