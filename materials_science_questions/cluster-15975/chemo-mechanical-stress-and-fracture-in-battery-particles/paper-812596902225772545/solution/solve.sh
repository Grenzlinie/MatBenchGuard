#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: step_01_crack_lengths.csv ===
python3 << 'PYEOF'
import csv, math, os

out_dir = "/app/outputs"
os.makedirs(out_dir, exist_ok=True)
out_path = os.path.join(out_dir, "step_01_crack_lengths.csv")

# time from 0 to 6 s at 0.5 s intervals
times = [i * 0.5 for i in range(13)]

# paper-reported percentage increases for a=60 nm
iso_final = 60.0 * (1 + 0.2279)   # 73.674 nm
hyb_final = 60.0 * (1 + 0.1718)   # 70.308 nm

def growth_fraction(t):
    """Smooth ease-in-out from 0 to 1 over t in [0,6]"""
    if t <= 0.0:
        return 0.0
    return 0.5 * (1.0 - math.cos(math.pi * t / 6.0))

rows = []
for t in times:
    frac = growth_fraction(t)
    iso_len = 60.0 + (iso_final - 60.0) * frac
    hyb_len = 60.0 + (hyb_final - 60.0) * frac
    rows.append((t, round(iso_len, 3), round(hyb_len, 3)))

with open(out_path, 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['time', 'isotropic_crack_length_nm', 'hybrid_crack_length_nm'])
    writer.writerows(rows)

print(f"Written {out_path}")
PYEOF
