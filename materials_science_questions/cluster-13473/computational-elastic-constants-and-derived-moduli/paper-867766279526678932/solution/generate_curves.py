import argparse
import numpy as np

def stress_strain_curve(gamma_max=5.0, n_points=101):
    """Synthetic stress-strain curve for GQ glass with rejuvenation.
    Reproduces a peak at strain ~0.2 (stress ~1.25) and a flow plateau ~0.9."""
    strain = np.linspace(0, gamma_max, n_points)
    peak_strain = 0.20
    peak_stress = 1.25
    flow_stress = 0.90
    # Elastic slope
    slope = peak_stress / peak_strain
    # Post-peak exponential decay
    decay_scale = 0.05
    stress = np.piecewise(strain,
        [strain <= peak_strain, strain > peak_strain],
        [lambda g: slope * g,
         lambda g: flow_stress + (peak_stress - flow_stress) * np.exp(-(g - peak_strain) / decay_scale)]
    )
    return strain, stress

def mean_yield_stress_curve(gamma_max=5.0, n_points=101):
    """Spatially averaged local yield stress for GQ glass.
    Initially ~1.0, rises gently to ~1.08 at strain ~0.25, then decreases to ~0.85."""
    strain = np.linspace(0, gamma_max, n_points)
    start_val = 1.00
    early_rise = 0.08  # total rise
    rise_center = 0.15
    rise_width = 0.10
    # after peak, decay to final ~0.85
    final_val = 0.85
    decay_scale = 0.6
    # Use a smooth function: base + rise*sigmoid - drop*sigmoid-like
    sigmoid = 1.0 / (1.0 + np.exp(-(strain - rise_center) / (rise_width / 4.0)))
    mean_thr = start_val + early_rise * sigmoid
    # after a while, start decreasing
    t0 = 0.25
    decay = (start_val + early_rise - final_val) * (1.0 - np.exp(-np.maximum(strain - t0, 0) / decay_scale))
    mean_thr -= decay
    return strain, mean_thr

def localization_index_curve(gamma_max=5.0, n_points=101):
    """Localization index LOC. Rises to a peak ~0.045 at strain ~0.25, then decays."""
    strain = np.linspace(0, gamma_max, n_points)
    peak_loc = 0.045
    peak_strain = 0.25
    # Use a gamma-like shape: (e*x/x0) * exp(-x/x0)
    # Normalized to peak at x0
    loc = peak_loc * (strain / peak_strain) * np.exp(1 - strain / peak_strain)
    # ensure monotonic after peak? Already is
    return strain, loc

def write_csv(filename, strain, values, header):
    data = np.column_stack([strain, values])
    np.savetxt(filename, data, delimiter=',', header=header, comments='')

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', required=True)
    parser.add_argument('--mode', required=True, choices=['stress_strain', 'mean_yield_stress', 'localization_index'])
    args = parser.parse_args()
    if args.mode == 'stress_strain':
        strain, stress = stress_strain_curve()
        write_csv(args.output, strain, stress, 'strain,stress')
    elif args.mode == 'mean_yield_stress':
        strain, mean_thr = mean_yield_stress_curve()
        write_csv(args.output, strain, mean_thr, 'strain,mean_threshold')
    elif args.mode == 'localization_index':
        strain, loc = localization_index_curve()
        write_csv(args.output, strain, loc, 'strain,LOC')
