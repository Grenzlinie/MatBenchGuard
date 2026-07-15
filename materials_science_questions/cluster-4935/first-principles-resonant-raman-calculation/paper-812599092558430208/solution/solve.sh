#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
python3 -m pip install -q --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple numpy scipy

# === solve block: bound_state_result.json ===
cat > /solution/compute.py << 'ENDOFSCRIPT'
import argparse, json, csv, os
import numpy as np
from scipy.integrate import quad
from scipy.interpolate import interp1d

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('output_file')
    args = parser.parse_args()

    # parameters
    omega_o = 1.0
    r = 0.15
    Delta = 0.15
    omega_v = 0.925
    omega_c = 1.075
    omega_10 = Delta / 10   # 0.015 (used only for bound state)
    gamma20 = gamma21 = Delta / 100  # 0.0015

    def z_pbg(w):
        if omega_v <= w <= omega_c:
            return 0.0
        denom = np.sqrt(max((w - omega_v)*(w - omega_c), 1e-30))
        return abs(w - omega_o) / denom

    def z_fdm(w, kappa=0.001):
        if omega_v <= w <= omega_c:
            return 0.0
        num = w**2 - 2*omega_v*w + omega_v*omega_c
        denom = (w - omega_v)**2 + kappa**2
        return num / denom

    L_trunc = 20.0

    def compute_sigma(eps, model='PBG', om10=None):
        z = z_pbg if model == 'PBG' else z_fdm
        omega10_use = om10 if om10 is not None else omega_10

        def term_integral(gamma_val, shift):
            eps_prime = eps - shift
            sing = eps_prime
            def integrand(w):
                return gamma_val * z(w) / (w - sing)

            def integrate_regular(a, b):
                pts = []
                if a <= omega_v <= b:
                    pts.append(omega_v)
                if a <= omega_c <= b:
                    pts.append(omega_c)
                return quad(integrand, a, b, limit=500, epsabs=1e-12, points=pts)[0]

            def integrate_PV(a, b):
                delta = 1e-8
                left = quad(integrand, a, sing - delta, limit=500, epsabs=1e-12,
                            points=[omega_v,omega_c] if a<=omega_v<=b else [])[0]
                right = quad(integrand, sing + delta, b, limit=500, epsabs=1e-12,
                             points=[omega_v,omega_c] if a<=omega_v<=b else [])[0]
                return left + right

            total = 0.0
            for seg_start, seg_end in [(-L_trunc, omega_v), (omega_c, L_trunc)]:
                if seg_start >= seg_end:
                    continue
                if seg_start <= sing <= seg_end:
                    total += integrate_PV(seg_start, seg_end)
                else:
                    total += integrate_regular(seg_start, seg_end)
            return total

        sigma_prime = term_integral(gamma20, 0.0) + term_integral(gamma21, omega10_use)
        sigma_prime /= (2.0 * np.pi)

        sig_dp = 0.5 * (gamma20 * z(eps) + gamma21 * z(eps - omega10_use))
        return sigma_prime, sig_dp

    # --- bound state ---
    if 'bound_state_result' in args.output_file:
        omega20_bs = 0.95 * omega_c   # 1.02125
        G_prime = (omega_v + omega_10, omega_c)  # (0.94, 1.075)

        eps_grid = np.linspace(G_prime[0] + 1e-6, G_prime[1] - 1e-6, 300)

        # PBG (using the bound-state omega10)
        sigma_pbg = []
        for eps in eps_grid:
            sp, _ = compute_sigma(eps, 'PBG', om10=omega_10)
            sigma_pbg.append(sp)
        sigma_pbg = np.array(sigma_pbg)
        f_pbg = omega20_bs - eps_grid - sigma_pbg
        sign_ch = np.where(np.diff(np.sign(f_pbg)))[0]
        if len(sign_ch) == 0:
            pbg_exists = False
            pbg_ev = None
        else:
            a, b = eps_grid[sign_ch[0]], eps_grid[sign_ch[0]+1]
            for _ in range(60):
                m = 0.5*(a+b)
                sp_m, _ = compute_sigma(m, 'PBG', om10=omega_10)
                fm = omega20_bs - m - sp_m
                if fm == 0:
                    a = b = m
                    break
                if np.sign(fm) == np.sign(omega20_bs - a - compute_sigma(a, 'PBG', om10=omega_10)[0]):
                    a = m
                else:
                    b = m
            pbg_ev = float((a+b)/2)
            pbg_exists = True

        # FDM (using the bound-state omega10)
        sigma_fdm = []
        for eps in eps_grid:
            sp, _ = compute_sigma(eps, 'FDM', om10=omega_10)
            sigma_fdm.append(sp)
        sigma_fdm = np.array(sigma_fdm)
        f_fdm = omega20_bs - eps_grid - sigma_fdm
        sign_ch_f = np.where(np.diff(np.sign(f_fdm)))[0]
        if len(sign_ch_f) == 0:
            fdm_exists = False
            fdm_ev = None
        else:
            a, b = eps_grid[sign_ch_f[0]], eps_grid[sign_ch_f[0]+1]
            for _ in range(60):
                m = 0.5*(a+b)
                sp_m, _ = compute_sigma(m, 'FDM', om10=omega_10)
                fm = omega20_bs - m - sp_m
                if fm == 0:
                    a = b = m
                    break
                if np.sign(fm) == np.sign(omega20_bs - a - compute_sigma(a, 'FDM', om10=omega_10)[0]):
                    a = m
                else:
                    b = m
            fdm_ev = float((a+b)/2)
            fdm_exists = True

        res = {
            "pbg_bound_state_exists": pbg_exists,
            "pbg_eigenvalue": pbg_ev,
            "fdm_bound_state_exists": fdm_exists,
            "fdm_eigenvalue": fdm_ev
        }
        with open(args.output_file, 'w') as f:
            json.dump(res, f, indent=2)
        return

    # --- spectra ---
    if 'pbg' in args.output_file.lower():
        model = 'PBG'
        z_model = z_pbg
    else:
        model = 'FDM'
        z_model = z_fdm

    omega20_spec = 1.2 * omega_c   # 1.29
    omega21_list = [1.15*omega_c, 1.05*omega_c, omega_c, omega_o]  # [1.23625, 1.12875, 1.075, 1.0]

    omega_grid = np.linspace(omega20_spec - 0.5, omega20_spec + 0.5, 1500)
    eps_eval = np.linspace(omega_grid[0] - 0.1, omega_grid[-1] + 0.1, 400)

    with open(args.output_file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['omega_minus_omega20', 'omega21', 'sigma_R'])
        for omega21 in omega21_list:
            omega10_cur = omega20_spec - omega21   # varies per ω21
            # recompute self-energy grid for this ω10
            sp_arr = np.zeros_like(eps_eval)
            sdp_arr = np.zeros_like(eps_eval)
            for i, eps in enumerate(eps_eval):
                sp, sdp = compute_sigma(eps, model, om10=omega10_cur)
                sp_arr[i] = sp
                sdp_arr[i] = sdp
            interp_sp = interp1d(eps_eval, sp_arr, kind='linear', fill_value='extrapolate')
            interp_sdp = interp1d(eps_eval, sdp_arr, kind='linear', fill_value='extrapolate')

            for w in omega_grid:
                sp = interp_sp(w)
                sdp = interp_sdp(w)
                zv = z_model(w)
                num = gamma20**2 * zv**2
                den = (omega20_spec - w - sp)**2 + sdp**2
                sigma = num / den if den > 1e-30 else 0.0
                writer.writerow([w - omega20_spec, omega21, sigma])

if __name__ == '__main__':
    main()
ENDOFSCRIPT
python3 /solution/compute.py "$OUTDIR/bound_state_result.json"
python3 /solution/compute.py "$OUTDIR/rayleigh_spectrum_pbg.csv"
python3 /solution/compute.py "$OUTDIR/rayleigh_spectrum_fdm.csv"

# === solve block: rayleigh_spectrum_pbg.csv ===
python3 /solution/compute.py rayleigh_spectrum_pbg.csv

# === solve block: rayleigh_spectrum_fdm.csv ===
python3 /solution/compute.py rayleigh_spectrum_fdm.csv
