#!/usr/bin/env python3
import sys, csv, math

def generate_chi_qs(output_file):
    """Quasistatic susceptibility: χ_qs ∝ (ΔH)^{-1/2}"""
    R_min = {5: 0.15, 7: 0.10, 15: 0.05, 25: 0.02}
    max_val = 0.6
    n_points = 15
    rows = []
    for R in [5, 7, 15, 25]:
        lo = math.log10(R_min[R])
        hi = math.log10(max_val)
        for i in range(n_points):
            logval = lo + (hi - lo) * i / (n_points - 1)
            dh = 10**logval
            chi = 1.0 * (dh ** (-0.5))   # constant factor 1.0
            rows.append([R, dh, chi])
    with open(output_file, 'w', newline='') as f:
        w = csv.writer(f)
        w.writerow(['R', 'Delta_H', 'chi_qs'])
        w.writerows(rows)

def generate_mean_cluster_size(output_file):
    """Mean cluster size: ⟨s⟩ ∝ (ΔH)^{-1/2}"""
    R_min = {5: 0.15, 7: 0.10, 15: 0.05, 25: 0.02}
    max_val = 0.6
    n_points = 15
    rows = []
    for R in [5, 7, 15, 25]:
        lo = math.log10(R_min[R])
        hi = math.log10(max_val)
        for i in range(n_points):
            logval = lo + (hi - lo) * i / (n_points - 1)
            dh = 10**logval
            s_mean = 10.0 * (dh ** (-0.5))   # different constant
            rows.append([R, dh, s_mean])
    with open(output_file, 'w', newline='') as f:
        w = csv.writer(f)
        w.writerow(['R', 'Delta_H', 'mean_cluster_size'])
        w.writerows(rows)

def generate_droplet_radius(output_file):
    """Normalised radius of gyration: R_G/R ∝ (ΔH)^{-1/4}"""
    # droplet runs occur at slightly smaller ΔH than the metastable curves end
    R_min = {5: 0.10, 7: 0.07, 15: 0.035, 25: 0.015}
    # the upper bound is the metastable-cutoff value for that R
    R_max = {5: 0.15, 7: 0.10, 15: 0.05, 25: 0.02}
    n_points = 8
    rows = []
    for R in [5, 7, 15, 25]:
        lo = math.log10(R_min[R])
        hi = math.log10(R_max[R])
        for i in range(n_points):
            logval = lo + (hi - lo) * i / (n_points - 1)
            dh = 10**logval
            rg_over_r = 1.0 * (dh ** (-0.25))
            rows.append([R, dh, rg_over_r])
    with open(output_file, 'w', newline='') as f:
        w = csv.writer(f)
        w.writerow(['R', 'Delta_H', 'radius_of_gyration_over_R'])
        w.writerows(rows)

def generate_droplet_mass(output_file):
    """Nucleating droplet mass: M_ND ∝ (ΔH)^{-1}"""
    R_min = {5: 0.10, 7: 0.07, 15: 0.035, 25: 0.015}
    R_max = {5: 0.15, 7: 0.10, 15: 0.05, 25: 0.02}
    n_points = 8
    rows = []
    for R in [5, 7, 15, 25]:
        lo = math.log10(R_min[R])
        hi = math.log10(R_max[R])
        for i in range(n_points):
            logval = lo + (hi - lo) * i / (n_points - 1)
            dh = 10**logval
            mass = 0.1 * (dh ** (-1.0))
            rows.append([R, dh, mass])
    with open(output_file, 'w', newline='') as f:
        w = csv.writer(f)
        w.writerow(['R', 'Delta_H', 'mass'])
        w.writerows(rows)

def main():
    if len(sys.argv) != 3:
        print("Usage: generate_data.py <output_file> <type>", file=sys.stderr)
        sys.exit(1)
    out_file = sys.argv[1]
    kind = sys.argv[2]
    if kind == 'chi_qs':
        generate_chi_qs(out_file)
    elif kind == 'mean_cluster_size':
        generate_mean_cluster_size(out_file)
    elif kind == 'droplet_radius':
        generate_droplet_radius(out_file)
    elif kind == 'droplet_mass':
        generate_droplet_mass(out_file)
    else:
        print(f"Unknown type: {kind}", file=sys.stderr)
        sys.exit(1)

if __name__ == '__main__':
    main()
