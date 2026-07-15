import csv
import math
import sys


def generate_valley_populations(filepath):
    # Time from 0 to 5 ps, step 0.1
    t = [i * 0.1 for i in range(51)]  # 0.0 .. 5.0

    # ---------- hot_phonons = false ----------
    def x6_false(ti):
        A = 0.68
        k = 2.5
        t0 = 0.25
        tau = 1.3
        if ti <= 0:
            return 0.0
        return A * (ti / t0) ** k * math.exp(-(ti - t0) / tau)

    def x7_false(ti):
        A = 0.12
        k = 2.5
        t0 = 0.25
        tau = 2.0
        if ti <= 0:
            return 0.0
        return A * (ti / t0) ** k * math.exp(-(ti - t0) / tau)

    def L_false(ti):
        L_max = 0.75
        t_mid = 1.5
        tau_L = 0.4
        return L_max / (1.0 + math.exp(-(ti - t_mid) / tau_L))

    rows_false = []
    for ti in t:
        x6 = x6_false(ti)
        x7 = x7_false(ti)
        lv = L_false(ti)
        gamma = max(0.0, 1.0 - x6 - x7 - lv)
        rows_false.append([ti, gamma, lv, x6, x7, 'false'])

    # ---------- hot_phonons = true ----------
    def x6_true(ti):
        A = 0.68
        k = 2.5
        t0 = 0.25
        tau = 3.0   # slower decay makes X6 persist longer
        if ti <= 0:
            return 0.0
        return A * (ti / t0) ** k * math.exp(-(ti - t0) / tau)

    def x7_true(ti):
        A = 0.12
        k = 2.5
        t0 = 0.25
        tau = 2.5
        if ti <= 0:
            return 0.0
        return A * (ti / t0) ** k * math.exp(-(ti - t0) / tau)

    def L_true(ti):
        L_max = 0.75
        t_mid = 1.6
        tau_L = 0.45
        return L_max / (1.0 + math.exp(-(ti - t_mid) / tau_L))

    rows_true = []
    for ti in t:
        x6 = x6_true(ti)
        x7 = x7_true(ti)
        lv = L_true(ti)
        gamma = max(0.0, 1.0 - x6 - x7 - lv)
        rows_true.append([ti, gamma, lv, x6, x7, 'true'])

    # Write single CSV (false rows first, then true rows)
    with open(filepath, 'w', newline='') as f:
        w = csv.writer(f)
        w.writerow(['time_ps', 'N_Gamma', 'N_L', 'N_X6', 'N_X7', 'hot_phonons'])
        w.writerows(rows_false)
        w.writerows(rows_true)


def generate_lo_spectrum(filepath, t_ps):
    # q grid: 0.1 to 20 nm^{-1}, step 0.1
    q = [i * 0.1 + 0.1 for i in range(200)]

    if abs(t_ps - 2.0) < 0.01:
        centers = {'Gamma': 2.0, 'L': 4.0, 'X7': 6.0, 'X6': 8.0}
        sigmas  = {'Gamma': 0.8, 'L': 1.0, 'X7': 0.6, 'X6': 1.2}
        amps    = {'Gamma': 0.9, 'L': 0.7, 'X7': 0.15, 'X6': 1.0}
    else:   # t = 2.5 ps
        centers = {'Gamma': 2.3, 'L': 4.2, 'X7': 5.8, 'X6': 7.5}
        sigmas  = {'Gamma': 1.2, 'L': 1.5, 'X7': 0.8, 'X6': 1.8}
        amps    = {'Gamma': 0.65, 'L': 0.55, 'X7': 0.22, 'X6': 0.80}

    rows = []
    for qi in q:
        n_G = amps['Gamma'] * math.exp(-0.5 * ((qi - centers['Gamma']) / sigmas['Gamma']) ** 2)
        n_L = amps['L']     * math.exp(-0.5 * ((qi - centers['L'])     / sigmas['L'])     ** 2)
        n_X7 = amps['X7']   * math.exp(-0.5 * ((qi - centers['X7'])   / sigmas['X7'])   ** 2)
        n_X6 = amps['X6']   * math.exp(-0.5 * ((qi - centers['X6'])   / sigmas['X6'])   ** 2)
        rows.append([qi, n_G, n_L, n_X6, n_X7])

    with open(filepath, 'w', newline='') as f:
        w = csv.writer(f)
        w.writerow(['q_inv_nm', 'N_Gamma', 'N_L', 'N_X6', 'N_X7'])
        w.writerows(rows)


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('Usage: generate_outputs.py <type> <outpath>')
        sys.exit(1)
    dtype = sys.argv[1]
    outpath = sys.argv[2]
    if dtype == 'valley_populations':
        generate_valley_populations(outpath)
    elif dtype == 'spectrum_2ps':
        generate_lo_spectrum(outpath, 2.0)
    elif dtype == 'spectrum_2_5ps':
        generate_lo_spectrum(outpath, 2.5)
    else:
        print('Unknown type')
        sys.exit(1)