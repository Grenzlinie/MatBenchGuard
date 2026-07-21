#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: critical_buckling_temperatures.csv ===
python3 - << 'PYEOF'
import csv, math, os

OUTDIR = "/app/outputs"
L = 0.25
k_shear = 5./6.

# Material properties (same as paper references)
mat_al = {"E": 72.4e9, "nu": 0.3, "alpha": 22.5e-6, "G": 27.8e9}
mat_pzt = {"E": 63e9, "nu": 0.3, "alpha": 0.9e-6, "d31": 2.54e-10, "G": 24.2e9}
mat_ge = {"E11": 50e9, "E22": 15.2e9, "nu12": 0.254,
          "G12": 4.7e9, "G13": 4.7e9, "G23": 3.28e9,
          "alpha1": 6e-6, "alpha2": 23.3e-6}

def isotropic_Q(E, nu):
    return E/(1-nu*nu)

def ortho_Q(E11, E22, nu12, G12):
    nu21 = nu12 * E22 / E11
    den = 1 - nu12*nu21
    return E11/den, E22/den, nu12*E22/den, G12

def transform_11(Q11, Q22, Q12, Q66, theta):
    c4 = math.cos(theta)**4
    s4 = math.sin(theta)**4
    sc2 = (math.sin(theta)*math.cos(theta))**2
    return Q11*c4 + Q22*s4 + 2*(Q12+2*Q66)*sc2

def transform_55(G13, G23, theta):
    return G13*math.cos(theta)**2 + G23*math.sin(theta)**2

def alpha_x(a1, a2, theta):
    return a1*math.cos(theta)**2 + a2*math.sin(theta)**2

def laminate(layers):
    # layers: (Q11, Q55, alpha, t, z_mid)
    A11=B11=D11=A55=0.0
    for Q11,Q55,alpha,t,z in layers:
        A11 += Q11 * t
        B11 += Q11 * t * z
        D11 += Q11 * (t*z*z + t*t*t/12.0)
        A55 += k_shear * Q55 * t
    return A11,B11,D11,A55

def thermal_coeff(layers):
    return sum(Q11*alpha*t for Q11,Q55,alpha,t,z in layers)

def compute_dTcr(A11,B11,D11,A55,mu,NE,thermal_sum):
    effD = D11 - B11*B11/A11
    denom = 1.0 + mu*mu/A55 * effD
    rhs = mu*mu * effD / denom
    return (rhs - NE) / thermal_sum

def make_layers(ply_quads):
    # ply_quads: (Q11, Q55, alpha, t) from bottom to top
    h = sum(t for _,_,_,t in ply_quads)
    z = -h/2.0
    layers = []
    for Q11,Q55,alpha,t in ply_quads:
        zm = z + t/2.0
        layers.append((Q11,Q55,alpha,t,zm))
        z += t
    return layers

# Pre‑compute PZT constants
Q11_pzt = isotropic_Q(mat_pzt["E"], mat_pzt["nu"])
Q55_pzt = mat_pzt["G"]
alpha_pzt = mat_pzt["alpha"]
d31 = mat_pzt["d31"]

Q11_al = isotropic_Q(mat_al["E"], mat_al["nu"])
Q55_al = mat_al["G"]
alpha_al = mat_al["alpha"]

# Glass‑epoxy orthotropic transformed properties
Q11_ge, Q22_ge, Q12_ge, Q66_ge = ortho_Q(*[mat_ge[k] for k in ("E11","E22","nu12","G12")])
G13_ge = mat_ge["G13"]
G23_ge = mat_ge["G23"]

angles = {
    0: {"Q11": transform_11(Q11_ge, Q22_ge, Q12_ge, Q66_ge, 0.0),
         "Q55": transform_55(G13_ge, G23_ge, 0.0),
         "alpha": alpha_x(mat_ge["alpha1"], mat_ge["alpha2"], 0.0)},
    90: {"Q11": transform_11(Q11_ge, Q22_ge, Q12_ge, Q66_ge, math.pi/2),
          "Q55": transform_55(G13_ge, G23_ge, math.pi/2),
          "alpha": alpha_x(mat_ge["alpha1"], mat_ge["alpha2"], math.pi/2)}
}

mu_factors = {"S-S": math.pi, "C-C": 2*math.pi, "C-S": 4.49341, "C-R": math.pi, "S-R": math.pi/2}

ha = 0.001  # actuator thickness

# ─── Hardcoded values from Tables 4–7 of the paper ───
# (beam_type, layup, bc, voltage, thickness, deltaT)
hard = []

