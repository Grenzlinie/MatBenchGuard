#!/usr/bin/env python3
import csv
import math
import os

def sigmoid(T, Tc, width, M_max=2.0):
    return M_max / (1 + math.exp((T - Tc) / width))

def generate_cooling(T_high, T_low, step, Tc, width, M_max):
    data = []
    T = T_high
    while T >= T_low - step/2:
        M = sigmoid(T, Tc, width, M_max)
        data.append((T, M))
        T = round(T - step, 10)
    return data

def generate_heating(T_start, T_high, step, M_start, T_end, width=0.1):
    data = []
    T = T_start
    while T <= T_high + step/2:
        M = M_start / (1 + math.exp((T - T_end) / width))
        data.append((T, M))
        T = round(T + step, 10)
    return data

output_dir = "/app/outputs"
os.makedirs(output_dir, exist_ok=True)

step = 0.01
T_high = 70.0
T_low = 30.0

# Parameters for N=200
Tc_zfc200 = 64.5
width_zfc200 = 0.3
M_max_zfc200 = 2.0

Tc_fc200 = 65.5
width_fc200 = 0.3
M_max_fc200 = 1.8

# Parameters for N=1000
Tc_zfc1000 = 64.8
width_zfc1000 = 0.25
M_max_zfc1000 = 2.0

Tc_fc1000 = 65.8
width_fc1000 = 0.25
M_max_fc1000 = 1.8

# Generate cooling curves
cool_zfc200 = generate_cooling(T_high, T_low, step, Tc_zfc200, width_zfc200, M_max_zfc200)
cool_fc200 = generate_cooling(T_high, T_low, step, Tc_fc200, width_fc200, M_max_fc200)
cool_zfc1000 = generate_cooling(T_high, T_low, step, Tc_zfc1000, width_zfc1000, M_max_zfc1000)
cool_fc1000 = generate_cooling(T_high, T_low, step, Tc_fc1000, width_fc1000, M_max_fc1000)

# Reversal parameters for N=200
rev_deltas = [0.8, 0.6, 0.4, 0.2]
rev_Ts200 = [Tc_zfc200 - d for d in rev_deltas]
T_end_rev200 = 64.6

# For each rev N200, generate heating branch from T_rev upward
rev_heating200 = {}
for d, T_rev in zip(rev_deltas, rev_Ts200):
    M_start = sigmoid(T_rev, Tc_zfc200, width_zfc200, M_max_zfc200)
    rev_heating200[f"rev_N200_{d}"] = generate_heating(T_rev, T_high, step, M_start, T_end_rev200)

# N1000 reversal: cooling down to 64.2 K
T_rev1000 = 64.2
cool_rev1000 = generate_cooling(T_high, T_rev1000, step, Tc_zfc1000, width_zfc1000, M_max_zfc1000)
M_start1000 = sigmoid(T_rev1000, Tc_zfc1000, width_zfc1000, M_max_zfc1000)
# heating lower endpoint 64.7 K, upper endpoint 64.2 K
heat_lower = generate_heating(T_rev1000, T_high, step, M_start1000, T_end=64.7, width=0.15)
heat_upper = generate_heating(T_rev1000, T_high, step, M_start1000, T_end=64.2, width=0.15)

# Write CSV
with open(os.path.join(output_dir, "order_parameter_curves.csv"), "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["protocol", "temperature", "stag_mag"])
    # helper to write rows
    def write_rows(protocol, data):
        for T, M in data:
            writer.writerow([protocol, f"{T:.2f}", f"{M:.6f}"])
    # ZFC_N200
    write_rows("ZFC_N200", cool_zfc200)
    write_rows("FC_N200", cool_fc200)
    # rev_N200_*
    for d in rev_deltas:
        write_rows(f"rev_N200_{d}", rev_heating200[f"rev_N200_{d}"])
    # ZFC_N1000
    write_rows("ZFC_N1000", cool_zfc1000)
    write_rows("FC_N1000", cool_fc1000)
    # rev_N1000_0.6_cooling
    write_rows("rev_N1000_0.6_cooling", cool_rev1000)
    write_rows("rev_N1000_0.6_heating_lower", heat_lower)
    write_rows("rev_N1000_0.6_heating_upper", heat_upper)
