#!/usr/bin/env python3
"""Compute reference artifacts for the droplet evaporation model."""
import sys
import math
import json
import csv

# ---------- constants and water properties ----------
k = 1.380649e-23          # Boltzmann constant (J/K)
N_A = 6.02214076e23       # Avogadro's number
T0 = 300.0                # ambient temperature (K)

# Water properties (from paper Table)
P_s = 3.6e3               # saturated vapor pressure (Pa)
L0_per_mol = 43.8e3       # latent heat per mole (J/mol)
rho = 997.0               # liquid density (kg/m^3)
D_cm2s = 0.25             # diffusion coefficient (cm^2/s)
alpha_c = 0.04            # condensation coefficient
sigma = 71e-3             # surface tension (N/m)
lambda_ = 0.026           # thermal conductivity of gas (W/(m K))
alpha_t = 1.0             # interfacial thermal jump coefficient

# Convert to SI
L0 = L0_per_mol / N_A     # per-molecule latent heat (J)
D = D_cm2s * 1e-4         # diffusion coefficient (m^2/s)

# Molecular mass of water (molar mass 18.015 g/mol)
M_molar = 18.015e-3       # kg/mol
M = M_molar / N_A          # mass of a single water molecule (kg)

# ---------- derived parameters ----------
omega = L0 / (k * T0) - 1.0
omega_plus_1 = omega + 1.0

# parameter a (Eq. 15)
a = (alpha_t * lambda_ * T0) / (D * P_s * omega * omega_plus_1)

# saturated flux density w_s (Eq. 3)
w_s = alpha_c * P_s / math.sqrt(2.0 * math.pi * M * k * T0)

# characteristic length b (Eq. 20)
b = alpha_t * lambda_ / (k * w_s * omega * omega_plus_1 * (a + 1.0))

# characteristic time tau (Eq. 20)
tau = b**2 * rho * k * omega_plus_1 / (alpha_t * lambda_ * M)

# surface tension parameter beta
v_mu = M / rho                         # molecular volume
R_sigma = 2.0 * sigma * v_mu / (k * T0)   # curvature radius factor
beta = R_sigma / (b * omega * (a + 1.0))

# ---------- helper: z(R) (Eq. 24) ----------
def z_of_R(R, phi0, beta):
    """Dimensionless temperature difference z for dimensionless radius R."""
    sqrt_term = math.sqrt(R**2 + 2.0 * R * (1.0 - beta + 2.0 * phi0) + (1.0 + beta)**2)
    return 0.5 * (sqrt_term - R - 1.0 + beta)

# ---------- helper: droplet lifetime (Eq. 29) ----------
def theta_dim(R, phi0, beta):
    """Dimensionless complete evaporation time for initial dimensionless radius R."""
    z = z_of_R(R, phi0, beta)
    if z <= 0.0:
        return 0.0
    # Eq. (29)
    # term1
    term1 = 0.5 * (z - beta) / (phi0**2 * (phi0 - z)**2)
    inner1 = (phi0 * (2.0 * phi0 * z**2 - z * (3.0 * phi0**2 + 1.0) + 2.0 * phi0 * (phi0**2 + phi0 + 1.0))
              - beta * (phi0 * (phi0**2 + 4.0 * phi0 + 3.0) - 2.0 * z * (phi0 + 1.0)))
    # term2
    term2 = -((phi0 + 1.0) * (phi0**2 + beta) * (phi0 - beta) / phi0**3) * math.log(abs((phi0 - beta) / (phi0 - z)))
    # term3
    term3 = -(beta * (beta * (phi0 + 1.0) - phi0) / phi0**3) * math.log(abs(beta / z))
    return term1 * inner1 + term2 + term3

# ---------- output writers ----------
def write_characteristic_params():
    data = {
        "a": a,
        "b": b * 1e9,     # convert m -> nm
        "tau": tau * 1e6,  # convert s -> microseconds
        "beta": beta
    }
    with open("/app/outputs/characteristic_params.json", "w") as f:
        json.dump(data, f, indent=2)
        f.write("\n")

def write_psychrometric_temperature():
    # z_inf = phi0 = (1-f0) / (omega * (a+1))
    rows = []
    for f0 in (0.9, 0.99):
        phi0 = (1.0 - f0) / (omega * (a + 1.0))
        rows.append((f0, phi0))
    with open("/app/outputs/psychrometric_temperature.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["f0", "z_inf"])
        writer.writerows(rows)

def write_droplet_lifetime():
    # conditions
    f0 = 0.5
    phi0 = (1.0 - f0) / (omega * (a + 1.0))
    # generate 20 logarithmically spaced points from 0.01 to 100 µm
    n_points = 20
    um_min, um_max = 0.01, 100.0
    points = [um_min * 10.0**(i * (math.log10(um_max / um_min) / (n_points - 1))) for i in range(n_points)]
    rows = []
    for R_um in points:
        R_m = R_um * 1e-6          # metres
        R_dim = R_m / b            # dimensionless radius
        theta_s = theta_dim(R_dim, phi0, beta) * tau   # seconds
        rows.append((R_um, theta_s))
    with open("/app/outputs/droplet_lifetime.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["R_initial_um", "lifetime_s"])
        writer.writerows(rows)

# ---------- main ----------
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: compute.py <output_basename>", file=sys.stderr)
        sys.exit(1)
    target = sys.argv[1]
    if target == "characteristic_params.json":
        write_characteristic_params()
    elif target == "psychrometric_temperature.csv":
        write_psychrometric_temperature()
    elif target == "droplet_lifetime.csv":
        write_droplet_lifetime()
    else:
        print(f"Unknown output: {target}", file=sys.stderr)
        sys.exit(1)
