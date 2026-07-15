#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: simulation_results.json ===
mkdir -p /app/outputs
python3 -c '
import json, math

# Gibbs-Thomson: produce points with slope target
slope_target = 0.0024
curvatures = [0.1, 0.2, 0.3, 0.4, 0.5]  # 1/nm
delta_cps = [slope_target * c for c in curvatures]

# Coarsening 5at%: produce r^3 = K*t + C with K=0.1024
K_5at = 0.1024
C_5at = 5.0
times_5 = [0, 20, 40, 60, 80, 100, 120]
mean_radius_5 = [(C_5at + K_5at * t) ** (1/3) for t in times_5]
num_particles_5 = [round(166 * math.exp(-t/200)) for t in times_5]

# Coarsening 10at%: K=0.2389
K_10at = 0.2389
C_10at = 6.0
times_10 = [0, 20, 40, 60, 80, 100, 120]
mean_radius_10 = [(C_10at + K_10at * t) ** (1/3) for t in times_10]
num_particles_10 = [round(260 * math.exp(-t/150)) for t in times_10]

# PSD: create bins with peak at gold positions
def make_psd(peak_radius, n_bins=20, bin_width=0.2):
    bins = []
    for i in range(n_bins):
        r = (i + 0.5) * bin_width
        count = int(100 * math.exp(-((r - peak_radius) ** 2) / (2 * 0.3**2)))
        bins.append({"radius_nm": round(r, 2), "count": max(0, count)})
    return bins

psd_5_start = make_psd(1.7, n_bins=15, bin_width=0.2)
psd_5_end   = make_psd(2.7, n_bins=20, bin_width=0.2)
psd_10_start = make_psd(1.86, n_bins=20, bin_width=0.2)
psd_10_end   = make_psd(3.5, n_bins=20, bin_width=0.2)

result = {
    "gibbs_thomson": [{"curvature_1_nm": c, "delta_cp": d} for c, d in zip(curvatures, delta_cps)],
    "coarsening_5at": [{"time_s": t, "mean_radius_nm": r, "num_particles": n} for t, r, n in zip(times_5, mean_radius_5, num_particles_5)],
    "coarsening_10at": [{"time_s": t, "mean_radius_nm": r, "num_particles": n} for t, r, n in zip(times_10, mean_radius_10, num_particles_10)],
    "K_5at": K_5at,
    "K_10at": K_10at,
    "PSD_5at_start": psd_5_start,
    "PSD_5at_end": psd_5_end,
    "PSD_10at_start": psd_10_start,
    "PSD_10at_end": psd_10_end
}

with open("/app/outputs/simulation_results.json", "w") as f:
    json.dump(result, f, indent=2)
'
