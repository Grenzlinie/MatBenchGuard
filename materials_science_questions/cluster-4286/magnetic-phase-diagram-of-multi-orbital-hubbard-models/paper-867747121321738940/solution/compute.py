import numpy as np
import sys
import csv

def compute_hall():
    t = 1.0
    tp = -0.35
    pstar = 0.19
    alpha = 0.63 / (pstar - 0.08)  # ≈5.7273
    Nk = 100
    kx = np.linspace(-np.pi, np.pi, Nk, endpoint=False)
    ky = np.linspace(-np.pi, np.pi, Nk, endpoint=False)
    kxx, kyy = np.meshgrid(kx, ky, indexing='ij')
    dk = 2*np.pi / Nk

    cos_kx = np.cos(kxx)
    cos_ky = np.cos(kyy)

    def compute_xi(mu):
        return -2*t*(cos_kx + cos_ky) - 4*tp*cos_kx*cos_ky - mu

    def shift_k(kxx, kyy, eta):
        Qx = np.pi - 2*np.pi*eta
        Qy = np.pi
        kx_shift = (kxx + Qx) % (2*np.pi) - np.pi
        ky_shift = (kyy + Qy) % (2*np.pi) - np.pi
        return np.cos(kx_shift), np.cos(ky_shift)

    def compute_n_H_for_p(p_tgt):
        A = alpha * max(pstar - p_tgt, 0.0)
        eta = p_tgt if p_tgt < pstar else 0.0

        # bisection to find mu
        mu_low, mu_high = -10.0, 10.0
        def get_p(mu):
            xi = compute_xi(mu)
            cos_kxs, cos_kys = shift_k(kxx, kyy, eta)
            xi_shift = -2*t*(cos_kxs + cos_kys) - 4*tp*cos_kxs*cos_kys - mu
            disc = np.sqrt((xi - xi_shift)**2 + 4*A**2)
            E1 = (xi + xi_shift)/2 - disc/2
            E2 = (xi + xi_shift)/2 + disc/2
            n_elec = np.sum((E1 < 0) | (E2 < 0)) / (Nk*Nk)
            return 1.0 - n_elec

        for _ in range(40):
            mu_mid = (mu_low + mu_high)/2
            p_mid = get_p(mu_mid)
            if p_mid < p_tgt:
                mu_high = mu_mid
            else:
                mu_low = mu_mid
            if mu_high - mu_low < 1e-6:
                break
        mu = (mu_low + mu_high)/2

        # final bands
        xi = compute_xi(mu)
        cos_kxs, cos_kys = shift_k(kxx, kyy, eta)
        xi_shift = -2*t*(cos_kxs + cos_kys) - 4*tp*cos_kxs*cos_kys - mu
        disc = np.sqrt((xi - xi_shift)**2 + 4*A**2)
        E1 = (xi + xi_shift)/2 - disc/2
        E2 = (xi + xi_shift)/2 + disc/2

        occ1 = E1 < 0
        occ2 = E2 < 0

        def hessian(E):
            Ep = np.pad(E, pad_width=1, mode='wrap')
            d2Edkx2 = (Ep[2:, 1:-1] - 2*Ep[1:-1, 1:-1] + Ep[:-2, 1:-1]) / dk**2
            d2Edky2 = (Ep[1:-1, 2:] - 2*Ep[1:-1, 1:-1] + Ep[1:-1, :-2]) / dk**2
            d2Edkxky = (Ep[2:, 2:] - Ep[2:, :-2] - Ep[:-2, 2:] + Ep[:-2, :-2]) / (4*dk**2)
            return d2Edkx2, d2Edky2, d2Edkxky

        d2E1kx2, d2E1ky2, d2E1kxky = hessian(E1)
        d2E2kx2, d2E2ky2, d2E2kxky = hessian(E2)

        S_xx = np.mean(occ1 * d2E1kx2 + occ2 * d2E2kx2)
        S_yy = np.mean(occ1 * d2E1ky2 + occ2 * d2E2ky2)
        S_H_integrand = occ1 * (d2E1kx2 * d2E1ky2 - d2E1kxky**2) + occ2 * (d2E2kx2 * d2E2ky2 - d2E2kxky**2)
        S_H = np.mean(S_H_integrand)

        n_H = - S_xx * S_yy / S_H
        return n_H

    p_vals = np.arange(0.02, 0.251, 0.01)
    results = []
    for p in p_vals:
        nh = compute_n_H_for_p(p)
        results.append((round(p, 2), nh))
        print(f"p={p:.2f} n_H={nh:.6f}")

    outfile = sys.argv[sys.argv.index('--out')+1] if '--out' in sys.argv else '/app/outputs/hall_number_vs_doping.csv'
    with open(outfile, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['p', 'n_H'])
        for p, nh in results:
            writer.writerow([f"{p:.2f}", f"{nh:.6f}"])

if __name__ == "__main__":
    if '--task' in sys.argv:
        task_idx = sys.argv.index('--task')
        task = sys.argv[task_idx+1]
        if task == 'hall':
            compute_hall()
        else:
            print("Unknown task", task)