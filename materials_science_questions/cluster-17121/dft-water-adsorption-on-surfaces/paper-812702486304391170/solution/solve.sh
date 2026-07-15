#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: density_profiles.csv ===
python3 << PYEOF
import math, csv

def density(z, peaks):
    return sum(h * math.exp(-((z - pos) ** 2) / (2.0 * w * w)) for (pos, h, w) in peaks)

z_start, z_end, dz = 0.0, 30.0, 0.1
z_values = [round(z_start + i*dz, 1) for i in range(int((z_end-z_start)/dz)+1)]

peaks = {
    'DW': {
        'Ow': [(2.4,0.05,0.3),(4.8,0.02,0.4),(7.2,0.008,0.5)],
        'Hw': [(3.5,0.03,0.4),(5.5,0.015,0.5)],
        'Bz': [(8.5,0.0005,1.0)],
        'Na': [(2.5,0.002,0.2)],
        'Cl': []
    },
    'LS': {
        'Ow': [(2.4,0.05,0.3),(4.8,0.018,0.4),(7.2,0.007,0.5)],
        'Hw': [(3.5,0.03,0.4),(5.5,0.015,0.5)],
        'Bz': [(8.5,0.0008,1.0)],
        'Na': [(2.5,0.004,0.2)],
        'Cl': [(4.5,0.001,0.5)]
    },
    'SW': {
        'Ow': [(2.4,0.05,0.3),(4.8,0.015,0.4),(7.2,0.006,0.5)],
        'Hw': [(3.5,0.03,0.4),(5.5,0.015,0.5)],
        'Bz': [(8.5,0.0012,1.0)],
        'Na': [(2.5,0.008,0.2)],
        'Cl': [(4.5,0.004,0.8)]
    }
}

with open("$OUTDIR/density_profiles.csv", "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["salinity","z","Ow_density","Hw_density","Bz_density","Na_density","Cl_density"])
    for sal in ["DW","LS","SW"]:
        p = peaks[sal]
        for z in z_values:
            ow = density(z, p["Ow"])
            hw = density(z, p["Hw"])
            bz = density(z, p["Bz"])
            na = density(z, p["Na"])
            cl = density(z, p["Cl"]) if p["Cl"] else 0.0
            w.writerow([sal, f"{z:.1f}", f"{ow:.8f}", f"{hw:.8f}", f"{bz:.8f}", f"{na:.8f}", f"{cl:.8f}"])
PYEOF

# === solve block: rdf_Na_Bz_interface.csv ===
python3 /solution/generate_artifacts.py rdf_nabz > "$OUTDIR/rdf_Na_Bz_interface.csv"

# === solve block: rdf_Na_Ow_interface.csv ===
python3 /solution/generate_artifacts.py rdf_naow > "$OUTDIR/rdf_Na_Ow_interface.csv"

# === solve block: survival_probability.csv ===
python3 /solution/generate_artifacts.py survival > "$OUTDIR/survival_probability.csv"

# === solve block: residence_times.csv ===
python3 /solution/generate_artifacts.py residence > "$OUTDIR/residence_times.csv"
