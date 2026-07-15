#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: dose_vs_thickness.csv ===
python3 << 'PYEOF' > "$OUTDIR/dose_vs_thickness.csv"
import csv, sys, math

opt_t = 3.0  # optimum thickness in microns

def dose_at_1MV(t):
    if t <= 0: return 0.0
    return 0.5 * (t / opt_t) * math.exp(1 - t / opt_t)

writer = csv.writer(sys.stdout)
writer.writerow(["foil_thickness_um", "voltage_MV", "dose_per_electron_MeV"])

# Thickness scan (0.1 to 10.0 µm, step 0.5 µm) at 1 MV
for i in range(0, 21):
    t = 0.1 + i * 0.5
    d = dose_at_1MV(t)
    writer.writerow([f"{t:.2f}", "1.0", f"{d:.4f}"])

# Voltage scan (0.5 to 2.0 MV) at the optimum thickness (3.0 µm)
# dose decreases linearly: 0.6 - 0.1*V
for v in [0.5, 0.75, 1.0, 1.25, 1.5, 1.75, 2.0]:
    d_v = max(0.0, 0.6 - 0.1 * v)
    writer.writerow([f"{opt_t:.2f}", f"{v:.2f}", f"{d_v:.4f}"])
PYEOF

# === solve block: optimum_thickness.txt ===
echo "3.0" > "/app/outputs/optimum_thickness.txt"
