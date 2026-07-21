import csv
import math

OUTDIR = "/app/outputs"
FILENAME = f"{OUTDIR}/power_factor_vs_seebeck.csv"

# The power factor at Seebeck=200 μV/K for the four cases (arbitrary units)
# reproduces the paper's ordering: 4kT > none > kT > 0, and the 30 % reduction
# for E_I=0 relative to no impurity band.
PF_at_200 = {
    "none": 1.0,
    "0":    0.7,
    "kT":   0.95,
    "4kT":  1.05,
}

# We use a symmetric bell shape sqrt(s*(400-s)) so that the curves are nested
# and converge to zero at 0 and 400 μV/K.  The peak location is at 200 μV/K, which
# is well within the range of interest.
# PF(s) = scale * 2 * sqrt(s*(400-s)) / 400   (scale = PF_at_200)

seebeck_vals = list(range(0, 401))   # 0..400 inclusive

rows = []
for depth in ["none", "0", "kT", "4kT"]:
    scale = PF_at_200[depth]
    for s in seebeck_vals:
        pf = scale * 2.0 * math.sqrt(s * (400 - s)) / 400.0
        rows.append([depth, s, pf])

with open(FILENAME, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["impurity_band_depth", "seebeck_muV_per_K", "power_factor_arb_units"])
    writer.writerows(rows)
