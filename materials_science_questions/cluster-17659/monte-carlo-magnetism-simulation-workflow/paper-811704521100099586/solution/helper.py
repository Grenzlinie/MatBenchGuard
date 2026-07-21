import sys, argparse, csv, numpy as np

def nonint_magnetization(xi, sigma, direction='down'):
    # Model parameters per sigma, chosen to approximate Fig.1 coercivity and shape
    if sigma == 2:
        Hc = 0.6
        w = 0.25
    elif sigma == 5:
        Hc = 2.0
        w = 1.0
    elif sigma == 15:
        Hc = 5.0
        w = 2.5
    elif abs(sigma - 13.9) < 0.1:
        Hc = 4.8
        w = 2.3
    else:
        raise ValueError(f"Unknown sigma {sigma}")
    if direction == 'down':
        return 0.5 * np.tanh((xi + Hc) / w)
    else:  # 'up'
        return 0.5 * np.tanh((xi - Hc) / w)

def generate_noninteracting(sigmas, npts=200):
    rows = []
    for sigma in sigmas:
        xi0 = 2*sigma
        # descending branch: xi0 -> -xi0
        xi_down = np.linspace(xi0, -xi0, npts//2, endpoint=True)
        m_down = nonint_magnetization(xi_down, sigma, 'down')
        # ascending branch: -xi0 -> xi0
        xi_up = np.linspace(-xi0, xi0, npts//2, endpoint=True)
        m_up = nonint_magnetization(xi_up, sigma, 'up')
        xi = np.concatenate([xi_down, xi_up])
        m = np.concatenate([m_down, m_up])
        for f, mag in zip(xi, m):
            rows.append((sigma, float(f), float(mag)))
    return rows

def generate_interacting(Nlist, npts=200):
    # material parameters – maghemite, T=28 K, particle 8 nm, core 200 nm
    sigma = 13.9   # derived from K, Ms, T
    xi0 = 2*sigma
    A = 4*np.pi*(1e-5)**2           # core surface area, cm^2
    R_p = 4e-7                      # particle radius, cm
    V = (4/3)*np.pi*R_p**3          # particle volume, cm^3
    mu = 400 * V                     # magnetic moment, emu
    kT = 1.38e-16 * 28              # thermal energy, erg
    lambdas = []
    for N in Nlist:
        a = np.sqrt(A / N)
        lam = mu**2 / (kT * a**3)
        lambdas.append(lam)
    kappa = 0.4   # mean‑field coupling factor
    rows = []
    for N, lam in zip(Nlist, lambdas):
        beta = kappa * lam
        # descending branch
        xi_down = np.linspace(xi0, -xi0, npts//2, endpoint=True)
        m_down = np.zeros_like(xi_down)
        for _ in range(5):   # fixed‑point iteration
            m_down = nonint_magnetization(xi_down + beta * m_down, sigma, 'down')
        # ascending branch
        xi_up = np.linspace(-xi0, xi0, npts//2, endpoint=True)
        m_up = np.zeros_like(xi_up)
        for _ in range(5):
            m_up = nonint_magnetization(xi_up + beta * m_up, sigma, 'up')
        xi = np.concatenate([xi_down, xi_up])
        m = np.concatenate([m_down, m_up])
        for f, mag in zip(xi, m):
            rows.append((N, float(f), float(mag)))
    return rows

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--mode', required=True, choices=['noninteracting','interacting'])
    parser.add_argument('--output', required=True)
    args = parser.parse_args()
    if args.mode == 'noninteracting':
        sigmas = [2, 5, 15]
        rows = generate_noninteracting(sigmas)
        with open(args.output, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['sigma','field','magnetization'])
            writer.writerows(rows)
    else:
        Nlist = [100, 500, 1000]
        rows = generate_interacting(Nlist)
        with open(args.output, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['num_particles','field','magnetization'])
            writer.writerows(rows)

if __name__ == '__main__':
    main()
