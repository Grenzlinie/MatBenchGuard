#!/usr/bin/env python3
import csv, math, sys, os

# ============================================================
# Material constants (all SI)
# ============================================================

# Aluminium
E_Al   = 72.4e9
nu_Al  = 0.3
G_Al   = 27.8e9
alpha_Al = 22.5e-6

# PZT-5A
E_PZT  = 63.0e9
nu_PZT = 0.3
G_PZT  = 24.2e9
alpha_PZT = 0.9e-6
d31    = 2.54e-10

# Glass-epoxy
E11_g  = 50.0e9
E22_g  = 15.2e9
nu12_g = 0.254
G12_g  = 4.7e9
G13_g  = 4.7e9
G23_g  = 3.28e9
alpha1_g = 6.0e-6
alpha2_g = 23.3e-6

# Derived
Q11_Al = E_Al / (1 - nu_Al**2)
Q11_PZT = E_PZT / (1 - nu_PZT**2)

# Glass-epoxy elastic constants
nu21_g = nu12_g * E22_g / E11_g
dem_g = 1 - nu12_g * nu21_g
Q11_g = E11_g / dem_g
Q22_g = E22_g / dem_g

# Shear correction
k = 5.0/6.0

# Beam length
L = 0.25

# Analytical mu_min * L values
MU_S_S = math.pi / L
MU_C_C = 2*math.pi / L
MU_C_S = 4.49341 / L
MU_C_R = math.pi / L
MU_S_R = math.pi/2 / L

bc_mu = {
    'S-S': MU_S_S,
    'C-C': MU_C_C,
    'C-S': MU_C_S,
    'C-R': MU_C_R,
    'S-R': MU_S_R,
}

# ============================================================
# Helper: compute laminate properties and DeltaT_cr
# ============================================================
def calc_delta_T(layers, bc_name, V):
    """
    layers: list of dicts with keys:
        z_bot, z_top, Q11, G (for shear), alpha, d31 (0 if not piezo)
    returns delta_T_cr in °C
    """
    mu = bc_mu[bc_name]
    mu2 = mu * mu

    a11 = 0.0
    b11 = 0.0
    d11 = 0.0
    a55 = 0.0
    n_T = 0.0   # per unit width, per °C
    n_E = 0.0   # per unit width, per V

    for lyr in layers:
        zb = lyr['z_bot']
        zt = lyr['z_top']
        t = zt - zb
        Q11_i = lyr['Q11']
        G_i   = lyr['G']
        alpha_i = lyr['alpha']
        d31_i  = lyr['d31']

        a11 += Q11_i * t
        b11 += 0.5 * Q11_i * (zt*zt - zb*zb)
        d11 += (1.0/3.0) * Q11_i * (zt**3 - zb**3)
        a55 += k * G_i * t
        n_T += Q11_i * alpha_i * t
        if d31_i != 0.0:   # piezoelectric layer
            n_E += Q11_i * d31_i   # N per unit width per volt

    # effective bending stiffness
    D_eff = d11 - (b11*b11)/a11

    # buckling condition RHS
    denominator = 1.0 + (mu2 * D_eff) / a55
    RHS = (mu2 * D_eff) / denominator

    # critical temperature rise
    delta_T = (RHS - n_E * V) / n_T
    return delta_T

# ============================================================
# Build layer stacks for each configuration
# ============================================================

def make_aluminium():
    # aluminium core 0.01 m, PZT top + bottom 0.001 m each
    # midplane at centre of aluminium
    z_bot_Al = -0.005
    z_top_Al =  0.005
    z_bot_PZT_b = -0.006
    z_top_PZT_b = -0.005
    z_bot_PZT_t =  0.005
    z_top_PZT_t =  0.006

    layers = [
        {'z_bot': z_bot_PZT_b, 'z_top': z_top_PZT_b, 'Q11': Q11_PZT, 'G': G_PZT, 'alpha': alpha_PZT, 'd31': d31},
        {'z_bot': z_bot_Al,    'z_top': z_top_Al,    'Q11': Q11_Al,  'G': G_Al,  'alpha': alpha_Al,  'd31': 0.0},
        {'z_bot': z_bot_PZT_t, 'z_top': z_top_PZT_t, 'Q11': Q11_PZT, 'G': G_PZT, 'alpha': alpha_PZT, 'd31': d31},
    ]
    total_thickness = 0.012
    return layers, total_thickness

