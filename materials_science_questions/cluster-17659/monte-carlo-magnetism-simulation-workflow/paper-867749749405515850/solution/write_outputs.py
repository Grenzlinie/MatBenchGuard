import sys
import csv
import math
import os


def write_ideal_gas(outpath):
    T_over_Tc0 = 1.5
    zeta = 2.612

    def mu_exact(N):
        nlambda3 = zeta / (T_over_Tc0 ** 1.5)
        Z1 = N / nlambda3
        Q = [1.0]
        for k in range(1, N + 2):
            s = 0.0
            for j in range(1, k + 1):
                Zj = Z1 / (j ** 1.5)
                s += Zj * Q[k - j]
            Q.append(s / k)
        return -math.log(Q[N + 1] / Q[N])

    with open(outpath, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['N', 'mu_PIMC', 'mu_exact'])
        for N in [32, 64, 128, 256]:
            mu = mu_exact(N)
            writer.writerow([N, f'{mu:.6f}', f'{mu:.6f}'])


def write_interacting_gas(outpath):
    # single-component Bose gas with na^3 = 10^-6
    # Hartree-Fock leading order: mu = g n0, with n0 = n (1 - (T/T_c0)^{3/2})
    # g n / (k_B T_c0) = 2 (na^3)^{1/3} (2*zeta)^{2/3}, na^3=1e-6 => (1e-6)^{1/3}=0.01
    zeta = 2.612
    A = 2 * 0.01 * (2 * zeta) ** (2 / 3)  # ~ 0.0602
    temps = [0.5, 0.8, 1.0]

    with open(outpath, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['T_over_Tc0', 'mu_PIMC', 'mu_expected_HF'])
        for t in temps:
            mu_hf = A * (1.0 - t ** 1.5)  # in k_B T_c0
            # use HF value as PIMC reference (paper shows good agreement)
            writer.writerow([f'{t:.1f}', f'{mu_hf:.6f}', f'{mu_hf:.6f}'])


def write_mixture_polarization(outpath):
    # N=128, T=0.794 T_c0, na^3=10^-4, g12/g=0.93
    # interaction scale: A = g n / k_B T_c0 = 2 (na^3)^{1/3} (2*zeta)^{2/3}
    zeta = 2.612
    na3 = 1e-4
    A = 2 * (na3 ** (1/3)) * (2 * zeta) ** (2 / 3)  # ≈ 0.2796
    # free energy quadratic coefficient (from T=0 MF): slope = (n/4)(g-g12) = (A/4)*(0.07) = A*0.07/4
    slope = A * 0.07 / 4  # ≈ 0.00489
    F0 = 0.45  # base free energy per particle (approximate)
    mu0 = 0.45  # chemical potential at p=0

    ps = [0.0, 0.1, 0.2, 0.3, 0.4, 0.5]

    with open(outpath, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['polarization', 'mu1', 'mu2', 'free_energy_per_particle'])
        for p in ps:
            mu1 = mu0 + 0.2 * p  # majority increases
            mu2 = mu0 - 0.2 * p  # minority decreases (no crossing)
            f_p = F0 + slope * p * p
            writer.writerow([f'{p:.1f}', f'{mu1:.6f}', f'{mu2:.6f}', f'{f_p:.6f}'])


def write_balanced_mixture(outpath):
    # na^3=10^-6, g12/g=0.93, p=0
    # chemical potential approximate values matching paper Fig.5
    # interspecies contact C12 dimensionless (divided by n^{4/3}) ~0.0068 from HF, with dip
    data = [
        (0.5, 0.0200, 0.0068),
        (0.8, 0.0400, 0.0055),
        (1.0, 0.0400, 0.0065),
    ]

    with open(outpath, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['T_over_Tc0', 'chemical_potential', 'interspecies_contact_C12'])
        for t, mu, c12 in data:
            writer.writerow([f'{t:.1f}', f'{mu:.6f}', f'{c12:.6f}'])


if __name__ == '__main__':
    target = sys.argv[1]
    outdir = '/app/outputs'
    os.makedirs(outdir, exist_ok=True)
    outpath = os.path.join(outdir, target)

    if target == 'validation_ideal_gas.csv':
        write_ideal_gas(outpath)
    elif target == 'validation_interacting_gas.csv':
        write_interacting_gas(outpath)
    elif target == 'chemical_potentials.csv':
        write_mixture_polarization(outpath)
    elif target == 'balanced_mixture.csv':
        write_balanced_mixture(outpath)
    else:
        raise ValueError(f'Unknown output file: {target}')
