import json, math

omega = 2 * math.pi * 55e6
v0 = 4.5e5
eta_sq = 0.02
epsilon = 8.23e-13
Delta_eV = 0.02
E_act_eV = 0.15
sigma0_inf = 0.05
k_B_eV = 8.617333262145e-5
T_illum = 300.0

pref = 0.7 * omega * eta_sq / v0

# temperature scenario
T_vals = [300 + i * (600 / 299) for i in range(300)]
sigma_T_vals = []
alpha_T_vals = []
for T in T_vals:
    sigma = sigma0_inf * math.exp(-E_act_eV / (k_B_eV * T))
    tau_c = epsilon / sigma
    x = omega * tau_c * math.exp(2.1 * Delta_eV / (k_B_eV * T))
    alpha = pref * (k_B_eV * T / Delta_eV) * math.atan(x / (1 + x * x))
    sigma_T_vals.append(sigma)
    alpha_T_vals.append(alpha)

# illumination scenario (fixed T=300 K)
sigma_I_vals = []
alpha_I_vals = []
for i in range(300):
    log_sigma = -10.0 + (10.0 * i / 299)
    sigma = 10 ** log_sigma
    tau_c = epsilon / sigma
    x = omega * tau_c * math.exp(2.1 * Delta_eV / (k_B_eV * T_illum))
    alpha = pref * (k_B_eV * T_illum / Delta_eV) * math.atan(x / (1 + x * x))
    sigma_I_vals.append(sigma)
    alpha_I_vals.append(alpha)

# find maxima
max_idx_T = max(range(len(alpha_T_vals)), key=lambda i: alpha_T_vals[i])
sigma_T = sigma_T_vals[max_idx_T]
alpha_T = alpha_T_vals[max_idx_T]

max_idx_I = max(range(len(alpha_I_vals)), key=lambda i: alpha_I_vals[i])
sigma_I = sigma_I_vals[max_idx_I]
alpha_I = alpha_I_vals[max_idx_I]

homogeneous_sigma = epsilon * omega

verification = {
    "sigma_T_gt_sigma_I": sigma_T > sigma_I,
    "sigma_T_not_equal_homogeneous": abs(sigma_T - homogeneous_sigma) / max(abs(sigma_T), abs(homogeneous_sigma)) > 1e-6
}

result = {
    "params": {
        "omega_rad_s": omega,
        "v0_cm_s": v0,
        "eta_sq": eta_sq,
        "epsilon_F_cm": epsilon,
        "Delta_eV": Delta_eV,
        "E_act_eV": E_act_eV,
        "sigma0_inf_S_cm": sigma0_inf,
        "k_B_eV_per_K": k_B_eV,
        "T_illum_K": T_illum
    },
    "curves": [
        {
            "scenario": "temperature",
            "sigma": sigma_T_vals,
            "alpha": alpha_T_vals
        },
        {
            "scenario": "illumination",
            "sigma": sigma_I_vals,
            "alpha": alpha_I_vals
        }
    ],
    "temperature_maximum": {
        "sigma_T": sigma_T,
        "alpha_T": alpha_T
    },
    "illumination_maximum": {
        "sigma_I": sigma_I,
        "alpha_I": alpha_I
    },
    "homogeneous_sigma": homogeneous_sigma,
    "verification": verification
}

with open("/app/outputs/absorption_results.json", "w") as f:
    json.dump(result, f, indent=2)
