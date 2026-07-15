import math
import json

# ---------- given inputs ----------
C11 = 105.49     # GPa
C12 = 19.75      # GPa
C44 = 17.29      # GPa
a = 4.48         # Angstrom
M_mol = 136.1703 # g/mol
n = 5            # atoms per formula unit
NA = 6.02214076e23  # mol^-1
h = 6.62607015e-34   # J*s
k = 1.380649e-23     # J/K

# ---------- density ----------
a_cm = a * 1e-8          # Angstrom -> cm
V_cm3 = a_cm ** 3
rho = (n * M_mol) / (NA * V_cm3)   # g/cm^3

# ---------- Voigt/Reuss/Hill moduli ----------
B_V = (C11 + 2 * C12) / 3.0
B_R = B_V   # cubic
B_H = (B_V + B_R) / 2.0

# shear moduli (cubic formulas)
G_V = (C11 - C12 + 3 * C44) / 5.0
G_R = 5 * C44 * (C11 - C12) / (4 * C44 + 3 * (C11 - C12))
G_H = (G_V + G_R) / 2.0

def young(B, G):
    return 9 * B * G / (3 * B + G)

def pugh(B, G):
    return B / G

def poisson(B, G):
    return (3 * B - 2 * G) / (2 * (3 * B + G))

E_V = young(B_V, G_V)
E_R = young(B_R, G_R)
E_H = young(B_H, G_H)

pugh_V = pugh(B_V, G_V)
pugh_R = pugh(B_R, G_R)
pugh_H = pugh(B_H, G_H)

v_H = poisson(B_H, G_H)

# ---------- sound velocities ----------
# convert moduli to Pa, density to kg/m^3
B_Pa = {key: val * 1e9 for key, val in [('V',B_V), ('R',B_R), ('H',B_H)]}
G_Pa = {key: val * 1e9 for key, val in [('V',G_V), ('R',G_R), ('H',G_H)]}
rho_kgm3 = rho * 1000.0

def shear_velocity(G, rho):
    return math.sqrt(G / rho)

def longitudinal_velocity(B, G, rho):
    return math.sqrt((B + 4.0/3.0 * G) / rho)

def average_velocity(vs, vp):
    return ((1/3) * (2/vs**3 + 1/vp**3)) ** (-1/3)

vs = {}
vp = {}
for key in ('V','R','H'):
    vs[key] = shear_velocity(G_Pa[key], rho_kgm3)
    vp[key] = longitudinal_velocity(B_Pa[key], G_Pa[key], rho_kgm3)
vm = {}
for key in ('V','R','H'):
    vm[key] = average_velocity(vs[key], vp[key])

# ---------- Debye temperature ----------
M_kg = M_mol * 1e-3   # kg/mol
factor = (3 * n * NA * rho_kgm3) / (4 * math.pi * M_kg)
factor13 = factor ** (1.0/3.0)
pre = h / k

theta = {}
for key in ('V','R','H'):
    theta[key] = pre * factor13 * vm[key]

# ---------- directional Young's moduli ----------
num_dir = C11**2 + C11 * C12 - 2 * C12**2
E100 = num_dir / (C11 + C12)
E110 = 4 * num_dir * C44 / (C11**2 + C11 * C12 + 2 * C11 * C44 - 2 * C12**2)
E111 = 3 * (C11 + 2 * C12) * C44 / (C11 + 2 * C12 + C44)

# ---------- rounding ----------
def r2(x): return round(x, 2)
def r0(x): return round(x)

result = {
    "density": {
        "value": r2(rho),
        "unit": "g/cm^3"
    },
    "bulk_modulus": {
        "Voigt": r2(B_V),
        "Reuss": r2(B_R),
        "Hill": r2(B_H),
        "unit": "GPa"
    },
    "shear_modulus": {
        "Voigt": r2(G_V),
        "Reuss": r2(G_R),
        "Hill": r2(G_H),
        "unit": "GPa"
    },
    "youngs_modulus": {
        "Voigt": r2(E_V),
        "Reuss": r2(E_R),
        "Hill": r2(E_H),
        "unit": "GPa"
    },
    "pugh_ratio": {
        "Voigt": r2(pugh_V),
        "Reuss": r2(pugh_R),
        "Hill": r2(pugh_H)
    },
    "poisson_ratio": {
        "Hill": r2(v_H)
    },
    "wave_velocities": {
        "shear": {
            "Voigt": r0(vs['V']),
            "Reuss": r0(vs['R']),
            "Hill": r0(vs['H']),
            "unit": "m/s"
        },
        "longitudinal": {
            "Voigt": r0(vp['V']),
            "Reuss": r0(vp['R']),
            "Hill": r0(vp['H']),
            "unit": "m/s"
        },
        "average": {
            "Voigt": r0(vm['V']),
            "Reuss": r0(vm['R']),
            "Hill": r0(vm['H']),
            "unit": "m/s"
        }
    },
    "debye_temperature": {
        "Voigt": r0(theta['V']),
        "Reuss": r0(theta['R']),
        "Hill": r0(theta['H']),
        "unit": "K"
    },
    "directional_youngs_moduli": {
        "E_100": r2(E100),
        "E_110": r2(E110),
        "E_111": r2(E111),
        "unit": "GPa"
    }
}

print(json.dumps(result, indent=2))
