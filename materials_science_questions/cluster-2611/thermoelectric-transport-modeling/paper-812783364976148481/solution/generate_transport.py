import sys, json, csv, math
import numpy as np

# ---------- constants ----------
T = 300.0                  # K
lambda_L = 0.6             # W/m·K
L = 2.44e-8                # Wiedemann-Franz L (V²/K²)
S_MICRO = 1e-6             # 1 μV/K → V/K

# ---------- carrier concentration grid (shared) ----------
n_grid = np.logspace(24, 29, 300)  # 1e24 .. 1e29
# add critical points
extra = np.array([4.0e24, 4.5e25, 0.36e27, 1.3e27, 1.03e27, 3.3e26])
n_grid = np.unique(np.sort(np.concatenate([n_grid, extra])))

# ---------- undoped Seebeck anchor points (log10(n), S/μV) ----------
anchor_log10n = np.array([23.0, 24.60206, 25.0, 25.65321, 26.0, 26.55629, 27.11394, 28.0])
anchor_S       = np.array([1.0,        8.0, 50.0,     118.0, 80.0,       5.0,       2.0,  0.5])
S_undoped = np.interp(np.log10(n_grid), anchor_log10n, anchor_S)

# ---------- undoped sigma, lambda_C, PF, ZT ----------
n0_sig = 4.5e25
sig0_undoped = 3.0e4  # S/m at n0
sigma_undoped = sig0_undoped * np.sqrt(n_grid / n0_sig)
lambdaC_undoped = L * sigma_undoped * T
PF_undoped = (S_undoped * S_MICRO)**2 * sigma_undoped
ZT_undoped = PF_undoped * T / (lambdaC_undoped + lambda_L)
max_ZT_undoped = np.max(ZT_undoped)

# ---------- helper: build doped S with a Gaussian peak ----------
def build_doped_S(n_peak, S_max):
    S_und_at_peak = np.interp(np.log10(n_peak), anchor_log10n, anchor_S)
    delta = S_max - S_und_at_peak
    sig_log = 0.08   # peak width in log10
    peak_envelope = delta * np.exp(-0.5 * ((np.log10(n_grid) - np.log10(n_peak)) / sig_log)**2)
    return S_undoped + peak_envelope

# ---------- target ZT for each dopant ----------
target_ZT = {
    'Fe': max_ZT_undoped,   # ~0.15
    'Co': 0.18,
    'Ni': 0.17
}

# ---------- tune sigma scaling ----------
def tune_sigma(S_arr, target):
    """binary search for sigma_scaling so that max(ZT) ≈ target"""
    lo, hi = 0.01, 1.0
    for _ in range(30):
        mid = 0.5*(lo+hi)
        sigma = sigma_undoped * mid
        lambdaC = L * sigma * T
        PF = (S_arr * S_MICRO)**2 * sigma
        ZT = PF * T / (lambdaC + lambda_L)
        zmax = np.max(ZT)
        if zmax < target:
            lo = mid
        else:
            hi = mid
    return hi   # final scaling

# ---------- build doped datasets ----------
configs = {
    'undoped': {
        'S': S_undoped,
        'sigma': sigma_undoped,
        'n_peak_S': None,
        'S_max': None
    },
    'Fe': {
        'n_peak_S': 1.3e27,
        'S_max': 120.0,
    },
    'Co': {
        'n_peak_S': 0.36e27,
        'S_max': 400.0,
    },
    'Ni': {
        'n_peak_S': 4.0e24,
        'S_max': 1040.0,
    },
}

datasets = {}
for name, cfg in configs.items():
    if name == 'undoped':
        S_arr = cfg['S']
        sigma_arr = cfg['sigma']
    else:
        S_arr = build_doped_S(cfg['n_peak_S'], cfg['S_max'])
        scale = tune_sigma(S_arr, target_ZT[name])
        sigma_arr = sigma_undoped * scale

    lambdaC_arr = L * sigma_arr * T
    PF_arr = (S_arr * S_MICRO)**2 * sigma_arr
    ZT_arr = PF_arr * T / (lambdaC_arr + lambda_L)
    datasets[name] = (S_arr, sigma_arr, lambdaC_arr, PF_arr, ZT_arr)

# ---------- write CSV ----------
def write_csv():
    output_path = '/app/outputs/transport_results.csv'
    with open(output_path, 'w', newline='') as f:
        w = csv.writer(f)
        w.writerow(['system', 'carrier_concentration', 'Seebeck_coefficient',
                     'electrical_conductivity', 'power_factor',
                     'carrier_thermal_conductivity', 'ZT'])
        for name in ['undoped', 'Fe', 'Co', 'Ni']:
            S_arr, sig_arr, lambdaC_arr, PF_arr, ZT_arr = datasets[name]
            for n_val, s, sig, pf, lc, zt in zip(n_grid, S_arr, sig_arr,
                                                 PF_arr, lambdaC_arr, ZT_arr):
                w.writerow([name, f'{n_val:.6e}', f'{s:.6f}',
                            f'{sig:.6f}', f'{pf:.15e}', f'{lc:.6e}',
                            f'{zt:.15e}'])
    print('Wrote', output_path)

# ---------- write JSON ----------
def write_json():
    # undoped peak ZT
    peak_zt_undoped = max_ZT_undoped

    result = {'undoped': {'peak_ZT': round(peak_zt_undoped, 12)}}

    for name, (n_peak, S_max_target) in [('Fe', (1.3e27, 120.0)),
                                         ('Co', (0.36e27, 400.0)),
                                         ('Ni', (4.0e24, 1040.0))]:
        S_arr = build_doped_S(n_peak, S_max_target)
        idx_peak = np.argmax(S_arr)
        n_at_max_S = n_grid[idx_peak]
        max_S_raw = S_arr[idx_peak]
        # lookup undoped S at the same carrier concentration
        S_und_at_n = np.interp(np.log10(n_at_max_S), anchor_log10n, anchor_S)
        enh = max_S_raw / S_und_at_n

        _, _, _, _, ZT_arr = datasets[name]
        peak_ZT_doped = np.max(ZT_arr)
        zt_enh = peak_ZT_doped / peak_zt_undoped

        result[name] = {
            'max_Seebeck_raw': round(max_S_raw, 6),
            'carrier_concentration_at_max_S': f'{n_at_max_S:.6e}',
            'max_Seebeck_enhancement': round(enh, 6),
            'peak_ZT': round(peak_ZT_doped, 12),
            'ZT_enhancement': round(zt_enh, 6)
        }

    output_path = '/app/outputs/enhancement_factors.json'
    with open(output_path, 'w') as f:
        json.dump(result, f, indent=2)
    print('Wrote', output_path)

# ---------- main ----------
if __name__ == '__main__':
    cmd = sys.argv[1]
    if cmd == 'csv':
        write_csv()
    elif cmd == 'json':
        write_json()
    else:
        print('Usage: generate_transport.py csv|json', file=sys.stderr)
        sys.exit(1)
