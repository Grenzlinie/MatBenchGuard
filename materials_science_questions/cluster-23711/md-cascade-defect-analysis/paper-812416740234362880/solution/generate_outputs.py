import csv, math, sys

def generate_cluster_distributions(path):
    sizes = list(range(2, 102))
    # params: (T, species) -> (peak, sigma_left, sigma_right)
    params = {
        (600, 'vacancy'): (44, 5, 2),
        (600, 'interstitial'): (10, 3, 15),
        (650, 'vacancy'): (44, 5, 8),
        (650, 'interstitial'): (10, 5, 5),
        (660, 'vacancy'): (44, 5, 15),
        (660, 'interstitial'): (10, 2, 2),
    }
    scale = 1e-5
    temps = [600, 650, 660]
    doses = [1, 5]
    species_list = ['vacancy', 'interstitial']
    with open(path, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Temperature', 'Dose', 'Species', 'ClusterSize', 'Concentration'])
        for T in temps:
            for Dose in doses:
                for Species in species_list:
                    peak, sigL, sigR = params[(T, Species)]
                    for size in sizes:
                        sigma = sigL if size < peak else sigR
                        conc = scale * math.exp(-((size - peak) ** 2) / (2 * sigma ** 2))
                        writer.writerow([T, Dose, Species, size, conc])

def generate_diffusion_coefficients(path):
    with open(path, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Temperature', 'Dose', 'D_total', 'D_vacancy', 'D_interstitial'])
        # 500 K: interstitial dominates
        D_v_500 = 1e-23
        D_i_500 = 8e-23
        writer.writerow([500, 5, D_v_500 + D_i_500, D_v_500, D_i_500])
        # 660 K: vacancy dominates
        D_v_660 = 1e-21
        D_i_660 = 3e-22
        writer.writerow([660, 5, D_v_660 + D_i_660, D_v_660, D_i_660])

if __name__ == '__main__':
    if len(sys.argv) != 3:
        sys.exit(1)
    filepath, mode = sys.argv[1], sys.argv[2]
    if mode == 'cluster_distributions':
        generate_cluster_distributions(filepath)
    elif mode == 'diffusion_coefficients':
        generate_diffusion_coefficients(filepath)
    else:
        sys.exit(1)
