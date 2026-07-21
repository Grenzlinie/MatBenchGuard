#!/usr/bin/env python3
"""
Fast oracle helper to produce amplitude‑frequency CSV files for the
moderately thick piezoelectric laminated plate model.

Uses:
  - Classical laminated plate theory (CLPT) to compute bending stiffness.
  - Linear frequency shift from piezoelectric actuator forces.
  - Cubic hardening nonlinearity to approximate the harmonic balance results.
"""

import argparse
import csv
import math
import sys

# ----------------------------------------------------------------------
# Material properties (SI)
# ----------------------------------------------------------------------
class Material:
    def __init__(self, E1, E2, G12, G23, G13, nu12, rho, e31, e32):
        self.E1 = E1
        self.E2 = E2
        self.G12 = G12
        self.G23 = G23
        self.G13 = G13
        self.nu12 = nu12
        self.rho = rho
        self.e31 = e31   # C/m^2 (used for actuator forces)
        self.e32 = e32

        # Plane‑stress reduced stiffness in material axes
        nu21 = nu12 * E2 / E1
        denom = 1.0 - nu12 * nu21
        self.Q11 = E1 / denom
        self.Q22 = E2 / denom
        self.Q12 = nu12 * E2 / denom   # = nu21 * E1 / denom
        self.Q66 = G12
        # Transverse shear moduli in material axes:
        # xz plane -> G13, yz plane -> G23

    def Qbar(self, angle_deg):
        """Return (Q11bar, Q22bar, Q12bar, Q66bar) and (C44bar, C55bar) for given angle."""
        if angle_deg == 0:
            return (self.Q11, self.Q22, self.Q12, self.Q66,
                    self.G23, self.G13)
        elif angle_deg == 90:
            # Swap 1<->2
            return (self.Q22, self.Q11, self.Q12, self.Q66,
                    self.G13, self.G23)
        else:
            raise ValueError("Only 0/90 orientations supported")

# Instantiate materials
GRAPHITE = Material(
    E1=132.4e9, E2=10.8e9, G12=5.5e9, G23=3.6e9, G13=5.6e9,
    nu12=0.24, rho=1580.0, e31=0.0, e32=0.0
)

PZT5 = Material(
    E1=62.0e9, E2=62.0e9, G12=23.6e9, G23=18.0e9, G13=23.6e9,
    nu12=0.31, rho=7750.0, e31=19.77, e32=19.77   # sign chosen to increase freq with +V
)

# ----------------------------------------------------------------------
# Laminate definition helpers
# ----------------------------------------------------------------------

# Each layer is a dict: {'mat': Material, 'angle': deg (0 or 90)}
def make_layer(material, angle):
    return {'mat': material, 'angle': angle}

def make_layup(layup):
    """layup is a list of tuples (material, angle)"""
    return [make_layer(m, a) for m, a in layup]

# Lamination sequences used in the paper
LAYUP_TOP_BOTTOM = make_layup([
    (PZT5, 0), (GRAPHITE, 0), (GRAPHITE, 90), (GRAPHITE, 0),
    (GRAPHITE, 90), (GRAPHITE, 0), (PZT5, 0)
])
LAYUP_MIDDLE = make_layup([
    (GRAPHITE, 0), (GRAPHITE, 90), (PZT5, 0), (GRAPHITE, 0),
    (PZT5, 0), (GRAPHITE, 90), (GRAPHITE, 0)
])
LAYUP_INNER = make_layup([
    (GRAPHITE, 0), (PZT5, 0), (GRAPHITE, 90), (GRAPHITE, 0),
    (GRAPHITE, 90), (PZT5, 0), (GRAPHITE, 0)
])

# All‑graphite‑epoxy baseline – same orientation sequence but no PZT5 layers
LAYUP_ALL_GRAPHITE = make_layup([
    (GRAPHITE, 0), (GRAPHITE, 0), (GRAPHITE, 90), (GRAPHITE, 0),
    (GRAPHITE, 90), (GRAPHITE, 0), (GRAPHITE, 0)
])

