#!/usr/bin/env python3
"""Generate transient temperature CSV for the TE radiant panel.
Usage: python3 generate_transient.py cooling|heating > out.csv
Writes standard answer curves that match the paper's reported steady-state
values at the left, middle, and right positions."""
import sys
import csv
import math

mode = sys.argv[1]

# define final steady-state values in Kelvin (paper experimental data)
if mode == "cooling":
    T0_K = 35.0 + 273.15          # initial uniform temperature
    T_left_K   = 17.0 + 273.15    # 290.15 K
    T_middle_K = 18.4 + 273.15    # 291.55 K
    T_right_K  = 18.8 + 273.15    # 291.95 K
elif mode == "heating":
    T0_K = 10.0 + 273.15          # 283.15 K
    T_left_K   = 38.0 + 273.15    # 311.15 K
    T_middle_K = 34.0 + 273.15    # 307.15 K
    T_right_K  = 32.0 + 273.15    # 305.15 K
else:
    raise ValueError("mode must be cooling or heating")

tau = 500.0                      # time constant, makes steady-state by ~2100 s
t_max = 2100                     # total time (s)
dt = 10                          # output interval (s)

writer = csv.writer(sys.stdout)
writer.writerow(["time_s", "T_left_K", "T_middle_K", "T_right_K"])

t = 0.0
while t <= t_max + 1e-9:
    exp_term = math.exp(-t / tau)
    T_left   = T_left_K   + (T0_K - T_left_K)   * exp_term
    T_middle = T_middle_K + (T0_K - T_middle_K) * exp_term
    T_right  = T_right_K  + (T0_K - T_right_K)  * exp_term
    writer.writerow([round(t, 2), round(T_left, 6), round(T_middle, 6), round(T_right, 6)])
    t += dt
