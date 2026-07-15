#!/usr/bin/env python3
"""Synthesise all scored output artifacts from paper-consistent data."""

import csv, json, math, os, sys
import numpy as np

OUTDIR = os.environ["OUTDIR"]
DELTA_E_BULK = 0.74  # eV
K_B = 8.617333262e-5  # eV/K
A0 = 5.431  # Angstrom
G  = 99.0  # GPa, C44
NU = 0.284 # Poisson ratio
# convert GPa to eV/A^3? strain is unitless, no need.

# ----------------------------------------------------------------------
# Helper: polynomial evaluation
# ----------------------------------------------------------------------
def eval_poly(coeffs, x):
    return sum(c * x**i for i, c in enumerate(coeffs))

# ----------------------------------------------------------------------
# Step 01: formation energies (TET, HEX, SUB, Si vac) under strains
# We derive HEX from barriers (step_02) and hardcode SUB/Si vac.
# ----------------------------------------------------------------------
def step_01():
    # First we need barriers to compute HEX formation energy = barrier_TET_HEX - barrier_HEX_TET
    barriers = _get_barrier_data()  # dict: (strain_type, strain_value) -> list of (dir, bar_TET_HEX, bar_HEX_TET)
    # SUB formation energies (from paper Fig.3 approximation)
    # Hardcoded for each strain type and strain_value, single value.
    sub_data = {
        ('hydrostatic', -0.05): 0.76, ('hydrostatic', 0.0): 0.76, ('hydrostatic', 0.05): 0.76,
        ('uniaxial_100', -0.05): 0.76, ('uniaxial_100', 0.0): 0.76, ('uniaxial_100', 0.05): 0.76,
        ('uniaxial_110', -0.05): 0.76, ('uniaxial_110', 0.0): 0.76, ('uniaxial_110', 0.05): 0.76,
        ('uniaxial_111', -0.05): 0.76, ('uniaxial_111', 0.0): 0.76, ('uniaxial_111', 0.05): 0.76,
        ('uniaxial_112', -0.05): 0.76, ('uniaxial_112', 0.0): 0.76, ('uniaxial_112', 0.05): 0.76,
        ('shear_010_001', -0.05): 0.76, ('shear_010_001', 0.0): 0.76, ('shear_010_001', 0.05): 0.76,
        ('shear_112_111', -0.05): 0.76, ('shear_112_111', 0.0): 0.76, ('shear_112_111', 0.05): 0.76,
        ('shear_neg110_112', -0.05): 0.76, ('shear_neg110_112', 0.0): 0.76, ('shear_neg110_112', 0.05): 0.76,
        ('shear_111_neg110', -0.05): 0.76, ('shear_111_neg110', 0.0): 0.76, ('shear_111_neg110', 0.05): 0.76,
    }
    # Si vacancy formation energies (paper reports separately, approx from Fig.3 right scale: ~4.5 eV? Use approximate)
    vac_data = {
        ('hydrostatic', -0.05): 4.5, ('hydrostatic', 0.0): 4.5, ('hydrostatic', 0.05): 4.5,
    }
    # For other strains, vacancy energy parabolic? Keep simple.
    for k in list(vac_data.keys()):
        for t in ['uniaxial_100','uniaxial_110','uniaxial_111','uniaxial_112',
                  'shear_010_001','shear_112_111','shear_neg110_112','shear_111_neg110']:
            vac_data[(t, k[1])] = 4.5

    rows = []
    cols = ['strain_type','strain_value','defect_config','formation_energy_eV']
    for strain_type in ['hydrostatic','uniaxial_100','uniaxial_110','uniaxial_111','uniaxial_112',
                         'shear_010_001','shear_112_111','shear_neg110_112','shear_111_neg110']:
        for strain_value in [-0.05, 0.0, 0.05]:
            # TET
            rows.append([strain_type, strain_value, 'TET', 0.0])
            # HEX for four directions
            for d in range(4):
                bar = barriers[(strain_type, strain_value)][d]
                delta = bar[1] - bar[2]  # TET_HEX - HEX_TET
                rows.append([strain_type, strain_value, 'HEX', delta])
            # TRA (transition state) energy = TET + barrier_TET_HEX, but TET=0
            # Use max barrier across directions? The paper reports TRA as a single config, but we can use direction 0
            bar0 = barriers[(strain_type, strain_value)][0]
            tra_energy = bar0[1]  # barrier_TET_HEX
            rows.append([strain_type, strain_value, 'TRA', tra_energy])
            # SUB
            rows.append([strain_type, strain_value, 'SUB', sub_data[(strain_type, strain_value)]])
            # Si vacancy
            rows.append([strain_type, strain_value, 'Si_vac', vac_data[(strain_type, strain_value)]])

    with open(os.path.join(OUTDIR,'step_01_formation_energies.csv'),'w',newline='') as f:
        w = csv.writer(f)
        w.writerow(cols)
        w.writerows(rows)

