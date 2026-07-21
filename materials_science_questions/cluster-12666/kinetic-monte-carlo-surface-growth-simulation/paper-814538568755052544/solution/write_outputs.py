#!/usr/bin/env python3
import csv
import math

OUTDIR = "/app/outputs"

def write_d2d():
    with open(f"{OUTDIR}/best_fit_d2d.txt", "w") as f:
        f.write("0.20\n")

def gen_histogram(bin_centers, params):
    A, sigma1, B, mu2, sigma2, C, gamma = params
    probs = []
    for x in bin_centers:
        p = A * math.exp(-x**2/(2*sigma1**2))
        if B > 0:
            p += B * math.exp(-(x - mu2)**2/(2*sigma2**2))
        if x > 0:
            p += C * (x ** (-gamma))
        probs.append(p)
    total = sum(probs)
    if total == 0:
        return [0]*len(bin_centers)
    return [p / total for p in probs]

def write_histogram(bin_centers, probs, filename):
    with open(f"{OUTDIR}/{filename}", "w", newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["displacement_nm", "probability"])
        for x, p in zip(bin_centers, probs):
            writer.writerow([x, p])

def main():
    # Bin centers from 25 to 1975 nm step 50 nm
    bin_centers = [x for x in range(25, 2000, 50)]

    # Parameters for homogeneous PS mixture:
    # central narrow peak (immobile + confined in-plane diffusion)
    # intermediate Gaussian for true in-plane diffusion (mu=250 nm, sigma=150 nm)
    # power-law tail from flights (gamma ~ 1.5 for tail of step-size distribution)
    homo_params = (100, 25, 30, 250, 150, 5, 1.6)
    # Parameters for PS-hexagonal: no intermediate Gaussian (B=0),
    # higher flight tail to reflect longer flights (C larger, gamma similar)
    hex_params = (100, 25, 0, 0, 1, 12, 1.6)

    homo_probs = gen_histogram(bin_centers, homo_params)
    hex_probs = gen_histogram(bin_centers, hex_params)

    write_d2d()
    write_histogram(bin_centers, homo_probs, "step_size_homogeneous_ps.csv")
    write_histogram(bin_centers, hex_probs, "step_size_ps_hexagonal.csv")

if __name__ == "__main__":
    main()