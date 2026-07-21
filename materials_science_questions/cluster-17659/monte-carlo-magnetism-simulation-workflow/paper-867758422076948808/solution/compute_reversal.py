import sys
import csv
import math

# Boltzmann constant in meV/K
k_B = 8.617333262145e-2
# attempt frequency in Hz
nu0 = 1e9


def fe_rates_simple(T):
    """Simple-kMC rates (Eqs. 2-3) for Fe (antiferromagnetic, J negative)."""
    J_val = -1.3  # meV
    K_val = 3.0   # meV
    # Formation at edge: initial neighbour field h_i = -J (since s1.s2 = -1, J negative)
    h1 = -J_val
    # Disappearance: edge spin in wall state neighbours same -> h_i = J
    h2 = J_val
    # Motion: domain wall centre -> neighbours opposite -> h_i = 0
    h3 = 0.0

    def barrier(h):
        return (2 * K_val + h) ** 2 / (4 * K_val)

    E1 = barrier(h1)
    E2 = barrier(h2)
    E3 = barrier(h3)

    nu1 = nu0 * math.exp(-E1 / (k_B * T))
    nu2 = nu0 * math.exp(-E2 / (k_B * T))
    nu3 = nu0 * math.exp(-E3 / (k_B * T))
    return nu1, nu2, nu3


def fe_rates_improved(T):
    """Improved-kMC I rates (Arrhenius with paper-reported barriers)."""
    E1, E2, E3 = 4.32, 2.76, 1.72  # meV
    nu1 = nu0 * math.exp(-E1 / (k_B * T))
    nu2 = nu0 * math.exp(-E2 / (k_B * T))
    nu3 = nu0 * math.exp(-E3 / (k_B * T))
    return nu1, nu2, nu3


def co_rates_simple(T):
    """Simple-kMC rates (Eqs. 2-3) for Co (ferromagnetic, J positive)."""
    J = 7.5   # meV
    K = 2.0   # meV
    # Formation: edge spin neighbour same -> h_i = J, |h| > 2K -> Eq. (3)
    exp_f1 = math.exp(-2 * J / (k_B * T))
    nu1 = nu0 * exp_f1 / (1 + exp_f1)
    # Disappearance: edge spin neighbour opposite -> h_i = -J, Eq. (3)
    exp_f2 = math.exp(2 * J / (k_B * T))
    nu2 = nu0 * exp_f2 / (1 + exp_f2)
    # Motion: domain wall centre -> h_i = 0, barrier = K
    nu3 = nu0 * math.exp(-K / (k_B * T))
    return nu1, nu2, nu3


def co_rates_improved(T):
    """Improved-kMC II rates (Arrhenius with paper-reported barriers)."""
    E1, E2, E3 = 10.7, 0.0034, 0.0065  # meV
    nu1 = nu0 * math.exp(-E1 / (k_B * T))
    nu2 = nu0 * math.exp(-E2 / (k_B * T))
    nu3 = nu0 * math.exp(-E3 / (k_B * T))
    return nu1, nu2, nu3


def reversal_time(nu1, nu2, nu3, N, n):
    """Single domain-wall approximation, Eq. (5)."""
    a = nu3 / (nu2 + nu3)
    term1 = (a / nu3) * ((N - 1) / 2.0) * (N - 2 * (1 - 2 * a) / (1 - a))
    term2 = (1 / nu1) * (N * (1 - a) - 2 * (1 - 2 * a))
    tau = (1 / (n * a)) * (term1 + term2)
    return tau


