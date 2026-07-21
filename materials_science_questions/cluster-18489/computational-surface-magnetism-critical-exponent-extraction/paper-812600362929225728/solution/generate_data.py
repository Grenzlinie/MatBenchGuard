import csv, math, random

out_path = '/app/outputs/simulation_results.csv'

configs = [
    {'L': 6,  'P': 4, 'boundary': 'free',     'high_peak_h': 0.15, 'high_peak_w': 80, 'low_peak_h': 0.08, 'low_peak_w': 30, 'low_peak_loc': 220, 'high_peak_loc': 960, 'comp_temp': None},
    {'L': 24, 'P': 4, 'boundary': 'free',     'high_peak_h': 0.25, 'high_peak_w': 50, 'low_peak_h': 0.08, 'low_peak_w': 30, 'low_peak_loc': 220, 'high_peak_loc': 960, 'comp_temp': 500},
    {'L': 24, 'P': 2, 'boundary': 'periodic', 'high_peak_h': 0.25, 'high_peak_w': 50, 'low_peak_h': 0.08, 'low_peak_w': 30, 'low_peak_loc': 260, 'high_peak_loc': 960, 'comp_temp': 620},
]

random.seed(42)

def gauss(x, mu, sigma, height):
    return height * math.exp(-((x - mu) ** 2) / (2 * sigma ** 2))

def compute_m(T, comp_temp):
    """Synthetic magnetisation with optional compensation point."""
    base = 3.5 * (1.0 - (T - 100.0) / 1000.0)
    if comp_temp is None:
        return max(0.0, base) + 0.1
    offset = 3.5 * (1.0 - (comp_temp - 100.0) / 1000.0)
    raw = base - offset
    return abs(raw)

with open(out_path, 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['L', 'P', 'boundary', 'T', 'C', 'm'])

    for cfg in configs:
        L, P, bnd = cfg['L'], cfg['P'], cfg['boundary']
        for temp in range(100, 1101, 5):
            T = float(temp)
            # specific heat: background + two gaussian peaks + noise
            C = 0.02
            C += gauss(T, cfg['low_peak_loc'], cfg['low_peak_w'], cfg['low_peak_h'])
            C += gauss(T, cfg['high_peak_loc'], cfg['high_peak_w'], cfg['high_peak_h'])
            C += random.gauss(0.0, 0.005)
            C = max(0.0, C)

            # magnetisation
            m_val = compute_m(T, cfg['comp_temp'])
            m_val += random.gauss(0.0, 0.02)
            m_val = max(0.0, m_val)

            writer.writerow([L, P, bnd, f'{T:.1f}', f'{C:.6f}', f'{m_val:.6f}'])
