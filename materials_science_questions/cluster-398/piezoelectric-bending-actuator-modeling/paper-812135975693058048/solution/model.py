import numpy as np

def compute_G(v_D_val, L=2e-6, v_s=6000, K2=0.16, eps_r=8.5, rho_res=1.5, Z_R=1.5e5, rho_mass=5680):
    """Compute electromechanical conversion efficiency G for one drift velocity."""
    # Half-wavelength resonance angular frequency
    omega = 2.0 * np.pi * v_s / (2.0 * L)   # f0 = v_s/(2L)

    # Material and transport parameters
    eps0 = 8.854187817e-12
    sigma = 1.0 / rho_res                     # conductivity (Omega.m)^{-1}
    omega_c = sigma / (eps0 * eps_r)          # conductivity frequency
    A = 1j * omega_c / omega                  # dimensionless conductivity term

    # Perturbation: if v_D is exactly zero, use a tiny value to keep a cubic
    v_D_eff = v_D_val if v_D_val != 0.0 else 1e-6

    # Solve cubic dispersion a*x^3 + b*x^2 + c*x + d = 0   where x = k/omega
    a = v_D_eff * (1.0 + K2)
    b = -(1.0 + A + K2)
    c = -v_D_eff / (v_s * v_s)
    d = (1.0 + A) / (v_s * v_s)
    coeffs = [a, b, c, d]
    x_vals = np.roots(coeffs)                # three complex wave numbers
    k = omega * x_vals                       # k_j

    # Mechanical impedance of the film (ZnO)
    Z_F = rho_mass * v_s

    # Build 3x3 linear system and right-hand side
    M = np.zeros((3, 3), dtype=complex)
    rhs = np.array([1.0, 1.0, 0.0])

    for j in range(3):
        xj = x_vals[j]
        kj = k[j]
        # Eq. (20): stress-free at x=0
        M[0, j] = (1j * omega) / (v_s * v_s * xj)
        # Eq. (21): loaded at x=L with delay rod
        M[1, j] = (1j * omega / v_s) * (1.0 / (v_s * xj) - Z_R / Z_F) * np.exp(1j * kj * L)
        # Eq. (22): electrical B.C. (plane-wave component of D zero)
        M[2, j] = (1j * omega * xj) * (1.0 + K2 - 1.0 / (v_s * v_s * xj * xj))

    # Solve for amplitude ratios λ_j
    lam = np.linalg.solve(M, rhs)

    # Auxiliary sums required by the efficiency formula (Eq. 15)
    S_exp = np.sum(lam * np.exp(1j * k * L))
    S_k   = np.sum(lam / k * np.exp(1j * k * L))
    S_d   = np.sum(lam * (1.0 - 1.0 / (v_s * v_s * x_vals * x_vals)) * (np.exp(1j * k * L) - 1.0))

    # Numerator: K^2 * Re{i ω Σ λ_j exp(i k_j L)} * [-1 + (i ω^2/v_s^2) Σ (λ_j/k_j) exp(i k_j L)]
    A_re = -omega * np.imag(S_exp)            # Re{ i ω S_exp }
    B = -1.0 + (1j * omega * omega / (v_s * v_s)) * S_k
    numerator = K2 * A_re * B

    # Denominator: ω_c * [ L + Σ λ_j(1 - ω^2/(v_s^2 k_j^2)) (exp(i k_j L)-1) ]
    D = L + S_d
    denominator = omega_c * D

    # Efficiency is a real quantity
    G = np.real(numerator / denominator)
    return G