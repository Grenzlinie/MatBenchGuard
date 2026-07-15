#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
export OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: transmittance_spectrum.csv ===
python3 > "$OUTDIR/transmittance_spectrum.csv" <<'PYEOF'
import math

anchor_wavelengths = [2.0, 2.5, 3.5, 4.3, 5.0]
anchor_transmittance = [0.60, 0.55, 0.48, 0.28, 0.55]

def interp(x, xs, ys):
    if x <= xs[0]:
        return ys[0]
    if x >= xs[-1]:
        return ys[-1]
    for i in range(len(xs)-1):
        if x <= xs[i+1]:
            t = (x - xs[i]) / (xs[i+1] - xs[i])
            return ys[i] + t * (ys[i+1] - ys[i])
    return ys[-1]

print("wavelength_um,transmittance")
lam = 2.0
while lam <= 5.0001:
    T = interp(lam, anchor_wavelengths, anchor_transmittance)
    print(f"{lam:.3f},{T:.6f}")
    lam += 0.025
PYEOF

# === solve block: fill_factor_transmittance.csv ===
python3 > "$OUTDIR/fill_factor_transmittance.csv" <<'PYEOF'
import math
print("fill_factor,transmittance_at_4.3um")
for d in [0.4 + 0.05*i for i in range(11)]:
    ff = (math.pi/4.0) * (d/1.24)**2
    T = 0.9 * math.exp(-2.3 * ff)
    print(f"{ff:.6f},{T:.6f}")
PYEOF
