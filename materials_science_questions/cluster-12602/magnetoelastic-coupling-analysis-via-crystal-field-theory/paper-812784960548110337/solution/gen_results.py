import csv
import os

output_dir = "/app/outputs"
filename = "bond_model_results.csv"

deltas = [round(i*0.005, 5) for i in range(0, 11)]
distortions = ["Ag1", "Ag2", "Ag3", "Ag4"]
elements = ["xxxz", "xxyy", "xzzz", "yxxx", "yyyz", "zzxx", "zzxy", "zzzz"]

def delta_chi(dtype, tensor, delta):
    if dtype == "Ag1":
        if tensor in ("xxxz", "yyyz"):
            return delta
        else:
            return 0.0
    elif dtype == "Ag2":
        if tensor == "zzzz":
            return delta
        else:
            return 0.0
    elif dtype in ("Ag3", "Ag4"):
        return delta
    else:
        return 0.0

rows = []
for dtype in distortions:
    for tensor in elements:
        for d in deltas:
            rows.append([dtype, tensor, d, delta_chi(dtype, tensor, d)])

with open(os.path.join(output_dir, filename), 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(["distortion_type", "tensor_element", "delta", "delta_chi"])
    writer.writerows(rows)