def make_three_layer_crossply():
    # core (0/90/0) thickness 0.0045 m, each lamina 0.0015 m, PZT top+bottom 0.001 m
    t_lam = 0.0015
    z_bot_c0 = -0.00225
    z1 = z_bot_c0 + t_lam        # -0.00075
    z2 = z1 + t_lam              # +0.00075
    z_top_c0 = z2 + t_lam        # +0.00225
    z_bot_PZT_b = z_bot_c0 - 0.001   # -0.00325
    z_top_PZT_b = z_bot_c0           # -0.00225
    z_bot_PZT_t = z_top_c0           #  0.00225
    z_top_PZT_t = z_top_c0 + 0.001   #  0.00325

    layers = [
        {'z_bot': z_bot_PZT_b, 'z_top': z_top_PZT_b, 'Q11': Q11_PZT, 'G': G_PZT,  'alpha': alpha_PZT, 'd31': d31},
        {'z_bot': z_bot_c0,    'z_top': z1,          'Q11': Q11_g,   'G': G13_g,  'alpha': alpha1_g,  'd31': 0.0},   # 0°
        {'z_bot': z1,          'z_top': z2,          'Q11': Q22_g,   'G': G23_g,  'alpha': alpha2_g,  'd31': 0.0},   # 90°
        {'z_bot': z2,          'z_top': z_top_c0,    'Q11': Q11_g,   'G': G13_g,  'alpha': alpha1_g,  'd31': 0.0},   # 0°
        {'z_bot': z_bot_PZT_t, 'z_top': z_top_PZT_t, 'Q11': Q11_PZT, 'G': G_PZT,  'alpha': alpha_PZT, 'd31': d31},
    ]
    total_thickness = 0.0065
    return layers, total_thickness

def make_four_layer_antisym_1piezo():
    # core (0/90/0/90) thickness 0.004 m, each lamina 0.001 m, piezo on top only 0.001 m
    t_lam = 0.001
    z_bot_c0 = -0.002
    z1 = -0.001
    z2 = 0.0
    z3 = 0.001
    z_top_c0 = 0.002
    z_bot_PZT_t = 0.002
    z_top_PZT_t = 0.003

    layers = [
        {'z_bot': z_bot_c0,    'z_top': z1,          'Q11': Q11_g,  'G': G13_g, 'alpha': alpha1_g, 'd31': 0.0},
        {'z_bot': z1,          'z_top': z2,          'Q11': Q22_g,  'G': G23_g, 'alpha': alpha2_g, 'd31': 0.0},
        {'z_bot': z2,          'z_top': z3,          'Q11': Q11_g,  'G': G13_g, 'alpha': alpha1_g, 'd31': 0.0},
        {'z_bot': z3,          'z_top': z_top_c0,    'Q11': Q22_g,  'G': G23_g, 'alpha': alpha2_g, 'd31': 0.0},
        {'z_bot': z_bot_PZT_t, 'z_top': z_top_PZT_t, 'Q11': Q11_PZT,'G': G_PZT, 'alpha': alpha_PZT,'d31': d31},
    ]
    total_thickness = 0.005
    return layers, total_thickness

def make_four_layer_antisym_2piezo():
    # core (0/90/0/90) thickness 0.004 m, each lamina 0.001 m, piezo top+bottom 0.001 m
    t_lam = 0.001
    z_bot_c0 = -0.002
    z1 = -0.001
    z2 = 0.0
    z3 = 0.001
    z_top_c0 = 0.002
    z_bot_PZT_b = -0.003
    z_top_PZT_b = -0.002
    z_bot_PZT_t = 0.002
    z_top_PZT_t = 0.003

    layers = [
        {'z_bot': z_bot_PZT_b, 'z_top': z_top_PZT_b, 'Q11': Q11_PZT,'G': G_PZT, 'alpha': alpha_PZT,'d31': d31},
        {'z_bot': z_bot_c0,    'z_top': z1,          'Q11': Q11_g,  'G': G13_g, 'alpha': alpha1_g, 'd31': 0.0},
        {'z_bot': z1,          'z_top': z2,          'Q11': Q22_g,  'G': G23_g, 'alpha': alpha2_g, 'd31': 0.0},
        {'z_bot': z2,          'z_top': z3,          'Q11': Q11_g,  'G': G13_g, 'alpha': alpha1_g, 'd31': 0.0},
        {'z_bot': z3,          'z_top': z_top_c0,    'Q11': Q22_g,  'G': G23_g, 'alpha': alpha2_g, 'd31': 0.0},
        {'z_bot': z_bot_PZT_t, 'z_top': z_top_PZT_t, 'Q11': Q11_PZT,'G': G_PZT, 'alpha': alpha_PZT,'d31': d31},
    ]
    total_thickness = 0.006
    return layers, total_thickness

