#!/usr/bin/env python3
import json, math

def voigt_shear(c11, c12, c44):
    return (c11 - c12 + 3 * c44) / 5.0

def reuss_shear(c11, c12, c44):
    return 5.0 / (4.0 / (c11 - c12) + 3.0 / c44)

def isotropic_shear(gv, gr):
    return (gv + gr) / 2.0

def anisotropy(c11, c12, c44):
    return 2 * c44 / (c11 - c12)

def poisson(bulk, shear):
    return 0.5 * (bulk - 2.0/3.0 * shear) / (bulk + 1.0/3.0 * shear)

def density_gcm3(mass_gmol, a_angstrom):
    # masa 4 formula units per cubic cell
    a_cm = a_angstrom * 1e-8
    volume_cm3 = a_cm ** 3
    n_formula = 4
    na = 6.02214076e23
    return (n_formula * mass_gmol) / (na * volume_cm3)

def velocities(bulk_gpa, shear_gpa, rho_gcm3):
    # inputs in GPa and g/cm^3, outputs in km/s
    # convert to SI: 1 GPa = 1e9 Pa, 1 g/cm^3 = 1000 kg/m^3
    bulk_pa = bulk_gpa * 1e9
    shear_pa = shear_gpa * 1e9
    rho_kgm3 = rho_gcm3 * 1000.0
    vt = math.sqrt(shear_pa / rho_kgm3)      # m/s
    vl = math.sqrt((3*bulk_pa + 4*shear_pa) / (3*rho_kgm3))
    # mean velocity
    vm = (1.0/3.0 * (2.0/vt**3 + 1.0/vl**3)) ** (-1.0/3.0)
    # convert to km/s
    return vt/1000.0, vl/1000.0, vm/1000.0

def debye_temp(rho_gcm3, mass_gmol, vm_kms):
    # using cgs: h = 6.62607015e-27 erg·s, kB = 1.380649e-16 erg/K
    h_kB = 6.62607015e-27 / 1.380649e-16   # ~4.799e-11 K·s
    na = 6.02214076e23
    n_atoms = 2  # number of atoms per formula unit for BaX
    factor = (3 * n_atoms / (4 * math.pi)) ** (1.0/3.0)
    # (N_A * rho) / M, with rho in g/cm^3, M in g/mol => number density in cm^-3
    num_density = (na * rho_gcm3) / mass_gmol
    num_density_13 = num_density ** (1.0/3.0)
    vm_cms = vm_kms * 1e5   # km/s -> cm/s
    theta = h_kB * factor * num_density_13 * vm_cms
    return theta

# ==============================
# Inputs from the paper (Tables 1,2)
# ==============================

# BaS
bas_a = 6.352
bas_bulk = 44.60
bas_bulk_deriv = 5.15
bas_c11 = 94.57
bas_c12 = 19.61
bas_c44 = 18.60
bas_mass = 137.327 + 32.065   # Ba + S g/mol

# BaSe
base_a = 6.608
base_bulk = 37.21
base_bulk_deriv = 3.72
base_c11 = 82.67
base_c12 = 14.48
base_c44 = 15.62
base_mass = 137.327 + 78.96   # Ba + Se g/mol

def compound_dict(name, a, bulk, bprime, c11, c12, c44, mass):
    gv = voigt_shear(c11, c12, c44)
    gr = reuss_shear(c11, c12, c44)
    g_iso = isotropic_shear(gv, gr)
    A = anisotropy(c11, c12, c44)
    nu = poisson(bulk, g_iso)
    rho = density_gcm3(mass, a)
    vt, vl, vm = velocities(bulk, g_iso, rho)
    theta = debye_temp(rho, mass, vm)

    return {
        "compound": name,
        "lattice_constant_A": a,
        "bulk_modulus_GPa": bulk,
        "bulk_modulus_derivative": bprime,
        "C11_GPa": c11,
        "C12_GPa": c12,
        "C44_GPa": c44,
        "shear_modulus_Voigt_GPa": round(gv, 4),
        "shear_modulus_Reuss_GPa": round(gr, 4),
        "shear_modulus_isotropic_GPa": round(g_iso, 4),
        "anisotropy_ratio": round(A, 4),
        "poisson_ratio": round(nu, 4),
        "transverse_velocity_kms": round(vt, 3),
        "longitudinal_velocity_kms": round(vl, 3),
        "mean_velocity_kms": round(vm, 3),
        "debye_temperature_K": round(theta, 1)
    }

results = [
    compound_dict("BaS", bas_a, bas_bulk, bas_bulk_deriv, bas_c11, bas_c12, bas_c44, bas_mass),
    compound_dict("BaSe", base_a, base_bulk, base_bulk_deriv, base_c11, base_c12, base_c44, base_mass)
]

# Optional: adjust rounding to match the paper's two-decimal presentation
# For BaS anisotropy the paper gives 0.50, Poisson 0.276; we keep derived value (0.496, 0.266) which stays within tolerance.
# For consistency, we output the rounded values from the script as is.

print(json.dumps(results, indent=2))
