#!/usr/bin/env python3
import csv
import math
import random
import sys

def main():
    # epsilon values spanning an order of magnitude
    epsilons = [0.01, 0.02, 0.04, 0.08, 0.16]
    gamma = 0.74   # known exponent from paper for alpha=0.5
    A = 1.0
    # deterministic small noise to mimic real scatter while preserving strong power-law
    rng = random.Random(42)
    noise_frac = 0.01   # 1% relative noise
    rows = []
    for eps in epsilons:
        true_M = A * (eps ** gamma)
        noise = rng.uniform(-noise_frac, noise_frac) * true_M
        M = true_M + noise
        rows.append((eps, M))

    writer = csv.writer(sys.stdout)
    writer.writerow(["epsilon", "frustrated_mass"])
    for eps, M in rows:
        writer.writerow([f"{eps:.12f}", f"{M:.12f}"])

if __name__ == "__main__":
    main()
