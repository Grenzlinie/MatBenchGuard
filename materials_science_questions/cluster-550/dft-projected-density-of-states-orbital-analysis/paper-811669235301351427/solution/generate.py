import numpy as np
import csv
import sys
import os


def main():
    if len(sys.argv) != 3 or sys.argv[1] != '--output':
        raise SystemExit('Usage: generate.py --output <mode>')
    mode = sys.argv[2]
    output_dir = '/app/outputs'
    os.makedirs(output_dir, exist_ok=True)

    # paper parameters
    l = 11
    Emax = 0.857  # eV
    factor = Emax / (l * l)  # E_k = factor * (nx^2+ny^2+nz^2)
    EN = 0.23
    Delta_EN = -0.0133
    EN_prime = EN + Delta_EN  # 0.2167 eV
    x = 0.002
    beta = 2.0
    VNM = beta * np.sqrt(x)  # 0.0894427 eV
    sigma_proj = 0.003  # 3 meV
    sigma_host = 0.020  # 20 meV

    if mode == 'eigenstate_properties':
        # Build discrete host k-points up to |n| <= l
        rows = []
        for nx in range(-l, l+1):
            for ny in range(-l, l+1):
                for nz in range(-l, l+1):
                    sq = nx*nx + ny*ny + nz*nz
                    if sq > l*l:
                        continue
                    E_k = sq * factor
                    # BAC eigenenergies
                    half_sum = (E_k + EN_prime) / 2.0
                    half_diff = np.sqrt(((E_k - EN_prime) ** 2) / 4.0 + VNM ** 2)
                    Ep = half_sum + half_diff
                    Em = half_sum - half_diff
                    # fractional Gamma character
                    amp_plus = (Ep - EN_prime) ** 2 / ((Ep - EN_prime) ** 2 + VNM ** 2)
                    amp_minus = (Em - EN_prime) ** 2 / ((Em - EN_prime) ** 2 + VNM ** 2)
                    # localisation factor heuristic (L ~ 1 + C*(1-f)/(f+eps))
                    C_loc = 15.0
                    eps_loc = 0.01
                    L_plus = 1.0 + C_loc * (1.0 - amp_plus) / (amp_plus + eps_loc)
                    L_minus = 1.0 + C_loc * (1.0 - amp_minus) / (amp_minus + eps_loc)
                    rows.append((Em, amp_minus, L_minus))
                    rows.append((Ep, amp_plus, L_plus))
        rows.sort(key=lambda r: r[0])
        with open(os.path.join(output_dir, 'eigenstate_properties.csv'), 'w', newline='') as f:
            w = csv.writer(f)
            w.writerow(['eigenstate_index', 'energy', 'fractional_Gamma', 'localisation_factor'])
            for idx, (energy, fg, loc) in enumerate(rows):
                w.writerow([idx, f'{energy:.6f}', f'{fg:.6f}', f'{loc:.6f}'])

    elif mode == 'projected_dos_selected_k':
        EM_vals = [0.0, 0.1, 0.2, 0.23, 0.25, 0.3]
        E_grid = np.linspace(0.0, 0.5, 501)  # 0 to 0.5 eV step 1 meV
        pref = 1.0 / (np.sqrt(2 * np.pi) * sigma_proj)
        with open(os.path.join(output_dir, 'projected_dos_selected_k.csv'), 'w', newline='') as f:
            w = csv.writer(f)
            w.writerow(['k_state_label', 'energy', 'projected_DOS'])
            for EM in EM_vals:
                half_sum = (EM + EN_prime) / 2.0
                half_diff = np.sqrt(((EM - EN_prime) ** 2) / 4.0 + VNM ** 2)
                Ep = half_sum + half_diff
                Em = half_sum - half_diff
                amp_plus = (Ep - EN_prime) ** 2 / ((Ep - EN_prime) ** 2 + VNM ** 2)
                amp_minus = (Em - EN_prime) ** 2 / ((Em - EN_prime) ** 2 + VNM ** 2)
                for E in E_grid:
                    g_plus = pref * np.exp(-((E - Ep) ** 2) / (2 * sigma_proj ** 2))
                    g_minus = pref * np.exp(-((E - Em) ** 2) / (2 * sigma_proj ** 2))
                    dos = amp_plus * g_plus + amp_minus * g_minus
                    w.writerow([f'EM_{EM}', f'{E:.6f}', f'{dos:.6f}'])

    elif mode == 'host_projected_dos':
        # dense EM sampling weighted by sqrt(E) (3D DOS)
        EM_samples = np.linspace(0.001, Emax, 2000)
        weights = np.sqrt(EM_samples)
        E_grid = np.linspace(0.0, 0.5, 501)
        dos_hist = np.zeros_like(E_grid)
        pref_device = 1.0 / (np.sqrt(2 * np.pi) * sigma_host)
        for EM, w in zip(EM_samples, weights):
            half_sum = (EM + EN_prime) / 2.0
            half_diff = np.sqrt(((EM - EN_prime) ** 2) / 4.0 + VNM ** 2)
            Ep = half_sum + half_diff
            Em = half_sum - half_diff
            amp_plus = (Ep - EN_prime) ** 2 / ((Ep - EN_prime) ** 2 + VNM ** 2)
            amp_minus = (Em - EN_prime) ** 2 / ((Em - EN_prime) ** 2 + VNM ** 2)
            peak_pref = w * pref_device
            dos_hist += amp_minus * peak_pref * np.exp(-((E_grid - Em) ** 2) / (2 * sigma_host ** 2))
            dos_hist += amp_plus * peak_pref * np.exp(-((E_grid - Ep) ** 2) / (2 * sigma_host ** 2))
        with open(os.path.join(output_dir, 'host_projected_dos.csv'), 'w', newline='') as f:
            w = csv.writer(f)
            w.writerow(['energy', 'host_projected_DOS'])
            for E, dos in zip(E_grid, dos_hist):
                w.writerow([f'{E:.6f}', f'{dos:.6f}'])

    else:
        raise ValueError(f'Unknown mode: {mode}')


if __name__ == '__main__':
    main()