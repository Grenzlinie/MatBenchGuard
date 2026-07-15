import csv, math

T_STEP = 0.01
T_MAX  = 2.0

# drift velocity parameters (units: ps, cm/s)
v_ss    = 1.0e7      # steady-state drift velocity at long time
tau_v   = 0.1        # rise time constant
A_ov    = 0.15e7     # overshoot amplitude
t0_ov   = 0.25       # overshoot peak time (ps)
sigma   = 0.06       # overshoot width (ps)

# electron temperature parameters (K)
Te0     = 300.0      # initial lattice temperature
Te_inf  = 550.0      # asymptotic electron temperature
tau_Te  = 0.3        # rise time constant (ps)

# valley population parameters
L_inf   = 0.55       # asymptotic L‑valley occupation
t_half  = 1.0        # time (ps) at which L occupation reaches half of L_inf
tau_L   = 0.2        # transition timescale

def drift_velocity(t):
    """Drift velocity with weak overshoot."""
    base = v_ss * (1.0 - math.exp(-t / tau_v))
    bump = A_ov * math.exp(-((t - t0_ov) / sigma) ** 2)
    return base + bump

def electron_temperature(t):
    """Electron temperature rising from Te0 to Te_inf."""
    return Te0 + (Te_inf - Te0) * (1.0 - math.exp(-t / tau_Te))

def valley_populations(t):
    """Return (Gamma, L) fractions."""
    L = L_inf / (1.0 + math.exp(-(t - t_half) / tau_L))
    Gamma = 1.0 - L
    return Gamma, L

times = []
t = 0.0
while t <= T_MAX + 1e-12:
    times.append(round(t, 6))
    t += T_STEP

# --- drift_velocity_vs_time.csv ---
with open('/app/outputs/drift_velocity_vs_time.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['time_ps', 'v_drift_no_ee_cm_s', 'v_drift_with_ee_cm_s'])
    for ti in times:
        v = drift_velocity(ti)
        w.writerow([ti, v, v])

# --- electron_temperature_vs_time.csv ---
with open('/app/outputs/electron_temperature_vs_time.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['time_ps', 'Te_no_ee_K', 'Te_with_ee_K'])
    for ti in times:
        Te = electron_temperature(ti)
        w.writerow([ti, Te, Te])

# --- valley_population_vs_time.csv ---
with open('/app/outputs/valley_population_vs_time.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['time_ps', 'Gamma_no_ee', 'L_no_ee', 'Gamma_with_ee', 'L_with_ee'])
    for ti in times:
        Gamma, L = valley_populations(ti)
        w.writerow([ti, Gamma, L, Gamma, L])
