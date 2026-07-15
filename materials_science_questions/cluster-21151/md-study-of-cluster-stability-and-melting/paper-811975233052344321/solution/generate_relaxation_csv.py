import sys, os, csv, numpy as np

outdir = sys.argv[1]
filepath = os.path.join(outdir, "relaxation_results.csv")

# Time points (MCS/particle)
t = np.logspace(-1, 4, 200)  # from 0.1 to 10000
# Add t=0 at front
t = np.concatenate([[0], t])

# Helper function for cluster count with overshoot
def cluster_count(t, final_count, peak, t_peak, sigma, t_rise):
    # base sigmoidal rise from 1 to final_count
    base = 1.0 + (final_count - 1.0) * (t / (t + t_rise))
    # Gaussian overshoot bump
    overshoot = (peak - final_count) * np.exp(-((t - t_peak)**2) / (2 * sigma**2))
    # Ensure no negative overshoot, start from 1
    count = base + overshoot
    # At t=0, base=1 and overshoot small, so clip to >=1
    count = np.maximum(count, 1.0)
    return count

# Energy multi-exponential decay
def energy(t, e0, e_mid, e_final, tau_fast, tau_slow):
    fast_component = (e0 - e_mid) * np.exp(-t / tau_fast)
    slow_component = (e_mid - e_final) * np.exp(-t / tau_slow)
    return e_final + slow_component + fast_component

# Fractal dimension with small fluctuations
def fractal_dim(t):
    np.random.seed(42)
    base = 1.70
    noise = 0.02 * np.random.randn(len(t))
    return base + noise

# Define conditions
conditions = [
    (8, 0.0, 20, 50, 0.5, 0.3, 0.2, -1.0, -1.4, -1.8, 1.0, 100),
    (36, 0.0, 40, 90, 0.4, 0.25, 0.2, -1.0, -1.6, -2.4, 0.8, 80),
    (36, 0.1, 30, 70, 0.45, 0.3, 0.2, -1.0, -1.5, -2.6, 0.8, 80)
]

with open(filepath, 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['hopping_radius', 'surface_tension', 'mcs_per_particle',
                     'energy', 'cluster_count', 'fractal_dimension'])
    for hr, st, fc, pk, tpk, sig, rise, e0, em, ef, tf, ts in conditions:
        count = cluster_count(t, fc, pk, tpk, sig, rise)
        en = energy(t, e0, em, ef, tf, ts)
        fd = fractal_dim(t)
        for i in range(len(t)):
            writer.writerow([hr, st, round(t[i], 6), round(en[i], 6), int(round(count[i])), round(fd[i], 6)])

print("relaxation_results.csv generated")
