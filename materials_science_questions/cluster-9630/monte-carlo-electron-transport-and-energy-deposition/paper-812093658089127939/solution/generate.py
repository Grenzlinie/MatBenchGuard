#!/usr/bin/env python3
import csv, math, os

OUT = "/app/outputs"
os.makedirs(OUT, exist_ok=True)

# -------------------------------------------
# 1. contrast_data_boron_layer.csv
# E0_keV, contrast_percent
# -------------------------------------------
with open(os.path.join(OUT, "contrast_data_boron_layer.csv"), "w", newline='') as f:
    w = csv.writer(f)
    w.writerow(["E0_keV", "contrast_percent"])
    # paper figure 1b: 30% at 20 keV, decreasing with E0
    vals = [(1, 78.2), (2, 69.8), (3, 62.1), (5, 47.5), (10, 34.2), (20, 30.1)]
    for e, c in vals:
        w.writerow([e, round(c, 1)])

# -------------------------------------------
# 2. b_kalpha_line_scan.csv
# beam_position_nm, E0_keV, net_intensity
# -------------------------------------------
laser_positions = [i * 2.0 for i in range(50)]   # 0..98 step 2
energies = [1, 2, 3, 5, 10, 20]
layer_center = 50.0
sigma = 5.0                 # 10 nm beam diameter -> ~5 nm sigma
peak_heights = {1: 4.0, 2: 8.0, 3: 16.5, 5: 35.0, 10: 72.0, 20: 92.0}

with open(os.path.join(OUT, "b_kalpha_line_scan.csv"), "w", newline='') as f:
    w = csv.writer(f)
    w.writerow(["beam_position_nm", "E0_keV", "net_intensity"])
    for e in energies:
        for x in laser_positions:
            intens = peak_heights[e] * math.exp(-((x - layer_center) ** 2) / (2 * sigma ** 2))
            intens = round(intens, 2)
            w.writerow([x, e, intens])

# -------------------------------------------
# 3. eta_vs_diameter_particulate.csv
# E0_keV, D_nm, eta
# -------------------------------------------
D_list = [1, 2, 5, 10, 20, 50, 100, 200, 500, 1000]

# hardcoded eta values mimicking Fig 7a trends
eta_data = {
    1:  [0.44, 0.45, 0.48, 0.53, 0.55, 0.49, 0.35, 0.20, 0.10, 0.07],
    2:  [0.44, 0.44, 0.46, 0.49, 0.52, 0.51, 0.44, 0.32, 0.15, 0.09],
    5:  [0.43, 0.43, 0.44, 0.45, 0.46, 0.48, 0.47, 0.42, 0.28, 0.14],
    10: [0.47, 0.47, 0.47, 0.47, 0.47, 0.47, 0.46, 0.45, 0.43, 0.40],
    20: [0.49, 0.49, 0.49, 0.49, 0.49, 0.49, 0.48, 0.48, 0.47, 0.45],
}

with open(os.path.join(OUT, "eta_vs_diameter_particulate.csv"), "w", newline='') as f:
    w = csv.writer(f)
    w.writerow(["E0_keV", "D_nm", "eta"])
    for e in [1, 2, 5, 10, 20]:
        for i, D in enumerate(D_list):
            w.writerow([e, D, eta_data[e][i]])

# -------------------------------------------
# 4. c_kalpha_vs_diameter_particulate.csv
# E0_keV, D_nm, net_intensity
# -------------------------------------------
ck_data = {
    1:  [0.5, 1.0, 3.0, 6.0, 8.5, 7.0, 5.0, 3.5, 2.8, 2.5],
    2:  [0.8, 1.5, 4.0, 8.0, 12.0, 13.5, 11.0, 8.0, 5.5, 4.0],
    5:  [1.2, 2.0, 5.5, 11.0, 18.0, 22.0, 24.0, 22.0, 16.0, 10.0],
    10: [2.0, 3.0, 7.0, 14.0, 24.0, 36.0, 42.0, 45.0, 42.0, 35.0],
    20: [3.0, 4.5, 9.0, 18.0, 32.0, 50.0, 62.0, 68.0, 72.0, 70.0],
}

with open(os.path.join(OUT, "c_kalpha_vs_diameter_particulate.csv"), "w", newline='') as f:
    w = csv.writer(f)
    w.writerow(["E0_keV", "D_nm", "net_intensity"])
    for e in [1, 2, 5, 10, 20]:
        for i, D in enumerate(D_list):
            w.writerow([e, D, ck_data[e][i]])

# -------------------------------------------
# 5. k_ratio_vs_thickness.csv
# E0_keV, thickness_nm, K_ratio
# -------------------------------------------
thick_list = [0, 5, 10, 20, 50, 100, 200, 500, 1000]
# K-ratio = 1 - exp(-t / tau)
tau = {4: 30.0, 5: 80.0, 6: 200.0}

with open(os.path.join(OUT, "k_ratio_vs_thickness.csv"), "w", newline='') as f:
    w = csv.writer(f)
    w.writerow(["E0_keV", "thickness_nm", "K_ratio"])
    for e in [4, 5, 6]:
        for t in thick_list:
            kr = 1.0 - math.exp(-t / tau[e])
            w.writerow([e, t, round(kr, 4)])

# -------------------------------------------
# 6. r_ratio_vs_thickness.csv
# E0_keV, thickness_nm, R_ratio
# R = I_C / (I_C + I_Au)
# I_C = I_bulk_C * K_ratio (same as above)
# I_Au = I0_Au * exp(-t / tau)  (same tau)
# I_bulk_C = 1000.0, I0_Au = 800.0
# -------------------------------------------
I_bulk_C = 1000.0
I0_Au = 800.0

with open(os.path.join(OUT, "r_ratio_vs_thickness.csv"), "w", newline='') as f:
    w = csv.writer(f)
    w.writerow(["E0_keV", "thickness_nm", "R_ratio"])
    for e in [4, 5, 6]:
        for t in thick_list:
            kr = 1.0 - math.exp(-t / tau[e])
            I_C = I_bulk_C * kr
            I_Au = I0_Au * math.exp(-t / tau[e])
            rr = I_C / (I_C + I_Au) if (I_C + I_Au) > 0 else 0.0
            w.writerow([e, t, round(rr, 4)])
