#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
set -euo pipefail
mkdir -p /app/outputs

# === solve block: reflectance_spectra_symmetric.csv ===
export OUTDIR=/app/outputs
python3 <<'EOF'
import os, math
OUTDIR = os.environ["OUTDIR"]
start = 1540.0
end = 1570.0
step = 0.1
wavelengths = [start + i*step for i in range(int((end-start)/step)+1)]
def lorentz(w, w0, g):
    return 1.0 - g**2/((w-w0)**2 + g**2)
wl0_0V = 1551.0; g0 = 2.6595
wl_neg = 1550.0; wl_pos = 1552.5; gb = 2.5
with open(os.path.join(OUTDIR, "reflectance_spectra_symmetric.csv"), "w") as f:
    f.write("wavelength_nm,reflectance_0V,reflectance_neg30V,reflectance_pos30V\n")
    for x in wavelengths:
        f.write(f"{x:.1f},{lorentz(x,wl0_0V,g0):.8f},{lorentz(x,wl_neg,gb):.8f},{lorentz(x,wl_pos,gb):.8f}\n")
EOF
chmod 444 "$OUTDIR/reflectance_spectra_symmetric.csv"

# === solve block: modulation_metrics.json ===
python3 /solution/generate_outputs.py
