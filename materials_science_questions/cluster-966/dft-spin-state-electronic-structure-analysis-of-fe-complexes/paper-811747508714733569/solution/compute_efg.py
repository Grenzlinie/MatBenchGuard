import math, json, csv

a = 4.78
b = 10.22
c = 5.96

# symmetry operations for Pbnm (origin choice 1)
ops = [
    lambda x,y,z: (x, y, z),
    lambda x,y,z: (-x, -y, -z),
    lambda x,y,z: (-x+0.5, y+0.5, z+0.5),
    lambda x,y,z: (x+0.5, -y+0.5, -z+0.5),
]

# asymmetric oxygen coordinates (fractional) from Birle et al. (1968)
asym_O = {
    'O1': (0.0949, 0.2685, 0.25),
    'O2': (0.4524, 0.2770, 0.25),
    'O3': (0.1637, 0.0368, 0.75),
}

def generate_all_O():
    atoms = []
    for name, (x0,y0,z0) in asym_O.items():
        for op in ops:
            x,y,z = op(x0,y0,z0)
            for tx in range(-1,2):
                for ty in range(-1,2):
                    for tz in range(-1,2):
                        xx = x + tx
                        yy = y + ty
                        zz = z + tz
                        atoms.append((name, xx, yy, zz))
    return atoms

all_O = generate_all_O()

def cartesian(frac):
    return (frac[0]*a, frac[1]*b, frac[2]*c)

def distance(frac1, frac2):
    dx = (frac1[0]-frac2[0])*a
    dy = (frac1[1]-frac2[1])*b
    dz = (frac1[2]-frac2[2])*c
    return math.sqrt(dx*dx+dy*dy+dz*dz)

def neighbor_O(center, max_dist=3.0):
    neighbors = []
    for name, x,y,z in all_O:
        d = distance(center, (x,y,z))
        if d < max_dist and d > 0.001:
            neighbors.append((name, (x,y,z), d))
    neighbors.sort(key=lambda t: t[2])
    return neighbors

def vector(center, frac):
    return ((frac[0]-center[0])*a, (frac[1]-center[1])*b, (frac[2]-center[2])*c)

def normalize(v):
    norm = math.sqrt(v[0]**2+v[1]**2+v[2]**2)
    return (v[0]/norm, v[1]/norm, v[2]/norm)

def cross(a,b):
    return (a[1]*b[2]-a[2]*b[1], a[2]*b[0]-a[0]*b[2], a[0]*b[1]-a[1]*b[0])

def dot(a,b):
    return a[0]*b[0]+a[1]*b[1]+a[2]*b[2]

# ------ M1 EFG axes for reference site (origin) ------
v_zz = (-0.1637*a, -0.0368*b, 0.25*c)
Vzz_m1 = normalize(v_zz)
vxx_raw = (0.0949*a, 0.2685*b, 0.25*c)
z = Vzz_m1
dotvz = dot(vxx_raw, z)
vxx_proj = (vxx_raw[0]-dotvz*z[0], vxx_raw[1]-dotvz*z[1], vxx_raw[2]-dotvz*z[2])
Vxx_m1 = normalize(vxx_proj)
Vyy_m1 = normalize(cross(z, Vxx_m1))

# M1 positions and symmetry relations (reflections across 001,100,010 for other sites)
m1_axes = []
# site1: identity
m1_axes.append((Vxx_m1, Vyy_m1, Vzz_m1))
# site2: reflect across 001 (flip z)
m1_axes.append((Vxx_m1, Vyy_m1, (-Vzz_m1[0], -Vzz_m1[1], -Vzz_m1[2])))
# site3: reflect across 100 (flip x)
m1_axes.append(((-Vxx_m1[0], Vxx_m1[1], Vxx_m1[2]), (-Vyy_m1[0], Vyy_m1[1], Vyy_m1[2]), (-Vzz_m1[0], Vzz_m1[1], Vzz_m1[2])))
# site4: reflect across 010 (flip y)
m1_axes.append(((Vxx_m1[0], -Vxx_m1[1], Vxx_m1[2]), (Vyy_m1[0], -Vyy_m1[1], Vyy_m1[2]), (Vzz_m1[0], -Vzz_m1[1], Vzz_m1[2])))

# ------ M2 EFG axes for reference site (0.2775,0.0099,0.25) ------
m2_center = (0.2775, 0.0099, 0.25)
neighbors_m2 = neighbor_O(m2_center, max_dist=3.0)
o3_neighbors = [n for n in neighbors_m2 if n[0]=='O3']
o3c = o3_neighbors[0][1]
o3d = o3_neighbors[1][1]
v_zz_raw = vector(m2_center, o3c)
v_xx_raw = vector(m2_center, o3d)
o1_neighbors = [n for n in neighbors_m2 if n[0]=='O1']
o1 = o1_neighbors[0][1]
v_yy_raw = vector(m2_center, o1)

z2 = normalize(v_zz_raw)
x2 = normalize(v_xx_raw)
y2 = normalize(v_yy_raw)

