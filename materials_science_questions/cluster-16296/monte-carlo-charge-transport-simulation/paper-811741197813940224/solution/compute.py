import csv
import math
import sys

def main(outpath):
    # Physical constants (SI)
    e = 1.602176634e-19          # C
    eps0 = 8.854187817e-12       # F/m
    kappa = 15.15                # static dielectric constant
    c = 2.99792458e8             # m/s
    m0 = 9.10938356e-31          # kg
    eV_to_J = 1.602176634e-19

    # InAs band parameters
    m_e0 = 0.022 * m0            # electron effective mass (Gamma valley)
    m_h0 = 0.60 * m0             # heavy hole mass
    alpha_Gamma_eV = 2.2         # nonparabolicity (eV^-1)
    eps_g_eV = 0.355             # band gap (eV)
    alpha_Gamma_SI = alpha_Gamma_eV / eV_to_J   # J^-1
    eps_g_J = eps_g_eV * eV_to_J

    # Equilibrium carrier density (n-InAs, doping 2e16 cm^-3)
    n_eq_cm3 = 2e16              # cm^-3

    # Momentum relaxation rate gamma (s^-1) as function of photon energy (eV)
    def gamma(hv_eV):
        if hv_eV < 1.2:
            return 1.7e12
        elif hv_eV <= 1.55:
            # linear ramp from (1.2, 1.7e12) to (1.55, 3.3e12)
            slope = (3.3e12 - 1.7e12) / (1.55 - 1.2)
            return 1.7e12 + slope * (hv_eV - 1.2)
        else:
            return 3.3e12

    # Absorption coefficient alpha (um^-1) vs photon energy (eV)
    alpha_points = [
        (0.50, 0.7),
        (0.70, 1.0),
        (1.00, 2.0),
        (1.20, 3.0),
        (1.40, 5.6),
        (1.50, 6.6),
        (1.55, 7.0),
        (1.60, 7.5),
        (1.70, 8.5),
        (1.80, 9.7),
        (1.90, 11.0),
        (2.00, 13.0),
    ]

    def alpha(hv_eV):
        xs = [pt[0] for pt in alpha_points]
        ys = [pt[1] for pt in alpha_points]
        if hv_eV <= xs[0]:
            return ys[0]
        if hv_eV >= xs[-1]:
            return ys[-1]
        # linear interpolation
        for i in range(len(xs)-1):
            if xs[i] <= hv_eV <= xs[i+1]:
                t = (hv_eV - xs[i]) / (xs[i+1] - xs[i])
                return ys[i] + t * (ys[i+1] - ys[i])
        return ys[-1]   # fallback

    photon_energies = [round(0.5 + 0.1*i, 2) for i in range(16)]  # 0.5 .. 2.0
    fluences_cm2 = [1e13, 1e14]

    rows = []
    for hv_eV in photon_energies:
        hv_J = hv_eV * eV_to_J
        alpha_um_inv = alpha(hv_eV)
        gamma_s = gamma(hv_eV)

        # compute eps_e (J) from energy and momentum conservation
        # Eq. (19) translated to SI with alpha_Gamma_SI
        m_e = m_e0
        m_h = m_h0
        denom = m_e + m_h + math.sqrt((m_e + m_h)**2 +
                                      4 * alpha_Gamma_SI * (hv_J - eps_g_J) * m_e * m_h)
        eps_e_J = (2.0 * (hv_J - eps_g_J) * m_h) / denom

        # eps_h = hv - eps_g - eps_e
        eps_h_J = hv_J - eps_g_J - eps_e_J

        # v_te^2  (Eq. 18)
        x = alpha_Gamma_SI * eps_e_J
        v_te2 = (2.0 * eps_e_J / (3.0 * m_e)) * (
            (1.0 + x) / (1.0 + 4.0 * x * (1.0 + x))
        )

        # v_th^2  (parabolic hole, v_th^2 = 2*eps_h/(3*m_h))
        v_th2 = (2.0 * eps_h_J) / (3.0 * m_h)

        v_t4 = (v_te2 - v_th2) ** 2

        # tilde m_{e0}  (Eq. 20)
        A = 1.0 + 4.0 * x * (1.0 + x)
        tilde_m_e0 = m_e * (3.0 * A ** 1.5) / (3.0 + 8.0 * x * (1.0 + x))

        # reduced mass m*
        m_star = 1.0 / (1.0 / tilde_m_e0 + 1.0 / m_h)

        for fluence_cm2 in fluences_cm2:
            # surface excitation density n_exc (m^-3)
            # alpha_um_inv -> cm⁻¹: multiply by 1e4, then fluence_cm2 yields n_exc_cm3,
            # then convert to m⁻³: multiply by 1e6, net factor 1e10
            n_exc_m3 = alpha_um_inv * fluence_cm2 * 1e10

            # plasma frequency omega_exc
            omega_exc_sq = e**2 * n_exc_m3 / (kappa * eps0 * m_star)
            if omega_exc_sq <= gamma_s**2 / 4.0:
                # low-density limit (Eq. 22), safe to use directly
                W_THz = (e**2 / (12.0 * math.pi * kappa * c**3 * gamma_s)) * (n_exc_m3**2) * v_t4
            else:
                # high-excitation expression (Eq. 24)
                p = gamma_s / math.sqrt(omega_exc_sq - gamma_s**2 / 4.0)
                # inner bracket
                term1 = (4.0/3.0 - p**2) * (2.0 * math.atan(1.0/p) - math.atan(2.0/p))
                term2 = (2.0*p - p**3/2.0) * math.log(p)
                term3 = (p**3/3.0 - 2.0*p) * math.log(p**2 + 1.0)
                term4 = (p - p**3/12.0) * math.log(p**2 + 4.0)
                inner = term1 + term2 + term3 + term4

                W_THz = (e**2 * n_exc_m3**2 * v_t4 *
                         (omega_exc_sq - gamma_s**2/4.0)**1.5) / (
                             6.0 * math.pi * kappa * c**3 * omega_exc_sq**2) * inner

            rows.append((hv_eV, fluence_cm2, W_THz))

    # Write CSV
    with open(outpath, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['photon_energy_eV', 'fluence_cm-2', 'W_THz_J'])
        for hv_eV, fluence_cm2, W in rows:
            writer.writerow([hv_eV, fluence_cm2, W])

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: python3 compute.py <output_csv_path>', file=sys.stderr)
        sys.exit(1)
    main(sys.argv[1])
