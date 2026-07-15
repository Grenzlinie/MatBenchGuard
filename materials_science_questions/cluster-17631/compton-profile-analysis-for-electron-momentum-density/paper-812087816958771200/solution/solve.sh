#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs
OUTDIR="/app/outputs"
export OUTDIR

# === solve block: scattering_factors.csv ===
python3 <<'EOF_SCATTER'
import csv, os
rows = [
    (0.0000, 1.000, 1.000, 1.000),
    (0.1330, 0.956, 0.956, 0.995),
    (0.2660, 0.831, 0.831, 0.978),
    (0.3990, 0.650, 0.649, 0.952),
    (0.5320, 0.443, 0.441, 0.918),
    (0.6650, 0.245, 0.237, 0.876),
    (0.7980, 0.080, 0.060, 0.829),
    (0.9310, 0.038, 0.078, 0.779),
    (1.0640, 0.105, 0.174, 0.727),
    (1.1970, 0.128, 0.234, 0.676),
    (1.3299, 0.118, 0.264, 0.625),
    (1.9949, 0.094, 0.174, 0.421),
    (2.6599, 0.267, 0.066, 0.307),
    (3.3249, 0.130, 0.106, 0.252),
]
outpath = os.path.join(os.environ['OUTDIR'], 'scattering_factors.csv')
with open(outpath, 'w') as f:
    writer = csv.writer(f)
    writer.writerow(['s', 'F_x_N', 'F_y_N', 'F_z_N'])
    for r in rows:
        writer.writerow(r)
EOF_SCATTER

# === solve block: compton_profiles.csv ===
python3 > "$OUTDIR/compton_profiles.csv" <<'PYEOF'
import csv, sys
# Table 2 directional and isotropic Compton profiles
rows = [
    (0.0, 17.964, 17.546, 17.735, 17.618),
    (0.1, 17.818, 17.452, 17.573, 17.484),
    (0.2, 17.373, 17.158, 17.094, 17.087),
    (0.3, 16.627, 16.633, 16.328, 16.437),
    (0.4, 15.618, 15.849, 15.320, 15.558),
    (0.5, 14.429, 14.803, 14.128, 14.484),
    (0.6, 13.157, 13.534, 12.818, 13.262),
    (0.7, 11.870, 12.118, 11.458, 11.943),
    (0.8, 10.596, 10.645, 10.110, 10.580),
    (0.9,  9.336,  9.203,  8.826,  9.226),
    (1.0,  8.095,  7.857,  7.646,  7.932),
    (1.2,  5.783,  5.604,  5.677,  5.689),
    (1.4,  3.966,  3.985,  4.237,  4.038),
    (1.6,  2.784,  2.906,  3.235,  2.949),
    (1.8,  2.109,  2.211,  2.545,  2.270),
    (2.0,  1.724,  1.764,  2.064,  1.844),
    (3.0,  0.968,  0.944,  0.989,  0.969),
    (4.0,  0.572,  0.583,  0.574,  0.574),
    (5.0,  0.333,  0.333,  0.334,  0.334),
]
writer = csv.writer(sys.stdout)
writer.writerow(['q', 'J_x', 'J_y', 'J_z', 'J_iso'])
for r in rows:
    writer.writerow(r)
PYEOF

# === solve block: jzero_surface.csv ===
python3 > "$OUTDIR/jzero_surface.csv" <<'PYEOF'
import csv, sys, math

# known axis values from Table 2 at q=0
J_z = 17.735      # theta=0
J_x = 17.964      # theta=90, phi=0
J_y = 17.546      # theta=90, phi=90

# average and amplitude at theta=90
J_avg90 = (J_x + J_y) / 2.0
J_amp90 = (J_x - J_y) / 2.0

# smoothstep function
def smoothstep(t):
    # t in [0,1], returns smooth from 0 to 1
    t2 = t * t
    t3 = t2 * t
    return 10.0 * t3 - 15.0 * t2 * t + 6.0 * t3 * t

# generate grid: theta 0..90 step 5, phi 0..355 step 5
rows = []
for theta in range(0, 91, 5):
    t = theta / 90.0
    s = smoothstep(t)
    A = J_z + (J_avg90 - J_z) * s
    B = J_amp90 * s
    for phi in range(0, 360, 5):
        rad = math.radians(6 * phi)  # sixfold
        J0 = A + B * math.cos(rad)
        rows.append((theta, phi, round(J0, 6)))  # round to prevent long strings

writer = csv.writer(sys.stdout)
writer.writerow(['theta_deg', 'phi_deg', 'J0'])
for r in rows:
    writer.writerow(r)
PYEOF
