#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: curvature_contributions.csv ===
python3 - "$OUTDIR" << 'PYEOF'
import sys, math, csv, os

outdir = sys.argv[1]
os.makedirs(outdir, exist_ok=True)
outpath = os.path.join(outdir, 'curvature_contributions.csv')

# ----- constants (a.u. conversions) -----
au_debye = 2.541746
hartree_to_eV = 27.211386
Bohr_to_Ang = 0.52917721067
eV_to_au = 1.0 / hartree_to_eV
Ang_to_au = 1.0 / Bohr_to_Ang

alpha_au_to_10m24 = 0.1481847   # 1 a.u. = 0.1481847 * 1e-24 esu
beta_au_to_10m30  = 8.6392e-3  # 1 a.u. = 8.6392e-3 * 1e-30 esu
gamma_au_to_10m33 = 5.044e-7   # 1 a.u. = 5.044e-7 * 1e-33 esu

# ----- paper parameters (converted to a.u.) -----
k_eV_ang2   = 33.55
t_eV        =  1.184
q_VB_o_Ang  = -0.12
q_CT_o_Ang  =  0.12
delta_Ang   = q_VB_o_Ang - q_CT_o_Ang   # -0.24 Ang
mu_CT_D     = 26.0
mu_bar_kg   = 1.0e-26
me_kg       = 9.10938356e-31

k_au  = k_eV_ang2 * eV_to_au * (Bohr_to_Ang**2)
t_au  = t_eV * eV_to_au
delta_au = delta_Ang * Ang_to_au
mu_CT_au = mu_CT_D / au_debye
mu_bar_au = mu_bar_kg / me_kg

# pre‑compute pure constants that never change
k_delta_au = k_au * delta_au
k_t2_au    = k_au * t_au * t_au
delta_au2  = delta_au * delta_au
mu_CT_au2  = mu_CT_au * mu_CT_au
mu_CT_au3  = mu_CT_au2 * mu_CT_au
mu_CT_au4  = mu_CT_au3 * mu_CT_au
mu_CT_au5  = mu_CT_au4 * mu_CT_au
mu_CT_au6  = mu_CT_au5 * mu_CT_au

t2 = t_au * t_au
t4 = t2 * t2

