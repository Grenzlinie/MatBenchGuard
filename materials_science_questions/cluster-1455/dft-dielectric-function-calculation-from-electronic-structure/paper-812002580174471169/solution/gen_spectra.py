import numpy as np
import csv

# Define epsilon2 as sum of Lorentzians
# Lorentzian: A * gamma^2 / ((w - w0)^2 + gamma^2)
# parameters (w0, A, gamma) where gamma = FWHM/2
peaks = [
    (3.42, 0.3, 0.25),   # E0 peak after scissor shift
    (8.5,  2.5, 1.0),    # E1 at ~8 eV
    (12.5, 3.5, 1.0),    # E2 at ~12 eV
    (50.0, 4.5, 10.0)    # broad high-energy contribution to give eps_inf ~4
]

def eps2(w):
    val = 0.0
    for w0, A, gamma in peaks:
        val += A * gamma**2 / ((w - w0)**2 + gamma**2)
    return val

# Output energies (0-20 eV, step 0.1 eV)
w_out = np.arange(0.0, 20.01, 0.1)
eps2_out = eps2(w_out)

# Dense grid for Kramers-Kronig integration (0-200 eV, step 0.01 eV)
w_dense = np.arange(0.0, 200.01, 0.01)
eps2_dense = eps2(w_dense)

# Compute epsilon1 via KK transform: eps1(w) = 1 + (2/pi) ∫ ω' ε2(ω')/(ω'^2 - w^2) dω'
eps1_out = np.zeros_like(w_out)
for i, w in enumerate(w_out):
    denom = w_dense**2 - w**2
    # Handle the principal value by avoiding the singular point
    integrand = (2.0 / np.pi) * w_dense * eps2_dense / denom
    # set integrand to zero where denom is very small (approximate PV)
    integrand[np.abs(denom) < 1e-8] = 0.0
    eps1_out[i] = 1.0 + np.trapz(integrand, w_dense)

# Complex dielectric function
eps_complex = eps1_out + 1j * eps2_out

# Reflectivity R = | (√ε - 1) / (√ε + 1) |^2
sqrt_eps = np.sqrt(eps_complex)
reflectivity = np.abs((sqrt_eps - 1.0) / (sqrt_eps + 1.0))**2

# Write CSV
with open('/app/outputs/spectra.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['energy', 'epsilon2', 'reflectivity'])
    for e, e2, r in zip(w_out, eps2_out, reflectivity):
        writer.writerow([f'{e:.2f}', f'{e2:.6f}', f'{r:.6f}'])
