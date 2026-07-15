#!/usr/bin/env python3
"""Oracle script: generate bandgap_vs_strain.csv and band_edges_vs_strain.csv."""
import csv
import sys
import os

OUTDIR = "/app/outputs"

# ------------------------------------------------------------------
# Bandgap data per structure (strain in %, bandgap in eV)
# ------------------------------------------------------------------
def bandgap_hpsi(eta):
    # Quadratic: peak 2.056 at 0%, endpoints 1.628 at ±10%
    a = (2.056 - 1.628) / 100.0   # coefficient for eta^2
    return 2.056 - a * eta * eta

def _linear_interp(eta, points):
    """Interpolate linearly from sorted (eta, value) pairs."""
    if eta <= points[0][0]:
        return points[0][1]
    if eta >= points[-1][0]:
        return points[-1][1]
    for i in range(len(points) - 1):
        if points[i][0] <= eta < points[i+1][0]:
            x1, y1 = points[i]
            x2, y2 = points[i+1]
            return y1 + (y2 - y1) * (eta - x1) / (x2 - x1)
    return points[-1][1]

# HSiP points from paper
HSIP_POINTS = [(-10, 1.866), (-3, 3.136), (0, 3.3), (8, 3.111), (9, 2.857), (10, 2.613)]
def bandgap_hsip(eta):
    return _linear_interp(eta, HSIP_POINTS)

# HSiPbp points from paper
HSIPBP_POINTS = [(-10, 1.862), (-5, 3.129), (0, 3.14), (5, 3.117), (10, 2.556)]
def bandgap_hsipbp(eta):
    return _linear_interp(eta, HSIPBP_POINTS)

# ------------------------------------------------------------------
# VBM parameters: VBM(eta) = VBM0 + slope * eta  (eta in %)
# ------------------------------------------------------------------
VBM_PARAMS = {
    "HPSi":    {"VBM0": -5.80, "slope": 0.01},
    "HSiP":    {"VBM0": -5.90, "slope": 0.005},
    "HSiPbp":  {"VBM0": -6.00, "slope": 0.008},
}

# ------------------------------------------------------------------
# Main:
# ------------------------------------------------------------------
def write_bandgap_csv():
    structures = ["HPSi", "HSiP", "HSiPbp"]
    funcs = {"HPSi": bandgap_hpsi, "HSiP": bandgap_hsip, "HSiPbp": bandgap_hsipbp}
    with open(os.path.join(OUTDIR, "bandgap_vs_strain.csv"), "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["structure", "strain", "bandgap"])
        for struc in structures:
            for eta in range(-10, 11):
                bg = funcs[struc](eta)
                w.writerow([struc, eta, f"{bg:.6f}"])

def write_band_edges_csv():
    structures = ["HPSi", "HSiP", "HSiPbp"]
    bandgap_funcs = {"HPSi": bandgap_hpsi, "HSiP": bandgap_hsip, "HSiPbp": bandgap_hsipbp}
    with open(os.path.join(OUTDIR, "band_edges_vs_strain.csv"), "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["structure", "strain", "CBM", "VBM"])
        for struc in structures:
            vbm0 = VBM_PARAMS[struc]["VBM0"]
            slope = VBM_PARAMS[struc]["slope"]
            for eta in range(-10, 11):
                bg = bandgap_funcs[struc](eta)
                vbm = vbm0 + slope * eta
                cbm = vbm + bg
                w.writerow([struc, eta, f"{cbm:.6f}", f"{vbm:.6f}"])

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: generate.py [bandgap|band_edges]")
        sys.exit(1)
    mode = sys.argv[1].lower()
    if mode == "bandgap":
        write_bandgap_csv()
    elif mode == "band_edges":
        write_band_edges_csv()
    else:
        print("Unknown mode: use bandgap or band_edges")
        sys.exit(1)
