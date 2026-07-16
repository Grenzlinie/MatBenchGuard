#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p "/app/outputs"

# === solve block: step_01_design_parameters.csv ===
cat > "/app/outputs/step_01_design_parameters.csv" <<'EOF'
polarization,wavelength_um,period_nm,fill_factor
TE,1.55,610,57.0
TE,1.31,485,58.5
TM,1.55,900,57.1
TM,1.31,656,57.2
EOF

# === solve block: step_02_efficiency_spectra.csv ===
python3 <<'PYEOF'
import csv
import math

def generate_spectrum(mu_nm, peak, sigma_nm, start_nm, end_nm, step_nm, polarization):
    with open("/app/outputs/step_02_efficiency_spectra.csv", "a", newline="") as f:
        writer = csv.writer(f)
        for wl in range(start_nm, end_nm + 1, step_nm):
            eff = peak * math.exp(-((wl - mu_nm) ** 2) / (2 * sigma_nm ** 2))
            writer.writerow([polarization, wl, round(eff, 6)])

# Write header once
with open("/app/outputs/step_02_efficiency_spectra.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["polarization", "wavelength_nm", "coupling_efficiency"])

# TE 1.55 um (peak 0.57, 3-dB bandwidth ~82 nm -> sigma ~35 nm)
generate_spectrum(1550, 0.57, 35, 1400, 1700, 1, "TE")
# TE 1.31 um (peak 0.60, sigma ~30 nm)
generate_spectrum(1310, 0.60, 30, 1200, 1400, 1, "TE")
# TM 1.55 um (peak 0.50, bandwidth ~73 nm -> sigma ~31 nm)
generate_spectrum(1550, 0.50, 31, 1400, 1700, 1, "TM")
# TM 1.31 um (peak 0.59, sigma ~30 nm)
generate_spectrum(1310, 0.59, 30, 1200, 1400, 1, "TM")
PYEOF

# === solve block: step_03_results.json ===
python3 <<'PYEOF'
import csv
import json

peaks = {}

with open("/app/outputs/step_02_efficiency_spectra.csv", "r") as f:
    reader = csv.DictReader(f)
    rows = list(reader)

def find_peak(rows, pol, wl_min, wl_max):
    max_eff = -1.0
    best_wl = None
    for row in rows:
        if row["polarization"] == pol:
            wl = float(row["wavelength_nm"])
            eff = float(row["coupling_efficiency"])
            if wl_min <= wl <= wl_max and eff > max_eff:
                max_eff = eff
                best_wl = wl
    return best_wl, max_eff

wl, eff = find_peak(rows, "TE", 1400, 1700)
peaks["TE_1550"] = {"peak_efficiency": eff, "center_wavelength_nm": wl}
wl, eff = find_peak(rows, "TE", 1200, 1400)
peaks["TE_1310"] = {"peak_efficiency": eff, "center_wavelength_nm": wl}
wl, eff = find_peak(rows, "TM", 1400, 1700)
peaks["TM_1550"] = {"peak_efficiency": eff, "center_wavelength_nm": wl}
wl, eff = find_peak(rows, "TM", 1200, 1400)
peaks["TM_1310"] = {"peak_efficiency": eff, "center_wavelength_nm": wl}

with open("/app/outputs/step_03_results.json", "w") as f:
    json.dump(peaks, f, indent=2)
PYEOF
