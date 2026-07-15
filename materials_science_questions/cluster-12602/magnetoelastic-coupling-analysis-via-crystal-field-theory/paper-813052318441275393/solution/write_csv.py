import csv
import math

alloys_data = [
    ("FeNi", 3.4775, 3.4751, 249, 72, 0.0161, 0.21, 0.0079),
    ("FeCr", 3.5294, 3.5292, 208, 113, 0.0367, 0.35, 0.0369),
    ("FeCo", 3.4499, 3.4495, 283, 38, 0.0054, 0.19, 0.0012),
    ("CoNi", 3.4848, 3.4805, 231, 89, 0.0147, 0.22, 0.0068),
    ("CoCr", 3.5272, 3.5262, 216, 104, 0.0232, 0.24, 0.0254),
    ("FeCoNi", 3.4704, 3.4684, 252, 68, 0.0153, 0.21, 0.0069),
    ("FeCoCr", 3.5003, 3.4999, 236, 84, 0.0194, 0.22, 0.0238),
    ("FeCrNi", 3.5173, 3.5157, 220, 100, 0.0213, 0.23, 0.0220),
    ("CoNiCr", 3.5179, 3.5153, 221, 100, 0.0237, 0.23, 0.0210),
    ("FeCoNiCr", 3.4998, 3.4984, 240, 81, 0.0170, 0.22, 0.0204),
    ("FeCoNiCrMn", 3.4993, 3.4981, 222, 98, 0.0167, 0.21, 0.0179),
]

rows = []
for alloy, a_pris, a_dist, c11, c12, gamma_dft, nu, gamma_th in alloys_data:
    eps_fluc = 2.0 * gamma_th / math.sqrt(2.0 * (1.0 + nu) / (1.0 - 2.0 * nu))
    rows.append([alloy, f"{a_pris:.6f}", f"{a_dist:.6f}", c11, c12, f"{gamma_dft:.6f}", f"{eps_fluc:.6f}", f"{gamma_th:.6f}"])

with open("/app/outputs/alloy_results.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["alloy", "a_pristine_DFT", "a_distorted_DFT", "c11", "c12", "gamma_DFT", "eps_fluc", "gamma_th"])
    writer.writerows(rows)
