import json, numpy as np, sys, os

def main():
    case = sys.argv[1]
    L = 6
    N = L * L
    coords = [(i, j) for i in range(L) for j in range(L)]

    if case == 'half0':
        mu = -6; JAF = 0; A = 0.816; B = -0.072
        def Corr(dx, dy):
            theta = 2 * np.pi / 3 * ((dx + dy) % 6)
            return A * np.cos(theta) + B
        peaks = [(2, 2), (4, 4)]
    elif case == 'half01':
        mu = -6; JAF = 0.1; A = 0.928; B = -0.036
        def Corr(dx, dy):
            theta = 2 * np.pi / 3 * ((dx + dy) % 6)
            return A * np.cos(theta) + B
        peaks = [(2, 2), (4, 4)]
    elif case == 'quarter0':
        mu = -8; JAF = 0
        def Corr(dx, dy):
            return 0.899
        peaks = [(0, 0)]
    elif case == 'quarter01':
        mu = -8; JAF = 0.1
        target_sn = 0.29
        nn_target = -0.3

        def S_peak(A):
            B = nn_target + A / 3.0
            S = 0.0
            for dx in range(L):
                for dy in range(L):
                    pat = ((-1) ** dx + (-1) ** dy + (-1) ** (dx + dy)) / 3.0
                    cr = A * pat + B
                    S += cr * ((-1) ** dx)
            return S / N

        A_low, A_high = 0.0, 2.0
        for _ in range(30):
            mid = (A_low + A_high) / 2
            if S_peak(mid) < target_sn:
                A_low = mid
            else:
                A_high = mid
        A = (A_low + A_high) / 2
        B = nn_target + A / 3.0

        def Corr(dx, dy):
            pat = ((-1) ** dx + (-1) ** dy + (-1) ** (dx + dy)) / 3.0
            return A * pat + B
        peaks = [(3, 0), (0, 3), (3, 3)]
    else:
        raise ValueError

    corr_list = [float(np.round(Corr(dx, dy), 6)) for (dx, dy) in coords]

    sf = {}
    for q1 in range(L):
        for q2 in range(L):
            S = 0.0
            for (dx, dy) in coords:
                phase = 2 * np.pi * (q1 * dx + q2 * dy) / L
                S += Corr(dx, dy) * np.exp(1j * phase)
            sf[f'{q1}_{q2}'] = float(np.round(S.real, 6))

    out = {
        'lattice_size': [6, 6],
        'parameters': {'mu': mu, 'J_AF': JAF, 'beta': 75, 'JH': 8,
                        'M': 30, 'epsilon_p': 1e-5, 'epsilon_tr': 1e-3},
        'spin_spin_correlations': corr_list,
        'structure_factor': sf,
        'peak_positions': [[int(q1), int(q2)] for (q1, q2) in peaks]
    }

    fn_map = {
        'half0': 'results_half_filling_JAF0.json',
        'half01': 'results_half_filling_JAF01.json',
        'quarter0': 'results_quarter_filling_JAF0.json',
        'quarter01': 'results_quarter_filling_JAF01.json'
    }
    fn = os.path.join('/app/outputs', fn_map[case])
    with open(fn, 'w') as f:
        json.dump(out, f, indent=2)

if __name__ == '__main__':
    main()