# orthogonalise to z2
x2_proj = (x2[0]-dot(x2,z2)*z2[0], x2[1]-dot(x2,z2)*z2[1], x2[2]-dot(x2,z2)*z2[2])
Vxx_m2 = normalize(x2_proj)
Vyy_m2 = normalize(cross(z2, Vxx_m2))

# M2 sites and symmetry relations (2-fold rotations about a,b,c)
def rot_c(v): return (-v[0], -v[1], v[2])
def rot_b(v): return (-v[0], v[1], -v[2])
def rot_a(v): return (v[0], -v[1], -v[2])

m2_axes = [
    (Vxx_m2, Vyy_m2, z2),                              # site1: identity
    (rot_c(Vxx_m2), rot_c(Vyy_m2), rot_c(z2)),      # site2: rotate about c
    (rot_b(Vxx_m2), rot_b(Vyy_m2), rot_b(z2)),      # site3: rotate about b
    (rot_a(Vxx_m2), rot_a(Vyy_m2), rot_a(z2)),      # site4: rotate about a
]

# ----- experimental orientations (Table 1) -----
orientations = [
    (90.0, 40.5),
    (90.0, 30.0),
    (90.0, 15.0),
    (90.0, 8.0),
    (90.0, 0.0),
    (78.0, 0.0),
    (66.0, 0.0),
    (57.0, 0.0),
    (52.0, 90.0),
    (45.0, 0.0),
    (38.5, 94.6),
    (38.5, 59.6),
    (35.0, 90.0),
    (30.0, 0.0),
    (18.0, 90.0),
    (15.0, 0.0),
    (0.0, 0.0),
]

eta_m1 = 0.2
eta_m2 = 0.4

def gamma_direction(Theta, Phi):
    Theta = math.radians(Theta)
    Phi   = math.radians(Phi)
    return (math.cos(Theta), math.sin(Theta)*math.cos(Phi), math.sin(Theta)*math.sin(Phi))

def p_values(g, x_axis, y_axis, z_axis, eta):
    dotx = dot(g, x_axis)
    doty = dot(g, y_axis)
    dotz = dot(g, z_axis)
    term = 3*dotz*dotz - 1 + eta * (dotx*dotx - doty*doty)
    fac = 4*math.sqrt((3+eta*eta)/3)
    return fac + term, fac - term

ratios = []
for Theta, Phi in orientations:
    g = gamma_direction(Theta, Phi)
    H = L = 0.0
    for axes in m1_axes:
        pH, pL = p_values(g, *axes, eta_m1)
        H += pH
        L += pL
    for axes in m2_axes:
        pH, pL = p_values(g, *axes, eta_m2)
        H += pH
        L += pL
    AH_AL = H / L if L != 0 else 1.0
    ratios.append((Theta, Phi, round(AH_AL, 4)))

# write theoretical_area_ratios.csv
with open('/app/outputs/theoretical_area_ratios.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['theta', 'phi', 'AH_AL_combined'])
    writer.writerows(ratios)

# build derived_parameters.json
params = {
    "M1": {
        "eta": eta_m1,
        "sign_q": "positive",
        "Vzz_direction": {
            "axis": "O(3b)-M(1)-O(3)",
            "direction_cosines": {
                "cx": round(Vzz_m1[0], 6),
                "cy": round(Vzz_m1[1], 6),
                "cz": round(Vzz_m1[2], 6)
            }
        },
        "Vxx_direction": {
            "axis": "O(1)-M(1)-O(1)",
            "direction_cosines": {
                "cx": round(Vxx_m1[0], 6),
                "cy": round(Vxx_m1[1], 6),
                "cz": round(Vxx_m1[2], 6)
            }
        },
        "Vyy_direction": {
            "axis": "O(2)-M(1)-O(2)",
            "direction_cosines": {
                "cx": round(Vyy_m1[0], 6),
                "cy": round(Vyy_m1[1], 6),
                "cz": round(Vyy_m1[2], 6)
            }
        }
    },
    "M2": {
        "eta": eta_m2,
        "sign_q": "positive",
        "Vzz_direction": {
            "axis": "M(2)-O(3c)",
            "direction_cosines": {
                "cx": round(z2[0], 6),
                "cy": round(z2[1], 6),
                "cz": round(z2[2], 6)
            }
        },
        "Vxx_direction": {
            "axis": "M(2)-O(3d)",
            "direction_cosines": {
                "cx": round(Vxx_m2[0], 6),
                "cy": round(Vxx_m2[1], 6),
                "cz": round(Vxx_m2[2], 6)
            }
        },
        "Vyy_direction": {
            "axis": "M(2)-O(1)",
            "direction_cosines": {
                "cx": round(Vyy_m2[0], 6),
                "cy": round(Vyy_m2[1], 6),
                "cz": round(Vyy_m2[2], 6)
            }
        }
    },
    "site_distribution": {"M1_fraction": 0.5, "M2_fraction": 0.5},
    "total_Fe_per_formula": 0.163,
    "Fe_per_site": {"M1": 0.081, "M2": 0.081}
}

with open('/app/outputs/derived_parameters.json', 'w') as f:
    json.dump(params, f, indent=2)
