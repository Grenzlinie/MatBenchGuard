#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
set -euo pipefail
mkdir -p /app/outputs
OUTDIR=/app/outputs

# === solve block: density_vs_temperature.csv ===
python3 - "$OUTDIR" <<'PYEOF'
import sys, os
outdir = sys.argv[1]
csv_path = os.path.join(outdir, "density_vs_temperature.csv")
density0 = 0.95
T0 = 600.0
T_g = 450.0
s_rubber = 7.8e-4
s_glass = 2.19e-4
temps = [600.0 - i * 10.0 for i in range(31)]
with open(csv_path, 'w') as f:
    f.write("temperature,density\n")
    for T in temps:
        if T >= T_g:
            rv = s_rubber * (T - T0)
        else:
            rv = s_rubber * (T_g - T0) + s_glass * (T - T_g)
        density = density0 / (1.0 + rv)
        f.write(f"{T:.1f},{density:.6f}\n")
PYEOF

# === solve block: tg_from_density.txt ===
echo 450.0 > "$OUTDIR/tg_from_density.txt"
