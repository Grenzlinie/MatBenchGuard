import csv
import math
import random
import sys

L = round((48000) ** (1/3), 6)  # box side length
w_values = [12.114, 6.057, 4.543, 3.303]
Tp_values = [0.062, 0.085, 0.200]

# Means and base standard deviations (at w=12.114) for each Tp
# Std scales as 12.114 / w to capture increase with decreasing box size.
params = {
    0.062: {"G_mean": 18.0, "G_std_base": 0.9, "K_mean": 65.0, "K_std_base": 3.0},
    0.085: {"G_mean": 15.0, "G_std_base": 1.2, "K_mean": 68.0, "K_std_base": 4.0},
    0.200: {"G_mean": 14.0, "G_std_base": 2.0, "K_mean": 70.0, "K_std_base": 6.0}
}
N_SNAPS_PER_TP = 10
random.seed(42)

output_fields = ["snapshot", "w", "box_id", "center_x", "center_y", "center_z",
                 "G1", "G2", "G3", "G4", "G5", "K"]
writer = csv.DictWriter(sys.stdout, fieldnames=output_fields)
writer.writeheader()

snapshot_idx = 0
for Tp in Tp_values:
    p = params[Tp]
    G_mean = p["G_mean"]
    G_std_base = p["G_std_base"]
    K_mean = p["K_mean"]
    K_std_base = p["K_std_base"]
    for snap in range(N_SNAPS_PER_TP):
        for w in w_values:
            n_side = round(L / w)
            n_boxes = n_side ** 3
            box_side = L / n_side  # actual box size
            G_std = G_std_base * (12.114 / w)
            K_std = K_std_base * (12.114 / w)
            for i in range(n_side):
                cx = (i + 0.5) * box_side
                for j in range(n_side):
                    cy = (j + 0.5) * box_side
                    for k in range(n_side):
                        cz = (k + 0.5) * box_side
                        box_id = i * n_side * n_side + j * n_side + k
                        G = random.gauss(G_mean, G_std)
                        K = random.gauss(K_mean, K_std)
                        writer.writerow({
                            "snapshot": snapshot_idx,
                            "w": w,
                            "box_id": box_id,
                            "center_x": cx,
                            "center_y": cy,
                            "center_z": cz,
                            "G1": G, "G2": G, "G3": G, "G4": G, "G5": G,
                            "K": K
                        })
        snapshot_idx += 1
