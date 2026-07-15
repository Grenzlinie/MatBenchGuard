import math

# Physical constants (SI)
kB = 1.380649e-23        # J/K
e_charge = 1.602176634e-19  # C
hbar = 1.054571817e-34   # J s
m_e = 9.10938356e-31     # kg

# Material parameters
m_star = 0.0565 * m_e          # kg
Eg_eV = 0.2131
Delta_eV = 0.77
F = 1.0e6                     # V/m

# Derived coefficient alpha in eV·Å²
alpha_SI = hbar**2 / (2 * m_star)   # J·m²
alpha = alpha_SI * (1.0 / e_charge) * (1e10)**2   # eV·Å²

# Rashba coefficient (derived from the paper's splitting 12 meV at k=1 Å)
lambda_R = 0.006   # eV·Å


def compute_fermi_energy_and_k(n_per_spin_cm2):
    """
    n_per_spin_cm2 : carrier density for ONE spin branch (cm^-2)
    Returns: ef_up (eV), ef_down (eV), kf_up (Å^-1), kf_down (Å^-1)
    Uses Eq. 22 and Eq. 23 from the paper.
    """
    n = n_per_spin_cm2 * 1e-16   # convert to Å^-2
    A = 16 * math.pi**2 * alpha**3
    term_sq = lambda_R**2 / A
    term_lin = n / (math.pi * alpha)
    sqrt_arg = term_sq + term_lin
    sqrt_term = math.sqrt(sqrt_arg)
    second_part = lambda_R / (4 * math.pi * alpha**1.5)
    inner_up = 2 * math.pi * alpha * (sqrt_term + second_part)
    inner_down = 2 * math.pi * alpha * (sqrt_term - second_part)
    ef_up = inner_up**2
    ef_down = inner_down**2
    # Fermi wave vectors (Eq. 23)
    kf_up = (math.sqrt(lambda_R**2 + 4*alpha*ef_up) - lambda_R) / (2*alpha)
    kf_down = (math.sqrt(lambda_R**2 + 4*alpha*ef_down) + lambda_R) / (2*alpha)
    return ef_up, ef_down, kf_up, kf_down


def compute_thermopower(ef_eV, B, tau, s, T):
    """
    ef_eV : Fermi energy in eV
    B     : magnetic field in T
    tau   : relaxation time in s
    s     : scattering exponent
    T     : temperature in K
    Returns: Qxx, Qyx in uV/K
    """
    ef_J = ef_eV * e_charge
    prefactor = (math.pi**2 * kB**2 * T) / (3 * e_charge)  # V/K
    wc = e_charge * B / m_star   # cyclotron frequency (rad/s)
    wc2t2 = (wc * tau)**2
    Qxx = - (prefactor / ef_J) * (1.0 + s / (1.0 + wc2t2))
    Qyx = - (prefactor / ef_J) * (s * wc * tau / (1.0 + wc2t2))
    return Qxx * 1e6, Qyx * 1e6


def compute_power_factor(ef_eV, kf_A, tau, s, T):
    """
    ef_eV : Fermi energy in eV
    kf_A  : Fermi wave vector in Å^-1
    tau   : relaxation time in s
    s     : scattering exponent
    T     : temperature in K
    Returns: PF in uW/(cm·K²)
    Uses Eq. 13 of the paper.
    """
    ef_J = ef_eV * e_charge
    kf = kf_A * 1e10   # convert to m^-1
    PF_SI = (math.pi**3 * kB**4 * T**2) / (18 * m_star)  * \
            (1.0 + s)**2 / (ef_J**2) * (kf**2) * tau
    # Convert from W/(m·K²) to uW/(cm·K²): 1 W/(m·K²) = 1e4 uW/(cm·K²)
    return PF_SI * 1e4