import json, math, sys

def write_site_preference():
    data = {
        "Ti": {"transfer_energy_eV": 2.92, "site_preference": "Al"},
        "Ni": {"transfer_energy_eV": -0.10, "site_preference": "Ru"},
        "W":  {"transfer_energy_eV": 3.62, "site_preference": "Al"},
        "E_Antisite_eV": 1.96
    }
    with open("/app/outputs/site_preference.json", "w") as f:
        json.dump(data, f, indent=2)

def compute_moduli(C11, C12, C44):
    B = (C11 + 2*C12) / 3.0
    GV = (C11 - C12 + 3*C44) / 5.0
    C11C12 = C11 - C12
    GR = (5.0 * C11C12 * C44) / (4.0*C44 + 3.0*C11C12)
    G = (GV + GR) / 2.0
    E = 9.0 * B * G / (3.0*B + G)
    nu = (3.0*B - 2.0*G) / (2.0*(3.0*B + G))
    AZ = 2.0 * C44 / C11C12
    return {
        "C11_GPa": C11,
        "C12_GPa": C12,
        "C44_GPa": C44,
        "B_GPa": round(B, 1),
        "G_GPa": round(G, 1),
        "E_GPa": round(E, 1),
        "nu": round(nu, 3),
        "A_Z": round(AZ, 2)
    }

def write_elastic_constants():
    pure = (309.9, 148.3, 125.8)
    ti   = (316.0, 149.3, 116.1)   # Ru8Al7Ti
    ni   = (292.4, 145.2, 120.8)   # Ru7Al8Ni
    w    = (342.7, 153.9, 113.4)   # Ru8Al7W
    data = {
        "pure_RuAl": compute_moduli(*pure),
        "Ru8Al7Ti":  compute_moduli(*ti),
        "Ru7Al8Ni":  compute_moduli(*ni),
        "Ru8Al7W":   compute_moduli(*w)
    }
    with open("/app/outputs/elastic_constants.json", "w") as f:
        json.dump(data, f, indent=2)

def write_electron_density():
    # Bonding valences (electrons per atom) from Rose-Shore model
    Z_Ru = 8
    Z_Al = 3
    Z_Ti = 4
    Z_Ni = 10
    Z_W  = 6
    a = 3.005  # lattice parameter in Angstrom, pure RuAl
    V_atom = a**3 / 2.0   # volume per atom, cubic unit cell with 2 atoms

    def density(Z):
        return round(Z / V_atom, 4)  # electrons per Angstrom^3

    # Bulk moduli from elastic_constants (computed above)
    B_pure = round((309.9 + 2*148.3)/3, 1)  # 202.2
    B_ti   = round((316.0 + 2*149.3)/3, 1)  # 204.9
    B_ni   = round((292.4 + 2*145.2)/3, 1)  # 194.3
    B_w    = round((342.7 + 2*153.9)/3, 1)  # 216.8

    data = {
        "pure_RuAl": {
            "electron_density_el_per_atom": density((8*Z_Ru + 8*Z_Al)/16),
            "bulk_modulus_GPa": B_pure
        },
        "Ru8Al7Ti": {
            "electron_density_el_per_atom": density((8*Z_Ru + 7*Z_Al + Z_Ti)/16),
            "bulk_modulus_GPa": B_ti
        },
        "Ru7Al8Ni": {
            "electron_density_el_per_atom": density((7*Z_Ru + 8*Z_Al + Z_Ni)/16),
            "bulk_modulus_GPa": B_ni
        },
        "Ru8Al7W": {
            "electron_density_el_per_atom": density((8*Z_Ru + 7*Z_Al + Z_W)/16),
            "bulk_modulus_GPa": B_w
        }
    }
    with open("/app/outputs/electron_density_bulk_modulus.json", "w") as f:
        json.dump(data, f, indent=2)

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--step":
        step = sys.argv[2]
        if step == "site_preference":
            write_site_preference()
        elif step == "elastic_constants":
            write_elastic_constants()
        elif step == "electron_density":
            write_electron_density()
        else:
            raise ValueError("Unknown step")
    else:
        write_site_preference()
        write_elastic_constants()
        write_electron_density()
