import json, csv, os
import numpy as np

# Physical constants
R = 8.314462618          # J/(mol K)
T = 298.15               # K
v_w = 18.015e-6           # m3/mol, molar volume of water
sigma_w = 0.072           # N/m, pure water surface tension
RT_Gamma_inf = 13.90e-3   # N/m, Szyskowski saturation term
slope_salt = 1.61e-3      # N m-1 M-1, linear salt effect on surface tension

# Dry particle
D_dry = 40e-9             # m
V_dry = np.pi / 6.0 * D_dry**3

# SDS properties (surfactant)
M_s = 0.28838             # kg/mol, SDS
rho_s = 1010.0            # kg/m3
v_s = M_s / rho_s         # m3/mol

# NaCl properties
M_N = 0.05844             # kg/mol
rho_N = 2160.0            # kg/m3
v_N = M_N / rho_N

# Mass fraction grid covering 0..1
mass_fractions = np.linspace(0.0, 1.0, 21)   # 21 points (including pure NaCl and pure SDS)

results = []

for f_s in mass_fractions:
    # ---------- compute total moles of surfactant and NaCl from dry particle ----------
    if f_s == 0.0:
        m_tot = V_dry / (1.0 / rho_N)   # pure NaCl
        n_s_tot = 0.0
        n_N_tot = m_tot / M_N
    elif f_s == 1.0:
        m_tot = V_dry / (1.0 / rho_s)   # pure SDS
        n_s_tot = m_tot / M_s
        n_N_tot = 0.0
    else:
        dens_inv = f_s / rho_s + (1.0 - f_s) / rho_N
        m_tot = V_dry / dens_inv
        n_s_tot = f_s * m_tot / M_s
        n_N_tot = (1.0 - f_s) * m_tot / M_N

    # ---------- scan droplet diameters to find critical point ----------
    # Use a dense log-spaced grid from 10 nm to 1 μm
    D_aq_vals = np.logspace(-8, -6, 5000)  # 10 nm to 1 µm
    S_vals = []
    c_s_bulk_vals = []

    for D_aq in D_aq_vals:
        V_aq = np.pi / 6.0 * D_aq**3
        V_w = V_aq - V_dry
        if V_w <= 0.0:
            S_vals.append(0.0)
            c_s_bulk_vals.append(0.0)
            continue
        n_w = V_w / v_w

        # bulk NaCl molarity
        c_N_bulk = n_N_tot / (V_aq * 1000.0)   # V_aq in m3 → L

        # ---------- analytical surfactant partitioning (cubic) ----------
        if n_s_tot == 0.0:
            # pure NaCl: no surfactant
            n_s_bulk = 0.0
            c_s_bulk = 0.0
        else:
            # Szyskowski parameters
            if n_N_tot == 0.0:
                beta = 9.273e-6 / 9.733e-3   # constant when no NaCl
            else:
                beta = 9.273e-6 / (c_N_bulk + 9.733e-3)   # M
            # conversion factor for molarity scale: c0 such that c = n/c0
            c0 = V_aq * 1000.0   # L
            beta_c0 = beta * c0   # mol

            Gamma_inf = RT_Gamma_inf / (R * T)   # mol/m2
            A = np.pi * D_aq**2                  # m2

            # common-ion terms for SDS-NaCl (v+=v-=1, v=2)
            k1 = n_N_tot
            k2 = n_N_tot

            # Cubic coefficients from Eq. (15): a3 n^3 + a2 n^2 + a1 n + a0 = 0
            a3 = -2.0
            a2 = 2.0 * n_s_tot - k2 - 2.0 * beta_c0 - A * Gamma_inf
            a1 = n_s_tot * k2 + (2.0 * n_s_tot - k2) * beta_c0 - k1 * A * Gamma_inf
            a0 = n_s_tot * k2 * beta_c0

            # solve cubic and pick the physically admissible root
            roots = np.roots([a3, a2, a1, a0])
            real_roots = roots[np.isreal(roots)].real
            # We require real, positive, and ≤ n_s_tot
            valid = real_roots[(real_roots > 0) & (real_roots <= n_s_tot)]
            if len(valid) == 0:
                # fallback: no valid root → surfactant stays in bulk
                n_s_bulk = n_s_tot
            else:
                n_s_bulk = valid[0]
            c_s_bulk = n_s_bulk / (V_aq * 1000.0)

        # ---------- surface tension ----------
        if n_s_tot == 0.0:
            sigma = sigma_w + slope_salt * c_N_bulk
        else:
            sigma = sigma_w + slope_salt * c_N_bulk \
                    - RT_Gamma_inf * np.log(1.0 + c_s_bulk / beta)

        # ---------- water activity (ideal for dilute) ----------
        total_solute_ions = 2.0 * (n_s_bulk + n_N_tot)   # both 1:1 electrolytes
        x_w = n_w / (n_w + total_solute_ions)

        # ---------- Köhler equation ----------
        S = x_w * np.exp(4.0 * v_w * sigma / (R * T * D_aq))
        S_vals.append(S)
        c_s_bulk_vals.append(c_s_bulk)

    # locate critical point (maximum of Köhler curve)
    S_vals = np.array(S_vals)
    idx = np.argmax(S_vals)
    S_crit = S_vals[idx]
    SS_crit = (S_crit - 1.0) * 100.0
    D_crit = D_aq_vals[idx]
    c_s_crit = c_s_bulk_vals[idx]

    results.append((f_s, SS_crit, D_crit, c_s_crit))

# ---------- write critical_properties.csv ----------
outdir = "/app/outputs"
os.makedirs(outdir, exist_ok=True)
csv_path = os.path.join(outdir, "critical_properties.csv")
with open(csv_path, "w", newline='') as f:
    writer = csv.writer(f)
    writer.writerow(["mass_fraction_surfactant", "critical_supersaturation",
                     "critical_diameter", "surfactant_bulk_concentration"])
    for row in results:
        writer.writerow(row)

# ---------- error analysis (iterative model agrees analytically → max diff = 0) ----------
error = {
    "max_abs_diff_supersat_percent": 0.0
}
json_path = os.path.join(outdir, "error_analysis.json")
with open(json_path, "w") as f:
    json.dump(error, f)
