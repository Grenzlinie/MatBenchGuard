import sys, csv, math, numpy as np

# Yeoh hyperelastic constants (Pa)
C10 = 180.7e3
C20 = -16.7e3
C30 = 6.6e3

# Membrane geometry and material
b = 0.0254            # square side length (m)
h0 = 100e-6           # initial thickness (m)
rho_mem = 1000.0      # membrane density (kg/m^3)
rho_E = 1010.0        # electrode density (kg/m^3)
t_elec = 25e-6        # total electrode thickness (m)

# Acoustic radiation
rho_air = 1.204       # air density (kg/m^3)

# Permittivity and pressure
epsilon0 = 8.8541878128e-12
p_ref = 20e-6          # reference pressure (Pa)
q0 = p_ref * (10**(80.0/20.0))   # 80 dB SPL -> 0.2 Pa RMS

# Prestretch values
lambdas = [1.15, 1.38]
# Voltage range 0..5 kV in steps of 0.5 kV
voltages_kV = np.arange(0, 5.01, 0.5)
V_steps = voltages_kV * 1e3   # convert to V

def stress_yeoh(lam):
    I1 = 2*lam**2 + 1/(lam**4)
    S = C10 + 2*C20*(I1-3) + 3*C30*(I1-3)**2
    sigma0 = 2*(lam**2 - 1/(lam**4)) * S
    return sigma0

def static_deflection_center(lam, sigma, Nmax=51):
    """Center displacement in meters."""
    h = h0 / lam**2
    # double series over odd (m,n) up to 2*Nmax+1
    S = 0.0
    for m in range(1, 2*Nmax+1, 2):
        for n in range(1, 2*Nmax+1, 2):
            S += 1.0 / (m * n * (m**2 + n**2))
    delta = (16.0 * q0 * b**2) / (math.pi**4 * sigma * h) * S
    return delta

def mode_shape_centerline(lam, sigma, Nmax=51):
    """Return (x_norm, displacement_norm) array."""
    h = h0 / lam**2
    xs = np.linspace(0, 1, 257)
    disp = np.zeros_like(xs)
    factor = 16.0 * q0 * b**2 / (math.pi**4 * sigma * h)
    for m in range(1, 2*Nmax+1, 2):
        sin_mx = np.sin(m * math.pi * xs)
        for n in range(1, 2*Nmax+1, 2):
            sin_ny05 = np.sin(n * math.pi * 0.5)   # scalar
            coeff = 1.0 / (m * n * (m**2 + n**2))
            disp += sin_mx * sin_ny05 * coeff
    disp *= factor
    max_disp = np.max(np.abs(disp))
    disp_norm = disp / max_disp
    return xs, disp_norm

def lumped_resonance(lam, sigma, include_electrode):
    """Return frequency in Hz."""
    h = h0 / lam**2
    M_aM = 1.3785 * rho_mem * h / (b**2)
    C_aM = 0.0351 * b**4 / (sigma * h)
    M_aRad = 1.486 * rho_air / (2.0 * b)   # radiation mass
    M_aE = 0.0
    if include_electrode:
        M_aE = 1.3785 * rho_E * t_elec / (b**2)
    M_total = M_aM + M_aRad + M_aE
    f = 1.0 / (2.0 * math.pi * math.sqrt(M_total * C_aM))
    return f

def voltage_normalised(lam, sigma0):
    eps_r = -0.28 * lam + 2.76
    h = h0 / lam**2
    M_aM = 1.3785 * rho_mem * h / (b**2)
    M_aRad = 1.486 * rho_air / (2.0 * b)
    M_aE = 1.3785 * rho_E * t_elec / (b**2)
    M_total = M_aM + M_aRad + M_aE
    norms = []
    f0 = None
    for V in V_steps:
        sigma = sigma0 - epsilon0 * eps_r * (lam**2 * V / h0)**2
        if sigma <= 0:
            sigma = 1e-9
        C_aM = 0.0351 * b**4 * (lam**2 / h0) / sigma
        f = 1.0 / (2.0 * math.pi * math.sqrt(M_total * C_aM))
        if V == 0:
            f0 = f
        norms.append(f / f0)
    return norms

# ---- Write functions ----
def write_center_disp():
    with open('/app/outputs/step_01_center_displacement.csv', 'w', newline='') as f:
        w = csv.writer(f)
        w.writerow(['prestretch', 'displacement_nm'])
        for lam in lambdas:
            sig = stress_yeoh(lam)
            delta_m = static_deflection_center(lam, sig)
            delta_nm = delta_m * 1e9
            w.writerow([lam, delta_nm])

def write_mode_shape():
    lam = 1.38
    sig = stress_yeoh(lam)
    xs, disp_norm = mode_shape_centerline(lam, sig)
    with open('/app/outputs/step_02_mode_shape.csv', 'w', newline='') as f:
        w = csv.writer(f)
        w.writerow(['x_norm', 'displacement_norm'])
        for xv, dv in zip(xs, disp_norm):
            w.writerow([float(xv), float(dv)])

def write_resonance():
    with open('/app/outputs/step_03_resonance_frequencies.csv', 'w', newline='') as f:
        w = csv.writer(f)
        w.writerow(['prestretch', 'with_electrode', 'frequency_Hz'])
        for lam in lambdas:
            sig = stress_yeoh(lam)
            f_no = lumped_resonance(lam, sig, False)
            w.writerow([lam, False, f_no])
            f_yes = lumped_resonance(lam, sig, True)
            w.writerow([lam, True, f_yes])

def write_voltage():
    with open('/app/outputs/step_04_voltage_dependence.csv', 'w', newline='') as f:
        w = csv.writer(f)
        w.writerow(['prestretch', 'voltage_kV', 'normalized_frequency'])
        for lam in lambdas:
            sig0 = stress_yeoh(lam)
            norms = voltage_normalised(lam, sig0)
            for Vkv, nf in zip(voltages_kV, norms):
                w.writerow([lam, Vkv, nf])

if __name__ == '__main__':
    target = sys.argv[1]
    if target == 'step_01_center_displacement.csv':
        write_center_disp()
    elif target == 'step_02_mode_shape.csv':
        write_mode_shape()
    elif target == 'step_03_resonance_frequencies.csv':
        write_resonance()
    elif target == 'step_04_voltage_dependence.csv':
        write_voltage()
    else:
        print('Unknown target', file=sys.stderr)
        sys.exit(1)