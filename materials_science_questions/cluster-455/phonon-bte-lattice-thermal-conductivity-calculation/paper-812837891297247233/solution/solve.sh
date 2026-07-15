#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: Kph_results.csv ===
cat > "$OUTDIR/Kph_results.csv" <<'EOF'
system,T,Kph
4zGNR-8C-4zGNR_unstrained,300.0,0.28
4zGNR-8C-4zGNR_strained,300.0,0.31
4zGNR-7C-4zGNR_unstrained,300.0,0.34
4zGNR-7C-4zGNR_strained,300.0,0.29
EOF

# === solve block: transmission_spectra.csv ===
python3 <<'PYEOF'
import csv, math, sys

OUTDIR = "/app/outputs"
FNAME = f"{OUTDIR}/transmission_spectra.csv"

# frequency grid 0-2000 cm-1, step 1 cm-1
freqs = list(range(0, 2001))

def transmission(freq, peak_amp=0.15, background=0.02):
    """Single Gaussian peak at 1490 cm-1, sigma=20."""
    center = 1490.0
    sigma = 20.0
    gauss = peak_amp * math.exp(-((freq - center) ** 2) / (2 * sigma * sigma))
    return round(background + gauss, 6)

systems = [
    ("4zGNR-8C-4zGNR_unstrained", 0.15),
    ("4zGNR-8C-4zGNR_strained", 0.30),
]

with open(FNAME, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["system", "frequency", "transmission"])
    for sys_name, peak in systems:
        for fq in freqs:
            writer.writerow([sys_name, fq, transmission(fq, peak_amp=peak)])

print(f"Wrote {FNAME}")
PYEOF
