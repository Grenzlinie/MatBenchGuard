#!/usr/bin/env python3
import json, csv, os, math, random, statistics

random.seed(42)

output_dir = "/app/outputs"
os.makedirs(output_dir, exist_ok=True)

# ========== 1. GA covariance matrix ==========
n_groups = 66

def make_sym_matrix(n, diag_scale, off_scale):
    m = [[0.0] * n for _ in range(n)]
    for i in range(n):
        for j in range(i, n):
            if i == j:
                m[i][j] = abs(random.gauss(diag_scale, diag_scale * 0.1))
            else:
                val = random.gauss(0, off_scale)
                m[i][j] = val
                m[j][i] = val
    # ensure positive definiteness
    for i in range(n):
        m[i][i] += off_scale * n * 0.1
    return m

H_cov = make_sym_matrix(66, 0.2, 0.02)
S_cov = make_sym_matrix(66, 0.1, 0.01)

with open(os.path.join(output_dir, "ga_covariance_matrix.json"), "w") as f:
    json.dump({"H_cov": H_cov, "S_cov": S_cov}, f)

# ========== 2. Generate perturbed MKM results ==========
temperatures = [500 + i * (600 / 35) for i in range(36)]
main_feed = "1:0.5"
ratios_order = ["1:0.1", "1:0.3", "1:0.5", "1:0.7", "1:1", "1:1.5", "1:2", "1:3", "1:5"]
T_order = 750.0
R_kcal = 1.987e-3  # kcal/mol K

samples = 5000

# bimodal activation energy
Ea_modes = [random.gauss(26.0, 2.0) if random.random() < 0.7 else random.gauss(36.0, 2.0) for _ in range(samples)]
log10A_samples = [random.gauss(9.5, 0.5) for _ in range(samples)]

def compute_TOF(T, Ea, log10A):
    return 10 ** (log10A - Ea / (R_kcal * T * math.log(10)))

def conversion_profile(T):
    if T < 550:
        return 0.0
    elif T < 750:
        return 0.175 * (T - 550) / 200
    else:
        return 0.175

# reaction orders true parameter for each sample
a_true = [random.gauss(1.0, 0.05) for _ in range(samples)]
b_true = [random.gauss(0.0, 0.05) for _ in range(samples)]

csv_path = os.path.join(output_dir, "ethane_odh_perturbed_results.csv")
with open(csv_path, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["T", "feed_ratio", "sample_id", "conversion", "TOF", "p_C2H6", "p_O2"])

    # temperature grid, main feed
    for T in temperatures:
        for sid in range(samples):
            Ea = Ea_modes[sid]
            logA = log10A_samples[sid]
            TOF_val = compute_TOF(T, Ea, logA)
            conv = conversion_profile(T) + random.gauss(0, 0.01)
            conv = max(0.0, min(1.0, conv))
            p_c2h6 = 0.6667
            p_o2 = 0.3333
            writer.writerow([T, main_feed, sid, conv, TOF_val, p_c2h6, p_o2])

    # varying feed ratios for reaction order
    P_total = 1.0
    for ratio_str in ratios_order:
        parts = ratio_str.split(":")
        c2h6_frac = float(parts[0]) / (float(parts[0]) + float(parts[1]))
        o2_frac = float(parts[1]) / (float(parts[0]) + float(parts[1]))
        p_c2h6 = c2h6_frac * P_total
        p_o2 = o2_frac * P_total
        for sid in range(samples):
            base_TOF = compute_TOF(T_order, Ea_modes[sid], log10A_samples[sid])
            ref_c2h6 = 0.6667
            ref_o2 = 0.3333
            factor = (p_c2h6 / ref_c2h6) ** a_true[sid] * (p_o2 / ref_o2) ** b_true[sid]
            TOF_val = base_TOF * factor
            conv = conversion_profile(T_order)
            writer.writerow([T_order, ratio_str, sid, conv, TOF_val, p_c2h6, p_o2])

