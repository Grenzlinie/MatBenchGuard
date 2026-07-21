#!/usr/bin/env python3
import numpy as np
import csv
import os

OUTDIR = '/app/outputs'
os.makedirs(OUTDIR, exist_ok=True)

# =============================================================================
# Parameters (all lengths in nm)
# =============================================================================
lambda_sf = 5.0
lambda_phi = 1.0
lambda_J = 1.0
D_arb = 1.0                # D for steps 1,2,4,5 (arbitrary units)

# Derived
lambda_par_inv2 = 1.0/lambda_sf**2 + 1.0/lambda_phi**2
k_hat = np.sqrt(lambda_par_inv2 - 1j / lambda_J**2)

# =============================================================================
# Helper: single-layer solution and torque
# =============================================================================
def S_hat_single(z, d, S0):
    """Complex transverse spin density for TI/FM bilayer, Eq. (6)."""
    return S0 * np.cosh(k_hat * (z - d)) / np.cosh(k_hat * d)

def T_hat_single(d, S0):
    """Integrated torque for TI/FM bilayer, Eq. (10) with D=1."""
    prefactor = (1.0/lambda_phi**2 - 1j/lambda_J**2)
    return S0 * prefactor * D_arb * np.tanh(k_hat * d) / k_hat

# =============================================================================
# Step 01: TI/FM spin accumulation profile
# =============================================================================
def step01():
    d = 8.0
    S0 = 1.0
    z_vals = np.linspace(0.0, d, 100)
    S_vals = S_hat_single(z_vals, d, S0)
    S_perp = np.real(S_vals)
    S_z = -np.imag(S_vals)        # paper convention: Š = S_perp + i S_z

    outfile = os.path.join(OUTDIR, 'step_01_spin_density_profile.csv')
    with open(outfile, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['z', 'S_perp', 'S_z'])
        for z, p, sz in zip(z_vals, S_perp, S_z):
            writer.writerow([f'{z:.6f}', f'{p:.12f}', f'{sz:.12f}'])

# =============================================================================
# Step 02: TI/FM integrated torque vs FM thickness
# =============================================================================
def step02():
    S0 = 1.0
    d_arr = np.arange(0.5, 20.1, 0.5)
    T_vals = T_hat_single(d_arr, S0)
    T_perp = np.real(T_vals)
    T_z = np.imag(T_vals)

    outfile = os.path.join(OUTDIR, 'step_02_torque_vs_d.csv')
    with open(outfile, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['d', 'T_perp', 'T_z'])
        for d, tp, tz in zip(d_arr, T_perp, T_z):
            writer.writerow([f'{d:.6f}', f'{tp:.12f}', f'{tz:.12f}'])

# =============================================================================
# Step 03: TI/FM spin-torque efficiency
# =============================================================================
def step03():
    # v_F = 5e5 m/s, D = 5 cm^2/s
    v_F_m_per_s = 5e5
    D_cm2_per_s = 5.0
    # Convert to nm units: 1 m = 1e9 nm, 1 cm = 1e7 nm
    v_F_nm_per_s = v_F_m_per_s * 1e9          # 5e14 nm/s
    D_nm2_per_s = D_cm2_per_s * 1e14          # 5e14 nm^2/s
    D_over_vF_nm = D_nm2_per_s / v_F_nm_per_s  # 1.0 nm

    prefactor = (1.0/lambda_phi**2 - 1j/lambda_J**2)
    theta_hat = -np.sqrt(2.0)/2.0 * D_over_vF_nm * prefactor / k_hat
    theta_perp = np.real(theta_hat)
    theta_z = np.imag(theta_hat)

    outfile = os.path.join(OUTDIR, 'step_03_torque_efficiency.csv')
    with open(outfile, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['theta_perp', 'theta_z'])
        writer.writerow([f'{theta_perp:.12f}', f'{theta_z:.12f}'])

