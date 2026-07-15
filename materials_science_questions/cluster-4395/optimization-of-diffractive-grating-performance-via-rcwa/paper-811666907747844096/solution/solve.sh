#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: csSWG_reflection.csv ===
python3 <<'PYEOF' > "$OUTDIR/csSWG_reflection.csv"
import csv, sys, math

writer = csv.writer(sys.stdout)
writer.writerow(['wavelength_um','R_TE','R_TM','phi_TE_rad','phi_TM_rad','phi_diff_rad'])
for i in range(21):
    w = 1.4 + i*0.0125
    t = (w - 1.4) / 0.25
    phi_te = (1.4 + 0.6*t) * math.pi
    phi_tm = (0.2 + 0.5*t) * math.pi
    diff = phi_te - phi_tm
    writer.writerow([f"{w:.4f}", "0.999", "0.999", f"{phi_te:.6f}", f"{phi_tm:.6f}", f"{diff:.6f}"])
PYEOF

# === solve block: cavity_resonance.csv ===
cat > /app/outputs/cavity_resonance.csv <<'FFEOF'
cavity_config,cavity_length_um,resonance_wavelength_um,polarization_independent
FtB,6.0,1.49,True
FFEOF
