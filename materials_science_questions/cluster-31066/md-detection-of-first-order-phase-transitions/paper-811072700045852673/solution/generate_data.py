#!/usr/bin/env python3
"""Generate synthetic compressibility kT ∂ρ/∂μ vs μ/kT curves with a peak."""
import argparse, csv, math, sys

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--case', required=True)
    ap.add_argument('--peak_mu', type=float, required=True)
    ap.add_argument('--peak_height', type=float, default=40.0)
    ap.add_argument('--width', type=float, default=0.2)
    ap.add_argument('--mu_min', type=float, required=True)
    ap.add_argument('--mu_max', type=float, required=True)
    ap.add_argument('--n_points', type=int, default=200)
    ap.add_argument('--seed', type=int, default=42)
    args = ap.parse_args()

    # Use a Lorentzian shape with a small background
    def compressibility(mu):
        return args.peak_height / (1 + ((mu - args.peak_mu) / args.width)**2) + 0.5

    # Generate points
    step = (args.mu_max - args.mu_min) / (args.n_points - 1)
    mus = [args.mu_min + i * step for i in range(args.n_points)]

    writer = csv.writer(sys.stdout)
    writer.writerow(['mu_kT', 'compressibility'])
    for mu in mus:
        writer.writerow([round(mu, 6), round(compressibility(mu), 6)])

if __name__ == '__main__':
    main()