# =============================================================================
# Two-layer solver for TI/mdTI
# =============================================================================
def solve_two_layer(d1, d2, S1, S2):
    """
    Solve spin diffusion in a two-layer structure (0..d1 layer1, d1..d_tot layer2)
    with S(0)=S1, S(d_tot)=S2, continuity of S and J at z=d1.
    Returns S piecewise coefficients (A1,B1,A2,B2) and total torque T_hat.
    """
    D_tot = d1 + d2
    k = k_hat
    sinhD = np.sinh(k * D_tot)
    coshD = np.cosh(k * D_tot)
    # B1 = (S2 - S1*cosh(k*D))/sinh(k*D)
    B1 = (S2 - S1 * coshD) / sinhD
    A1 = S1
    # A2, B2 at interface
    A2 = A1 * np.cosh(k * d1) + B1 * np.sinh(k * d1)
    B2 = A1 * np.sinh(k * d1) + B1 * np.cosh(k * d1)

    # Spin current J = -D * dS/dz
    J0 = -D_arb * k * B1                      # dS/dz(0) = k*B1
    J_D = -D_arb * k * (A2 * np.sinh(k * d2) + B2 * np.cosh(k * d2))

    # Integral of S over both layers
    # Layer1 integral
    if d1 > 0:
        int_S1 = (1.0/k) * (A1 * np.sinh(k * d1) + B1 * (np.cosh(k * d1) - 1.0))
    else:
        int_S1 = 0.0
    # Layer2 integral
    int_S2 = (1.0/k) * (A2 * np.sinh(k * d2) + B2 * (np.cosh(k * d2) - 1.0))
    int_S = int_S1 + int_S2

    # Total torque T_hat = -J(d_tot) + J(0) - (1/tau_sf) * int_S
    # tau_sf = lambda_sf^2 / D_arb
    tau_sf = lambda_sf**2 / D_arb
    T_hat = -J_D + J0 - (1.0/tau_sf) * int_S
    return T_hat

# =============================================================================
# Step 04: TI/mdTI torque vs TI thickness d1
# =============================================================================
def step04():
    d2 = 6.0
    S1 = 1.0 + 0j
    S2 = -1.0 + 0j
    d1_arr = np.arange(0.0, 10.1, 0.1)
    T_perp = []
    T_z = []
    for d1 in d1_arr:
        T = solve_two_layer(d1, d2, S1, S2)
        T_perp.append(np.real(T))
        T_z.append(np.imag(T))

    outfile = os.path.join(OUTDIR, 'step_04_TI_mdTI_torque_d1.csv')
    with open(outfile, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['d1', 'T_perp', 'T_z'])
        for d1, tp, tz in zip(d1_arr, T_perp, T_z):
            writer.writerow([f'{d1:.6f}', f'{tp:.12f}', f'{tz:.12f}'])

# =============================================================================
# Step 05: TI/mdTI torque vs spin-source ratio
# =============================================================================
def step05():
    d1 = 3.0
    d2 = 6.0
    ratios = np.arange(0.1, 1.91, 0.1)
    T_perp = []
    T_z = []
    for r in ratios:
        # |S1|+|S2| = 2, |S1|/|S2| = r
        S2_mag = 2.0 / (r + 1.0)
        S1_mag = r * S2_mag
        S1 = S1_mag + 0j   # positive real
        S2 = -S2_mag + 0j  # negative real
        T = solve_two_layer(d1, d2, S1, S2)
        T_perp.append(np.real(T))
        T_z.append(np.imag(T))

    outfile = os.path.join(OUTDIR, 'step_05_TI_mdTI_torque_ratio.csv')
    with open(outfile, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['ratio', 'T_perp', 'T_z'])
        for r, tp, tz in zip(ratios, T_perp, T_z):
            writer.writerow([f'{r:.6f}', f'{tp:.12f}', f'{tz:.12f}'])

# =============================================================================
if __name__ == '__main__':
    step01()
    step02()
    step03()
    step04()
    step05()
