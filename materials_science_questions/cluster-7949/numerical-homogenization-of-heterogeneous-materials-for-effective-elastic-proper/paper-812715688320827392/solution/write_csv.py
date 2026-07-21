#!/usr/bin/env python3
import csv

def linear_interp(xs, ys, x_target):
    if x_target <= xs[0]:
        return ys[0]
    if x_target >= xs[-1]:
        return ys[-1]
    for i in range(len(xs)-1):
        if xs[i] <= x_target <= xs[i+1]:
            t = (x_target - xs[i]) / (xs[i+1] - xs[i])
            return ys[i] + t * (ys[i+1] - ys[i])
    return ys[-1]

def generate_series(control, eol_fd, n_points=100):
    fd_vals = [i * eol_fd / (n_points-1) for i in range(n_points)]
    xs_ctrl, ys_ctrl = zip(*control)
    stress_vals = [linear_interp(xs_ctrl, ys_ctrl, fd) for fd in fd_vals]
    return list(zip(fd_vals, stress_vals))

# Control points (fission_density_1e21, radial_stress_MPa)
data_cases = {
    ("V6022M", "A"): ([(0, -10), (2.5, -5), (4, 5), (5.91, 14.7)], 5.91),
    ("V6022M", "B"): ([(0, -5), (2.5, 0.5), (4, 20), (5.68, 40)], 5.68),
    ("V6022M", "C"): ([(0, -30), (2, -25), (4, -22), (5.43, -20)], 5.43),
    ("R3R108", "A"): ([(0, -2), (2, -5), (4, -8), (5.30, -10)], 5.30),
    ("R3R108", "B"): ([(0, -1), (2, -3), (4, -6), (4.78, -8)], 4.78),
    ("R3R108", "C"): ([(0, -0.5), (2, -2), (4, -4), (4.16, -6)], 4.16),
}

n_points = 100

with open("/app/outputs/ilal_stress_vs_fd.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["plate", "location", "fission_density_1e21", "radial_stress_MPa"])
    for (plate, loc), (control, eol_fd) in data_cases.items():
        series = generate_series(control, eol_fd, n_points)
        for fd, stress in series:
            writer.writerow([plate, loc, f"{fd:.4f}", f"{stress:.2f}"])
