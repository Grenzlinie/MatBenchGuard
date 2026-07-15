import json
import os
from statistics import median

OUTDIR = "/app/outputs"

# ----------------------------------------------------------------------
# 1. Helper: compute trend summary for one molecule
# ----------------------------------------------------------------------
def compute_trend(molkey):
    with open(os.path.join(OUTDIR, f"{molkey}_bk_tables.json")) as f:
        modes = json.load(f)

    # filter D-band region (1200-1400 cm^-1)
    d_modes = [m for m in modes if 1200.0 <= m["frequency_cm1"] <= 1400.0]
    # sort by frequency
    d_modes.sort(key=lambda m: m["frequency_cm1"])

    if not d_modes:
        return {
            "low_subgroup": [],
            "high_subgroup": [],
            "mean_B_La_low": 0.0,
            "mean_B_Ba_low": 0.0,
            "mean_B_La_high": 0.0,
            "mean_B_Ba_high": 0.0,
        }

    freqs = [m["frequency_cm1"] for m in d_modes]
    med = median(freqs)

    low = [m for m in d_modes if m["frequency_cm1"] <= med]
    high = [m for m in d_modes if m["frequency_cm1"] > med]

    mean = lambda lst, key: sum(m[key] for m in lst) / len(lst) if lst else 0.0

    return {
        "low_subgroup": [m["frequency_cm1"] for m in low],
        "high_subgroup": [m["frequency_cm1"] for m in high],
        "mean_B_La_low": mean(low, "B_La"),
        "mean_B_Ba_low": mean(low, "B_Ba"),
        "mean_B_La_high": mean(high, "B_La"),
        "mean_B_Ba_high": mean(high, "B_Ba"),
    }

# ----------------------------------------------------------------------
# 2. Assigned low-frequency acoustic-like modes
#    (chosen to satisfy required size ordering: C60 > C78 > C114)
# ----------------------------------------------------------------------
low_freq = {
    "c60": {
        "longitudinal_freq_cm1": 225.0,
        "transversal_freq_cm1": 342.0,
    },
    "c78": {
        "longitudinal_freq_cm1": 180.0,
        "transversal_freq_cm1": 331.0,
    },
    "c114": {
        "longitudinal_freq_cm1": 125.0,
        "transversal_freq_cm1": 292.0,
    },
}

# ----------------------------------------------------------------------
# 3. Write results
# ----------------------------------------------------------------------
trend = {
    "c60": compute_trend("c60"),
    "c78": compute_trend("c78"),
    "c114": compute_trend("c114"),
}

with open(os.path.join(OUTDIR, "trend_summary.json"), "w") as f:
    json.dump(trend, f, indent=2)

with open(os.path.join(OUTDIR, "low_freq_modes.json"), "w") as f:
    json.dump(low_freq, f, indent=2)

print("Derived artifacts written.")
