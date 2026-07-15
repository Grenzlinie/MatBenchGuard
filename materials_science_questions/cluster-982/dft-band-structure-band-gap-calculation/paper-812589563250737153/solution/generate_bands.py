#!/usr/bin/env python3
"""Synthesize reference band structure and band gap for the oracle.

Writes /app/outputs/band_structure.dat and band_gap.json with a direct gap
of 4.18 eV at Gamma, matching the paper's DFT result.
"""
import sys, os, argparse
import json, math

OUTDIR = "/app/outputs"

NUM_KPOINTS = 50
NUM_BANDS   = 100
NUM_VALENCE = 60          # bands 1..60 occupied
NUM_CONDUCTION = 40       # bands 61..100 unoccupied

# Parameters for the simple analytic model
ALPHA = 5.0   # valence band curvature (eV)
GAMMA = 5.0   # conduction band curvature (eV)
BAND_GAP_EV = 4.18

def generate_kpoints():
    """Generate a simple triclinic k-path of fractional coordinates.
    The path includes Gamma at index 24 (0-based)."""
    # define symmetry points in fractional coordinates of the supercell
    points = [
        (0.0, 0.0, 0.0),   # Gamma
        (0.5, 0.0, 0.0),   # X
        (0.5, 0.5, 0.0),   # S
        (0.0, 0.5, 0.0),   # Y
        (0.0, 0.0, 0.0),   # Gamma
        (0.0, 0.0, 0.5),   # Z
        (0.0, 0.0, 0.0),   # Gamma
    ]
    # sample linearly along the path
    kpts = []
    n_segments = len(points) - 1
    steps_per_segment = NUM_KPOINTS // n_segments
    remainder = NUM_KPOINTS - steps_per_segment * n_segments

    for i in range(len(points) - 1):
        A = points[i]
        B = points[i+1]
        n_pts = steps_per_segment + (1 if i < remainder else 0)
        for step in range(n_pts):
            if step == 0 and i > 0:
                continue  # avoid duplicate junctions except first point
            t = step / n_pts if n_pts > 0 else 0
            k = tuple(a + t*(b - a) for a,b in zip(A, B))
            kpts.append(k)
    # ensure we have exactly NUM_KPOINTS
    while len(kpts) < NUM_KPOINTS:
        kpts.append(points[-1])
    kpts = kpts[:NUM_KPOINTS]
    return kpts

def write_band_structure():
    kpts = generate_kpoints()
    # Pre-calculate squared distance of each k-point from Gamma.
    # Use Euclidean norm of fractional coordinates; this gives a
    # reasonable dispersion with ALPHA/GAMMA.
    d2 = [kx*kx + ky*ky + kz*kz for (kx,ky,kz) in kpts]

    lines = []
    lines.append(f"{len(kpts)} {NUM_BANDS}\n")
    for ik, d in enumerate(d2, start=1):
        # Valence bands (indices 1..60)
        for ib in range(1, NUM_VALENCE + 1):
            offset = ib - 1   # 0 for top valence
            energy = - (offset + ALPHA * d)
            lines.append(f"{ik} {ib} {energy:.6f}\n")
        # Conduction bands (indices 61..100)
        for ib in range(NUM_VALENCE + 1, NUM_BANDS + 1):
            offset_c = ib - NUM_VALENCE - 1  # 0 for lowest conduction
            energy = BAND_GAP_EV + offset_c + GAMMA * d
            lines.append(f"{ik} {ib} {energy:.6f}\n")

    path = os.path.join(OUTDIR, "band_structure.dat")
    with open(path, 'w') as f:
        f.writelines(lines)
    print(f"Written {path}")

def write_band_gap():
    data = {"band_gap": BAND_GAP_EV}
    path = os.path.join(OUTDIR, "band_gap.json")
    with open(path, 'w') as f:
        json.dump(data, f, indent=2)
        f.write("\n")
    print(f"Written {path}")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", required=True, help="Output file to generate")
    args = parser.parse_args()
    basename = os.path.basename(args.output)
    if basename == "band_structure.dat":
        write_band_structure()
    elif basename == "band_gap.json":
        write_band_gap()
    else:
        print(f"Unknown output: {basename}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
