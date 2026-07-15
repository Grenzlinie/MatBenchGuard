#!/usr/bin/env python3
import csv, sys, math

# RVE geometry (nm)
L_rve = 50.0
V_rve = L_rve**3          # 125000 nm^3

# CNT
r_i = 0.315
r_o = 0.650
r_int = 1.404
L_cnt = 50.0
vol_eff_cnt = math.pi * r_int**2 * L_cnt          # effective CNT volume per fibre
V_CF_per = vol_eff_cnt / V_rve

# Clay
w_plate = 25.0            # platelet width (X2-X3 plane, nm)
d_c    = 1.0
d_I    = 3.0
d_p    = d_c + 2*d_I       # 7 nm effective thickness
vol_eff_clay = w_plate * d_p * L_rve               # effective clay particle volume
V_CP_per = vol_eff_clay / V_rve

# Volume fractions within effective fillers
alpha = d_c / d_p                                     # clay in effective clay
beta = (r_o**2 - r_i**2) / r_int**2                   # CNT in effective CNT

# Constituent material properties (moduli GPa, Poisson's ratio dimensionless)
E_epoxy, v_epoxy = 2.026, 0.4
E_cnt, v_cnt = 1054.0, 0.25
E_clay, v_clay = 178.0, 0.28
E_int, v_int = 16.10, 0.4

# Effective filler properties (rule of mixtures)
E_CP = E_clay * alpha + E_int * (1 - alpha)
E_CF = E_cnt * beta + E_int * (1 - beta)
v_CP = v_clay * alpha + v_int * (1 - alpha)
v_CF = v_cnt * beta + v_int * (1 - beta)
G_CP = E_CP / (2*(1+v_CP))
G_CF = E_CF / (2*(1+v_CF))
G_m  = E_epoxy / (2*(1+v_epoxy))

# Efficiency parameters (l = 50 nm)
l = L_rve
d_cf_eff = 2*r_int
d_cp_eff = d_p
eps_long_CP = 2*l / d_cp_eff        # ≈ 14.2857
eps_long_CF = 2*l / d_cf_eff       # ≈ 35.61
eps_trans_CP = math.sqrt(3) * math.log(l / d_cp_eff)   # ≈ 3.406
eps_trans_CF = 1.0

# Same eps for shear as transverse (Halpin‑Tsai for G often uses these)
eps_shear_CP = eps_trans_CP
eps_shear_CF = eps_trans_CF

# RVE configurations: (n_CNT, n_clay, config_label)
configs = [
    (1,1,"1CNT+1Clay"),
    (1,2,"1CNT+2Clay"),
    (1,3,"1CNT+3Clay"),
    (1,4,"1CNT+4Clay"),
    (1,1,"1Clay+1CNT"),
    (2,1,"1Clay+2CNT"),
    (3,1,"1Clay+3CNT"),
    (4,1,"1Clay+4CNT")
]

writer = csv.writer(sys.stdout)
writer.writerow(["RVE_config","E_L","E_T","G_T","v_L","v_T"])

for n_cnt, n_clay, label in configs:
    V_CP = n_clay * V_CP_per
    V_CF = n_cnt * V_CF_per
    V_m  = 1.0 - V_CP - V_CF
    if V_m < 0:
        V_m = 0.0

    # --- E_L ---
    eta_CP_long = (E_CP/E_epoxy - 1) / (E_CP/E_epoxy + eps_long_CP)
    eta_CF_long = (E_CF/E_epoxy - 1) / (E_CF/E_epoxy + eps_long_CF)
    num = 1 + eps_long_CP*eta_CP_long*V_CP + eps_long_CF*eta_CF_long*V_CF
    den = 1 - eta_CP_long*V_CP - eta_CF_long*V_CF
    E_L = E_epoxy * num / den if den>0 else E_epoxy

    # --- E_T ---
    eta_CP_trans = (E_CP/E_epoxy - 1) / (E_CP/E_epoxy + eps_trans_CP)
    eta_CF_trans = (E_CF/E_epoxy - 1) / (E_CF/E_epoxy + eps_trans_CF)
    num = 1 + eps_trans_CP*eta_CP_trans*V_CP + eps_trans_CF*eta_CF_trans*V_CF
    den = 1 - eta_CP_trans*V_CP - eta_CF_trans*V_CF
    E_T = E_epoxy * num / den if den>0 else E_epoxy

    # --- G_T (Halpin‑Tsai analogue) ---
    eta_CP_shear = (G_CP/G_m - 1) / (G_CP/G_m + eps_shear_CP)
    eta_CF_shear = (G_CF/G_m - 1) / (G_CF/G_m + eps_shear_CF)
    num = 1 + eps_shear_CP*eta_CP_shear*V_CP + eps_shear_CF*eta_CF_shear*V_CF
    den = 1 - eta_CP_shear*V_CP - eta_CF_shear*V_CF
    G_T = G_m * num / den if den>0 else G_m

    # --- v_L (rule of mixtures) ---
    v_L = v_epoxy*V_m + v_CP*V_CP + v_CF*V_CF

    # --- v_T (rule of mixtures; approximate) ---
    v_T = v_epoxy*V_m + v_CP*V_CP + v_CF*V_CF   # same as v_L in simple mixtures
    # Note: a more advanced model would give a different v_T, but the paper's Halpin‑Tsai
    # row provides a single v_T = 0.5423.  The simple mixture yields plausible monotonic values.

    writer.writerow([label, f"{E_L:.4f}", f"{E_T:.4f}", f"{G_T:.4f}", f"{v_L:.4f}", f"{v_T:.4f}"])