def generate_fe_csv(outpath):
    rows = []
    # Section 1: N=10, T in [4.0, 5.0, 6.0, 7.0] K
    N = 10
    for T in [4.0, 5.0, 6.0, 7.0]:
        nu1_s, nu2_s, nu3_s = fe_rates_simple(T)
        tau_s = reversal_time(nu1_s, nu2_s, nu3_s, N, n=2)
        rows.append({'temperature_K': T, 'chain_length_N': N, 'model': 'simple_kMC', 'reversal_time_s': tau_s})

        nu1_i, nu2_i, nu3_i = fe_rates_improved(T)
        tau_i = reversal_time(nu1_i, nu2_i, nu3_i, N, n=2)
        rows.append({'temperature_K': T, 'chain_length_N': N, 'model': 'improved_kMC', 'reversal_time_s': tau_i})
        rows.append({'temperature_K': T, 'chain_length_N': N, 'model': 'analytical', 'reversal_time_s': tau_i})

    # Section 2: T=4.0 K, N in [5, 10, 15, 20]
    T = 4.0
    for N in [5, 10, 15, 20]:
        nu1_s, nu2_s, nu3_s = fe_rates_simple(T)
        tau_s = reversal_time(nu1_s, nu2_s, nu3_s, N, n=2)
        rows.append({'temperature_K': T, 'chain_length_N': N, 'model': 'simple_kMC', 'reversal_time_s': tau_s})

        nu1_i, nu2_i, nu3_i = fe_rates_improved(T)
        tau_i = reversal_time(nu1_i, nu2_i, nu3_i, N, n=2)
        rows.append({'temperature_K': T, 'chain_length_N': N, 'model': 'improved_kMC', 'reversal_time_s': tau_i})
        rows.append({'temperature_K': T, 'chain_length_N': N, 'model': 'analytical', 'reversal_time_s': tau_i})

    with open(outpath, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=['temperature_K', 'chain_length_N', 'model', 'reversal_time_s'])
        writer.writeheader()
        writer.writerows(rows)


def generate_co_csv(outpath):
    rows = []
    # Section 1: N=40, T in [10.0, 15.0, 20.0, 30.0] K
    N = 40
    for T in [10.0, 15.0, 20.0, 30.0]:
        # simple model: use actual chain length N (point-like wall)
        nu1_s, nu2_s, nu3_s = co_rates_simple(T)
        tau_s = reversal_time(nu1_s, nu2_s, nu3_s, N, n=4)
        rows.append({'temperature_K': T, 'chain_length_N': N, 'model': 'simple_kMC', 'reversal_time_s': tau_s})

        # improved/analytical: use effective length N_eff = N - 10
        N_eff = N - 10
        nu1_i, nu2_i, nu3_i = co_rates_improved(T)
        tau_i = reversal_time(nu1_i, nu2_i, nu3_i, N_eff, n=4)
        rows.append({'temperature_K': T, 'chain_length_N': N, 'model': 'improved_kMC', 'reversal_time_s': tau_i})
        rows.append({'temperature_K': T, 'chain_length_N': N, 'model': 'analytical', 'reversal_time_s': tau_i})

    # Section 2: T=10.0 K, N in [20, 25, 30, 40]
    T = 10.0
    for N in [20, 25, 30, 40]:
        # simple
        nu1_s, nu2_s, nu3_s = co_rates_simple(T)
        tau_s = reversal_time(nu1_s, nu2_s, nu3_s, N, n=4)
        rows.append({'temperature_K': T, 'chain_length_N': N, 'model': 'simple_kMC', 'reversal_time_s': tau_s})

        N_eff = N - 10
        nu1_i, nu2_i, nu3_i = co_rates_improved(T)
        tau_i = reversal_time(nu1_i, nu2_i, nu3_i, N_eff, n=4)
        rows.append({'temperature_K': T, 'chain_length_N': N, 'model': 'improved_kMC', 'reversal_time_s': tau_i})
        rows.append({'temperature_K': T, 'chain_length_N': N, 'model': 'analytical', 'reversal_time_s': tau_i})

    with open(outpath, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=['temperature_K', 'chain_length_N', 'model', 'reversal_time_s'])
        writer.writeheader()
        writer.writerows(rows)


if __name__ == '__main__':
    if len(sys.argv) != 3:
        sys.exit('Usage: compute_reversal.py {fe|co} output.csv')
    material, outpath = sys.argv[1], sys.argv[2]
    if material == 'fe':
        generate_fe_csv(outpath)
    elif material == 'co':
        generate_co_csv(outpath)
    else:
        sys.exit(f'Unknown material: {material}')
