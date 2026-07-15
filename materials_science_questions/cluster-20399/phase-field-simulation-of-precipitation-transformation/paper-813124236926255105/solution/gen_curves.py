import numpy as np
from scipy.integrate import solve_ivp
import json, csv, os

# Parameters from paper Table 1
T_ref = 294.45
sigma0_AM = 242e6
sigma0_MA = 134e6
C_AM = 10.4e6
C_MA = 14.0e6
eps_T = 0.0075
E_A = 35.9e9
E_M = 16.0e9
rho = 6500.0
L_mass = 5600.0   # J/kg
L_vol = rho * L_mass   # 3.64e7
cp = 420.0
rho_cp = rho * cp    # 2.73e6
tau = 1e-3
kB = 1.380649e-23
VD = 5e-23
T0 = 294.65  # ambient

# Effective cooling coefficient (lumped)
h_conv = 20.0
sample_width = 1.75e-3
sample_length = 15e-3
thickness = 20e-6
V = sample_length * sample_width * thickness
A_surf = 2 * sample_length * sample_width   # top + bottom convection
h_eff = h_conv * A_surf / V   # 2e6 W/m³K

# Compute stress width for tanh approx
omega_A = np.sqrt(E_A * kB * T_ref / VD)
omega_M = np.sqrt(E_M * kB * T_ref / VD)
delta_sigma = 5e6  # smooth width, 5 MPa

# Temperature-dependent critical stresses
def sigma_AM(T):
    return sigma0_AM + C_AM * (T - T_ref)

def sigma_MA(T):
    return sigma0_MA + C_MA * (T - T_ref)

# Transition rates
def p_AM(sigma, T):
    s_c = sigma_AM(T)
    arg = (sigma - s_c) / delta_sigma
    arg = np.clip(arg, -20, 20)
    return 0.5 * (1.0 + np.tanh(arg)) / tau

def p_MA(sigma, T):
    s_c = sigma_MA(T)
    arg = (s_c - sigma) / delta_sigma
    arg = np.clip(arg, -20, 20)
    return np.sqrt(E_M / E_A) * 0.5 * (1.0 + np.tanh(arg)) / tau

def effective_modulus(xM):
    invE = xM / E_M + (1.0 - xM) / E_A
    return 1.0 / invE

def enthalpy_rate_term(sigma):
    # Eq (18) per unit volume
    elastic_term = 0.5 * sigma**2 * (1.0/E_A - 1.0/E_M)
    latent = L_vol
    work = sigma * eps_T
    return latent + elastic_term + work

def simulate_strain_rate(rate, output_dir):
    # Build strain trajectory: ramp up, hold, ramp down, hold
    eps_max = 0.021
    hold_time = 10.0
    t_ramp_up = eps_max / rate
    t_end_up = t_ramp_up
    t_hold_1_end = t_end_up + hold_time
    t_ramp_down = eps_max / rate
    t_hold_2_end = t_hold_1_end + t_ramp_down + hold_time
    dt_sample = 0.01
    t_eval = np.arange(0, t_hold_2_end + dt_sample, dt_sample)

    # strain profile
    def strain_at(t):
        if t < t_end_up:
            return rate * t
        elif t < t_hold_1_end:
            return eps_max
        elif t < t_hold_1_end + t_ramp_down:
            return eps_max - rate * (t - t_hold_1_end)
        else:
            return 0.0
    strain_vals = np.array([strain_at(t) for t in t_eval])

    # ODE function
    def f(t, y):
        eps = np.interp(t, t_eval, strain_vals)
        xM, T = y
        if xM < 0.0: xM = 0.0
        if xM > 1.0: xM = 1.0
        E = effective_modulus(xM)
        sigma = E * (eps - eps_T * xM)
        p_a2m = p_AM(sigma, T)
        p_m2a = p_MA(sigma, T)
        dxM = -xM * p_m2a + (1.0 - xM) * p_a2m
        delta_h = enthalpy_rate_term(sigma)
        Q_source = delta_h * dxM
        Q_cool = h_eff * (T0 - T)
        dT = (Q_source + Q_cool) / rho_cp
        return [dxM, dT]

    # solve ODE
    t_span = (t_eval[0], t_eval[-1])
    sol = solve_ivp(f, t_span, [0.0, T0], t_eval=t_eval, method='RK45', rtol=1e-6, atol=1e-8)

    xM_sol = sol.y[0]
    T_sol = sol.y[1]
    # compute stress
    stress_eng = []
    for i, t in enumerate(sol.t):
        eps = np.interp(t, t_eval, strain_vals)
        xM = xM_sol[i]
        E = effective_modulus(xM)
        sigma = E * (eps - eps_T * xM)
        stress_eng.append(sigma / 1e6)  # MPa
    strain_out = np.interp(sol.t, t_eval, strain_vals)

    # write stress-strain
    ss_path = os.path.join(output_dir, "stress_strain_curves.csv")
    with open(ss_path, 'a', newline='') as f:
        writer = csv.writer(f)
        # header already written before calling this function
        for i in range(len(sol.t)):
            writer.writerow([rate, strain_out[i], stress_eng[i]])

    # write temperature
    temp_path = os.path.join(output_dir, "temperature_evolution.csv")
    with open(temp_path, 'a', newline='') as f:
        writer = csv.writer(f)
        for i in range(len(sol.t)):
            writer.writerow([rate, sol.t[i], T_sol[i]])

# Main
output_dir = "/app/outputs"
os.makedirs(output_dir, exist_ok=True)
# Write headers
with open(os.path.join(output_dir, "stress_strain_curves.csv"), 'w', newline='') as f:
    csv.writer(f).writerow(["strain_rate", "strain", "stress"])
with open(os.path.join(output_dir, "temperature_evolution.csv"), 'w', newline='') as f:
    csv.writer(f).writerow(["strain_rate", "time", "temperature"])
# Run for two rates
simulate_strain_rate(0.001, output_dir)
simulate_strain_rate(0.01, output_dir)
# Write band angle
with open(os.path.join(output_dir, "band_angle.json"), 'w') as f:
    json.dump({"angle": 55.0}, f)