# ----------------------------------------------------------------------
# Laminate analysis
# ----------------------------------------------------------------------
PZT5_COUPLING_SIGN = 1.0  # sign convention such that +V raises frequency

def compute_stiffness_and_mass(layup, h_total, N_layers):
    """Return A11..A66, D11..D66, A44, A55, I_p (mass per unit area)."""
    assert len(layup) == N_layers
    t_layer = h_total / N_layers
    z0 = -h_total / 2.0

    A = [0.0]*6   # indices 11,12,22,66 for separate use; we'll store in dict
    D = [0.0]*6
    A44 = 0.0
    A55 = 0.0
    I_p = 0.0

    A11 = A12 = A22 = A66 = 0.0
    D11 = D12 = D22 = D66 = 0.0

    for i, layer in enumerate(layup):
        mat = layer['mat']
        angle = layer['angle']
        z_top = z0 + (i+1) * t_layer
        z_bot = z0 + i * t_layer

        Q11b, Q22b, Q12b, Q66b, C44b, C55b = mat.Qbar(angle)

        # A matrix
        A11 += Q11b * t_layer
        A22 += Q22b * t_layer
        A12 += Q12b * t_layer
        A66 += Q66b * t_layer

        # D matrix (integrate z^2)
        z3_diff = (z_top**3 - z_bot**3) / 3.0
        D11 += Q11b * z3_diff
        D22 += Q22b * z3_diff
        D12 += Q12b * z3_diff
        D66 += Q66b * z3_diff

        # Transverse shear stiffness
        A44 += C44b * t_layer
        A55 += C55b * t_layer

        I_p += mat.rho * t_layer

    return {
        'A11': A11, 'A22': A22, 'A12': A12, 'A66': A66,
        'D11': D11, 'D22': D22, 'D12': D12, 'D66': D66,
        'A44': A44, 'A55': A55,
        'I_p': I_p
    }

def bending_stiffness_eff(D_dict):
    """Effective bending stiffness for square simply‑supported plate (m=n=1)."""
    return D_dict['D11'] + D_dict['D22'] + 2.0 * (D_dict['D12'] + 2.0 * D_dict['D66'])

# ----------------------------------------------------------------------
# Frequency computation
# ----------------------------------------------------------------------

def compute_omega0_sq(Deff, I_p, a, h, E_ref):
    """
    Dimensional linear frequency squared [rad^2/s^2] of the square plate.
    ω^2 = (π^4 / a^4) * Deff / I_p
    """
    return (math.pi**4 / a**4) * Deff / I_p

def dim_freq(omega, a, h, E_ref, I_p):
    """
    Convert dimensional ω (rad/s) to dimensionless Ω = ω * a^2 * sqrt(I_p / (E h^3)).
    Actually, from the paper τ = (t / a^2) * sqrt(E h^3 / I_p), so Ω = ω * a^2 / sqrt(E h^3 / I_p).
    """
    return omega * a**2 / math.sqrt(E_ref * h**3 / I_p)

def omega_lin0_direct(Deff, a, h, E_ref, I_p):
    """Direct dimensionless linear frequency Ω_lin0 for the plate (no piezo forces)."""
    omega = math.sqrt(compute_omega0_sq(Deff, I_p, a, h, E_ref))
    return dim_freq(omega, a, h, E_ref, I_p)

def compute_ndelta_omega_sq(N_x, N_y, a, h, E_ref):
    """
    Dimensionless shift Δ(Ω^2) from uniform in‑plane forces N_x, N_y (N/m).
    Derived as:  Δ(Ω^2) = π^2 a^2 (N_x + N_y) / (E h^3)
    """
    return (math.pi**2 * a**2 * (N_x + N_y)) / (E_ref * h**3)

# ----------------------------------------------------------------------
# Actuator forces
# ----------------------------------------------------------------------
def compute_actuator_forces(layup, voltage):
    """
    Return (N_xp, N_yp) for the given layup and applied voltage.
    For each PZT5 layer, N_xp_sum += e31 * V (using positive e31 so +V -> tensile).
    """
    N_x = 0.0
    N_y = 0.0
    for layer in layup:
        mat = layer['mat']
        if mat is PZT5:
            N_x += PZT5_COUPLING_SIGN * mat.e31 * voltage
            N_y += PZT5_COUPLING_SIGN * mat.e32 * voltage
    return N_x, N_y

