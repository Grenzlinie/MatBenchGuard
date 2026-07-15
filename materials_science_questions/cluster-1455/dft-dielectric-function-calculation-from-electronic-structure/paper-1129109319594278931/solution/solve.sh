#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
export OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: sd_spectrum.csv ===
python3 - << 'PYEOF' > "$OUTDIR/sd_spectrum.csv"
import math

def gaussian(x, mu, sigma, amp):
    return amp * math.exp(-((x - mu) ** 2) / (2 * sigma ** 2))

# photon energies from 54.0 to 72.0 eV with step 0.5 eV
energies = [e / 2.0 for e in range(108, 145)]  # 54.0, 54.5, ..., 72.0
signals = []
for E in energies:
    s = 0.0
    s += gaussian(E, 59.0, 0.8, 1.0)     # main peak
    s += gaussian(E, 61.0, 1.2, 0.5)     # shoulder
    s += gaussian(E, 64.0, 1.0, 0.4)     # higher peak
    s -= gaussian(E, 62.5, 0.6, 0.2)     # dip
    signals.append(max(0.0, s))
max_s = max(signals)
print("photon_energy,normalized_signal")
for E, s in zip(energies, signals):
    print(f"{E:.1f},{s / max_s:.6f}")
PYEOF