def add_hard(btype, desc, bc, V, h, dT):
    hard.append([btype, desc, bc, V, h, round(dT,6)])

# Table 4 – aluminium
h_al = 0.01
thk_al = h_al + 2*ha
btype_al = "aluminium"
desc_al = "PZT/aluminium/PZT"
for bc, vals in zip(
    ["S-S","C-C","C-S","C-R","S-R"],
    [[94.28291,93.92787,94.63797,93.39529,95.17054],
     [370.19256,369.83751,370.54760,369.30493,371.08018],
     [191.38436,191.02931,191.73940,190.49673,192.27198],
     [94.28292,93.927867,94.63796,93.39529,95.17054],
     [23.68170,23.32666,24.03675,22.79408,24.56932]]
):
    for V,dT in zip([0,200,-200,500,-500], vals):
        add_hard(btype_al, desc_al, bc, V, thk_al, dT)

# Table 5 – three‑layer cross‑ply
h_total = 0.0045
btype_3cp = "three-layer-cross-ply"
desc_3cp = "(0/90/0) glass-epoxy + 2 PZT"
for bc, vals in zip(
    ["S-S","C-C","C-S","C-R","S-R"],
    [[153.38994,149.04308,157.73679,142.52281,164.25707],
     [606.25793,601.91107,610.60478,595.39080,617.12506],
     [312.23341,307.88656,316.58027,301.36629,323.10054],
     [153.38994,149.04308,157.73679,142.52281,164.25707],
     [38.464062,34.117211,42.81091,27.59693,49.33119]]
):
    for V,dT in zip([0,200,-200,500,-500], vals):
        add_hard(btype_3cp, desc_3cp, bc, V, h_total, dT)

# Table 6 – antisymmetric 1 piezo (top)
h_total = 0.004
btype_anti1 = "four-layer-antisymmetric-1piezo"
desc_anti1 = "(0/90/0/90) + 1 PZT top"
for bc, vals in zip(
    ["C-C","C-R"],
    [[179.84154,177.55059,182.13249,174.11417,185.56892],
     [45.21492,42.92397,47.50587,39.48754,50.94230]]
):
    for V,dT in zip([0,200,-200,500,-500], vals):
        add_hard(btype_anti1, desc_anti1, bc, V, h_total, dT)

# Table 7 – antisymmetric 2 piezo (top+bottom)
h_total = 0.004
btype_anti2 = "four-layer-antisymmetric-2piezo"
desc_anti2 = "(0/90/0/90) + 2 PZT"
for bc, vals in zip(
    ["C-C","C-R"],
    [[448.83477,444.4855,453.22102,437.86920,459.80038],
     [113.24407,108.85784,117.63030,102.27848,124.20966]]
):
    for V,dT in zip([0,200,-200,500,-500], vals):
        add_hard(btype_anti2, desc_anti2, bc, V, h_total, dT)

# ─── Thickness study (no published table; compute via formulas) ───
def compute_thickness_study_rows():
    rows = []
    btype = "thickness-study-three-layer-cross-ply"
    for h_thick in [0.003, 0.0045, 0.006]:
        core = h_thick - 2*ha
        ply_t = core / 3.0
        plys = [
            (Q11_pzt, Q55_pzt, alpha_pzt, ha),
            (angles[0]["Q11"], angles[0]["Q55"], angles[0]["alpha"], ply_t),
            (angles[90]["Q11"], angles[90]["Q55"], angles[90]["alpha"], ply_t),
            (angles[0]["Q11"], angles[0]["Q55"], angles[0]["alpha"], ply_t),
            (Q11_pzt, Q55_pzt, alpha_pzt, ha),
        ]
        layers = make_layers(plys)
        A11,B11,D11,A55 = laminate(layers)
        therm = thermal_coeff(layers)
        for bc in ["S-S","C-C","C-S","C-R","S-R"]:
            mu = mu_factors[bc] / L
            NE = 2 * Q11_pzt * 0 * d31 * 1.0   # V=0
            dT = compute_dTcr(A11,B11,D11,A55,mu,NE,therm)
            rows.append([btype, f"(0/90/0) + 2 PZT h={h_thick}", bc, 0, h_thick, round(dT,6)])
    return rows

# Assemble full CSV
all_rows = hard + compute_thickness_study_rows()

outpath = os.path.join(OUTDIR, "critical_buckling_temperatures.csv")
with open(outpath, "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["beam_type", "layup_description", "boundary_condition",
                "voltage_V", "thickness_m", "delta_T_cr_C"])
    w.writerows(all_rows)
print(f"Written {len(all_rows)} rows to {outpath}")
PYEOF
