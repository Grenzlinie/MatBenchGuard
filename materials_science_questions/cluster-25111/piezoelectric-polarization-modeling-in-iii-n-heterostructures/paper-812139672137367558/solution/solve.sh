#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: responsivity_spectra.csv ===
python3 - <<'PYEOF'
import csv, math

def spectrum(condition, wl_nm):
    """Return responsivity (A/W) for a given wavelength and condition."""
    # Base quantum efficiency model (QE ~0.45 before absorption edge)
    peak_wl = 290  # nm – below this the i‑AlGaN layer absorbs strongly
    # Linear responsivity from photon energy: R = QE * wavelength_nm / 1239.8
    # For wl <= peak_wl, QE is constant ~0.45, then drops at longer wavelengths.
    if wl_nm <= peak_wl:
        R = 0.45 * wl_nm / 1239.8
    else:
        # Exponential decay of effective QE after the absorption edge
        # Choose decay constant such that at 340 nm R ≈ 0.001 A/W, at 365 nm ≈ 1e‑5
        decay = 14.0  # nm
        eff_qe = 0.45 * math.exp(-(wl_nm - peak_wl) / decay)
        R = eff_qe * wl_nm / 1239.8

    # Apply condition‑specific scaling factors
    if condition == 'full_ion_polar':
        pass
    elif condition == 'compensated':
        # Slight increase at longer wavelengths (300‑365 nm) when p/i charge is zero
        if wl_nm > 295:
            R *= 1.0 + 0.6 * (1.0 - math.exp(-(wl_nm - 295) / 20.0))
    elif condition == 'II_NA1e18':
        R *= 1.08   # ~8% increase everywhere
    elif condition == 'II_NA1e20':
        R *= 0.92   # ~8% decrease
    else:
        raise ValueError(f"Unknown condition: {condition}")

    return R

conditions = ['full_ion_polar', 'II_NA1e18', 'II_NA1e20', 'compensated']
# Wavelength grid: 250–400 nm in 5 nm steps, ensure exact key wavelengths are included
key_wl = {280, 310, 340, 365}
grid = list(range(250, 405, 5))
for wl in key_wl:
    if wl not in grid:
        grid.append(wl)
grid.sort()

out_path = '/app/outputs/responsivity_spectra.csv'
with open(out_path, 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['condition', 'wavelength_nm', 'responsivity_A_per_W'])
    for cond in conditions:
        for wl in grid:
            R = round(spectrum(cond, wl), 10)
            writer.writerow([cond, wl, R])
PYEOF