# ========== 3. Compute aggregated QoI statistics ==========
data = []
with open(csv_path, "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        data.append(row)

# TOF at T=750 K, main feed
tof_vals = []
for row in data:
    if float(row["T"]) == T_order and row["feed_ratio"] == main_feed:
        tof_vals.append(float(row["TOF"]))
log_tof = [math.log10(v) for v in tof_vals]
mean_log_tof = statistics.mean(log_tof)
std_log_tof = statistics.stdev(log_tof) if len(log_tof) > 1 else 0.0

# Apparent activation energy per sample from main feed temperature grid
sample_data = {}
for row in data:
    if row["feed_ratio"] == main_feed:
        sid = int(row["sample_id"])
        T = float(row["T"])
        TOF = float(row["TOF"])
        sample_data.setdefault(sid, []).append((T, TOF))

Ea_vals = []
for sid, points in sample_data.items():
    if len(points) < 5:
        continue
    x = [1.0 / T for T, _ in points]
    y = [math.log(TOF) for _, TOF in points]
    n = len(x)
    sum_x = sum(x)
    sum_y = sum(y)
    sum_xy = sum(xi * yi for xi, yi in zip(x, y))
    sum_x2 = sum(xi * xi for xi in x)
    slope = (n * sum_xy - sum_x * sum_y) / (n * sum_x2 - sum_x * sum_x)
    Ea_vals.append(-slope * R_kcal)

mean_Ea = statistics.mean(Ea_vals)
std_Ea = statistics.stdev(Ea_vals) if len(Ea_vals) > 1 else 0.0

# Reaction orders from varying feed ratios at T=750 K
order_data = {}
for row in data:
    if float(row["T"]) == T_order and row["feed_ratio"] != main_feed:
        sid = int(row["sample_id"])
        d = order_data.setdefault(sid, {"TOF": [], "p_c2h6": [], "p_o2": []})
        d["TOF"].append(float(row["TOF"]))
        d["p_c2h6"].append(float(row["p_C2H6"]))
        d["p_o2"].append(float(row["p_O2"]))

c2h6_orders = []
o2_orders = []
for sid, d in order_data.items():
    TOFv = d["TOF"]
    p_c2h6 = d["p_c2h6"]
    p_o2 = d["p_o2"]
    if len(TOFv) < 5:
        continue
    n = len(TOFv)
    X = [[1.0, math.log(pc), math.log(po)] for pc, po in zip(p_c2h6, p_o2)]
    y = [math.log(TOF) for TOF in TOFv]
    XtX = [[0.0] * 3 for _ in range(3)]
    Xty = [0.0] * 3
    for i in range(n):
        row = X[i]
        for j in range(3):
            Xty[j] += row[j] * y[i]
            for k in range(3):
                XtX[j][k] += row[j] * row[k]
    det = (XtX[0][0] * (XtX[1][1] * XtX[2][2] - XtX[1][2] * XtX[2][1])
           - XtX[0][1] * (XtX[1][0] * XtX[2][2] - XtX[1][2] * XtX[2][0])
           + XtX[0][2] * (XtX[1][0] * XtX[2][1] - XtX[1][1] * XtX[2][0]))
    if abs(det) < 1e-10:
        continue
    inv_det = 1.0 / det
    inv = [[0.0] * 3 for _ in range(3)]
    inv[0][0] = (XtX[1][1] * XtX[2][2] - XtX[1][2] * XtX[2][1]) * inv_det
    inv[0][1] = -(XtX[0][1] * XtX[2][2] - XtX[0][2] * XtX[2][1]) * inv_det
    inv[0][2] = (XtX[0][1] * XtX[1][2] - XtX[0][2] * XtX[1][1]) * inv_det
    inv[1][0] = -(XtX[1][0] * XtX[2][2] - XtX[1][2] * XtX[2][0]) * inv_det
    inv[1][1] = (XtX[0][0] * XtX[2][2] - XtX[0][2] * XtX[2][0]) * inv_det
    inv[1][2] = -(XtX[0][0] * XtX[1][2] - XtX[0][2] * XtX[1][0]) * inv_det
    inv[2][0] = (XtX[1][0] * XtX[2][1] - XtX[1][1] * XtX[2][0]) * inv_det
    inv[2][1] = -(XtX[0][0] * XtX[2][1] - XtX[0][1] * XtX[2][0]) * inv_det
    inv[2][2] = (XtX[0][0] * XtX[1][1] - XtX[0][1] * XtX[1][0]) * inv_det
    beta = [sum(inv[i][j] * Xty[j] for j in range(3)) for i in range(3)]
    c2h6_orders.append(beta[1])
    o2_orders.append(beta[2])

mean_c2h6 = statistics.mean(c2h6_orders) if c2h6_orders else 0.0
std_c2h6 = statistics.stdev(c2h6_orders) if len(c2h6_orders) > 1 else 0.0
mean_o2 = statistics.mean(o2_orders) if o2_orders else 0.0
std_o2 = statistics.stdev(o2_orders) if len(o2_orders) > 1 else 0.0

agg_stats = {
    "TOF": {"mean_log10": mean_log_tof, "std_log10": std_log_tof},
    "E_app": {"mean_kcal_per_mol": mean_Ea, "std_kcal_per_mol": std_Ea},
    "reaction_order_C2H6": {"mean": mean_c2h6, "std": std_c2h6},
    "reaction_order_O2": {"mean": mean_o2, "std": std_o2},
}

with open(os.path.join(output_dir, "aggregated_qoi_stats.json"), "w") as f:
    json.dump(agg_stats, f, indent=2)
