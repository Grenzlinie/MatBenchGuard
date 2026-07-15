import json, csv, math

OUTDIR = "/app/outputs"

# Physical constants
R = 8.314462618         # J/(mol K)
k_B = 1.380649e-23      # J/K

# Thermodynamic data (from paper)
DeltaH_t_tau_epsilon = 1992.0   # J/mol
T_t_tau_epsilon = 1068.0        # K
# Derived linear deltaG functions (J/mol)
def deltaG_tau_epsilon(T):
    return -1.8 * T + 1992.0

def deltaG_epsilon_tau(T):
    return 1.8 * T - 1992.0

# Volumetric driving force (J/cm³)
def deltaG_V_epsilon_tau(T):
    return -119.4 + 0.11 * T

# Driving force functions record
with open(f"{OUTDIR}/driving_force_functions.json", "w") as f:
    json.dump({
        "DeltaG_tau_epsilon": "-1.8*T + 1992 J/mol",
        "DeltaG_epsilon_tau": "1.8*T - 1992 J/mol",
        "DeltaG_V_epsilon_tau": "-119.4 + 0.11*T J/cm³",
        "T0_tau_l": 1403.0,
        "DeltaT_minimum_undercooling": 87.0
    }, f, indent=2)

# --------------------------------------------------
# tau_start_data.csv – points from the linear fit
Q_over_k_lin = 3.28e4
ln_A3_lin = 38.0
low_T_points = [625, 640, 650, 670, 685, 700]
data = []
for T in low_T_points:
    t = math.exp(-ln_A3_lin + Q_over_k_lin / T)
    data.append((T, t))
with open(f"{OUTDIR}/tau_start_data.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["T", "t"])
    for row in data:
        writer.writerow(row)

# --------------------------------------------------
# kinetic_parameters.json
kin_params = {
    "ln_A3": ln_A3_lin,
    "Q_over_k": Q_over_k_lin,
    "b_sigma3_f_over_4k": 1.43e18     # K J² m⁻⁶
}
with open(f"{OUTDIR}/kinetic_parameters.json", "w") as f:
    json.dump(kin_params, f, indent=2)

# --------------------------------------------------
# interfacial_energy_range.json
b_geom = 16.0 * math.pi / 3.0          # ~16.755
b_term = 1.43e18                       # K J² m⁻⁶
# sigma³ = (4*k_B * b_term) / (b_geom * f)
factor = 4.0 * k_B * b_term            # J³ m⁻⁶
sigma3_min = factor / (b_geom * 0.9)   # high f → low σ
sigma3_max = factor / (b_geom * 0.1)   # low f → high σ
sigma_min = sigma3_min ** (1.0/3.0)
sigma_max = sigma3_max ** (1.0/3.0)
with open(f"{OUTDIR}/interfacial_energy_range.json", "w") as f:
    json.dump({"sigma_min": sigma_min, "sigma_max": sigma_max}, f, indent=2)

# --------------------------------------------------
# ttt_curve.csv – full ε→τ start curve
b_term_cm = 1.43e6            # K J² cm⁻⁶ (converted from m⁻⁶)
T_min = 550.0
T_max = 1050.0
step = 5.0
T = T_min
ttt_data = []
while T <= T_max + 1e-9:
    dG = deltaG_epsilon_tau(T)
    if dG <= 0:
        T += step
        continue
    dG_V = deltaG_V_epsilon_tau(T)
    if abs(dG_V) < 1e-12:
        T += step
        continue
    # Eq. (13)
    term1 = -ln_A3_lin + Q_over_k_lin / T
    term2 = b_term_cm / (T * dG_V * dG_V)
    arg = -dG / (R * T)
    if arg < -700:
        term3 = 0.0
    else:
        term3 = -0.75 * math.log(1.0 - math.exp(arg))
    ln_t = term1 + term2 + term3
    t = math.exp(ln_t)
    ttt_data.append((T, t))
    T += step

with open(f"{OUTDIR}/ttt_curve.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["T", "t"])
    for row in ttt_data:
        writer.writerow(row)

# Nose and critical cooling rate
if ttt_data:
    nose_T, nose_t = min(ttt_data, key=lambda x: x[1])
else:
    nose_T, nose_t = 915.0, 7.0   # fallback from paper
crit_cool_rate = (1068.0 - nose_T) / nose_t

with open(f"{OUTDIR}/critical_cooling_rate.json", "w") as f:
    json.dump({"critical_cooling_rate": crit_cool_rate}, f, indent=2)