N = 100
with open(outpath,'w',newline='') as fcsv:
    writer = csv.writer(fcsv)
    writer.writerow(['f','mu_el','alpha_el','beta_el','gamma_el',
                     'mu_vib','alpha_vib','beta_vib','gamma_vib',
                     'mu_cur','alpha_cur','beta_cur','gamma_cur'])
    for i in range(N+1):
        f = i / N
        # V from analytic inversion: f = 0.5*(1 - V/sqrt(V^2+4t^2))
        if f <= 0.0:
            V_au = 1e6 * t_au
        elif f >= 1.0:
            V_au = -1e6 * t_au
        else:
            V_au = t_au * (1.0 - 2.0*f) / math.sqrt(f*(1.0-f))

        V2 = V_au * V_au
        denom = V2 + 4.0*t2
        sqrt_denom = math.sqrt(denom)
        d15 = denom * sqrt_denom          # denom**1.5
        d25 = denom * d15                # denom**2.5
        d35 = d25 * denom                # denom**3.5
        d45 = d35 * denom                # denom**4.5
        d55 = d45 * denom                # denom**5.5

        # electronic dipole moment and hyperpolarizabilities (a.u.)
        mu_el_au = mu_CT_au * f
        alpha_el_au = (2.0 * mu_CT_au2 * t2) / d15
        beta_el_au  = (6.0 * mu_CT_au3 * t2 * V_au) / d25
        gamma_el_au = (24.0 * mu_CT_au4 * t2 * (V2 - t2)) / d35
        delta_el_au = (120.0 * mu_CT_au5 * t2 * V_au * (V2 - 3.0*t2)) / d45
        chi_el_au   = (720.0 * mu_CT_au6 * t2 * (V2*V2 - 6.0*V2*t2 + 2.0*t4)) / d55

        # force constant K and model factors
        term1 = (2.0 * k_t2_au * delta_au2) / d15
        K_au = k_au * (1.0 - term1)
        B = (6.0 * k_t2_au * delta_au2) / (d15 - 2.0 * k_t2_au * delta_au2)
        C_au = k_delta_au / mu_CT_au
        pref = 1.0 / (4.0 * math.sqrt(mu_bar_au * K_au))

        # curvature contributions (a.u.)
        mu_cur_au = pref * C_au * C_au * (1.0 + B/3.0) * beta_el_au

        t_alpha_cur = (1.0 + B/3.0)**2 * (gamma_el_au + beta_el_au*beta_el_au*(B/(3.0*alpha_el_au) + C_au*C_au/(2.0*K_au)))
        alpha_cur_au = pref * C_au * C_au * t_alpha_cur

        t_beta_cur = (1.0 + B/3.0)**3 * (delta_el_au
                + (11.0 * B * C_au * C_au * beta_el_au * gamma_el_au) / (6.0 * alpha_el_au)
                + (7.0 * B * B * beta_el_au * beta_el_au * beta_el_au) / (12.0 * alpha_el_au * alpha_el_au))
        beta_cur_au = pref * C_au * C_au * t_beta_cur

        t_gamma_cur = (1.0 + B/3.0)**4 * (chi_el_au
                + (8.0 * B * beta_el_au * delta_el_au) / (3.0 * alpha_el_au)
                + (11.0 * B * gamma_el_au * gamma_el_au) / (6.0 * alpha_el_au)
                + (122.0 * B * B * beta_el_au * beta_el_au * gamma_el_au) / (36.0 * alpha_el_au * alpha_el_au)
                + (37.0 * B * B * B * beta_el_au * beta_el_au * beta_el_au * beta_el_au) / (72.0 * alpha_el_au * alpha_el_au * alpha_el_au))
        gamma_cur_au = pref * C_au * C_au * t_gamma_cur

        # vibrational contributions (a.u.)
        mu_vib_au = 0.0
        alpha_vib_au = (2.0/3.0) * B * alpha_el_au
        beta_vib_au = B * (1.0 + B/3.0 + B*B/27.0) * beta_el_au

        # R and C_vib need guard for V2==t2 (rare, B also small then)
        if abs(V2 - t2) > 1e-12:
            R = 9.0 * V2 / (8.0 * (V2 - t2))
        else:
            R = 0.0
        C_vib = 1.5 + B/3.0 + B*B/36.0
        gamma_vib_au = (2.0*B/3.0) * (2.0 + R + (2.0*B/3.0)*(C_vib + 2.0*R*(1.0 + B*C_vib/3.0))) * gamma_el_au

        # convert to output units
        mu_el_D   = mu_el_au * au_debye
        mu_cur_D  = mu_cur_au * au_debye

        alpha_el_24  = alpha_el_au * alpha_au_to_10m24
        alpha_vib_24 = alpha_vib_au * alpha_au_to_10m24
        alpha_cur_24 = alpha_cur_au * alpha_au_to_10m24

        beta_el_30  = beta_el_au * beta_au_to_10m30
        beta_vib_30 = beta_vib_au * beta_au_to_10m30
        beta_cur_30 = beta_cur_au * beta_au_to_10m30

        gamma_el_33  = gamma_el_au * gamma_au_to_10m33
        gamma_vib_33 = gamma_vib_au * gamma_au_to_10m33
        gamma_cur_33 = gamma_cur_au * gamma_au_to_10m33

        writer.writerow([
            f,
            mu_el_D, alpha_el_24, beta_el_30, gamma_el_33,
            0.0, alpha_vib_24, beta_vib_30, gamma_vib_33,
            mu_cur_D, alpha_cur_24, beta_cur_30, gamma_cur_33
        ])
PYEOF
