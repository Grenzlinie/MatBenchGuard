import numpy as np
import argparse
import json
import csv
import io
import sys

def generate_data(rng):
    # create deterministic data with controlled correlations
    n_events = 20
    sample_ids = [1 if i % 2 == 0 else 2 for i in range(n_events)]
    event_ids = list(range(1, n_events+1))
    
    # parameters for defect analysis
    target_corr_phi = 0.26
    target_R2 = 0.72
    slope = 0.2
    intercept = 0.0
    
    # generate phi_esh_loc and phi_fit with correlation target_corr_phi
    # start from standard normal latent variables
    latent = rng.normal(0, 1, n_events)
    noise1 = rng.normal(0, 1, n_events)
    noise2 = rng.normal(0, 1, n_events)
    # compute weights to achieve correlation
    # phi_esh = a*latent + b*noise1, phi_fit = c*latent + d*noise2
    # correlation = a*c / sqrt((a^2+b^2)*(c^2+d^2))
    # choose a=1, b=0.2
    a = 1.0
    b = 0.2
    var1 = a*a + b*b
    # solve for c,d such that correlation = target_corr_phi
    # set c = k, d = m
    # correlation = a*k / sqrt(var1*(k*k+m*m))
    # pick m=0.3, solve for k
    m = 0.3
    # corr = a*k / sqrt(var1*(k*k+m*m))
    # square: corr^2 * var1 * (k*k+m*m) = a^2 * k^2
    # (corr^2 * var1 - a^2) * k^2 + corr^2 * var1 * m^2 = 0
    # k^2 = - corr^2 * var1 * m^2 / (corr^2 * var1 - a^2)
    # with corr=0.26, a=1, var1=1.04, m=0.3
    corr = target_corr_phi
    denom = corr*corr * var1 - a*a
    num = -corr*corr * var1 * m*m
    k_sq = num / denom
    k = np.sqrt(max(0, k_sq))
    phi_esh_loc = a*latent + b*noise1
    phi_fit = k*latent + m*noise2
    # shift and scale to meaningful angles (centered around pi/4)
    phi_esh_loc = np.pi/4 + phi_esh_loc * 0.2
    phi_fit = np.pi/4 + phi_fit * 0.2
    # ensure within [0, pi/2]
    phi_esh_loc = np.clip(phi_esh_loc, 0, np.pi/2)
    phi_fit = np.clip(phi_fit, 0, np.pi/2)
    
    # generate u_na_avg and epsilon_star_fit with R^2 = target_R2
    u_na_avg = rng.uniform(0.1, 0.6, n_events)
    epsilon_true = slope * u_na_avg + intercept
    # to achieve R^2 = 1 - Var(noise)/Var(epsilon_star)
    # we can control noise variance
    # compute Var(epsilon_true)
    var_true = np.var(epsilon_true)
    # desired Var(noise) = (1 - R^2) * var_true
    var_noise = (1 - target_R2) * var_true
    noise_eps = rng.normal(0, np.sqrt(var_noise), n_events)
    epsilon_star_fit = epsilon_true + noise_eps
    # ensure positive
    epsilon_star_fit = np.maximum(epsilon_star_fit, 1e-5)
    
    defects = []
    for i in range(n_events):
        d = {
            'event_id': event_ids[i],
            'sample_id': sample_ids[i],
            'defect_x': rng.uniform(0, 98.8),
            'defect_y': rng.uniform(0, 98.8),
            'phi_esh_loc': round(float(phi_esh_loc[i]), 6),
            'u_na_avg': round(float(u_na_avg[i]), 6),
            'epsilon_star_fit': round(float(epsilon_star_fit[i]), 6),
            'phi_fit': round(float(phi_fit[i]), 6)
        }
        defects.append(d)
    
    # stress drops
    target_corr_global = 0.97
    target_corr_local = 0.92
    # base stress drops from lognormal
    sigma_md = rng.lognormal(mean=np.log(0.01), sigma=0.2, size=n_events)
    # add noise to achieve correlations
    # for simplicity, generate as: sigma_global = sigma_md + noise_g, sigma_local = sigma_md + noise_l
    # with variances chosen to give desired correlations
    # correlation = 1 / sqrt(1 + var_noise/var_sigma)
    # so var_noise = (1/corr^2 - 1) * var_sigma
    var_sigma = np.var(sigma_md)
    var_noise_g = (1/target_corr_global**2 - 1) * var_sigma if target_corr_global > 0 else 0
    var_noise_l = (1/target_corr_local**2 - 1) * var_sigma if target_corr_local > 0 else 0
    noise_g = rng.normal(0, np.sqrt(var_noise_g), n_events)
    noise_l = rng.normal(0, np.sqrt(var_noise_l), n_events)
    sigma_global = sigma_md + noise_g
    sigma_local = sigma_md + noise_l
    sigma_global = np.maximum(sigma_global, 1e-10)
    sigma_local = np.maximum(sigma_local, 1e-10)
    
    stress = []
    for i in range(n_events):
        s = {
            'event_id': event_ids[i],
            'sample_id': sample_ids[i],
            'Delta_sigma_MD': round(float(sigma_md[i]), 6),
            'Delta_sigma_global_fit': round(float(sigma_global[i]), 6),
            'Delta_sigma_local_descriptor': round(float(sigma_local[i]), 6)
        }
        stress.append(s)
    return defects, stress