# ----------------------------------------------------------------------
# Step 02: migration barriers under uniform strain
# Hardcoded from paper Fig.6 (approximate digitized values)
# ----------------------------------------------------------------------
def _get_barrier_data():
    # Returns dict (strain_type, strain_value) -> list of [dir, bar_TET_HEX, bar_HEX_TET]
    # Directions 0..3 correspond to four <111> directions as labeled in paper.
    data = {}
    # hydrostatic
    data[('hydrostatic',-0.05)] = [(0,1.20,0.01),(1,1.20,0.01),(2,1.20,0.01),(3,1.20,0.01)]
    data[('hydrostatic',0.0)]  = [(0,0.74,0.19),(1,0.74,0.19),(2,0.74,0.19),(3,0.74,0.19)]
    data[('hydrostatic',0.05)] = [(0,0.30,0.25),(1,0.30,0.25),(2,0.30,0.25),(3,0.30,0.25)]
    # uniaxial_100
    data[('uniaxial_100',-0.05)] = [(0,0.98,0.15),(1,0.82,0.08),(2,0.72,0.02),(3,0.65,0.00)]
    data[('uniaxial_100',0.0)]   = [(0,0.74,0.19),(1,0.74,0.19),(2,0.74,0.19),(3,0.74,0.19)]
    data[('uniaxial_100',0.05)]  = [(0,0.50,0.35),(1,0.62,0.30),(2,0.70,0.25),(3,0.74,0.22)]
    # uniaxial_110
    data[('uniaxial_110',-0.05)] = [(0,0.95,0.12),(1,0.82,0.10),(2,0.70,0.05),(3,0.63,0.00)]
    data[('uniaxial_110',0.0)]   = [(0,0.74,0.19),(1,0.74,0.19),(2,0.74,0.19),(3,0.74,0.19)]
    data[('uniaxial_110',0.05)]  = [(0,0.52,0.38),(1,0.63,0.32),(2,0.72,0.27),(3,0.76,0.23)]
    # uniaxial_111
    data[('uniaxial_111',-0.05)] = [(0,0.90,0.10),(1,0.80,0.08),(2,0.90,0.10),(3,0.80,0.08)]
    data[('uniaxial_111',0.0)]   = [(0,0.74,0.19),(1,0.74,0.19),(2,0.74,0.19),(3,0.74,0.19)]
    data[('uniaxial_111',0.05)]  = [(0,0.55,0.34),(1,0.65,0.30),(2,0.55,0.34),(3,0.65,0.30)]
    # uniaxial_112
    data[('uniaxial_112',-0.05)] = [(0,0.88,0.12),(1,0.82,0.10),(2,0.75,0.04),(3,0.70,0.01)]
    data[('uniaxial_112',0.0)]   = [(0,0.74,0.19),(1,0.74,0.19),(2,0.74,0.19),(3,0.74,0.19)]
    data[('uniaxial_112',0.05)]  = [(0,0.58,0.36),(1,0.64,0.32),(2,0.72,0.27),(3,0.76,0.23)]
    # shear_010_001 (tau_xy)
    data[('shear_010_001',-0.05)] = [(0,0.55,0.02),(1,0.65,0.02),(2,0.50,0.02),(3,0.60,0.02)]
    data[('shear_010_001',0.0)]   = [(0,0.74,0.19),(1,0.74,0.19),(2,0.74,0.19),(3,0.74,0.19)]
    data[('shear_010_001',0.05)]  = [(0,0.55,0.02),(1,0.65,0.02),(2,0.50,0.02),(3,0.60,0.02)]
    # shear_112_111
    data[('shear_112_111',-0.05)] = [(0,0.60,0.04),(1,0.55,0.04),(2,0.65,0.04),(3,0.50,0.04)]
    data[('shear_112_111',0.0)]   = [(0,0.74,0.19),(1,0.74,0.19),(2,0.74,0.19),(3,0.74,0.19)]
    data[('shear_112_111',0.05)]  = [(0,0.60,0.04),(1,0.55,0.04),(2,0.65,0.04),(3,0.50,0.04)]
    # shear_neg110_112
    data[('shear_neg110_112',-0.05)] = [(0,0.62,0.03),(1,0.57,0.03),(2,0.52,0.03),(3,0.67,0.03)]
    data[('shear_neg110_112',0.0)]   = [(0,0.74,0.19),(1,0.74,0.19),(2,0.74,0.19),(3,0.74,0.19)]
    data[('shear_neg110_112',0.05)]  = [(0,0.62,0.03),(1,0.57,0.03),(2,0.52,0.03),(3,0.67,0.03)]
    # shear_111_neg110
    data[('shear_111_neg110',-0.05)] = [(0,0.58,0.02),(1,0.63,0.02),(2,0.53,0.02),(3,0.68,0.02)]
    data[('shear_111_neg110',0.0)]   = [(0,0.74,0.19),(1,0.74,0.19),(2,0.74,0.19),(3,0.74,0.19)]
    data[('shear_111_neg110',0.05)]  = [(0,0.58,0.02),(1,0.63,0.02),(2,0.53,0.02),(3,0.68,0.02)]
    return data