# ----------------------------------------------------------------------
# Generate amplitude‑frequency curve
# ----------------------------------------------------------------------

def generate_curve(layup, voltage, a, b, h, E_ref, C_nl):
    """
    Compute frequency ratio ω/ω₀ for a range of dimensionless amplitudes.
    ω₀ is the linear dimensionless frequency of the ALL‑GRAPHITE baseline.
    Returns list of (amplitude_ratio, frequency_ratio).
    """
    # Baseline (all‑graphite) properties
    base_props = compute_stiffness_and_mass(LAYUP_ALL_GRAPHITE, h, len(LAYUP_ALL_GRAPHITE))
    Deff_base = bending_stiffness_eff(base_props)
    Omega0_base = omega_lin0_direct(Deff_base, a, h, E_ref, base_props['I_p'])

    # Current laminate properties (V=0)
    props = compute_stiffness_and_mass(layup, h, len(layup))
    Deff = bending_stiffness_eff(props)
    Omega_lin0 = omega_lin0_direct(Deff, a, h, E_ref, props['I_p'])

    # Piezoelectric induced forces and dimensionless frequency shift
    N_x, N_y = compute_actuator_forces(layup, voltage)
    delta_Omega_sq = compute_ndelta_omega_sq(N_x, N_y, a, h, E_ref)

    # Effective linear dimensionless frequency (including piezo forces)
    Omega_lin_sq = Omega_lin0**2 + delta_Omega_sq
    if Omega_lin_sq <= 0:
        Omega_lin_sq = 0.0   # safety
    Omega_lin = math.sqrt(Omega_lin_sq)

    ampl_range = [0.0, 0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45,
                  0.5, 0.55, 0.6, 0.65, 0.7, 0.75, 0.8, 0.85, 0.9, 0.95, 1.0]
    result = []
    for ampl in ampl_range:
        nonlin_factor = math.sqrt(1.0 + C_nl * ampl**2)
        freq_ratio = (Omega_lin / Omega0_base) * nonlin_factor
        result.append((ampl, freq_ratio))
    return result

# ----------------------------------------------------------------------
# Main
# ----------------------------------------------------------------------
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', required=True, help='CSV file path')
    parser.add_argument('--mode', choices=['voltage', 'location'], required=True)
    args = parser.parse_args()

    # Plate geometry (square moderately thick)
    a = 1.0          # m
    b = 1.0          # m
    h = 0.1          # m  (a/h = 10)
    E_ref = 132.4e9  # reference modulus (E_L of graphite-epoxy)
    C_nl = 0.65      # approximate cubic hardening coefficient

    if args.mode == 'voltage':
        voltages = [0, 200, 400, -200, -400]
        layup = LAYUP_TOP_BOTTOM
        with open(args.output, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['amplitude_ratio', 'frequency_ratio', 'voltage'])
            for V in voltages:
                curve = generate_curve(layup, V, a, b, h, E_ref, C_nl)
                for ampl, freq_ratio in curve:
                    writer.writerow([f'{ampl:.4f}', f'{freq_ratio:.6f}', f'{V}'])
    else:  # location
        cases = [
            ('top_bottom', LAYUP_TOP_BOTTOM),
            ('middle', LAYUP_MIDDLE),
            ('inner', LAYUP_INNER)
        ]
        with open(args.output, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['amplitude_ratio', 'frequency_ratio', 'lamination_case'])
            for case_name, layup in cases:
                curve = generate_curve(layup, 0.0, a, b, h, E_ref, C_nl)
                for ampl, freq_ratio in curve:
                    writer.writerow([f'{ampl:.4f}', f'{freq_ratio:.6f}', case_name])

    print(f'Wrote {args.output}')

if __name__ == '__main__':
    main()
