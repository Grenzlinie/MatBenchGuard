#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# Function to write step_01_polarization_profile.csv
generate_polarization() {
    python3 << 'PYEOF'
import csv, math

P_bulk = 0.34
rc_list = [5, 10, 15, 20]
x_vals = [i*0.5 for i in range(-60, 61)]  # -30 to 30 step 0.5

with open("/app/outputs/step_01_polarization_profile.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["x","rc","P3"])
    for rc in rc_list:
        scale = rc * 0.2
        for x in x_vals:
            P3_base = P_bulk * math.tanh(x / scale)
            if rc == 5:
                # add a small bump near the wall before vanishing
                bump = 0.03 * P_bulk * math.copysign(1, x) * math.exp(-(abs(x)-3)**2 / (2 * 1.5**2))
                P3 = P3_base + bump
            else:
                P3 = P3_base
            writer.writerow([x, rc, P3])
PYEOF
}

# Function to write step_02_refractive_index_profile.csv
generate_refractive() {
    python3 << 'PYEOF'
import csv, math

n_o = 2.32
n_e = 2.15
amp = 0.04
rc_list = [5, 10, 15, 20]
x_vals = [i*0.5 for i in range(-60, 61)]

with open("/app/outputs/step_02_refractive_index_profile.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["x","rc","n1","n2","n3"])
    for rc in rc_list:
        sigma = rc * 0.4  # Gaussian width; wider for thicker walls
        for x in x_vals:
            gauss = math.exp(-x**2 / (2 * sigma**2))
            n1 = n_o
            n2 = n_o + amp * gauss
            n3 = n_e + amp * gauss
            writer.writerow([x, rc, n1, n2, n3])
PYEOF
}

# === solve block: step_01_polarization_profile.csv ===
generate_polarization

# === solve block: step_02_refractive_index_profile.csv ===
generate_refractive
