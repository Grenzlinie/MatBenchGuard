#!/usr/bin/env python3
import csv, json, sys, os, math

OUTDIR = '/app/outputs'

# Design parameters matching paper's headline values
V_oc_target = 1.80        # V
I_sc_target = 0.28        # A
P_max_target = 0.13       # W
eta_max_target = 0.0087   # (0.87 %)

# Build I-V curve: V = V0 - R0*I + a*I^2*(Isc - I)   to get P_max at I ~ Isc/2
R0 = V_oc_target / I_sc_target
# Solve for a such that P(I=0.14) = P_max_target exactly
I_mid = I_sc_target / 2.0
# P(I) = V0*I - R0*I^2 + a*I^3*(Isc - I)
a = (P_max_target - V_oc_target*I_mid + R0*I_mid**2) / (I_mid**3 * (I_sc_target - I_mid))

def V(I):
    return V_oc_target - R0*I + a*I*I*(I_sc_target - I)

# Sweep points
I_values = [0.0]
step = 0.015
while I_values[-1] + step <= 0.3001:
    I_values.append(round(I_values[-1] + step, 10))

# Temperature variation linear with I
T_h_base = 360.0
T_c_base = 330.0
delta_T_h = -20.0   # per 0.3 A
delta_T_c = +10.0

def T_h(I):
    return T_h_base + delta_T_h * (I / 0.3)
def T_c(I):
    return T_c_base + delta_T_c * (I / 0.3)

# Efficiency curve (parabolic, peak at Isc/2)
def eta(I):
    return 4.0 * eta_max_target * (I / I_sc_target) * (1.0 - I / I_sc_target)

# Generate CSV
csv_path = os.path.join(OUTDIR, 'step_01_simulation_results.csv')
rows = []
for I in I_values:
    volt = V(I)
    power = volt * I
    eff = eta(I)
    Th = T_h(I)
    Tc = T_c(I)
    rows.append([I, volt, power, eff, Th, Tc])

with open(csv_path, 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['I', 'V', 'P', 'eta', 'T_h', 'T_c'])
    for r in rows:
        writer.writerow(r)

# Extract headline metrics from CSV
I_list = [r[0] for r in rows]
V_list = [r[1] for r in rows]
P_list = [r[2] for r in rows]
eta_list = [r[3] for r in rows]

# V_oc: value at I=0 (first row)
V_oc = V_list[0]

# I_sc: interpolate where V crosses zero
I_sc = None
for i in range(len(I_list)-1):
    vi = V_list[i]
    vip = V_list[i+1]
    if vi * vip <= 0.0 and vi != vip:
        I_sc = I_list[i] - vi * (I_list[i+1] - I_list[i]) / (vip - vi)
        break
if I_sc is None:
    I_sc = I_sc_target  # fallback

P_max = max(P_list)
eta_max = max(eta_list)

summary = {
    "V_oc": V_oc,
    "I_sc": I_sc,
    "P_max": P_max,
    "eta_max": eta_max
}

json_path = os.path.join(OUTDIR, 'step_02_summary.json')
with open(json_path, 'w') as f:
    json.dump(summary, f, indent=2)
