import numpy as np
import json
from scipy.signal import hilbert


def main():
    # Physical parameters
    alpha = 1.0
    EF_K = 4.21
    T_K = 0.15
    kB_cm = 1.4388
    EF = EF_K / kB_cm
    T = T_K / kB_cm
    beta = 1.0 / T

    # Energy grid (cm^{-1})
    E_min, E_max, N = -80.0, 80.0, 2048
    E = np.linspace(E_min, E_max, N)
    dE = E[1] - E[0]
    idx0 = np.argmin(np.abs(E))

    # Cutoff function xi(E)
    xi = 1.0 / (1.0 + (np.abs(E) / 20.0)**4)

    # Particle-hole response function phi_PH (Eq. 23)
    phi_PH = np.zeros(N)
    non_zero = np.abs(E) > 1e-8
    E_nz = E[non_zero]
    denom = 1.0 - np.exp(-beta * E_nz)
    ln_term = np.log((1.0 + np.exp(-beta * EF)) / (1.0 + np.exp(beta * (E_nz - EF))))
    phi_PH[non_zero] = alpha * xi[non_zero] * (E_nz + ln_term / beta) / denom
    # limit at E=0
    phi_PH[idx0] = alpha * xi[idx0] * T

    # Phonon response function (simplified Eq. 24)
    ELP = 8.05
    Gamma_LP = 0.5
    A_LP = 5.0
    phi_phon_peak = A_LP * Gamma_LP**2 / ((E - ELP)**2 + Gamma_LP**2)
    phi_phon_cont = 0.02 * E**2 * xi
    phi_phon = (phi_phon_peak + phi_phon_cont) * xi / (1.0 - np.exp(-beta * E) + 1e-12)
    phi_phon[idx0] = 0.0

    total_phi = phi_PH + phi_phon

    # Regularize to ensure integrability (phi ~ E^2 at small E)
    delta_reg = 0.1
    reg = E**2 / (E**2 + delta_reg**2)
    total_phi_reg = total_phi * reg
    total_phi_reg[idx0] = 0.0

    # H(E) = phi_reg(E) / E^2 (regular)
    H = np.zeros(N)
    mask = np.abs(E) > 1e-8
    H[mask] = total_phi_reg[mask] / (E[mask]**2)
    if idx0 > 0 and idx0 < N - 1:
        H[idx0] = (H[idx0 - 1] + H[idx0 + 1]) / 2.0
    else:
        H[idx0] = 0.0

    # Compute g(t) = K(t) - K0
    T_max = 40.0
    Nt = 2000
    t = np.linspace(0, T_max, Nt)
    dt = t[1] - t[0]
    integrand_K = H[:, None] * np.exp(1j * E[:, None] * t[None, :])
    K = np.trapz(integrand_K, E, axis=0)
    K0 = np.trapz(H, E)
    g = K - K0

    # Absorption spectrum I(omega) via integration
    gamma = 0.5  # cm^{-1}
    I = np.zeros(N)
    exp_g_damp = np.exp(g[None, :] - gamma * t[None, :])
    for i, omega in enumerate(E):
        integrand_t = np.exp(-1j * omega * t) * exp_g_damp[0, :]
        I[i] = 2.0 * np.real(np.trapz(integrand_t, t))
    I = np.maximum(I, 0.0)

    # Complex refractive index Phi using Hilbert transform
    analytic = hilbert(I)
    H_I = np.imag(analytic)
    Phi = np.pi * H_I - 1j * np.pi * I

    # First-order Raman spectra W1
    B = 1.0
    excitations = [30.0, 50.0, -30.0, -50.0]
    keys = ['E0_plus_30', 'E0_plus_50', 'E0_minus_30', 'E0_minus_50']
    Raman_spectra = {}
    for w0, key in zip(excitations, keys):
        shift = w0 - E
        H_shift = np.interp(shift, E, H, left=0.0, right=0.0)
        Phi_w0 = np.interp(w0, E, Phi)
        diff = np.abs(Phi - Phi_w0)**2
        W1 = B * H_shift * diff
        Raman_spectra[key] = W1.tolist()

    result = {
        'Raman_spectra': Raman_spectra,
        'response_function': total_phi.tolist(),
        'energy_grid': E.tolist()
    }

    with open('/app/outputs/rrs_results.json', 'w') as f:
        json.dump(result, f)


if __name__ == '__main__':
    main()