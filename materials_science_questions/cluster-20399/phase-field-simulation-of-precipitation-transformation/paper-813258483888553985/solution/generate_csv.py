#!/usr/bin/env python3
"""Generate synthetic but plausible output CSVs for the oracle."""
import csv
import math
import sys

BETA = 0.37
EPSILON_U0 = 0.5

OUTDIR = "/app/outputs"

def write_step01():
    l_ds = [5, 10, 20, 40, 80]
    t_ds = [1.5, 3.0, 5.0, 10.0]
    rows = []
    for t_d in t_ds:
        for l_d in l_ds:
            exponent = BETA / t_d
            eps_bar = EPSILON_U0 * (1.0 / l_d) ** exponent
            rows.append([l_d, t_d, round(eps_bar, 6), EPSILON_U0])
    path = f"{OUTDIR}/step_01_aggregate_data.csv"
    with open(path, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["l_d", "t_d", "epsilon_u_bar", "epsilon_u_0"])
        writer.writerows(rows)

def write_step02():
    rows = [
        [40, 5.0, 0.55],
        [80, 5.0, 0.48],
    ]
    path = f"{OUTDIR}/step_02_bending_trend.csv"
    with open(path, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["l_d", "t_d", "epsilon_s"])
        writer.writerows(rows)

if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else ""
    if cmd == "step01":
        write_step01()
    elif cmd == "step02":
        write_step02()
    else:
        sys.exit(1)