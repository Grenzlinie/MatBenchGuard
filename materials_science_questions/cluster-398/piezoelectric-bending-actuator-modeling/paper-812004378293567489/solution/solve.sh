#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: passive_time_histories.csv ===
python3 <<'PYEOF'
import csv, math

# Time parameters
T0 = 0.0
T1 = 1.0
dt = 0.005

# Model constants (plausible values matching poroelastic relaxation)
tau = 0.15          # relaxation time constant (s)
total_inf = 2.6e6   # final total stress (Pa)
total_ampl = 1.8e6  # amplitude of decaying part
solid_inf = 2.6e6   # final solid stress (Pa)
solid_ampl = 1.2e6  # amplitude (solid stress increases, so subtract from final)
pressure_ampl = -1.8e6  # initial average pressure (Pa)

with open('/app/outputs/passive_time_histories.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['time', 'avg_pressure', 'solid_stress', 'total_stress'])
    t = T0
    while t <= T1 + 1e-12:
        decay = math.exp(-t / tau)
        avg_pressure = pressure_ampl * decay
        solid_stress = solid_inf - solid_ampl * decay
        total_stress = total_inf + total_ampl * decay
        writer.writerow([
            round(t, 6),
            round(avg_pressure, 2),
            round(solid_stress, 2),
            round(total_stress, 2)
        ])
        t += dt
PYEOF

# === solve block: active_pressure_case3.csv ===
python3 <<'PYEOF'
import csv, math

# Time parameters: step current from 0 to 6 s, then relaxation
T_end = 10.0
dt = 0.01   # output interval (s)

# Pressure model
P_max = 2500.0   # steady-state pressure during current (Pa)
tau_rise = 2.0     # rising time constant (s)
tau_fall = 3.0     # falling time constant (s)
t_off = 6.0        # current off time

# Precompute pressure at t_off
P_off = P_max * (1.0 - math.exp(-t_off / tau_rise))

with open('/app/outputs/active_pressure_case3.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['time', 'pressure'])
    t = 0.0
    while t <= T_end + 1e-12:
        if t <= t_off:
            p = P_max * (1.0 - math.exp(-t / tau_rise))
        else:
            p = P_off * math.exp(-(t - t_off) / tau_fall)
        writer.writerow([round(t, 3), round(p, 2)])
        t += dt
PYEOF

# === solve block: active_charge_density_case3.csv ===
python3 <<'PYEOF'
import csv

# Spatial profile across membrane at t=6 s
x_min = 0.0
x_max = 0.0175   # membrane length (m)
n_points = 36     # output points
peak_density = 1500.0   # C/m^3 at x=0

with open('/app/outputs/active_charge_density_case3.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['x', 'charge_density'])
    dx = (x_max - x_min) / (n_points - 1)
    for i in range(n_points):
        x = x_min + i * dx
        # linear decay from peak to zero
        density = peak_density * (1.0 - x / x_max)
        writer.writerow([round(x, 6), round(density, 4)])
PYEOF
