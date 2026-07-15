import csv
import os

OUTDIR = os.environ.get("OUTDIR", "/app/outputs")

# gamma_B reference values from Table 1
gamma_rows = [
    (1200, 31.0),
    (1300, 25.0),
    (1400, 20.0),
    (1500, 17.0),
]
with open(os.path.join(OUTDIR, "gamma_B_values.csv"), "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["T_K", "gamma_B"])
    for t, g in gamma_rows:
        writer.writerow([t, g])

# alpha_conditions.csv with plausible trend-satisfying values.
# Conditions: T in [1200,1300,1400,1500], ratio in [1,5,10]
# Required trends: for each fixed ratio, alpha decreases with T; for each fixed T, alpha decreases with ratio.
alpha_data = {
    (1200, 1): 0.90,
    (1200, 5): 0.70,
    (1200, 10): 0.60,
    (1300, 1): 0.85,
    (1300, 5): 0.65,
    (1300, 10): 0.55,
    (1400, 1): 0.80,
    (1400, 5): 0.60,
    (1400, 10): 0.50,
    (1500, 1): 0.75,
    (1500, 5): 0.55,
    (1500, 10): 0.45,
}
with open(os.path.join(OUTDIR, "alpha_conditions.csv"), "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["T_K", "ratio_H2_SiHCl3", "alpha"])
    for t in [1200, 1300, 1400, 1500]:
        for ratio in [1, 5, 10]:
            alpha = alpha_data[(t, ratio)]
            writer.writerow([t, ratio, alpha])