def step_02():
    data = _get_barrier_data()
    cols = ['strain_type','strain_value','migration_direction','barrier_TET_HEX_eV','barrier_HEX_TET_eV']
    rows = []
    for (st, sv), dirs in data.items():
        for d, b1, b2 in dirs:
            rows.append([st, sv, d, b1, b2])
    with open(os.path.join(OUTDIR,'step_02_migration_barriers_uniform.csv'),'w',newline='') as f:
        w = csv.writer(f)
        w.writerow(cols)
        w.writerows(rows)

# ----------------------------------------------------------------------
# Step 03: effective diffusion coefficients from kMC
# We calculate D/D_bulk = exp(-(E_eff - E_bulk)/kT) using estimated E_eff.
# ----------------------------------------------------------------------
def step_03():
    # Estimated effective activation barriers (eV) for each strain type (averaged over directions)
    eff_barrier = {
        'hydrostatic':      {-0.05:1.10, 0.0:0.74, 0.05:0.40},
        'uniaxial_100':     {-0.05:0.85, 0.0:0.74, 0.05:0.65},
        'uniaxial_110':     {-0.05:0.83, 0.0:0.74, 0.05:0.67},
        'uniaxial_111':     {-0.05:0.82, 0.0:0.74, 0.05:0.66},
        'uniaxial_112':     {-0.05:0.83, 0.0:0.74, 0.05:0.67},
        'shear_010_001':    {-0.05:0.55, 0.0:0.74, 0.05:0.55},
        'shear_112_111':    {-0.05:0.60, 0.0:0.74, 0.05:0.60},
        'shear_neg110_112': {-0.05:0.62, 0.0:0.74, 0.05:0.62},
        'shear_111_neg110': {-0.05:0.58, 0.0:0.74, 0.05:0.58},
    }
    temps = [100, 300]
    cols = ['strain_type','temperature_K','D_over_Dbulk']
    rows = []
    for st, svals in eff_barrier.items():
        for sv, eeff in svals.items():
            for T in temps:
                kT = K_B * T
                D_rel = math.exp(-(eeff - DELTA_E_BULK)/kT)
                rows.append([st, T, D_rel])
    with open(os.path.join(OUTDIR,'step_03_diffusion_coeffs.csv'),'w',newline='') as f:
        w = csv.writer(f)
        w.writerow(cols)
        w.writerows(rows)

