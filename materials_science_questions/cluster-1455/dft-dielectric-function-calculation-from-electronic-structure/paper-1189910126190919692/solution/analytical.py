import json
import math
import cmath

# Reference static dielectric constants (paper-reported DFT)
pristine = {'epsilon_x': 6.7, 'epsilon_y': 6.5, 'epsilon_z': 4.5}
sn_intercalated = {'epsilon_x': 13.3, 'epsilon_y': 13.2, 'epsilon_z': 4.8}

# Lorentz oscillator parameters for epsilon_x along [100] (neglect damping)
omega_TO = 820.0   # cm^-1
omega_LO = 972.0   # cm^-1
gamma = 0.0

# Dielectric environment
epsilon_air = 1.0
epsilon_Si = 11.7   # mid-IR

# Flake thickness
d_um = 0.120   # 120 nm

def epsilon_x(nu, eps_inf):
    """Complex epsilon_x at wavenumber nu (cm^-1)."""
    den = omega_TO**2 - nu**2 - 1j * gamma * nu
    return eps_inf * (1.0 + (omega_LO**2 - omega_TO**2) / den)

def compute_dispersion(eps_x_inf, eps_z_inf, freqs):
    wavevecs = []
    for nu in freqs:
        k0_um = 2.0 * math.pi * nu * 1e-4          # k0 in um^-1
        k0_d = k0_um * d_um                        # dimensionless
        eps_x_c = epsilon_x(nu, eps_x_inf)
        eps_z_c = complex(eps_z_inf, 0.0)
        rho = 1j * cmath.sqrt(eps_z_c / eps_x_c)   # rho = i * sqrt(eps_z / eps_x)
        arg1 = (epsilon_air * rho) / eps_z_c
        arg2 = (epsilon_Si * rho) / eps_z_c
        sum_atan = cmath.atan(arg1) + cmath.atan(arg2)
        q = (rho / k0_d) * sum_atan                # normalised in-plane momentum
        k_um = (q * k0_um).real                    # in-plane wavevector, um^-1
        if k_um < 0.0:
            k_um = -k_um
        wavevecs.append(round(k_um, 6))
    return wavevecs

# Frequency sampling (inside the Reststrahlen band, avoiding the exact TO pole)
nu_list = list(range(825, 970, 5))  # 825,830,...,965
if 860 not in nu_list:
    nu_list.append(860)
    nu_list.sort()

k_pristine = compute_dispersion(pristine['epsilon_x'], pristine['epsilon_z'], nu_list)
k_sn = compute_dispersion(sn_intercalated['epsilon_x'], sn_intercalated['epsilon_z'], nu_list)

# Build dispersion arrays
disp_pristine = [{'frequency_cm-1': nu, 'wavevector_um-1': k} for nu, k in zip(nu_list, k_pristine)]
disp_sn = [{'frequency_cm-1': nu, 'wavevector_um-1': k} for nu, k in zip(nu_list, k_sn)]

# Relative shift at 860 cm^-1
idx860 = nu_list.index(860)
shift = (k_pristine[idx860] - k_sn[idx860]) / k_pristine[idx860]

output = {
    'pristine': pristine,
    'Sn_intercalated': sn_intercalated,
    'dispersion_shift': round(shift, 6),
    'analytical_dispersion_pristine': disp_pristine,
    'analytical_dispersion_Sn': disp_sn
}

with open('/app/outputs/dft_and_dispersion_results.json', 'w') as f:
    json.dump(output, f, indent=2)
