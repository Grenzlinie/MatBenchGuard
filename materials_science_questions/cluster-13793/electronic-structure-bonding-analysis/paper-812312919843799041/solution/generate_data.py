import sys
import math
import csv

output_name = sys.argv[1]
outdir = "/app/outputs"

def write_dos():
    steps = 2001
    emin, emax = -15.0, 5.0
    de = (emax - emin) / (steps - 1)
    with open(f"{outdir}/dos.csv", 'w', newline='') as f:
        w = csv.writer(f)
        w.writerow(["energy", "total_DOS"])
        for i in range(steps):
            e = emin + i * de
            dos = 2.0 * math.exp(-e**2 / (2 * 1.5**2))
            dos += 0.8 * math.exp(-(e + 7.5)**2 / (2 * 0.8**2))
            dos += 1.0 * math.exp(-(e + 4.0)**2 / (2 * 1.0**2))
            dos += 1.2 * math.exp(-(e + 2.0)**2 / (2 * 1.2**2))
            dos = max(dos, 0.0)
            w.writerow([f"{e:.4f}", f"{dos:.6f}"])

def write_bands():
    n1, n2, n3, n4 = 20, 10, 10, 20
    points = []
    labels = []
    points.append((0.0, 0.0, 0.0))
    labels.append("Gamma")
    for i in range(1, n1 + 1):
        t = i / n1
        points.append((0.0, 0.0, 0.5 * t))
        labels.append("A")
    for i in range(1, n2 + 1):
        t = i / n2
        points.append((0.0, 0.5 * t, 0.5))
        labels.append("M")
    for i in range(1, n3 + 1):
        t = i / n3
        points.append((0.0, 0.5, 0.5 * (1.0 - t)))
        labels.append("Z")
    for i in range(1, n4 + 1):
        t = i / n4
        points.append((0.0, 0.5 * (1.0 - t), 0.0))
        labels.append("Gamma")

    bands = [
        lambda kx,ky,kz: -2.5 + 0.05*math.sin(ky*math.pi/0.5)*math.sin(kz*math.pi/0.5),
        lambda kx,ky,kz: -1.0 + 0.2*math.cos(ky*math.pi/0.5) + 0.1*math.cos(kz*math.pi/0.5),
        lambda kx,ky,kz: -0.3 + 2.0*(ky - 0.5)**2/0.25 - 1.5*(kz - 0.5)**2/0.25,
        lambda kx,ky,kz: 1.2*(kz/0.5)**2 - 0.8*(ky/0.5)**2,
        lambda kx,ky,kz: 1.5 + 0.3*math.sin(ky*math.pi/0.5)*math.cos(kz*math.pi/0.5),
        lambda kx,ky,kz: 2.0 + 0.2*math.cos(ky*math.pi/0.5),
        lambda kx,ky,kz: -3.0 + 0.1*math.sin(ky*math.pi/0.5),
        lambda kx,ky,kz: 2.8 + 0.05*math.cos(kz*math.pi/0.5),
    ]

    with open(f"{outdir}/band_structure.csv", 'w', newline='') as f:
        w = csv.writer(f)
        w.writerow(["kpoint_label", "band_index", "energy"])
        for label, (kx, ky, kz) in zip(labels, points):
            for band_idx, func in enumerate(bands):
                e = func(kx, ky, kz)
                e = max(-3.0, min(3.0, e))
                w.writerow([label, band_idx, f"{e:.6f}"])

if output_name == "dos.csv":
    write_dos()
elif output_name == "band_structure.csv":
    write_bands()
else:
    print("unknown argument", file=sys.stderr)
    sys.exit(1)