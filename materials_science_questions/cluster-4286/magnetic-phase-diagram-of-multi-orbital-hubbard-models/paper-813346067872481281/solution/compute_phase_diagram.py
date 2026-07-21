#!/usr/bin/env python3
import sys
import numpy as np

def main(output_path):
    # Settings
    t = 1.0                     # n.n. hopping (energy unit)
    nk = 200                    # k-mesh size per dimension
    delta = 1e-10               # small threshold for denominator
    # tA/tB ratio range
    ratios = np.arange(0.5, 4.05, 0.25)   # 0.50, 0.75, ..., 4.00 = 15 points

    # k-grid over [0,2pi)^2
    kx = 2*np.pi * np.arange(nk) / nk
    ky = kx.copy()
    KX, KY = np.meshgrid(kx, ky)   # shape (nk, nk)
    # Precompute cosines for efficiency
    cos_kx = np.cos(KX)
    cos_ky = np.cos(KY)
    cos_kp = np.cos(KX + KY)        # kx+ky
    cos_km = np.cos(KX - KY)        # kx-ky

    def compute_uc(ratio):
        # hopping parameters from Eq. (4) with t=1
        t1 = 0.5 * ratio
        t2 = 0.5 / ratio
        
        # dispersions
        eps_xz = -2.0 * (cos_kx + cos_ky) - 2*t1 * cos_kp - 2*t2 * cos_km
        eps_yz = -2.0 * (cos_kx + cos_ky) - 2*t1 * cos_km - 2*t2 * cos_kp
        
        # chemical potential for half-filling (2 electrons per site)
        # each orbital holds 2 (spin) electrons, so half-filling means n_xz=n_yz=1
        target_filling = 1.0   # per orbital
        # find mu
        lo = -10.0
        hi = 10.0
        for it in range(60):
            mid = (lo + hi) * 0.5
            occ_xz = np.mean(eps_xz < mid)
            occ_yz = np.mean(eps_yz < mid)
            total = occ_xz + occ_yz
            if total > 2.0:
                hi = mid
            else:
                lo = mid
        mu = (lo + hi) * 0.5
        # recalc occupation for safety
        f_xz = (eps_xz < mu).astype(float)
        f_yz = (eps_yz < mu).astype(float)
        # Build shifted k points for Q=(pi,pi)
        # (kx+pi, ky+pi)
        cos_kx_sh_pi = np.cos(KX + np.pi)
        cos_ky_sh_pi = np.cos(KY + np.pi)
        cos_kp_sh_pi = np.cos(KX + KY + 2*np.pi)   # same as cos(KX+KY)
        cos_km_sh_pi = np.cos(KX - KY)             # unchanged
        eps_xz_pipi = -2.0*(cos_kx_sh_pi + cos_ky_sh_pi) - 2*t1*cos_kp_sh_pi - 2*t2*cos_km_sh_pi
        eps_yz_pipi = -2.0*(cos_kx_sh_pi + cos_ky_sh_pi) - 2*t1*cos_km_sh_pi - 2*t2*cos_kp_sh_pi

        # Q=(pi,0)
        cos_kx_sh_pi0 = np.cos(KX + np.pi)
        cos_ky_sh_pi0 = np.cos(KY)                  # unchanged
        cos_kp_sh_pi0 = np.cos(KX + KY + np.pi)     # shift by pi
        cos_km_sh_pi0 = np.cos(KX - KY + np.pi)     # shift by pi
        eps_xz_pi0 = -2.0*(cos_kx_sh_pi0 + cos_ky_sh_pi0) - 2*t1*cos_kp_sh_pi0 - 2*t2*cos_km_sh_pi0
        eps_yz_pi0 = -2.0*(cos_kx_sh_pi0 + cos_ky_sh_pi0) - 2*t1*cos_km_sh_pi0 - 2*t2*cos_kp_sh_pi0

        def chi0(f_eps, f_epsQ, eps, epsQ):
            num = f_eps - f_epsQ
            den = epsQ - eps
            valid = np.abs(den) > delta
            chi = np.zeros_like(num)
            chi[valid] = num[valid] / den[valid]
            # where den==0, contribution is zero (by symmetry)
            return np.mean(chi)

        chi_pipi = chi0(f_xz, f_xz, eps_xz, eps_xz_pipi) + chi0(f_yz, f_yz, eps_yz, eps_yz_pipi)
        chi_pi0  = chi0(f_xz, f_xz, eps_xz, eps_xz_pi0)  + chi0(f_yz, f_yz, eps_yz, eps_yz_pi0)
        Uc_pipi = 1.0 / (2.0 * max(chi_pipi, 1e-12)) if chi_pipi > 0 else np.inf
        Uc_pi0  = 1.0 / (2.0 * max(chi_pi0, 1e-12))  if chi_pi0 > 0 else np.inf
        return Uc_pipi, Uc_pi0

    results = []
    for x in ratios:
        upi, u0 = compute_uc(x)
        results.append((x, upi, u0))
    
    # Write CSV
    with open(output_path, 'w') as f:
        f.write('tA_over_tB,Uc_pipi,Uc_pi0\n')
        for row in results:
            f.write(f'{row[0]:.4f},{row[1]:.6e},{row[2]:.6e}\n')

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: compute_phase_diagram.py <output_csv>')
        sys.exit(1)
    main(sys.argv[1])
