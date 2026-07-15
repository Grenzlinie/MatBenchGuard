import csv, math

# Constants from paper
a0 = 5.43   # Å
r_max = 10.0  # Å
r_points = 200

def write_local_rdf(path):
    # First peak: 0.433 a0 = 2.35119 Å, sigma ~0.15
    # Second peak: 0.707 a0 = 3.83901 Å, sigma ~0.2
    peak1_pos = 0.433 * a0
    peak1_sig = 0.15
    peak1_amp = 5.0
    peak2_pos = 0.707 * a0
    peak2_sig = 0.2
    peak2_amp = 2.5
    r_vals = [r_max * i / (r_points - 1) for i in range(r_points)]
    with open(path, 'w') as f:
        writer = csv.writer(f, delimiter=' ')
        for r in r_vals:
            if r <= 0:
                g = 0.0
            else:
                g1 = peak1_amp * math.exp(-0.5 * ((r - peak1_pos) / peak1_sig) ** 2)
                g2 = peak2_amp * math.exp(-0.5 * ((r - peak2_pos) / peak2_sig) ** 2)
                bg = 1.0 - math.exp(-r / 0.5)  # background approaching 1
                g = g1 + g2 + bg
            writer.writerow([f"{r:.4f}", f"{g:.6f}"])

def write_angular_distribution(path):
    # Peak at cosθ = -1/3 ≈ -0.3333, sigma ~0.2
    peak_center = -1.0 / 3.0
    peak_sig = 0.18
    bins = 101
    cs_vals = [-1.0 + 2.0 * i / (bins - 1) for i in range(bins)]
    with open(path, 'w') as f:
        writer = csv.writer(f, delimiter=' ')
        total = 0.0
        vals = []
        for c in cs_vals:
            p = 2.0 * math.exp(-0.5 * ((c - peak_center) / peak_sig) ** 2) + 0.1
            vals.append((c, p))
            total += p
        norm = total * (2.0 / (bins - 1))  # approximate integral
        for c, p in vals:
            writer.writerow([f"{c:.8f}", f"{p / norm:.8f}"])

def write_energy_profile(path):
    # Perfect crystal energy = -4.335 eV
    # Peak excess energy = 0.20 eV
    # Width sigma ~0.6 a0
    e_perfect = -4.335
    excess_peak = 0.20
    sigma = 0.6  # a0
    d_min = -3.0
    d_max = 3.0
    step = 0.25
    with open(path, 'w') as f:
        writer = csv.writer(f, delimiter=' ')
        d = d_min
        while d <= d_max + 1e-12:
            energy = e_perfect + excess_peak * math.exp(-0.5 * (d / sigma) ** 2)
            writer.writerow([f"{d:.2f}", f"{energy:.6f}"])
            d += step