def make_thickness_study(t_core):
    # core (0/90/0) thickness t_core, piezo top+bottom 0.001 m
    t_lam = t_core / 3.0
    z_bot_c0 = -t_core/2.0
    z1 = z_bot_c0 + t_lam
    z2 = z1 + t_lam
    z_top_c0 = z_bot_c0 + t_core
    z_bot_PZT_b = z_bot_c0 - 0.001
    z_top_PZT_b = z_bot_c0
    z_bot_PZT_t = z_top_c0
    z_top_PZT_t = z_top_c0 + 0.001

    layers = [
        {'z_bot': z_bot_PZT_b, 'z_top': z_top_PZT_b, 'Q11': Q11_PZT,'G': G_PZT, 'alpha': alpha_PZT,'d31': d31},
        {'z_bot': z_bot_c0,    'z_top': z1,          'Q11': Q11_g,  'G': G13_g, 'alpha': alpha1_g, 'd31': 0.0},
        {'z_bot': z1,          'z_top': z2,          'Q11': Q22_g,  'G': G23_g, 'alpha': alpha2_g, 'd31': 0.0},
        {'z_bot': z2,          'z_top': z_top_c0,    'Q11': Q11_g,  'G': G13_g, 'alpha': alpha1_g, 'd31': 0.0},
        {'z_bot': z_bot_PZT_t, 'z_top': z_top_PZT_t, 'Q11': Q11_PZT,'G': G_PZT, 'alpha': alpha_PZT,'d31': d31},
    ]
    total_thickness = t_core + 0.002
    return layers, total_thickness

# ============================================================
# Collect all rows
# ============================================================
rows = []
all_bcs = ['S-S','C-C','C-S','C-R','S-R']
voltages_all = [0, 200, -200, 500, -500]

# --- 1) aluminium beam ---
layers, thick = make_aluminium()
beam_type = 'aluminium'
layup = 'surface-bonded PZT-5A on aluminium'
for bc in all_bcs:
    for V in voltages_all:
        dt = calc_delta_T(layers, bc, V)
        rows.append([beam_type, layup, bc, V, thick, dt])

# --- 2) three-layer cross-ply ---
layers, thick = make_three_layer_crossply()
beam_type = 'three-layer-cross-ply'
layup = '(0/90/0) with two PZT-5A layers'
for bc in all_bcs:
    for V in voltages_all:
        dt = calc_delta_T(layers, bc, V)
        rows.append([beam_type, layup, bc, V, thick, dt])

# --- 3) antisymmetric 1 piezo ---
layers, thick = make_four_layer_antisym_1piezo()
beam_type = 'four-layer-antisymmetric-1piezo'
layup = '(0/90/0/90) with one PZT-5A layer top'
bcs_part = ['C-C','C-R']
for bc in bcs_part:
    for V in voltages_all:
        dt = calc_delta_T(layers, bc, V)
        rows.append([beam_type, layup, bc, V, thick, dt])

# --- 4) antisymmetric 2 piezo ---
layers, thick = make_four_layer_antisym_2piezo()
beam_type = 'four-layer-antisymmetric-2piezo'
layup = '(0/90/0/90) with two PZT-5A layers'
for bc in bcs_part:
    for V in voltages_all:
        dt = calc_delta_T(layers, bc, V)
        rows.append([beam_type, layup, bc, V, thick, dt])

# --- 5) thickness study ---
thicknesses = [0.003, 0.0045, 0.006]
for t_core in thicknesses:
    layers, thick = make_thickness_study(t_core)
    beam_type = 'thickness-study-three-layer-cross-ply'
    layup = 'thickness study (0/90/0) with two PZT-5A layers'
    for bc in all_bcs:
        V = 0.0
        dt = calc_delta_T(layers, bc, V)
        rows.append([beam_type, layup, bc, V, thick, dt])

# ============================================================
# Write CSV
# ============================================================
outpath = '/app/outputs/critical_buckling_temperatures.csv'
fieldnames = ['beam_type', 'layup_description', 'boundary_condition', 'voltage_V', 'thickness_m', 'delta_T_cr_C']
with open(outpath, 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(fieldnames)
    for r in rows:
        writer.writerow(r)
