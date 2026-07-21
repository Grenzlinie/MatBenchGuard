import sys, math

n_points = 100
x_min = 0.5
x_max = 5.0
dx = (x_max - x_min) / (n_points - 1)

def baseline(x):
    return 1.0

def bump(x, center, height, sigma):
    return height * math.exp(-((x - center) ** 2) / (2 * sigma ** 2))

bumps_params = [(1, 0.3, 0.05), (2, 0.3, 0.05), (3, 0.3, 0.05), (4, 0.3, 0.05)]

print("omega_over_Omega_n,relative_current")
for i in range(n_points):
    x = x_min + i * dx
    y = baseline(x) + sum(bump(x, c, h, s) for c, h, s in bumps_params)
    print(f"{x:.6f},{y:.6f}")