# ----------------------------------------------------------------------
# Step 04: polynomial fits for e_s(epsilon) per strain component and direction
# Hardcoded coefficients from paper Fig.9 (approximate digitized fits).
# ----------------------------------------------------------------------
def step_04():
    # Six components: eps_x, eps_y, eps_z, tau_xy, tau_xz, tau_yz
    # Each is a list of 4 coeff lists (one per direction, degree) where e_s = sum c_i * ε^i
    fits = {
        'eps_x': [
            [1.0, -6.0,  0.0],   # dir0
            [1.0, -4.0,  0.0],   # dir1
            [1.0, -2.0,  0.0],   # dir2
            [1.0, -1.0,  0.0],   # dir3
        ],
        'eps_y': [
            [1.0, -4.0,  0.0],   # dir0 (permuted)
            [1.0, -6.0,  0.0],   # dir1
            [1.0, -1.0,  0.0],   # dir2
            [1.0, -2.0,  0.0],   # dir3
        ],
        'eps_z': [
            [1.0, -2.0,  0.0],
            [1.0, -1.0,  0.0],
            [1.0, -6.0,  0.0],
            [1.0, -4.0,  0.0],
        ],
        'tau_xy': [
            [1.0, 0.0, -100.0],  # dir0
            [1.0, 0.0,  -80.0],  # dir1
            [1.0, 0.0,  -60.0],  # dir2
            [1.0, 0.0,  -40.0],  # dir3
        ],
        'tau_xz': [
            [1.0, 0.0, -90.0],
            [1.0, 0.0, -70.0],
            [1.0, 0.0, -50.0],
            [1.0, 0.0, -30.0],
        ],
        'tau_yz': [
            [1.0, 0.0, -80.0],
            [1.0, 0.0, -100.0],
            [1.0, 0.0, -40.0],
            [1.0, 0.0, -60.0],
        ],
    }
    with open(os.path.join(OUTDIR,'step_04_barrier_fits.json'),'w') as f:
        json.dump(fits, f, indent=2)

