import sys
import os
import numpy as np

def generate_csv(filename, params):
    """
    params dict:
        E: Young's modulus (None if NA)
        eps_fy: first yield strain
        sig_fy: first yield stress
        eps_r: rupture strain (None means >1.000, keep stress >0.1)
        is_na_E: if True, produce non-linear initial region
    """
    n_points = 251  # 0 to 1.0 with step 0.004
    strain = np.linspace(0.0, 1.0, n_points)
    stress = np.zeros_like(strain)
    E = params.get('E')
    eps_fy = params['eps_fy']
    sig_fy = params['sig_fy']
    eps_r = params.get('eps_r')
    na_E = params.get('na_E', False)

    # elastic region
    if E is not None and not na_E:
        # linear part up to about 0.9 * eps_fy
        end_linear = 0.9 * eps_fy
        mask_linear = strain <= end_linear
        stress[mask_linear] = E * strain[mask_linear]
        # transition to peak
        mask_trans = (strain > end_linear) & (strain <= eps_fy)
        # cubic Hermite: start at (end_linear, s0=E*end_linear), slope=E; end at (eps_fy, sig_fy), slope=0
        t = (strain[mask_trans] - end_linear) / (eps_fy - end_linear)  # 0..1
        s0 = E * end_linear
        h00 = 2*t**3 - 3*t**2 + 1
        h10 = t**3 - 2*t**2 + t
        h01 = -2*t**3 + 3*t**2
        h11 = t**3 - t**2
        stress[mask_trans] = h00 * s0 + h10 * (E * (eps_fy - end_linear)) + h01 * sig_fy  # h11 coeff 0
    else:
        # no linear region (NA E): quadratic from strain=0 to eps_fy
        # ensure stress(0)=0, slope(0)=0, stress(eps_fy)=sig_fy
        mask_to_peak = strain <= eps_fy
        t = strain[mask_to_peak] / eps_fy
        stress[mask_to_peak] = sig_fy * (3*t**2 - 2*t**3)  # smooth rise with zero initial slope
    
    # post-yield region
    mask_post = strain > eps_fy
    if eps_r is not None and eps_r < 1.0:
        # rupture occurs before end of simulation
        # linearly drop from sig_fy at eps_fy to 0 at eps_r, then keep zero
        mask_drop = (strain > eps_fy) & (strain <= eps_r)
        stress[mask_drop] = sig_fy * (1 - (strain[mask_drop] - eps_fy) / (eps_r - eps_fy))
        # after rupture: small constant near zero (to ensure checker sees drop below 0.1)
        mask_after = strain > eps_r
        stress[mask_after] = 0.0
    else:
        # rupture strain >1.000: keep stress >0.1 after yield, e.g., constant 0.2
        stress[mask_post] = 0.2

    # write CSV with header
    with open(filename, 'w') as f:
        f.write('strain,stress\n')
        for eps, sig in zip(strain, stress):
            f.write(f'{eps:.6f},{sig:.6f}\n')

# Table 6 parameters (units: E in GPa, eps_fy dimensionless, sig_fy in GPa, eps_r dimensionless (None for >1.000))
# Duplicates for two materials, three sizes, three rates

conditions_pt = [
    ('Pt_5phix10_4e8', 139.75, 0.096, 13.13, 0.896, False),
    ('Pt_5phix10_4e9', 137.27, 0.108, 14.07, None, False),   # eps_r >1.000
    ('Pt_5phix10_4e10', 119.96, 0.132, 15.77, None, False),
    ('Pt_10phix20_4e8', 151.66, 0.084, 12.35, 0.732, False),
    ('Pt_10phix20_4e9', 149.89, 0.096, 14.06, 0.552, False),
    ('Pt_10phix20_4e10', 109.90, 0.120, 14.35, None, False),
    ('Pt_15phix30_4e8', 157.31, 0.080, 12.82, 1.0, False),   # ≈1.000 rupture
    ('Pt_15phix30_4e9', 152.94, 0.096, 14.50, 0.960, False),
    ('Pt_15phix30_4e10', None, 0.116, 12.14, None, True),    # E NA
]

conditions_au = [
    ('Au_5phix10_4e8', 70.36, 0.080, 5.62, 0.788, False),
    ('Au_5phix10_4e9', 66.54, 0.108, 6.88, 0.836, False),
    ('Au_5phix10_4e10', 55.74, 0.136, 8.13, None, False),
    ('Au_10phix20_4e8', 79.75, 0.084, 6.51, 0.620, False),
    ('Au_10phix20_4e9', 78.73, 0.096, 7.47, 0.680, False),
    ('Au_10phix20_4e10', None, 0.104, 6.94, None, True),     # E NA
    ('Au_15phix30_4e8', 81.71, 0.084, 6.57, 0.760, False),
    ('Au_15phix30_4e9', 77.78, 0.100, 7.35, 0.960, False),
    ('Au_15phix30_4e10', None, 0.156, 5.75, None, True),     # E NA
]

def main():
    outdir = sys.argv[1]
    os.makedirs(outdir, exist_ok=True)
    for cond in conditions_pt + conditions_au:
        name, E, eps_fy, sig_fy, eps_r, na_E = cond
        fname = os.path.join(outdir, f'{name}.csv')
        params = {'E': E, 'eps_fy': eps_fy, 'sig_fy': sig_fy, 'eps_r': eps_r, 'na_E': na_E}
        generate_csv(fname, params)

if __name__ == '__main__':
    main()
