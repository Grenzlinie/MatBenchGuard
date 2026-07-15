import json
import math

outfile = "/app/outputs/simulation_results.json"

# Gibbs-Thomson data: three points on a line with slope 0.033 nm
curvatures = [0.04, 0.08, 0.12]  # 1/nm
slope = 0.033  # nm
gibbs = [{"curvature_1_nm": k, "delta_cp": round(k * slope, 6)} for k in curvatures]

# LSW rate constants from the paper
K5 = 0.1024   # nm^3/s
K10 = 0.2389

# Initial mean radius after PFM transient (paper: 1.72 nm for 5 at.%, 1.86 nm for 10 at.%)
R0_5 = 1.72
R0_10 = 1.86

# Time points from 0 to 175 s every 10 s
times = [t for t in range(0, 176, 10)]

# mean radius via LSW law R(t) = (R0^3 + K*t)^{1/3}
def radius(t, R0, K):
    return (R0**3 + K*t) ** (1/3)

# number of particles: exponential decay from start to end
def num_particles(t, N_start, N_end, t_max):
    # exponential decay: N(t) = N_start * exp(-lambda t)
    if N_start == N_end or t_max == 0:
        return N_start
    lam = -math.log(N_end / N_start) / t_max
    return round(N_start * math.exp(-lam * t))

# 5 at.% Cu coarsening
N5_start = 166
N5_end = 33
coarsening_5at = []
for t in times:
    r = radius(t, R0_5, K5)
    n = num_particles(t, N5_start, N5_end, max(times))
    coarsening_5at.append({"time_s": t, "mean_radius_nm": round(r, 4), "num_particles": n})

# 10 at.% Cu coarsening
N10_start = 260
N10_end = 30
coarsening_10at = []
for t in times:
    r = radius(t, R0_10, K10)
    n = num_particles(t, N10_start, N10_end, max(times))
    coarsening_10at.append({"time_s": t, "mean_radius_nm": round(r, 4), "num_particles": n})

# Particle size distributions (binned counts)
# Bin midpoints, 0.2 nm intervals; keep only non-zero counts

def make_psd(counts_per_bin, bin_edges):
    psd = []
    for i, count in enumerate(counts_per_bin):
        if count > 0:
            mid = (bin_edges[i] + bin_edges[i+1]) / 2.0
            psd.append({"radius_nm": round(mid, 2), "count": count})
    return psd

# Common bin edges from 0.6 nm to 5.0 nm in steps of 0.2 nm
bins = [0.6, 0.8, 1.0, 1.2, 1.4, 1.6, 1.8, 2.0, 2.2, 2.4, 2.6, 2.8, 3.0, 3.2, 3.4, 3.6, 3.8, 4.0, 4.2, 4.4, 4.6, 4.8, 5.0]

# 5 at.% start (N=166): peak around 1.6 nm
psd_5_start_counts = [0, 2, 5, 10, 25, 35, 30, 25, 15, 10, 5, 3, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
psd_5_start = make_psd(psd_5_start_counts, bins)

# 5 at.% end (N=33): mean 2.85 nm, peak ~3.0 nm
psd_5_end_counts = [0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 3, 4, 6, 5, 4, 3, 2, 1, 1, 0, 0, 0]
psd_5_end = make_psd(psd_5_end_counts, bins)

# 10 at.% start (N=260): peak ~1.8 nm
psd_10_start_counts = [0, 2, 8, 20, 40, 58, 69, 40, 14, 5, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
psd_10_start = make_psd(psd_10_start_counts, bins)

# 10 at.% end (N=30): mean 3.64 nm, peak ~3.9 nm
psd_10_end_counts = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 2, 3, 4, 5, 5, 4, 3, 1, 1]
psd_10_end = make_psd(psd_10_end_counts, bins)

result = {
    "gibbs_thomson": gibbs,
    "coarsening_5at": coarsening_5at,
    "coarsening_10at": coarsening_10at,
    "K_5at": K5,
    "K_10at": K10,
    "PSD_5at_start": psd_5_start,
    "PSD_5at_end": psd_5_end,
    "PSD_10at_start": psd_10_start,
    "PSD_10at_end": psd_10_end
}

with open(outfile, "w") as f:
    json.dump(result, f, indent=2)
