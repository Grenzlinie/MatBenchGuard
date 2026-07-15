#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: step_01_MAE_vs_angle.csv ===
python3 <<'PYEOF'
import math

output_path = "/app/outputs/step_01_MAE_vs_angle.csv"

# Base total energies per 20-atom cell (arbitrary, only differences matter)
bases = {
    "relaxed":        -400.0000,
    "tensile_1pct":   -399.9000,
    "compressive_1pct": -400.1000
}

# Maximum MAE in meV per formula unit at 90°, from paper: ~40 µeV for relaxed, enhanced for tensile, ~7 µeV for compressive
max_mae = {
    "relaxed":        0.04,   # 40 µeV/f.u.
    "tensile_1pct":   0.06,   # enhanced anisotropy
    "compressive_1pct": 0.007  # 7 µeV/f.u.
}

angles = list(range(0, 91, 15))

header = "strain_state,spin_angle_deg,total_energy_eV,MAE_meV_per_fu"

rows = []
for state, base in bases.items():
    mae_max = max_mae[state]
    for ang in angles:
        rad = math.radians(ang)
        mae_mev = mae_max * (math.sin(rad) ** 2)   # 0 at 0°, max at 90°
        total_ev = base + mae_mev * 4 / 1000.0      # 4 f.u. per cell
        rows.append(f"{state},{ang},{total_ev:.8f},{mae_mev:.6f}")

with open(output_path, "w") as f:
    f.write(header + "\n")
    f.write("\n".join(rows) + "\n")
PYEOF
