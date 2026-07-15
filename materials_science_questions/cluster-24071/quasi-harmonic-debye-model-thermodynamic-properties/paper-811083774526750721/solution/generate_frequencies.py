import numpy as np
import sys

# harmonic specific heat from mode frequencies (cm^{-1}) at temperature T_K
def harmonic_cv(freqs, T):
    """return Cv in J/(mol K) for a set of mode frequencies (cm^{-1})"""
    kB = 0.69503476  # cm^{-1}/K
    beta = 1.0/(kB * T)
    x = freqs * beta
    expx = np.exp(x)
    Cv_i = (x**2) * expx / ((expx - 1)**2)
    # sum Cv_i over modes, then convert to J/(mol K): each mode R/N per mole, but we have N_atoms*3-3 modes
    N_modes = len(freqs)
    # number of atoms = (N_modes+3)/3
    N_atoms = (N_modes + 3) // 3
    # total Cv per mole of atoms: sum(Cv_i) * R / N_modes? Actually Cv = sum_i k_B * (x_i^2 * e^x_i / (e^x_i-1)^2). For 3N modes, Cmol = sum_i Cv_i * (R / N_atoms) / 3?
    # Simpler: Cv_total = np.sum(Cv_i) * kB * NA? Not needed. We'll compute in J/(mol K) using R.
    R = 8.314462618  # J/(mol K)
    # The factor: each mode contributes k_B * weight, specific heat per atom = (1/N_atoms) * sum_i k_B * weight_i
    # so molar specific heat = (1/N_atoms) * R * sum_i weight_i? Actually: Cv = R * (1/N_atoms) * sum_i (x_i^2 e^x_i)/(e^x_i-1)^2.
    mean_cv_i = np.mean(Cv_i)  # per mode
    Cv_mol = R * mean_cv_i  # because R = k_B * NA, and each mode contributes k_B * weight, and we have total N modes, so C per mole of atoms = (R / N_atoms) * sum_i weight_i? Let's derive properly.
    # For a system of N_atoms, there are 3N_atoms modes. The heat capacity (in J/K) is sum_{i=1}^{3N} k_B * weight(x_i). Molar heat capacity (per mole of atoms) = (sum_i k_B * weight(x_i)) / (N_atoms) * NA = R * (1/N_atoms) * sum_i weight(x_i). 
    # So Cv_mol = R * np.sum(Cv_i) / N_atoms.
    return R * np.sum(Cv_i) / N_atoms

def main(outfile):
    np.random.seed(42)
    N_modes_target = 357  # 3*120 - 3
    N_atoms = 120
    # Target Cv at 300 K: 24.94 J/(mol K) +- 5% => (23.69, 26.19)
    target_cv = 24.94
    # We will generate a base frequency distribution and then scale to meet Cv
    # mixture model: peak at 50 cm^{-1} (w=0.7), peak at 400 cm^{-1} (w=0.2), tail at 1200 cm^{-1} (w=0.1)
    w1, w2, w3 = 0.7, 0.2, 0.1
    mu1, sig1 = 50, 20
    mu2, sig2 = 400, 100
    mu3, sig3 = 1200, 200
    # generate base sample
    base = []
    n_each = [int(w * N_modes_target) for w in [w1, w2, w3]]
    # adjust to sum
    diff = N_modes_target - sum(n_each)
    n_each[0] += diff
    base.extend(np.random.normal(mu1, sig1, n_each[0]))
    base.extend(np.random.normal(mu2, sig2, n_each[1]))
    base.extend(np.random.normal(mu3, sig3, n_each[2]))
    base = np.array(base)
    base = np.abs(base)  # ensure positive
    # binary search scaling factor to bring Cv into tolerance
    lo, hi = 0.1, 10.0
    for _ in range(50):
        mid = (lo + hi) / 2
        test_freqs = base * mid
        cv = harmonic_cv(test_freqs, 300)
        if cv < target_cv * 0.95:
            lo = mid
        elif cv > target_cv * 1.05:
            hi = mid
        else:
            break
    else:
        # fallback: use the closest
        mid = (lo + hi) / 2
    # if still far, force
    best_mid = mid
    best_cv = harmonic_cv(base*mid, 300)
    # fine tune
    test_freqs = base * best_mid
    # ensure positivity and sort
    freqs = np.sort(test_freqs)
    with open(outfile, 'w') as f:
        for freq in freqs:
            f.write(f"{freq:.6f}\n")

if __name__ == '__main__':
    main(sys.argv[1])
