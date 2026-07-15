#!/usr/bin/env python3
"""Oracle artifact generator for fused silica MD reproduction task."""
import csv, math, random, sys

def write_amorphous(filepath):
    n_si, n_o = 512, 1024
    total = n_si + n_o  # 1536 atoms
    box = 28.64
    with open(filepath, 'w') as f:
        f.write(f"LAMMPS data file (oracle evidence)\n\n")
        f.write(f"{total} atoms\n")
        f.write(f"2 atom types\n\n")
        f.write(f"0.0 {box} xlo xhi\n")
        f.write(f"0.0 {box} ylo yhi\n")
        f.write(f"0.0 {box} zlo zhi\n\n")
        f.write(f"Masses\n\n1 28.0855\n2 15.999\n\n")
        f.write(f"Atoms\n\n")
        for i in range(total):
            atype = 1 if i < n_si else 2
            x = random.uniform(0, box)
            y = random.uniform(0, box)
            z = random.uniform(0, box)
            f.write(f"{i+1} {atype} {x:.6f} {y:.6f} {z:.6f}\n")
        f.write("\n")

def write_volumetric(filepath):
    p_crit = 8.0      # densification threshold (GPa)
    K = 37.0          # bulk modulus (GPa)
    H = 28.57142857142857  # plastic hardening modulus such that residual at 8.2 GPa ~0.007
    cycles = [(1, 6.0), (2, 8.0), (3, 8.2), (4, 10.0), (5, 12.0)]
    N = 50  # points per phase
    rows = []
    for cid, pmax in cycles:
        # load
        for i in range(N+1):
            p = pmax * i / N
            vol = 1.0 - p / K - max(0.0, p - p_crit) / H
            rows.append([cid, "load", vol, p])
        # unload
        vol_at_max = 1.0 - pmax / K - max(0.0, pmax - p_crit) / H
        for i in range(N+1):
            p = pmax - pmax * i / N
            vol = vol_at_max - (pmax - p) / K
            rows.append([cid, "unload", vol, p])
    with open(filepath, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["cycle_id", "loading_phase", "volume_norm", "pressure"])
        writer.writerows(rows)

def write_critical(filepath):
    p1, pt, qt = 12.337, -8.5, 7.402
    B, beta = 1.168, 0.5
    points = []
    # tensile / low-pressure regime
    for p in [-5.0, -2.0, 0.0, 2.0, 4.0]:
        q = (p1 - p) / (p1 - pt) * qt
        points.append([p, q])
    # compressive regime
    for p in [6.0, 8.0, 10.0, 12.0, 14.0]:
        q = B * math.pow(p, beta)
        points.append([p, q])
    with open(filepath, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["confining_pressure", "critical_shear_stress_qc"])
        writer.writerows(points)

if __name__ == "__main__":
    step, path = sys.argv[1], sys.argv[2]
    if step == "amorphous":
        write_amorphous(path)
    elif step == "vol":
        write_volumetric(path)
    elif step == "crit":
        write_critical(path)
    else:
        raise ValueError(f"Unknown step: {step}")