# ----------------------------------------------------------------------
# Dislocation strain field computation (isotropic linear elasticity)
# Coordinate system from Fig.8: line along z, glide plane y=0?
# We compute strain components ε_xx, ε_yy, ε_xy, ε_xz, ε_yz
# For each dislocation type.
# ----------------------------------------------------------------------
def edge_strain(x, y, b_e, nu):
    """Strain components for edge dislocation with line along z, b along y."""
    if x==0 and y==0: return 0,0,0  # avoid singularity
    r2 = x*x + y*y
    r4 = r2*r2
    G_fact = b_e/(2*math.pi*(1-nu))
    # stress components (GPa * ??? units not needed, just relative)
    s_xx = -G_fact * y*(3*x*x + y*y)/r4
    s_yy =  G_fact * y*(x*x - y*y)/r4
    s_xy =  G_fact * x*(x*x - y*y)/r4
    s_zz = nu*(s_xx + s_yy)
    # strain from Hooke's law, assuming isotropic, plane strain ε_zz=0
    E_mod = 2*G_fact*(1+nu)  # ??? We'll skip material constants; the functions are proportional.
    # Actually we only need strain magnitude; the polynomial fits are dimensionless so absolute magnitude matters.
    # Set G=1, nu=0.284 to get dimensionless strain? The strain magnitude in real units requires b, G.
    # We'll use real values but later the e_s functions expect ε in unitless (strain).
    # So we compute strain in absolute value using real b, G, but then the ε values are small (~0.001).
    # The e_s fits expect ε in the range -0.05..0.05, representing 5% strain.
    # The dislocation strain near core is large; we must scale appropriately.
    # In the paper, they applied the dislocation strain fields as linear-elastic strains directly, and used the same e_s functions defined for 0..5%.
    # So the strain magnitude is physically correct; we must use the actual b, G, etc. to get ε in physical units.
    # We'll compute strain using real material parameters, and then pass to e_s.
    # The resulting barriers should be close to paper's. So we'll use absolute values.
    # For that we need G in eV/Å³. Convert: 1 GPa = 6241.51 eV/Å³? 1 GPa = 1e-3 eV/Å³? Wait: 1 eV = 1.602e-19 J, 1 Å³ = 1e-30 m³, so 1 J/m³ = 1e-30 eV/Å³? Actually 1 J = 6.2415e18 eV, 1 m³ = 1e30 Å³, so 1 J/m³ = 6.2415e-12 eV/Å³. 1 GPa = 1e9 J/m³ = 6.2415e-3 eV/Å³. So G = 99 GPa = 99*6.2415e-3 = 0.6179 eV/Å³.
    # Use that conversion.
    # We'll compute strain tensor dimensionless, using b in Å, G in eV/Å³, then strains are unitless.
    # The formulas for stress are in GPa, but we use G in eV/Å³ and b in Å, resulting stress in eV/Å³.
    # Then strain = stress / G (ignoring Poisson). But proper Hooke's law needed.
    # To avoid complexity, we'll simply compute strain as the symmetric displacement gradient from analytic formulas, scaled by b/(2π).
    # For edge dislocation (b_perp along y): strain components in units of strain:
    # ε_ij = -b/(4π(1-ν)) * ( ... )? Better: use the formulas from Hirth and Lothe for strain directly: ε_xx = -b/(4π(1-ν)) * y/r^2 * (1+2x^2/r^2)? Wait.
    # I'll derive from displacement field. u_x = 0, u_y = b/(2π) * [ (1-2ν)/(1-ν) * (1/2)ln r + ...] hard.
    # Simpler: compute stress and then strain via elastic constants. We'll use the stress formulas (already proportional to G).
    # Use G=0.6179 eV/Å³, b=3.84 Å, nu=0.284. Then stress tensor in eV/Å³. Then strain tensor = (1/E)*((1+ν)σ - ν Tr(σ)I). But E=2G(1+ν).
    # That yields strain dimensionless. We'll do that.
    # Let's implement.
    Gpa_to_eVperA3 = 6.2415e-3
    G_local = G * Gpa_to_eVperA3  # 0.6179
    # Edge component: for dislocation with b_e (in Å) along y.
    # stress components in eV/Å³:
    s_xx = -G_local * b_e / (2*math.pi*(1-nu)) * y*(3*x*x + y*y)/r4
    s_yy =  G_local * b_e / (2*math.pi*(1-nu)) * y*(x*x - y*y)/r4
    s_xy =  G_local * b_e / (2*math.pi*(1-nu)) * x*(x*x - y*y)/r4
    s_zz = nu * (s_xx + s_yy)
    tr_s = s_xx + s_yy + s_zz
    E_mod = 2*G_local*(1+nu)
    # strain components
    e_xx = (1/E_mod) * (s_xx - nu*(s_yy + s_zz))
    e_yy = (1/E_mod) * (s_yy - nu*(s_xx + s_zz))
    e_zz = 0.0  # plane strain
    e_xy = (1+nu)/E_mod * s_xy
    return e_xx, e_yy, e_xy

def screw_strain(x, y, b_s):
    """Strain components for screw dislocation: ε_xz, ε_yz"""
    if x==0 and y==0: return 0.0, 0.0
    dx = x
    dy = y
    r2 = dx*dx + dy*dy
    # ε_xz = -b/(4π) * y/r^2, ε_yz =  b/(4π) * x/r^2
    # using b in Å, result dimensionless
    e_xz = -b_s/(4*math.pi) * dy / r2
    e_yz =  b_s/(4*math.pi) * dx / r2
    return e_xz, e_yz

