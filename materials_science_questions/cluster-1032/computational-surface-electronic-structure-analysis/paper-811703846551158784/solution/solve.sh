#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: band_dispersion_dirac.csv ===
python3 << 'PYEOF'
import csv, math

outfile = "/app/outputs/band_dispersion_dirac.csv"
kappa_points = [i * math.pi / 50.0 for i in range(51)]  # 0 to pi inclusive, 51 points
with open(outfile, "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["kappa", "beta_upper", "beta_lower"])
    for kappa in kappa_points:
        val = 2.0 * math.sin(kappa / 2.0)
        w.writerow([kappa, val, -val])
PYEOF

# === solve block: surface_mode_existence.csv ===
python3 << 'PYEOF'
import csv, math

def compute_r(eta, Z):
    if Z == 0:
        # Shockley state condition
        if eta < -1:
            r = -1.0 / eta
            return [r], [abs(r)]
        else:
            return [], []
    term = (eta**3) / (Z**2) - eta
    disc = term**2 + 4.0 * (eta / Z)**2
    sqrt_disc = math.sqrt(disc)
    r_plus = 0.5 * (term + sqrt_disc)
    r_minus = 0.5 * (term - sqrt_disc)
    return [r_plus, r_minus], [abs(r_plus), abs(r_minus)]

outfile = "/app/outputs/surface_mode_existence.csv"
eta_vals = [round(-2.0 + i * 0.1, 10) for i in range(16)]  # -2.0 ... -0.5
Z_vals = [round(-2.0 + i * 0.1, 10) for i in range(41)]    # -2.0 ... 2.0

with open(outfile, "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["eta", "Z", "exists", "r_magnitude"])
    for eta in eta_vals:
        for Z in Z_vals:
            r_vals, r_abs = compute_r(eta, Z)
            if not r_vals:
                w.writerow([eta, Z, 0, 1.0])
                continue
            valid = [a for a in r_abs if a < 1.0]
            if valid:
                exists = 1
                r_mag = min(valid)
            else:
                exists = 0
                r_mag = max(r_abs)
            w.writerow([eta, Z, exists, r_mag])
PYEOF
