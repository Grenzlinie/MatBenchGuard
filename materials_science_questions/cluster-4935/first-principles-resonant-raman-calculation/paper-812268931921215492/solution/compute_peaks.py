import math

def compute_peak(q_cm, n, mstar_fraction, eps_inf, eps_0, LO_cm):
    e = 4.8032047e-10       # esu
    hbar = 1.0545718e-27    # erg·s
    m_e = 9.1093837e-28     # g
    c_cm = 2.99792458e10    # cm/s

    mstar = mstar_fraction * m_e
    kF = (3.0 * math.pi**2 * n) ** (1.0/3.0)
    alpha = (mstar * math.pi * c_cm) / (hbar * kF**2)
    C = (4.0 * e**2 * mstar * kF) / (math.pi * eps_inf * hbar**2)
    C_over_q2 = C / (q_cm**2)
    factor = 1.0 - eps_inf / eps_0

    best_peak = None
    best_J = -1.0

    omega = 10.0
    while omega <= 300.0:
        u = alpha * omega
        z = q_cm / (2.0 * kF)
        u_minus = u - z
        u_plus = u + z

        # F1 real part
        F1 = 0.5
        if abs(z) > 1e-20:
            if abs(u_minus) > 1e-12:
                ratio1 = (u_minus + 1.0) / (u_minus - 1.0)
                if ratio1 > 0:
                    F1 += (1.0 - u_minus**2) / (8.0 * z) * math.log(abs(ratio1))
            if abs(u_plus) > 1e-12:
                ratio2 = (u_plus + 1.0) / (u_plus - 1.0)
                if ratio2 > 0:
                    F1 += (1.0 - u_plus**2) / (8.0 * z) * math.log(abs(ratio2))
        # F2 imag part
        F2 = 0.0
        if abs(u_minus) < 1.0:
            F2 += (1.0 - u_minus**2) * (math.pi / (8.0 * z))
        if abs(u_plus) < 1.0:
            F2 -= (1.0 - u_plus**2) * (math.pi / (8.0 * z))

        eps_real = 1.0 + C_over_q2 * F1
        eps_imag = C_over_q2 * F2
        den_eps = eps_real**2 + eps_imag**2
        inv_eps_real = eps_real / den_eps
        inv_eps_imag = -eps_imag / den_eps

        coupling_real = factor * (inv_eps_real - 1.0)
        coupling_imag = factor * inv_eps_imag

        D_real = omega**2 - LO_cm**2 - LO_cm**2 * coupling_real
        D_imag = -LO_cm**2 * coupling_imag

        J = -D_imag / (D_real**2 + D_imag**2)
        if J > best_J:
            best_J = J
            best_peak = omega

        omega += 0.2

    return best_peak

if __name__ == '__main__':
    n = 8.4e17       # cm^{-3}
    mstar_frac = 0.0775
    eps_inf = 10.9
    eps_0 = 12.6
    LO_cm = 292.0

    pairs = [
        (1.050e6, '5145'),
        (1.156e6, '4880'),
        (1.205e6, '4765'),
    ]

    print('wavelength,peak_frequency')
    for q_cm, wl in pairs:
        peak = compute_peak(q_cm, n, mstar_frac, eps_inf, eps_0, LO_cm)
        print(f'{wl},{peak:.3f}')