def compute_metrics(defects, stress):
    # extract arrays
    phi_fit = np.array([d['phi_fit'] for d in defects])
    phi_loc = np.array([d['phi_esh_loc'] for d in defects])
    u_na = np.array([d['u_na_avg'] for d in defects])
    eps = np.array([d['epsilon_star_fit'] for d in defects])
    # correlation phi
    corr_phi = np.corrcoef(phi_fit, phi_loc)[0,1]
    # linear fit eps vs u_na
    coeffs = np.polyfit(u_na, eps, 1)
    slope = coeffs[0]
    intercept = coeffs[1]
    pred = np.polyval(coeffs, u_na)
    ss_res = np.sum((eps - pred)**2)
    ss_tot = np.sum((eps - np.mean(eps))**2)
    r2 = 1 - ss_res/ss_tot if ss_tot > 0 else 0.0
    # stress correlations
    sig_md = np.array([s['Delta_sigma_MD'] for s in stress])
    sig_glob = np.array([s['Delta_sigma_global_fit'] for s in stress])
    sig_loc = np.array([s['Delta_sigma_local_descriptor'] for s in stress])
    rho_global = np.corrcoef(sig_md, sig_glob)[0,1]
    rho_local = np.corrcoef(sig_md, sig_loc)[0,1]
    return {
        'rho_phi': round(float(corr_phi), 6),
        'slope_u_vs_eps': round(float(slope), 6),
        'intercept_u_vs_eps': round(float(intercept), 6),
        'R2_u_vs_eps': round(float(r2), 6),
        'rho_stress_global': round(float(rho_global), 6),
        'rho_stress_local': round(float(rho_local), 6)
    }

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--basename', required=True, help='output file basename')
    args = parser.parse_args()
    rng = np.random.default_rng(42)
    defects, stress = generate_data(rng)
    if args.basename == 'defect_analysis.csv':
        output = io.StringIO()
        writer = csv.writer(output)
        writer.writerow(['event_id', 'sample_id', 'defect_x', 'defect_y', 'phi_esh_loc', 'u_na_avg', 'epsilon_star_fit', 'phi_fit'])
        for d in defects:
            writer.writerow([d['event_id'], d['sample_id'], d['defect_x'], d['defect_y'], d['phi_esh_loc'], d['u_na_avg'], d['epsilon_star_fit'], d['phi_fit']])
        sys.stdout.write(output.getvalue())
    elif args.basename == 'stress_drop_predictions.csv':
        output = io.StringIO()
        writer = csv.writer(output)
        writer.writerow(['event_id', 'sample_id', 'Delta_sigma_MD', 'Delta_sigma_global_fit', 'Delta_sigma_local_descriptor'])
        for s in stress:
            writer.writerow([s['event_id'], s['sample_id'], s['Delta_sigma_MD'], s['Delta_sigma_global_fit'], s['Delta_sigma_local_descriptor']])
        sys.stdout.write(output.getvalue())
    elif args.basename == 'summary_metrics.json':
        metrics = compute_metrics(defects, stress)
        sys.stdout.write(json.dumps(metrics, indent=2))
    else:
        raise ValueError(f'Unknown basename: {args.basename}')

if __name__ == '__main__':
    main()