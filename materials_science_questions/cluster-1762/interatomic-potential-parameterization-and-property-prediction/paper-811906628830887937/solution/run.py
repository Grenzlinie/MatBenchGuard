import numpy as np
import math
import csv

# Experimental data for Cu, Ag, Au (Foiles et al., PRB 33, 7983 (1986))
# a0 in Angstrom, Es (sublimation energy) in eV, Ev (unrelaxed vacancy-formation energy) in eV,
# B in GPa, C12, C44 in GPa.
metals = {
    "Cu": {"a0": 3.615, "Es": 3.54, "Ev": 1.30, "B": 137.0, "C12": 124.0, "C44": 76.0},
    "Ag": {"a0": 4.09, "Es": 2.85, "Ev": 1.10, "B": 104.0, "C12": 93.0, "C44": 46.0},
    "Au": {"a0": 4.08, "Es": 3.93, "Ev": 0.90, "B": 173.0, "C12": 157.0, "C44": 42.0}
}

# conversion factor: 1 GPa = 0.0062415 eV/Ang^3
GPa_to_eVA3 = 0.0062415

def generate_fcc_shells(nmax):
    """Generate w(n) for integer shell indices n=1..nmax for fcc lattice."""
    w = np.zeros(nmax+1, dtype=int)
    max_idx = int(np.sqrt(2*nmax)) + 2
    for n1 in range(-max_idx, max_idx+1):
        for n2 in range(-max_idx, max_idx+1):
            for n3 in range(-max_idx, max_idx+1):
                S = (n1+n2)**2 + (n1+n3)**2 + (n2+n3)**2
                if S % 2 == 0:
                    n = S // 2
                    if 1 <= n <= nmax:
                        w[n] += 1
    return w

def compute_mobius(w, nmax):
    """Compute Möbius inverse coefficients m(n) for n=1..nmax."""
    m = np.zeros(nmax+1)
    m[1] = 1.0 / w[1]
    for n in range(2, nmax+1):
        total = 0.0
        for d in range(1, n):
            if n % d == 0:
                k = n // d
                if k <= nmax:
                    total += m[d] * w[k]
        m[n] = -total / w[1]
    return m

def S_rho(R1, n_e, alpha, R1e):
    return n_e * np.exp(-alpha * (R1/R1e - 1.0))

def E_cohesive(R1, Es, beta, R1e):
    x = R1/R1e - 1.0
    return -Es * (1.0 + beta * x) * np.exp(-beta * x)

def E_TB(R1, Es, Ev, alpha, R1e):
    return -2.0 * (Es - Ev) * np.exp(-0.5 * alpha * (R1/R1e - 1.0))

output_path = "/app/outputs/inverted_functions.csv"
with open(output_path, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["metal", "distance_R1", "hopping_integral", "pair_potential"])
    for metal, props in metals.items():
        a0 = props["a0"]
        Es = props["Es"]
        Ev = props["Ev"]
        B_GPa = props["B"]
        C12_GPa = props["C12"]
        C44_GPa = props["C44"]
        B_eV = B_GPa * GPa_to_eVA3
        C12_eV = C12_GPa * GPa_to_eVA3
        C44_eV = C44_GPa * GPa_to_eVA3
        Omega_e = a0**3 / 4.0
        R1e = a0 / math.sqrt(2.0)
        diff_elastic = C12_eV - C44_eV
        diff_energy = Es - Ev
        alpha = math.sqrt(18.0 * Omega_e * diff_elastic / diff_energy)
        n_e = 4.0 * diff_energy**2
        beta = math.sqrt(9.0 * B_eV * Omega_e / Es)
        r_values = np.linspace(0.9 * R1e, 1.2 * R1e, 100)
        nmax = 100
        w = generate_fcc_shells(nmax)
        m = compute_mobius(w, nmax)
        for r in r_values:
            rho_val = 0.0
            phi_val = 0.0
            for n in range(1, nmax+1):
                if m[n] == 0.0:
                    continue
                rn = r * math.sqrt(n)
                S_rho_val = S_rho(rn, n_e, alpha, R1e)
                E_val = E_cohesive(rn, Es, beta, R1e)
                ETB_val = E_TB(rn, Es, Ev, alpha, R1e)
                sumPhi_val = 2.0 * (E_val - ETB_val)
                rho_val += m[n] * S_rho_val
                phi_val += m[n] * sumPhi_val
            if rho_val > 0:
                h_val = math.sqrt(rho_val)
            else:
                h_val = 0.0
            writer.writerow([metal, f"{r:.6f}", f"{h_val:.8f}", f"{phi_val:.8f}"])
