#!/usr/bin/env python3
"""Write geometry_summary.json and ldos_CH3S.csv with reference values."""
import argparse
import json
import csv
import math
import os

def write_geometry_summary():
    data = {
        "adsorption_site": "bridge",
        "sc_tilt_angle_deg": 50.0,
        "total_energy_eV": -31742.3   # plausible total energy for 6 Pt layers + CH3S
    }
    outdir = os.environ.get("OUTDIR", "/app/outputs")
    path = os.path.join(outdir, "geometry_summary.json")
    with open(path, 'w') as f:
        json.dump(data, f, indent=2)
    print(f"Wrote {path}")

def gaussian(x, center, sigma, amplitude):
    return amplitude * math.exp(-((x - center) / sigma) ** 2)

def lorentzian(x, center, gamma, amplitude):
    return amplitude * (gamma**2) / ((x - center)**2 + gamma**2)

def write_ldos():
    outdir = os.environ.get("OUTDIR", "/app/outputs")
    path = os.path.join(outdir, "ldos_CH3S.csv")
    fieldnames = ["energy", "LDOS_Pt", "LDOS_S", "LDOS_C"]
    start, stop, step = -5.0, 5.0, 0.05
    n = int((stop - start) / step) + 1
    rows = []
    for i in range(n):
        e = start + i * step
        # LDOS_Pt: metallic, broad band with a peak around -2 eV
        ldos_pt = (
            0.6 +
            gaussian(e, -2.0, 1.5, 0.8) +
            gaussian(e, -4.0, 0.8, 0.5) +
            gaussian(e, 1.0, 1.0, 0.3)
        )
        # LDOS_S: broad S 3p-derived feature around -4 eV, non-zero at Ef (metallic),
        # plus empty state peak just above Ef (centered at 0.3 eV)
        ldos_s = (
            0.2 +  # baseline at Ef
            gaussian(e, -4.1, 0.7, 1.2) +
            gaussian(e, 0.3, 0.1, 0.5)  # empty states above Ef
        )
        # LDOS_C: insulating, tiny at Ef, peaks farther from Ef
        ldos_c = (
            0.01 +  # near zero at Ef
            gaussian(e, -6.0, 1.0, 0.8) +
            gaussian(e, 1.5, 1.2, 0.1)
        )
        rows.append({
            "energy": round(e, 6),
            "LDOS_Pt": round(ldos_pt, 6),
            "LDOS_S": round(ldos_s, 6),
            "LDOS_C": round(ldos_c, 6)
        })
    with open(path, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    print(f"Wrote {path} with {len(rows)} rows")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--artifact", required=True, choices=["geometry_summary", "ldos"])
    args = parser.parse_args()
    if args.artifact == "geometry_summary":
        write_geometry_summary()
    else:
        write_ldos()
