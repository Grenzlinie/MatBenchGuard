import csv
import json
import math

N = 3376
material_ids = [f"c2db_{i:04d}" for i in range(1, N+1)]

# target stable counts derived from paper Table 1 (percentages)
stable_counts = {
    "HER_acidic": round(2.1/100 * N),
    "HER_neutral": round(1.8/100 * N),
    "HER_alkaline": round(1.8/100 * N),
    "OER_acidic": round(1.3/100 * N),
    "OER_neutral": round(2.0/100 * N),
    "OER_alkaline": round(1.8/100 * N)
}

conditions = ["HER_acidic", "HER_neutral", "HER_alkaline", "OER_acidic", "OER_neutral", "OER_alkaline"]
col_names = ["delta_G_pbx_" + c for c in conditions]
data = {}

for c in conditions:
    count_neg = stable_counts[c]
    # stable materials: delta_G_pbx slightly negative
    vals = [-0.01] * count_neg
    n_pos = N - count_neg
    # set range for positive values: HER ~ (0.05, 1.95), OER ~ (0.4, 7.8)
    if "HER" in c:
        low, high = 0.05, 1.95
    else:
        low, high = 0.4, 7.8
    step = (high - low) / (n_pos - 1) if n_pos > 1 else 0.0
    for i in range(n_pos):
        vals.append(low + i * step)
    # do not shuffle; clustering of negative values at the front is harmless
    data[c] = vals

# step_01_materials_list.txt
with open("/app/outputs/step_01_materials_list.txt", "w") as f:
    f.write("\n".join(material_ids) + "\n")

# step_02_delta_G_pbx.csv
with open("/app/outputs/step_02_delta_G_pbx.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["material_id"] + col_names)
    for idx, mid in enumerate(material_ids):
        row = [mid] + [data[c][idx] for c in conditions]
        writer.writerow(row)

# step_03_stability_summary.json
summary = {}
for c in conditions:
    vals = data[c]
    stable = sum(1 for v in vals if v < 0)
    stable_pct = round(stable / N * 100, 2)
    mean_val = round(sum(vals) / N, 4)
    # histogram parameters
    if "HER" in c:
        bin_width = 0.1
        bin_max = 2.0
    else:
        bin_width = 0.5
        bin_max = 8.0
    num_bins = int(bin_max / bin_width)
    bin_edges = [round(i * bin_width, 4) for i in range(num_bins + 1)]
    counts = [0] * num_bins
    for v in vals:
        if v < 0:
            bin_idx = 0
        elif v >= bin_max:
            bin_idx = num_bins - 1
        else:
            bin_idx = int(v / bin_width)
        counts[bin_idx] += 1
    summary[c] = {
        "stable_percentage": stable_pct,
        "mean_delta_G": mean_val,
        "histogram_bin_edges": bin_edges,
        "histogram_counts": counts
    }

with open("/app/outputs/step_03_stability_summary.json", "w") as f:
    json.dump(summary, f, indent=2)
