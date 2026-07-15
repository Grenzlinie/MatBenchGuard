#!/usr/bin/env python3
"""Generate reference oracle outputs for the thermal transport task.
Uses only stdlib."""
import sys
import csv
import math

K300 = 645.0
ALPHA = 0.735

temperatures = [300, 400, 500, 600, 700]

def compute_thermal():
    rows = []
    for T in temperatures:
        # K_lat = K300 * (300/T)^alpha
        k_lat = K300 * math.pow(300.0 / T, ALPHA)
        # K_RTA approximately half at 300 K, approaching K_lat at higher T
        ratio = 1.0 - 0.5 * (300.0 / T)
        k_rta = k_lat * ratio
        rows.append([T, round(k_lat, 3), round(k_rta, 3)])
    return rows

def compute_mode():
    # branch contributions from paper: ZA~60%, TA 19.45%, LA 16.02%, optical 4.53%
    return [
        ["ZA", 60.0],
        ["TA", 19.45],
        ["LA", 16.02],
        ["optical", 4.53]
    ]

def write_csv(path, header, rows):
    with open(path, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(header)
        w.writerows(rows)

def main():
    if len(sys.argv) < 2:
        print("Usage: generate_outputs.py <thermal|mode|all> [outdir]", file=sys.stderr)
        sys.exit(1)
    mode = sys.argv[1]
    if len(sys.argv) >= 3:
        outdir = sys.argv[2]
    else:
        outdir = ""

    if mode in ("thermal", "all"):
        rows = compute_thermal()
        write_csv(f"{outdir}/thermal_conductivity_vs_temperature.csv" if outdir else "thermal_conductivity_vs_temperature.csv",
                  ["Temperature_K", "K_lat_W_mK", "K_RTA_W_mK"], rows)
    if mode in ("mode", "all"):
        rows = compute_mode()
        write_csv(f"{outdir}/mode_contributions_at_300K.csv" if outdir else "mode_contributions_at_300K.csv",
                  ["phonon_branch", "contribution_percentage"], rows)

if __name__ == "__main__":
    main()
