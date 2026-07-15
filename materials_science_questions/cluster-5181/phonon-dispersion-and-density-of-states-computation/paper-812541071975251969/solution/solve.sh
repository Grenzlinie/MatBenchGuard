#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# Write the generator script
cat > /tmp/gen_nwpdos.py <<'PYEOF'
import sys, csv, json, math

# Peak parameters for ordered and disordered models
ORDERED_PEAKS = [
    (98.0, 0.50, 5.0),
    (102.0, 0.55, 5.0),
    (162.0, 0.90, 5.0),
    (200.0, 0.65, 6.0),
    (236.0, 0.75, 5.0),
    (251.0, 1.00, 5.0),
]

DISORDERED_PEAKS = [
    (98.0, 0.50, 5.0),
    (102.0, 0.55, 5.0),
    (165.0, 0.90, 5.0),   # shifted up slightly
    (200.0, 0.50, 6.0),   # reduced ~23%
    (236.0, 0.60, 5.0),   # reduced ~20%
    (251.0, 0.90, 5.0),   # reduced 10%
]

def gaussian(x, center, height, sigma):
    return height * math.exp(-0.5 * ((x - center) / sigma) ** 2)

def generate_nwpdos(peaks, xmin=0, xmax=400, step=1.0):
    data = []
    x = xmin
    while x <= xmax:
        y = sum(gaussian(x, c, h, s) for c, h, s in peaks)
        data.append((x, y))
        x += step
    return data

def local_maxima(xy, min_height=0.01, min_distance=5):
    """Find local maxima in xy data."""
    peaks = []
    n = len(xy)
    for i in range(1, n-1):
        if xy[i][1] > xy[i-1][1] and xy[i][1] > xy[i+1][1]:
            if xy[i][1] > min_height:
                peaks.append(xy[i])
    # filter by min_distance
    filtered = []
    for p in sorted(peaks, key=lambda p: p[1], reverse=True):
        if all(abs(p[0] - fp[0]) >= min_distance for fp in filtered):
            filtered.append(p)
    filtered.sort(key=lambda p: p[0])
    return filtered

def get_band_peaks(xy, windows):
    """For each energy window (lo,hi), return the highest local maximum."""
    all_peaks = local_maxima(xy)
    bands = []
    for lo, hi in windows:
        best = None
        for p in all_peaks:
            if lo <= p[0] <= hi:
                if best is None or p[1] > best[1]:
                    best = p
        if best:
            bands.append(best)
    return bands

def relative_intensities(peaks):
    if not peaks:
        return []
    max_h = max(p[1] for p in peaks)
    return [{"peak_cm1": round(p[0], 2), "relative_intensity": round(p[1]/max_h, 4)} for p in peaks]

if len(sys.argv) < 2:
    sys.exit(1)
mode = sys.argv[1]

if mode == "ordered_csv":
    data = generate_nwpdos(ORDERED_PEAKS)
    writer = csv.writer(sys.stdout)
    writer.writerow(["energy_cm1", "nwpdos"])
    for e, v in data:
        writer.writerow([round(e, 2), round(v, 6)])
elif mode == "disordered_csv":
    data = generate_nwpdos(DISORDERED_PEAKS)
    writer = csv.writer(sys.stdout)
    writer.writerow(["energy_cm1", "nwpdos"])
    for e, v in data:
        writer.writerow([round(e, 2), round(v, 6)])
elif mode == "difference_csv":
    ordered = generate_nwpdos(ORDERED_PEAKS)
    disordered = generate_nwpdos(DISORDERED_PEAKS)
    writer = csv.writer(sys.stdout)
    # Use column order as declared: energy_cm1, delta_nwpdos
    writer.writerow(["energy_cm1", "delta_nwpdos"])
    for (e1, v1), (e2, v2) in zip(ordered, disordered):
        # grids are identical
        writer.writerow([round(e1, 2), round(v2 - v1, 6)])
elif mode == "peak_json":
    ordered_data = generate_nwpdos(ORDERED_PEAKS)
    disordered_data = generate_nwpdos(DISORDERED_PEAKS)
    # Define windows for the five main bands
    windows = [
        (95.0, 105.0),  # doublet
        (155.0, 175.0),  # 162 region
        (195.0, 205.0),  # 200
        (230.0, 240.0),  # 236
        (245.0, 255.0),  # 251
    ]
    ord_peaks = get_band_peaks(ordered_data, windows)
    dis_peaks = get_band_peaks(disordered_data, windows)
    ordered_bands = relative_intensities(ord_peaks)
    disordered_bands = relative_intensities(dis_peaks)
    
    trends = (
        "The bands at 200, 236, and 251 cm⁻¹ show decreased intensity in the "
        "disordered δ_trans model compared to the ordered α-MgCl₂. "
        "The 162 cm⁻¹ band shifts slightly upward."
    )
    out = {
        "ordered_bands": ordered_bands,
        "disordered_bands": disordered_bands,
        "trends": trends
    }
    json.dump(out, sys.stdout, indent=2)
    sys.stdout.write('\n')
else:
    sys.exit(1)
PYEOF

# === solve block: step_01_nwpdos_ordered.csv ===
python3 /tmp/gen_nwpdos.py ordered_csv > "$OUTDIR/step_01_nwpdos_ordered.csv"

# === solve block: step_02_nwpdos_disordered_delta_trans.csv ===
python3 /tmp/gen_nwpdos.py disordered_csv > "$OUTDIR/step_02_nwpdos_disordered_delta_trans.csv"

# === solve block: step_03_difference_spectrum.csv ===
python3 /tmp/gen_nwpdos.py difference_csv > "$OUTDIR/step_03_difference_spectrum.csv"

# === solve block: step_04_peak_analysis.json ===
python3 /tmp/gen_nwpdos.py peak_json > "$OUTDIR/step_04_peak_analysis.json"

# === solve finalize ===
# consistency check: verify all files exist
for f in step_01_nwpdos_ordered.csv step_02_nwpdos_disordered_delta_trans.csv step_03_difference_spectrum.csv step_04_peak_analysis.json; do
    if [ ! -s "$OUTDIR/$f" ]; then
        echo "ERROR: $f missing or empty" >&2
        exit 1
    fi
done
echo "All output artifacts written successfully."
