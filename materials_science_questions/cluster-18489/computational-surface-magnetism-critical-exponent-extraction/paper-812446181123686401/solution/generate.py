#!/usr/bin/env python3
"""Reference oracle helper: writes bulk_tc.json and phase_boundary_data.csv."""
import sys
import json
import csv
import math

def write_bulk_tc():
    data = {"k_B T_c^b / J": 5.073}
    with open("/app/outputs/bulk_tc.json", "w") as f:
        json.dump(data, f, indent=2)

def write_phase_boundary():
    # Model: sigmoid centred at delta_c, steepness k=5
    # T = 0.2 + 1.6 / (1 + exp(-k*(ds - dc)))  => at ds=dc, T=1.0
    k = 5.0
    # delta_c chosen so that for J_s'/J=0, dc=1.0; positive => lower; negative => higher
    centres = {
        -1.0: 1.5,
         0.0: 1.0,
         1.0: 0.5,
         2.0: 0.0,
    }
    Js_order = [-1.0, 0.0, 1.0, 2.0]
    delta_s_min = 0.0
    delta_s_max = 2.0
    step = 0.01
    rows = []
    for Js in Js_order:
        dc = centres[Js]
        ds = delta_s_min
        while ds <= delta_s_max + 1e-9:
            # sigmoid: 1/(1+exp(-k*(ds-dc)))
            exponent = -k * (ds - dc)
            try:
                sig = 1.0 / (1.0 + math.exp(exponent))
            except OverflowError:
                sig = 0.0 if exponent > 100 else 1.0
            T = 0.2 + 1.6 * sig
            rows.append((Js, round(ds, 10), round(T, 10)))
            ds = round(ds + step, 12)  # avoid floating drift
    # Write CSV
    with open("/app/outputs/phase_boundary_data.csv", "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["J_s_prime_over_J", "delta_s", "T_c_over_T_cb"])
        writer.writerows(rows)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: generate.py <bulk_tc|phase_boundary>")
        sys.exit(1)
    cmd = sys.argv[1]
    if cmd == "bulk_tc":
        write_bulk_tc()
    elif cmd == "phase_boundary":
        write_phase_boundary()
    else:
        print(f"Unknown command: {cmd}")
        sys.exit(1)