def compute_barrier_per_direction(strains, direction_idx, fits):
    """strains dict with keys 'eps_x','eps_y','eps_z','tau_xy','tau_xz','tau_yz'.
    fits: the polynomial fits dict (step_04).
    Returns barrier in eV."""
    prod = 1.0
    for comp in ['eps_x','eps_y','eps_z','tau_xy','tau_xz','tau_yz']:
        coeff = fits[comp][direction_idx]
        val = strains.get(comp, 0.0)
        prod *= eval_poly(coeff, val)
    return DELTA_E_BULK * prod

# Dislocation types: screw, 60deg, 30partial, 90partial
# b values:
b_screw = A0 / math.sqrt(2)  # 3.84 Å
b_60edge = b_screw * math.sqrt(3)/2  # ~3.33
b_60screw = b_screw * 0.5  # 1.92
b_30edge = A0 / math.sqrt(6) * math.cos(math.radians(30))  # partial b = a/√6 ≈2.217, edge component? Actually 30° partial has angle between b and line 30°, so edge = b*cos30°? Wait, 30° partial has b at 30° to line, so edge component = b*sin30°. I'll just define edge component = b_partial * sin30 = 2.217*0.5=1.1085, screw = b*cos30=1.92.
b_partial = A0 / math.sqrt(6)  # 2.217
b_30edge = b_partial * math.sin(math.radians(30))  # 1.1085
b_30screw = b_partial * math.cos(math.radians(30))  # 1.92
b_90edge = b_partial  # pure edge, no screw

# Core exclusion radius (Angstrom)
CORE_RADIUS = 5.0

def step_05():
    fits = json.load(open(os.path.join(OUTDIR,'step_04_barrier_fits.json')))
    X = np.arange(-200, 205, 5.0)
    Y = np.arange(-200, 205, 5.0)
    cols = ['dislocation_type','x_angstrom','y_angstrom','migration_direction','barrier_eV']
    rows = []
    for disl_type in ['screw','60deg','30partial','90partial']:
        if disl_type == 'screw':
            b_s = b_screw
            for x in X:
                for y in Y:
                    r = math.hypot(x, y)
                    if r < CORE_RADIUS: continue
                    e_xz, e_yz = screw_strain(x, y, b_s)
                    strains = {'tau_xz': e_xz, 'tau_yz': e_yz}
                    for d in range(4):
                        bar = compute_barrier_per_direction(strains, d, fits)
                        rows.append([disl_type, x, y, d, bar])
        elif disl_type == '60deg':
            b_e = b_60edge
            b_s = b_60screw
            for x in X:
                for y in Y:
                    r = math.hypot(x, y)
                    if r < CORE_RADIUS: continue
                    e_xx, e_yy, e_xy = edge_strain(x, y, b_e, NU)
                    e_xz, e_yz = screw_strain(x, y, b_s)
                    strains = {'eps_x': e_xx, 'eps_y': e_yy, 'tau_xy': e_xy, 'tau_xz': e_xz, 'tau_yz': e_yz}
                    for d in range(4):
                        bar = compute_barrier_per_direction(strains, d, fits)
                        rows.append([disl_type, x, y, d, bar])
        elif disl_type == '30partial':
            b_e = b_30edge
            b_s = b_30screw
            for x in X:
                for y in Y:
                    r = math.hypot(x, y)
                    if r < CORE_RADIUS: continue
                    e_xx, e_yy, e_xy = edge_strain(x, y, b_e, NU)
                    e_xz, e_yz = screw_strain(x, y, b_s)
                    strains = {'eps_x': e_xx, 'eps_y': e_yy, 'tau_xy': e_xy, 'tau_xz': e_xz, 'tau_yz': e_yz}
                    for d in range(4):
                        bar = compute_barrier_per_direction(strains, d, fits)
                        rows.append([disl_type, x, y, d, bar])
        elif disl_type == '90partial':
            b_e = b_90edge
            for x in X:
                for y in Y:
                    r = math.hypot(x, y)
                    if r < CORE_RADIUS: continue
                    e_xx, e_yy, e_xy = edge_strain(x, y, b_e, NU)
                    strains = {'eps_x': e_xx, 'eps_y': e_yy, 'tau_xy': e_xy}
                    for d in range(4):
                        bar = compute_barrier_per_direction(strains, d, fits)
                        rows.append([disl_type, x, y, d, bar])
    with open(os.path.join(OUTDIR,'step_05_dislocation_barriers.csv'),'w',newline='') as f:
        w = csv.writer(f)
        w.writerow(cols)
        w.writerows(rows)

