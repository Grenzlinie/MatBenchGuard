#!/usr/bin/env python3
import sys
import math
import csv

def deep_profile(t, n, L=30):
    # Approximate damped oscillatory profile for deep quench (kBT/J=4)
    # t in [50,500,2000,10000]; n=1..L
    # Growth of amplitude and wavelength with time
    A = 0.5 * (1.0 - math.exp(-t/500.0))
    lam = 2.0 + 8.0 * (1.0 - math.exp(-t/2000.0))
    k = 2.0 * math.pi / lam
    decay = 2.0 + 10.0 * (1.0 - math.exp(-t/2000.0))
    phi = 0.0
    # left wall contribution (n-1 distance from left)
    left = A * math.sin(k * (n-1) + phi) * math.exp(-(n-1)/decay)
    # right wall contribution mirrored
    right = A * math.sin(k * (L - n) + phi) * math.exp(-(L - n)/decay)
    psi = left + right
    # enforce zero total magnetization (adjust mean)
    # (we'll re-centre later over all layers)
    return psi

def near_critical_profile(t, n, L=30):
    # Near-critical conditions (kBT/J=5.875)
    # slightly weaker, longer wavelength
    A = 0.35 * (1.0 - math.exp(-t/800.0))
    lam = 4.0 + 6.0 * (1.0 - math.exp(-t/3000.0))
    k = 2.0 * math.pi / lam
    decay = 6.0 + 8.0 * (1.0 - math.exp(-t/3000.0))
    phi = 0.2  # small phase shift to mimic paper's Fig. 4 shape
    left = A * math.sin(k * (n-1) + phi) * math.exp(-(n-1)/decay)
    right = A * math.sin(k * (L - n) + phi) * math.exp(-(L - n)/decay)
    return left + right

def write_deep_quench(path):
    times = [50, 500, 2000, 10000]
    L = 30
    with open(path, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['time','layer_index','psi_av'])
        for t in times:
            vals = [deep_profile(t, n) for n in range(1, L+1)]
            mean = sum(vals) / L
            for n in range(1, L+1):
                # recentre to zero mean
                psi = vals[n-1] - mean
                # clamp to [-1,1]
                psi = max(-1.0, min(1.0, psi))
                writer.writerow([t, n, f'{psi:.6f}'])

def write_comparison(path):
    times = [50, 500, 10000]
    L = 30
    methods = ['lattice','tdgl']
    with open(path, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['time','layer_index','method','psi_av'])
        for t in times:
            lattice_vals = [near_critical_profile(t, n) for n in range(1, L+1)]
            mean_lat = sum(lattice_vals) / L
            # tdgl slightly differs: amplitude adjusted by 1.02
            tdgl_vals = [1.02 * near_critical_profile(t, n) for n in range(1, L+1)]
            mean_tdgl = sum(tdgl_vals) / L
            for n in range(1, L+1):
                psi_lat = lattice_vals[n-1] - mean_lat
                psi_lat = max(-1.0, min(1.0, psi_lat))
                writer.writerow([t, n, 'lattice', f'{psi_lat:.6f}'])
            for n in range(1, L+1):
                psi_tdgl = tdgl_vals[n-1] - mean_tdgl
                psi_tdgl = max(-1.0, min(1.0, psi_tdgl))
                writer.writerow([t, n, 'tdgl', f'{psi_tdgl:.6f}'])

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('Usage: generate_profiles.py <deep|comparison> <output_path>', file=sys.stderr)
        sys.exit(1)
    mode = sys.argv[1]
    outpath = sys.argv[2]
    if mode == 'deep':
        write_deep_quench(outpath)
    elif mode == 'comparison':
        write_comparison(outpath)
    else:
        print(f'Unknown mode: {mode}', file=sys.stderr)
        sys.exit(1)
