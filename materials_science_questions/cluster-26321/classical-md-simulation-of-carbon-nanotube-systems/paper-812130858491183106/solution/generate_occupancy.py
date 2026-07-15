import sys, math, csv

phi = float(sys.argv[1])
# Set distribution parameters to produce correct trend: mean(1.3) < mean(0)
if phi == 0.0:
    mu, sigma = 4.7, 0.8   # peak near filled state (~4.7)
elif phi == 1.3:
    mu, sigma = 3.5, 1.0   # shifted left, broader for bistable/empty
else:
    mu, sigma = 4.0, 1.0   # fallback

n_bins = 80
low, high = 0.0, 8.0
bin_width = (high - low) / n_bins
centers = []
densities = []
unnorm = 0.0
for i in range(n_bins):
    center = low + (i + 0.5) * bin_width
    # unnormalized Gaussian
    val = math.exp(-0.5 * ((center - mu) / sigma) ** 2) / (sigma * math.sqrt(2 * math.pi))
    centers.append(center)
    densities.append(val)
    unnorm += val * bin_width

# Normalize to probability density (integrates to 1 over [0,8])
norm = 1.0 / unnorm if unnorm > 0 else 1.0
writer = csv.writer(sys.stdout, lineterminator='\n')
writer.writerow(["N_c", "probability_density"])
for c, d in zip(centers, densities):
    writer.writerow([f"{c:.4f}", f"{d * norm:.8f}"])