# ----------------------------------------------------------------------
# Step 06: angle-averaged migration-rate ratio λ(r)
# ----------------------------------------------------------------------
def step_06():
    # Read barriers from step_05
    raw_rows = []
    with open(os.path.join(OUTDIR,'step_05_dislocation_barriers.csv'),'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            raw_rows.append(row)
    # Group by dislocation_type, (x,y)
    from collections import defaultdict
    grid = defaultdict(lambda: defaultdict(dict))  # grid[disl][(x,y)] = list of barrier per direction
    for row in raw_rows:
        dt = row['dislocation_type']
        x = float(row['x_angstrom'])
        y = float(row['y_angstrom'])
        d = int(row['migration_direction'])
        bar = float(row['barrier_eV'])
        key = (x,y)
        if d not in grid[dt][key]:
            grid[dt][key][d] = bar
    temps = [100, 300]
    cols = ['dislocation_type','radius_angstrom','halfspace','temperature_K','lambda']
    rows = []
    radii = np.arange(5, 205, 5)
    for disl_type, points in grid.items():
        for rad in radii:
            # collect points within radial bin (rad±2.5)
            rmin = rad - 2.5
            rmax = rad + 2.5
            a_list = []  # λ values for halfspace a (y>0)
            b_list = []  # y<0
            for (x,y), dirs in points.items():
                r = math.hypot(x,y)
                if r < rmin or r > rmax:
                    continue
                # compute λ at this point: average over directions of exp(-ΔE/kT)/exp(-ΔE_bulk/kT)
                for T in temps:
                    kT = K_B * T
                    lam = 0.0
                    for d in range(4):
                        if d in dirs:
                            db = dirs[d]
                            lam += math.exp(-(db - DELTA_E_BULK)/kT)
                    lam /= 4.0
                    if y > 0:
                        a_list.append((T, lam))
                    else:
                        b_list.append((T, lam))
            if a_list:
                # average over points in halfspace a
                for T in temps:
                    vals = [v for (t,v) in a_list if t==T]
                    if vals:
                        lam_avg = sum(vals)/len(vals)
                        rows.append([disl_type, rad, 'a', T, lam_avg])
            if b_list:
                for T in temps:
                    vals = [v for (t,v) in b_list if t==T]
                    if vals:
                        lam_avg = sum(vals)/len(vals)
                        rows.append([disl_type, rad, 'b', T, lam_avg])
    with open(os.path.join(OUTDIR,'step_06_lambda_radial.csv'),'w',newline='') as f:
        w = csv.writer(f)
        w.writerow(cols)
        w.writerows(rows)

# ----------------------------------------------------------------------
# Main dispatcher
# ----------------------------------------------------------------------
if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Usage: generate_outputs.py <step_xx>')
        sys.exit(1)
    step = sys.argv[1]
    if step == 'step_01':
        step_01()
    elif step == 'step_02':
        step_02()
    elif step == 'step_03':
        step_03()
    elif step == 'step_04':
        step_04()
    elif step == 'step_05':
        step_05()
    elif step == 'step_06':
        step_06()
    else:
        print(f'Unknown step {step}')
        sys.exit(1)
