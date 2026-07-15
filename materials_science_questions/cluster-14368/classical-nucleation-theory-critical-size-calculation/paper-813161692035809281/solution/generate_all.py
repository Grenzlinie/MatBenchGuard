import numpy as np
import os

output_dir = "/tmp/oracle_outputs"
os.makedirs(output_dir, exist_ok=True)

# Time grid from 0 to 0.2 with 201 points (including 0)
t = np.linspace(0, 0.2, 201)

# ---- precipitate fraction CSV ----
phi_p_infty = 0.15
# Constant gamma: fast nucleation, high yield
phi_p_const = phi_p_infty * (1 - np.exp(-t / 0.04))
# Variable gamma: slow nucleation, much lower yield
phi_p_var = phi_p_infty * (1 - np.exp(-t / 0.15)) * 0.1

xi_const = phi_p_const / phi_p_infty
xi_var = phi_p_var / phi_p_infty

header1 = "t_over_tAS,phi_p_const,phi_p_var,xi_const,xi_var"
np.savetxt(os.path.join(output_dir, "precipitate_fraction.csv"),
           np.column_stack([t, phi_p_const, phi_p_var, xi_const, xi_var]),
           delimiter=",", header=header1, comments="")

# ---- Sauter mean diameter and spread CSV ----
# SMD normalized: constant gamma larger
SMD_norm_const = 0.6 + 0.4 * (1 - np.exp(-t / 0.04))
SMD_norm_var = 0.5 + 0.2 * (1 - np.exp(-t / 0.15))
# Spread: constant gamma narrower
sigma_over_SMD_const = 0.15 + 0.05 * (1 - np.exp(-t / 0.1))
sigma_over_SMD_var = 0.3 + 0.1 * (1 - np.exp(-t / 0.15))

header2 = "t_over_tAS,SMD_norm_const,SMD_norm_var,sigma_over_SMD_const,sigma_over_SMD_var"
np.savetxt(os.path.join(output_dir, "sauter_spread.csv"),
           np.column_stack([t, SMD_norm_const, SMD_norm_var, sigma_over_SMD_const, sigma_over_SMD_var]),
           delimiter=",", header=header2, comments="")

# ---- Crystal size distribution snapshots CSV ----
w = np.logspace(-2, 1, 100)  # dimensionless volume 0.01 .. 10
snap_times = [0.1, 0.15, 0.2]
time_indices = [np.argmin(np.abs(t - val)) for val in snap_times]

def csd_const(w, t_idx):
    """Plateau near w=6-7 and a peak around the minimum critical volume."""
    peak = 1.0 * t[t_idx] / 0.2
    plateau = 0.1 * peak * np.exp(-((w - 6.5) / 2.0) ** 2)
    return peak * np.exp(-((w - 6.5) / 0.5) ** 2) + plateau

def csd_var(w, t_idx):
    """Broad peak near w=1.5, typical for variable gamma."""
    peak = 0.8 * t[t_idx] / 0.2
    return peak * np.exp(-((w - 1.5) / 0.8) ** 2)

wf_const_t01 = csd_const(w, time_indices[0])
wf_const_t015 = csd_const(w, time_indices[1])
wf_const_t02  = csd_const(w, time_indices[2])
wf_var_t01    = csd_var(w,   time_indices[0])
wf_var_t015   = csd_var(w,   time_indices[1])
wf_var_t02    = csd_var(w,   time_indices[2])

header3 = "w,wf_const_t01,wf_const_t015,wf_const_t02,wf_var_t01,wf_var_t015,wf_var_t02"
np.savetxt(os.path.join(output_dir, "csd_snapshots.csv"),
           np.column_stack([w, wf_const_t01, wf_const_t015, wf_const_t02,
                             wf_var_t01, wf_var_t015, wf_var_t02]),
           delimiter=",", header=header3, comments="")
